# Avaliação do Artigo P16 — Corpus Fundacional

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P16  
**Artigo:** *A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey*  
**Autores:** Josu Diaz-de-Arcaya, Ana I. Torre-Bastida, Gorka Zárate, Raúl Miñón e Aitor Almeida  
**Fonte de evidência:** PDF anexado, 30 páginas.  
**Abordagem:** avaliação retroativa do corpus fundacional; a decisão de inclusão herdada do Trabalho I não é reaberta.

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P16 | *ACM Computing Surveys*, 56(4), artigo 84 | 2023 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão sistemática da literatura (*systematic survey*) | [10.1145/3625289](https://doi.org/10.1145/3625289) |

**Evidência:** primeira página, referência bibliográfica ACM e resumo (p. 1). O prompt informa **SJR Q1** e **Qualis A1** como dados já verificados anteriormente, mas o PDF não permite confirmá-los de modo independente; portanto, nas células exigidas pela rubrica, constam **[VERIFICAR]**. Não se deve confundir o quartil JIF usado como critério no próprio survey com quartil SJR do periódico que o publicou.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / justificativa |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicação indicada como outubro de 2023, p. 1. |
| Veículo identificável | Atendido | *ACM Computing Surveys*, vol. 56, n. 4, artigo 84, p. 1. |
| Citações ≥ 1 | [VERIFICAR] | Total de citações **recebidas pelo P16** não é comprovável pelo PDF. Os números de citações utilizados pelo artigo para selecionar **outros trabalhos** não respondem a este critério. |
| SJR Q1–Q2 | [VERIFICAR] | Validar em Scimago Journal Rank (SJR), com referência ao ano adequado. O prompt de origem registra Q1, sem comprovação interna ao PDF. |
| Qualis A1–A2 | [VERIFICAR] | Validar na Plataforma Sucupira / Qualis CAPES, considerando área e período avaliativo. O prompt de origem registra A1, sem comprovação interna ao PDF. |

**Resultado formal da triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações recebidas, quartil SJR e Qualis). A análise prossegue conforme regra do protocolo para elegibilidade pendente, **sem rediscutir a inclusão herdada do Trabalho I**.

## Etapa 2 — Extração e classificação das RQs

**Nota metodológica:** RQ1–RQ5 nesta tabela são as perguntas da RSL de destino, não as perguntas homônimas utilizadas pelos autores do P16 na Tabela 2 (p. 4). Evidências de AIOps/MLOps são classificadas como **indiretas** quando não sustentam especificamente Agentic AI.

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P16 | Diaz-de-Arcaya et al. (2023) | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | Tabela 1, §1.1, p. 3; §4.3.1, p. 15 | **(a) Parcial:** AIOps busca reduzir intervenção humana e há menção a detecção/ação autônoma em sistema citado. **(b) Parcial:** monitoramento, automação e auto-recuperação são características operacionais, não uma taxonomia de agentes. **(c) Ausente no recorte agêntico:** não há modelo integrado de planejamento, memória, ferramentas, supervisão humana e decisão de um copiloto Agentic AI. |
| P16 | Diaz-de-Arcaya et al. (2023) | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | Tabela 1, p. 3; §4.1.3, pp. 12–13; §4.4, pp. 16–18, Tabela 6, p. 17 | **(a) Coberta para AIOps/MLOps:** taxonomia de arquiteturas e infraestrutura cloud/edge. **(b) Coberta em sentido genérico:** contêineres, serverless, APIs, orquestração e pipelines. **(c) Parcial:** observabilidade, monitoramento e adaptação são abordados, mas não mecanismos explícitos de memória, guardrails e orquestração multiagente em produção. |
| P16 | Diaz-de-Arcaya et al. (2023) | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | Tabela 1, p. 3; §4.3.1–4.3.3, pp. 15–16; §4.5.2, p. 19 | **(a) Coberta indiretamente:** eficiência de TI, redução de intervenção e suporte à análise de logs/incidentes. **(b) Parcial:** desempenho, atrasos de rede, consumo energético e custo são dimensões mencionadas em estudos revisados, sem síntese quantitativa de MTTD/MTTR ou carga cognitiva para o P16. **(c) Evidência secundária:** a revisão cita estudos, mas não oferece experimento próprio de copiloto para resposta a incidentes. |
| P16 | Diaz-de-Arcaya et al. (2023) | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | §4.1.1–4.1.5, pp. 11–13; Figura 6, p. 13 | **(a) Coberta:** confiabilidade, segurança, privacidade, escalabilidade, heterogeneidade, drift e qualidade dos dados. **(b) Parcial:** vieses, transparência, explicabilidade e governança de dados/modelos são apontados. **(c) Insuficiente para agentes:** não apresenta mecanismos concretos de accountability, aprovação humana, contenção de ações ou governança de copilotos agênticos. |
| P16 | Diaz-de-Arcaya et al. (2023) | RQ5 — Research Gaps | Parcialmente Respondida | P (0,5) | §4.1.5, p. 13; §4.3, pp. 15–16; §4.4, pp. 16–18; §6, p. 22 | Lacunas claras de monitoramento, treinamento/retraining, implantação, orquestração, dados e maturação de AIOps, além de necessidade de pesquisas futuras sobre LLMs. Contudo, benchmarks de copilotos agênticos, modelos de ameaça e governança de autonomia não são desenvolvidos como agenda de pesquisa própria. |
| **P16** | **Total** | **SCORE_RQ** | **2,5 / 5,0** | **P+P+P+P+P** | **5 RQs × 0,5** | **Aderência indireta e fundacional; nenhuma RQ é integralmente respondida no recorte específico de Agentic AI para incidentes.** |

