# Avaliação do Estudo P29

## Identificação do estudo

**ID:** P29  
**Artigo:** *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review*  
**Autores:** Miguel De la Cruz Cabello, Tiago Prince Sales e Marcos R. Machado  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q1 e Qualis A2.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P29 | *Intelligent Systems with Applications*, v. 28, artigo 200608 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão sistemática da literatura com síntese qualitativa, análise bibliométrica e proposição de framework teórico baseado em LLM e RAG | 10.1016/j.iswa.2025.200608 |

**Evidência bibliométrica:** a primeira página identifica o periódico, o volume 28, o ano de 2025, o número do artigo 200608 e o DOI. O artigo foi recebido em 13 de julho de 2025, aceito em 9 de novembro de 2025 e disponibilizado online em 19 de novembro de 2025.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, ScienceDirect ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | *Intelligent Systems with Applications*, volume 28, 2025, p. 1. | Atendido |
| Publicação identificável | Periódico, volume, número do artigo e DOI são apresentados na primeira página. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos critérios bibliométricos externos.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução, pp. 1–2; Seção 4.1, pp. 6–8; Seção 4.4 e Figura 10, pp. 12–14. | O artigo descreve o ciclo AIOps como observação, análise e atuação, além de apresentar a remediação automatizada como estágio avançado, com execução de estratégias predefinidas e menor intervenção manual. Também menciona agentes autônomos de defesa cibernética e um framework de classificação com LLM e RAG. Entretanto, não oferece definição formal de Agentic AI, níveis de autonomia, planejamento agêntico, supervisão humana estruturada ou um modelo completo de decisão de agentes. A cobertura das subdimensões é, portanto, genérica e indireta. |
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seções 4.2–4.4, pp. 8–14; Figura 10, pp. 13–14; Apêndice, pp. 15–18. | A revisão apresenta mecanismos relevantes para sistemas inteligentes de produção: parsing de logs, embeddings, banco vetorial, RAG, prompt engineering, fine-tuning, LoRA, recuperação de contexto e classificação por LLM. O framework proposto segue princípios CRISP-ML e inclui preparação de dados, base vetorial, recuperação de logs e avaliação da saída. Contudo, não especifica arquitetura agêntica com orquestração, memória episódica, seleção autônoma de ferramentas, guardrails de execução, observabilidade do agente ou fallback operacional detalhado. |
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seções 4.1–4.3, pp. 6–12; Tabela 2, p. 5; Apêndice, pp. 15–18; Conclusão, p. 14. | O estudo sintetiza benefícios qualitativos como maior precisão, interpretabilidade, adaptabilidade, confiabilidade, escalabilidade, redução de esforço manual, diagnóstico mais rápido e menor downtime. Também reúne métricas quantitativas, incluindo precisão, recall, F1-score, AUROC, AUPR, falsos positivos, latência, throughput e custo. Entre os resultados secundários, registra que LogLLM supera métodos anteriores em 6,6% no F1 médio e apresenta comparações de múltiplos modelos e datasets no apêndice. O nível de evidência é secundário, derivado de 33 estudos, sem meta-análise ou experimento próprio, mas as três subdimensões da RQ estão explicitamente cobertas. |
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seções 4.1–4.3, pp. 7–12; Conclusão, p. 14. | O artigo apresenta desafios técnicos e operacionais relevantes: concept drift, escassez de dados rotulados, desbalanceamento, mudanças no formato dos logs, necessidade de processamento em tempo real, custo computacional, latência, manutenção do banco vetorial, integração com sistemas legados, alucinações e dependência de modelos de terceiros. Também aborda privacidade e confidencialidade, especialmente em ambientes militares. Como mecanismos de mitigação, recomenda RAG, conhecimento atualizado, fine-tuning, modelos menores e monitoramento de drift e alucinação. Entretanto, não discute de forma suficiente accountability, auditoria, autorização de decisões, responsabilidade por falsos negativos ou governança institucional. |
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção 4.4 e Figura 10, pp. 12–14; Conclusão, p. 14. | O estudo explicita lacunas e direções futuras: detecção em tempo real, especialização de RAG para logs, adaptação a concept drift, redução de alucinações, maior disponibilidade de dados rotulados, melhoria da eficiência computacional, modelos específicos de domínio e aplicações em setores críticos. O domínio militar é destacado como oportunidade de pesquisa, com necessidade de sistemas capazes de tratar dados sensíveis, grandes volumes de telemetria e respostas contextuais rápidas. |
| P29 |  | **SCORE_RQ** | **3,5 / 5,0** | **P + P + T + P + T** |  | O estudo oferece contribuição relevante para benefícios, desafios, métricas e agenda de pesquisa em AIOps com LLM e RAG. Sua aderência ao componente “Agentic AI” é parcial, pois o foco principal é detecção de anomalias e não o comportamento autônomo, a colaboração entre agentes ou a execução de resposta a incidentes em ciclo fechado. |

