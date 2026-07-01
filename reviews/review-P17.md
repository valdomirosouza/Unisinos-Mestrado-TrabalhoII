# Avaliação RSL — Estudo P17

**Artigo:** _A Review of Trustworthy and Explainable Artificial Intelligence (XAI)_ — V. Chamola, V. Hassija, A. R. Sulthana, D. Ghosh, D. Dhingra, B. Sikdar (BITS-Pilani / National University of Singapore / University of Greenwich / Jaypee Institute of Information Technology)
**Arquivo:** P17-A1 - A_Review_of_Trustworthy_and_Explainable_Artificial_Intelligence_XAI.pdf (22 páginas)

> ⚠️ **Recomendação: EXCLUIR — não-aderência ao escopo.** Revisão narrativa de Trustworthy/Explainable AI (IA geral, 2023); sem Agentic AI (LLM) e sem Resposta a Incidentes. Pilar conceitual adjacente (explicabilidade/confiança), análogo a P8. SCORE_RQ 0.0/5; QA 1.5/4.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                   | DOI                         |
| --- | ----------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------- | --------------------------- |
| P17 | _IEEE Access_ (Vol. 11) | 2023 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Survey / revisão narrativa (TAI + XAI) | 10.1109/ACCESS.2023.3294569 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2023.3294569; recebido 18/06/2023, publicado 20/07/2023; "VOLUME 11, 2023"; licença CC-BY-NC-ND). Revisão de componentes de TAI, métodos XAI (transparency design, post-hoc, LIME, DARPA XAI) e verticais (banking/saúde/veículos autônomos/IoT). Varredura confirmou ausência de "agentic", "LLM", "incident", "SOC"; "autonomous" refere-se a veículos/sistemas. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                 | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)   | Parecer do revisor                                                                                                                                                                                                                                 |
| --- | -------------------------------------- | ---------------------------- | --------------------------- | ------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P17 | Review of Trustworthy & Explainable AI | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §I–II (p.1–7)            | Trata **Trustworthy AI / XAI de IA em geral** (ML/DL "caixa-preta"). **Não** define Agentic AI; autonomia mencionada é de ML/veículos autônomos, não agêntica (LLM).                                                                               |
| P17 | "                                      | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §IV (p.11–17)            | "Arquitetura" tratada é de **modelos XAI** (transparency design, post-hoc, LIME, surrogate models, DARPA XAI), **não** arquitetura de engenharia de agentic AI (orquestração/memória/ferramentas/guardrails agênticos).                            |
| P17 | "                                      | RQ3 Evidence Benefits        | Não tem conteúdo suficiente | **N**         | §III (p.9–11)            | Aplicações em **banking/healthcare/veículos autônomos/IoT** — não benefícios de Agentic AI nem de Resposta a Incidentes. Fora do domínio de IR.                                                                                                    |
| P17 | "                                      | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | §II, §IV (p.4–17)        | Cobre pilares de confiança/explicabilidade (viés, robustez adversarial, transparência, supervisão humana) — **relevantes como fundamentação**, mas para **IA geral, não agentic AI**; sem governança/ética de sistemas agênticos no sentido da RQ. |
| P17 | "                                      | RQ5 Research Gaps            | Não tem conteúdo suficiente | **N**         | §IV, Conclusão (p.17–20) | Direções futuras de XAI/TAI (drawbacks/pitfalls de XAI, políticas para veículos autônomos) — **não** lacunas de agentic AI (benchmarking/threat models/observabilidade/alinhamento agêntico).                                                      |
|     |                                        | **SCORE_RQ**                 |                             | **0.0 / 5.0** |                          | N + N + N + N + N                                                                                                                                                                                                                                  |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                         | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | -------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P17 | Survey / revisão narrativa (TAI + XAI) | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (construir IA confiável e explicável; IA como caixa-preta) e escopo (componentes de TAI, métodos XAI, verticais) explícitos (§I, Abstract).
- **QA2 = N** — **revisão narrativa sem protocolo sistemático** (sem bases, string de busca, critérios de inclusão/exclusão, contagens/PRISMA).
- **QA3 = N** — **sem validação empírica própria**; síntese secundária da literatura de XAI/TAI.
- **QA4 = P** — conclusões coerentes e discute **drawbacks/pitfalls de XAI**; porém sem discussão das limitações do próprio survey.

## Parecer final do revisor

**Síntese.** P17 é uma **revisão narrativa de Trustworthy AI (TAI) e Explainable AI (XAI)** de 2023, cobrindo componentes de confiança (viés, robustez, supervisão humana), métodos de explicabilidade (transparency design, post-hoc, LIME, DARPA XAI) e verticais (banking, saúde, **veículos autônomos**, IoT). **Não trata de Agentic AI** (nenhum framing agêntico; sem LLMs) **nem de Resposta a Incidentes** (varredura confirmou ausência de "agentic", "LLM", "incident", "SOC"; "autonomous" refere-se a veículos/sistemas). Nenhuma das cinco RQs é atendida (SCORE_RQ 0,0/5). É um caso **análogo a P8 (HITL)**: pilar conceitual adjacente (explicabilidade/confiança ↔ oversight humano) relevante à IA confiável, mas fora do paradigma e do domínio da RSL. QA 1,5 (Média): narrativa sem protocolo (QA2=N), sem evidência própria (QA3=N).

**Recomendação: EXCLUIR — por não-aderência ao escopo.** Justificativa: apesar de passar (provisoriamente) na elegibilidade formal, o estudo **não contribui para nenhuma RQ** da RSL sobre Agentic AI para IR — é XAI/TAI de IA geral, pré-agêntica (2023), em domínios não-IR. **Nuance (como em P8):** explicabilidade/transparência/confiabilidade **são pilares de agentic AI confiável** (dimensão de governança da RQ4); assim, P17 poderia, se desejado, servir como **referência de fundamentação sobre XAI/TAI** (conceitos de transparência e explicabilidade a exigir de um copiloto agêntico), mas **não como estudo do corpus** (não aborda agentic AI nem IR; pontua 0 em todas as RQs). Recomenda-se excluir e revisar os critérios de busca (provável casamento por "explainable/trustworthy AI"/"autonomous").

**Pendências de verificação externa:** (registradas por completude; não alteram a exclusão por escopo)

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
