#!/usr/bin/env python3
"""Monta o pacote de replicação da RSL (Zenodo-ready).

Lê replication/manifest.txt (whitelist), copia os artefatos para
dist/<nome>/, injeta replication/package-README.md como README.md do
pacote, gera MANIFEST.csv (caminho, bytes, sha256), compacta em .zip e
publica o SHA-256 do arquivo final.

Política de segurança (falha o build se violada):
  - nada de docs/ (textos integrais com copyright) nem de arquivos .pdf
    oriundos de docs/; PDFs próprios (ex.: reviews/relatorio-sintese.pdf)
    são permitidos e listados no relatório final para conferência;
  - nenhum arquivo de credencial (.scopus_key, *.key, .env*) e nenhuma
    ocorrência do conteúdo de .scopus_key dentro dos arquivos copiados.

Uso: python3 scripts/build-replication-package.py [--version v1.0.0]
"""

import argparse
import csv
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "replication" / "manifest.txt"
PKG_README = ROOT / "replication" / "package-README.md"
DIST = ROOT / "dist"
BASENAME = "agentic-ir-slr-replication"

SKIP_NAMES = {".DS_Store", "Thumbs.db"}  # lixo de SO: pulado em silêncio
DENY_NAMES = {".scopus_key", ".env"}
DENY_SUFFIXES = {".key"}
DENY_DIR_PARTS = {".git", ".github", ".claude", ".serena", ".agents", "__pycache__", "docs"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_manifest() -> list[Path]:
    entries = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = ROOT / line
        if not p.exists():
            sys.exit(f"ERRO: entrada do manifesto não existe: {line}")
        entries.append(p)
    return entries


def iter_files(entry: Path):
    if entry.is_file():
        yield entry
        return
    for p in sorted(entry.rglob("*")):
        if p.is_file():
            yield p


def denied(path: Path) -> str | None:
    rel = path.relative_to(ROOT)
    if path.name in DENY_NAMES:
        return "credencial/artefato local"
    if path.suffix in DENY_SUFFIXES:
        return "credencial"
    if any(part in DENY_DIR_PARTS for part in rel.parts[:-1]):
        return f"diretório vetado ({rel.parts[0]})"
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="v1.0.0")
    args = ap.parse_args()

    secret = (ROOT / ".scopus_key").read_bytes().strip() if (ROOT / ".scopus_key").exists() else b""

    pkg_name = f"{BASENAME}-{args.version}"
    pkg_dir = DIST / pkg_name
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir(parents=True)

    rows, pdfs, total = [], [], 0
    for entry in read_manifest():
        for src in iter_files(entry):
            if src.name in SKIP_NAMES:
                continue
            reason = denied(src)
            if reason:
                sys.exit(f"ERRO: {src.relative_to(ROOT)} vetado ({reason}) — remova do manifesto.")
            data = src.read_bytes()
            if secret and secret in data:
                sys.exit(f"ERRO: vazamento de credencial detectado em {src.relative_to(ROOT)}.")
            rel = src.relative_to(ROOT)
            dst = pkg_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            rows.append((str(rel), len(data), sha256(src)))
            total += len(data)
            if src.suffix.lower() == ".pdf":
                pdfs.append(str(rel))

    shutil.copy2(PKG_README, pkg_dir / "README.md")
    rows.append(("README.md", PKG_README.stat().st_size, sha256(PKG_README)))

    with open(pkg_dir / "MANIFEST.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["path", "bytes", "sha256"])
        w.writerows(sorted(rows))

    zip_path = DIST / f"{pkg_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(pkg_dir.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(DIST))

    print(f"Pacote:   {pkg_dir.relative_to(ROOT)}  ({len(rows)} arquivos, {total / 1e6:.1f} MB)")
    print(f"Zip:      {zip_path.relative_to(ROOT)}  ({zip_path.stat().st_size / 1e6:.1f} MB)")
    print(f"SHA-256:  {sha256(zip_path)}")
    if pdfs:
        print("PDFs incluídos (conferir se são de autoria própria):")
        for p in pdfs:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
