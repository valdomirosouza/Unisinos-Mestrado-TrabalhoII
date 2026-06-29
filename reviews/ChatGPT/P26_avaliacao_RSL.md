# Avaliação do Estudo P26

## Identificação do estudo

**ID:** P26  
**Artigo:** *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications*  
**Autores:** Zhijing Li, Jianbo Yu, Zhijun Huang e Yusheng Huang  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Embora o arquivo de instruções informe SJR Q1 e Qualis A1, esses campos permanecem como **[VERIFICAR]**, em conformidade com as regras antifabricação.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P26 | *IEEE Transactions on Services Computing*, v. 19, n. 1 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Survey paper / revisão sistemática da literatura baseada nas diretrizes de Kitchenham et al. | 10.1109/TSC.2025.3631913 |

**Observação sobre o ano:** o artigo foi publicado antecipadamente em 13 de novembro de 2025, mas integra a edição de janeiro/fevereiro de **2026**. Para a Tabela 3, foi adotado o ano bibliográfico da edição.

**Fontes para verificação externa:**

- **Citações:** base indexadora, como Scopus, Web of Science, IEEE Xplore ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | Edição de janeiro/fevereiro de 2026; publicação antecipada em 13 de novembro de 2025, p. 1 do PDF. | Atendido |
| Publicação identificável | *IEEE Transactions on Services Computing*, v. 19, n. 1, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | RQ1 — Context Definitions | Não tem conteúdo suficiente | N | Seção II.A, pp. 2–3; Seção VII, p. 8. | O artigo define RCA e diferencia localização de falhas, análise de causa raiz e mitigação de incidentes. Também menciona um agente baseado em ReAct que recupera logs, métricas e tickets. Contudo, não caracteriza Agentic AI em termos de níveis de autonomia, planejamento, memória, supervisão humana ou modelo decisório agêntico. A referência ao uso de ferramentas por um agente é pontual e tangencial às subdimensões da RQ1. |
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seções III–VII, pp. 4–9; Seção IX.B, pp. 12–13; Seção XII, pp. 15–16. | A revisão cobre arquiteturas de RCA baseadas em logs, traces, métricas, documentos, grafos causais e fusão multimodal. Também descreve ferramentas de observabilidade, datasets e um exemplo de agente ReAct que acessa diferentes fontes operacionais. As direções futuras incluem arquiteturas híbridas, raciocínio causal, inferência em streaming e integração de conhecimento específico do sistema. Entretanto, não apresenta uma arquitetura de Agentic AI em produção com orquestração, memória, guardrails e observabilidade do próprio agente. |
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | RQ3 — Evidence Benefits | Parcialmente Respondida | P | Seção II.A, p. 3; Seções III–VIII, pp. 4–12; Seção X, pp. 13–15; Figura 5, p. 4. | O estudo sintetiza benefícios qualitativos da RCA, como diagnóstico mais rápido, redução da análise manual, prevenção de recorrências, colaboração e maior precisão. Também reúne métricas quantitativas como Accuracy, Precision, Recall, F1, Top@N, MRR, falsos positivos, falsos negativos e runtime. Entre as evidências secundárias, cita melhoria superior a 17% na localização por métricas, processamento industrial de 150 bilhões de spans por dia e apenas 11,3% de casos resolvidos pelo melhor agente no benchmark OpenRCA. Porém, não realiza meta-análise nem apresenta evidência empírica própria sobre MTTD, MTTR ou carga cognitiva. |
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seções III–VIII, pp. 4–12; Seção XII, pp. 15–16. | O artigo discute desafios técnicos relevantes: volume e heterogeneidade da telemetria, dependências dinâmicas, propagação de falhas, dados desbalanceados, baixa disponibilidade de datasets realistas, generalização entre domínios, baixa interpretabilidade, contexto limitado dos LLMs, alucinações e baixo sucesso em cenários reais. Contudo, não desenvolve desafios éticos, accountability, privacidade, autorização de ações, auditoria ou mecanismos formais de governança para sistemas autônomos. |
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção XII, pp. 15–16; Seção XIII, p. 16. | As lacunas e direções futuras são explícitas: fortalecimento do raciocínio causal, ampliação de contexto, redução de alucinações, explicabilidade, datasets multimodais e multidomínio, adaptação online, robustez a mudanças de topologia, fusão de logs, traces, métricas e topologia, arquiteturas híbridas e análise em tempo real. O artigo também reconhece que sua estratégia de busca pode ter excluído trabalhos de outros veículos e literatura cinzenta. |
| P26 |  | **SCORE_RQ** | **2,5 / 5,0** | **N + P + P + P + T** |  | O estudo oferece contribuição forte para contextualização de RCA, observabilidade, métricas e agenda de pesquisa. Sua aderência é limitada às dimensões específicas de Agentic AI, pois o foco principal está nas técnicas de diagnóstico e apenas uma pequena parte da revisão aborda agentes baseados em LLM. |

