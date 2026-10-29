# Avaliações RSL — Síntese Consolidada (P20–P40)

> 🧭 **Navegação:** [📊 Dashboard](DASHBOARD.md) · [📄 Relatório](relatorio-sintese.md) · [🧮 CSV](resultados-consolidados.csv) · [🖼️ Gráficos](graficos.md) · [🏠 README raiz](../README.md)

Pareceres de revisão dos estudos candidatos da RSL **"Agentic AI Copilot para Resposta a Incidentes"**, produzidos executando o prompt de cada artigo (`../prompts/prompt-Pxx.md`) contra o respectivo PDF (`../docs/`), seguindo as diretrizes de Kitchenham et al. (2009) e a lógica DARE (QA1–QA4).

- **20 estudos avaliados:** P20–P35 e P37–P40.
- **P36 omitido:** duplicata de **P31/LEMAD** (já removida do corpus e do CSV).
- Um arquivo por estudo: [`review-Pxx.md`](.). Cada um traz Tabela A (Bibliométrica/Tab. 3), Tabela B (RQs/Tab. 5), Tabela C (QA/Tab. 7) e parecer final.

> ✅ **Pendência transversal (RESOLVIDA):** durante a avaliação, Citações, SJR e Qualis **não eram verificáveis nos PDFs** e os valores vieram dos **insumos** do CSV (marcados `[VERIFICAR]` nos pareceres). A verificação externa foi concluída em [`../papers.csv`](../papers.csv) — DOI, Qualis 2025-2028, percentil Scopus, SJR quartile, ISSN, ano e **citações em três fontes** (OpenAlex/Crossref/Scopus, 2026-07-27) dos 39 estudos —, confirmando os estratos usados na triagem (incl. P39/P40 = A3, inelegíveis) e o critério **Citações ≥ 1** para todos os incluídos (exceção: P35 com 0 citações, coberto pela `RECENCY_EXCEPTION` de publicação < 12 meses). Fluxo de seleção completo em [`PRISMA.md`](PRISMA.md).

## Tabela-síntese

