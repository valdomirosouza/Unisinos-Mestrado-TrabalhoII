# Avaliação do Estudo P32

## Identificação do estudo

**ID:** P32  
**Artigo:** *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems*  
**Autores:** Wenya Zhang, Zhi Yang, Fang Peng, Le Zhang, Yiting Chen e Ruibo Chen  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A2.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P32 | *Electronics*, v. 15, artigo 243 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com framework GNN–LLM, observabilidade multimodal, RAG, injeção controlada de falhas, comparação com baselines e ablação | 10.3390/electronics15010243 |

**Evidência bibliométrica:** a primeira página identifica o periódico, o volume 15, o artigo 243, o ano de 2026 e o DOI. O artigo foi recebido em 14 de novembro de 2025, aceito em 29 de dezembro de 2025 e publicado em 5 de janeiro de 2026.

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
| Ano ≥ 2020 | *Electronics*, volume 15, artigo 243, publicado em 2026, p. 1. | Atendido |
| Publicação identificável | Periódico, volume, artigo e DOI são apresentados na primeira página. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos três itens bibliométricos externos.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução, pp. 1–3; Seções 3.3–3.5, pp. 9–11; Algoritmo 1, p. 11; Discussão, p. 16. | O artigo associa autonomia à gestão adaptativa de falhas com intervenção humana mínima e apresenta um agente de recuperação que consulta casos históricos, produz planos estruturados e considera métricas de verificação, rollback e resultados esperados. A biblioteca de casos funciona como memória externa, e o modelo decisório combina probabilidades semânticas do LLM, atenção em grafo, ranking de causas e recuperação por similaridade. Entretanto, não há taxonomia de níveis de autonomia, planejamento iterativo, reflexão sobre resultados ou ciclo de replanejamento. A execução também permanece separada da geração, com confirmação manual prevista para planos inseguros. |
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seção 3, pp. 5–11; Figura 1, p. 6; Algoritmo 1, p. 11; Seção 4.3, pp. 13–14. | GALR integra quatro módulos: fusão multimodal, localização por GNN, enriquecimento semântico por LLM e planejamento de recuperação com RAG. A arquitetura utiliza métricas, logs, traces, grafo de chamadas, GAT com decaimento temporal e viés semântico, DeepSeek V3, BGE-M3, Prometheus, Fluent Bit, Kubernetes, Chaos-Mesh e Locust. As capacidades avançadas incluem representação explícita de incerteza, memória por biblioteca de 500 casos, recuperação semântica, espaço restrito de ações, comparação com playbooks especializados, rollback, validação de parâmetros, allowlists, canary release e integração com observabilidade multimodal. |
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seções 4.1–4.5, pp. 11–16; Tabelas 2–5; Figura 2, p. 14. | O estudo apresenta benefícios qualitativos em interpretação de logs, modelagem de propagação, priorização de causas e geração de planos acionáveis. Nos três datasets, GALR obtém Top-1 de 0,842, 0,883 e 0,931 e MRR de 0,923, 0,916 e 0,953. O MRR médio é 0,931, aproximadamente 3,2% superior ao melhor baseline. O agente LLM + RAG alcança acurácia de recuperação de 79,2%, 75,8% e 70,1%, superando zero-shot e few-shot. A evidência inclui 52.036 traces, três ambientes, seis tipos de falha e ablação. Contudo, os planos são avaliados offline por sobreposição de ações, sem execução real, e não são medidos MTTD, MTTR ou carga cognitiva. |
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Introdução, pp. 1–2; Seção 3.4, pp. 10–11; Seção 4.1, p. 12; Seção 5, pp. 16–17. | O artigo discute ruído e incompletude da telemetria, dependências dinâmicas, drift, escalabilidade, latência, alinhamento multimodal, generalização, alucinações e risco de planos incorretos. Como mecanismos de governança técnica, propõe grounding por RAG, comparação com playbooks, espaço de ações restrito, templates de comandos, allowlists, limites de parâmetros, bloqueio de operações proibidas, rejeição de planos inseguros, confirmação manual e canary release. Apesar disso, não aprofunda accountability organizacional, privacidade, controle de acesso, auditoria independente ou responsabilidade por danos decorrentes de uma recuperação incorreta. |
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | RQ5 — Research Gaps | Respondida Plenamente | T | Seções 4.1 e 4.4, pp. 12 e 15; Seção 5, pp. 16–17; Conclusão, p. 17. | As limitações e direções futuras são explícitas: melhorar escalabilidade e latência com anotação seletiva, cache e políticas de atualização; criar guardrails mais rigorosos; validar parâmetros e planos em ambientes controlados; executar testes online; desenvolver benchmarks de recuperação; ampliar o realismo dos incidentes; avaliar falhas múltiplas, efeitos atrasados e cascatas; e aplicar testes estatísticos. |
| P32 |  | **SCORE_RQ** | **4,0 / 5,0** | **P + T + T + P + T** |  | O estudo apresenta elevada aderência à arquitetura, RCA, observabilidade multimodal e planejamento de recuperação. A cobertura é parcial para autonomia e governança, pois o agente não realiza execução e validação online no experimento e não implementa planejamento iterativo ou supervisão humana formal ao longo de todo o ciclo. |

