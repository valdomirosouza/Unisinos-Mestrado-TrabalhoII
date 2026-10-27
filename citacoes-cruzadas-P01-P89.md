# Citações Cruzadas no Corpus — Quem Cita Quem (P01–P89)

> 🧭 **Navegação:** [🏠 README raiz](README.md) · [📑 Fichas](report/README.md) · [🔀 PRISMA](reviews/PRISMA.md) · [🕸️ Versão P01–P40](citacoes-cruzadas.md) · bibliometria em [`papers.csv`](papers.csv) / [`papers-ciclo2.csv`](papers-ciclo2.csv)

Levantamento de **citações entre os artigos do corpus ampliado** (P01–P89: 88 artigos), agora com **tripla checagem completa**: **OpenAlex** (`referenced_works`) e **Crossref** (listas `reference` com DOIs), verificados em **2026-10-25**, e **Scopus** (`REF()` por título × DOIs do corpus), verificado em **2026-10-26** com a chave regenerada. A [versão P01–P40](citacoes-cruzadas.md) (2026-07-27) permanece como registro histórico.

## Método

1. **OpenAlex:** `referenced_works` × IDs do corpus (88/88 por DOI + ID do preprint do P09).
2. **Crossref:** DOIs das listas de referências × DOIs canônicos (+ alias de preprint do P09).
3. **Scopus:** `REF("<título do alvo>") AND (DOI(…) OR …)` com os 87 DOIs citadores em **blocos de 30** — `REF()` casa por **título**, não por DOI (quirk do ciclo 1). **Quirk novo (2026-10-26): o nível de serviço da chave limita `count ≤ 25` por requisição** — valores maiores retornam HTTP 400 "Exceeds the maximum number allowed for the service level" (diagnóstico desta rodada: duas varreduras completas falharam com 400 até isolar o parâmetro). Correção pontual: o título do P14 no índice traz o sufixo "(Kshetri)", que zerava o `REF()` — consulta refeita com o título real.
4. **Alias do P09** incluído na correspondência OA/CR (contagem por conteúdo, independente da versão).

## Matriz de citações no corpus

Somente artigos **citados por ao menos um par** (27); os demais 61 têm contagem 0 nas três fontes.

| ID | Artigo (curto) | OpenAlex | Crossref | Scopus | União | Citado nos artigos |
| --- | --- | :-: | :-: | :-: | :-: | --- |
| **P10** | Agentic AI: Autonomous Intelligence | 7 | 7 | 6 | **7** | P01, P03, P06, P09, P15, P24, P33 _(P01 invisível no Scopus — não indexado)_ |
| **P09** | AI Agents vs. Agentic AI | 6 | 6 | 5 | **6** | P01, P03, P06, P15, P33, P55 _(inclui alias de preprint; P01 invisível no Scopus)_ |
| **P14** | Transforming Cybersecurity w/ Agentic AI | 5 | 5 | 5 | **5** | P03, P06, P15, P28, P37 |
| **P16** | MLOps and AIOps Survey | 2 | 1 | 3 | **3** | P05, P29, P43 |
| **P65** | DL for Log Anomaly Detection (survey) | 3 | 3 | 3 | **3** | P28, P31, P89 |
| **P02** | Agentic AI Shaping a Smart Future | 2 | 2 | 2 | **2** | P03, P15 |
| **P13** | Retail Resilience Engine | 2 | 2 | 2 | **2** | P03, P15 |
| **P39** | Agentic AI & the Cyber Arms Race | 2 | 2 | 2 | **2** | P33, P76 |
| **P53** | LLM + Bayesian Nets RCA | 2 | 1 | 2 | **2** | P31, P40 |
| **P54** | LLM Reasoning → AI Agents | 0 | 0 | 2 | **2** | P06, P15 _(arestas detectadas apenas no Scopus)_ |
| **P70** | OS Log Anomaly via Sentiment | 2 | 2 | 2 | **2** | P65, P89 |
| **P12** | Autonomous System Security w/ GenAI | 1 | 1 | 1 | **1** | P28 |
| **P15** | The Rise of Agentic AI | 1 | 1 | 1 | **1** | P55 |
| **P18** | Model-Based Automation in DevOps | 1 | 1 | 1 | **1** | P43 |
| **P20** | LLM Agentic Workflow (IaC) | 1 | 1 | 0 | **1** | P79 |
| **P24** | AgentAI Survey (Industry 4.0) | 1 | 1 | 1 | **1** | P15 |
| **P31** | LEMAD | 0 | 1 | 1 | **1** | P38 |
| **P45** | DL Anomaly Detection TS (review) | 1 | 0 | 1 | **1** | P41 |
| **P50** | Observability of Microservices (survey) | 1 | 1 | 1 | **1** | P16 |
| **P52** | LLMs in Cybersecurity (SLR) | 1 | 1 | 1 | **1** | P28 |
| **P68** | Big-Data RCA (quality) | 1 | 1 | 1 | **1** | P26 |
| **P72** | LLMs Vulnerability → Defense | 1 | 1 | 1 | **1** | P28 |
| **P76** | SOC Hyper-Automation Agentic AI | 1 | 1 | 0 | **1** | P28 |
| **P77** | GenAI in Cybersecurity | 1 | 1 | 1 | **1** | P28 |
| **P78** | RAG + LLM Incident Timeline | 1 | 0 | 1 | **1** | P79 |
| **P80** | Imbalanced Learning for Alerts | 1 | 1 | 1 | **1** | P73 |
| **P83** | Wazuh RAG Copilot SOC | 1 | 1 | 1 | **1** | P76 |
| — | **Demais 61 artigos** | 0 | 0 | 0 | **0** | — |

