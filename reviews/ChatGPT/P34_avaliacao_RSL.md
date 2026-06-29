# Avaliação do Estudo P34

## Identificação do estudo

**ID:** P34  
**Artigo:** *Analysing the Role of LLMs in Cybersecurity Incident Management*  
**Autores:** Gavin Jones, Dimitrios Kasimatis, Nikolaos Pitropakis, Richard Macfarlane e William J. Buchanan  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas pelo artigo, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A2.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P34 | *International Journal of Information Security*, v. 24, artigo 228 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com protótipo de copiloto, comparação de quatro LLMs, três níveis de contexto e avaliação quantitativa e qualitativa | 10.1007/s10207-025-01144-7 |

**Evidência bibliométrica:** a primeira página identifica o periódico, o volume 24, o artigo 228, o ano de 2025 e o DOI. O manuscrito foi recebido em 27 de junho de 2025, aceito em 19 de outubro de 2025 e publicado online em 30 de outubro de 2025.

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
| Ano ≥ 2020 | *International Journal of Information Security*, volume 24, publicado em 2025, p. 1. | Atendido |
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
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | RQ1 — Context Definitions | Não tem conteúdo suficiente | N | Seções 2.2 e 4.1, pp. 2–5; Seção 6.1.1, p. 11. | O estudo avalia LLMs como assistentes ou copilotos que recebem a descrição de um incidente e produzem recomendações. Não define Agentic AI, níveis de autonomia, memória agêntica, planejamento autônomo, reflexão, seleção dinâmica de ferramentas ou um ciclo de percepção–ação. A decisão final permanece com o usuário e a supervisão humana aparece principalmente como recomendação de governança. O modelo operacional é um pipeline de prompt e resposta, não um agente autônomo. |
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seções 4.1–4.2, pp. 4–6; Seção 4.1.1, p. 5; Seção 6.1.1, p. 11. | O artigo descreve uma arquitetura cliente–servidor: scripts Python executados localmente, cenários em JSON, prompt wrapper, chamadas à API da OpenAI, registros em XML e posterior conversão para XLSX. São avaliados GPT-3.5-turbo, GPT-4-0125-preview, GPT-4o e o1-preview. Há logging para depuração e três regimes de contexto, incluindo runbook NIST e conhecimento de incidentes anteriores. Entretanto, não existem orquestração multiagente, memória persistente, RAG implementado, seleção autônoma de ferramentas, observabilidade operacional do copiloto ou guardrails incorporados ao protótipo. |
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seções 4.1–4.3, pp. 4–8; Seção 5, pp. 8–10; Figuras 1–7; Tabela 1 do Apêndice, p. 12; Seção 6, pp. 10–11. | O estudo apresenta benefícios qualitativos diretamente relacionados à resposta a incidentes, identificando modelos mais adequados a diferentes fases. A avaliação compreende dez cenários, quatro LLMs, três condições de contexto e dez repetições, totalizando 1.200 invocações. As métricas incluem BERTScore, concisão, coerência por NLP, clareza, relevância, terminologia específica e coerência lógica avaliada por LLM. GPT-4o e GPT-3.5 se destacam em clareza, consistência e coerência para contenção, erradicação e recuperação; GPT-o1 e GPT-4 apresentam vantagens em relevância, terminologia, concisão e raciocínio para preparação e análise posterior. A evidência é experimental, mas baseada em cenários textuais, sem incidentes operacionais reais, tempo de resposta, MTTD, MTTR ou medição direta da carga cognitiva. |
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | RQ4 — Challenges & Ethics | Respondida Plenamente | T | Seção 2.2, p. 3; Seção 6 e Seções 6.1–6.1.1, pp. 10–11; Conclusão, pp. 11–12. | O artigo discute alucinações, dependência da qualidade das fontes em RAG, limites de contexto, variabilidade probabilística, viés do LLM-as-a-judge e risco de recomendações operacionalmente incorretas. Os desafios éticos incluem falsa confiança, erosão da competência humana, enfraquecimento da contratação e treinamento, ausência de cadeia de accountability, privacidade e uso ofensivo de LLMs. Os mecanismos recomendados abrangem human-in-the-loop, aprovação para ações de alto impacto, controle duplo, confiança calibrada, abstention, evidência e proveniência, implantação em shadow/advisory mode, versionamento fixo, logs de auditoria, least privilege, segregação de funções, red teaming, minimização de dados e inferência privada ou on-premise. |
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção 6, pp. 10–11; Seção 7, pp. 11–12. | O artigo aponta como lacunas a dependência de um único modelo julgador e uma única rubrica, a ausência de correção operacional nas métricas, os limites de contexto e o uso de configurações padrão. Como direções futuras, propõe avaliar outros modelos e alternativas locais, implementar RAG e consultas iterativas, variar formatos de entrada, incorporar participação humana mais realista, medir tempo médio de resposta e avaliar usabilidade com cenários e runbooks especializados. |
| P34 |  | **SCORE_RQ** | **3,5 / 5,0** | **N + P + T + T + T** |  | O estudo apresenta forte aderência à avaliação de copilotos baseados em LLM para incident response, benefícios, riscos e supervisão humana. Sua aderência ao núcleo de Agentic AI é limitada, pois o protótipo não possui autonomia deliberativa, memória, ferramentas ou execução de ações no ambiente. |

