# Avaliação do Estudo P38

## Identificação do estudo

**ID:** P38  
**Artigo:** *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation*  
**Autores:** Irina Radeva, Ivan Popchev, Lyubka Doukovska e Miroslava Dimitrova  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas pelo artigo, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A2.

---

## Etapa 0 - Extração bibliométrica

### Tabela A - Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P38 | *Electronics*, v. 14, artigo 4883 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental comparativo entre RAG de agente único e quatro estratégias de coordenação multiagente | 10.3390/electronics14244883 |

**Evidência bibliométrica:** a primeira página identifica o periódico *Electronics*, o volume 14, o artigo 4883, o ano de 2025 e o DOI. O manuscrito foi recebido em 15 de novembro de 2025, revisado em 7 de dezembro de 2025, aceito em 8 de dezembro de 2025 e publicado em 11 de dezembro de 2025.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 - Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano >= 2020 | O artigo foi publicado em 11 de dezembro de 2025, p. 1. | Atendido |
| Publicação identificável | O PDF apresenta periódico, volume, número do artigo e DOI, p. 1. | Atendido |
| Citações >= 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1-Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1-A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério bibliométrico interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos três itens externos.

---

## Etapa 2 - Extração e classificação das RQs

### Tabela B - Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | RQ1 - Context Definitions | Parcialmente Respondida | P | Introdução e Seções 1.1-1.2, pp. 1-3; Seção 2, pp. 3-5; Seções 3.2.1-3.2.6, pp. 6-8. | O artigo caracteriza quatro modelos de coordenação: colaborativo, sequencial, competitivo e hierárquico. Também descreve protocolos decisórios explícitos, como agregação, refinamento em pipeline, seleção por confiança e síntese manager-worker. As características centrais incluem processamento distribuído, RAG, compartilhamento ou fragmentação de contexto, consenso e comunicação entre agentes. Entretanto, não define níveis de autonomia, planejamento autônomo, supervisão humana, limites de atuação ou memória agêntica persistente. |
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | RQ2 - Engineering Architecture | Respondida Plenamente | T | Seção 3.1, pp. 5-6; Figuras 1-2, p. 6; Seções 3.2-3.4, pp. 6-15; Apêndice A, pp. 29-32. | A arquitetura PaSSER possui camadas de infraestrutura, aplicação, avaliação e armazenamento. O ambiente inclui Mistral 7B, Llama 3.1 8B, Granite 3.2 8B, ChromaDB, embeddings, RAG com LangChain, backend Python, frontend React, Ollama, MLX, MongoDB, métricas CPS/T-CPS e registro verificável por blockchain. As capacidades avançadas incluem quatro estratégias de coordenação, memória de contexto, recuperação independente ou compartilhada, monitoramento em tempo real, pontuação de confiança, síntese em duas fases, fallback para a melhor resposta e avaliação de estabilidade. |
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | RQ3 - Evidence Benefits | Respondida Plenamente | T | Resumo, p. 1; Seções 3.2-3.4, pp. 6-15; Seção 4, pp. 15-23; Tabelas 1-4 e análises de desempenho, estabilidade e eficiência. | O estudo fornece evidência quantitativa e qualitativa sobre a utilidade da coordenação multiagente. O resultado central é negativo: todas as 28 configurações multiagente degradaram em relação aos baselines RAG de agente único, com variação de -4,4% a -35,3%. Mistral otimizado hierárquico apresentou a menor degradação, de aproximadamente 4,4%, enquanto Llama tolerou melhor estratégias sequenciais e hierárquicas. São utilizados CPS, T-CPS, nove métricas componentes, coeficiente de variação, latência, consumo de tokens, testes t pareados, intervalos de confiança e Cohen's d. A evidência decorre de 3.100 avaliações controladas, porém está restrita a perguntas factuais no domínio agrícola e não mede incident response, MTTD, MTTR ou carga operacional humana. |
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | RQ4 - Challenges & Ethics | Parcialmente Respondida | P | Seções 1.1-1.2, pp. 2-3; Seções 3.2.6-3.2.7, pp. 8-9; Seções 4-6, pp. 15-28. | O artigo cobre desafios técnicos de forma consistente: overhead de coordenação, fragmentação do contexto recuperado, propagação de erros, variabilidade, seleção inadequada por confiança, truncamento de respostas, aumento de latência e tokens, limitações dos modelos pequenos e sensibilidade à estratégia. Há mecanismos técnicos como contexto compartilhado, consenso em duas fases, monitoramento, fallback e registro verificável. Entretanto, não discute segurança, privacidade, accountability, supervisão humana, controle de privilégios, impacto de decisões ou governança ética em sistemas críticos. |
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | RQ5 - Research Gaps | Respondida Plenamente | T | Introdução, pp. 2-3; Discussão e Conclusão, pp. 23-28; seção de limitações e direções futuras, pp. 27-28. | O estudo identifica lacunas explícitas: domínio único, tarefas factuais, modelos de 7-8 bilhões de parâmetros, agentes homogêneos, estratégias simples, ausência de debate iterativo e limitação da comparação temporal entre hardwares. As direções futuras incluem modelos acima de 70 bilhões de parâmetros, equipes heterogêneas, prompts específicos por função, mecanismos avançados de consenso, seleção adaptativa da estratégia e ajuste conjunto de recuperação e coordenação. |
| P38 |  | **SCORE_RQ** | **4,0 / 5,0** | **P + T + T + P + T** |  | O estudo oferece evidência robusta sobre arquitetura, coordenação e desempenho de sistemas LLM multiagentes. Contudo, sua aderência ao escopo específico da RSL é indireta, pois avalia perguntas factuais sobre agricultura e não aborda detecção, diagnóstico, contenção ou recuperação de incidentes. |

