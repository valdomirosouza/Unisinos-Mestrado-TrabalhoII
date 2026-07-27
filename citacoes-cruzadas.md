# Citações Cruzadas no Corpus — Quem Cita Quem (P01–P40)

> 🧭 **Navegação:** [🏠 README raiz](README.md) · [📑 Fichas](report/README.md) · [🔀 PRISMA](reviews/PRISMA.md) · bibliometria em [`papers.csv`](papers.csv)

Levantamento de **citações entre os 39 artigos do corpus** (quantas vezes cada artigo é citado pelos seus pares P01–P40), com **tripla checagem** em três APIs: **OpenAlex** (`referenced_works`), **Crossref** (lista `reference` com DOIs) e **Scopus** (campo `REF()` cruzado com os DOIs do corpus). Verificado em **2026-07-27**.

## Método

1. **OpenAlex:** para cada artigo, obteve-se `referenced_works` e verificou-se a interseção com os IDs OpenAlex do corpus (resolvidos por DOI, 39/39).
2. **Crossref:** para cada artigo, extraíram-se os DOIs da lista de referências e casaram-se com os DOIs canônicos do corpus.
3. **Scopus:** o campo `REF()` **não indexa DOIs — indexa os títulos** das referências (descoberta desta verificação). A consulta usada foi `REF("<título do artigo alvo>") AND (DOI("…") OR …)` com o OR dos 38 DOIs do corpus como citadores potenciais, validada contra pares positivos e negativos conhecidos.
4. **Corroboração:** divergências foram conferidas em [`referencias.csv`](referencias.csv) (proveniência Crossref/OpenAlex/OpenCitations/Semantic Scholar extraída via [`DOIS.py`](DOIS.py)).

## Matriz de citações no corpus

Somente os artigos **citados por ao menos um par** são listados; os demais 29 artigos têm contagem 0 nas três fontes (esperado: P20–P40 são de 2025–2026, recentes demais para citação interna).

| ID      | Artigo (curto)                           | OpenAlex | Crossref | Scopus | União | Citado nos artigos                                                                                               |
| ------- | ---------------------------------------- | :------: | :------: | :----: | :---: | ---------------------------------------------------------------------------------------------------------------- |
| **P10** | Agentic AI: Autonomous Intelligence      |    7     |    7     |   6    | **7** | P01, P03, P06, P09, P15, P24, P33 _(P01 invisível no Scopus — não indexado)_                                     |
| **P14** | Transforming Cybersecurity w/ Agentic AI |    5     |    5     |   5    | **5** | P03, P06, P15, P28, P37                                                                                          |
| **P09** | AI Agents vs. Agentic AI                 |    0     |    0     |   4    | **4** | P03, P06, P15, P33 _(citado via DOI de preprint `10.70777/…`; só Scopus/S2 resolvem para a versão do periódico)_ |
| **P02** | Agentic AI Shaping a Smart Future        |    2     |    2     |   2    | **2** | P03, P15                                                                                                         |
| **P13** | Retail Resilience Engine                 |    2     |    2     |   2    | **2** | P03, P15                                                                                                         |
| **P16** | MLOps and AIOps Survey                   |    1     |    1     |   2    | **2** | P05, P29 _(P29→P16 só detectado no Scopus)_                                                                      |
| **P12** | Autonomous System Security w/ GenAI      |    1     |    1     |   1    | **1** | P28                                                                                                              |
| **P24** | AgentAI Survey (Industry 4.0)            |    1     |    1     |   1    | **1** | P15                                                                                                              |
| **P31** | LEMAD                                    |    0     |    1     |   1    | **1** | P38 _(ausente na OpenAlex)_                                                                                      |
| **P39** | Agentic AI & the Cyber Arms Race         |    1     |    1     |   1    | **1** | P33                                                                                                              |
| —       | **Demais 29 artigos**                    |    0     |    0     |   0    | **0** | —                                                                                                                |

**Totais de arestas detectadas:** OpenAlex **20** · Crossref **21** · Scopus **25** · **União: 26** pares (citador → citado).

## Arestas completas (citador → citado)

| Citador | Cita no corpus                |
| ------- | ----------------------------- |
| P01     | P10                           |
| P03     | P02, P09*, P10, P13, P14      |
| P05     | P16                           |
| P06     | P09*, P10, P14                |
| P09     | P10                           |
| P15     | P02, P09*, P10, P13, P14, P24 |
| P24     | P10                           |
| P28     | P12, P14                      |
| P29     | P16*                          |
| P33     | P09*, P10, P39                |
| P37     | P14                           |
| P38     | P31                           |

_\* arestas detectadas apenas no Scopus (resolução por título); as demais constam em OpenAlex e/ou Crossref._

## Observações

1. **Os hubs do corpus são os surveys fundacionais:** P10 (7 citações internas), P14 (5) e P09 (4) — consistente com seu papel de fundamentação conceitual; os 14 estudos incluídos (P20–P37) ainda não citam uns aos outros (todos de 2025–2026).
2. **Divergência OpenAlex/Crossref × Scopus no P09:** as 4 citações apontam para o DOI de preprint `10.70777/si.v2i3.15161`; OpenAlex/Crossref registram essa versão como obra distinta, enquanto Scopus (busca por título) e Semantic Scholar (em `referencias.csv`) resolvem para a versão do periódico (Information Fusion). A contagem da União considera a citação ao conteúdo, independente da versão.
3. **Limitação do Scopus:** P01 (F1000Research) não é indexado — a aresta P01→P10 é invisível lá; e `REF()` casa por título, não por DOI (falha silenciosa com DOIs — mesma família de quirks da [validação da string](picoc/picoc-search-string.md)).
4. **P38→P31 ausente na OpenAlex** (presente em Crossref e Scopus) — lacuna pontual de indexação de referências.
5. Ligação com a rede maior de referências: as listas completas (4.995 arestas para fora do corpus) estão em [`referencias.csv`](referencias.csv).

---

_Gerado em 2026-07-27 via APIs OpenAlex, Crossref e Scopus Search (chave institucional; não versionada). Direção das arestas: A→B = "A cita B"._
