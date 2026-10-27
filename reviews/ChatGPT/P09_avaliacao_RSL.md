# Avaliação do estudo P09 — Corpus Fundacional da RSL

**RSL:** *Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura*  
**ID:** P09  
**Título:** *AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges*  
**Autores:** Ranjan Sapkota, Konstantinos I. Roumeliotis e Manoj Karkee  
**Natureza da avaliação:** avaliação retroativa de aderência às RQs e qualidade, sem rediscussão da inclusão herdada do Trabalho I.  
**Fonte primária:** PDF anexado, 30 páginas. As referências de página abaixo correspondem à numeração impressa no artigo.

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P09 | *Information Fusion*, v. 126, art. 103599 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão de literatura conceitual e taxonômica, com busca híbrida | `10.1016/j.inffus.2025.103599` |

**Evidência documental:** cabeçalho editorial e DOI na p. 1; resumo na p. 1; metodologia e estratégia de busca nas pp. 3–4. O artigo identifica 2026 como ano do volume, embora informe aceite em 30/07/2025 e disponibilização online em 22/08/2025 (p. 1). O ano adotado na tabela é **2026**, conforme a identificação bibliográfica do volume.

**Nota de rastreabilidade:** o roteiro de avaliação informa Qualis A1 e SJR Q1 como verificados em fonte anterior (`papers.csv`, 27/07/2026). Esses valores **não são verificáveis no PDF** e, por exigência do próprio protocolo, permanecem `[VERIFICAR]` na extração estritamente documental. Esse registro não invalida a verificação externa anterior, apenas evita apresentá-la como evidência extraída do artigo.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / pendência |
|---|---|---|
| Ano ≥ 2020 | Atendido | Ano bibliográfico 2026, p. 1. |
| Publicação identificável | Atendido | *Information Fusion*, v. 126, artigo 103599, p. 1. |
| Citações ≥ 1 | Pendente de verificação externa | O PDF não apresenta contagem atual de citações recebidas. |
| SJR Q1–Q2 | Pendente de verificação externa | O quartil não consta no PDF; roteiro informa Q1 previamente verificado. |
| Qualis A1–A2 | Pendente de verificação externa | O estrato não consta no PDF; roteiro informa A1 previamente verificado. |

**Resultado formal da triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, quartil SJR e estrato Qualis).** Prossegue-se à avaliação completa, conforme regra do protocolo para estudos pendentes. A decisão de inclusão original do corpus fundacional permanece inalterada.

## Etapa 2 — Extração e classificação das questões de pesquisa

**Escala:** T = Respondida Plenamente (1,0); P = Parcialmente Respondida (0,5); N = Não tem conteúdo suficiente (0,0).

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P09 | *AI Agents vs. Agentic AI* | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | Seções 2, 2.0.1 e 3; Figura 4 (p. 5), Figura 7 (p. 8), Tabelas 1–3 (pp. 9–10). | Define autonomia delimitada de agentes individuais e autonomia coordenada em sistemas multiagentes; especifica reatividade, especialização, planejamento, memória, ferramentas, decomposição de objetivos e mecanismos de decisão. Menciona intervenção humana, embora a taxonomia seja o foco principal. |
| P09 | *AI Agents vs. Agentic AI* | RQ2 — Engineering Architecture | Respondida Plenamente | **T (1,0)** | Seções 2.1.2 (p. 7), 3.0.1 (p. 7), 3.1 (a partir da p. 10) e 6.1 (pp. 22–24); Tabelas 4–9 (pp. 11–12) e Figura 13 (p. 23). | Compara arquiteturas monoagente e multiagente, orquestração centralizada/descentralizada, memória compartilhada/persistente e ferramentas/APIs; exemplifica AutoGPT, AutoGen, CrewAI, LangGraph e ReAct. Discute segurança, rastreabilidade e controles, mas não fornece arquitetura de produção validada pelo próprio estudo. |
| P09 | *AI Agents vs. Agentic AI* | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | Seção 4 (pp. 13–16), especialmente aplicações de suporte à decisão, automação de fluxos e resposta a incidentes de cibersegurança na p. 16; Figuras 10–11 (pp. 14–17). | Relata benefícios potenciais/qualitativos como adaptação, redução de esforço cognitivo, apoio à decisão e respostas mais rápidas. O exemplo de resposta a incidentes correlaciona logs, classifica ameaças e recomenda ações, porém não traz experimento próprio, comparação controlada nem valores verificáveis de MTTD, MTTR, latência, carga operacional ou precisão. O nível de evidência para IR é conceitual/ilustrativo. |
| P09 | *AI Agents vs. Agentic AI* | RQ4 — Challenges & Ethics | Respondida Plenamente | **T (1,0)** | Seções 5, 5.0.1, 5.0.2, 5.1 (pp. 16–22); Figura 12 (p. 18); seção 6.1 (pp. 22–24). | Abrange alucinações, raciocínio causal insuficiente, planejamento frágil, cascatas de erros, falhas de coordenação, comportamentos emergentes, riscos adversariais, confiança, explicabilidade, vieses e accountability. Propõe mecanismos como RBAC, sandboxing, identidade/autenticação dos agentes, auditoria, isolamento de papéis e controles de governança. |
| P09 | *AI Agents vs. Agentic AI* | RQ5 — Research Gaps | Respondida Plenamente | **T (1,0)** | Seção 5.1 (p. 22), seções 6.1–6.2 (pp. 22–25), Figura 13 (p. 23), Figura 14 (p. 25). | Identifica lacunas de causalidade, segurança, interoperabilidade, coordenação, verificabilidade, escalabilidade, avaliações e governança. Apresenta agenda futura de memória, planejamento coordenado, aprendizagem contínua, integração de ferramentas e operações orientadas à confiança. A observabilidade é tratada indiretamente por auditabilidade/rastreabilidade, sem um modelo específico de telemetria SRE. |
| **P09** | **TOTAL** | **SCORE_RQ** | | **4,5 / 5,0** | | **Forte aderência conceitual, arquitetural e de riscos; evidência empírica sobre benefícios em resposta a incidentes permanece insuficiente.** |

