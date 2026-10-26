# Citações Cruzadas no Corpus — Quem Cita Quem (P01–P89)

> 🧭 **Navegação:** [🏠 README raiz](README.md) · [📑 Fichas](report/README.md) · [🔀 PRISMA](reviews/PRISMA.md) · [🕸️ Versão P01–P40](citacoes-cruzadas.md) · bibliometria em [`papers.csv`](papers.csv) / [`papers-ciclo2.csv`](papers-ciclo2.csv)

Atualização do levantamento de **citações entre os artigos do corpus ampliado** (P01–P89: 88 artigos — os 39 do corpus original mais os 49 candidatos do ciclo 2), verificada em **2026-10-25** com **dupla checagem**: **OpenAlex** (`referenced_works`) e **Crossref** (lista `reference` com DOIs). A terceira fonte (**Scopus**) está **PENDENTE** — sem chave de API na sessão; a coluna será preenchida quando a chave for regenerada. A [versão P01–P40](citacoes-cruzadas.md) (2026-07-27, tripla checagem) permanece como registro histórico.

## Método

1. **OpenAlex:** `referenced_works` de cada um dos 88 artigos, cruzado com os IDs OpenAlex do corpus (88/88 resolvidos por DOI, mais o ID da versão preprint do P09).
2. **Crossref:** DOIs das listas de referências casados com os DOIs canônicos do corpus (mais o DOI de preprint do P09).
3. **Alias do P09:** diferentemente da rodada de 2026-07-27 (em que OpenAlex/Crossref mostravam 0 para o P09 por registrarem o preprint `10.70777/si.v2i3.15161` como obra distinta), esta rodada **inclui o alias na correspondência** — as contagens OA/CR do P09 agora refletem citações ao conteúdo, independentemente da versão, alinhadas ao critério da União do ciclo 1.
4. Insumos: DOIs de [`Papers_Index.csv`](Papers_Index.csv); corroboração disponível em [`referencias.csv`](referencias.csv) (via [`DOIS.py`](DOIS.py)).

## Matriz de citações no corpus

Somente os artigos **citados por ao menos um par** são listados (26); os demais 62 têm contagem 0 nas duas fontes.

| ID      | Artigo (curto)                           | OpenAlex | Crossref | Scopus | União | Citado nos artigos                                        |
| ------- | ---------------------------------------- | :------: | :------: | :----: | :---: | --------------------------------------------------------- |
| **P10** | Agentic AI: Autonomous Intelligence      |    7     |    7     | PEND.  | **7** | P01, P03, P06, P09, P15, P24, P33                         |
| **P09** | AI Agents vs. Agentic AI                 |    6     |    6     | PEND.  | **6** | P01, P03, P06, P15, P33, P55 _(inclui alias de preprint)_ |
| **P14** | Transforming Cybersecurity w/ Agentic AI |    5     |    5     | PEND.  | **5** | P03, P06, P15, P28, P37                                   |
| **P65** | DL for Log Anomaly Detection (survey)    |    3     |    3     | PEND.  | **3** | P28, P31, P89                                             |
| **P02** | Agentic AI Shaping a Smart Future        |    2     |    2     | PEND.  | **2** | P03, P15                                                  |
| **P13** | Retail Resilience Engine                 |    2     |    2     | PEND.  | **2** | P03, P15                                                  |
| **P16** | MLOps and AIOps Survey                   |    2     |    1     | PEND.  | **2** | P05, P43†                                                 |
| **P39** | Agentic AI & the Cyber Arms Race         |    2     |    2     | PEND.  | **2** | P33, P76                                                  |
| **P53** | LLM + Bayesian Nets RCA                  |    2     |    1     | PEND.  | **2** | P31, P40†                                                 |
| **P70** | OS Log Anomaly via Sentiment             |    2     |    2     | PEND.  | **2** | P65, P89                                                  |
| **P12** | Autonomous System Security w/ GenAI      |    1     |    1     | PEND.  | **1** | P28                                                       |
| **P15** | The Rise of Agentic AI                   |    1     |    1     | PEND.  | **1** | P55                                                       |
| **P18** | Model-Based Automation in DevOps         |    1     |    1     | PEND.  | **1** | P43                                                       |
| **P20** | LLM Agentic Workflow (IaC)               |    1     |    1     | PEND.  | **1** | P79                                                       |
| **P24** | AgentAI Survey (Industry 4.0)            |    1     |    1     | PEND.  | **1** | P15                                                       |
| **P31** | LEMAD                                    |    0     |    1     | PEND.  | **1** | P38‡                                                      |
| **P45** | DL Anomaly Detection TS (review)         |    1     |    0     | PEND.  | **1** | P41†                                                      |
| **P50** | Observability of Microservices (survey)  |    1     |    1     | PEND.  | **1** | P16                                                       |
| **P52** | LLMs in Cybersecurity (SLR)              |    1     |    1     | PEND.  | **1** | P28                                                       |
| **P68** | Big-Data RCA (quality)                   |    1     |    1     | PEND.  | **1** | P26                                                       |
| **P72** | LLMs Vulnerability → Defense             |    1     |    1     | PEND.  | **1** | P28                                                       |
| **P76** | SOC Hyper-Automation Agentic AI          |    1     |    1     | PEND.  | **1** | P28                                                       |
| **P77** | GenAI in Cybersecurity                   |    1     |    1     | PEND.  | **1** | P28                                                       |
| **P78** | RAG + LLM Incident Timeline              |    1     |    0     | PEND.  | **1** | P79†                                                      |
| **P80** | Imbalanced Learning for Alerts           |    1     |    1     | PEND.  | **1** | P73                                                       |
| **P83** | Wazuh RAG Copilot SOC                    |    1     |    1     | PEND.  | **1** | P76                                                       |
| —       | **Demais 62 artigos**                    |    0     |    0     | PEND.  | **0** | —                                                         |

