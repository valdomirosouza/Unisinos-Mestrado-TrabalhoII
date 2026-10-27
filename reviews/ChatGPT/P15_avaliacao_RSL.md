# Avaliação de qualidade e aderência à RSL — P15

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**Corpus:** Fundacional (P01–P19), inclusão herdada do Trabalho I  
**Protocolo:** prompt-P15(1).md; avaliação de aderência às RQs e qualidade no padrão DARE (QA1–QA4).  
**Fonte primária:** Bandi, A.; Kongari, B.; Naguru, R.; Pasnoor, S.; Vilipala, S. V. *The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges*. **Future Internet**, 17(9), artigo 404, 2025. https://doi.org/10.3390/fi17090404 (p. 1).

> **Nota metodológica:** Esta é uma avaliação retroativa de um estudo já incluído no corpus fundacional. Não constitui nova decisão de seleção. As evidências e os julgamentos abaixo derivam exclusivamente do PDF. Dados de indexadores externos são separados e marcados como **[VERIFICAR]**, mesmo quando o prompt informa valores previamente registrados.

## Etapa 0 — Tabela A: Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P15 | Future Internet | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado no prompt) | [VERIFICAR] (A2 informado no prompt) | Revisão de literatura / survey de escopo amplo | 10.3390/fi17090404 |

**Evidência:** cabeçalho editorial e resumo, p. 1; metodologia de busca e seleção de 143 estudos primários, seção 2, p. 5. O texto também informa consulta a 21 artigos de revisão (seção 2, p. 5). Esses dados descrevem o corpus secundário da revisão e **não** constituem experimento original dos autores.

## Etapa 1 — Elegibilidade formal

| Critério | Verificação | Resultado |
|---|---|---|
| Ano ≥ 2020 | Publicado em 4 de setembro de 2025 (p. 1). | Atende |
| Publicação identificável | Future Internet, 17, 404 (p. 1). | Atende |
| Citações ≥ 1 | Contagem de citações não demonstrável no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | Prompt registra Q1, mas o quartil não é verificável no PDF. | [VERIFICAR] |
| Qualis A1–A2 | Prompt registra A2, mas o estrato não é verificável no PDF. | [VERIFICAR] |

**Resultado formal:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR, Qualis).** Conforme o protocolo, a extração prossegue. O vínculo ao corpus fundacional permanece herdado, sem rediscussão de inclusão.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P15 | The Rise of Agentic AI | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | §3.1, pp. 7–10; Tabela 2, pp. 8–9; §3.3, pp. 13–14 | Define autonomia orientada a objetivos e supervisão limitada (a), caracteriza planejamento, memória, ferramentas, reflexão e coordenação (b), e distingue modelos de decisão adaptativa e execução multietapas (c). |
| P15 | The Rise of Agentic AI | RQ2 — Engineering Architecture | Respondida Plenamente | **T (1,0)** | §3.2, pp. 10–12 e Tabela 3, p. 10; §3.3, pp. 13–17, Figuras 4 e 5 e modelos arquiteturais subsequentes | Discute tipos arquiteturais, incluindo ReAct, supervisor/hierárquico, híbrido reativo-deliberativo, BDI e neuro-simbólico (a); compara frameworks e ferramentas (b); descreve memória, reflexão, orquestração, execução, monitoramento e verificações (c). Não oferece um blueprint industrial comprovado de SRE. |
| P15 | The Rise of Agentic AI | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | §3.6, pp. 33–38; Figura 11, p. 34; §3.6.2, pp. 36–38 | Sintetiza benefícios qualitativos (explicabilidade, satisfação, robustez) e métricas quantitativas reportadas por trabalhos citados (ex.: acurácia e Task Completion Time). Porém, não produz validação empírica própria nem demonstra ganhos específicos de MTTD, MTTR ou carga operacional/cognitiva em incident response. |
| P15 | The Rise of Agentic AI | RQ4 — Challenges & Ethics | Respondida Plenamente | **T (1,0)** | §3.7, pp. 38–40; seção de segurança, p. 40; §4, pp. 40–41 | Discute falhas técnicas, planejamento e coordenação, integrações e robustez (a); privacidade, vieses, transparência e responsabilização (b); e propõe mecanismos como auditoria contínua, guardrails, supervisão humana e secure-by-design (c). |
| P15 | The Rise of Agentic AI | RQ5 — Research Gaps | Respondida Plenamente | **T (1,0)** | §2, pp. 5–6; §3.6, pp. 33–38; §3.7, pp. 38–40; §4, pp. 40–41 | Identifica lacunas em benchmarks padronizados, avaliação de desempenho e recuperação de falhas; aponta necessidade de arquiteturas mais robustas, coordenação, transparência, segurança e governança. Trata observabilidade operacional e threat models específicos de IR com menor profundidade. |
| **P15** | **TOTAL** | **SCORE_RQ** | | **4,5 / 5,0** | | **Forte aderência como referência conceitual e arquitetural; aderência empírica à resposta a incidentes é limitada.** |

**Nota sobre RQ3:** os valores numéricos de desempenho descritos na seção 3.6 são **resultados secundários atribuídos a pesquisas referenciadas pelo survey**. Não são resultados de um benchmark próprio de P15, e não devem ser transportados para a síntese como evidência causal de redução de MTTD/MTTR.

### Rastreamento por subdimensão

