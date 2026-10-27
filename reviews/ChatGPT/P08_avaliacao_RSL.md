# Avaliação do estudo P08 — Corpus Fundacional da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P08  
**Título:** *Applications, Challenges, and Future Directions of Human-in-the-Loop Learning*  
**Autores:** Sushant Kumar, Sumit Datta, Vishakha Singh, Deepanwita Datta, Sanjay Kumar Singh e Ritesh Sharma.  
**Fonte:** IEEE Access, vol. 12 (2024), início na p. 75735.  
**DOI:** https://doi.org/10.1109/ACCESS.2024.3401547  
**Natureza:** survey/revisão narrativa da literatura.  
**Política de evidência:** a classificação científica abaixo baseia-se exclusivamente no artigo PDF enviado. Informações SJR, Qualis e citações exigem verificação externa, mesmo quando registradas no enunciado.

## Etapa 0 — Tabela A: extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P08 | IEEE Access | 2024 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Survey (revisão narrativa) | 10.1109/ACCESS.2024.3401547 |

**Origem PDF:** primeira página, cabeçalho (DOI, datas), identificação da revista e indicação “SURVEY”. O prompt registra SJR Q1 e Qualis A1 como previamente verificados em fonte externa, mas esses atributos **não são certificáveis a partir do PDF**, conforme a regra antifabricação.

## Etapa 1 — triagem PRISMA / elegibilidade

| Critério | Situação | Evidência ou pendência |
|---|---|---|
| Ano ≥ 2020 | Cumpre | 2024, primeira página |
| Veículo identificado | Cumpre | IEEE Access, primeira página |
| Citações ≥ 1 | [VERIFICAR] | O PDF não informa citações recebidas; referências bibliográficas não equivalem a citações do artigo |
| SJR Q1–Q2 | [VERIFICAR] | Confirmar o quartil aplicável no Scimago Journal Rank |
| Qualis A1–A2 | [VERIFICAR] | Confirmar classificação e período na Plataforma Sucupira / Qualis CAPES |

**Resultado formal: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis).** O artigo é parte do corpus fundacional herdado (P01–P19); a presente avaliação não modifica retrospectivamente a decisão original de inclusão.

## Etapa 2 — Tabela B: aderência às RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P08 | Applications, Challenges, and Future Directions of Human-in-the-Loop Learning | RQ1 | Parcialmente Respondida | P (0,5) | Introdução e Fig. 1, p. 75736; Seção II-B e Fig. 3, pp. 75738–75739; Seção III-A, p. 75741 | Apresenta cooperação humano-máquina, treinamento por reforço com ações e feedback humanos e alocação dinâmica de autoridade em direção autônoma. Não define as capacidades completas de Agentic AI (memória, planejamento e ferramentas) nem seus níveis de autonomia como sistema agêntico. |
| P08 | Applications, Challenges, and Future Directions of Human-in-the-Loop Learning | RQ2 | Parcialmente Respondida | P (0,5) | Seção II-A–C e Figs. 1–4, pp. 75736–75739 | Expõe frameworks HITL de processamento, active learning, reinforcement learning e XAI com interação humana. Não especifica arquitetura de orquestração agêntica em produção, memória, tool-use, telemetria/observabilidade nem mecanismos operacionais de guardrails. |
| P08 | Applications, Challenges, and Future Directions of Human-in-the-Loop Learning | RQ3 | Parcialmente Respondida | P (0,5) | Seção III-A, p. 75740; Seção III-C, pp. 75743–75744 | Compila benefícios qualitativos e resultados numéricos de estudos de terceiros. Um estudo citado em direção autônoma relata aproximadamente +7% em desempenho, −35% em carga física e −50% em carga mental. Evidências são secundárias e fora de incident response; não avalia MTTD, MTTR, tempo de triagem ou carga cognitiva de SREs. |
| P08 | Applications, Challenges, and Future Directions of Human-in-the-Loop Learning | RQ4 | Parcialmente Respondida | P (0,5) | Seção IV-A–I, pp. 75747–75751, especialmente IV-H (Validation) e IV-I (Ethical and Legal Issues); Fig. 6, p. 75748 | Aborda vieses humanos, inconsistências, custos, escalabilidade, qualidade de dados, validação, privacidade e explicabilidade. Propõe estratégias como múltiplos anotadores, acordos interanotadores e privacidade diferencial, mas sem governança operacional de agentes autônomos críticos, accountability end-to-end ou threat model específico. |
| P08 | Applications, Challenges, and Future Directions of Human-in-the-Loop Learning | RQ5 | Parcialmente Respondida | P (0,5) | Seção V, pp. 75751–75754; Seção VI, p. 75754 | Explicita oportunidades em qualidade e complexidade do feedback, confiança, interfaces humano-IA, escalabilidade, avaliação e estruturas computacionais formais de HITL. Não estabelece agenda específica de benchmarking de copilotos agênticos em operações de TI, observabilidade ou resposta a incidentes. |
| **P08** | | **SCORE_RQ** | | **2,5 / 5,0** | | **Cinco RQs parcialmente atendidas, sobretudo como fundamentação transversal de HITL.** |

### Justificativa por subdimensão

**RQ1 — Context Definitions (P, 0,5).** (a) O artigo discute autonomia compartilhada e realocação de autoridade humano/máquina, mas não propõe uma taxonomia de níveis de autonomia de Agentic AI (Seção III-A, p. 75741). (b) Feedback, interação e supervisão estão descritos; planejamento, memória e integração de ferramentas agênticas não estão demonstrados como conjunto de características (Seção II, pp. 75737–75739). (c) O ciclo ambiente/ação/recompensa/intervenção humana é visualizado na Figura 3 (p. 75739). Cobertura parcial pela diferença entre HITL e arquitetura agêntica.

