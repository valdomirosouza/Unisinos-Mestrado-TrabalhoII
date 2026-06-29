# Gráficos — Resultados da RSL (P20–P40)

> 🧭 [📊 Dashboard](DASHBOARD.md) · [🛠️ Como criar os gráficos](COMO-CRIAR-GRAFICOS.md) · [🏠 README raiz](../README.md)

Visualizações geradas a partir de [`resultados-consolidados.csv`](resultados-consolidados.csv) (20 estudos; 18 avaliados + 2 inelegíveis). Formato **SVG** (vetorial, renderiza no GitHub, versionável). Gerados sem dependências externas.

> Verde = Plenamente/Sim (T/Y) · Âmbar = Parcial (P) · Vermelho = Insuficiente/Não (N/N).

---

## 1. Aderência por estudo (SCORE_RQ e SCORE_QA)

Estudos ordenados pela soma dos escores. ID em **verde = Incluir**, **vermelho = Excluir**.

![Aderência por estudo](charts/chart-scores-by-study.svg)

---

## 2. Cobertura por questão de pesquisa (RQ)

Distribuição T/P/N entre os 18 estudos avaliados. **RQ4 (Ética & Desafios) é a lacuna** — apenas 4 plenamente respondidas.

![Cobertura por RQ](charts/chart-rq-coverage.svg)

---

## 3. Avaliação de qualidade (QA/DARE)

QA1 universal; QA3=N nos 4 estudos secundários (sem validação empírica própria).

![Cobertura por QA](charts/chart-qa-coverage.svg)

---

## 4. Mapa SCORE_RQ × SCORE_QA

Cada célula = uma coordenada de escore; mostra a contagem e os IDs. Cor = consenso de recomendação (verde = todos Incluir, laranja = todos Excluir, cinza = misto); opacidade ∝ nº de estudos.

![Mapa RQ x QA](charts/chart-grid-rq-qa.svg)

---

## 5. Distribuição das recomendações

![Distribuição das recomendações](charts/chart-recommendations.svg)

---

_Para regenerar: os SVGs derivam diretamente de `resultados-consolidados.csv`. Demais artefatos: [`README.md`](README.md) (índice), [`relatorio-sintese.md`](relatorio-sintese.md) (análise), `review-Pxx.md` (pareceres)._
