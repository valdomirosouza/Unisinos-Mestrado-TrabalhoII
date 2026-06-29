# Avaliação do Estudo P30

## Identificação do estudo

**ID:** P30  
**Artigo:** *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports*  
**Autores:** Hongwei Li e Yongjun Wang  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q1 e Qualis A2.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P30 | *Big Data and Cognitive Computing*, v. 10, artigo 60 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico exploratório com dataset de defeitos reais, classificação supervisionada, localização de módulos, geração de recomendações por LLM e avaliação humana | 10.3390/bdcc10020060 |

**Evidência bibliométrica:** a primeira página identifica o periódico, o volume 10, o número do artigo 60, o ano de 2026 e o DOI. O artigo foi recebido em 12 de janeiro de 2026, aceito em 12 de fevereiro de 2026 e publicado em 13 de fevereiro de 2026.

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
| Ano ≥ 2020 | *Big Data and Cognitive Computing*, volume 10, artigo 60, publicado em 2026, p. 1. | Atendido |
| Publicação identificável | Periódico, volume, artigo e DOI são apresentados na primeira página. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério bibliométrico interno que determine inelegibilidade. A extração completa prossegue, condicionada à confirmação dos três itens externos.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | RQ1 — Context Definitions | Não tem conteúdo suficiente | N | Seções 3.4 e 4.4, pp. 8–10; Figura 1, p. 4. | O estudo não define Agentic AI, níveis de autonomia, planejamento, memória agêntica ou supervisão humana durante a tomada de decisão. O próprio artigo afirma que o LLM é utilizado somente como gerador textual condicional na etapa final, enquanto o diagnóstico é realizado por componentes estatísticos ou determinísticos. A arquitetura não possui ciclo autônomo de percepção, planejamento, ação e reflexão. Assim, as subdimensões de autonomia, características centrais e modelo decisório agêntico não são cobertas de forma suficiente. |
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seção 3, pp. 4–9; Figura 1; Algoritmos 1–4; Seção 4, pp. 9–10. | O artigo descreve uma arquitetura modular composta por construção do dataset, classificação da causa raiz, localização do módulo e geração de recomendações. Informa Python 3.10, scikit-learn, NumPy, TF-IDF, regressão logística, similaridade por cosseno, GPT-5.2 e Qwen3-235B-A22B. O prompt estruturado, os padrões de reparo e os resultados intermediários funcionam como mecanismos de grounding e redução de alucinações. Entretanto, não há orquestração agêntica, memória operacional, seleção autônoma de ferramentas, observabilidade do agente, guardrails de execução ou mecanismos de fallback em produção. |
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seção 5, pp. 10–15; Tabelas 3–6; Figuras 2–3. | O estudo apresenta benefícios qualitativos e quantitativos. A classificação da causa raiz alcança acurácia de 68,8% e Macro-F1 de 0,421. A localização de módulos obtém Top-1 de 70,5% e Top-2 de 84,1%, com processamento inferior a um segundo para 150 issues. Na avaliação entre engines, o modelo alcança 64,0% de acurácia e Macro-F1 de 0,405 em TensorRT-LLM sem retreinamento. A avaliação humana com 50 issues e cinco pesquisadores reporta, para GPT-5.2, médias de 3,7 em correção, 3,6 em utilidade e 4,3 em clareza, além de concordância entre avaliadores por Fleiss’ κ. A evidência é empírica e baseada em defeitos reais, embora esteja voltada à depuração de software, não à resposta operacional a incidentes. |
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Introdução, pp. 1–3; Seções 5.2–5.5, pp. 11–15; Seção 6, pp. 15–16. | O artigo discute desafios técnicos importantes: dados limitados e desbalanceados, categorias raras, dependência da qualidade dos relatos, localização apenas em nível de módulo, propagação de erros entre etapas e dificuldade de reproduzir bugs dependentes de hardware. Os mecanismos de mitigação incluem balanceamento de classes, validação cruzada estratificada, prompts estruturados, padrões de reparo, intermediários interpretáveis e avaliação humana. Entretanto, não aborda de forma substancial accountability, privacidade, segurança do uso do LLM, controle de acesso, auditoria operacional, responsabilidade por sugestões incorretas ou governança institucional. |
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | RQ5 — Research Gaps | Respondida Plenamente | T | Seções 6 e 7, pp. 15–16. | As limitações e direções futuras são explícitas: ampliar o dataset para outras engines e categorias, incorporar commits, diffs, stack traces e relações de dependência, melhorar a robustez diante de issues incompletas, avançar da localização por módulo para função ou bloco de código e integrar o método a técnicas de reparo e testes automatizados. O artigo também reconhece a necessidade de ampliar a avaliação humana e investigar técnicas de reparo mais automatizadas. |
| P30 |  | **SCORE_RQ** | **3,0 / 5,0** | **N + P + T + P + T** |  | O estudo oferece evidência empírica relevante para RCA, localização de falhas e apoio à manutenção. Contudo, sua aderência ao núcleo de Agentic AI é baixa: o LLM não atua como agente, não planeja, não seleciona ferramentas e não executa respostas em ciclo fechado. |