**RQ2 — Engineering Architecture (P, 0,5).** (a) A Figura 1 representa um pipeline HITL e as Figuras 2–4 representam active learning, reinforcement learning e XAI. (b) A Seção II descreve famílias de métodos, não uma stack de implementação de agentes em produção. (c) A explicabilidade e o feedback humano são capacidades relevantes, mas não há especificação de memória persistente, ferramentas externas, orquestração, controle de execução ou observabilidade operacional.

**RQ3 — Evidence Benefits (P, 0,5).** (a) As seções introdutórias e de aplicações descrevem precisão, eficiência, maior confiança e colaboração humano-IA. (b) A p. 75740 apresenta valores aproximados de +7% em desempenho, −35% em carga física e −50% em carga mental de motoristas no estudo externo [55]; a p. 75743 reporta estudos humanos de auxílio à decisão. (c) O nível de evidência para o próprio P08 é síntese secundária; os experimentos pertencem às publicações citadas e não ao survey. Nenhuma medida de IR/SRE é aferida pelo artigo.

**RQ4 — Challenges & Ethics (P, 0,5).** (a) A Seção IV trata de custo, dados, fatores humanos, complexidade, aprendizagem online, interação e validação. (b) A Seção IV-I discute viés e privacidade. (c) Há medidas de mitigação em termos de consistência da anotação, divisão de tarefas, verificação e privacidade diferencial. O foco, porém, é HITL para ML, não governança e limites de atuação de agentes autônomos em sistemas críticos.

**RQ5 — Research Gaps (P, 0,5).** A Seção V lista numerosos trabalhos futuros específicos de HITL, incluindo feedback, estudos com pessoas, confiança, explicações, segurança e modelos formais de colaboração. Não desenvolve lacunas de MTTD/MTTR, confiabilidade operacional de copilotos agênticos, traces/metrics/logs ou políticas de execução no ciclo de incidentes.

## Etapa 3 — Tabela C: qualidade DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P08 | Survey (revisão narrativa) | P (0,5) | N (0,0) | N (0,0) | Y (1,0) | **1,5 / 4,0** | **Média** |

**QA1 — P (0,5):** O resumo, as perguntas do artigo na Introdução e a seção *Contribution* (pp. 75735–75737) apresentam explicitamente objetivo, problemas e abordagens HITL. Entretanto, não definem uma solução agêntica voltada a resposta a incidentes, como pede a rubrica específica da RSL. A clareza do survey é reconhecida; a adequação ao problema agêntico é parcial.

**QA2 — N (0,0):** A Seção II (pp. 75737–75739) descreve categorias de métodos e diagramas ilustrativos, mas o PDF não fornece protocolo sistemático e reproduzível de busca, seleção e avaliação de estudos nem configuração, parâmetros e cenário experimental de uma arquitetura própria que permitam replicar sua aplicação. Estruturas esquemáticas de trabalhos alheios não satisfazem a exigência.

**QA3 — N (0,0):** O artigo compila estudos de caso, experimentos e números extraídos de outras fontes (ex.: Seção III-A, p. 75740). Não apresenta experimento, simulação ou estudo de caso original com métricas próprias; pela rubrica fornecida, uma revisão descritiva sem validação empírica própria recebe N. Isso não nega o valor das pesquisas primárias citadas.

**QA4 — Y (1,0):** A Seção VI (p. 75754) retoma os benefícios, desafios e limites de HITL discutidos ao longo das seções II–V, incluindo problemas de interação, ambiguidade, viés, ética e necessidade de colaboração multidisciplinar. As conclusões mantêm-se no plano de revisão, sem alegar validação de um copiloto próprio.

**Interpretação da banda:** Média (1,5–2,5), conforme os limiares definidos no protocolo. Não se deve confundir avaliação da utilidade científica do survey com avaliação de sua evidência empírica primária.

## Parecer final do revisor

O artigo P08 sistematiza conceitualmente abordagens de supervisão humana, feedback, reinforcement learning e explicabilidade em aplicações de inteligência artificial. Sua contribuição mais direta à RSL é fundamentar decisões compartilhadas, governança e fatores humanos em ambientes complexos. A síntese de resultados experimentais de outros estudos inclui medições de desempenho e carga de trabalho, porém não constitui evidência primária sobre resposta a incidentes. O texto não avalia arquitetura de Agentic AI Copilot, MTTD, MTTR ou utilização em equipes SRE. Assim, é um estudo fundacional útil, com aderência indireta às RQs e restrições metodológicas para inferência sobre incident response.

**Recomendação: INCLUIR COM RESSALVAS.** Preservar o estudo no corpus fundacional já incluído, usando-o para fundamentar HITL, human oversight, feedback e segurança da colaboração humano-IA. Não utilizá-lo como prova de ganhos operacionais em resposta a incidentes ou validação de arquitetura agêntica em produção.

### Pendências de verificação externa

1. **Citações recebidas:** verificar contagem em uma base indexadora e data da coleta.
2. **SJR:** verificar no **Scimago Journal Rank**, com ano do indicador e categoria de área. O prompt registra **Q1** como dado pré-verificado, ainda não atestado no PDF.
3. **Qualis CAPES:** verificar na **Plataforma Sucupira / Qualis CAPES**, indicando área e quadriênio. O prompt registra **A1** de conferência prévia em `papers.csv`, mas o CSV não faz parte dos documentos comprobatórios disponíveis nesta avaliação.

**Nota de consistência:** As páginas citadas são as páginas impressas do periódico (início em 75735), e não a numeração sequencial do arquivo PDF. A classificação do P08 avalia o conteúdo do próprio survey; resultados de experimentos citados são evidência secundária.