| ID                   | Estudo (resumo)                    | Veículo               | Tipo / paradigma       | Domínio                     | SCORE_RQ | SCORE_QA | Banda | Recomendação                        |
| -------------------- | ---------------------------------- | --------------------- | ---------------------- | --------------------------- | :------: | :------: | ----- | ----------------------------------- |
| [P20](review-P20.md) | LLM Agentic Workflow (IaC vuln)    | IEEE Access           | LLM+RAG multiagente    | IaC (prevenção)             |   4.0    |   3.0    | Alta  | Incluir c/ ressalvas                |
| [P21](review-P21.md) | SLM Agent for ICT Ops              | IEEE Access           | SLM-agente             | ICT ops / AIOps             |   4.5    |   4.0    | Alta  | **Incluir**                         |
| [P22](review-P22.md) | ARM: Autonomous Remediation        | IEEE IoT Journal      | LLM-agente closed-loop | Remediação IoT/edge         |   4.5    |   4.0    | Alta  | **Incluir**                         |
| [P23](review-P23.md) | TAMO (RCA tool-assisted)           | IEEE TSC              | LLM + tools            | RCA cloud-native            |   3.5    |   3.5    | Alta  | Incluir c/ ressalvas                |
| [P24](review-P24.md) | AgentAI Survey                     | Elsevier ESWA         | Survey agêntico        | Industry 4.0                |   4.0    |   2.5    | Média | Incluir c/ ressalvas (fund.)        |
| [P25](review-P25.md) | AI-Driven MAS (cyber range)        | Scientific Reports    | MAS/RL (não-LLM)       | Cyber range / IR            |   4.5    |   4.0    | Alta  | **Incluir**                         |
| [P26](review-P26.md) | Surveying RCA Techniques           | IEEE TSC              | Survey RCA             | RCA (não-agêntico)          |   2.5    |   2.5    | Média | **Excluir**                         |
| [P27](review-P27.md) | MA-RCA (multi-agente RCA)          | Complex & Intel. Sys. | LLM multi-agente       | RCA                         |   4.5    |   4.0    | Alta  | **Incluir**                         |
| [P28](review-P28.md) | MAS Cybersecurity (LLM)            | IEEE Access           | LLM multi-agente       | SOC / detecção              |   4.5    |   3.5    | Alta  | **Incluir**                         |
| [P29](review-P29.md) | AIOps Log Anomaly SLR              | Elsevier ISwA         | SLR                    | Anomaly det. (não-agêntico) |   2.5    |   2.5    | Média | **Excluir**                         |
| [P30](review-P30.md) | LLM Inference Engine RCA           | MDPI BDCC             | Pipeline LLM           | Bug triage (não-agêntico)   |   3.0    |   4.0    | Alta  | **Excluir**                         |
| [P31](review-P31.md) | LEMAD (anomaly detection)          | MDPI Electronics      | LLM multi-agente       | AIOps rede elétrica         |   4.5    |   3.5    | Alta  | **Incluir**                         |
| [P32](review-P32.md) | GALR (RCA + recovery)              | MDPI Electronics      | GNN + LLM agent        | RCA / recovery              |   4.0    |   3.5    | Alta  | Incluir c/ ressalvas                |
| [P33](review-P33.md) | Review of Agentic AI in Cyber      | F1000Research         | Review agêntico        | Cibersegurança              |   4.0    |   2.5    | Média | Incluir c/ ressalvas (fund.)        |
| [P34](review-P34.md) | LLMs in IR management              | Springer IJIS         | LLM copilot            | IR (NIST 800-61)            |   4.0    |   4.0    | Alta  | Incluir c/ ressalvas                |
| [P35](review-P35.md) | Graph-Augmented Multi-Agent RCA    | CMC / Tech Sci. Press | LLM multi-agente       | RCA AIOps                   |   4.0    |   4.0    | Alta  | **Incluir**                         |
| [P37](review-P37.md) | AI Trust & Framework Readiness     | MDPI Algorithms       | Survey de percepção    | IR (adoção/governança)      |   3.0    |   4.0    | Alta  | Incluir c/ ressalvas                |
| [P38](review-P38.md) | Multi-Agent vs RAG                 | MDPI Electronics      | Multi-agente vs RAG    | Agricultura                 |   3.5    |   4.0    | Alta  | **Excluir (domínio)**               |
| [P39](review-P39.md) | Agentic AI and the Cyber Arms Race | IEEE Computer         | Opinião/perspectiva    | Cibersegurança              |    —     |    —     | —     | **Excluir (INELEGÍVEL: Qualis A3)** |
| [P40](review-P40.md) | LLM-Based Network Mgmt Survey      | Wiley IJNM            | Survey                 | Gestão de redes             |    —     |    —     | —     | **Excluir (INELEGÍVEL: Qualis A3)** |

## Balanço

- ✅ **Incluir — 14:** P20, P21, P22, P23, P24, P25, P27, P28, P31, P32, P33, P34, P35, P37
  - _Plenos, sem ressalva explícita (7):_ P21, P22, P25, P27, P28, P31, P35 — agênticos e próximos de IR/AIOps/SOC.
  - _Com ressalvas (5):_ P20 (escopo prevenção), P23 (agêntico limitado), P32 (recuperação avaliada offline), P34 (copilot não-agêntico, mas IR puro), P37 (survey de percepção, não é sistema).
  - _Fundacionais — secundários, condicionais ao protocolo (2):_ P24, P33 — revisões **de** Agentic AI; úteis para fundamentação (RQ1/RQ4/RQ5), a citar se o protocolo admitir estudos secundários.
- ❌ **Excluir por relevância/tipo — 4:** P26, P29 (secundários não-agênticos), P30 (não-agêntico, bug-triage), P38 (off-domain: agricultura).
- ⛔ **Inelegíveis na triagem (ETAPA 1) — 2:** P39, P40 (**Qualis A3** < A1–A2).

