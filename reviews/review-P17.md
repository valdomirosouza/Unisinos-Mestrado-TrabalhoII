# Avaliação RSL — Estudo P17 (fundacional, retroativa)

**Artigo:** _A Review of Trustworthy and Explainable Artificial Intelligence (XAI)_ — V. Chamola, V. Hassija, A. R. Sulthana, D. Ghosh, D. Dhingra, B. Sikdar (BITS-Pilani; NUS; Univ. of Greenwich; JIIT Noida)
**Arquivo:** P17-A1-A_Review_of_Trustworthy_and_Explainable_Artificial_Intelligence_XAI.pdf (22 páginas, pp. 78994–79015)
**Natureza da avaliação:** RETROATIVA — estudo do corpus FUNDACIONAL (P01–P19), herdado da RSL do Trabalho I; a inclusão NÃO é rediscutida, apenas medem-se aderência às RQs e qualidade DARE para padronização com os ciclos 1 e 2.

## Etapa 1 — Elegibilidade

**FUNDACIONAL — inclusão herdada do Trabalho I (não rediscutida); bibliometria verificada.** Ano 2023 ≥ 2020 ✓; veículo identificável (IEEE Access, Vol. 11) ✓; Citações ≥ 1 ✓ (OA 300 / CR 297 / Scopus 290); SJR Q1 ✓; Qualis A1 ✓.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.       | Ano  | Cit.                                                  | SJR             | Qualis          | Tipo                                    | DOI                         |
| --- | --------------------- | ---- | ----------------------------------------------------- | --------------- | --------------- | --------------------------------------- | --------------------------- |
| P17 | IEEE Access (Vol. 11) | 2023 | OA 300 / CR 297 / Scopus 290 (papers.csv, 2026-07-27) | Q1 (verificado) | A1 (verificado) | Revisão narrativa (survey) de TAI e XAI | 10.1109/ACCESS.2023.3294569 |

_Evidências: cabeçalho p.78994 (DOI, recebido 18/06/2023, publicado 20/07/2023); rodapé "VOLUME 11, 2023"; licença CC BY-NC-ND 4.0; financiamento Ministry of Education, Singapore. Citações/SJR/Qualis verificados externamente nas três fontes (papers.csv, 2026-07-27)._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                       | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                                     | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | ---------------------------- | ---------------------------- | ----------------------- | ------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P17 | Review of Trustworthy AI/XAI | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §II.A (p.78997), §V.C (p.79008-79010)                      | Supervisão humana bem definida — governança HITL/HOTL/HIC e agências de oversight local/global (a parcial); autonomia tratada genericamente para AI/autonomous systems, não para Agentic AI; sem capacidades agênticas (planejamento, memória, uso de ferramentas) (b ausente); decisão abordada só pela ótica da explicabilidade do output, sem modelo decisório (c ausente).                                 |
| P17 | "                            | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §III.E (p.79001-79002), §IV.A-B (p.79003-79005)            | Cobre mecanismos de transparência/observabilidade utilizáveis como guardrails: taxonomia transparent design (simulatability, decomposability, computational transparency) e post-hoc (model extraction/knowledge distillation, PDP, ALE, H-statistic, ICE, LIME, feature importance) (c parcial); sem arquitetura agêntica, orquestração, memória ou stack de produção (a/b ausentes).                         |
| P17 | "                            | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §V.A-B (p.79006-79008), Fig. 2 (p.78995), Tab. 2 (p.79011) | Benefícios qualitativos explícitos de TAI/XAI por setor — conformidade regulatória, confiança do consumidor, mitigação de risco legal em banking; validação e comunicação clínica em healthcare (a); quantitativo apenas citado de terceiros (survey de confiança Univ. Queensland; IoU >80% per-category de Hofmarcher et al.) (b fraco); evidência terciária, sem métricas próprias e sem IR (c).            |
| P17 | "                            | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §II (p.78996-79000), §V.C (p.79008-79010), §VI (p.79011)   | Núcleo do artigo: desafios técnicos — black-box, ataques adversariais, trade-off acurácia×interpretabilidade, falhas de sistemas autônomos (caso MCAS/Boeing) (a); ética/governança — sete princípios EC de TAI, GDPR/CCPA, fairness, accountability decomposta em responsibility/answerability/sanctionability (b); mecanismos — HITL/HOTL/HIC, agências de oversight, ISO 21448/26262/TC 204, NHTSA/SAE (c). |
| P17 | "                            | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §VI (p.79011), §II.E (p.78999-79000), §V.A.6 (p.79008)     | Lacunas explícitas: replicabilidade dos métodos post-hoc; ausência de entendimento, critérios e métricas unificados de interpretabilidade (avaliação/benchmarking); fricção eficiência×preditividade; limites de explicação de DNNs; fairness sub-pesquisada; governança/regulação de AI ainda em estágio preliminar.                                                                                          |
|     |                              | **SCORE_RQ**                 |                         | **3.5 / 5.0** |                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                          | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | --------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P17 | Revisão narrativa (survey) de TAI e XAI | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema explícito (síndrome black-box, déficit de confiança — só ~25% dos indivíduos confiam em sistemas de AI, Fig. 2) e objetivo declarado: nenhum estudo compreensivo cobria todos os elementos de TAI + integração de XAI por setor; a revisão visa fechar essa lacuna (§I, p.78996; §VI, p.79011).
- **QA2 = N** — revisão narrativa sem protocolo: não há string de busca, bases consultadas, critérios de inclusão/exclusão nem processo de seleção descritos; a metodologia não é replicável.
- **QA3 = N** — sem validação empírica própria (sem experimento, estudo de caso ou simulação com métricas); estudo teórico/terciário que apenas reporta resultados de trabalhos citados (rubrica: teórico = N).
- **QA4 = P** — conclusões coerentes com o material revisado e desafios abertos do campo listados (replicabilidade post-hoc, métricas de interpretabilidade, DNNs) (§VI, p.79011); porém limitações do próprio método de revisão não são discutidas.

## Parecer final do revisor

**STATUS: MANTIDO NO CORPUS (fundacional)**

**Síntese.** Revisão narrativa abrangente de **Trustworthy AI** (sete princípios da European Commission: human agency/oversight, robustness, privacy/data governance, transparency, diversity/fairness, well-being, accountability) e de **XAI** (transparent design e post-hoc explainability, métodos globais e locais), com aplicação setorial em healthcare, banking, IoT e sistemas autônomos. Aderência plena a **RQ4** (desafios técnicos, éticos e mecanismos de governança — o núcleo do artigo) e **RQ5** (lacunas explícitas de avaliação, métricas e regulação); parcial em **RQ1** (supervisão humana HITL/HOTL/HIC sem capacidades agênticas), **RQ2** (taxonomia XAI como insumo de guardrails/observabilidade, sem arquitetura agêntica) e **RQ3** (benefícios qualitativos, sem evidência empírica própria nem IR). Na RSL, cumpre o papel de **fundamento de trustworthy/XAI para a governança do copilot**: fornece o arcabouço de princípios, mecanismos de oversight e técnicas de explicabilidade que sustentam o uso responsável de Agentic AI em resposta a incidentes. SCORE_RQ 3.5/5.0; QA 1.5/4.0 (Banda Média — esperado para survey narrativo sem protocolo sistemático nem validação empírica, o que não compromete seu papel conceitual no corpus fundacional).

**Pendências de verificação externa:** nenhuma (bibliometria verificada nas três fontes).
