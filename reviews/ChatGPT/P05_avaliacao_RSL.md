# Avaliação do artigo P05 — Corpus Fundacional

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P05  
**Artigo:** *A Survey of AIOps in the Era of Large Language Models*  
**Autores:** Lingzhe Zhang et al.  
**Natureza:** avaliação retroativa de estudo fundacional já incluído no Trabalho I. A decisão de inclusão herdada não é reaberta.  
**Fonte da análise:** exclusivamente o PDF anexado. As páginas abaixo são as páginas impressas do artigo.

## 0. Tabela A — Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P05 | *ACM Computing Surveys*, 58(2), artigo 44 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Survey / revisão sistemática da literatura de LLMs aplicados a AIOps | 10.1145/3746635 |

**Evidência:** folha de rosto, p. 1, e referência editorial, p. 2: publicação em setembro de 2025, veículo, volume, número e DOI. O resumo, p. 1, e seção 2, pp. 5–6, qualificam o estudo como survey com protocolo de revisão.

**Metadados fornecidos no prompt, mas não auditáveis no PDF:** SJR Q1 e Qualis A1 constam como previamente verificados nos metadados de entrada. Por exigência de rastreabilidade da presente avaliação, permanecem **[VERIFICAR]** na Tabela A até confronto com as fontes respectivas. O número de citações também não é estabelecido pelo PDF. Não confundir citações *recebidas* pelo artigo com referências que ele cita.

## 1. Elegibilidade (triagem documental)

| Critério | Resultado | Fundamentação |
|---|---|---|
| Ano ≥ 2020 | Atende | Publicação em setembro de 2025, pp. 1–2. |
| Publicação identificável | Atende | *ACM Computing Surveys*, volume 58, número 2, artigo 44, pp. 1–2. |
| Citações ≥ 1 | [VERIFICAR] | Não é possível determinar citações recebidas a partir do PDF. |
| SJR Q1–Q2 | [VERIFICAR] | Q1 informado nos insumos, não verificável no artigo. |
| Qualis A1–A2 | [VERIFICAR] | A1 informado nos insumos, não verificável no artigo. |

**Resultado formal:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR, Qualis)**. A análise prossegue porque o protocolo permite prosseguir em caso pendente e o estudo faz parte do corpus fundacional herdado.

## 2. Tabela B — Classificação das RQs (Tabela 5)

**Escala:** T = Respondida Plenamente (1,0); P = Parcialmente Respondida (0,5); N = Não tem conteúdo suficiente (0,0). As RQs abaixo são as da RSL atual, não as quatro questões de pesquisa internas do artigo.

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P05 | *A Survey of AIOps in the Era of Large Language Models* | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | §1.1, p. 3; §4.3 e Fig. 9, pp. 14–15; §5.5, pp. 20–21 | Apresenta cinco níveis crescentes de automação na remediação e discute uso de ferramentas e apoio a operadores, mas não formaliza um modelo geral de Agentic AI com planejamento, memória, supervisão humana e tomada de decisão. |
| P05 | *A Survey of AIOps in the Era of Large Language Models* | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | §3, pp. 6–11; §5 e Fig. 10, pp. 15–21; §7.4, p. 26 | Sistematiza métricas, logs, traces, relatórios de incidentes, RAG e geração aumentada por ferramentas; descreve integrações com toolchains. Não especifica arquitetura de referência em produção com memória, orquestração, guardrails e observabilidade do agente de ponta a ponta. |
| P05 | *A Survey of AIOps in the Era of Large Language Models* | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | §4.3, pp. 14–15; §6.1 e Fig. 11, pp. 21–23; §6.2, pp. 23–24 | Reúne benefícios qualitativos reportados e métricas de classificação, geração, execução e avaliação humana, com benchmarks de terceiros. Não consolida evidência própria de redução de MTTD, MTTR ou carga cognitiva. Os resultados empíricos mencionados pertencem aos estudos revisados. |
| P05 | *A Survey of AIOps in the Era of Large Language Models* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | §6.1.4, p. 23; §7 e §§7.1–7.4, pp. 24–26 | Discute alucinações, respostas inconsistentes, limites de contexto, custo, latência, generalização e riscos operacionais de integração. A discussão sistemática sobre accountability, governança, segurança, modelos de ameaça e controles de aprovação é insuficiente. |
| P05 | *A Survey of AIOps in the Era of Large Language Models* | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | §6.2, pp. 23–24; §7 e §§7.1–7.4, pp. 24–26; §8, p. 26 | Identifica e explica lacunas sobre benchmarking, eficiência temporal e econômica, utilização de traces, generalização durante evolução de software e integração com ferramentas legadas. Isso responde explicitamente à investigação sobre lacunas e direções futuras, embora governança e threat models não sejam eixos centrais. |
| **P05** | | **SCORE_RQ** | | **3,0 / 5,0** | | **Cobertura parcial em quatro RQs e plena em RQ5.** |

