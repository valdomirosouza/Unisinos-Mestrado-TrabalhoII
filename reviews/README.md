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

## Avaliações comparativas (ChatGPT)

Avaliações paralelas dos mesmos 20 estudos produzidas com **ChatGPT** (conjunto separado dos pareceres oficiais), usadas na [comparação entre avaliadores](comparacao-avaliadores.md) (concordância 90%, κ = 0,74). Um arquivo por estudo em [`ChatGPT/`](ChatGPT/):

[P20](ChatGPT/P20_avaliacao_RSL.md) · [P21](ChatGPT/P21_avaliacao_RSL.md) · [P22](ChatGPT/P22_avaliacao_RSL.md) · [P23](ChatGPT/P23_avaliacao_RSL.md) · [P24](ChatGPT/P24_avaliacao_RSL.md) · [P25](ChatGPT/P25_avaliacao_RSL.md) · [P26](ChatGPT/P26_avaliacao_RSL.md) · [P27](ChatGPT/P27_avaliacao_RSL.md) · [P28](ChatGPT/P28_avaliacao_RSL.md) · [P29](ChatGPT/P29_avaliacao_RSL.md) · [P30](ChatGPT/P30_avaliacao_RSL.md) · [P31](ChatGPT/P31_avaliacao_RSL.md) · [P32](ChatGPT/P32_avaliacao_RSL.md) · [P33](ChatGPT/P33_avaliacao_RSL.md) · [P34](ChatGPT/P34_avaliacao_RSL.md) · [P35](ChatGPT/P35_avaliacao_RSL.md) · [P37](ChatGPT/P37_avaliacao_RSL.md) · [P38](ChatGPT/P38_avaliacao_RSL.md) · [P39](ChatGPT/P39_avaliacao_RSL.md) · [P40](ChatGPT/P40_avaliacao_RSL.md)

## Ciclo 2 (em andamento)

- [`triagem-ciclo2.md`](triagem-ciclo2.md) — **triagem PRISMA dos candidatos P41–P89** (2026-09-09), com evidência da extração PICOC de leitura integral: 49 triados → **22 aprovados para avaliação integral** (4 com ressalva de estrato, por emenda de protocolo) · 27 excluídos (E2 = 19 · E3 = 8). Elegibilidade bibliométrica em [`../papers-ciclo2.csv`](../papers-ciclo2.csv).
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

## Padrões e observações para a síntese

- **Eixo organizador = agêntico × domínio-IR.** Incluídos são agênticos **e** aderentes a IR/AIOps/SOC; exclusões recaem em não-agênticos (P26/P29/P30), off-domain (P38) ou inelegíveis (P39/P40).
- **Forte aderência a IR/segurança:** P25 (cyber range), P28 (SOC), P34 (copilot IR), P37 (governança/adoção).
- **Paradigmas de agente distintos** (registrar no mapeamento): LLM multi-agente (P27/P28/P31/P35), LLM-agente closed-loop (P22), SLM-agente (P21), GNN+LLM (P23/P32), **MAS/RL não-LLM** (P25), **copilot/baixa autonomia** (P34), **survey de percepção** (P37).
- **Procedência recorrente State Grid (China):** P31, P32, P35 — atentar para independência dos estudos.
- **Critério "Citações ≥ 1" — verificado (2026-07-27):** dos estudos de 2026 em risco, P30 (máx. 1), P32 (1) e P37 (5) satisfazem o critério; **P35 tem 0 citações** nas três fontes (OpenAlex/Crossref/Scopus) e permanece elegível pela `RECENCY_EXCEPTION` (< 12 meses). Contagens em [`../papers.csv`](../papers.csv).

---

_Gerado a partir dos pareceres individuais em `reviews/`. Para detalhes (evidências por RQ, âncoras de QA, pendências), ver cada `review-Pxx.md`._
