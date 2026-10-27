# Avaliação da RSL — P18

**Artigo:** Eramo, R.; Said, B.; Oriol, M.; Bruneliere, H.; Morales, S. *An architecture for model-based and intelligent automation in DevOps*.

**Natureza da avaliação:** estudo fundacional herdado do Trabalho I. A recomendação abaixo avalia a contribuição e a qualidade para a síntese atual, **sem reabrir a decisão anterior de inclusão**.

**Base documental:** exclusivamente o PDF anexado, 21 páginas. Os metadados externos fornecidos no roteiro (Qualis A2 e SJR Q1) não são considerados documentalmente verificados no PDF.

## Etapa 0 — Tabela A: dados bibliométricos (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P18 | *The Journal of Systems & Software*, v. 217, artigo 112180 | 2024 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Proposição e avaliação empírica de arquitetura de software, com estudos de caso industriais | [10.1016/j.jss.2024.112180](https://doi.org/10.1016/j.jss.2024.112180) |

**Evidência:** cabeçalho, resumo e DOI (p. 1); natureza do estudo e avaliação com casos industriais (Seções 6–7, pp. 10–18).

**Verificações externas previstas:** citações em base indexadora (por exemplo, Scopus ou Web of Science); quartil em *SCImago Journal Rank*; estrato no sistema *Plataforma Sucupira / Qualis CAPES*, considerando o período de avaliação e o periódico correto. O roteiro informa **Q1 e A2**, mas tais valores permanecem **[VERIFICAR]** nesta avaliação restrita ao PDF; não representam confirmações independentes.

## Etapa 1 — Elegibilidade

| Critério | Resultado | Fundamentação |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicação em 2024, p. 1. |
| Publicação com veículo identificável | Atendido | *The Journal of Systems & Software*, v. 217, p. 1. |
| Citações ≥ 1 | [VERIFICAR] | Número de citações recebidas não está demonstrado no PDF. |
| SJR Q1–Q2 | [VERIFICAR] | Quartil não é comprovado no PDF. |
| Qualis A1–A2 | [VERIFICAR] | Estrato não é comprovado no PDF. |

**Resultado formal:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações, SJR e Qualis). A avaliação integral prossegue conforme o protocolo, que admite estudos pendentes. O artigo permanece no **corpus fundacional**, por decisão herdada e não reavaliada nesta etapa.

## Etapa 2 — Tabela B: classificação das questões de pesquisa (Tabela 5)

