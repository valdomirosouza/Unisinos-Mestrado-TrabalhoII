# Avaliação do Estudo P40

## Identificação do estudo

**ID:** P40  
**Artigo:** *A Comprehensive Survey on LLM-Based Network Management and Operations*  
**Autores:** Jibum Hong, Nguyen Van Tu e James Won-Ki Hong  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A3.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P40 | *International Journal of Network Management*, v. 35, artigo e70029 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Survey abrangente / revisão narrativa e taxonômica com síntese de estudos de caso sobre LLMs em gerenciamento e operações de redes | 10.1002/nem.70029 |

**Evidência bibliométrica:** a primeira página identifica o periódico, o volume 35, o artigo e70029, o ano de 2025 e o DOI. O manuscrito foi recebido em 1º de abril de 2025, revisado em 18 de setembro de 2025 e aceito em 24 de setembro de 2025.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | O artigo integra o volume de 2025, p. 1. | Atendido |
| Publicação identificável | O PDF apresenta periódico, volume, número do artigo e DOI, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado no próprio PDF um critério bibliométrico que permita encerrar imediatamente a avaliação como inelegível. Entretanto, o arquivo de instruções informa **Qualis A3**. Caso essa informação seja confirmada na Plataforma Sucupira, o estudo será **inelegível**, pois a RSL exige Qualis A1–A2.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | RQ1 — Context Definitions | Parcialmente Respondida | P | Seções 2.1–2.2, pp. 3–8; Tabelas 2–3, pp. 6 e 8; Seção 3, pp. 8–14. | O artigo descreve autonomia como transição de gerenciamento reativo para redes preditivas, adaptativas, self-healing e self-optimizing. Também cobre RL, sistemas multiagentes, intent-based networking, feedback humano, self-refinement, RAG e decisão em closed loop. Entretanto, não define formalmente Agentic AI, não apresenta níveis explícitos de autonomia nem consolida planejamento, memória, uso de ferramentas e supervisão humana em um único modelo decisório agêntico. |
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seções 2.1.2–2.2.2, pp. 5–8; Figuras 1–2, pp. 4 e 9; Seções 3–4, pp. 8–42; Seções 5.2.3–5.2.5, pp. 44–46. | A revisão cobre arquiteturas de IBN, SDN/NFV, ZSM, closed-loop control, sistemas distribuídos e multiagentes. Também apresenta frameworks e ferramentas como ONAP, OSM, O-RAN, RAG, LoRA, RLHF, ChatOps, digital twins, sandboxes, APIs, edge/cloud offloading e human-in-the-loop. As capacidades avançadas incluem adaptação por feedback, automação de configuração, monitoramento contínuo, RCA, recuperação, validação, fallback, explicabilidade e proteção de dados. |
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seção 3.3, p. 11; Seções 4.1–4.5, pp. 14–42; Tabelas 4–9, pp. 14–42. | O estudo sintetiza benefícios qualitativos como redução de erros humanos, interpretação de intenções, automação, troubleshooting, RCA, self-healing, melhoria de eficiência e redução de downtime. As tabelas de casos reportam métricas secundárias como acurácia, precisão, recall, F1, latência, tempo de processamento, disponibilidade, throughput, QoE, custos e consumo de energia. Exemplos incluem redução de 17,09% no MAE de previsão de tráfego, F1 de 0,89 em análise de logs e disponibilidade de 99,99% em correção de intent drift. A evidência é secundária e heterogênea, sem experimento próprio ou meta-análise, e não consolida MTTD, MTTR ou carga cognitiva. |
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | RQ4 — Challenges & Ethics | Respondida Plenamente | T | Seção 5.1, pp. 43–46; Seção 5.2.5, p. 46; discussão de segurança nas pp. 30–31. | O artigo cobre desafios técnicos como latência, consumo de memória e energia, alucinações, integração com legado, dados de domínio insuficientes, falta de confiabilidade, prompt injection e decisões incorretas em closed loops. Também discute privacidade, exposição de configurações e logs, explicabilidade, accountability e supervisão. Os mecanismos recomendados incluem RAG, validação simbólica, digital twins, sandbox, human-in-the-loop, XAI, adversarial training, federated learning, homomorphic encryption, secure MPC, validação padronizada, restrições operacionais e definição de responsabilidades. |
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção 5, pp. 43–46; Conclusão, p. 46. | A agenda futura é explícita: modelos leves e quantizados, adaptação específica de domínio, integração entre LLM, ML, RL e controladores tradicionais, inferência distribuída e offloading, validação estruturada, fallback, proteção contra adversarial inputs, XAI, privacidade, padronização e colaboração humano–IA. O artigo também destaca a necessidade de validação em redes reais, ambientes multidomínio e cenários com requisitos rígidos de tempo real. |
| P40 |  | **SCORE_RQ** | **4,5 / 5,0** | **P + T + T + T + T** |  | O estudo oferece cobertura ampla de arquitetura, benefícios, riscos e lacunas de LLMs aplicados a operações de rede. Sua aderência ao núcleo de Agentic AI é parcial, pois o conceito é tratado por meio de redes autônomas, closed loops, RL, feedback e automação, sem uma taxonomia explícita de agentes, autonomia ou planejamento. |

