#!/usr/bin/env python3
"""Generate SVG charts from the consolidated RSL results CSV (no deps).

Run from anywhere:  python3 reviews/scripts/gen_charts.py
Reads:  reviews/resultados-consolidados.csv
Writes: reviews/charts/*.svg
"""
import csv, os, html

HERE = os.path.dirname(os.path.abspath(__file__))   # reviews/scripts
REVIEWS = os.path.dirname(HERE)                       # reviews
CSV = os.path.join(REVIEWS, "resultados-consolidados.csv")
OUT = os.path.join(REVIEWS, "charts")
os.makedirs(OUT, exist_ok=True)

rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
elig = [r for r in rows if r["SCORE_RQ"] != "NA"]

# palette
G, A, R = "#2e7d32", "#f9a825", "#c62828"          # full / partial / none
GREY = "#b0bec5"
REC_COLOR = {
    "Incluir": "#2e7d32",
    "Incluir c/ ressalvas": "#66bb6a",
    "Incluir c/ ressalvas (fundacional)": "#aed581",
    "Excluir (relevancia/tipo)": "#ef6c00",
    "Excluir (dominio)": "#ff8a65",
    "Excluir (INELEGIVEL - Qualis A3)": "#b0bec5",
}
FONT = 'font-family="Segoe UI, Helvetica, Arial, sans-serif"'

def esc(s): return html.escape(str(s))

def svg_open(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" {FONT}>\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n'
            f'<text x="{w/2}" y="26" text-anchor="middle" font-size="17" '
            f'font-weight="700" fill="#1a1a1a">{esc(title)}</text>\n')

def write(name, body):
    p = f"{OUT}/{name}"
    open(p, "w", encoding="utf-8").write(body + "</svg>\n")
    print("wrote", p)

# ---------- Chart 1: paired bars SCORE_RQ (/5) and SCORE_QA (/4) per study ----------
def chart_scores():
    data = sorted(elig, key=lambda r: (float(r["SCORE_RQ"]) + float(r["SCORE_QA"]),
                                       float(r["SCORE_RQ"])), reverse=True)
    rowh, top, left, trackw = 30, 64, 92, 560
    h = top + rowh * len(data) + 56
    w = left + trackw + 70
    s = svg_open(w, h, "Aderência por estudo — SCORE_RQ (/5) e SCORE_QA (/4)")
    # gridlines at 0,25,50,75,100%
    for f in (0, .25, .5, .75, 1):
        x = left + trackw * f
        s += (f'<line x1="{x:.0f}" y1="{top-6}" x2="{x:.0f}" y2="{top+rowh*len(data)}" '
              f'stroke="#e6e6e6"/>\n'
              f'<text x="{x:.0f}" y="{top-12}" text-anchor="middle" font-size="9" '
              f'fill="#999">{int(f*100)}%</text>\n')
    for i, r in enumerate(data):
        y = top + i * rowh
        rq, qa = float(r["SCORE_RQ"]), float(r["SCORE_QA"])
        incl = r["Recomendacao"].startswith("Incluir")
        idcol = "#1b5e20" if incl else "#b71c1c"
        s += (f'<text x="{left-8}" y="{y+rowh/2+1}" text-anchor="end" font-size="11" '
              f'font-weight="700" fill="{idcol}">{esc(r["ID"])}</text>\n')
        # RQ bar (blue) top, QA bar (purple) bottom
        bw = (trackw) * (rq/5.0)
        s += (f'<rect x="{left}" y="{y+4}" width="{bw:.1f}" height="9" rx="2" fill="#1565c0"/>\n'
              f'<text x="{left+bw+5:.1f}" y="{y+12}" font-size="9" fill="#1565c0">{rq:.1f}</text>\n')
        bw2 = (trackw) * (qa/4.0)
        s += (f'<rect x="{left}" y="{y+16}" width="{bw2:.1f}" height="9" rx="2" fill="#6a1b9a"/>\n'
              f'<text x="{left+bw2+5:.1f}" y="{y+24}" font-size="9" fill="#6a1b9a">{qa:.1f}</text>\n')
    # legend
    ly = top + rowh*len(data) + 22
    s += (f'<rect x="{left}" y="{ly}" width="14" height="9" rx="2" fill="#1565c0"/>'
          f'<text x="{left+20}" y="{ly+8}" font-size="11" fill="#333">SCORE_RQ (máx. 5,0)</text>\n'
          f'<rect x="{left+200}" y="{ly}" width="14" height="9" rx="2" fill="#6a1b9a"/>'
          f'<text x="{left+220}" y="{ly+8}" font-size="11" fill="#333">SCORE_QA (máx. 4,0)</text>\n'
          f'<text x="{left}" y="{ly+26}" font-size="10" fill="#999">ID verde = Incluir · ID vermelho = Excluir · barras normalizadas ao máximo de cada escala</text>\n')
    write("chart-scores-by-study.svg", s)

