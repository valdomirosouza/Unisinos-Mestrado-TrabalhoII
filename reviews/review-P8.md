# Avaliação RSL — Estudo P8

**Artigo:** _Applications, Challenges, and Future Directions of Human-in-the-Loop Learning_ — S. Kumar, S. Datta, V. Singh, D. Datta, S. K. Singh, R. Sharma (IIT-BHU Varanasi / Digital University Kerala / IIM Sambalpur / Manipal Institute of Technology)
**Arquivo:** P8-A1 - Applications_Challenges_and_Future_Directions_of_Human-in-the-Loop_Learning.pdf (26 páginas)

> ⚠️ **Recomendação: EXCLUIR — não-aderência ao escopo.** Survey de HITL em Machine Learning (active learning, RLHF, XAI); sem Agentic AI (LLM) e sem Resposta a Incidentes. SCORE_RQ 0.0/5; QA 1.5/4.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                    | DOI                         |
| --- | ----------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | --------------------------------------- | --------------------------- |
| P8  | _IEEE Access_ (Vol. 12) | 2024 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Survey / revisão narrativa (HITL em ML) | 10.1109/ACCESS.2024.3401547 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2024.3401547; recebido 28/04/2024, publicado 15/05/2024; "VOLUME 12, 2024"; licença CC-BY). Revisão narrativa de metodologias HITL (active learning, RL a partir de feedback humano, XAI, crowdsourcing). Varredura textual confirmou ausência de "agentic", "incident response", "LLM agent", "copilot". Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                  | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.) | Parecer do revisor                                                                                                                                                                                                                                                                                                                                               |
| --- | --------------------------------------- | ---------------------------- | --------------------------- | ------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P8  | HITL Learning: Apps, Challenges, Future | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §I–II (p.1–5)          | Trata **Human-in-the-Loop em treinamento de ML** (active learning, RLHF, XAI, crowdsourcing). Cobre "supervisão humana", mas no enquadramento de anotação/treino de modelos, **não** como nível de autonomia de Agentic AI; ausentes definição de autonomia agêntica, capacidades núcleo (planejamento/memória/uso de ferramentas) e modelo de decisão agêntico. |
| P8  | "                                       | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §II (p.3–5)            | Frameworks HITL (loop de AL, RL-HITL, XAI) são **pipelines de ML**, não arquitetura de agentic AI: sem orquestração, ferramentas/frameworks agênticos, guardrails ou observabilidade no sentido da RQ.                                                                                                                                                           |
| P8  | "                                       | RQ3 Evidence Benefits        | Não tem conteúdo suficiente | **N**         | §III (p.5–13)          | Benefícios/métricas reportados são de **HITL em ML** (ex.: HCFC +7% desempenho, −35% carga física, −50% carga mental em direção; casos em CV/saúde/NLP), **não** de agentic AI nem de Resposta a Incidentes.                                                                                                                                                     |
| P8  | "                                       | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | §IV (p.13–17)          | Desafios de HITL (fatores humanos, custo, complexidade, viés, privacidade, ética) — relevantes como tema, mas **não** desafios/governança de agentic AI.                                                                                                                                                                                                         |
| P8  | "                                       | RQ5 Research Gaps            | Não tem conteúdo suficiente | **N**         | §V (p.17–20)           | Direções futuras de HITL-ML (granularidade de feedback, capacidade geradora de LLM, timing de intervenção, estudos com usuários) — **não** lacunas de agentic AI (benchmarking/threat models/governança/observabilidade/alinhamento).                                                                                                                            |
|     |                                         | **SCORE_RQ**                 |                             | **0.0 / 5.0** |                        | N + N + N + N + N                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                          | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | --------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P8  | Survey / revisão narrativa (HITL em ML) | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (integrar expertise humana ao ML) e escopo (metodologias/desafios/oportunidades de HITL) explícitos, com 10 perguntas de pesquisa e contribuições listadas (§I).
- **QA2 = N** — revisão **narrativa sem protocolo sistemático** (sem bases, string de busca, critérios de inclusão/exclusão ou contagens). Não replicável.
- **QA3 = N** — **sem validação empírica própria**; síntese secundária (os "case studies" são de terceiros). Teórico/secundário = N.
- **QA4 = P** — conclusões coerentes com o corpo; porém sem discussão explícita das limitações do próprio survey.

## Parecer final do revisor

**Síntese.** P8 é um survey narrativo sobre **Human-in-the-Loop (HITL) em Machine Learning** — active learning, RL a partir de feedback humano, XAI, crowdsourcing — com aplicações em veículos autônomos, visão computacional, saúde e NLP. **Não trata de Agentic AI** (agentes autônomos baseados em LLM, orquestração, uso de ferramentas) **nem de Resposta a Incidentes** (varredura confirmou ausência dos termos agentic/incident/copilot/orquestração agêntica). Nenhuma das cinco RQs é atendida (SCORE_RQ 0.0/5). A qualidade metodológica também é baixa (QA 1.5): revisão narrativa sem protocolo (QA2=N) e sem evidência empírica própria (QA3=N).

**Recomendação: EXCLUIR — por não-aderência ao escopo.** Justificativa: apesar de passar (provisoriamente) na elegibilidade formal, o estudo não contribui para nenhuma RQ da revisão sobre "Agentic AI Copilot para Resposta a Incidentes". **Nuance:** diferentemente de P7 (totalmente alheio), o tema HITL/supervisão humana é conceitualmente adjacente a copilotos agênticos (oversight humano é pilar de agentic AI confiável); assim, P8 poderia, se desejado, servir apenas como **referência de fundamentação sobre HITL/supervisão humana**, mas **não como estudo do corpus** (não aborda agentic AI nem IR e pontua 0 em todas as RQs). Recomenda-se excluir e revisar os critérios de busca (provável casamento por "human-in-the-loop"/"autonomous").

**Pendências de verificação externa:** (registradas por completude; não alteram a exclusão por escopo)

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
