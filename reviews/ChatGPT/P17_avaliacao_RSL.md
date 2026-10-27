# P17 — Avaliação retroativa do corpus fundacional da RSL

**RSL:** *Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura*  
**ID:** P17  
**Artigo:** Chamola, V. et al. *A Review of Trustworthy and Explainable Artificial Intelligence (XAI).*  
**Fonte exclusiva da avaliação de conteúdo:** PDF do artigo fornecido.  
**Natureza:** estudo fundacional herdado do Trabalho I. A inclusão prévia não é rediscutida.

## Etapa 0 — Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P17 | IEEE Access, v. 11 | 2023 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão narrativa abrangente / survey sobre TAI e XAI | 10.1109/ACCESS.2023.3294569 |

**Rastreabilidade:** o título, o DOI e as datas de publicação estão na primeira página do PDF (p. 1, página editorial 78994); a natureza de revisão é indicada no resumo e na introdução (pp. 1–4, 78994–78997). O PDF não comprova contagem atualizada de citações, classificação SJR ou Qualis CAPES. O prompt informa **SJR Q1** e **Qualis A1** como previamente verificados em base externa, mas, conforme a regra de avaliação exclusiva do PDF, esses valores **não são reproduzidos como verificações independentes** na tabela.

## Etapa 1 — Triagem de elegibilidade (PRISMA)

| Critério | Constatação | Situação |
|---|---|---|
| Ano ≥ 2020 | Publicado em 2023 (p. 1, 78994). | Atende |
| Publicação identificável | IEEE Access, volume 11 (p. 1, 78994). | Atende |
| Citações ≥ 1 | Não há contagem de citações recebidas pelo artigo no PDF. As referências citadas **pelo** artigo não constituem essa métrica. | [VERIFICAR] |
| SJR Q1–Q2 | A classificação do periódico não é demonstrada pelo PDF. | [VERIFICAR] |
| Qualis A1–A2 | A classificação do periódico não é demonstrada pelo PDF. | [VERIFICAR] |

**Resultado: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis).** Prossegue-se à avaliação de conteúdo porque o protocolo admite essa situação. O P17 permanece integrante do corpus fundacional por decisão herdada, sem uma nova deliberação de inclusão bibliométrica.

## Etapa 2 — Classificação das questões de pesquisa (Tabela 5)

**Escala:** T = Respondida Plenamente (1,0); P = Parcialmente Respondida (0,5); N = Não tem conteúdo suficiente (0,0). A cobertura considera as subdimensões de cada RQ e a diferença entre IA/XAI geral e Agentic AI aplicada à resposta a incidentes.

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI) | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | § II.A, *Human Agency and Oversight*, p. 4 (78997); § III.D, *Robotics and Autonomous AI*, p. 9 (79002). | Discute autonomia de sistemas de IA, interação decisória e supervisão HITL/HOTL/HIC. Não caracteriza conjuntamente planejamento, memória e uso de ferramentas de Agentic AI nem especifica modelo decisório de copiloto agêntico. |
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI) | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | § III.E, *Explainability in AI*, pp. 9–10 (79002–79003); § IV, *Developments in XAI*, pp. 10–12 (79003–79005), com Fig. 10 e métodos locais/globais. | Apresenta técnicas implementáveis para explicabilidade, como LIME, PDP, ALE, ICE, modelos substitutos e explicações *post hoc*. Elas são mecanismos auxiliares potenciais de governança, não uma arquitetura de orquestração agêntica em produção com memória, ferramentas, observabilidade e guardrails integrados. |
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI) | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | § III.E, pp. 9–10 (79002–79003); § V.B, *Banking and Commerce*, p. 14 (79008); § V.D, *Explainable AI for Autonomous Systems*, pp. 16–17 (79010–79011), Tabela 2. | Relata qualitativamente compreensão, transparência, detecção de comportamento inadequado e confiança. Compila resultados quantitativos de pesquisas citadas sobre outros domínios, sem experimento próprio e sem indicadores de resposta a incidentes (MTTD, MTTR, tempo de resposta operacional ou carga cognitiva). |
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI) | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | § II.A–G, pp. 4–7 (78997–79000), em especial Tabela 1, p. 3 (78996); § V.C.1–2, pp. 14–15 (79008–79009). | Cobre explicitamente desafios técnicos (robustez, ataques adversariais, confiabilidade), desafios éticos (viés, privacidade, autonomia, accountability) e mecanismos de governança (supervisão humana, transparência, direitos, princípios e normas de segurança). Evidência robusta para os três eixos, embora no contexto mais amplo de IA confiável. |
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI) | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | § VI, *Conclusion*, p. 17 (79011–79012); § IV, pp. 10–12 (79003–79005), Fig. 9. | Explicita lacunas de reprodutibilidade de explicações *post hoc*, ausência de critérios e métricas unificados, tensões entre desempenho e interpretabilidade e dificuldades em explicar redes neurais profundas. Contribuição a benchmarking e confiança/alinhamento; não propõe agenda específica para observabilidade ou avaliação de sistemas multiagentes em incidentes. |
| **P17** | **Total** | **SCORE_RQ** | **3,0 / 5,0** | **P + P + P + T + T** | **Seções II–VI** | **Aderência conceitual relevante; evidência operacional/agêntica indireta.** |

### Fundamentação pelas subdimensões

**RQ1:** (a) autonomia: presente em sentido geral, incluindo supervisão humana; (b) características nucleares: cobertura incompleta, sem memória, planejamento e ferramentas como conjunto agêntico; (c) tomada de decisão: exemplos de decisões automatizadas e explicabilidade, sem ciclo formal de decisão de agentes. **P**.

