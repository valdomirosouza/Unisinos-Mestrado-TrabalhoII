# Avaliação RSL — Estudo P18

**Artigo:** _An architecture for model-based and intelligent automation in DevOps_ — R. Eramo (Univ. Teramo), B. Said (Softeam/Docaposte), M. Oriol (UPC), H. Bruneliere (IMT Atlantique/LS2N), S. Morales (UOC)
**Arquivo:** P18-A1 - An architecture for model-based and intelligent automation in DevOps.pdf (21 páginas)

> ⚖️ **Recomendação: INCLUIR COM RESSALVAS (referência de contexto/precursor operacional).** Artigo primário de alta qualidade (JSS, casos industriais, QA 4.0/4), mas é **arquitetura MDE+AI/ML para DevOps**, não Agentic AI (LLM só de passagem). Domínio operacional adjacente (anomaly detection/RCA/remediation/incident handling). SCORE_RQ 0.5/5.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                       | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                  | DOI                       |
| --- | ------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------- | ------------------------- |
| P18 | _J. of Systems & Software_ (Vol. 217) | 2024 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo primário (arquitetura MDE+AI/ML p/ DevOps + casos industriais) | 10.1016/j.jss.2024.112180 |

_Evidências: cabeçalho p.1 (DOI 10.1016/j.jss.2024.112180; recebido 22/12/2023, aceito 30/07/2024, online 02/08/2024; "The Journal of Systems and Software 217 (2024) 112180"; licença CC-BY). Arquitetura AI-augmented para DevOps (projeto EU AIDOaRt) combinando AI/ML + Model-Driven Engineering, com estudos de caso industriais. LLM citado uma vez, de passagem (§2.1). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                            | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)   | Parecer do revisor                                                                                                                                                                                                                                                                                                                                  |
| --- | ------------------------------------------------- | ---------------------------- | --------------------------- | ------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P18 | Architecture for intelligent automation in DevOps | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §1–2 (p.1–5)             | Trata **DevOps / Continuous SE / MDE + AI/ML / AIOps**. **Não** define Agentic AI; "automação inteligente" é AI-augmented DevOps, não autonomia agêntica. LLM citado **uma vez, de passagem** (§2.1).                                                                                                                                               |
| P18 | "                                                 | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §3 (p.5–11)              | O núcleo é uma **arquitetura MDE+AI/ML para DevOps** (data engineering / core / AI-augmented tool sets; mega-model; padrões de mediação), **não** arquitetura de engenharia de agentic AI (sem agentes LLM, orquestração de agentes, memória agêntica, uso de ferramentas por agentes, guardrails agênticos).                                       |
| P18 | "                                                 | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §3.3, §6 (p.9–11, 14–20) | Capacidades **operacionais aderentes a IR**: AI para monitoramento, **anomaly detection** (séries temporais), **root cause analysis**, **remediation e response automation** ("incident handling, threat mitigation") (a) — avaliadas em **estudos de caso industriais** (§6). Porém entregues por **AI/ML+MDE, não Agentic AI**; domínio é DevOps. |
| P18 | "                                                 | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | §2.2, §7 (p.4–5, 18)     | Desafios são de **integração AI+DevOps/MDE** e ameaças à validade do estudo, não desafios/ética/governança de **Agentic AI**.                                                                                                                                                                                                                       |
| P18 | "                                                 | RQ5 Research Gaps            | Não tem conteúdo suficiente | **N**         | §8, §10 (p.18–20)        | Discussão/futuro tratam de AI-augmented DevOps/MDE — **não** lacunas de agentic AI (benchmarking/threat models/governança/observabilidade/alinhamento agêntico).                                                                                                                                                                                    |
|     |                                                   | **SCORE_RQ**                 |                             | **0.5 / 5.0** |                          | N + N + P + N + N                                                                                                                                                                                                                                                                                                                                   |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                    | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P18 | Artigo primário (arquitetura + casos industriais) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (falta de abordagem holística de AI-augmented DevOps) e contribuição (arquitetura + avaliação) explícitos (§1).
- **QA2 = Y** — replicável: arquitetura detalhada (§3), estratégia de integração (§4), implementação/mega-model (§5), metodologia de avaliação (§6). Veículo SE rigoroso (JSS).
- **QA3 = Y** — **validação empírica por múltiplos estudos de caso industriais** (projeto AIDOaRt) com resultados (§6.3).
- **QA4 = Y** — conclusões coerentes e **§7 Threats to Validity** completa (construct/internal/external/conclusion) — rigor metodológico elevado.

## Parecer final do revisor

**Síntese.** P18 é um **artigo primário de alta qualidade** (QA 4,0/4, banda Alta; JSS, estudos de caso industriais, ameaças à validade) que propõe uma **arquitetura de software AI-augmented para DevOps** combinando AI/ML + Model-Driven Engineering (projeto AIDOaRt). **Não é Agentic AI**: LLM aparece uma única vez, de passagem; não há agentes autônomos, orquestração agêntica, memória ou uso de ferramentas por agentes. Daí SCORE_RQ 0,5/5 — o mais baixo não-zero do corpus — com apenas **RQ3=P** por conter **capacidades operacionais aderentes a IR** (anomaly detection, root cause analysis, **remediation/response automation, incident handling, threat mitigation**) validadas industrialmente. É análogo a **P16 (AIOps)**: domínio operacional adjacente (DevOps/AIOps com tratamento de incidentes), paradigma errado (MDE+AI/ML, não agêntico).

**Recomendação: INCLUIR COM RESSALVAS — como referência de fundamentação/contexto (precursor não-agêntico de automação de IR).** Justificativa: é um **exemplar industrial de arquitetura de automação operacional com RCA/anomaly detection/remediation/incident handling** — baseline valioso de "como se automatiza tratamento de incidentes com IA **antes** dos agentes", útil para **RQ3 (capacidades/benefícios operacionais de IR)** e como **trabalho relacionado** de arquitetura. **Ressalvas fortes:** (i) **NÃO é Agentic AI** (MDE+AI/ML; LLM só de passagem) — usar apenas para RQ3/contexto operacional, **não** para RQ1/RQ2/RQ4/RQ5 (todos N); (ii) domínio é DevOps/continuous SE, IR é um subconjunto das capacidades; (iii) SCORE_RQ 0,5 é muito baixo — peso pequeno na síntese. **Complementaridade:** P16 (AIOps, SLR) e P18 (DevOps, primário) formam o **baseline operacional pré-agêntico** que P5/P14/P15 (LLM/agentic) sucedem.

**Nota de decisão (para o orientando).** Sob critério **estrito "somente Agentic AI"**, P18 seria **EXCLUÍDA por escopo** (SCORE_RQ 0,5; não-agêntica). Recomendo **incluí-la como referência de contexto/precursor operacional** (não como estudo agêntico), dada a qualidade (JSS/A1) e as capacidades de IR (RCA/remediation/incident handling) — decisão a fixar no protocolo, coerente com P16.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_J. Systems & Software_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
