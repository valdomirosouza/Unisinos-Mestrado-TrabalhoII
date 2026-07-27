# Comparação entre Avaliadores — Extração PICOC (Claude × ChatGPT × Gemini)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [Prompt PICOC](picoc-extraction-prompt.md) · [Claude](picoc-results-consolidated-P01-P40-Claude.md) · [ChatGPT](picoc-results-consolidated-P01-P40-ChatGPT.md) · [Gemini](picoc-results-consolidated-P01-P40-Gemini-Atualizado.md) · dados em [CSV](picoc-comparacao-avaliadores.csv)

Comparação da extração PICOC executada com o mesmo prompt ([`picoc-extraction-prompt.md`](picoc-extraction-prompt.md) v1.0.0) por **três avaliadores** (Claude, ChatGPT, Gemini) sobre o corpus completo de **39 artigos** (P01–P35, P37–P40). A unidade de comparação é o **status atribuído a cada elemento PICOC** por artigo: `DECLARED` (conteúdo substantivo extraído) ou `NA` (registrado como "N/A", p.ex. estudo de mapeamento); nenhum avaliador usou `NÃO DECLARADO` como valor integral de elemento. A matriz completa está em [`picoc-comparacao-avaliadores.csv`](picoc-comparacao-avaliadores.csv).

> ℹ️ **Versão dos insumos:** o arquivo original do Gemini ([`picoc-results-consolidated-P01-P40-Gemini.md`](picoc-results-consolidated-P01-P40-Gemini.md)) não cobria P01–P09; esta comparação usa a versão corrigida [`picoc-results-consolidated-P01-P40-Gemini-Atualizado.md`](picoc-results-consolidated-P01-P40-Gemini-Atualizado.md), que cobre os 39 artigos. O original é mantido como registro histórico.

## Cobertura

| Avaliador | Artigos cobertos | Fonte                                                 |
| --------- | :--------------: | ----------------------------------------------------- |
| Claude    |      39/39       | `…-Claude.md`                                         |
| ChatGPT   |      39/39       | `…-ChatGPT.md`                                        |
| Gemini    |      39/39       | `…-Gemini-Atualizado.md` (original cobria só P10–P40) |

## Acordo por elemento PICOC (39 artigos)

| Elemento       | Acordo médio (3 avaliadores) | Fleiss' κ |
| -------------- | :--------------------------: | :-------: |
| Population     |             100%             |   1,00    |
| Intervention   |             100%             |   1,00    |
| **Comparison** |           **79%**            | **0,37**  |
| Outcomes       |             100%             |   1,00    |
| Context        |             100%             |   1,00    |