**RQ2:** (a) arquitetura: modelos de IA/XAI e arquiteturas conceituais de explicação, não arquitetura de agentes em produção; (b) ferramentas/métodos: LIME, PDP, ALE, ICE e substitutos, detalhados como métodos de XAI; (c) capacidades avançadas: interpretabilidade, transparência e mecanismos de controle em nível conceitual. **P**.

**RQ3:** (a) benefícios qualitativos: sim, para confiança e compreensão de decisões; (b) benefícios quantitativos/métricas: o texto cita e resume achados externos de XAI/autonomia, sem métricas de MTTD/MTTR/carga operacional próprias; (c) nível de evidência: revisão secundária, sem validação experimental originária. **P**.

**RQ4:** (a) desafios técnicos: sim; (b) éticos/de governança: sim; (c) mecanismos de governança: sim, com tabela de princípios e supervisão humana. **T**.

**RQ5:** discute lacunas e necessidades de pesquisa com especificidade na área de XAI, sobretudo reprodutibilidade, critérios padronizados de avaliação e compromisso entre desempenho e explicabilidade. A transferência para Agentic AI/IR é uma **inferência de aplicabilidade**, não um resultado testado no artigo. **T**, considerando a formulação ampla da RQ5.

## Etapa 3 — Avaliação de qualidade DARE adaptada (Tabela 7)

**Escala:** Y = 1,0; P = 0,5; N = 0,0. Banda alta ≥ 3,0; média 1,5–2,5; baixa < 1,5.

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P17 | Survey / revisão narrativa abrangente sobre TAI e XAI | P (0,5) | N (0,0) | N (0,0) | Y (1,0) | **1,5 / 4,0** | **Média** |

### Justificativas QA

**QA1 — Objetivos Claros: P (0,5).** O resumo e a introdução, pp. 1–4 (78994–78997), definem claramente a necessidade de IA confiável e explicável e o propósito de revisar seus componentes e aplicações. Entretanto, o problema de resposta a incidentes e a proposta de solução **agêntica** não são objetivos do estudo. Pelo critério particular da RSL, a correspondência é parcial, e não plena.

**QA2 — Metodologia Replicável: N (0,0).** A introdução e a Fig. 3 (p. 5, 78998) organizam os tópicos da revisão. As seções posteriores descrevem métodos e estudos de terceiros, mas o artigo não explicita protocolo reprodutível de seleção e análise bibliográfica nem arquitetura, parâmetros, implementação e cenário experimental de um sistema próprio de Agentic AI. Explicação conceitual de técnicas de XAI não equivale à replicabilidade de uma solução avaliada.

**QA3 — Base de Evidências Sólidas: N (0,0).** As seções III–V, em especial a Tabela 2 (p. 17, 79011), compilam resultados e exemplos de trabalhos anteriores. Não há experimento, estudo de caso industrial ou simulação quantitativa **executada e reportada pelos autores** para a proposta objeto da RSL. Resultados quantitativos de fontes citadas não foram tomados por validação original do P17.

**QA4 — Conclusões Coerentes: Y (1,0).** A § VI, *Conclusion* (p. 17, 79011–79012), retoma os objetivos da revisão, sintetiza os desafios de IA explicável e reconhece limites: replicabilidade de explicações, métricas não unificadas, compromisso desempenho/interpretabilidade e dificuldade de explicar redes profundas. As conclusões são proporcionais ao conteúdo de revisão apresentado, sem alegar comprovação experimental própria.

**Nota interpretativa:** a banda **Média** decorre estritamente da rubrica operacional da RSL, voltada a soluções agênticas empiricamente avaliadas. Não constitui uma afirmação de que a revisão publicada seja de baixa qualidade editorial ou científica em seu próprio campo.

## Parecer final do revisor

O P17 sustenta a discussão transversal de **confiabilidade, explicabilidade, supervisão humana e governança** que deve orientar copilotos agênticos usados em ambientes críticos. Seus principais aportes estão em **RQ4** e **RQ5**, ao organizar riscos, mecanismos de controle e lacunas de avaliação de XAI; em RQ1–RQ3, a correspondência é parcial e essencialmente indireta. O artigo **não** apresenta arquitetura de resposta a incidentes, orquestração de múltiplos agentes, observabilidade operacional integrada nem validação de redução de MTTD, MTTR ou carga cognitiva. Deve, portanto, apoiar a fundamentação e discussão de riscos, não ser contado como evidência empírica de eficácia de copilotos agênticos para IR.

**Recomendação: INCLUIR COM RESSALVAS.** Manter no **corpus fundacional herdado**, sem reabrir a decisão de inclusão do Trabalho I, assinalando explicitamente a natureza conceitual/transversal da contribuição. **SCORE_RQ: 3,0/5,0. SCORE_QA: 1,5/4,0 (Média).**

### Pendências externas

1. **Citações recebidas pelo artigo:** [VERIFICAR] em uma base indexadora (p. ex., Scopus, Web of Science ou Google Scholar), registrando data da consulta e contagem identificada.
2. **SJR:** [VERIFICAR] em *SCImago Journal Rank* o quartil correspondente ao periódico e ao ano pertinente. O prompt registra Q1 como histórico, não confirmado a partir do PDF.
3. **Qualis CAPES:** [VERIFICAR] na *Plataforma Sucupira / Qualis CAPES*, documentando área e quadriênio de referência. O prompt registra A1 como histórico, não confirmado a partir do PDF.

**Controle de não fabricação:** não foram inferidas estatísticas de citações a partir do volume de referências, nem resultados de MTTD/MTTR a partir de benefícios genéricos de XAI. As páginas editoriais referidas são aquelas impressas no próprio PDF; a numeração física do documento é de 22 páginas.
