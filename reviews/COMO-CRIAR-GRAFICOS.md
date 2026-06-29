# Como criar os gráficos (How-to)

Guia de como as visualizações da RSL são produzidas — a abordagem, como **regenerar**, como **adicionar um novo gráfico** e como **pré-visualizar/embutir** em relatórios. Tudo sem dependências externas (apenas Python 3 da biblioteca padrão).

## TL;DR

```bash
# regenerar os 5 gráficos a partir do CSV
python3 reviews/scripts/gen_charts.py

# (opcional) reconstruir o PDF do relatório, que embute os gráficos
python3 reviews/scripts/build_pdf.py
```

- **Fonte de verdade:** [`resultados-consolidados.csv`](resultados-consolidados.csv).
- **Gerador:** [`scripts/gen_charts.py`](scripts/gen_charts.py).
- **Saída:** `charts/*.svg` (5 arquivos) → exibidos em [`graficos.md`](graficos.md) e embutidos no [relatório](relatorio-sintese.md)/[PDF](relatorio-sintese.pdf).

## Por que SVG escrito à mão (e não matplotlib)?

| Critério                     | SVG à mão                            | matplotlib/PNG     |
| ---------------------------- | ------------------------------------ | ------------------ |
| Dependências                 | **nenhuma** (só `csv`, `os`, `html`) | numpy + matplotlib |
| Renderiza no GitHub Markdown | **sim** (`![](x.svg)`)               | sim (PNG)          |
| Versionável com diff legível | **sim** (texto)                      | não (binário)      |
| Nitidez em qualquer escala   | **vetorial**                         | rasterizado        |
| Controle fino de layout      | total                                | alto               |

O custo é escrever o SVG na unha — mitigado por **funções utilitárias** reaproveitáveis (barras empilhadas, etc.).

## Fluxo de dados

```
resultados-consolidados.csv
        │   (csv.DictReader)
        ▼
  rows  ──filter SCORE_RQ != "NA"──▶  elig  (18 estudos avaliados)
        │
        ├─▶ chart_scores()  ─▶ charts/chart-scores-by-study.svg
        ├─▶ chart_rq()      ─▶ charts/chart-rq-coverage.svg
        ├─▶ chart_qa()      ─▶ charts/chart-qa-coverage.svg
        ├─▶ chart_grid()    ─▶ charts/chart-grid-rq-qa.svg
        └─▶ chart_recs()    ─▶ charts/chart-recommendations.svg   (usa os 20 estudos)
```

## Anatomia do `gen_charts.py`

1. **Caminhos relativos ao script** — funciona de qualquer diretório:
   ```python
   HERE = os.path.dirname(os.path.abspath(__file__))   # reviews/scripts
   REVIEWS = os.path.dirname(HERE)                       # reviews
   CSV = os.path.join(REVIEWS, "resultados-consolidados.csv")
   OUT = os.path.join(REVIEWS, "charts")
   ```
2. **Paleta e helpers** — cores T/P/N (verde/âmbar/vermelho), cores por recomendação, `esc()` (escape HTML), `svg_open(w,h,title)` (abre o `<svg>` + título) e `write(name, body)` (fecha `</svg>` e grava).
3. **Funções de gráfico** — cada uma monta uma string SVG e chama `write(...)`:
   - `chart_scores()` — barras pareadas SCORE_RQ/SCORE_QA por estudo, ordenadas pela soma; ID verde = Incluir, vermelho = Excluir.
   - `chart_stacked(...)` — helper genérico de **barras empilhadas T/P/N**; usado por `chart_rq()` e `chart_qa()`.
   - `chart_grid()` — **mapa** SCORE_RQ × SCORE_QA: agrupa estudos por coordenada (lida com empates), célula colorida pelo consenso de recomendação, opacidade ∝ contagem.
   - `chart_recs()` — barras horizontais da distribuição das recomendações (20 estudos).

## Receita: adicionar um novo gráfico

1. Escreva uma função `chart_novo()` que monte o SVG e chame `write("chart-novo.svg", s)`. Reaproveite `svg_open`, `esc` e, se for barra empilhada, `chart_stacked(...)`.
2. Registre a chamada no final do arquivo (junto de `chart_scores(); chart_rq(); ...`).
3. Rode `python3 reviews/scripts/gen_charts.py`.
4. **Pré-visualize** (macOS, sem instalar nada):
   ```bash
   qlmanage -t -s 950 -o /tmp reviews/charts/chart-novo.svg   # gera /tmp/chart-novo.svg.png
   ```
5. Adicione `![Título](charts/chart-novo.svg)` em [`graficos.md`](graficos.md) (e/ou no relatório).

### Esqueleto mínimo

```python
def chart_novo():
    w, h = 760, 360
    s = svg_open(w, h, "Meu gráfico")
    # ... desenhe <rect>, <line>, <text>, <circle> usando coordenadas SVG ...
    s += f'<rect x="40" y="60" width="200" height="20" fill="#1565c0"/>\n'
    s += f'<text x="40" y="100" font-size="12" fill="#333">{esc("rótulo")}</text>\n'
    write("chart-novo.svg", s)
```

> Dica: coordenadas SVG têm origem no canto **superior-esquerdo** (y cresce para baixo). Texto longo? reserve margem suficiente (vários bugs corrigidos aqui foram rótulos cortados por margem pequena).

## Como os gráficos entram no PDF

[`scripts/build_pdf.py`](scripts/build_pdf.py) converte o relatório Markdown em HTML e **embute cada SVG como `data:image/svg+xml;base64,...`** (auto-contido, sem depender de caminhos), depois imprime via **Chromium headless** (`--print-to-pdf`). Detalhes em [`scripts/README.md`](scripts/README.md).

## Boas práticas adotadas

- **Determinismo:** mesmo CSV ⇒ SVGs byte-idênticos (sem timestamps/aleatoriedade) — diffs limpos no git.
- **Validação:** confira o SVG como XML bem-formado e **inspecione visualmente** (Quick Look → PNG) antes de commitar.
- **Cores consistentes** com o relatório (T/Y = verde, P = âmbar, N = vermelho; Incluir = verde, Excluir = laranja/cinza).

---

_Ver também: [galeria de gráficos](graficos.md) · [scripts](scripts/README.md) · [dashboard](DASHBOARD.md)._