### Fundamentação por subdimensão

**RQ1 (a/b/c):** (a) autonomia caracterizada pela operação com pouca intervenção humana e pela coordenação de agentes especializados (seções 2.0.1 e 3); (b) características de especialização, reatividade, adaptação, memória e ferramentas (Figura 4, Tabelas 1–3); (c) decisão orientada a objetivos, decomposição de tarefas, ciclos de ação/feedback e orquestração (seções 2.1 e 3). **T**.

**RQ2 (a/b/c):** (a) diferencia arquiteturas individuais, redes especializadas e controladores centrais/distribuídos (seção 3.1); (b) descreve frameworks e mecanismos de invocação de ferramentas e APIs (seções 2.1.2 e 3.1); (c) cobre planejamento, memória, coordenação, comunicação e controles de segurança/governança (seções 3 e 6.1). **T**, considerando que a questão examina mecanismos arquiteturais, não exige implementação original.

**RQ3 (a/b/c):** (a) benefícios qualitativos afirmados e ilustrados, inclusive em ambiente corporativo de resposta a ameaças (seção 4); (b) não há métricas de benefício extraídas de uma avaliação empírica própria de IR; (c) evidências são principalmente narrativas, exemplos e literatura citada, sem validação quantitativa reproduzida. **P**.

**RQ4 (a/b/c):** (a) desafios técnicos extensamente mapeados (seção 5); (b) questões éticas e de accountability discutidas (seção 5.0.2); (c) salvaguardas de controle de acesso, isolamento, auditoria e governança propostas (seção 6.1). **T**.

**RQ5:** discussão explícita de limitações do campo (seção 5.1), de soluções ainda em maturação (seção 6.1) e de roteiro de pesquisa futura (seção 6.2). **T**.

## Etapa 3 — Avaliação de qualidade metodológica (DARE adaptado)

**Escala:** Y = 1,0; P = 0,5; N = 0,0. A pontuação obedece aos critérios operacionais da RSL, não a uma validação externa do método do artigo.

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P09 | Revisão conceitual e taxonômica da literatura | **Y (1,0)** | **P (0,5)** | **N (0,0)** | **Y (1,0)** | **2,5 / 4,0** | **Média** |

### Justificativa individual dos critérios de qualidade

**QA1 — Objetivos claros: Y (1,0).** O resumo e a introdução (pp. 1–3) explicitam o problema de confusão terminológica e arquitetural entre AI Agents e Agentic AI. O objetivo é propor distinção taxonômica, mapear aplicações e discutir desafios. Não reivindica resolver especificamente fadiga de alertas ou incidentes SRE, o que não prejudica a clareza de seu objetivo real.

