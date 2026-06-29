#!/usr/bin/env python3
"""Build a PDF of the RSL synthesis report (no pandoc/LaTeX).

Pipeline: relatorio-sintese.md -> HTML (inlining the SVG charts as base64)
-> PDF via headless Chrome (--print-to-pdf). Run from anywhere:

    python3 reviews/scripts/build_pdf.py

Reads:  reviews/relatorio-sintese.md  +  reviews/charts/*.svg
Writes: reviews/relatorio-sintese.pdf  (and a temp .html alongside it)
"""
import re, sys, os, base64, subprocess, tempfile, shutil, html as H

HERE = os.path.dirname(os.path.abspath(__file__))   # reviews/scripts
BASE = os.path.dirname(HERE)                          # reviews
SRC = os.path.join(BASE, "relatorio-sintese.md")
PDF = os.path.join(BASE, "relatorio-sintese.pdf")
OUT = os.path.join(tempfile.gettempdir(), "rsl-relatorio-sintese.html")

def inline(t):
    t = H.escape(t, quote=False)
    codes = []
    def stash(m):
        codes.append(m.group(1)); return f"\x00{len(codes)-1}\x00"
    t = re.sub(r"`([^`]+)`", stash, t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w_])_([^_\n]+)_(?![\w_])", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{H.escape(codes[int(m.group(1))])}</code>", t)
    return t

def img_tag(alt, path):
    full = os.path.join(BASE, path)
    if os.path.isfile(full) and full.endswith(".svg"):
        b64 = base64.b64encode(open(full, "rb").read()).decode()
        return (f'<figure><img class="chart" alt="{H.escape(alt)}" '
                f'src="data:image/svg+xml;base64,{b64}"/></figure>')
    return f'<p><em>[imagem ausente: {H.escape(path)}]</em></p>'

def align_of(cell):
    c = cell.strip()
    if c.startswith(":") and c.endswith(":"): return "center"
    if c.endswith(":"): return "right"
    if c.startswith(":"): return "left"
    return "left"

lines = open(SRC, encoding="utf-8").read().split("\n")
out, i, n = [], 0, len(lines)
para, lst = [], []
def flush_para():
    global para
    if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
def flush_lst():
    global lst
    if lst:
        out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in lst) + "</ul>"); lst = []
def flush(): flush_para(); flush_lst()

while i < n:
    ln = lines[i]
    s = ln.strip()
    # image
    m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)\s*$", s)
    if m:
        flush(); out.append(img_tag(m.group(1), m.group(2))); i += 1; continue
    # heading
    m = re.match(r"(#{1,6})\s+(.*)$", s)
    if m:
        flush(); lvl = len(m.group(1)); out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
    # hr
    if re.match(r"^(---+|\*\*\*+)$", s):
        flush(); out.append("<hr/>"); i += 1; continue
    # table
    if "|" in s and i+1 < n and re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", lines[i+1]):
        flush()
        def cells(row):
            row = row.strip()
            if row.startswith("|"): row = row[1:]
            if row.endswith("|"): row = row[:-1]
            return [c.strip() for c in row.split("|")]
        hdr = cells(lines[i]); aligns = [align_of(c) for c in cells(lines[i+1])]
        body = []; j = i+2
        while j < n and "|" in lines[j] and lines[j].strip():
            body.append(cells(lines[j])); j += 1
        t = ['<table><thead><tr>']
        for k,c in enumerate(hdr):
            a = aligns[k] if k < len(aligns) else "left"
            t.append(f'<th style="text-align:{a}">{inline(c)}</th>')
        t.append("</tr></thead><tbody>")
        for r in body:
            t.append("<tr>")
            for k,c in enumerate(r):
                a = aligns[k] if k < len(aligns) else "left"
                t.append(f'<td style="text-align:{a}">{inline(c)}</td>')
            t.append("</tr>")
        t.append("</tbody></table>")
        out.append("".join(t)); i = j; continue
    # blockquote
    if s.startswith(">"):
        flush(); buf = []
        while i < n and lines[i].strip().startswith(">"):
            buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
        out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>"); continue
    # list
    m = re.match(r"^[-*]\s+(.*)$", s)
    if m:
        flush_para(); lst.append(m.group(1)); i += 1; continue
    # blank
    if not s:
        flush(); i += 1; continue
    # paragraph
    flush_lst(); para.append(s); i += 1
flush()

CSS = """
@page { size: A4; margin: 16mm 14mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 10.3pt; line-height: 1.45; color: #1f2328; max-width: 100%; }
h1 { font-size: 20pt; margin: 0 0 4pt; color: #0d1117; }
h2 { font-size: 14pt; margin: 18pt 0 6pt; padding-bottom: 3pt;
  border-bottom: 2px solid #d0d7de; color: #0d1117; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; }
p { margin: 5pt 0; }
ul { margin: 5pt 0 5pt 0; padding-left: 18pt; }
li { margin: 2pt 0; }
hr { border: none; border-top: 1px solid #d8dee4; margin: 12pt 0; }
a { color: #0969da; text-decoration: none; }
code { background: #f2f3f5; padding: 1px 4px; border-radius: 4px;
  font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 9pt; }
blockquote { margin: 8pt 0; padding: 6pt 12pt; background: #fff8e6;
  border-left: 4px solid #f5b800; color: #4a3c00; border-radius: 0 4px 4px 0; }
blockquote p { margin: 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 8.8pt;
  page-break-inside: avoid; }
th, td { border: 1px solid #d0d7de; padding: 4pt 6pt; vertical-align: top; }
th { background: #f2f4f7; font-weight: 700; }
tr:nth-child(even) td { background: #fafbfc; }
figure { margin: 10pt 0; text-align: center; page-break-inside: avoid; }
img.chart { max-width: 100%; height: auto; border: 1px solid #eaecef; border-radius: 6px; }
h2 { page-break-after: avoid; }
"""
html = (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Relatório de Síntese — RSL</title><style>{CSS}</style></head>'
        f'<body>{"".join(out)}</body></html>')
open(OUT, "w", encoding="utf-8").write(html)
print("wrote HTML:", OUT, f"({len(html)} bytes)")

# ---- HTML -> PDF via headless Chrome (renders SVG + CSS tables) ----
CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome"), shutil.which("chromium"),
    shutil.which("chromium-browser"), shutil.which("brave-browser"),
]
chrome = next((c for c in CANDIDATES if c and os.path.exists(c)), None)
if not chrome:
    print("\nChrome/Chromium não encontrado. HTML pronto em:", OUT)
    print("Gere o PDF manualmente (ex.): abra o HTML e 'Imprimir > Salvar como PDF'.")
    sys.exit(0)

cmd = [chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
       f"--print-to-pdf={PDF}", f"file://{OUT}"]
r = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(PDF) and os.path.getsize(PDF) > 0:
    print("wrote PDF: ", PDF, f"({os.path.getsize(PDF)} bytes)")
else:
    sys.stderr.write(r.stderr + "\n")
    sys.exit("Falha ao gerar PDF via Chrome.")
