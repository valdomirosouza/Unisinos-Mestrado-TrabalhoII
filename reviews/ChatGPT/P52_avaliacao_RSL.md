# P52 — Avaliação de elegibilidade, aderência às RQs e qualidade metodológica

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**Estudo:** Hasanov, I.; Virtanen, S.; Hakkala, A.; Isoaho, J. *Application of Large Language Models in Cybersecurity: A Systematic Literature Review*.  
**Escopo da análise:** exclusivamente o PDF fornecido. As páginas indicadas são as páginas **do PDF (1–28)**, e não a paginação impressa do periódico.  
**Natureza:** estudo secundário de síntese; a revisão contempla 177 trabalhos (resumo, p. 1; Seção II, pp. 3–5).

## Tabela A — Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P52 | *IEEE Access*, vol. 12 | 2024 | [VERIFICAR] | [VERIFICAR] (Q1 informado no prompt, não demonstrado pelo PDF) | [VERIFICAR] (A1 informado no prompt, não demonstrado pelo PDF) | Revisão sistemática da literatura (estudo secundário) | 10.1109/ACCESS.2024.3505983 |

**Evidência bibliométrica:** cabeçalho, resumo e identificação editorial da p. 1; identificação do método na Seção II, p. 3. O PDF não comprova número atual de citações, quartil SJR ou enquadramento Qualis.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Fundamentação |
|---|---|---|
| Ano ≥ 2020 | Atende | Publicado em 25 de novembro de 2024 (p. 1). |
| Veículo identificável | Atende | *IEEE Access*, volume 12 (p. 1). |
| Citações ≥ 1 | [VERIFICAR] | Contagem de citações externas do próprio artigo não constata no PDF. |
| SJR Q1–Q2 | [VERIFICAR] | Q1 é informado como metadado pelo prompt, sem comprovação documental no PDF. |
| Qualis A1–A2 | [VERIFICAR] | A1 é informado como metadado pelo prompt, sem comprovação documental no PDF. |

**Resultado formal: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis).** A indicação anterior de aprovação na triagem não substitui a evidência verificável exigida por este protocolo. A análise prossegue por ser candidato pendente, conforme o prompt.

## Tabela B — Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P52 | *Application of Large Language Models in Cybersecurity: A Systematic Literature Review* | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | Seção III.A–B, pp. 6–7; Seção IV.D, p. 13 | Discute execução autônoma em IA, aprendizado por reforço e RLHF com participação humana, bem como supervisão humana em sistemas de segurança. Não define sistematicamente *Agentic AI* nem articula planejamento, memória, ferramentas e modelos de tomada de decisão em um agente de IR. **a: parcial; b: parcial; c: insuficiente.** |
| P52 | Mesmo artigo | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | Seção IV.C.6, p. 12 (AI4CYBER e ciclo de incidentes); Seção IV.D, p. 13 (STRIDE-AI, 3LoD); Seção IV.G, pp. 19–21 (aplicações de LLMs) | Identifica frameworks e aplicações de IA na segurança, inclusive AI4CYBER alinhado ao NIST 800-61, mas não descreve uma arquitetura agêntica integrada, com orquestração, memória, uso de ferramentas, guardrails e observabilidade de produção. **a: parcial; b: parcial; c: insuficiente.** |
| P52 | Mesmo artigo | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | Seção III.A, pp. 6–7 (accuracy, precision, recall, F1, AUC-ROC); Seção IV.C, pp. 10–12 (resultados de estudos revisados); Seção V, pp. 21–22 | Sintetiza benefícios qualitativos (detecção, análise de logs, produtividade, apoio ao SOC) e métricas quantitativas de trabalhos primários citados. Contudo, os resultados são heterogêneos, sem avaliação empírica própria de copiloto agêntico nem medição consistente de MTTD, MTTR, carga cognitiva e qualidade decisória em IR. **a: presente; b: presente em estudos relatados; c: indireto/secundário.** |
| P52 | Mesmo artigo | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | Seção III.B, p. 7 (prompt injection/jailbreak); Seção IV.A–B, pp. 8–9 (privacidade, vieses, legislação e governança); Seção IV.D, pp. 12–14 (ataques e mitigação, STRIDE-AI, 3LoD); Seção V, p. 22 | Examina riscos técnicos (envenenamento de dados, ataques adversariais, insegurança e confiabilidade), questões éticas/legais (privacidade, viés, responsabilidade) e mecanismos de mitigação/governança (supervisão, padrões, modelagem de ameaças, estruturas regulatórias). A cobertura é sólida para IA/LLMs em cibersegurança, embora não específica de agentes. **a, b e c: presentes.** |
| P52 | Mesmo artigo | RQ5 — Research Gaps | Parcialmente Respondida | P (0,5) | Seção IV.D, p. 13 (benchmarks padronizados de robustez, threat models realistas); Seção V, pp. 21–22 (limitações e requisitos de utilização segura); Seção VI, pp. 22–23 (alucinações, verificação de saídas) | Aponta necessidade de avaliações mais realistas, benchmarking, regulação, confiabilidade e mitigação dos riscos. Não sistematiza lacunas específicas de orquestração multiagente, observabilidade do agente, autonomia controlada ou métricas operacionais da resposta a incidentes. |
| **P52** | **TOTAL** | **SCORE_RQ** | **3,0 / 5,0** | **P + P + P + T + P** | **Seções III–VI** | **Contribuição predominantemente fundacional e transversal, não evidência direta de sistema Agentic AI Copilot para IR.** |