### Justificativas por subdimensão

**RQ1:** (a) autonomia: coberta por tipologia de cinco níveis de remediação (§4.3); (b) características: parcialmente cobertas por uso de ferramentas e conhecimento externo (§§1.1 e 5.5); (c) decisão: abordada em função da interação com operadores, sem modelagem formal do ciclo decisório ou planejamento. **P**.

**RQ2:** (a) tipos de arquitetura: abordagens classificadas em foundation models, fine-tuning, embeddings, prompting e métodos baseados em conhecimento (§5), sem desenho completo de arquitetura agêntica; (b) ferramentas: RAG, APIs, ferramentas analíticas e de execução (§5.5); (c) capacidades: suporte à combinação de dados e execução, mas guardrails e memória operacional não são especificados como componentes de uma arquitetura de produção. **P**.

**RQ3:** (a) benefícios qualitativos: auxílio à análise e reparo, adaptação a dados não estruturados (§§1.1 e 4.3); (b) métricas: accuracy, precision, recall, F1, AUC-ROC, BLEU, ROUGE, BERTScore, functional correctness, execution success rate e avaliação humana (§6.1); (c) nível da evidência: síntese secundária de trabalhos empíricos e benchmarks, não experimento original do survey. Não demonstra diretamente MTTD, MTTR ou carga cognitiva. **P**.

**RQ4:** (a) problemas técnicos: explicitamente presentes (§7); (b) ética/governança: não tratadas como eixo sistemático; (c) controles: menções a atuação humana e integração com sistemas tradicionais não constituem modelo de governança ou auditoria de decisões. **P**.

**RQ5:** lacunas claramente definidas e justificadas sobre tempo, custo, traces, adaptação e integração (§§7.1–7.4), somadas a benchmarks e avaliação (§6.2). Não se devem atribuir ao artigo pesquisas propostas sobre threat models ou mecanismos formais de governança. **T**, restrito às lacunas efetivamente apontadas.

## 3. Tabela C — Avaliação de qualidade DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P05 | Survey / revisão sistemática de literatura | P (0,5) | P (0,5) | N (0,0) | Y (1,0) | **2,0 / 4,0** | **Média** |

### Evidência e fundamentação de QA1–QA4

**QA1 — Objetivos claros: P (0,5).** Objetivos e quatro perguntas explícitos em §1.3, p. 4, com foco nas mudanças provocadas por LLMs em dados, tarefas, métodos e avaliação de AIOps. O problema de diagnóstico e remediação está explicitado na introdução, pp. 2–3. Contudo, a solução *agêntica* enquanto objeto específico da RSL atual não constitui o objetivo central do artigo. Parcial conforme a rubrica aplicada à pesquisa atual.