**QA2 — Metodologia replicável: P (0,5).** O artigo apresenta um fluxo de revisão (Figura 3, p. 3) e uma busca híbrida com bases acadêmicas, interfaces de IA e exemplos de expressões de busca (seção 1.1.1, p. 4). Entretanto, a descrição não fornece, em nível suficiente para repetição fiel, datas completas das buscas, strings integrais por fonte, número de registros em cada etapa, protocolo de seleção, planilha de extração ou parâmetros experimentais de arquitetura. Há rastreabilidade parcial, não replicabilidade integral.

**QA3 — Base de evidências sólidas: N (0,0).** Trata-se de uma síntese de literatura, taxonomias e cenários ilustrativos. O PDF não apresenta experimento próprio, estudo de caso industrial conduzido pelos autores ou simulação com métricas de desempenho de um sistema agêntico. Exemplos de aplicações (seção 4), diagramas e afirmações de ganhos potenciais não devem ser convertidos em comprovação empírica. A Figura 1 apresenta tendências de interesse de busca, mas não valida benefícios de desempenho em IR.

**QA4 — Conclusões coerentes: Y (1,0).** A conclusão (seção 7, pp. 25–26) retoma as distinções, arquiteturas e desafios analisados ao longo do artigo. As limitações e críticas do campo são explicitadas na seção 5 e na seção 5.1. A conclusão é coerente com o caráter de revisão conceitual, desde que suas indicações de aplicabilidade não sejam interpretadas como comprovação experimental.

**Cálculo:** `SCORE_QA = 1,0 + 0,5 + 0,0 + 1,0 = 2,5 / 4,0` → banda **Média** (1,5–2,5).

## Parecer final do revisor

O P09 apresenta **elevada aderência temática** aos fundamentos de Agentic AI, descrevendo autonomia, tomada de decisão, memória, planejamento, ferramentas, orquestração multiagente, riscos e governança. É especialmente útil para sustentar a taxonomia e a justificativa arquitetural de um copiloto agêntico de resposta a incidentes. A seção 4 inclui um cenário de resposta a incidentes de cibersegurança envolvendo classificação de ameaças, correlação de logs, simulação de mitigação e recomendações a analistas humanos. Contudo, o artigo **não demonstra empiricamente redução de MTTD/MTTR nem de carga cognitiva em SRE**. Sua contribuição para RQ3 deve, portanto, ser interpretada como contexto e hipótese de benefício, não como evidência de eficácia operacional.

**Recomendação: INCLUIR COM RESSALVAS.** Preservar o estudo no corpus fundacional, conforme decisão herdada, usando-o como **base conceitual e arquitetural** (RQ1, RQ2, RQ4, RQ5). Exigir estudos empíricos independentes para fundamentar resultados quantitativos sobre resposta a incidentes (RQ3). A inclusão formal permanece condicionada à reconciliação documental das pendências bibliométricas do protocolo, sem refazer a decisão original do Trabalho I.

### Pendências de verificação externa

1. **Citações:** confirmar contagem ≥ 1 e registrar data e base consultada (por exemplo, Scopus, Web of Science ou Google Scholar).
2. **SJR:** confirmar quartil Q1–Q2 do periódico para o ano de referência aplicável no **SCImago Journal Rank**; o roteiro informa previamente **Q1**, mas o PDF não o comprova.
3. **Qualis CAPES:** conferir estrato A1–A2, área e quadriênio na **Plataforma Sucupira / Qualis CAPES**; o roteiro informa previamente **A1**, mas o PDF não o comprova.
4. **Referência bibliográfica:** manter separadas as datas de publicação antecipada online (2025) e do volume (2026), evitando divergência no cadastro da RSL.

### Registro compacto para consolidação

| ID | Ano | Tipo | RQ1 | RQ2 | RQ3 | RQ4 | RQ5 | SCORE_RQ | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda | Recomendação |
|---|---:|---|---|---|---|---|---|---:|---|---|---|---|---:|---|---|
| P09 | 2026 | Revisão conceitual/taxonômica | T | T | P | T | T | **4,5** | Y | P | N | Y | **2,5** | Média | **INCLUIR COM RESSALVAS** |

---

*Avaliação baseada exclusivamente no PDF fornecido e nos critérios operacionais explicitados em `prompt-P09.md`. Não houve consulta a fontes externas para preenchimento de indicadores bibliométricos.*