### Observação sobre a natureza do sistema

O próprio estudo descreve a ferramenta como um **incident response assistant or copilot**. O fluxo experimental recebe um cenário, acrescenta diferentes níveis de contexto e solicita ao LLM recomendações de resposta. Não há execução automática, interação iterativa com o ambiente, validação das ações, aprendizagem ou replanejamento. Portanto, o trabalho oferece evidência direta sobre **LLM Copilot para Resposta a Incidentes**, mas não sobre um sistema Agentic AI completo.

### Observação crítica sobre as métricas

A Tabela 1 do Apêndice apresenta os valores completos, incluindo BERTScore entre **0,3258 e 0,4938**. Entretanto, o texto da Seção 5.1.1 afirma que o GPT-3.5 alcançou “4.9”, embora a métrica seja definida entre 0 e 1. O valor coerente com a tabela é aproximadamente **0,49**. Esta avaliação preserva os valores da tabela e registra a inconsistência textual, sem realizar correções não explicitadas pelos autores.

A avaliação qualitativa utiliza GPT-4o como único julgador para todas as respostas. Embora os autores repitam cada condição dez vezes e apliquem uma rubrica fixa, esse desenho não elimina viés do avaliador, preferência por estilos semelhantes ao próprio modelo ou discrepância entre qualidade textual e correção operacional.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P34 | Estudo empírico experimental com protótipo de copiloto LLM para resposta a incidentes | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitamente delimitado: os processos lineares e predominantemente humanos de resposta a incidentes podem ser lentos diante de ameaças complexas, enquanto LLMs oferecem capacidade de analisar grandes volumes de informação e produzir recomendações. O objetivo é avaliar a efetividade prática de diferentes LLMs em etapas de incident management e discutir riscos éticos e de accountability. Evidências: Resumo, Introdução e contribuições, pp. 1–2.

**QA2 — Metodologia replicável: P (0,5).**  
O estudo informa os quatro modelos, dez cenários, três níveis de contexto, dez repetições, total de 1.200 invocações, prompt wrapper, hardware, arquitetura cliente–servidor, OpenAI API, uso das configurações padrão e procedimentos de logging. Também apresenta as definições e escalas das métricas. Entretanto, o código não é disponibilizado no PDF, o dataset está disponível apenas mediante solicitação, nem todos os cenários e referências de avaliação são reproduzidos integralmente, não há sementes ou snapshots das configurações padrão da API, e o uso de um único LLM julgador limita a reprodução independente. Assim, a metodologia é detalhada, mas não integralmente replicável.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A validação empírica compara quatro LLMs em dez classes de incidentes, três regimes de contexto e dez repetições por condição. O estudo combina métricas quantitativas e qualitativas, apresenta resultados completos e discute diferenças entre modelos e etapas do ciclo de incident response. A evidência é relevante e suficientemente ampla para um experimento de copiloto textual. Como limitação, não há execução em SOC, usuários humanos, incidentes ao vivo ou avaliação da correção das ações após aplicação no ambiente.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões derivam das métricas reportadas e diferenciam modelos conforme suas características observadas. O artigo reconhece limitações do julgador único, das rubricas, do contexto, das configurações padrão e da ausência de correção operacional. Também relaciona essas limitações às propostas de RAG, modelos locais, novos formatos de entrada, métricas de tempo e estudos de usabilidade. Evidências: Seção 6 e Conclusão, pp. 10–12.

---

## Parecer final do revisor

O estudo apresenta aderência muito alta ao eixo **Copilot para Resposta a Incidentes**, pois implementa e avalia uma ferramenta que recomenda ações em diferentes fases do ciclo NIST. Sua contribuição mais forte está na comparação empírica entre LLMs, níveis de contexto e métricas de qualidade textual, além da discussão detalhada de supervisão e governança. A aderência a **Agentic AI** é baixa, porque o sistema não planeja, usa ferramentas, mantém memória ou atua autonomamente no ambiente.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada por sua relação direta com incident response, pela avaliação empírica de um copiloto e pela cobertura de riscos, accountability e human-in-the-loop. As ressalvas decorrem da ausência de características agênticas, da avaliação exclusivamente textual, do uso de cenários simulados, do único LLM julgador, da inexistência de métricas de MTTD, MTTR, tempo real de resposta e carga cognitiva, e da falta de validação das recomendações após execução. O estudo deve ser utilizado como evidência sobre **assistência por LLM e seleção de modelos ao longo do ciclo de incidentes**, não como validação de resposta autônoma.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
