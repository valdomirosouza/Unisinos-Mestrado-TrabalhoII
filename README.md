# RSL — Agentic AI Copilot para Resposta a Incidentes

Repositório da **Revisão Sistemática da Literatura (RSL)** do Trabalho II (PPGCA · Unisinos), seguindo as diretrizes de **Kitchenham et al. (2009)** e a lógica **DARE (QA1–QA4)**. Reúne os estudos candidatos **P20–P40**, os prompts de avaliação, os pareceres do revisor e a síntese dos resultados (dados, gráficos e relatório).

> ⚠️ **Repositório privado.** Contém PDFs de artigos com direitos autorais (IEEE, Elsevier, Springer, MDPI, Wiley, etc.) em `docs/`, mantidos apenas para a avaliação acadêmica.
>
> ⚠️ **Pendência transversal:** Citações, SJR e Qualis **não são verificáveis nos PDFs** — os valores vêm dos insumos e permanecem pendentes de verificação externa (Scimago; Plataforma Sucupira/Qualis CAPES; base indexadora).

## 🚀 Comece por aqui

| Quero…                     | Abra                                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| Uma visão geral interativa | 📊 **[Dashboard de resultados](reviews/DASHBOARD.md)**                                         |
| A análise completa         | 📄 [Relatório de síntese](reviews/relatorio-sintese.md) · [PDF](reviews/relatorio-sintese.pdf) |
| Os dados crus              | 🧮 [Resultados consolidados (CSV)](reviews/resultados-consolidados.csv)                        |
| Os gráficos                | 🖼️ [Galeria](reviews/graficos.md) · [como criá-los](reviews/COMO-CRIAR-GRAFICOS.md)            |
| Um estudo específico       | 📚 [Índice de pareceres](reviews/README.md) ou a tabela abaixo                                 |

## 📈 Resultado em um relance

20 estudos · **18 avaliados** + **2 inelegíveis** (Qualis A3) · **14 Incluir** · **4 Excluir** · SCORE_RQ médio **3,83** · SCORE_QA médio **3,50** · **14 em Banda Alta** · lacuna sistemática em **RQ4 (Ética & Desafios)**.

![Distribuição das recomendações](reviews/charts/chart-recommendations.svg)

## 🗂️ Índice de estudos (P20–P40)

> P36 era duplicata de P31/LEMAD e foi removido do corpus.

