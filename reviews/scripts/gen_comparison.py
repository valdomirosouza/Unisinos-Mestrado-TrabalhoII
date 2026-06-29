#!/usr/bin/env python3
"""Compare the two evaluator sets (Claude vs ChatGPT).

Reads:  reviews/resultados-consolidados.csv  (Claude)
        reviews/ChatGPT/P*_avaliacao_RSL.md   (ChatGPT)
Writes: reviews/comparacao-avaliadores.csv
        reviews/charts/chart-comparacao.svg
Run:    python3 reviews/scripts/gen_comparison.py
"""
import re, os, glob, csv, html, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEWS = os.path.dirname(HERE)
CHATDIR = os.path.join(REVIEWS, "ChatGPT")
CLAUDE_CSV = os.path.join(REVIEWS, "resultados-consolidados.csv")
OUT_CSV = os.path.join(REVIEWS, "comparacao-avaliadores.csv")
OUT_SVG = os.path.join(REVIEWS, "charts", "chart-comparacao.svg")

def num(s): return float(s.replace(",", ".")) if s else None

def extract_gpt(path):
    t = open(path, encoding="utf-8").read()
    srq = re.search(r"SCORE_RQ\D{0,8}(\d,\d)\s*/\s*5", t)
    rq = re.search(r"([TPN])\s*\+\s*([TPN])\s*\+\s*([TPN])\s*\+\s*([TPN])\s*\+\s*([TPN])", t)
    qa = re.search(r"(\d,\d)\s*/\s*4,0\s*\*{0,2}\s*\|\s*\*{0,2}\s*(Alta|M[ée]dia|Baixa)", t)
    rec = re.search(r"###\s*Recomenda[çc][ãa]o\s*\n+\**\s*([^\n*]+?)\.?\**\s*\n", t)
    return dict(srq=num(srq.group(1)) if srq else None,
                rq="".join(rq.groups()) if rq else None,
                sqa=num(qa.group(1)) if qa else None,
                banda=(qa.group(2).replace("é", "e") if qa else ""),
                rec=rec.group(1).strip() if rec else "")

def decision(s):
    return "INCLUIR" if s.lower().startswith("incluir") else "EXCLUIR"

gpt = {re.match(r"P\d+", os.path.basename(f)).group(): extract_gpt(f)
       for f in glob.glob(f"{CHATDIR}/P*.md")}
claude = {r["ID"]: r for r in csv.DictReader(open(CLAUDE_CSV, encoding="utf-8"))}
ids = [f"P{n}" for n in range(20, 41) if n != 36]

# ---- comparison CSV ----
cols = ["ID", "Claude_SCORE_RQ", "GPT_SCORE_RQ", "d_RQ",
        "Claude_SCORE_QA", "GPT_SCORE_QA", "d_QA",
        "Claude_Banda", "GPT_Banda", "Banda_igual",
        "Claude_decisao", "GPT_decisao", "Decisao_igual",
        "Claude_recomendacao", "GPT_recomendacao"]
rows = []
for pid in ids:
    c, g = claude[pid], gpt[pid]
    crq = None if c["SCORE_RQ"] == "NA" else float(c["SCORE_RQ"])
    cqa = None if c["SCORE_QA"] == "NA" else float(c["SCORE_QA"])
    cd, gd = decision(c["Recomendacao"]), decision(g["rec"])
    rows.append([pid, c["SCORE_RQ"], g["srq"], None if crq is None else round(g["srq"]-crq, 1),
                 c["SCORE_QA"], g["sqa"], None if cqa is None else round(g["sqa"]-cqa, 1),
                 c["Banda"], g["banda"], "sim" if c["Banda"].replace("é","e")==g["banda"] and c["Banda"]!="NA" else ("NA" if c["Banda"]=="NA" else "nao"),
                 cd, gd, "sim" if cd == gd else "nao",
                 c["Recomendacao"], g["rec"]])
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(cols); w.writerows(rows)
print("wrote", OUT_CSV)

