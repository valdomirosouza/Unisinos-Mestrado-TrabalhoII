# Avaliação do artigo P78 — Ciclo 2 da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P78  
**Artigo:** Loumachi, F. Y.; Ghanem, M. C.; Ferrag, M. A. *Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models*. *Computers*, 14, 67, 2025.  
**Fonte exclusiva:** PDF fornecido, 42 páginas.  
**DOI:** https://doi.org/10.3390/computers14020067

## Etapa 0 — Tabela A: extração bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P78 | Computers | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado no protocolo) | [VERIFICAR] (A2 informado no protocolo) | Proposta de framework com prova de conceito e avaliação experimental em cenários sintéticos | 10.3390/computers14020067 |

**Fonte no artigo:** página 1 (identificação editorial, ano, DOI e resumo); Seções 3–5, pp. 9–33 (método, implementação e avaliação). O quartil Q1 e o Qualis A2 constam somente no prompt de avaliação, não constituindo comprovação bibliométrica pelo PDF.

## Etapa 1 — Triagem de elegibilidade

| Critério | Avaliação | Evidência |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicação em 13 fev. 2025 (p. 1) |
| Veículo de publicação identificado | Atendido | *Computers*, volume 14, artigo 67 (p. 1) |
| Citações ≥ 1 | Pendente | Contagem não comprovada no PDF; consultar base indexadora |
| SJR Q1–Q2 | Pendente | Q1 informado como insumo no protocolo, mas não demonstrável pelo PDF; confirmar no SCImago Journal Rank |
| Qualis A1–A2 | Pendente | A2 informado como insumo no protocolo, mas não demonstrável pelo PDF; confirmar na Plataforma Sucupira / Qualis CAPES e critérios do quadriênio aplicável |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis)**. A extração completa pode prosseguir conforme o protocolo. O estudo foi informado como aprovado na triagem e com Comparison N/A na extração PICOC; isso não substitui a checagem bibliométrica.

## Etapa 2 — Tabela B: classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P78 | Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | Seção 2.3, pp. 8–9; Seções 3 e 4.1, pp. 9–21; Seção 6.2, p. 35 | **a)** O agente é descrito como autônomo no processo de recuperação contextual, mas não há taxonomia rigorosa de níveis de autonomia. **b)** Apresenta uso de ferramentas de recuperação, base de conhecimento e supervisão humana; não detalha planejamento autônomo e memória persistente. **c)** A decisão é apoiada por relatórios e análises, cabendo ao especialista a validação e o julgamento final. Não comprova decisão operacional autônoma. |
| P78 | Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | Seções 3.1–3.2, pp. 10–13; Figura 7 e Algoritmo 1, pp. 18–19; Seções 4.1–4.3, pp. 20–23 | **a)** Arquitetura de agente RAG especializado, com base de conhecimento de eventos, fragmentação por evento, embeddings, recuperação e geração. **b)** Llama 3.1 8B, mxbai-embed-large, similaridade cosseno, Python, PyTorch, NumPy, pandas e GPU CUDA. **c)** Há enriquecimento semântico e correlação temporal, mas não são demonstradas orquestração multiagente implementada, observabilidade operacional contínua, guardrails executáveis ou operação em produção. |
| P78 | Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | Seção 4.3, Tabela 4, pp. 22–23; Seções 5.2–5.3, Tabelas 5 e 8, pp. 23–32 | **a)** Relata geração de cronologias interpretáveis e apoio à identificação de evidências. **b)** Acurácia 95,52%, relevância 94,51%, exact match 100%, top-k 100%, agregado 97,51% em configuração controlada. **c)** Evidência experimental baseada em seis cenários sintéticos, sem implantação industrial, grupo de controle convincente para produtividade ou medição direta de MTTD, MTTR, tempo de resposta ou carga cognitiva. Métricas medem qualidade das saídas, não ganhos operacionais. |
| P78 | Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | Seção 4, pp. 19–21; Seções 6.1–6.2, pp. 33–36; Seção 6.3, p. 36 | **a)** Discute alucinações, limitações de tokens, escalabilidade, generalização, anti-forense e qualidade das evidências. **b)** Aborda privacidade, confidencialidade, consentimento, viés, justiça e implicações legais. **c)** Propõe revisão por especialistas, anonimização, auditorias de viés, engenharia de prompts e mecanismos de privacidade; são principalmente recomendações, e não controles comprovadamente implementados. |
| P78 | Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | Seções 6.1–6.3, pp. 33–36; Seção 7, pp. 36–37 | Identifica necessidade de dados reais, cenários complexos com anti-forense, avaliações específicas de DFIR, novos benchmarks, aumento de escala, modelos maiores e agentes especializados para correlação, cronologia e identificação de causa raiz. Discute lacuna de estruturas regulatórias específicas, sem fornecer agenda aprofundada de observabilidade operacional. |
| **P78** | **TOTAL** | **SCORE_RQ** | **3,5 / 5,0** | **P + P + P + T + T** | | **Alta relevância contextual para DFIR; evidência limitada para Agentic AI operacional em produção.** |