### Observação sobre a aderência ao conceito de Agentic AI

O artigo aborda redes autônomas, sistemas multiagentes, RL, human-in-the-loop, self-refinement e automação em closed loop. Entretanto, seu objeto principal são **LLMs para gerenciamento de redes**, e não Agentic AI como paradigma autônomo formal. Muitos casos descritos correspondem a geração de configurações, classificação, recomendação ou tradução de intenções, sem necessariamente combinar planejamento, memória, ferramentas e ação autônoma.

### Observação sobre resposta a incidentes e recuperação

A Seção 3.3 descreve um fluxo de gerenciamento de falhas com monitoramento, análise, detecção, previsão e recuperação. O LLM pode sugerir comandos como reinício de switches, rollback de configuração e desvio de tráfego, além de acompanhar o resultado da recuperação. Essa cobertura é diretamente relevante para incident response. Contudo, as evidências são derivadas de estudos primários heterogêneos e não demonstram, no próprio artigo, redução observada de MTTD ou MTTR.

### Observação sobre as Figuras 1 e 2

A **Figura 1, p. 4**, organiza o survey em cinco domínios: design, configuração, fault management, segurança e orquestração. Em fault management, destaca anomaly detection e mitigation/recovery.

A **Figura 2, p. 9**, apresenta uma arquitetura conceitual na qual conhecimentos, configurações e dados de monitoramento alimentam um LLM adaptado por prompt engineering, fine-tuning, RAG e feedback. O modelo produz decisões para design, configuração, falhas, segurança e orquestração.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P40 | Survey abrangente / revisão narrativa e taxonômica sobre LLMs em gerenciamento de redes | Y (1,0) | N (0,0) | N (0,0) | P (0,5) | **1,5 / 4,0** | **Média** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitamente delimitado: crescimento da capacidade, heterogeneidade e complexidade das redes, insuficiência de processos manuais e regras estáticas e necessidade de operações mais autônomas. O objetivo é revisar abordagens LLM para design, configuração, fault management, segurança e orquestração, comparar suas vantagens e limitações e propor direções futuras. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: N (0,0).**  
O artigo não apresenta uma seção de metodologia da revisão. Não informa bases consultadas, strings de busca, período de coleta, quantidade de registros, critérios de inclusão e exclusão, processo de seleção, revisores, resolução de divergências ou avaliação da qualidade dos estudos primários. As taxonomias e tabelas são detalhadas, mas o processo de formação do corpus não pode ser reproduzido ou auditado conforme as diretrizes de Kitchenham.

**QA3 — Base de evidências sólidas: N (0,0).**  
O artigo não realiza experimento próprio, estudo de caso industrial, simulação ou implementação avaliada pelos autores. As métricas e resultados quantitativos pertencem aos estudos primários resumidos nas Tabelas 4–9. Conforme a rubrica da RSL, uma revisão sem validação empírica direta recebe **N** neste critério.

**QA4 — Conclusões coerentes: P (0,5).**  
As conclusões são coerentes com a síntese sobre automação, fault management, riscos e direções futuras. O artigo reconhece limitações técnicas dos sistemas LLM, como latência, alucinação, privacidade e integração. Entretanto, não discute as limitações da própria revisão, possíveis vieses de seleção, cobertura das fontes, qualidade dos estudos incluídos ou ameaças à validade da síntese.

---

## Parecer final do revisor

O estudo apresenta forte relevância para gerenciamento autônomo de redes, fault management, RCA, recuperação, segurança e orquestração. Sua principal contribuição para a RSL é conceitual e secundária, organizando arquiteturas, técnicas de adaptação, métricas, riscos e direções futuras. Contudo, não é uma revisão sistemática replicável, não produz evidência empírica própria e não tem Agentic AI como objeto central.

### Recomendação

**EXCLUIR DO CORPUS PRINCIPAL.**

A exclusão é recomendada por três razões. Primeiro, o estudo não apresenta metodologia de busca e seleção reproduzível segundo Kitchenham. Segundo, não possui validação empírica própria e deve ser tratado como fonte secundária de contextualização. Terceiro, o arquivo de instruções informa Qualis A3, abaixo do critério A1–A2 da RSL. Embora esse dado deva ser confirmado externamente, sua confirmação tornará o artigo bibliometricamente inelegível.

O artigo pode ser preservado como referência de apoio para fundamentar gerenciamento de falhas, redes autônomas, closed loops, human-in-the-loop, riscos de LLMs e mecanismos de validação.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES. O arquivo de instruções informa **A3**; caso confirmado, o estudo é inelegível.