# ---------- generic stacked coverage (counts) ----------
def chart_stacked(name, title, cats, seglabels, segcolors, total):
    rowh, top, left, trackw = 40, 64, 230, 540
    h = top + rowh*len(cats) + 50
    w = left + trackw + 30
    s = svg_open(w, h, title)
    for i, (label, counts) in enumerate(cats):
        y = top + i*rowh
        s += (f'<text x="{left-8}" y="{y+rowh/2+4}" text-anchor="end" font-size="12" '
              f'font-weight="700" fill="#222">{esc(label)}</text>\n')
        x = left
        for j, c in enumerate(counts):
            segw = trackw * (c/total)
            if c > 0:
                s += (f'<rect x="{x:.1f}" y="{y+6}" width="{segw:.1f}" height="22" '
                      f'fill="{segcolors[j]}"/>\n')
                s += (f'<text x="{x+segw/2:.1f}" y="{y+21}" text-anchor="middle" '
                      f'font-size="12" font-weight="700" fill="#fff">{c}</text>\n')
            x += segw
    ly = top + rowh*len(cats) + 18
    lx = left
    for j, lab in enumerate(seglabels):
        s += (f'<rect x="{lx}" y="{ly}" width="14" height="12" fill="{segcolors[j]}"/>'
              f'<text x="{lx+20}" y="{ly+11}" font-size="11" fill="#333">{esc(lab)}</text>\n')
        lx += 24 + len(lab)*6.6 + 16
    write(name, s)

def chart_rq():
    cats = []
    for rq, name in [("RQ1","RQ1 · Context Definitions"),("RQ2","RQ2 · Engineering Architecture"),
                     ("RQ3","RQ3 · Evidence Benefits"),("RQ4","RQ4 · Challenges & Ethics"),
                     ("RQ5","RQ5 · Research Gaps")]:
        c = [sum(1 for r in elig if r[rq]==v) for v in ("T","P","N")]
        cats.append((name, c))
    chart_stacked("chart-rq-coverage.svg",
                  "Cobertura por RQ (18 estudos avaliados)",
                  cats, ["T — Plenamente (1,0)","P — Parcial (0,5)","N — Insuficiente (0,0)"],
                  [G,A,R], len(elig))

def chart_qa():
    cats = []
    for qa, name in [("QA1","QA1 · Objetivos claros"),("QA2","QA2 · Metodologia replicável"),
                     ("QA3","QA3 · Base de evidências"),("QA4","QA4 · Conclusões coerentes")]:
        c = [sum(1 for r in elig if r[qa]==v) for v in ("Y","P","N")]
        cats.append((name, c))
    chart_stacked("chart-qa-coverage.svg",
                  "Qualidade (QA/DARE) — 18 estudos avaliados",
                  cats, ["Y — Sim (1,0)","P — Parcial (0,5)","N — Não (0,0)"],
                  [G,A,R], len(elig))