### Fundamentação complementar das classificações

**RQ1.** O artigo contrapõe MLOps a AIOps na Tabela 1 (p. 3), associando a segunda disciplina à operação inteligente de TI, ao tratamento da complexidade e à redução de intervenção humana. Em §4.3.1 (p. 15), descreve, por referência a um estudo incluído, detecção autônoma de estado, alocação de recursos, alertas e detecção de anomalias. Esse material é relevante para autonomia operacional, mas não equivale à definição formal de agente com planejamento, memória e supervisão humana.

**RQ2.** A Tabela 6 (p. 17) organiza frameworks e arquiteturas por foco. A seção 4.4 (pp. 16–18) apresenta categorias de gestão de dados, infraestrutura, ciclo de vida e tecnologias, incluindo orquestração de pipelines, conteinerização, serverless e monitoramento. A cobertura é suficientemente concreta para uma classificação parcial, mas não descreve arquitetura específica de copiloto Agentic AI com controles de ações e memória contextual.

**RQ3.** §4.3 (pp. 15–16) discute inferência de KPIs, monitoramento, anomalias e análise de causa raiz, além de eficiência e desempenho. §4.5.2 (p. 19) relaciona AIOps a análise de logs e remediação de incidentes. São resultados **atribuídos à literatura revisada**, não medições empíricas realizadas pelos autores do P16. Não há demonstração de redução quantificada de MTTD ou MTTR de um copiloto agêntico nem avaliação direta de carga cognitiva de operadores.

**RQ4.** As seções 4.1.1–4.1.5 (pp. 11–13) sistematizam dificuldades de engenharia, gestão de dados, orquestração, hardware e monitoramento. O texto aborda também *trustworthiness*, privacidade, segurança, vieses e explicabilidade. Falta, entretanto, converter esses desafios em políticas e mecanismos específicos de governança para agentes autônomos operando mudanças em sistemas críticos.

**RQ5.** A discussão e a conclusão (§6, p. 22) apontam a necessidade de novas pesquisas sobre distinções entre AIOps e MLOps, sobre monitoramento/redeployment e sobre a crescente presença de LLMs. Essas lacunas são pertinentes ao contexto tecnológico da RSL, mas não fornecem diretamente um protocolo de avaliação de copilotos agênticos em resposta a incidentes.

## Etapa 3 — Avaliação de qualidade DARE adaptada

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P16 | Revisão sistemática da literatura (*systematic survey*) | P (0,5) | P (0,5) | N (0,0) | Y (1,0) | **2,0 / 4,0** | **Média** |

**QA1 — Objetivos Claros: P (0,5).** O objetivo do estudo é explicitado em §1.2 e suas cinco perguntas estão na Tabela 2 (pp. 3–4). Entretanto, a rubrica **adaptada para esta RSL** exige explicitação do problema operacional e de uma **solução agêntica**. O P16 não propõe essa solução; por isso, recebe crédito parcial apesar da clareza de seus objetivos originais.