### Observação sobre a natureza agêntica do estudo

O artigo aborda automação avançada em AIOps, LLMs, RAG e remediação automática como parte do ciclo operacional. Entretanto, o framework proposto na Figura 10 corresponde principalmente a um pipeline de classificação de logs com recuperação de contexto. Ele não apresenta um agente que planeja, seleciona ferramentas dinamicamente, reflete sobre resultados ou executa autonomamente ações de recuperação. Assim, sua contribuição para Agentic AI deve ser interpretada como **fundamentação tecnológica e contextual**, não como evidência direta de um copiloto agêntico completo.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P29 | Revisão sistemática da literatura com framework teórico | Y (1,0) | P (0,5) | N (0,0) | Y (1,0) | **2,5 / 4,0** | **Média** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitamente delimitado: sistemas modernos geram grandes volumes de logs, enquanto métodos tradicionais exigem feature engineering, apresentam dificuldade de adaptação e têm compreensão contextual limitada. O objetivo é revisar como LLMs e RAG podem melhorar a detecção de anomalias em AIOps. O estudo apresenta quatro questões de conhecimento sobre benefícios, técnicas, métricas e RAG. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo informa as questões de pesquisa, critérios de inclusão e exclusão, base principal, consultas completas, processo de snowballing, etapas de seleção e total final de 33 estudos. A Figura 1 registra a redução de 826 resultados para 593, depois 23 artigos, com dez estudos adicionados por snowballing. Entretanto, a busca principal foi limitada ao Scopus, com uso complementar do arXiv, e não são informados claramente a data exata da busca, o número de revisores, o procedimento para resolver discordâncias ou critérios formais de avaliação da qualidade de cada estudo primário. A avaliação descrita como leitura de títulos e resumos não equivale a uma rubrica sistemática de risco de viés.

**QA3 — Base de evidências sólidas: N (0,0).**  
O artigo não apresenta experimento próprio, estudo de caso industrial, simulação ou protótipo empiricamente avaliado pelos autores. Os resultados quantitativos são extraídos dos estudos primários, e a Figura 10 apresenta um framework teórico sem implementação ou validação. Conforme a rubrica definida para esta RSL, estudos teóricos ou secundários sem validação empírica direta recebem **N**.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões respondem às quatro questões de conhecimento e permanecem coerentes com a síntese sobre benefícios, técnicas, métricas e uso de RAG. O artigo também reconhece limitações metodológicas: Scopus e arXiv não são exaustivos, podem omitir estudos de veículos menores e podem introduzir viés de seleção. Além disso, registra limitações técnicas relativas a privacidade, eficiência computacional, alucinações e adoção em domínios críticos.

---

## Parecer final do revisor

O estudo apresenta forte relevância para o eixo AIOps, observabilidade e detecção de anomalias em logs. Ele sintetiza técnicas, métricas, benefícios e limitações de LLMs e RAG e propõe um pipeline conceitual alinhado ao CRISP-ML. Entretanto, sua aderência ao conceito de Agentic AI é parcial: não há arquitetura multiagente, planejamento autônomo, seleção dinâmica de ferramentas ou validação de resposta a incidentes em ciclo fechado.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada como fonte secundária para fundamentar detecção de anomalias, uso de RAG, métricas de qualidade e desafios técnicos de LLMs em AIOps. O artigo não deve ser utilizado como evidência primária de redução de MTTD, MTTR ou carga cognitiva, nem como comprovação de um copiloto agêntico em produção. As principais ressalvas são a baixa cobertura de autonomia agêntica, a ausência de avaliação empírica do framework proposto, a busca concentrada em uma base indexadora e a falta de avaliação formal da qualidade dos estudos incluídos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, ScienceDirect ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
