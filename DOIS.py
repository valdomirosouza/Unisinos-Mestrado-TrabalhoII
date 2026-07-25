#!/usr/bin/env python3
"""
doi_refs.py — Extrai a lista de referencias citadas por um artigo (a partir do
seu DOI) e o DOI de cada referencia, consultando multiplas fontes e unindo os
resultados com registro de proveniencia.

Fontes: Crossref, OpenAlex, Semantic Scholar, OpenCitations (COCI).

Uso:
    python doi_refs.py 10.1016/j.infsof.2008.09.009 --email voce@dominio.br
    python doi_refs.py --input dois.txt --email voce@dominio.br --out refs.csv

Requisitos:
    pip install requests
"""

import argparse
import csv
import json
import re
import sys
import time
from collections import defaultdict

import requests

TIMEOUT = 30
SLEEP = 0.34  # ~3 req/s, educado com todas as APIs


# --------------------------------------------------------------------------
# utilitarios
# --------------------------------------------------------------------------

def norm_doi(doi):
    """Normaliza um DOI: minusculas, sem prefixo de URL, sem espacos."""
    if not doi:
        return None
    d = str(doi).strip().lower()
    d = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d)
    d = re.sub(r'^doi:\s*', '', d)
    return d if d.startswith('10.') else None


def get_json(url, params=None, headers=None):
    """GET com tratamento de erro; retorna None em falha."""
    try:
        r = requests.get(url, params=params, headers=headers or {}, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        if r.status_code == 429:
            time.sleep(5)
            r = requests.get(url, params=params, headers=headers or {}, timeout=TIMEOUT)
            if r.status_code == 200:
                return r.json()
        return None
    except (requests.RequestException, ValueError):
        return None


# --------------------------------------------------------------------------
# fontes
# --------------------------------------------------------------------------

def from_crossref(doi, email):
    """Le a lista `reference` depositada pelo editor no Crossref."""
    data = get_json(f"https://api.crossref.org/works/{doi}",
                    params={"mailto": email})
    if not data:
        return [], {}
    msg = data.get("message", {})
    meta = {
        "titulo": (msg.get("title") or [""])[0],
        "ano": (msg.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "veiculo": (msg.get("container-title") or [""])[0],
        "refs_declaradas": msg.get("reference-count"),
    }
    refs = []
    for ref in msg.get("reference", []) or []:
        refs.append({
            "doi": norm_doi(ref.get("DOI")),
            "titulo": ref.get("article-title") or ref.get("volume-title") or "",
            "ano": ref.get("year"),
            "bruto": ref.get("unstructured", ""),
        })
    return refs, meta


def from_openalex(doi, email):
    """Le `referenced_works` e resolve os IDs em lote (ate 50 por chamada)."""
    data = get_json(f"https://api.openalex.org/works/doi:{doi}",
                    params={"mailto": email})
    if not data:
        return [], {}
    meta = {
        "titulo": data.get("title") or "",
        "ano": data.get("publication_year"),
        "veiculo": ((data.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
        "citado_por": data.get("cited_by_count"),
        "refs_declaradas": len(data.get("referenced_works") or []),
    }

    ids = [w.rsplit("/", 1)[-1] for w in (data.get("referenced_works") or [])]
    refs = []
    for i in range(0, len(ids), 50):
        lote = "|".join(ids[i:i + 50])
        page = get_json("https://api.openalex.org/works",
                        params={"filter": f"openalex_id:{lote}",
                                "per-page": 50,
                                "select": "id,doi,title,publication_year",
                                "mailto": email})
        time.sleep(SLEEP)
        if not page:
            continue
        for w in page.get("results", []):
            refs.append({
                "doi": norm_doi(w.get("doi")),
                "titulo": w.get("title") or "",
                "ano": w.get("publication_year"),
                "bruto": "",
            })
    return refs, meta


def from_semantic_scholar(doi, api_key=None):
    """Le as referencias do Semantic Scholar (boa cobertura de preprints)."""
    headers = {"x-api-key": api_key} if api_key else {}
    refs, offset = [], 0
    while True:
        page = get_json(
            f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/references",
            params={"fields": "externalIds,title,year", "limit": 100, "offset": offset},
            headers=headers)
        time.sleep(SLEEP)
        if not page or not page.get("data"):
            break
        for item in page["data"]:
            cited = item.get("citedPaper") or {}
            ext = cited.get("externalIds") or {}
            refs.append({
                "doi": norm_doi(ext.get("DOI")),
                "titulo": cited.get("title") or "",
                "ano": cited.get("year"),
                "bruto": "",
            })
        if "next" not in page:
            break
        offset = page["next"]
    return refs, {}


def from_opencitations(doi):
    """Indice COCI: relacoes DOI-a-DOI, util como terceiro voto."""
    data = get_json(f"https://opencitations.net/index/api/v1/references/{doi}")
    if not data:
        return [], {}
    return [{"doi": norm_doi(r.get("cited")), "titulo": "", "ano": "", "bruto": ""}
            for r in data], {}


# --------------------------------------------------------------------------
# uniao com proveniencia
# --------------------------------------------------------------------------

def coletar(doi, email, api_key=None, fontes=None):
    fontes = fontes or ["crossref", "openalex", "s2", "opencitations"]
    resultados, meta = {}, {}

    if "crossref" in fontes:
        resultados["crossref"], m = from_crossref(doi, email)
        meta.setdefault("crossref", m)
        time.sleep(SLEEP)
    if "openalex" in fontes:
        resultados["openalex"], m = from_openalex(doi, email)
        meta.setdefault("openalex", m)
        time.sleep(SLEEP)
    if "s2" in fontes:
        resultados["s2"], _ = from_semantic_scholar(doi, api_key)
    if "opencitations" in fontes:
        resultados["opencitations"], _ = from_opencitations(doi)
        time.sleep(SLEEP)

    # uniao por DOI normalizado; sem DOI -> mantem separado pelo titulo
    uniao = {}
    sem_doi = []
    for fonte, refs in resultados.items():
        for r in refs:
            if r["doi"]:
                item = uniao.setdefault(r["doi"], {
                    "doi": r["doi"], "titulo": r["titulo"],
                    "ano": r["ano"], "fontes": set()})
                item["fontes"].add(fonte)
                if not item["titulo"] and r["titulo"]:
                    item["titulo"] = r["titulo"]
                if not item["ano"] and r["ano"]:
                    item["ano"] = r["ano"]
            else:
                sem_doi.append({**r, "fonte": fonte})

    contagens = {f: len(v) for f, v in resultados.items()}
    return uniao, sem_doi, contagens, meta


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Extrai referencias e DOIs a partir de um DOI.")
    p.add_argument("doi", nargs="?", help="DOI do artigo de origem")
    p.add_argument("--input", help="arquivo texto com um DOI por linha")
    p.add_argument("--email", required=True, help="seu e-mail (polite pool)")
    p.add_argument("--api-key", help="chave Semantic Scholar (opcional)")
    p.add_argument("--out", default="referencias.csv", help="CSV de saida")
    p.add_argument("--json-out", help="JSON de saida (opcional)")
    p.add_argument("--fontes", default="crossref,openalex,s2,opencitations",
                   help="lista separada por virgula")
    args = p.parse_args()

    if args.input:
        with open(args.input) as fh:
            dois = [norm_doi(l) for l in fh if norm_doi(l)]
    elif args.doi:
        dois = [norm_doi(args.doi)]
    else:
        p.error("informe um DOI ou --input")

    fontes = [f.strip() for f in args.fontes.split(",")]
    linhas, dump = [], {}

    for origem in dois:
        print(f"\n>>> {origem}", file=sys.stderr)
        uniao, sem_doi, contagens, meta = coletar(origem, args.email, args.api_key, fontes)

        for f, n in contagens.items():
            print(f"    {f:<15} {n:>4} refs", file=sys.stderr)
        print(f"    {'UNIAO (com DOI)':<15} {len(uniao):>4} refs", file=sys.stderr)
        print(f"    {'sem DOI':<15} {len(sem_doi):>4} entradas", file=sys.stderr)

        for r in sorted(uniao.values(), key=lambda x: int(x["ano"]) if str(x["ano"] or "").isdigit() else 0):
            linhas.append({
                "doi_origem": origem,
                "doi_referencia": r["doi"],
                "titulo_referencia": r["titulo"],
                "ano_referencia": r["ano"],
                "fontes": ";".join(sorted(r["fontes"])),
                "n_fontes": len(r["fontes"]),
            })
        for r in sem_doi:
            linhas.append({
                "doi_origem": origem,
                "doi_referencia": "",
                "titulo_referencia": r["titulo"] or r["bruto"][:200],
                "ano_referencia": r["ano"],
                "fontes": r["fonte"],
                "n_fontes": 1,
            })

        dump[origem] = {"meta": meta, "contagens": contagens,
                        "uniao": [{**v, "fontes": sorted(v["fontes"])} for v in uniao.values()],
                        "sem_doi": sem_doi}

    campos = ["doi_origem", "doi_referencia", "titulo_referencia",
              "ano_referencia", "fontes", "n_fontes"]
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)
    print(f"\nCSV: {args.out} ({len(linhas)} linhas)", file=sys.stderr)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(dump, fh, ensure_ascii=False, indent=2)
        print(f"JSON: {args.json_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