**QA2 — Metodologia replicável: P (0,5).** §2, pp. 5–6, documenta cinco bases (Scopus, Web of Science, IEEE Xplore, ACM Digital Library e arXiv), estratégia de busca na Fig. 3, critérios IC1–IC4 e EC1–EC5 e seleção na Fig. 4 (p. 7). Isso sustenta reprodução parcial da revisão. Entretanto, não há protocolo experimental de arquitetura agêntica reproduzível, e existe inconsistência quantitativa interna: o resumo (p. 1) reporta **183 artigos analisados**, ao passo que §2.3 (p. 6) reporta **163 novos estudos selecionados**. No mesmo parágrafo de §2.3, as contagens intermediárias de triagem não são integralmente reconciliadas. Não presumir uma explicação ausente.

**QA3 — Base de evidências sólidas: N (0,0).** O documento é um survey, não apresenta validação empírica original de um copiloto agêntico ou cenário experimental próprio com métricas de MTTD, MTTR ou carga cognitiva. §6, pp. 21–24, revisa métricas, avaliações e conjuntos de dados de **outros trabalhos**. As entrevistas com engenheiros on-call mencionadas em §4.3, p. 14, refinam a taxonomia de remediação, mas não equivalem à validação quantitativa do desempenho de um copiloto agêntico. A nota N aplica estritamente a rubrica experimental fornecida e **não nega o valor da síntese secundária**.

**QA4 — Conclusões coerentes: Y (1,0).** §7, pp. 24–26, apresenta limitações de custos, desempenho temporal, cobertura de dados, generalização e integração; §8, p. 26, retoma as quatro questões e sintetiza desafios compatíveis com a análise. O artigo delimita explicitamente problemas ainda não resolvidos, incluindo insuficiência de pesquisas sobre execução automática (§4.3, p. 15). **Y**, ressalvada a inconsistência de contagem apontada em QA2.

## 4. Parecer final do revisor

O P05 oferece fundamentação pertinente para a RSL por sistematizar fontes de observabilidade (métricas, logs e traces), análise de causa raiz e remediação assistida por LLMs em sistemas distribuídos. A taxonomia com cinco níveis de automação é especialmente útil para situar copilotos e agentes de remediação. Sua contribuição mais forte está no mapeamento de métodos, avaliações e lacunas de pesquisa, não na experimentação com um copiloto agêntico. A aderência é **3,0/5,0** e a qualidade segundo a rubrica fornecida é **2,0/4,0 (Média)**.

**Recomendação: INCLUIR COM RESSALVAS.** Manter P05 no corpus fundacional herdado, empregando-o prioritariamente como referência de contexto, taxonomias, métricas, ferramentas e agenda de pesquisa. Evitar utilizá-lo como prova empírica de redução de MTTD/MTTR ou carga cognitiva; para isso, são necessários estudos primários. Registrar divergência de contagem de estudos no protocolo e as limitações de cobertura de governança e avaliação agêntica.

### Pendências de verificação externa

1. **Citações recebidas:** [VERIFICAR] em Scopus, Web of Science ou outra base indexadora, com data da consulta.
2. **SJR:** [VERIFICAR] no *SCImago Journal Rank*; insumos indicam **Q1**, ainda não auditado pelo PDF.
3. **Qualis:** [VERIFICAR] na *Plataforma Sucupira / Qualis CAPES*, com período de avaliação informado; insumos indicam **A1**, ainda não auditado pelo PDF.
4. **Consistência editorial interna:** verificar se há esclarecimento dos totais **183 vs. 163**, sem substituir silenciosamente os números que constam do PDF.

### Nota de rastreabilidade

As classificações deste documento refletem a rubrica específica fornecida para a RSL em andamento. Como se trata de uma revisão, avaliar a ausência de experimento original em QA3 pode penalizar um estudo secundário apesar de seu valor como síntese científica; tal efeito deve ser mantido consistente para todos os surveys do corpus. As evidências mencionadas foram extraídas somente do PDF recebido. Não foi realizada consulta bibliométrica externa.