**QA2 — Metodologia Replicável: P (0,5).** §2 (pp. 4–6), a Figura 1 e a Figura 2 (p. 5), as Tabelas 3–4 (pp. 6–7) e a Figura 3 (p. 8) informam fonte bibliográfica Scopus, estratégia automatizada, termos, período, critérios de seleção e métricas de qualidade. O §2.1 (p. 4) ainda aponta um cliente disponível em repositório de código citado. Ainda assim, a rubrica solicitada privilegia **arquitetura, tecnologias, parâmetros e cenário experimental replicável** de uma solução, ausentes porque o P16 é uma revisão, não um experimento com copiloto. Ressalva: o artigo contém discrepâncias internas entre totais narrativos e tabulados do fluxo de seleção (ver §3.1 e Figura 3/Tabela 5, pp. 7–8), que devem ser verificadas antes de reutilizar os números intermediários.

**QA3 — Base de Evidências Sólidas: N (0,0).** A revisão examina 93 estudos e fornece síntese secundária (§3.1, pp. 7–8; §4, pp. 10–20). **Não apresenta validação empírica própria** de arquitetura ou sistema agêntico por experimento, estudo industrial ou simulação com métricas, exigida expressamente pela rubrica de QA3. A nota N avalia a adequação ao critério experimental adaptado, **não significa que revisões sistemáticas careçam de valor científico**.

**QA4 — Conclusões Coerentes: Y (1,0).** As conclusões (§6, p. 22) retomam as questões sobre adoção, ciclo de vida de ML, dados, infraestrutura e oportunidades em redes 5G/6G. Há discussão de ameaças de viés no §3.2 (p. 9), limitações de cobertura e necessidade de trabalhos futuros. As afirmações principais acompanham a síntese realizada. A ressalva sobre consistência de contagens no fluxo de seleção não invalida, por si só, a coerência geral da discussão.

**Cálculo:** QA1 0,5 + QA2 0,5 + QA3 0,0 + QA4 1,0 = **2,0**. Banda **Média** (intervalo 1,5–2,5).

## Parecer final do revisor

O P16 apresenta uma revisão sistemática de MLOps e AIOps e contribui com taxonomias de arquitetura, desafios de operacionalização, observabilidade e oportunidades de automação de TI. Sua discussão de análise de logs, detecção de anomalias e remediação oferece contexto útil para resposta a incidentes. Entretanto, não caracteriza integralmente Agentic AI nem valida um copiloto com autonomia supervisionada, métricas de MTTD/MTTR ou redução de carga cognitiva. Recomenda-se utilizá-lo como **referência fundacional** sobre AIOps e operacionalização de IA, sem atribuir-lhe evidências experimentais de copilotos agênticos.

**Recomendação:** **INCLUIR COM RESSALVAS.** A inclusão original no corpus é preservada. O artigo é pertinente como base contextual de AIOps/MLOps, mas sua aderência é indireta (**SCORE_RQ = 2,5/5,0**) e a qualidade sob a rubrica adaptada é **Média** (**SCORE_QA = 2,0/4,0**). Esta recomendação diz respeito à utilidade na síntese, e não elimina a pendência formal de elegibilidade externa.

### Pendências de verificação externa

1. **Citações recebidas pelo artigo P16:** consultar Scopus, Web of Science ou outra base indexadora e registrar data de consulta.
2. **SJR:** confirmar quartil do periódico *ACM Computing Surveys* no **Scimago Journal Rank**, com ano de referência documentado.
3. **Qualis CAPES:** confirmar classificação do periódico na **Plataforma Sucupira / Qualis CAPES**, explicitando área e período de avaliação.
4. **Conferência interna do PDF:** se os dados do fluxo PRISMA forem citados na RSL, preferir conferência direta da Figura 3 e Tabela 5, p. 8, pois o texto corrente de §3.1 relata alguns totais diferentes dos apresentados nesses elementos.

### Nota de rastreabilidade

Todas as evidências científicas acima foram extraídas do PDF fornecido. Os qualificadores bibliométricos comunicados no prompt (**A1/Q1**) foram tratados como **informações históricas declaradas**, não como dados confirmados pelo artigo. A avaliação não realizou consulta bibliométrica externa, respeitando a regra de fonte exclusiva do protocolo.