_Total: 14 + 4 + 2 = 20 estudos. Se o protocolo restringir o corpus a estudos primários, os 2 fundacionais (P24, P33) migram para fundamentação, resultando em **12 incluídos no corpus primário**._

## Avaliações comparativas (ChatGPT e Gemini)

**Ciclo 2 (adicionadas em 2026-10-25):** os 22 estudos aprovados na triagem (P43–P88) foram avaliados em paralelo pelo **ChatGPT** ([`ChatGPT/`](ChatGPT/)) e pelo **Gemini** ([`Gemini/`](Gemini/)) — nova pasta com P20–P88 completos —, executando os mesmos prompts (`../prompts/prompt-PNN.md`) contra os PDFs. _Nota: o arquivo do ChatGPT para P85 chegou nomeado `P84_avaliacao_RSL.md` e foi renomeado conforme o conteúdo (avaliação do P85; P84 foi excluído na triagem e não possui avaliação)._

**Consolidados por avaliador — P01–P88 (2026-10-26):** com os três conjuntos completos (61 avaliações por avaliador: 19 fundacionais retroativos + 20 do ciclo 1 + 22 do ciclo 2), cada fonte tem seu CSV consolidado de 61 linhas: [`resultados-consolidados-claude-P01-P88.csv`](resultados-consolidados-claude-P01-P88.csv) (merge dos três CSVs oficiais, 23 colunas + Conjunto) · [`resultados-consolidados-chatgpt-P01-P88.csv`](resultados-consolidados-chatgpt-P01-P88.csv) · [`resultados-consolidados-gemini-P01-P88.csv`](resultados-consolidados-gemini-P01-P88.csv) (escores extraídos dos arquivos dos avaliadores; `NA` onde o ChatGPT parou na triagem por estrato; bandas derivadas do SCORE_QA pela rubrica). Os CSVs por conjunto permanecem como registros históricos.

**Comparação GLOBAL (P01–P88, três avaliadores, 2026-10-26):** [`comparacao-avaliadores-global.md`](comparacao-avaliadores-global.md) — acordo 90,2–91,8% por par (κ 0,51–0,57; Fleiss 0,53), **53/61 decisões unânimes** (19/19 nos fundacionais; exclusões unânimes: P30, P39, P86); as **8 divergências formam 3 famílias protocolares** (secundários não-agênticos; emenda de estratos; fronteiras de domínio/estrato) — nenhuma de mérito · dados em [`comparacao-avaliadores-global.csv`](comparacao-avaliadores-global.csv).

**Comparação do ciclo 2 (três avaliadores):** [`comparacao-avaliadores-ciclo2.md`](comparacao-avaliadores-ciclo2.md) — acordo de decisão 81,8–95,5% por par (Claude×Gemini κ = 0,65; Fleiss κ = 0,36 sob paradoxo da prevalência); **as 4 divergências são todas protocolares** (3 = aplicação da emenda de estratos pelo ChatGPT; 1 = destino do cluster de carga cognitiva em P85), nenhuma de mérito · dados em [`comparacao-avaliadores-ciclo2.csv`](comparacao-avaliadores-ciclo2.csv).

Avaliações paralelas dos mesmos 20 estudos produzidas com **ChatGPT** (conjunto separado dos pareceres oficiais), usadas na [comparação entre avaliadores](comparacao-avaliadores.md) (concordância 90%, κ = 0,74). Um arquivo por estudo em [`ChatGPT/`](ChatGPT/):

