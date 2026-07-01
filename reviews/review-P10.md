# Avaliação RSL — Estudo P10

**Artigo:** _Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey_ — D. B. Acharya (The University of Alabama in Huntsville), K. Kuppan (JPMorgan Chase), B. Divya (Manipal Institute of Technology)
**Arquivo:** P10-A1 - Agentic AI Autonomous Intelligence for Complex Goals - A Comprehensive Survey.pdf (25 páginas)

> ✅ **Recomendação: INCLUIR COM RESSALVAS.** Survey abrangente de Agentic AI (par de P6). Forte em RQ1/RQ2/RQ4/RQ5; fraco em RQ3 (benefícios ilustrativos, IR mínimo). SCORE_RQ 4.5/5; QA 1.5/4 (Média).

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                       | DOI                         |
| --- | ----------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------- | --------------------------- |
| P10 | _IEEE Access_ (Vol. 13) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Survey / revisão narrativa | 10.1109/ACCESS.2025.3532853 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2025.3532853; recebido 01/01/2025, aceito 19/01/2025, publicado 22/01/2025; "VOLUME 13, 2025"; licença CC-BY). Autodeclara "systematic review" nas contribuições (§I.C), mas o corpo é revisão narrativa sem protocolo. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                              | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)     | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | ----------------------------------- | ---------------------------- | ----------------------- | ------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P10 | Agentic AI: Autonomous Intelligence | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §II–III (p.2–5), Tab. 1–2  | Define Agentic AI (autonomia, adaptabilidade, goal-directedness), contrasta com IA tradicional/generativa, agentes clássicos e RL vs. LLM-agents (a); caracteriza autonomia/complexidade de metas, complexidade ambiental, decisão independente/adaptabilidade (b); modelo de decisão goal-directed/adaptativo (c).                                                                                          |
| P10 | "                                   | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §IV (p.6–8), §IX (p.15–17) | Arquiteturas MAS/HRL/modular orientada a metas; paradigmas de aprendizado; **avanços — reasoning & planning, tool use/APIs, memória (episódica/semântica), RAG, instruction fine-tuning** (a); ferramentas/frameworks — OpenAI Gym, Unity ML-Agents, TensorFlow Agents, Rasa (b); guardrails/observabilidade em §IX (safety protocols, fail-safe, monitoring/control, transparency) (c).                     |
| P10 | "                                   | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §VI (p.11–14), Tab. 8–9    | Define métricas (adaptabilidade, eficiência de meta, robustez, escalabilidade, satisfação) e catálogo de benchmarks (MIMIC-III, Yahoo Finance, CARLA, MultiWOZ, NASA); case studies (saúde/finanças/e-commerce/manufatura) (a). Porém **benefícios qualitativos/ilustrativos, sem números empíricos próprios** (b); evidência secundária (c). **IR quase ausente** (cyber só de passagem).                   |
| P10 | "                                   | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §VII–VIII (p.14–16)        | Desafios técnicos — alinhamento de metas, adaptabilidade, restrições de recursos, escalabilidade (a); ético-governança — accountability, viés/justiça/transparência, **privacidade e segurança (ciberataques a sistemas agênticos)**, regulatório/legal (GDPR, "AI responsibility chain") (b); mecanismos — XAI, differential privacy, auditorias, safety protocols, governance frameworks (Tab. 11–12) (c). |
| P10 | "                                   | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §X (p.17–19), Tab. 13      | Lacunas explícitas: adaptabilidade/resiliência (meta/transfer-learning), alinhamento de valores (IRL/CIRL), integração ciber-física, frameworks éticos/padrões globais, avanços teóricos em agência de IA, escalabilidade/eficiência.                                                                                                                                                                        |
|     |                                     | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                            | T + T + P + T + T                                                                                                                                                                                                                                                                                                                                                                                            |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo             | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | -------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P10 | Survey / revisão narrativa | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — objetivos e contribuições explícitos (§I.C: revisão de elementos, técnicas/arquiteturas, aplicações, desafios, ética, direções futuras).
- **QA2 = N** — autodeclara "systematic review", mas **sem protocolo sistemático** (sem bases, string de busca, critérios de inclusão/exclusão, contagens/PRISMA). Revisão narrativa não replicável.
- **QA3 = N** — **sem validação empírica própria**; case studies e benchmarks são catalogados/descritos de forma secundária, sem experimento/medição conduzido pelos autores.
- **QA4 = P** — conclusões coerentes e com §VI.D "Critical Evaluation" (sucessos/limitações/lições); porém **sem discussão das limitações metodológicas do próprio survey**.

## Parecer final do revisor

**Síntese.** P10 é um **survey abrangente diretamente sobre Agentic AI** — praticamente um **par de P6** (ambos _IEEE Access_ 2025, mesmo gênero e perfil). Cobre com solidez conceitual definições/características (**RQ1**), metodologias/arquitetura e ferramentas (**RQ2**), desafios técnicos e ético-governança (**RQ4**) e lacunas/direções futuras (**RQ5**), com SCORE_RQ 4.5/5. É mais fraco em **RQ3**: apresenta um bom **catálogo de métricas e benchmarks** (§VI, Tab. 8–9) e case studies, mas os benefícios são **qualitativos/ilustrativos, sem números empíricos próprios**, e a aderência a **Resposta a Incidentes é mínima** (cibersegurança tratada apenas como área de risco/privacidade). A qualidade metodológica é baixa (QA 1.5): revisão narrativa **sem protocolo** (QA2=N) e **sem validação empírica** (QA3=N).

**Recomendação: INCLUIR COM RESSALVAS.** Justificativa: forte aderência às RQs conceituais/arquitetura/desafios/lacunas (RQ1/RQ2/RQ4/RQ5), útil como **primer de Agentic AI** e, em particular, pelo **inventário de métricas de avaliação e benchmarks** (§VI) — insumo prático para a discussão de avaliação da RSL. **Ressalvas:** (i) metodologia narrativa não-reprodutível apesar de se autodenominar "systematic" (QA2=N); (ii) sem evidência empírica própria — não citar os case studies como prova de desempenho (QA3=N, RQ3=P); (iii) baixíssima aderência a IR; (iv) **forte sobreposição com P6** — ponderar uso complementar/deduplicação (ambos surveys conceituais IEEE Access 2025) ao consolidar as Tabelas da RSL.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