### Observação metodológica sobre a seleção dos estudos

Há uma inconsistência interna nas quantidades apresentadas. A Seção II.B, p. 3, informa **845 artigos coletados e 97 selecionados**, enquanto as Tabelas II e III, p. 4, apresentam totais de **893 artigos coletados e 104 selecionados**. Como o PDF não explica a divergência, os valores não foram reconciliados por inferência.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P26 | Survey paper / revisão sistemática da literatura | Y (1,0) | P (0,5) | N (0,0) | Y (1,0) | **2,5 / 4,0** | **Média** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O estudo explicita como problema a fragmentação das técnicas de RCA entre diferentes domínios, fontes de dados e cenários de serviços. O objetivo é sintetizar métodos organizados por cenário de aplicação e tipo de entrada, além de consolidar algoritmos, abordagens híbridas e baseadas em LLM, métricas, datasets, ferramentas e lacunas de pesquisa. Evidências: Resumo e Introdução, pp. 1–2.

**QA2 — Metodologia replicável: P (0,5).**  
A revisão declara seguir Kitchenham et al., informa cinco bases, o intervalo de 2017 a 2025, critérios de inclusão, termos centrais, 96 combinações de palavras-chave e veículos, uso de crawler, deduplicação e material suplementar com consultas detalhadas. Entretanto, não descreve claramente os critérios de exclusão completos, o número de revisores, a resolução de discordâncias ou uma avaliação formal da qualidade dos estudos primários. Há ainda divergência entre as quantidades informadas no texto e nas Tabelas II e III. Assim, a estratégia é parcialmente reproduzível, mas não integralmente auditável.

**QA3 — Base de evidências sólidas: N (0,0).**  
O artigo é um estudo secundário e não apresenta experimento próprio, estudo de caso industrial, simulação ou protótipo validado pelos autores. Os resultados quantitativos são extraídos dos estudos primários revisados. Conforme a rubrica definida para esta RSL, a ausência de validação empírica direta corresponde a **N**.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões refletem a classificação dos métodos, datasets, ferramentas, métricas e desafios discutidos ao longo do artigo. A Seção XIII reconhece explicitamente uma limitação da própria estratégia de busca, que pode ter excluído trabalhos de outros veículos e literatura cinzenta, e sugere ampliar esse escopo. As conclusões e direções futuras permanecem coerentes com a síntese apresentada.

---

## Parecer final do revisor

O estudo apresenta forte relevância para a compreensão de RCA em sistemas distribuídos, microserviços e nuvem, além de organizar fontes de observabilidade, métricas, datasets e desafios técnicos. A aderência ao escopo de resposta a incidentes é clara na fase de diagnóstico, mas a cobertura de Agentic AI é limitada e concentrada em poucos trabalhos com LLMs e agentes. O artigo não avalia planejamento, memória, supervisão ou remediação autônoma de forma sistemática.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada como fonte secundária para fundamentar RCA, observabilidade multimodal, métricas de avaliação e lacunas de pesquisa. O estudo não deve ser utilizado como evidência primária de benefícios de um copiloto agêntico nem de redução de MTTD, MTTR ou carga cognitiva. As principais ressalvas são a baixa cobertura de Agentic AI, a ausência de validação empírica própria, a falta de avaliação formal da qualidade dos estudos primários e a inconsistência nos números do processo de seleção.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