# ---------- Chart 4: heatmap grid SCORE_RQ x SCORE_QA (handles ties cleanly) ----------
def chart_grid():
    rq_vals = [2.5, 3.0, 3.5, 4.0, 4.5]
    qa_vals = [4.0, 3.5, 3.0, 2.5]          # top -> bottom
    cw, ch = 116, 84
    pl, pt = 92, 88
    gw, gh = cw*len(rq_vals), ch*len(qa_vals)
    w, h = pl + gw + 24, pt + gh + 60
    s = svg_open(w, h, "Mapa SCORE_RQ × SCORE_QA (contagem e IDs por célula)")
    groups = {}
    for r in elig:
        groups.setdefault((float(r["SCORE_RQ"]), float(r["SCORE_QA"])), []).append(r)
    # axis titles
    s += (f'<text x="{pl+gw/2:.0f}" y="{h-18}" text-anchor="middle" font-size="12" '
          f'font-weight="700" fill="#333">SCORE_RQ (máx. 5,0) →</text>\n'
          f'<text x="26" y="{pt+gh/2:.0f}" text-anchor="middle" font-size="12" font-weight="700" '
          f'fill="#333" transform="rotate(-90 26 {pt+gh/2:.0f})">↑ SCORE_QA (máx. 4,0)</text>\n')
    # column headers
    for ci, rqv in enumerate(rq_vals):
        x = pl + ci*cw
        s += (f'<text x="{x+cw/2:.0f}" y="{pt-10}" text-anchor="middle" font-size="12" '
              f'font-weight="700" fill="#555">{rqv:.1f}</text>\n')
    for ri, qav in enumerate(qa_vals):
        y = pt + ri*ch
        s += (f'<text x="{pl-12}" y="{y+ch/2+4:.0f}" text-anchor="end" font-size="12" '
              f'font-weight="700" fill="#555">{qav:.1f}</text>\n')
    for ri, qav in enumerate(qa_vals):
        for ci, rqv in enumerate(rq_vals):
            x, y = pl + ci*cw, pt + ri*ch
            members = groups.get((rqv, qav), [])
            n = len(members)
            if n == 0:
                fill, op = "#fafafa", 1
            else:
                cats = set("inc" if m["Recomendacao"].startswith("Incluir") else "exc" for m in members)
                base = "#2e7d32" if cats == {"inc"} else ("#ef6c00" if cats == {"exc"} else "#78909c")
                fill, op = base, 0.16 + 0.20*n
            s += (f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" rx="6" '
                  f'fill="{fill}" fill-opacity="{op:.2f}" stroke="#e0e0e0"/>\n')
            if n:
                cats = set("inc" if m["Recomendacao"].startswith("Incluir") else "exc" for m in members)
                txt = "#1b5e20" if cats=={"inc"} else ("#bf360c" if cats=={"exc"} else "#37474f")
                s += (f'<text x="{x+cw/2:.0f}" y="{y+30}" text-anchor="middle" font-size="20" '
                      f'font-weight="800" fill="{txt}">{n}</text>\n')
                # ID list wrapped (max ~4 per line)
                ids = [m["ID"] for m in members]
                lines = [", ".join(ids[i:i+4]) for i in range(0, len(ids), 4)]
                for li, ln in enumerate(lines):
                    s += (f'<text x="{x+cw/2:.0f}" y="{y+48+li*14}" text-anchor="middle" '
                          f'font-size="10.5" fill="#333">{esc(ln)}</text>\n')
    # legend
    items = [("Todos Incluir","#2e7d32"),("Todos Excluir","#ef6c00"),("Misto","#78909c")]
    cur = pl
    for lab,col in items:
        s += (f'<rect x="{cur}" y="46" width="14" height="12" rx="2" fill="{col}" fill-opacity="0.55"/>'
              f'<text x="{cur+20}" y="56" font-size="11" fill="#333">{esc(lab)}</text>\n')
        cur += 30 + len(lab)*6.6 + 20
    s += (f'<text x="{w-24}" y="56" text-anchor="end" font-size="10" fill="#999">'
          f'opacidade ∝ nº de estudos</text>\n')
    write("chart-grid-rq-qa.svg", s)

# ---------- Chart 5: recommendation distribution (all 20) ----------
def chart_recs():
    order = ["Incluir","Incluir c/ ressalvas","Incluir c/ ressalvas (fundacional)",
             "Excluir (relevancia/tipo)","Excluir (dominio)","Excluir (INELEGIVEL - Qualis A3)"]
    labels = {"Incluir":"Incluir","Incluir c/ ressalvas":"Incluir c/ ressalvas",
              "Incluir c/ ressalvas (fundacional)":"Incluir — fundacional",
              "Excluir (relevancia/tipo)":"Excluir — relevância/tipo",
              "Excluir (dominio)":"Excluir — domínio",
              "Excluir (INELEGIVEL - Qualis A3)":"Inelegível — Qualis A3"}
    counts = [(labels[o], sum(1 for r in rows if r["Recomendacao"]==o), REC_COLOR[o]) for o in order]
    rowh, top, left, trackw = 38, 64, 220, 420
    mx = max(c for _,c,_ in counts)
    h = top + rowh*len(counts) + 30; w = left + trackw + 50
    s = svg_open(w, h, "Distribuição das recomendações (20 estudos)")
    for i,(lab,c,col) in enumerate(counts):
        y = top + i*rowh
        bw = trackw*(c/mx)
        s += (f'<text x="{left-8}" y="{y+rowh/2+4}" text-anchor="end" font-size="11.5" '
              f'fill="#222">{esc(lab)}</text>\n'
              f'<rect x="{left}" y="{y+5}" width="{bw:.1f}" height="22" rx="3" fill="{col}"/>'
              f'<text x="{left+bw+8:.1f}" y="{y+21}" font-size="13" font-weight="700" fill="#333">{c}</text>\n')
    write("chart-recommendations.svg", s)

chart_scores(); chart_rq(); chart_qa(); chart_grid(); chart_recs()
print("done")
