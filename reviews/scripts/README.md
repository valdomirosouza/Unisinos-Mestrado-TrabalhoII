# reviews/scripts — geradores dos artefatos da RSL

Scripts que regeneram, **a partir da fonte de verdade** [`../resultados-consolidados.csv`](../resultados-consolidados.csv), os gráficos e o PDF do relatório de síntese. Sem dependências externas (só Python 3 da biblioteca padrão + um navegador Chromium para o PDF).

## Cadeia de regeneração

```
resultados-consolidados.csv ──(gen_charts.py)──▶ charts/*.svg
relatorio-sintese.md + charts/*.svg ──(build_pdf.py)──▶ relatorio-sintese.pdf
```

## Uso

Execute a partir da raiz do repositório (os caminhos são resolvidos relativos ao próprio script):

```bash
# 1) gráficos SVG  (CSV  ->  reviews/charts/*.svg)
python3 reviews/scripts/gen_charts.py

# 2) PDF do relatório  (md + SVGs  ->  reviews/relatorio-sintese.pdf)
python3 reviews/scripts/build_pdf.py
```

## `gen_charts.py`

- **Lê:** `reviews/resultados-consolidados.csv`
- **Escreve:** `reviews/charts/chart-*.svg` (5 gráficos: aderência por estudo, cobertura por RQ, cobertura por QA, mapa RQ×QA, distribuição de recomendações)
- SVG vetorial puro, gerado à mão — sem matplotlib/numpy. Determinístico: mesmo CSV ⇒ SVGs idênticos.

## `build_pdf.py`

- **Lê:** `reviews/relatorio-sintese.md` + `reviews/charts/*.svg`
- **Escreve:** `reviews/relatorio-sintese.pdf` (A4) + um `.html` temporário
- Pipeline: conversor Markdown→HTML focado (headings, tabelas GFM com alinhamento, imagens com SVG embutido em base64, blockquotes, listas, ênfase/código/links) → **PDF via Chromium headless** (`--print-to-pdf`). Sem pandoc/LaTeX/wkhtmltopdf.
- Detecta automaticamente Google Chrome / Chromium / Brave / Edge. Se nenhum for encontrado, deixa o HTML pronto e instrui a impressão manual.
- Observação: o Chrome grava um timestamp interno no PDF, então execuções repetidas produzem bytes ligeiramente diferentes mesmo com conteúdo idêntico.

## Fluxo completo após editar dados/relatório

1. Atualize `reviews/resultados-consolidados.csv` (e/ou `relatorio-sintese.md`).
2. `python3 reviews/scripts/gen_charts.py`
3. `python3 reviews/scripts/build_pdf.py`
4. Revise e faça commit dos artefatos alterados.

> Os demais geradores do projeto (prompts e o próprio CSV de resultados) foram produzidos uma vez e ficam fora deste diretório; estes dois scripts cobrem a regeneração das **visualizações** e do **PDF**, que dependem diretamente do CSV.