Pares (Comparison, Cohen's κ): **Claude × ChatGPT** 82% / 0,42 · **Claude × Gemini** 82% / 0,47 · **ChatGPT × Gemini** 74% / 0,22.

- **Population, Intervention, Outcomes e Context:** acordo perfeito de status nos 39 artigos. Nota metodológica: com distribuição quase uniforme (tudo `DECLARED`), o κ = 1,00 é trivial; o acordo relevante é o de **conteúdo**, tratado qualitativamente abaixo.
- **Comparison segue como único elemento discriminante:** 79% de acordo, **Fleiss' κ = 0,37 (razoável/moderado)**. Completar a cobertura do Gemini _reduziu_ o κ (era 0,42 com 30 artigos): os P01–P09 recém-incluídos adicionaram 4 divergências novas (P01, P03, P04, P08) — reforçando que a discordância é sistemática na fronteira definicional, não artefato de amostra.

## Distribuição de Comparison por avaliador (39 artigos)

| Avaliador | DECLARED | N/A |
| --------- | :------: | :-: |
| Claude    |    31    |  8  |
| ChatGPT   |    32    |  7  |
| Gemini    |    30    |  9  |

## Divergências em Comparison (12 artigos)

| ID  |  Claude  | ChatGPT  |  Gemini   | Natureza da divergência                                                               |
| --- | :------: | :------: | :-------: | ------------------------------------------------------------------------------------- |
| P01 |   N/A    | DECLARED | DECLARED  | ChatGPT/Gemini aceitam contrastes internos (arquiteturas; "IA/LLMs tradicionais")     |
| P03 |   N/A    | DECLARED |    N/A    | ChatGPT aceita comparação exploratória GPT-4o vs. DeepSeek-R1                         |
| P04 |   N/A    |   N/A    | DECLARED  | Gemini aceita "automação tradicional e planejamento humano" como contraste            |
| P08 |   N/A    |   N/A    | DECLARED  | Gemini aceita "ML totalmente automatizado" como contraste do HITL                     |
| P12 |   N/A    | DECLARED |    N/A    | ChatGPT aceita contraste conceitual GenAI vs. AI/ML tradicional                       |
| P15 | DECLARED | DECLARED |    N/A    | Gemini rejeita o contraste de paradigmas por ser não-experimental                     |
| P16 | DECLARED | DECLARED |    N/A    | Gemini rejeita o framework conceitual MLOps vs. AIOps                                 |
| P17 |   N/A    | DECLARED |    N/A    | ChatGPT aceita o contraste XAI vs. black-box                                          |
| P18 | DECLARED |   N/A    |    N/A    | Claude aceita a comparação pontual ML vs. rule-based (AVL)                            |
| P29 | DECLARED | DECLARED |    N/A    | Gemini trata a SLR como mapeamento; os demais aceitam ML/DL vs. LLM-driven            |
| P33 | DECLARED |   N/A    | DECLARED* | *Gemini contraditório: raciocínio diz N/A, tabela consolidada declara                 |
| P40 | DECLARED |   N/A    | DECLARED  | Claude/Gemini aceitam contraste com manual/rule-based/ML-DL; ChatGPT marca survey N/A |

## Interpretação

1. **A divergência é definicional, não factual.** Os 12 casos são estudos secundários ou com comparação **conceitual/paradigmática** (não empírica); a discordância está na fronteira "contraste conceitual conta como Comparison?", não na leitura dos artigos. Nenhum estudo primário com baseline experimental divergiu.
2. **Nenhum avaliador é uniformemente mais restritivo.** ChatGPT é permissivo com contrastes internos/exploratórios (P01, P03, P12, P17) mas restritivo com surveys comparativos (P33, P40); Gemini rejeita paradigmas conceituais (P15, P16, P29) mas aceita contrastes difusos em P04/P08; Claude exige que o artigo estruture o contraste explicitamente. O menor acordo é ChatGPT × Gemini (74%, κ = 0,22).
3. **Acordo de conteúdo onde coincidem:** nos artigos com `DECLARED` em comum, os gists convergem semanticamente (p.ex. P29, P40) — a leitura dos PDFs é consistente entre avaliadores.
4. **Achado central preservado nos três:** nenhum avaliador encontrou medição nominal de **MTTD/MTTR** no corpus — o padrão "outcomes substantivos + MTTD/MTTR NÃO DECLARADO" repete-se nos três conjuntos e **triangula a lacuna** que fundamenta a RSL.

## Ressalvas

- **Comparação em nível de status, não de texto:** as métricas medem acordo sobre a _classificação_ dos elementos; equivalência textual fina não foi quantificada (apenas amostrada via gists).
- **Inconsistência interna do Gemini em P33:** o raciocínio registra "N/A (revisão conceitual)" mas a tabela consolidada declara comparação substantiva; a tabela foi priorizada.
- **Cautela de conteúdo (exemplo):** para P14, o conjunto do Gemini reporta "redução do MTTR em 30%" como outcome — número que o artigo atribui a **claims de fornecedores**, não a medição própria; verificar a procedência ao citar.
- **κ com prevalência alta:** em Comparison, a predominância de `DECLARED` deprime o κ (paradoxo de prevalência); os valores 0,37/0,42/0,47/0,22 devem ser lidos junto com os acordos brutos (74–82%).

## Regra de protocolo aplicada e reclassificação (v1.1.0)

A recomendação foi **adotada e aplicada**: a regra **"Comparison = DECLARED somente com baseline empírico; contraste conceitual/paradigmático registra-se como `N/A (contraste conceitual)`"** foi formalizada como **Regra 5 do prompt** ([`picoc-extraction-prompt.md`](picoc-extraction-prompt.md) **v1.1.0**), e os 12 casos divergentes foram adjudicados por ela. O status final está na coluna `Comparison_Final_Protocolo` do [CSV](picoc-comparacao-avaliadores.csv).

### Reclassificação dos 12 casos

| ID      | Status final (v1.1.0)                    | Justificativa                                                                                                                                                                                |
| ------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P01     | N/A (contraste conceitual)               | Revisão narrativa; contraste entre arquiteturas/políticas é textual, sem experimento próprio                                                                                                 |
| P03     | N/A (contraste conceitual)               | Scoping review; o contraste GPT-4o vs. DeepSeek-R1 é demonstrativo/exploratório, sem baseline central                                                                                        |
| P04     | N/A (contraste conceitual)               | Literature review; LMA vs. MoE e automação tradicional são contrastes discursivos                                                                                                            |
| P08     | N/A (contraste conceitual)               | Survey; "HITL vs. ML totalmente automatizado" é eixo conceitual, sem experimento comparativo                                                                                                 |
| P12     | N/A (contraste conceitual)               | Survey; GenAI vs. AI/ML tradicional é categorização, não comparação empírica                                                                                                                 |
| P15     | N/A (contraste conceitual)               | Review; contraste de paradigmas (Agentic AI vs. GenAI/MAS/autonomic) em tabelas, sem experimento                                                                                             |
| P16     | N/A (contraste conceitual)               | Survey; framework conceitual MLOps vs. AIOps, sem baseline empírico                                                                                                                          |
| P17     | N/A (contraste conceitual)               | Review; XAI vs. black-box é contraste argumentativo                                                                                                                                          |
| **P18** | **DECLARED** (baseline empírico parcial) | Única exceção: há comparação **experimental** de componente — modelo ML vs. rule-based no caso AVL (Seç. 6.2.1) — embora sem baseline da arquitetura completa; ressalva de escopo registrada |
| P29     | N/A (contraste conceitual)               | SLR; ML/DL vs. LLM-driven é eixo de organização dos estudos revisados, não experimento dos autores                                                                                           |
| P33     | N/A (contraste conceitual)               | Revisão narrativa; defesas convencionais vs. quantum-resilient é contraste textual (resolve também a inconsistência interna do Gemini)                                                       |
| P40     | N/A (contraste conceitual)               | Survey; contraste com manual/rule-based/ML-DL é taxonômico, sem benchmark próprio                                                                                                            |

### Distribuição final de Comparison (39 artigos, pós-regra)

| Status                       |   n    | Artigos                                                                |
| ---------------------------- | :----: | ---------------------------------------------------------------------- |
| DECLARED (baseline empírico) | **26** | 25 por consenso dos 3 avaliadores + P18 (adjudicado: empírico parcial) |
| N/A (contraste conceitual)   | **11** | P01, P03, P04, P08, P12, P15, P16, P17, P29, P33, P40 (adjudicados)    |
| N/A (estudo de mapeamento)   | **2**  | P24, P26 (consenso dos 3 avaliadores)                                  |

Efeito: com a regra aplicada, as 12 divergências se resolvem por definição — a classificação final de Comparison torna-se determinística e auditável (critério: existência de baseline empírico), eliminando a fronteira subjetiva que produzia κ = 0,37. O padrão confirma o eixo da RSL: **todos os 11 reclassificados são estudos secundários/conceituais**; os 26 DECLARED são majoritariamente estudos primários com experimento.

---

_Gerado a partir dos três arquivos consolidados em `picoc/` (Gemini na versão Atualizado, cobertura completa), normalizados para status por elemento (matriz em [`picoc-comparacao-avaliadores.csv`](picoc-comparacao-avaliadores.csv)). Metodologia: acordo bruto, Cohen's κ (pares) e Fleiss' κ (trio) sobre os 39 artigos P01–P35, P37–P40._