### Observação crítica sobre o ciclo de recuperação

O resumo utiliza expressões como “recovery execution” e “closed-loop solution”. Entretanto, a Seção 4.4 informa explicitamente que os planos foram avaliados **offline**, sem execução em sistema ativo. A métrica mede a cobertura das ações presentes em playbooks especializados, e não o sucesso operacional da recuperação. O próprio artigo afirma que implantação controlada, validação online e canary release ainda são necessárias. Portanto, GALR deve ser interpretado como um framework de **RCA e planejamento de recuperação assistido por LLM**, e não como evidência consolidada de remediação autônoma em produção.

### Observação sobre os resultados experimentais

A avaliação contempla:

- **Customer Service:** 23.183 traces, 67 serviços e 24 falhas injetadas.
- **Power Grid Resource:** 19.872 traces, 89 serviços e 32 falhas injetadas.
- **SockShop:** 8.981 traces, 15 serviços e 30 falhas injetadas.
- **Falhas:** atraso de rede, perda de pacotes, estresse de CPU, estresse de memória, falha de pod e encerramento de pod.
- **Limite experimental:** cada trace contém, no máximo, uma falha injetada associada a uma única instância de serviço.

Essa configuração favorece supervisão inequívoca e comparações reproduzíveis, mas não representa integralmente incidentes simultâneos, falhas naturais de cauda longa ou propagação tardia em produção.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P32 | Estudo empírico experimental com framework GNN–LLM para RCA e planejamento de recuperação | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é claramente delimitado: sinais multimodais, dependências profundas e dinâmicas, alertas ruidosos, caminhos ambíguos de propagação e playbooks manuais pouco adaptáveis. A solução proposta combina grafo multimodal, GAT, enriquecimento semântico por LLM e recuperação baseada em casos. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo detalha equações, fluxo do algoritmo, normalização, construção do grafo, GAT de duas camadas com quatro cabeças, AdamW, taxa de aprendizado de 0,001, batch de 32, 30 épocas, gradient clipping, datasets, divisão 6:4, falhas injetadas, ferramentas de observabilidade, LLM, modelo de embeddings e biblioteca com 500 casos. Entretanto, não fornece o código-fonte, os dados estão disponíveis apenas sob solicitação, o limiar de consistência não é informado, os prompts e parâmetros do LLM não são integralmente especificados, as sementes não são registradas e os resultados são médias de apenas duas execuções sem teste de significância. Esses fatores impedem uma reprodução fiel.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A avaliação utiliza três datasets, 52.036 traces, diferentes topologias e seis tipos de falha. GALR é comparado com seis baselines de RCA, avaliado com Top-1, Top-3, Top-10 e MRR, e submetido a ablação. O módulo de recuperação é comparado em configurações zero-shot, few-shot e RAG. A evidência é quantitativa e diversificada. Como ressalva, as falhas são controladas, únicas por trace, e a recuperação não é executada online.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões refletem os resultados de localização e geração de estratégias e reconhecem explicitamente os limites da injeção de falhas, das labels por janela, da avaliação offline, das duas execuções e da ausência de significância estatística. As direções futuras são diretamente derivadas desses limites: escalabilidade, guardrails, validação online e benchmarks mais realistas.

---

## Parecer final do revisor

GALR apresenta forte aderência ao escopo da RSL ao integrar métricas, logs, traces, GNN, LLM e RAG em um fluxo de RCA e planejamento de recuperação. O estudo oferece arquitetura detalhada, métricas quantitativas, comparação com baselines e ablação. Sua principal limitação é que a recuperação permanece offline e baseada na semelhança com playbooks, sem comprovação de execução segura ou redução de MTTR em ambiente operacional.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada pela relevância direta para RCA, apoio à decisão e geração de ações de recuperação em microserviços. As ressalvas decorrem da autonomia parcial, da ausência de execução online, do cenário de falha única, da falta de métricas de MTTD, MTTR e carga cognitiva, da ausência de testes estatísticos e da cobertura incompleta de accountability e governança. O estudo deve ser utilizado como evidência de **planejamento de recuperação assistido por agente LLM**, não como validação de remediação autônoma completa.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