- **RQ1:** a) autonomia orientada a objetivos: §3.1, p. 7; b) planejamento, memória e uso de ferramentas: §3.1, pp. 8–9; c) decisão contextual e adaptação: Tabela 2, pp. 8–9.
- **RQ2:** a) modelos de arquitetura: §3.3.2, p. 14 e seguintes; b) frameworks: Tabela 3, p. 10; c) monitoramento, reflexão, limites de execução e controle de fluxo: §3.3.1, pp. 13–14 e §3.6.1, p. 35.
- **RQ3:** a) benefícios qualitativos, §3.6.2, p. 36; b) métricas quantitativas, §3.6.2, pp. 37–38; c) evidência própria: **ausente**; a seção sistematiza pesquisas anteriores.
- **RQ4:** a) desafios arquiteturais e de coordenação, §3.7, pp. 38–40; b) riscos éticos e responsabilidade, §3.7, p. 39; c) auditoria, guardrails e secure-by-design, §3.7, p. 40.
- **RQ5:** lacunas sobre métricas padronizadas, recuperação de erros e segurança, §2, p. 6 e §§3.6–3.7, pp. 38–40; síntese de necessidades futuras em §4, pp. 40–41.

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P15 | Revisão de literatura / survey | **Y (1,0)** | **P (0,5)** | **N (0,0)** | **Y (1,0)** | **2,5 / 4,0** | **Média** |

### Fundamentação DARE

**QA1 — Objetivos claros: Y (1,0).** A seção 1.1 (p. 3) estabelece o objetivo de sintetizar definições, frameworks, arquitetura, aplicações, formatos de entrada e saída, métodos de avaliação e desafios. A seção 1.2 (pp. 3–4) apresenta sete perguntas específicas do *próprio artigo*. O problema é a fragmentação de conhecimentos sobre sistemas agênticos, não especificamente fadiga de alertas ou incidentes operacionais.

**QA2 — Metodologia replicável: P (0,5).** A seção 2 (p. 5) identifica bases de busca, expressão de consulta, remoção de duplicatas, triagem de resumos/conclusões e seleção de 143 estudos. Há transparência parcial do processo. Entretanto, não são detalhadas, de forma suficiente para reprodução integral, as buscas individualizadas por base, suas datas exatas, fluxo de exclusões e critérios operacionalizados completos. Tampouco se apresenta arquitetura experimental com parâmetros de um protótipo implementado pelo próprio estudo. Portanto, não cabe Y.

**QA3 — Base de evidências sólidas: N (0,0).** O artigo apresenta levantamento e análise de literatura, inclusive números de desempenho que pertencem aos trabalhos citados (§3.6.2, pp. 36–38), mas não executa experimento original, estudo de caso industrial próprio ou simulação quantitativa replicável que valide sua síntese. Sob a rubrica estrita solicitada (teórico = N), a atribuição é N. Isso não invalida o valor bibliográfico da revisão.

**QA4 — Conclusões coerentes: Y (1,0).** A seção 4 (pp. 40–41) retoma as dimensões analisadas e ressalta riscos técnicos, sociais e de governança; a seção 3.7 (pp. 38–40) detalha limitações. As conclusões são proporcionais a uma síntese descritiva, sem apresentar resultados experimentais como se fossem próprios.

**Cálculo:** 1,0 + 0,5 + 0,0 + 1,0 = **2,5**. Conforme a faixa do protocolo, **qualidade Média** (1,5–2,5).

## Parecer final do revisor

**Síntese:** O artigo P15 é uma revisão ampla, com 143 estudos primários e 21 revisões complementares descritos na metodologia, que oferece forte sustentação a conceitos de autonomia, capacidades de agentes, frameworks, padrões arquiteturais e desafios de implantação. É particularmente útil para fundamentar a estrutura e os requisitos de um copiloto agêntico de resposta a incidentes, inclusive reflexão, monitoramento, limites de ação e supervisão humana. A contribuição à avaliação operacional é indireta: as métricas são compiladas de fontes secundárias e não demonstram, no estudo, redução de MTTD, MTTR ou carga cognitiva de equipes SRE. O método de revisão é parcialmente reproduzível e falta validação empírica própria.

**Recomendação: INCLUIR COM RESSALVAS.** Manter P15 no corpus fundacional herdado, utilizando-o prioritariamente para a síntese conceitual (RQ1), arquitetural (RQ2), de riscos/governança (RQ4) e lacunas (RQ5). Para RQ3, empregá-lo como referência sobre *categorias de métricas e avaliação*, não como evidência de efetividade de um copiloto de IR. A recomendação não reabre a inclusão herdada; qualifica seu peso na síntese comparativa.

**Pendências de verificação externa:**

1. **Citações ≥ 1:** consultar base indexadora (Scopus, Web of Science ou Google Scholar) e registrar data e contagem.
2. **SJR Q1–Q2:** confirmar quartil do periódico e ano de referência no **SCImago Journal Rank**. O prompt registra Q1, mas a checagem não é parte desta leitura do PDF.
3. **Qualis A1–A2:** confirmar área e quadriênio pertinentes na **Plataforma Sucupira / Qualis CAPES**. O prompt registra A2, mas a checagem não é parte desta leitura do PDF.

**Nota de consolidação:** Aplicar as linhas das três tabelas aos quadros 3, 5 e 7 da RSL, mantendo as colunas de verificabilidade bibliométrica pendentes até conferência documental em fonte externa.