### Observações sobre a classificação

A terminologia **“autonomous context-augmented agent”** utilizada pelos autores não equivale, isoladamente, à demonstração de planejamento autônomo, execução de ações de contenção ou coordenação multiagente. Na Seção 6.3 (p. 36), a inclusão de agentes especializados autônomos aparece como **trabalho futuro**. A interpretação mantém separadas capacidades implementadas e capacidades apenas propostas.

Embora RQ4 e RQ5 recebam classificação T por cobrirem explicitamente as dimensões solicitadas, a nota **não afirma** que todos os mecanismos de governança tenham sido implementados ou empiricamente validados.

## Etapa 3 — Tabela C: avaliação de qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P78 | Proposta de framework e prova de conceito experimental com dados sintéticos | Y (1,0) | P (0,5) | P (0,5) | Y (1,0) | **3,0 / 4,0** | **Alta** |

**QA1 — Objetivos claros: Y (1,0).** A introdução identifica a dificuldade de correlacionar evidências e reconstruir cronologias contextualizadas; formula três questões de pesquisa próprias (pp. 2–3). O GenDFIR e o papel do agente RAG são descritos na Seção 3 (pp. 9–10). O objetivo é delimitado e verificável, embora não vise um copiloto de contenção de ponta a ponta.

**QA2 — Metodologia replicável: P (0,5).** Existem arquitetura, equações de chunking e recuperação, Algoritmo 1 (p. 18), Figura 7 (p. 18), modelos e configurações: Llama 3.1 8B zero-shot, mxbai-embed-large, temperatura 0,1, máximo de 2.000 tokens, n=1, RTX 4060 e CUDA 12.6 (Seções 3–4, pp. 10–23). Contudo, descrição e trechos de código não estabelecem, por si sós, replicação independente integral de todas as etapas de avaliação, decisões de anotação humana e preparação de dados.

**QA3 — Base de evidências sólidas: P (0,5).** Há experimentação com seis cenários sintéticos, métricas definidas e resultados numéricos nas Tabelas 4, 5 e 8 (pp. 22–32): acurácia 95,52%, relevância 94,51%, EM 100%, Top-K 100% e taxa agregada 97,51%. Porém, a evidência é predominantemente uma prova de conceito em ambiente controlado, sem estudo industrial, cenários adversariais complexos ou benefício causal sobre tempos de resposta. Conforme a rubrica, prova de conceito/toy example é P, não Y.

**QA4 — Conclusões coerentes: Y (1,0).** A conclusão descreve potencial e estágio de prova de conceito (Seção 7, pp. 36–37). As Seções 5.3 e 6 (pp. 32–36) reconhecem limitações de generalização, dados sintéticos, riscos éticos, qualidade de resultados e necessidades de validação adicional. Eventuais comparações funcionais com ferramentas existentes (Tabela 9, p. 32) não devem ser interpretadas como benchmark quantitativo controlado.

## Parecer final do revisor

### Síntese

O P78 apresenta o GenDFIR, um framework de IA generativa com RAG e agente especializado para análise de artefatos, correlação de eventos e reconstrução semântica de linhas do tempo de incidentes cibernéticos. Sua contribuição é diretamente pertinente ao apoio à decisão de especialistas DFIR, especialmente em recuperação contextual e geração de relatórios. O estudo possui resultados quantitativos em seis cenários sintéticos, mas não comprova ganhos de MTTD, MTTR, carga cognitiva ou desempenho operacional em produção. Também não demonstra um sistema multiagente completo: agentes adicionais especializados são propostos como trabalho futuro. A aplicabilidade à RSL é relevante, porém circunscrita ao apoio investigativo, e não à resposta autônoma de ponta a ponta.

### Recomendação: **INCLUIR COM RESSALVAS**

**Justificativa:** O trabalho responde às dimensões centrais de arquitetura RAG, apoio à decisão, evidência experimental e desafios éticos. Deve ser classificado como **framework assistivo de DFIR com agente RAG e automação parcial**, não como evidência de autonomia plena para executar resposta a incidentes. A inclusão definitiva depende da confirmação dos três critérios bibliométricos pendentes.

### Pendências de verificação externa

1. **Citações ≥ 1:** confirmar em base indexadora (por exemplo, Scopus, Web of Science ou outra adotada no protocolo).
2. **SJR Q1–Q2:** confirmar o quartil e o ano de referência de *Computers* no **SCImago Journal Rank**; Q1 foi informado no prompt, mas não constatado no PDF.
3. **Qualis A1–A2:** confirmar na **Plataforma Sucupira / Qualis CAPES**, inclusive a aplicabilidade da regra e período de avaliação; A2 foi informado no prompt, mas não consta do artigo.

**Nota metodológica:** nenhuma fonte externa foi consultada para esta avaliação. Valores e classificações bibliométricas informados no protocolo foram distinguidos de evidências diretamente verificáveis no PDF.
