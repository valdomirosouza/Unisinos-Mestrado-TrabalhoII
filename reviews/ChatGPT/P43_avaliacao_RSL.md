# P43 — Avaliação para a Revisão Sistemática da Literatura (Ciclo 2)

**Estudo:** Zota, R. D.; Bărbulescu, C.; Constantinescu, R. *A Practical Approach to Defining a Framework for Developing an Agentic AIOps System*. **Electronics**, 14, 1775 (2025). https://doi.org/10.3390/electronics14091775

**Escopo e método:** Avaliação exclusivamente do PDF fornecido, segundo o protocolo `prompt-P43.md`. As RQs abaixo são as da **RSL do pesquisador**, não as três perguntas de pesquisa formuladas pelos autores nas pp. 3 e 14–16. Pontuações resultam de interpretação crítica do texto, não de testes independentes.

## Etapa 0 — Tabela A: Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P43 | Electronics, 14, 1775 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Proposição de framework conceitual, fundamentada em revisão da literatura e discussões com especialistas; sem validação experimental | 10.3390/electronics14091775 |

**Fonte:** metadados, resumo e método nas pp. 1, 4–5; framework nas pp. 11–16; ausência de resultados experimentais expressa na p. 17. O protocolo informa *SJR Q2* e *Qualis A2* como dados preliminares fornecidos, **não confirmados pelo PDF**. Verificações necessárias: citações em base indexadora (mínimo 1); quartil em **SCImago Journal Rank** (Q1–Q2); estrato na **Plataforma Sucupira / Qualis CAPES** (A1–A2). Confirmar ainda a correspondência do período e da classificação da revista à regra CAPES informada, sem assumir que o percentil Scopus prova o Qualis.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / pendência |
|---|---|---|
| Ano ≥ 2020 | Atende | 2025 (p. 1). |
| Publicação identificável | Atende | *Electronics*, volume 14, artigo 1775 (p. 1). |
| Citações ≥ 1 | [VERIFICAR] | Contagem não consta do artigo; consultar base indexadora. |
| SJR Q1–Q2 | [VERIFICAR] | Informação preliminar no prompt: Q2; não verificável no PDF. |
| Qualis A1–A2 | [VERIFICAR] | Informação preliminar no prompt: A2; não verificável no PDF. |

**Resultado: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, quartil SJR e Qualis).** É admissível prosseguir na extração conforme o protocolo; a inclusão final fica condicionada à confirmação dos três critérios.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P43 | A Practical Approach to Defining a Framework for Developing an Agentic AIOps System | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | §3.1, pp. 8–9; §4, p. 11; §4.2, pp. 13–14; §4.3, pp. 15–16. | **a)** Dez níveis de autonomia explicitados, inclusive aprovação, notificação e atuação humana; **b)** agentes especializados, aprendizagem e diagnóstico/ação orientados a serviço; **c)** modelo *Understand–Decide–Take Action*, progressão da autonomia conforme risco e supervisão humana. A memória é tratada apenas indiretamente pela aprendizagem/reutilização de resoluções, sem implementação formal. |
| P43 | A Practical Approach to Defining a Framework for Developing an Agentic AIOps System | RQ2 — Engineering Architecture | Parcialmente Respondida | **P (0,5)** | §4.1, pp. 11–13, Figura 4; §4.2, pp. 13–14, Figura 5; §4.3, pp. 15–16. | **a)** Arquitetura conceitual em três dimensões: processos, serviços e capacidades; **b)** orquestrador, IA discriminativa, RAG e exemplos de Jenkins/Ansible; **c)** automação fechada e aprendizagem progressiva propostas. Não especifica detalhadamente memória operacional, guardrails técnicos, contratos de ferramentas ou implantação validada em produção. |
| P43 | A Practical Approach to Defining a Framework for Developing an Agentic AIOps System | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | Resumo, p. 1; §3.1, pp. 8–9; §4.3, pp. 15–16; §5, pp. 16–17. | **a)** Benefícios qualitativos **projetados**: menor intervenção humana, diagnóstico e remediação ágeis; **b)** não apresenta métricas observadas de MTTD, MTTR, qualidade de decisão ou carga cognitiva; **c)** evidência conceitual, sem experimento, simulação mensurada ou estudo de caso que demonstre tais ganhos. Crédito parcial restrito à discussão qualitativa de benefícios esperados, **não à comprovação**. |
| P43 | A Practical Approach to Defining a Framework for Developing an Agentic AIOps System | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | §3.1, p. 9; §4.3, p. 16; §5, p. 17. | **a)** reconhece risco de automação e efeitos entre camadas; exclui segurança do escopo; **b)** discute responsabilidade, transparência e impacto de decisões autônomas; **c)** sugere supervisão humana, caminhos de escalonamento, revisão pré-produção e monitoramento por KPIs. Os controles são diretrizes gerais, não mecanismos técnicos implementados ou avaliados. |
| P43 | A Practical Approach to Defining a Framework for Developing an Agentic AIOps System | RQ5 — Research Gaps | Parcialmente Respondida | **P (0,5)** | §5, pp. 16–17. | Indica necessidade de definir capacidades por processo, componentes por tecnologia, arquitetura conceitual detalhada e **testes empíricos futuros**; reconhece segurança fora do escopo. Não desenvolve plano de benchmarking, threat models, métricas de avaliação ou protocolo empírico. |
| **P43** | **Total** | **SCORE_RQ** | | **3,0 / 5,0** | | **Uma RQ plena e quatro parciais; nenhuma ausente.** |