**Nota de interpretação:** “T” em RQ4 indica cobertura das subdimensões explicitadas pelo protocolo; não implica que o artigo valide governança de agentes autônomos em produção. Métricas relatadas dos artigos primários não podem ser tratadas como medidas de um experimento conduzido por Hasanov et al.

## Tabela C — Avaliação de Qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P52 | Revisão sistemática da literatura (estudo secundário) | P (0,5) | P (0,5) | N (0,0) | Y (1,0) | **2,0 / 4,0** | **Média** |

### Fundamentação da pontuação QA

**QA1 — P (0,5), objetivos claros:** resumo e introdução (pp. 1–2) delimitam o problema da falta de síntese holística e apresentam três perguntas claras sobre eficácia, aplicações e limitações de LLMs em segurança. Porém, **não** apresentam como problema e solução centrais um *copiloto agêntico de resposta a incidentes*, exigência explícita da rubrica de QA1 desta RSL.

**QA2 — P (0,5), replicabilidade:** Seção II e Figura 1 (pp. 3–4) descrevem fontes pesquisadas, conjuntos de palavras-chave (Tabelas 2–5), período 2018–2024, critérios de seleção e fluxo 624 → 421 → 250 → 177. A própria Seção II informa que introdução, discussão e conclusão dos trabalhos foram examinadas em detalhe e o restante foi consultado superficialmente (p. 4). Não oferece arquitetura, configurações, parâmetros ou cenário experimental de um sistema agêntico que permitam sua replicação. Assim, há transparência **parcial** do protocolo de revisão, mas não replicação do artefato-alvo.

**QA3 — N (0,0), evidência empírica própria:** o artigo sintetiza resultados quantitativos e qualitativos dos 177 trabalhos (Seções II e IV), mas **não realiza experimento, simulação medida ou estudo de caso industrial próprio** com sistema Agentic AI Copilot para IR. Atribuir resultados de estudos primários ao artigo revisado produziria dupla contagem da evidência. A rubrica do prompt requer validação empírica e atribui N quando esta é ausente no estudo avaliado.

**QA4 — Y (1,0), coerência:** a discussão responde às três perguntas autorais (Seção V, pp. 21–22), e a conclusão sintetiza vantagens e limitações, incluindo saídas incorretas/alucinações e necessidade de checagem (Seção VI, pp. 22–23). As conclusões acompanham a natureza de revisão de literatura; generalizações devem ser interpretadas como síntese de estudos heterogêneos, não validação do desempenho de um agente.

**SCORE_QA = 0,5 + 0,5 + 0,0 + 1,0 = 2,0/4,0 (Média).**

## Parecer final do revisor

**Síntese:** O P52 reúne 177 estudos e estabelece um panorama relevante sobre aplicações de LLMs em cibersegurança, particularmente detecção, análise de logs, atividades de SOC, ameaças técnicas, ética e governança. Sua maior contribuição à RSL é a fundamentação de RQ4, com suporte complementar às RQ2, RQ3 e RQ5. A ausência de projeto e validação específicos de um copiloto agêntico para resposta a incidentes impede interpretá-lo como evidência primária de eficácia, autonomia, integração operacional ou redução de MTTD/MTTR. Metodologicamente, constitui estudo secundário, adequado para contextualização e identificação de referências primárias.

**Recomendação: INCLUIR COM RESSALVAS**, condicionada à verificação externa dos requisitos bibliométricos. Classificá-lo como **estudo fundacional/secundário**, não como validação empírica de um sistema agêntico. Ao agregar evidências, evitar contar métricas de estudos citados como experimentos independentes conduzidos no P52; conferir os trabalhos primários antes de transportar quaisquer números à síntese quantitativa.

**Pendências externas (não consultadas por restrição expressa do prompt):**

1. **Citações ≥ 1:** consultar Scopus, Web of Science, Google Scholar ou outra base indexadora e registrar data e contagem.
2. **SJR Q1–Q2:** consultar *SCImago Journal Rank*, periódico *IEEE Access*, ano de referência e quartil aplicável.
3. **Qualis A1–A2:** consultar Plataforma Sucupira / Qualis CAPES e conferir área e período válidos. A1 e Q1 fornecidos no prompt são **dados declarados de triagem**, não verificados pelo PDF.

**Decisão PRISMA provisória:** manter como **pendente de confirmação bibliométrica**, com **inclusão recomendada na categoria fundacional** após confirmação dos três requisitos.