[P20](ChatGPT/P20_avaliacao_RSL.md) · [P21](ChatGPT/P21_avaliacao_RSL.md) · [P22](ChatGPT/P22_avaliacao_RSL.md) · [P23](ChatGPT/P23_avaliacao_RSL.md) · [P24](ChatGPT/P24_avaliacao_RSL.md) · [P25](ChatGPT/P25_avaliacao_RSL.md) · [P26](ChatGPT/P26_avaliacao_RSL.md) · [P27](ChatGPT/P27_avaliacao_RSL.md) · [P28](ChatGPT/P28_avaliacao_RSL.md) · [P29](ChatGPT/P29_avaliacao_RSL.md) · [P30](ChatGPT/P30_avaliacao_RSL.md) · [P31](ChatGPT/P31_avaliacao_RSL.md) · [P32](ChatGPT/P32_avaliacao_RSL.md) · [P33](ChatGPT/P33_avaliacao_RSL.md) · [P34](ChatGPT/P34_avaliacao_RSL.md) · [P35](ChatGPT/P35_avaliacao_RSL.md) · [P37](ChatGPT/P37_avaliacao_RSL.md) · [P38](ChatGPT/P38_avaliacao_RSL.md) · [P39](ChatGPT/P39_avaliacao_RSL.md) · [P40](ChatGPT/P40_avaliacao_RSL.md)

## Corpus fundacional — avaliação retroativa (2026-10-26)

Os **19 estudos fundacionais** do Trabalho I (P01–P19) receberam avaliação **retroativa de padronização** (prompts [`prompt-P01…P19.md`](../prompts/); inclusão herdada, **não rediscutida** — mede-se apenas RQs/QA para tornar as Tabelas 3/5/7 comparáveis com P20–P88). Bibliometria da Tabela A verificada nas três fontes ([`../papers.csv`](../papers.csv), 2026-07-27). Estatística: SCORE_RQ médio **3,66** (mediana 4,0) · SCORE_QA médio **2,53** (mediana 2,5) · bandas **9 Alta / 10 Média** — RQ alto e QA mais baixo que P20–P40, coerente com o perfil de surveys conceituais dos fundacionais.

> Consolidação: [`resultados-consolidados-fundacionais.csv`](resultados-consolidados-fundacionais.csv) (19 × 23 colunas, símbolos RQ/QA extraídos dos pareceres e conferidos contra os escores) · [`graficos-fundacionais.md`](graficos-fundacionais.md) (5 SVGs em `charts-fundacionais/`).

| ID                   | Estudo (resumo)                          | SCORE_RQ | SCORE_QA | Banda | Status                |
| -------------------- | ---------------------------------------- | :------: | :------: | ----- | --------------------- |
| [P01](review-P01.md) | Trustworthy Agentic AI Systems           |   4.5    |   2.5    | Média | Mantido (fundacional) |
| [P02](review-P02.md) | Agentic AI Smart Future (SLR)            |   4.5    |   1.5    | Média | Mantido (fundacional) |
| [P03](review-P03.md) | Research Landscape Agentic AI & LLMs     |   4.0    |   3.0    | Alta  | Mantido (fundacional) |
| [P04](review-P04.md) | LLM-Based MAS for SE                     |   4.5    |   3.5    | Alta  | Mantido (fundacional) |
| [P05](review-P05.md) | AIOps in the Era of LLMs                 |   3.5    |   3.5    | Alta  | Mantido (fundacional) |
| [P06](review-P06.md) | Agentic AI Comprehensive Survey          |   4.0    |   1.5    | Média | Mantido (fundacional) |
| [P07](review-P07.md) | Artificial Empathy in MAS                |   2.0    |   3.0    | Alta  | Mantido (fundacional) |
| [P08](review-P08.md) | Human-in-the-Loop Learning               |   3.5    |   1.5    | Média | Mantido (fundacional) |
| [P09](review-P09.md) | AI Agents vs. Agentic AI                 |   4.5    |   2.5    | Média | Mantido (fundacional) |
| [P10](review-P10.md) | Agentic AI: Autonomous Intelligence      |   4.5    |   1.5    | Média | Mantido (fundacional) |
| [P11](review-P11.md) | Co-Evolving Multi-Agent RL               |   2.5    |   3.5    | Alta  | Mantido (fundacional) |
| [P12](review-P12.md) | Autonomous System Security w/ GenAI      |   3.5    |   2.0    | Média | Mantido (fundacional) |
| [P13](review-P13.md) | Retail Resilience Engine                 |   4.0    |   3.5    | Alta  | Mantido (fundacional) |
| [P14](review-P14.md) | Transforming Cybersecurity w/ Agentic AI |   4.0    |   1.5    | Média | Mantido (fundacional) |
| [P15](review-P15.md) | The Rise of Agentic AI                   |   4.5    |   2.0    | Média | Mantido (fundacional) |
| [P16](review-P16.md) | MLOps and AIOps Survey                   |   3.0    |   3.5    | Alta  | Mantido (fundacional) |
| [P17](review-P17.md) | Trustworthy & Explainable AI (XAI)       |   3.5    |   1.5    | Média | Mantido (fundacional) |
| [P18](review-P18.md) | Model-Based Automation in DevOps         |   2.0    |   3.5    | Alta  | Mantido (fundacional) |
| [P19](review-P19.md) | Agent System Mining                      |   3.0    |   3.0    | Alta  | Mantido (fundacional) |