### Justificativa das classificações limítrofes

- **RQ1 = T:** as subdimensões da rubrica (definição de autonomia, características centrais, modelo decisório) têm conteúdo explícito. Isso **não** equivale a dizer que memória computacional e planejamento executável estejam arquitetados em detalhe.
- **RQ3 = P:** o artigo formula expectativas qualitativas, mas os autores afirmam literalmente, na seção 5 (p. 17), que não possuem resultados experimentais. Portanto, não se deve reportar eficácia demonstrada ou estimar ganhos em MTTD/MTTR.
- **RQ5 = P:** há agenda futura explícita, porém sem detalhamento metodológico de avaliação/benchmarking ou modelagem de ameaças.

## Etapa 3 — Tabela C: Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P43 | Framework conceitual/propositivo, com revisão e consulta a especialistas | **Y (1,0)** | **P (0,5)** | **N (0,0)** | **P (0,5)** | **2,0 / 4,0** | **Média** |

**Racional critério a critério**

- **QA1 — Y (1,0), p. 1; §1, pp. 2–4:** problema, objetivo e solução agêntica são identificáveis: superar limitações da automação tradicional mediante diagnóstico, decisão e remediação orientados por agentes.
- **QA2 — P (0,5), §2, pp. 4–5; §4.1–4.2, pp. 11–14:** define dimensões, fluxos operacionais e um mapeamento ilustrativo com componentes (Figura 5). Contudo, não informa arquitetura implementada, configuração, dados, parâmetros, protocolo experimental ou instruções suficientes para replicar um sistema e sua avaliação. A revisão também não apresenta protocolo bibliográfico exaustivamente reprodutível. Pontuação parcial diz respeito **ao mapeamento conceitual**, não a replicabilidade experimental.
- **QA3 — N (0,0), §5, p. 17:** os autores registram expressamente inexistência de resultados experimentais que materializem a proposta. Exemplo de incidente na Figura 5 (p. 14) é **ilustrativo**, não um *toy experiment* executado com métricas; entrevistas/discussões não demonstram ganhos de desempenho da solução.
- **QA4 — P (0,5), §5, pp. 16–17:** conclusões são alinhadas à **proposta conceitual**, com limitações reconhecidas (ausência de experimentos e segurança fora do escopo). Entretanto, afirmações sobre redução de tempo e melhoria operacional no resumo e discussão não são sustentadas por mensuração própria.

## Parecer final do revisor

**Síntese.** O P43 contribui para a fundamentação de Agentic AIOps ao articular um framework de três dimensões, integrando processos ITIL/UPF-IT, elementos de serviços e capacidades *Understand–Decide–Take Action*. Seu exemplo de incident management explicita componentes para classificação, diagnóstico com RAG, orquestração e execução de automações. A maior aderência à RSL está nas definições de autonomia e na arquitetura conceitual para resposta a incidentes. Seu valor probatório sobre MTTD, MTTR e carga cognitiva é limitado, pois **não há validação experimental**.

**Recomendação: INCLUIR COM RESSALVAS**, após confirmação bibliométrica. Classificar como evidência **conceitual/arquitetural**, e não como comprovação empírica de eficácia. Na síntese da RSL, separar explicitamente benefícios esperados daqueles mensurados em outros estudos. Atribuições sobre agentes plenamente implementados ou operacionalizados em produção não são justificadas por este PDF.

**Pendências externas obrigatórias:**
1. **Citações ≥ 1:** consultar base indexadora e registrar data/contagem.
2. **SJR Q1–Q2:** conferir SCImago Journal Rank para *Electronics* e ano pertinente; valor Q2 informado no prompt segue **[VERIFICAR]**.
3. **Qualis A1–A2:** conferir Plataforma Sucupira / Qualis CAPES e período de avaliação pertinente; valor A2 informado no prompt segue **[VERIFICAR]**.

**Nota de fidelidade:** todo o conteúdo analítico acima foi extraído ou inferido criticamente do artigo fornecido; não foi realizada pesquisa externa. O estudo apresenta suas próprias três research questions (§1 e §4.3), distintas das cinco RQs avaliadas nesta RSL.