| ID  | Estudo                           | Parecer                          | Prompt                          | PDF                                                                                                                                                                       | Recom.                                |
| --- | -------------------------------- | -------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| P20 | LLM Agentic Workflow (IaC)       | [parecer](reviews/review-P20.md) | [prompt](prompts/prompt-P20.md) | [PDF](docs/P20-A1-LLM_Agentic_Workflow_for_Automated_Vulnerability_Detection_and_Remediation_in_Infrastructure-as-Code.pdf)                                               | ✅ Incluir c/ ressalvas               |
| P21 | SLM Agent for ICT Ops            | [parecer](reviews/review-P21.md) | [prompt](prompts/prompt-P21.md) | [PDF](docs/P21-A1-Small_Language_Model_Agent_for_the_Operations_of_Continuously_Updating_ICT_Systems.pdf)                                                                 | ✅ Incluir                            |
| P22 | ARM — Autonomous Remediation     | [parecer](reviews/review-P22.md) | [prompt](prompts/prompt-P22.md) | [PDF](docs/P22-A1-ARM_Autonomous_Remediation_and_Management_With_LLM_Agents_for_Intent-Driven_Control.pdf)                                                                | ✅ Incluir                            |
| P23 | TAMO (RCA tool-assisted)         | [parecer](reviews/review-P23.md) | [prompt](prompts/prompt-P23.md) | [PDF](docs/P23-A1-TAMOFine-Grained_Root_Cause_Analysis_via_Tool-Assisted_LLM_Agent_With_Multi-Modality_Observation_Data_in_Cloud-Native_Systems.pdf)                      | ✅ Incluir c/ ressalvas               |
| P24 | AgentAI Survey                   | [parecer](reviews/review-P24.md) | [prompt](prompts/prompt-P24.md) | [PDF](docs/P24-A1-1-s2.0-S0957417425020238-main.pdf)                                                                                                                      | ✅ Incluir c/ ressalvas (fundacional) |
| P25 | AI-Driven MAS (cyber range)      | [parecer](reviews/review-P25.md) | [prompt](prompts/prompt-P25.md) | [PDF](docs/P25-A1-s41598-026-45937-9.pdf)                                                                                                                                 | ✅ Incluir                            |
| P26 | Surveying RCA Techniques         | [parecer](reviews/review-P26.md) | [prompt](prompts/prompt-P26.md) | [PDF](docs/P26-A1-Surveying_Root_Cause_Analysis_Techniques_A_Comprehensive_Review_of_Aspects_for_Multi-Service_Applications.pdf)                                          | ❌ Excluir (relevância/tipo)          |
| P27 | MA-RCA (multi-agente RCA)        | [parecer](reviews/review-P27.md) | [prompt](prompts/prompt-P27.md) | [PDF](docs/P27-A1-s40747-025-02096-0.pdf)                                                                                                                                 | ✅ Incluir                            |
| P28 | MAS Cybersecurity (LLM)          | [parecer](reviews/review-P28.md) | [prompt](prompts/prompt-P28.md) | [PDF](docs/P28-A1-A_Multi-Agent_System_for_Cybersecurity_Threat_Detection_and_Correlation_Using_Large_Language_Models.pdf)                                                | ✅ Incluir                            |
| P29 | AIOps Log Anomaly SLR            | [parecer](reviews/review-P29.md) | [prompt](prompts/prompt-P29.md) | [PDF](docs/P29-A2-1-s2.0-S2667305325001346-main.pdf)                                                                                                                      | ❌ Excluir (relevância/tipo)          |
| P30 | LLM Inference Engine RCA         | [parecer](reviews/review-P30.md) | [prompt](prompts/prompt-P30.md) | [PDF](docs/P30-A2-BDCC-10-00060-v2.pdf)                                                                                                                                   | ❌ Excluir (relevância/tipo)          |
| P31 | LEMAD (anomaly detection)        | [parecer](reviews/review-P31.md) | [prompt](prompts/prompt-P31.md) | [PDF](docs/P31-A2-electronics-14-03008.pdf)                                                                                                                               | ✅ Incluir                            |
| P32 | GALR (RCA + recovery)            | [parecer](reviews/review-P32.md) | [prompt](prompts/prompt-P32.md) | [PDF](docs/P32-A2-electronics-15-00243-v2.pdf)                                                                                                                            | ✅ Incluir c/ ressalvas               |
| P33 | Review of Agentic AI in Cyber    | [parecer](reviews/review-P33.md) | [prompt](prompts/prompt-P33.md) | [PDF](docs/P33-A2-64b5f019-bc3d-42da-870b-8f7434e7057c_f1000res169337.pdf)                                                                                                | ✅ Incluir c/ ressalvas (fundacional) |
| P34 | LLMs in IR management            | [parecer](reviews/review-P34.md) | [prompt](prompts/prompt-P34.md) | [PDF](docs/P34-A2-s10207-025-01144-7.pdf)                                                                                                                                 | ✅ Incluir c/ ressalvas               |
| P35 | Graph-Augmented Multi-Agent RCA  | [parecer](reviews/review-P35.md) | [prompt](prompts/prompt-P35.md) | [PDF](docs/P35-A2-TSP_CMC_77908.pdf)                                                                                                                                      | ✅ Incluir                            |
| P37 | AI Trust & Framework Readiness   | [parecer](reviews/review-P37.md) | [prompt](prompts/prompt-P37.md) | [PDF](docs/P37-A2-algorithms-19-00062-v2.pdf)                                                                                                                             | ✅ Incluir c/ ressalvas               |
| P38 | Multi-Agent vs RAG               | [parecer](reviews/review-P38.md) | [prompt](prompts/prompt-P38.md) | [PDF](docs/P38-A2-electronics-14-04883-v2.pdf)                                                                                                                            | ❌ Excluir (domínio)                  |
| P39 | Agentic AI & the Cyber Arms Race | [parecer](reviews/review-P39.md) | [prompt](prompts/prompt-P39.md) | [PDF](docs/P39-A3-Agentic_AI_and_the_Cyber_Arms_Race.pdf)                                                                                                                 | ❌ Excluir (Qualis A3)                |
| P40 | LLM-Based Network Mgmt Survey    | [parecer](reviews/review-P40.md) | [prompt](prompts/prompt-P40.md) | [PDF](docs/P40-A3-Int%20J%20Network%20Mgmt%20-%202025%20-%20Hong%20-%20A%20Comprehensive%20Survey%20on%20LLM%E2%80%90Based%20Network%20Management%20and%20Operations.pdf) | ❌ Excluir (Qualis A3)                |

## 📁 Estrutura do repositório