**Totais de arestas:** OpenAlex **48** · Crossref **45** · Scopus **48** · **União: 52** pares (citador → citado) — contra 26 na rodada P01–P40.

## Arestas completas (citador → cita no corpus)

| Citador | Cita no corpus |
| --- | --- |
| P01 | P09 (†‡), P10 (†‡) |
| P03 | P02, P09, P10, P13, P14 |
| P05 | P16 |
| P06 | P09, P10, P14, P54 (§) |
| P09 | P10 |
| P15 | P02, P09, P10, P13, P14, P24, P54 (§) |
| P16 | P50 |
| P24 | P10 |
| P26 | P68 |
| P28 | P12, P14, P52, P65, P72, P76 (†‡), P77 |
| P29 | P16 (§) |
| P31 | P53, P65 |
| P33 | P09, P10, P39 |
| P37 | P14 |
| P38 | P31 (‡§) |
| P40 | P53 (†§) |
| P41 | P45 (†§) |
| P43 | P16 (†§), P18 |
| P55 | P09, P15 |
| P65 | P70 |
| P73 | P80 |
| P76 | P39, P83 |
| P79 | P20 (†‡), P78 (†§) |
| P89 | P65, P70 |

_Arestas sem marcador constam nas três fontes; caso contrário, os marcadores indicam as fontes: † OpenAlex · ‡ Crossref · § Scopus._

## Observações

1. **Hubs:** P10 (7), P09 (6), P14 (5), e os novos P16 e P65 (3 cada). **P28 segue como o maior citador interno** (7 arestas).
2. **O Scopus agregou 3 arestas exclusivas:** P06→P54 e P15→P54 (o survey "LLM Reasoning → AI Agents" é citado por dois fundacionais, mas as referências só resolvem por título) e P29→P16 (já vista no ciclo 1).
3. **Invisíveis no Scopus (4):** P01→P09 e P01→P10 (P01/F1000Research não é indexado como citador), P79→P20 e P28→P76 (referências não resolvidas por título — limitação do `REF()`).
4. **O ciclo 2 permanece tecido ao corpus nas duas direções** (P28 cita 5 candidatos do ciclo 2; P79→P20/P78; P76→P39/P83; P43→P16/P18; P55→P09/P15) — agora com confirmação em três fontes na maioria das arestas.
5. Contagens por fonte, nunca somadas; **NÃO INDEXADO ≠ 0**. Rede completa de referências externas em [`referencias.csv`](referencias.csv).

---

_OpenAlex/Crossref verificados em 2026-10-25; Scopus em 2026-10-26 (chave institucional local, não versionada). Direção: A→B = "A cita B". Versão anterior (P01–P40): [`citacoes-cruzadas.md`](citacoes-cruzadas.md)._