**Totais de arestas detectadas:** OpenAlex **48** · Crossref **45** · **União: 49** pares (citador → citado) — contra 26 na rodada P01–P40.

## Arestas completas (citador → cita no corpus)

| Citador | Cita no corpus                    |
| ------- | --------------------------------- |
| P01     | P09, P10                          |
| P03     | P02, P09, P10, P13, P14           |
| P05     | P16                               |
| P06     | P09, P10, P14                     |
| P09     | P10                               |
| P15     | P02, P09, P10, P13, P14, P24      |
| P16     | P50                               |
| P24     | P10                               |
| P26     | P68                               |
| P28     | P12, P14, P52, P65, P72, P76, P77 |
| P31     | P53, P65                          |
| P33     | P09, P10, P39                     |
| P37     | P14                               |
| P38     | P31‡                              |
| P40     | P53†                              |
| P41     | P45†                              |
| P43     | P16†, P18                         |
| P55     | P09, P15                          |
| P65     | P70                               |
| P73     | P80                               |
| P76     | P39, P83                          |
| P79     | P20, P78†                         |
| P89     | P65, P70                          |

_† aresta detectada apenas na OpenAlex · ‡ apenas no Crossref; as demais constam nas duas fontes._

## Observações

1. **Os hubs seguem sendo os surveys fundacionais** — P10 (7), P09 (6) e P14 (5) — e surge um hub novo: **P65** (survey de log anomaly detection, 3 citações internas, incl. do P28 do corpus incluído e do P89).
2. **O ciclo 2 está tecido no corpus, nas duas direções.** Estudos do corpus original citam candidatos do ciclo 2 — **P28 cita cinco** (P52, P65, P72, P76, P77), P31 cita P53/P65, P40 cita P53, P26 cita P68 — e candidatos do ciclo 2 citam o corpus: **P79 cita P20** (incluído no ciclo 1) e P78; **P76 cita P39 e P83**; P43 cita P16/P18; **P55 cita P09 e P15**. Isso corrobora a aderência temática do lote e cria trilhas de snowballing já capturadas.
3. **Maior citador do corpus: P28** (7 arestas internas) — o estudo de MAS/LLM para SOC conecta o núcleo incluído aos fundacionais do ciclo 2.
4. **P09 normalizado:** com o alias de preprint incluído na correspondência, OpenAlex/Crossref agora registram 6 citações (a rodada de 2026-07-27 mostrava 0/0 e dependia do Scopus) — e duas arestas novas (P01→P09, P55→P09) além das 4 conhecidas.
5. **Arestas entre excluídos também mapeadas** (P41→P45, P26→P68, P73→P80, P65→P70, P89→P65/P70): úteis para discutir a coesão do cluster de detecção não-agêntico excluído na triagem.
6. **Scopus pendente:** a rodada do ciclo 1 mostrou que o Scopus adiciona arestas resolvidas por título (lá, +5 sobre OpenAlex/Crossref); a coluna será completada quando houver chave de API. **Contagens permanecem por fonte — nunca somadas; PENDENTE ≠ 0.**

---

_Gerado em 2026-10-25 via APIs OpenAlex e Crossref (sem chave; coluna Scopus pendente de chave institucional). Direção das arestas: A→B = "A cita B". Versão anterior (P01–P40, tripla checagem): [`citacoes-cruzadas.md`](citacoes-cruzadas.md)._