## Ciclo 2 (concluído em 2026-09-10)

> Consolidação: [`resultados-consolidados-ciclo2.csv`](resultados-consolidados-ciclo2.csv) · [`graficos-ciclo2.md`](graficos-ciclo2.md) · fluxo PRISMA do ciclo 2 em [`PRISMA.md`](PRISMA.md) · painel em [`DASHBOARD.md`](DASHBOARD.md) · **[síntese consolidada dos 2 ciclos](relatorio-sintese-consolidado.md)** ([PDF](relatorio-sintese-consolidado.pdf)).

- [`triagem-ciclo2.md`](triagem-ciclo2.md) — **triagem PRISMA dos candidatos P41–P89** (2026-09-09), com evidência da extração PICOC de leitura integral: 49 triados → **22 aprovados para avaliação integral** (4 com ressalva de estrato, por emenda de protocolo) · 27 excluídos (E2 = 19 · E3 = 8). Elegibilidade bibliométrica em [`../papers-ciclo2.csv`](../papers-ciclo2.csv).
- [`triagem-ciclo3.md`](triagem-ciclo3.md) — **triagem PRISMA do ciclo 3** (2026-10-28), com evidência da extração PICOC ([`../picoc/picoc-results-ciclo3.md`](../picoc/picoc-results-ciclo3.md)): 19 elegíveis → 5 adiados (texto integral não obtido, Springer) → 14 triados → 1 excluído (E3: P108) → **13 aprovados para avaliação integral** (2 plenos + 11 com ressalva de estrato, PDR-0006/0007). Elegibilidade bibliométrica em [`../papers-ciclo3.csv`](../papers-ciclo3.csv); fluxo do ciclo em [`PRISMA.md`](PRISMA.md).
- **Prompts de avaliação do ciclo 2** — 22 prompts preenchidos (`../prompts/prompt-P43.md` … `prompt-P88.md`) gerados do [template](../prompts/prompt-chatgpt-consultation.md) com INSUMOS do [`../papers-ciclo2.csv`](../papers-ciclo2.csv) (Qualis derivado do percentil) e a linha `ressalvas_triagem` transcrevendo as flags da triagem (incl. as 4 ressalvas de estrato).
- **Pareceres do ciclo 2** (2026-09-10) — um `review-Pxx.md` por estudo, mesmo formato do ciclo 1 (Tabelas A/B/C + parecer). Resultado: **20 Incluir c/ ressalvas · 2 Excluir**:

| ID                   | Estudo (resumo)                      | SCORE_RQ | SCORE_QA | Banda | Recomendação                                        |
| -------------------- | ------------------------------------ | :------: | :------: | ----- | --------------------------------------------------- |
| [P43](review-P43.md) | Agentic AIOps framework              |   3.0    |   2.0    | Média | Incluir c/ ressalvas (sem evidência empírica)       |
| [P52](review-P52.md) | LLMs in Cybersecurity (SLR)          |   3.5    |   2.5    | Média | Incluir c/ ressalvas (fundacional)                  |
| [P53](review-P53.md) | LLM + Bayesian nets RCA cloud-native |   3.5    |   3.0    | Alta  | Incluir c/ ressalvas                                |
| [P54](review-P54.md) | LLM Reasoning → AI Agents (review)   |   4.5    |   2.0    | Média | Incluir c/ ressalvas (fundacional)                  |
| [P55](review-P55.md) | Telemetry & Agentic AI (óptica)      |   4.5    |   2.5    | Média | Incluir c/ ressalvas (mapeamento)                   |
| [P62](review-P62.md) | Neuroergonomics mental workload      |   2.0    |   1.5    | Média | Incluir c/ ressalvas ⚠️ estrato A3 · cognitive load |
| [P63](review-P63.md) | Chatbot Usability Scale (BUS-15)     |   2.0    |   3.5    | Alta  | Incluir c/ ressalvas (instrumento)                  |
| [P69](review-P69.md) | WAUC mental workload database        |   1.0    |   3.5    | Alta  | Incluir c/ ressalvas ⚠️ estrato A3 · cognitive load |
| [P72](review-P72.md) | LLMs Vulnerability → Defense         |   3.5    |   1.5    | Média | Incluir c/ ressalvas (fundacional)                  |
| [P73](review-P73.md) | Alert fatigue AI-assisted SIEM       |   3.5    |   4.0    | Alta  | Incluir c/ ressalvas (agência limitada)             |
| [P74](review-P74.md) | MLOps → LLMOps (review)              |   3.0    |   1.0    | Baixa | Incluir c/ ressalvas (fonte conceitual LLMOps)      |
| [P76](review-P76.md) | SOC hyper-automation Agentic AI      |   4.0    |   2.5    | Média | Incluir c/ ressalvas (PoC; MTTR vs. literatura)     |
| [P77](review-P77.md) | GenAI in cybersecurity (review)      |   3.5    |   1.5    | Média | Incluir c/ ressalvas (fundacional)                  |
| [P78](review-P78.md) | RAG + LLM incident timeline          |   4.0    |   3.5    | Alta  | Incluir c/ ressalvas                                |
| [P79](review-P79.md) | AI-Augmented SOC survey              |   5.0    |   3.0    | Alta  | Incluir c/ ressalvas (fundacional)                  |
| [P81](review-P81.md) | Control room operator DSS            |   3.0    |   3.5    | Alta  | Incluir c/ ressalvas ⚠️ estrato A4 · HITL/decisão   |
| [P82](review-P82.md) | AI Agent predictive maintenance      |   3.5    |   2.5    | Média | Incluir c/ ressalvas (conceitual; domínio)          |
| [P83](review-P83.md) | Wazuh RAG copilot SOC                |   3.5    |   2.5    | Média | Incluir c/ ressalvas                                |
| [P85](review-P85.md) | Fadiga operadores VTS                |   0.5    |   3.5    | Alta  | **Excluir** (sem aderência às RQs)                  |
| [P86](review-P86.md) | Distributed tracing rule-induction   |   2.0    |   3.0    | Alta  | **Excluir** ⚠️ estrato B1+Q3 · não-agêntico         |
| [P87](review-P87.md) | LLM agentic incident-report (rede)   |   3.5    |   3.5    | Alta  | Incluir c/ ressalvas                                |
| [P88](review-P88.md) | MAS self-healing descentralizado     |   3.0    |   4.0    | Alta  | Incluir c/ ressalvas (não-LLM, análogo P25)         |

## Ciclo 3 — avaliação integral (Claude 2026-10-28; tripla concluída 2026-10-29)

