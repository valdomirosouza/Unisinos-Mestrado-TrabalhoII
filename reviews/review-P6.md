# Avaliação RSL — Estudo P6

**Artigo:** _Agentic AI: A Comprehensive Survey of Technologies, Applications, and Societal Implications_ — A. K. Pati (Siksha 'O' Anusandhan Deemed to be University, Bhubaneswar, Índia)
**Arquivo:** P6-A1 - Agentic AI A Comprehensive Survey of Technologies Applications and Societal Implications.pdf (14 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                       | DOI                         |
| --- | ----------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------- | --------------------------- |
| P6  | _IEEE Access_ (Vol. 13) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Survey / revisão narrativa | 10.1109/ACCESS.2025.3585609 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2025.3585609; recebido 01/06/2025, aceito 30/06/2025, publicado 03/07/2025; "VOLUME 13, 2025"; licença CC-BY). Autor único (Ashis Kumar Pati). Revisão narrativa: possui seção "Literature Survey" (§II) e comparação com trabalhos existentes (Tab. 3, codificação BC/ID/ND), mas **sem protocolo sistemático** (sem bases, string de busca ou critérios de inclusão/exclusão). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                           | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)        | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                           |
| --- | -------------------------------- | ---------------------------- | ----------------------- | ------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P6  | Agentic AI: Comprehensive Survey | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §I, §III (p.1–5)              | Define autonomia/proatividade e distingue de IA tradicional e de "AI agents" (a); tríade núcleo autonomia/adaptabilidade/goal-directedness + modelo de 4 fases (coleta→decisão→aprendizado→colaboração) + tipos de agentes reflex/model/goal/utility/learning/meta-reasoning (b); modelos de decisão via BDI/SOAR/ACT-R e utilidade (c).                                     |
| P6  | "                                | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §IV (p.6–7)                   | Arquiteturas single/multi-agente/swarm/human-AI e frameworks BDI/SOAR/ACT-R (a); tecnologias/ferramentas — LangGraph/AutoGen/OpenAI Swarm, JADE, ACO/PSO, Unity ML, OpenAI Gym, Mesa, knowledge graphs, STRIPS/HTN (b); capacidades avançadas — memória (ACT-R), neurossimbólico, XAI, planejamento (c). Orquestração/guardrails "em produção" tratados de forma conceitual. |
| P6  | "                                | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §I, §IV.B.3, §V (p.2, 6, 7–9) | Benefícios qualitativos amplos (produtividade, custo, experiência, decisão, colaboração) (a); métrica quantitativa apenas **secundária** — −34,2% tempo, +7,7% acurácia, +13,6% utilização (ref [2], ~500 orgs) + lista de métricas de avaliação (b); evidência narrativa/secundária (c). Foco em IR mínimo (breve §IT & Cyber Security).                                    |
| P6  | "                                | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §VI, §VII (p.9–10)            | Desafios técnicos — escalabilidade, interpretabilidade, colaboração humano-AI, ameaças de segurança (a); ético-sociais — viés, accountability, perda de controle, deslocamento de emprego (b); mecanismos — XAI, HITL, audit trail em blockchain, AI Guardians, defesas multicamada, debiasing (c).                                                                          |
| P6  | "                                | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §VII.B (p.10–11)              | Problemas abertos explícitos: agentic AI transparente, agentes neuro-simbólicos, cooperação/negociação multiagente, colaboração humano-AI, arquiteturas energeticamente eficientes, Sim2Real, quantum, robustez adversarial; tendências (swarm, DAOs, AIaaS, XRL, self-explaining AI).                                                                                       |
|     |                                  | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                               | T + T + P + T + T                                                                                                                                                                                                                                                                                                                                                            |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo             | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | -------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P6  | Survey / revisão narrativa | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (campo fragmentado, ausência de recurso unificado sobre agentic AI) e contribuição (síntese abrangente/fonte primária) explícitos (§II, §IX).
- **QA2 = N** — revisão **narrativa sem protocolo sistemático**: sem bases, string de busca, critérios de inclusão/exclusão ou contagens; Tab. 3 apenas compara cobertura de trabalhos (BC/ID/ND). Não replicável.
- **QA3 = N** — **sem validação empírica própria** (nenhum experimento/estudo de caso/simulação do autor); síntese secundária da literatura. Teórico = N.
- **QA4 = P** — conclusões coerentes com o corpo; porém **sem discussão explícita das limitações do próprio survey** (§IX lista contribuições, não limitações).

## Parecer final do revisor

**Síntese.** P6 é um survey de autor único **diretamente sobre agentic AI** (diferente de P4/P5, ligados a SE/AIOps), cobrindo com solidez conceitual definições/tipos/capacidades (**RQ1**), tecnologias e frameworks (**RQ2**), desafios técnicos e ético-sociais (**RQ4**) e problemas abertos/tendências (**RQ5**) — daí o SCORE_RQ alto (4.5/5). É fraco em **RQ3**: benefícios qualitativos, uma única métrica quantitativa secundária e foco mínimo em Resposta a Incidentes. A qualidade metodológica é baixa (QA 1.5): revisão narrativa **sem protocolo sistemático** (QA2=N) e **sem validação empírica** (QA3=N).

**Recomendação: INCLUIR COM RESSALVAS.** Justificativa: forte aderência temática às RQs conceituais/de arquitetura/desafios/lacunas (RQ1/RQ2/RQ4/RQ5) o torna útil como **primer conceitual de agentic AI** (tríade de capacidades, tipos de agentes, frameworks BDI/SOAR/ACT-R, taxonomia de desafios éticos). Ressalvas: (i) metodologia narrativa não-reprodutível (QA2=N) e sem evidência empírica (QA3=N); (ii) não citar seus números de benefício como evidência (secundários); (iii) baixa aderência a IR (RQ3); (iv) survey de autor único em IEEE Access — ponderar peso relativo a P4/P5.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