# ---- metrics ----
n = len(ids)
dec_agree = sum(1 for r in rows if r[12] == "sim")
po = dec_agree / n
both_in = sum(1 for r in rows if r[12]=="sim" and r[10]=="INCLUIR")
both_ex = sum(1 for r in rows if r[12]=="sim" and r[10]=="EXCLUIR")
cl_in_g_ex = sum(1 for r in rows if r[10]=="INCLUIR" and r[11]=="EXCLUIR")
cl_ex_g_in = sum(1 for r in rows if r[10]=="EXCLUIR" and r[11]=="INCLUIR")
cl_in, cl_ex = both_in+cl_in_g_ex, both_ex+cl_ex_g_in
g_in, g_ex = both_in+cl_ex_g_in, both_ex+cl_in_g_ex
pe = (cl_in*g_in + cl_ex*g_ex)/(n*n)
kappa = (po-pe)/(1-pe)
rqm = []
for k in range(5):
    tot = mat = 0
    for pid in ids:
        c, g = claude[pid], gpt[pid]
        if c["RQ1"] != "NA" and g["rq"]:
            tot += 1; mat += (c[f"RQ{k+1}"] == g["rq"][k])
    rqm.append((mat, tot))
print(f"decisao: {dec_agree}/{n} ({po:.0%}) kappa={kappa:.3f}; RQ match={[f'{m}/{t}' for m,t in rqm]}")

# ---- SVG chart ----
G, GR = "#2e7d32", "#c0c4cc"
FONT = 'font-family="Segoe UI, Helvetica, Arial, sans-serif"'
def esc(s): return html.escape(str(s))
w, hgt = 760, 430
s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{hgt}" viewBox="0 0 {w} {hgt}" {FONT}>'
     f'<rect width="{w}" height="{hgt}" fill="#fff"/>'
     f'<text x="{w/2}" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="#1a1a1a">'
     f'Concordância entre avaliadores — Claude × ChatGPT (20 estudos)</text>')
# left: per-RQ + decision agreement bars
left, top, trackw, rowh = 150, 64, 360, 34
bars = [("Decisão (Incluir/Excluir)", dec_agree, n),
        ("Banda de qualidade", sum(1 for r in rows if r[9]=="sim"), sum(1 for r in rows if r[9]!="NA"))]
bars += [(f"RQ{k+1}", rqm[k][0], rqm[k][1]) for k in range(5)]
s += f'<text x="{left}" y="{top-12}" font-size="11" font-weight="700" fill="#555">% de acordo</text>'
for i,(lab,m,t) in enumerate(bars):
    y = top + i*rowh; frac = m/t
    s += (f'<text x="{left-8}" y="{y+15}" text-anchor="end" font-size="11" fill="#222">{esc(lab)}</text>'
          f'<rect x="{left}" y="{y+4}" width="{trackw}" height="18" rx="3" fill="#eef0f2"/>'
          f'<rect x="{left}" y="{y+4}" width="{trackw*frac:.1f}" height="18" rx="3" fill="{G if frac>=0.9 else ("#f9a825" if frac>=0.7 else "#ef6c00")}"/>'
          f'<text x="{left+trackw+8}" y="{y+17}" font-size="11" font-weight="700" fill="#333">{frac:.0%} ({m}/{t})</text>')
# footer metric
s += (f'<text x="{left}" y="{top+len(bars)*rowh+20}" font-size="11" fill="#555">'
      f'Cohen’s κ (decisão) = {kappa:.2f} · erro abs. médio SCORE_RQ = '
      f'{st.mean([abs(r[3]) for r in rows if r[3] is not None]):.2f} · '
      f'SCORE_QA = {st.mean([abs(r[6]) for r in rows if r[6] is not None]):.2f}</text>')
s += "</svg>"
open(OUT_SVG, "w", encoding="utf-8").write(s)
print("wrote", OUT_SVG)