**Pareceres do avaliador Claude — 13 arquivos** (`review-P91.md`, `review-P93.md`,
`review-P94.md`, `review-P97.md`, `review-P100.md`, `review-P101.md`,
`review-P102.md`, `review-P106.md`, `review-P110.md`, `review-P112.md`,
`review-P119.md`, `review-P121.md`, `review-P123.md`), no formato canônico
[`templates/review.md`](../templates/review.md), a partir dos prompts
imutáveis de [`../prompts/`](../prompts/README.md) (template v1.1.0, emendas
PDR-0006/0007 no texto normativo). Resultado Claude: **1 Incluir** (P94) ·
**11 Incluir c/ ressalvas** · **1 Excluir** (P106, E2 — agência nominal,
confirmando a flag da [triagem](triagem-ciclo3.md)). Scores: RQ 2.0–5.0;
QA 1.0–3.5 (9 banda Alta · 3 Média · 1 Baixa — contagem conferida no
[CSV consolidado](resultados-consolidados-ciclo3.csv), fonte de verdade).

**Consolidação parcial (2026-10-28):** [`resultados-consolidados-ciclo3.csv`](resultados-consolidados-ciclo3.csv)
(fonte de verdade, 13 linhas) · [`graficos-ciclo3.md`](graficos-ciclo3.md)
(SVGs em [`charts-ciclo3/`](charts-ciclo3/README.md)) · seção do ciclo 3 no
[`DASHBOARD.md`](DASHBOARD.md) · adendo nº 4 na
[síntese consolidada](relatorio-sintese-consolidado.md) (PDF regenerado).
Estatísticas Claude: RQ média 3,85/mediana 4,0 · QA média 2,77/mediana 3,0.

> ✅ **Avaliação tripla concluída (2026-10-29):** pareceres **ChatGPT** e
> **Gemini** dos 13 estudos recebidos em `ChatGPT/PXX_avaliacao_RSL.md` e
> `Gemini/PXX_avaliacao_RSL.md` (artefatos de terceiros — imutáveis, Art. VI).
> No colapso Incluir/Excluir os três avaliadores são **unânimes nos 13**
> (12 Incluir · 1 Excluir — P106, E2); escores dos três no
> [`Papers_Index`](../Papers_Index.md), resumo no [dashboard](DASHBOARD.md) e
> adendo nº 5 na [síntese consolidada](relatorio-sintese-consolidado.md).
> Restam a comparação entre avaliadores (Etapa 8) e as fichas (Etapa 9).

## Padrões e observações para a síntese

- **Eixo organizador = agêntico × domínio-IR.** Incluídos são agênticos **e** aderentes a IR/AIOps/SOC; exclusões recaem em não-agênticos (P26/P29/P30), off-domain (P38) ou inelegíveis (P39/P40).
- **Forte aderência a IR/segurança:** P25 (cyber range), P28 (SOC), P34 (copilot IR), P37 (governança/adoção).
- **Paradigmas de agente distintos** (registrar no mapeamento): LLM multi-agente (P27/P28/P31/P35), LLM-agente closed-loop (P22), SLM-agente (P21), GNN+LLM (P23/P32), **MAS/RL não-LLM** (P25), **copilot/baixa autonomia** (P34), **survey de percepção** (P37).
- **Procedência recorrente State Grid (China):** P31, P32, P35 — atentar para independência dos estudos.
- **Critério "Citações ≥ 1" — verificado (2026-07-27):** dos estudos de 2026 em risco, P30 (máx. 1), P32 (1) e P37 (5) satisfazem o critério; **P35 tem 0 citações** nas três fontes (OpenAlex/Crossref/Scopus) e permanece elegível pela `RECENCY_EXCEPTION` (< 12 meses). Contagens em [`../papers.csv`](../papers.csv).

---

_Gerado a partir dos pareceres individuais em `reviews/`. Para detalhes (evidências por RQ, âncoras de QA, pendências), ver cada `review-Pxx.md`._