### Observação sobre a natureza agêntica

Os componentes são denominados agentes e executam protocolos de coordenação bem definidos. Contudo, o comportamento é fortemente delimitado por pipelines fixos. Os agentes não formulam objetivos próprios, não escolhem ferramentas dinamicamente, não observam um ambiente operacional e não executam ações externas. O estudo investiga principalmente **coordenação de múltiplas instâncias de LLM com RAG**, não autonomia operacional em ciclo fechado.

### Observação sobre os resultados negativos

A ausência de ganho multiagente é uma contribuição relevante. As 28 configurações multiagente apresentaram degradação estatisticamente observável em relação aos três baselines calibrados. Os resultados indicam que adicionar agentes não produz benefício automático. Em tarefas factuais com modelos locais pequenos, o overhead de coordenação pode superar qualquer ganho obtido por diversidade ou consenso.

### Observação sobre o domínio da avaliação

O corpus contém 100 pares de perguntas e respostas extraídos do *Climate-Smart Agriculture Sourcebook*. Portanto, os resultados não demonstram eficácia em AIOps, SRE, SOC ou resposta a incidentes. A transferência das conclusões para esses contextos exigiria validação com telemetria operacional, casos de incidentes, runbooks, ferramentas e operadores humanos.

---

## Etapa 3 - Avaliação de qualidade

### Tabela C - Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P38 | Estudo empírico experimental comparativo de arquiteturas RAG e coordenação multiagente | Y (1,0) | Y (1,0) | Y (1,0) | Y (1,0) | **4,0 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 - Objetivos claros: Y (1,0).**  
O problema e os objetivos são explícitos. O estudo investiga se a coordenação multiagente melhora um RAG previamente calibrado, separa o efeito de overhead do efeito de fragmentação da recuperação, compara interações entre modelos e estratégias e avalia o trade-off entre desempenho médio e consistência. Evidências: Seção 1.1, pp. 2-3.

**QA2 - Metodologia replicável: Y (1,0).**  
O artigo detalha arquitetura, versões dos modelos, hardware, software, estratégias, protocolos de consenso, modos de recuperação, limiares, corpus, métricas, pesos, fórmulas, parâmetros de geração e testes estatísticos. O Apêndice A apresenta especificações adicionais e prompts. Código-fonte, corpus, resultados brutos, scripts de análise e instruções de instalação são declarados como públicos no repositório do projeto. Há uma pequena variação terminológica entre Flask e FastAPI na descrição do backend, mas os artefatos disponibilizados permitem verificar a implementação.

**QA3 - Base de evidências sólidas: Y (1,0).**  
A avaliação inclui três modelos, quatro estratégias, versões originais e otimizadas, recuperação independente e compartilhada, 31 configurações e 3.100 execuções. Os baselines foram calibrados separadamente com 369 questões. O artigo utiliza métricas multidimensionais, análise de estabilidade, testes t pareados, intervalos de confiança e tamanhos de efeito. A evidência é sólida para o cenário experimental definido, embora sua validade externa seja limitada.

**QA4 - Conclusões coerentes: Y (1,0).**  
As conclusões refletem os resultados negativos e evitam generalização irrestrita. O artigo reconhece limitações de domínio, tamanho dos modelos, homogeneidade dos agentes, simplicidade das estratégias e heterogeneidade de hardware. As recomendações futuras decorrem diretamente dessas limitações e dos padrões observados.

---

## Parecer final do revisor

O estudo é metodologicamente forte e oferece evidência importante de que arquiteturas multiagentes podem degradar qualidade, estabilidade e eficiência quando aplicadas a RAG factual com modelos locais pequenos. Sua contribuição é relevante para decisões arquiteturais e para evitar a adoção acrítica de múltiplos agentes. Entretanto, não investiga resposta a incidentes, ambientes operacionais, ferramentas de SRE ou SOC, autonomia de ação ou interação humano-agente.

### Recomendação

**EXCLUIR DO CORPUS PRINCIPAL.**

A exclusão é recomendada por desalinhamento temático com o núcleo da RSL. O domínio experimental é agricultura e a tarefa é question answering factual. Não há incidentes, telemetria operacional, RCA, triagem, contenção, remediação, MTTD, MTTR ou carga cognitiva de técnicos. O artigo pode ser mantido como referência metodológica ou de apoio para discutir riscos de overhead e seleção de arquitetura multiagente, mas não como estudo primário sobre Agentic AI Copilot para Resposta a Incidentes.

### Pendências de verificação externa

1. **Número de citações >= 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1-Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1-A2:** verificar na Plataforma Sucupira / Qualis CAPES.