### Observação sobre a natureza do sistema

Apesar de empregar um LLM para gerar recomendações de reparo, o sistema não é apresentado como agente autônomo. O artigo delimita o LLM como um componente de geração textual condicionado por resultados produzidos por classificadores e mecanismos de similaridade. Portanto, a solução se aproxima de um **assistente de depuração baseado em pipeline**, não de um copiloto agêntico com autonomia deliberativa.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P30 | Estudo empírico exploratório sobre diagnóstico e recomendação de reparos em engines de inferência LLM | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O artigo delimita três problemas: inexistência de datasets públicos bem anotados, dependência de execução e instrumentação dinâmica e ausência de abordagens que ofereçam recomendações de reparo interpretáveis. A solução é explicitada como um pipeline estático que utiliza issues reais para classificar causas, localizar módulos e gerar orientações de reparo. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo descreve o processo de coleta e anotação, a taxonomia, os algoritmos, o TF-IDF com unigramas e bigramas, a regressão logística com balanceamento de classes, a validação cruzada estratificada de cinco partes, a similaridade por cosseno, os modelos de linguagem, o ambiente de hardware e software e o template de prompt. Também fornece endereço para código e dados. Entretanto, faltam detalhes sobre sementes aleatórias, limiares de frequência, hiperparâmetros completos, temperatura e parâmetros das APIs, seleção dos comentários das issues, regras integrais dos padrões de reparo e resolução de discordâncias na anotação. Há ainda uma diferença entre a descrição conceitual da representação dos módulos por agregação de issues e a implementação por documentos manuais de descrição. Esses fatores limitam a reprodução fiel.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A avaliação utiliza 176 issues reais do vLLM e 100 do TensorRT-LLM, compara três classificadores, emprega validação cruzada, mede Accuracy, Macro-F1, Top-1, Top-2 e tempo de processamento, conduz teste de generalização entre engines e inclui avaliação humana independente com cinco pesquisadores e 50 issues. A concordância é analisada com Fleiss’ κ. Embora os resultados de classificação sejam modestos e o corpus seja pequeno, a validação é diversificada e empiricamente fundamentada.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões reconhecem que a classificação automática é viável, porém ainda limitada pelo tamanho e desbalanceamento dos dados. O artigo também discute a dependência da qualidade das issues, a granularidade limitada da localização, a necessidade de investigação manual e o efeito cascata dos erros de diagnóstico sobre as recomendações. As direções futuras decorrem diretamente dessas limitações.

---

## Parecer final do revisor

O estudo apresenta qualidade metodológica alta e contribui para RCA, localização de falhas e geração de recomendações em engines de inferência LLM. Sua evidência empírica é relevante para manutenção de software e assistência ao desenvolvedor. Entretanto, a solução não caracteriza Agentic AI e não está diretamente vinculada ao ciclo operacional de resposta a incidentes, MTTD, MTTR ou redução mensurada da carga cognitiva de equipes SRE.

### Recomendação

**EXCLUIR DO CORPUS PRINCIPAL.**

A exclusão é recomendada por desalinhamento temático com o núcleo da RSL. O LLM funciona como gerador textual condicionado dentro de um pipeline determinístico, sem autonomia, planejamento, memória, seleção de ferramentas ou atuação no ambiente. Além disso, o estudo trata defeitos de software reportados em GitHub, e não detecção, triagem, diagnóstico ou recuperação de incidentes operacionais. O trabalho pode ser preservado como referência de apoio sobre RCA estática, explicabilidade e avaliação humana de sugestões de reparo, mas não como estudo primário de Agentic AI Copilot para Resposta a Incidentes.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