Critério: **T = 1,0** (todas as subdimensões explicitamente contempladas); **P = 0,5** (cobertura parcial ou genérica); **N = 0,0** (ausência ou mera tangência). A análise diferencia automação inteligente com AI/ML de **Agentic AI**: uma arquitetura com componentes de análise e automação não comprova, por si só, autonomia deliberativa, planejamento, memória ou atuação de agentes.

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P18 | *An architecture for model-based and intelligent automation in DevOps* | RQ1 — Context Definitions | Parcialmente Respondida | **P (0,5)** | Seção 2.2, p. 3 (T3: operação autônoma, decisão); Seção 3.3, p. 6 (análise, predição e automação). | **a) Autonomia:** mencionada genericamente; **b) características:** análise e automação, sem descrição de planejamento/memória de agentes; **c) decisão:** pipeline de insights e ação, sem modelo formal de decisões de um agente. Não define níveis de autonomia agêntica ou supervisão humana operacional. |
| P18 | Idem | RQ2 — Engineering Architecture | Parcialmente Respondida | **P (0,5)** | Seções 3.1–3.4, pp. 4–7; Figuras 2–5, p. 5; Seções 4–5, pp. 7–9. | **a) Arquitetura:** camadas Data Engineering, Core e AI-Augmented; **b) ferramentas:** interfaces, metamodelos, Modelio, exemplos de implementações; **c) capacidades avançadas:** ingestão, análise, anomalias, remediação, accountability e explainability. Apesar da cobertura arquitetural expressiva, não apresenta uma arquitetura operacional de agentes com memória, guardrails e orquestração agêntica caracterizados. |
| P18 | Idem | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | Seção 6, pp. 10–17; Tabelas 2–4, p. 17; Seção 6.3.1, p. 16; Figura 22, p. 18. | **a) Benefícios qualitativos:** integração, colaboração e aplicabilidade industrial; **b) quantitativos:** contagens de soluções e requisitos mapeados e 91% de correspondência das colaborações existentes com vínculos indiretos identificados; **c) nível de evidência:** estudos de caso reais, porém orientados à arquitetura. Não há demonstração de redução de MTTD, MTTR, carga cognitiva ou qualidade decisória de resposta a incidentes. |
| P18 | Idem | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | Seção 2.2, p. 3; Seção 3.2, p. 6 (accountability e explainability); Seção 7, pp. 17–18 (ameaças à validade). | **a) Desafios técnicos:** heterogeneidade, flexibilidade, integração e gestão de dados; **b) ética/governança:** serviços genéricos de prestação de contas e explicabilidade; **c) mecanismos:** componentes arquiteturais previstos, mas sem políticas, autorização, auditoria detalhada, guardrails ou modelo de responsabilização para agentes autônomos em sistemas críticos. Ameaças à validade são limitações metodológicas, não substitutos para análise de risco agêntico. |
| P18 | Idem | RQ5 — Research Gaps | Parcialmente Respondida | **P (0,5)** | Introdução e Seção 2.2, pp. 2–3; Seção 9, pp. 19–20; Seção 10, p. 19–20, conforme paginação do PDF. | Identifica lacuna na integração MDE + AI/ML + DevOps e explicita como trabalho futuro uma avaliação da qualidade arquitetural, com atributos/métricas e possíveis avaliações por entrevistas ou surveys. Não desenvolve agenda específica de benchmarks agênticos, threat models, alinhamento, governança ou métricas de incident response. |
| **P18** | **TOTAL** | **SCORE_RQ** | **2,5 / 5,0** | **5 × P** | **Seções 2–10** | **Aderência indireta e de base arquitetural, não uma demonstração de Agentic AI Copilot em resposta a incidentes.** |

### Notas analíticas por RQ

**RQ1:** A expressão “operate autonomously” integra um elenco de possibilidades da inteligência artificial (Seção 2.2, p. 3), não uma taxonomia de autonomia agêntica. O artigo não fornece implementação identificável de ciclo perceber–planejar–agir–refletir de um agente.

**RQ2:** A **Figura 2 (p. 5)** é a evidência central: o *Data Engineering Tool Set* fornece coleta, gestão e representação; o *Core Tool Set* inclui dados/modelos, infraestrutura e serviços de accountability/explainability; o *AI-Augmented Tool Set* inclui *AIOps Engineering* (ingestão, análise, automação) e *AI DevOps Engineering*. A Seção 3.3 (p. 6) aborda explicitamente análise de causa raiz, detecção de anomalias, remediação automatizada e tratamento de incidentes como **capacidades previstas**. Isso é relevante para um copiloto de IR, mas não equivale a validação empírica de um agente de IR.

**RQ3:** O indicador de **91%** (Seção 6.3.1, p. 16, Figura 22, p. 18) refere-se à identificação de **colaborações existentes** mediante relações indiretas potenciais no projeto, e **não** à precisão de detecção de incidentes ou ao desempenho de um sistema agêntico. Os autores informam **10 estudos de caso** (Seções 2 e 6), e, na avaliação da flexibilidade, **54 soluções tecnológicas de 22 parceiros** (Seção 6.3.1, p. 16). A Seção 5.1 (p. 8) menciona **136 soluções** em um inventário mais amplo de implementações; os dois números aparecem em contextos distintos e não devem ser tratados como uma mesma população medida.

**RQ4:** Embora accountability e explainability estejam representados como serviços genéricos (p. 6, Figura 2, p. 5), o texto não permite inferir controles concretos para autorização de ações, revisão humana de remediações ou limites de autonomia. A Seção 7 aborda riscos de validade do estudo, incluindo vínculos com parceiros do projeto e limites de generalização.

**RQ5:** A **Seção 10** reconhece expressamente a falta de uma análise de qualidade da arquitetura e propõe trabalho futuro relacionado a atributos, métricas, avaliações por questionários ou entrevistas e referências ao ATAM. Essa lacuna é substantiva, porém não é um roteiro de pesquisa voltado à segurança de agentes ou desempenho de resposta a incidentes.