```
.
├── README.md                     ← este arquivo (índice geral)
├── prompt-template.md            ← template do prompt de avaliação (papel, RQs, QA, saída)
├── Artigos-TrabalhoII.csv        ← insumos: ID, artigo, arquivo, Qualis, SJR
├── research/                     ← Etapa 1: descoberta de candidatos (Gemini/Claude/ChatGPT)
├── prompts/                      ← 20 prompts preenchidos (prompt-P20..P40)
├── docs/                         ← 20 PDFs dos artigos avaliados
└── reviews/                      ← avaliação e síntese
    ├── DASHBOARD.md              ← painel central (hub de tudo)
    ├── README.md                 ← índice/tabela-síntese dos pareceres
    ├── relatorio-sintese.md/.pdf ← análise agregada (com gráficos)
    ├── resultados-consolidados.csv ← matriz de escores (RQ/QA/banda/recomendação)
    ├── graficos.md               ← galeria dos gráficos
    ├── COMO-CRIAR-GRAFICOS.md     ← how-to de geração dos gráficos
    ├── review-P20..P40.md        ← 20 pareceres do revisor
    ├── charts/                   ← 5 gráficos SVG
    ├── scripts/                  ← geradores (gen_charts.py, build_pdf.py)
    └── ChatGPT/                  ← avaliações comparativas (P20–P40, sem P36)
```

## 📚 Documentos por categoria

### Descoberta de candidatos (Etapa 1)

- [`research/`](research/) — **descoberta de artigos candidatos** para ampliar o corpus, executando o mesmo prompt de busca em **Gemini**, **Claude** e **ChatGPT**. Insumos exploratórios (Qualis/SJR/citações majoritariamente `UNVERIFIED`) que originaram os estudos P20–P40. Ver [`research/README.md`](research/README.md).

### Insumos (entrada)

- [`prompt-template.md`](prompt-template.md) — template do prompt (papel, contexto, RQ1–RQ5, QA1–QA4, formato de saída).
- [`Artigos-TrabalhoII.csv`](Artigos-TrabalhoII.csv) — metadados dos estudos (ID, arquivo, Qualis, SJR).
- [`prompts/`](prompts/) — 20 prompts preenchidos, um por estudo.
- [`docs/`](docs/) — 20 PDFs dos artigos.

### Avaliação & síntese (saída)

- [`reviews/DASHBOARD.md`](reviews/DASHBOARD.md) — **painel central**.
- [`reviews/relatorio-sintese.md`](reviews/relatorio-sintese.md) / [`.pdf`](reviews/relatorio-sintese.pdf) — relatório de síntese.
- [`reviews/resultados-consolidados.csv`](reviews/resultados-consolidados.csv) — dados consolidados.
- [`reviews/README.md`](reviews/README.md) — índice dos pareceres.
- [`reviews/graficos.md`](reviews/graficos.md) — galeria · [`reviews/charts/`](reviews/charts/) — SVGs.
- [`reviews/review-P20.md` … `review-P40.md`](reviews/) — 20 pareceres.

### Ferramentas

- [`reviews/scripts/`](reviews/scripts/) — geradores ([`gen_charts.py`](reviews/scripts/gen_charts.py), [`build_pdf.py`](reviews/scripts/build_pdf.py)) + [README](reviews/scripts/README.md).
- [`reviews/COMO-CRIAR-GRAFICOS.md`](reviews/COMO-CRIAR-GRAFICOS.md) — how-to dos gráficos.

### Comparação

- [`reviews/ChatGPT/`](reviews/ChatGPT/) — avaliações paralelas dos 20 estudos (P20–P40, sem P36) com ChatGPT, para comparação entre avaliadores. _(Conjunto separado dos pareceres oficiais `review-Pxx.md`.)_
- [`reviews/comparacao-avaliadores.md`](reviews/comparacao-avaliadores.md) — **comparação Claude × ChatGPT** (concordância de decisão 90%, κ = 0,74) · dados em [`reviews/comparacao-avaliadores.csv`](reviews/comparacao-avaliadores.csv).

## 🔁 Reproduzir

```bash
python3 reviews/scripts/gen_charts.py   # CSV → gráficos SVG
python3 reviews/scripts/build_pdf.py    # relatório + SVGs → PDF
```

Detalhes em [`reviews/scripts/README.md`](reviews/scripts/README.md) e [`reviews/COMO-CRIAR-GRAFICOS.md`](reviews/COMO-CRIAR-GRAFICOS.md).

## 🧭 Metodologia (resumo)

**Etapa 1 — Descoberta:** o [prompt de busca](research/prompt.md) é executado em três assistentes (Gemini, Claude, ChatGPT) para levantar candidatos que estendam o corpus P1–P19; os resultados ficam em [`research/`](research/) e, após triagem e verificação, originam os estudos P20–P40.

**Etapa 2 — Avaliação:** para cada estudo: o [template](prompt-template.md) é preenchido com os insumos → o prompt é executado contra o PDF → o revisor produz **3 tabelas** (Bibliométrica, Classificação das RQs, Avaliação de Qualidade) e um **parecer** (Incluir / Incluir com ressalvas / Excluir). Os escores alimentam o [CSV consolidado](reviews/resultados-consolidados.csv), que origina os [gráficos](reviews/graficos.md) e o [relatório de síntese](reviews/relatorio-sintese.md).
