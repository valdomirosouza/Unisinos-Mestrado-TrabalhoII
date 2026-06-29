# 📊 Dashboard de Resultados — RSL "Agentic AI Copilot para Resposta a Incidentes"

Painel central que reúne **todos os artefatos** da avaliação dos estudos candidatos **P20–P40** (20 estudos; P36 era duplicata de P31/LEMAD, removida).

## 🔗 Navegação rápida

| Artefato                                                                                     | Descrição                                                                                                                                         |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📄 [Relatório de síntese (MD)](relatorio-sintese.md) · [PDF](relatorio-sintese.pdf)          | Análise agregada: funil, cobertura por RQ, qualidade, ranking, achados                                                                            |
| 🧮 [Resultados consolidados (CSV)](resultados-consolidados.csv)                              | Matriz machine-readable: RQ1-5, QA1-4, escores, banda, recomendação                                                                               |
| 🖼️ [Galeria de gráficos](graficos.md)                                                        | Os 5 gráficos com leitura                                                                                                                         |
| 📚 [Índice de pareceres](README.md)                                                          | Tabela-síntese por estudo                                                                                                                         |
| 🛠️ [Scripts geradores](scripts/README.md) · [Como criar os gráficos](COMO-CRIAR-GRAFICOS.md) | Regeneração de gráficos e PDF                                                                                                                     |
| 📥 Fontes                                                                                    | [Prompts](../prompts/) · [PDFs dos artigos](../docs/) · [Template do prompt](../prompt-template.md) · [CSV de insumos](../Artigos-TrabalhoII.csv) |

## 📈 Números-chave

| Métrica                               |                                               Valor |
| ------------------------------------- | --------------------------------------------------: |
| Estudos processados                   |                                              **20** |
| Avaliados integralmente               |                                              **18** |
| Inelegíveis na triagem (Qualis A3)    |                                    **2** (P39, P40) |
| **Incluir**                           | **14** (7 plenos · 5 c/ ressalvas · 2 fundacionais) |
| **Excluir** (relevância/tipo/domínio) |                          **4** (P26, P29, P30, P38) |
| SCORE_RQ médio (mediana)              |                                      **3,83** (4,0) |
| SCORE_QA médio (mediana)              |                                     **3,50** (3,75) |
| Banda Alta / Média / Baixa            |                                      **14 / 4 / 0** |
| Lacuna sistemática                    |         **RQ4 (Ética & Desafios)** — só 4/18 plenas |

![Distribuição das recomendações](charts/chart-recommendations.svg)

![Cobertura por RQ](charts/chart-rq-coverage.svg)

## 🗂️ Estudos avaliados (parecer · escores · recomendação)

> Clique no **ID** para abrir o parecer completo. Fontes: [prompt](../prompts/) · [PDF](../docs/).

| ID                   | Estudo                             | Veículo               | SCORE_RQ | SCORE_QA | Banda | Recomendação                 |
| -------------------- | ---------------------------------- | --------------------- | :------: | :------: | ----- | ---------------------------- |
| [P20](review-P20.md) | LLM Agentic Workflow (IaC)         | IEEE Access           |   4.0    |   3.0    | Alta  | Incluir c/ ressalvas         |
| [P21](review-P21.md) | SLM Agent for ICT Ops              | IEEE Access           |   4.5    |   4.0    | Alta  | **Incluir**                  |
| [P22](review-P22.md) | ARM — Autonomous Remediation       | IEEE IoT Journal      |   4.5    |   4.0    | Alta  | **Incluir**                  |
| [P23](review-P23.md) | TAMO (RCA tool-assisted)           | IEEE TSC              |   3.5    |   3.5    | Alta  | Incluir c/ ressalvas         |
| [P24](review-P24.md) | AgentAI Survey                     | Elsevier ESWA         |   4.0    |   2.5    | Média | Incluir c/ ressalvas (fund.) |
| [P25](review-P25.md) | AI-Driven MAS (cyber range)        | Scientific Reports    |   4.5    |   4.0    | Alta  | **Incluir**                  |
| [P26](review-P26.md) | Surveying RCA Techniques           | IEEE TSC              |   2.5    |   2.5    | Média | Excluir                      |
| [P27](review-P27.md) | MA-RCA (multi-agente RCA)          | Complex & Intel. Sys. |   4.5    |   4.0    | Alta  | **Incluir**                  |
| [P28](review-P28.md) | MAS Cybersecurity (LLM)            | IEEE Access           |   4.5    |   3.5    | Alta  | **Incluir**                  |
| [P29](review-P29.md) | AIOps Log Anomaly SLR              | Elsevier ISwA         |   2.5    |   2.5    | Média | Excluir                      |
| [P30](review-P30.md) | LLM Inference Engine RCA           | MDPI BDCC             |   3.0    |   4.0    | Alta  | Excluir                      |
| [P31](review-P31.md) | LEMAD (anomaly detection)          | MDPI Electronics      |   4.5    |   3.5    | Alta  | **Incluir**                  |
| [P32](review-P32.md) | GALR (RCA + recovery)              | MDPI Electronics      |   4.0    |   3.5    | Alta  | Incluir c/ ressalvas         |
| [P33](review-P33.md) | Review of Agentic AI in Cyber      | F1000Research         |   4.0    |   2.5    | Média | Incluir c/ ressalvas (fund.) |
| [P34](review-P34.md) | LLMs in IR management              | Springer IJIS         |   4.0    |   4.0    | Alta  | Incluir c/ ressalvas         |
| [P35](review-P35.md) | Graph-Augmented Multi-Agent RCA    | CMC / Tech Sci. Press |   4.0    |   4.0    | Alta  | **Incluir**                  |
| [P37](review-P37.md) | AI Trust & Framework Readiness     | MDPI Algorithms       |   3.0    |   4.0    | Alta  | Incluir c/ ressalvas         |
| [P38](review-P38.md) | Multi-Agent vs RAG                 | MDPI Electronics      |   3.5    |   4.0    | Alta  | Excluir (domínio)            |
| [P39](review-P39.md) | Agentic AI and the Cyber Arms Race | IEEE Computer         |    —     |    —     | —     | Excluir (inelegível)         |
| [P40](review-P40.md) | LLM-Based Network Mgmt Survey      | Wiley IJNM            |    —     |    —     | —     | Excluir (inelegível)         |

![Aderência por estudo](charts/chart-scores-by-study.svg)

![Mapa SCORE_RQ × SCORE_QA](charts/chart-grid-rq-qa.svg)

## 🧭 Como navegar

- **Quer a visão geral?** → [Relatório de síntese](relatorio-sintese.md) (ou o [PDF](relatorio-sintese.pdf)).
- **Quer um estudo específico?** → clique no ID na tabela acima.
- **Quer os dados crus?** → [CSV consolidado](resultados-consolidados.csv).
- **Quer regenerar gráficos/PDF?** → [scripts](scripts/README.md) + [como criar os gráficos](COMO-CRIAR-GRAFICOS.md).

## 🔬 Conjunto comparativo (ChatGPT)

A pasta `ChatGPT/` (quando presente) contém avaliações paralelas de **P20–P31** geradas com ChatGPT, para **comparação entre avaliadores**. Não fazem parte do corpus oficial de pareceres deste diretório (estes são `review-Pxx.md`).

---

_Hub gerado a partir de [`resultados-consolidados.csv`](resultados-consolidados.csv). Última atualização do lote: 20 estudos (P20–P40)._