## Etapa 3 — Tabela C: avaliação da qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P18 | Arquitetura proposta e avaliação empírica com estudos de caso industriais | **P (0,5)** | **P (0,5)** | **Y (1,0)** | **Y (1,0)** | **3,0 / 4,0** | **Alta** |

**Justificativa individual:**

- **QA1 — P (0,5):** problema e objetivos da integração AI/ML + MDE + DevOps são explícitos (Introdução, pp. 1–2; Seção 2.2, p. 3). Contudo, a solução é **AI-augmented**, não uma solução **agêntica** explicitamente definida conforme a rubrica específica desta RSL. Avalia-se o enquadramento no problema agêntico, não a clareza do objetivo arquitetural em seu domínio próprio.
- **QA2 — P (0,5):** componentes, relações, integrações e estudos de caso são descritos nas Seções 3–6 (pp. 3–17). A replicação integral independente fica limitada pela heterogeneidade de ferramentas e cenários, pela dependência de artefatos do projeto e por detalhes de estudos de caso indicados como confidenciais na Seção 5.1 (p. 8). Não há protocolo experimental completamente reproduzível para avaliar um copiloto agêntico de IR.
- **QA3 — Y (1,0):** evidência empírica de integração e aplicabilidade arquitetural em estudos de caso industriais, com mapeamentos quantitativos de requisitos e soluções (Seção 6, pp. 10–17; Tabelas 2–4 e Figuras 19–22). **Este Y atesta evidência para a finalidade do estudo**, não demonstra efeito causal sobre MTTD/MTTR.
- **QA4 — Y (1,0):** as conclusões são alinhadas às evidências de viabilidade/aplicabilidade e a Seção 7 (pp. 17–18) discute validade de construto, interna, externa e de conclusão. A Seção 10 explicita a ausência de avaliação formal de qualidade arquitetural. Os autores inclusive evitam conclusões estatísticas fortes (Seção 7.4, p. 18).

**Interpretação da banda:** *Alta* na escala DARE operacionalizada pelo roteiro, **não** indicação de alta aderência temática a Agentic AI. A qualidade metodológica da avaliação arquitetural e a relevância às RQs são dimensões diferentes.

## Parecer final do revisor

O estudo apresenta uma arquitetura em camadas que integra engenharia dirigida por modelos, AI/ML e DevOps, com capacidades relevantes de observabilidade, análise de anomalias e automação de remediação. Sua contribuição mais forte para a RSL está na **RQ2**, como referência para decomposição arquitetural e integração de ferramentas em AIOps, embora a pontuação permaneça **P** por não explicitar mecanismos próprios de agentes. A validação industrial sustenta a aplicabilidade da arquitetura, mas **não comprova ganhos de MTTD, MTTR ou carga cognitiva** na resposta a incidentes. As dimensões de autonomia deliberativa, governança de agentes e avaliação específica de copilotos permanecem insuficientemente cobertas.

**Recomendação: INCLUIR COM RESSALVAS.** Preservar P18 no corpus fundacional já incluído e utilizá-lo como **referência arquitetural contextual** para ingestão, representação de dados, análise e automação em DevOps/AIOps. Não codificá-lo como evidência direta de um *Agentic AI Copilot* em IR, nem como comprovação de eficácia operacional na mitigação de incidentes.

**Pendências externas:** confirmar (1) ≥1 citação em base indexadora, (2) quartil SJR Q1/Q2 no período apropriado, (3) estrato Qualis A1/A2 e período CAPES aplicável. O roteiro registra Q1/A2 provenientes de planilha externa, mas o PDF não permite validar essas atribuições.

## Registro consolidado para as tabelas da RSL

- **Tabela 3:** P18 | *The Journal of Systems & Software* | 2024 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | arquitetura com estudo de caso industrial | 10.1016/j.jss.2024.112180.
- **Tabela 5:** P18 | RQ1=P | RQ2=P | RQ3=P | RQ4=P | RQ5=P | **SCORE_RQ=2,5/5,0**.
- **Tabela 7:** P18 | QA1=P | QA2=P | QA3=Y | QA4=Y | **SCORE_QA=3,0/4,0** | **Alta**.

*Ressalva de rigor:* os escores expressam a aplicação crítica da rubrica do roteiro fornecido ao conteúdo verificável do artigo; não são notas emitidas pelos próprios autores do estudo.
