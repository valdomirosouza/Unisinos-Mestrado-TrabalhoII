# Avaliação RSL — P19

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**Identificador:** P19  
**Artigo:** *Agent System Mining: Vision, Benefits, and Challenges*  
**Autores:** Andrei Tour; Artem Polyvyanyy; Anna Kalenkova  
**Condição:** Estudo fundacional herdado do Trabalho I; análise retroativa, sem rediscutir sua inclusão.  
**Critério:** Protocolo fornecido para a RSL, inspirado na avaliação DARE/Kitchenham (2009).  
**Fonte:** Exclusivamente o PDF anexado.

## Etapa 0 — Extração bibliométrica

O cabeçalho do artigo informa recebimento em 16/06/2021, aceite em 01/07/2021, publicação em 08/07/2021 e versão de 20/07/2021 (p. 99480). A identificação do periódico é *IEEE Access* (cabeçalho e rodapé do PDF); o DOI consta na primeira página.

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P19 | IEEE Access, vol. 9 | 2021 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Artigo de visão/proposição de framework conceitual, acompanhado de exemplo ilustrativo e revisão de trabalhos relacionados | 10.1109/ACCESS.2021.3095464 |

**Nota sobre metadados externos:** o prompt registra previamente **SJR Q1** e **Qualis A1**, mas estes valores não são comprováveis apenas pelo PDF. Portanto, figuram como **[VERIFICAR]** na Tabela A, sem invalidar o registro histórico do corpus. Não há contagem de citações recebidas pelo artigo no documento.

## Etapa 1 — Triagem de elegibilidade

| Critério | Constatação no PDF | Situação |
|---|---|---|
| Ano ≥ 2020 | Publicado em 2021 (p. 99480). | Atende |
| Veículo de publicação identificável | *IEEE Access*, volume 9 (pp. 99480–99494). | Atende |
| Citações ≥ 1 | O PDF contém referências bibliográficas, mas não informa quantas vezes o próprio artigo foi citado. | [VERIFICAR] |
| SJR Q1–Q2 | Quartil ausente do PDF. Prompt informa Q1 como registro externo anterior. | [VERIFICAR] |
| Qualis A1–A2 | Estrato ausente do PDF. Prompt informa A1 como registro externo anterior. | [VERIFICAR] |

**Resultado formal: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis).**

A análise prossegue porque o estudo é fundacional, previamente incluído, e o protocolo determina prosseguir também quando há pendências bibliométricas externas. Esta conclusão não implica nova decisão de inclusão ou exclusão no corpus.

## Etapa 2 — Extração e classificação das questões de pesquisa

**Escala:** T = Respondida Plenamente (1,0); P = Parcialmente Respondida (0,5); N = Não tem conteúdo suficiente (0,0). As RQs dizem respeito à RSL sobre **Agentic AI e resposta a incidentes**, não às três RQs próprias da revisão de literatura realizada pelos autores na Seção V.

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P19 | Agent System Mining: Vision, Benefits, and Challenges | RQ1 — Context Definitions | Parcialmente Respondida | P | Seção III.D, p. 99485; Seção IV.A–B, pp. 99485–99487 | Define autonomia, situacionalidade, proatividade e sociabilidade; descreve decisões locais de agentes e o papel dos especialistas no ciclo de modelagem. Não especifica memória, uso de ferramentas ou políticas de supervisão para sistemas de Agentic AI baseados em LLMs. |
| P19 | Agent System Mining: Vision, Benefits, and Challenges | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seções II e IV.A–B, pp. 99481–99488; Figuras 4, 6 e 7 | Apresenta arquitetura conceitual MAS com agentes, ambiente, interações, logs, simulador, repositório e cinco fases de ciclo de vida. Cita Disco e AnyLogic no exemplo; não apresenta arquitetura operacional de copiloto LLM, guardrails, gerenciamento de memória ou implantação de serviços agênticos em produção. |
| P19 | Agent System Mining: Vision, Benefits, and Challenges | RQ3 — Evidence Benefits | Parcialmente Respondida | P | Seção II, pp. 99481–99483; Seção IV.C, pp. 99488–99489 | Discute benefícios qualitativos esperados, como modelos mais interpretáveis, ciclos de modelagem menores, conformidade e análise de processos complexos. Não quantifica ganhos nem avalia MTTD, MTTR, tempo de resposta a incidentes ou carga operacional. O exemplo é ilustrativo. |
| P19 | Agent System Mining: Vision, Benefits, and Challenges | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seção IV.D, pp. 99489–99490; Figura 8 | Identifica desafios técnicos de metamodelo, escopo, interoperabilidade, validação, seleção de eventos, tipagem de agentes e descoberta de submodelos. Menciona privacidade de dados entre organizações, mas não desenvolve mecanismos de governança, accountability, auditoria de decisões autônomas ou guardrails para sistemas críticos. |
| P19 | Agent System Mining: Vision, Benefits, and Challenges | RQ5 — Research Gaps | Parcialmente Respondida | P | Seção IV.D, pp. 99489–99490; Seção V.C, pp. 99491–99492; Seção VI, p. 99492 | Identifica lacunas explícitas em metamodelos, algoritmos de descoberta, validação e mensuração da qualidade dos modelos MAS. Oferece agenda de pesquisa pertinente à engenharia multiagente, mas não trata especificamente de benchmarks de resposta a incidentes, threat models de Agentic AI, observabilidade de agentes LLM ou alinhamento. |
| **P19** | **TOTAL** | **SCORE_RQ** | **2,5 / 5,0** | **P + P + P + P + P** | — | **Aderência transversal conceitual, sem evidências específicas de copilotos agênticos em resposta a incidentes.** |

### Fundamentação por RQ

**RQ1 — Autonomia e tomada de decisão (P = 0,5).** A Seção III.D (p. 99485) identifica quatro atributos dos agentes: *autonomy, situatedness, proactivity* e *sociality*. A descrição de regras locais, estados, entradas e saídas permite compreender a emergência do comportamento coletivo (Seção III.D). A Seção IV distingue o papel de usuários e modeladores das atividades automatizáveis. A aderência é parcial porque a concepção é de agentes de modelagem/simulação e não inclui as capacidades contemporâneas de planejamento com LLM, memória persistente, ferramentas externas e autonomia graduada sob supervisão humana.

**RQ2 — Arquitetura de engenharia (P = 0,5).** A Figura 6 (p. 99487) relaciona usuários, objetivos, algoritmos ASM, registros de eventos, modelos e simuladores. A Figura 7 (p. 99488) apresenta um ciclo com **Motivate, Plan, Develop, Evaluate e Use**. O texto descreve sete atividades: **search, project, discover, enhance, integrate, diagnose e check** (Seção IV.B, pp. 99487–99488). O desenho é arquiteturalmente aproveitável para o domínio de modelagem multiagente, mas não é uma especificação implementável de um copiloto de IR baseado em LLMs.

**RQ3 — Benefícios e métricas (P = 0,5).** A Seção IV.C (pp. 99488–99489) separa ganhos diretos e indiretos: descoberta baseada em eventos, redução potencial de ciclos de desenvolvimento, conformidade e gestão de processos complexos, flexíveis e sensíveis ao contexto. A Seção II inclui um exemplo de processamento de pedidos, modelos DFM e visualização de uma simulação (Figuras 1–4). Esses elementos dão suporte à plausibilidade da proposta, mas não a um efeito quantitativo observado e generalizável. Não há indicadores reportados de redução de tempo ou carga cognitiva em resposta a incidentes.

**RQ4 — Riscos, ética e governança (P = 0,5).** Os oito desafios enumerados na Seção IV.D incluem seleção de metamodelo, definição de escopo, suporte à simulação e análise estática, validação, seleção de eventos, identificação de tipos de agentes, descoberta de submodelos e seleção de linguagem. A p. 99490 destaca possível indisponibilidade de logs completos por exigências de preservação de privacidade. Essa menção não constitui proposta de controles éticos, autorização de ações, accountability, governança de IA ou contenção de autonomia.

**RQ5 — Lacunas e pesquisa futura (P = 0,5).** A conclusão (p. 99492) organiza a agenda futura em três linhas: metamodelos/formalismos para MAS descobertos de dados de processos; algoritmos de descoberta e melhoria de modelos executáveis; e técnicas para avaliar qualidade de modelos inferidos. A seção também solicita análises futuras de benefícios em diferentes setores, reforçando que a validação da proposta ainda é limitada. Trata-se de contribuição útil como base conceitual, mas não supre as lacunas específicas de segurança, avaliação e observabilidade de copilotos agênticos de IR.

## Etapa 3 — Avaliação de qualidade DARE-adaptada

**Escala:** Y = 1,0; P = 0,5; N = 0,0. **Bandas:** Alta ≥ 3,0; Média de 1,5 a 2,5; Baixa < 1,5.

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---:|---|
| P19 | Visão e proposição de framework conceitual, com exemplo ilustrativo e revisão de literatura | Y (1,0) | P (0,5) | P (0,5) | Y (1,0) | **3,0 / 4,0** | **Alta** |

### Justificativas com evidências

**QA1 — Objetivos claros: Y (1,0).** O resumo (p. 99480) e a introdução (pp. 99480–99481) apresentam a limitação de modelos tradicionais de Process Mining, notadamente modelos de fluxo difíceis de compreender (*spaghetti models*), e o objetivo de propor ASM e seu framework. O problema e a solução baseada em sistemas multiagentes são explícitos. A nota alta mede clareza **do objetivo do artigo**, não identidade entre MAS tradicional e Agentic AI baseada em LLMs.

**QA2 — Metodologia replicável: P (0,5).** A Seção IV.B (pp. 99486–99488), Figuras 6–7 e a descrição das sete atividades fornecem estrutura, entradas, saídas e tarefas. A Seção V.B (p. 99491) explicita bases Scopus e Web of Science, consultas, filtros e data de busca para a revisão de trabalhos relacionados. Apesar disso, a proposta ASM não fornece implementação completa dos algoritmos, parâmetros de execução, protocolo experimental e infraestrutura suficientes para reproduzir integralmente a inferência automática proposta. Replicabilidade **da busca bibliográfica** não equivale à replicabilidade **do framework ASM**.

**QA3 — Base de evidências sólidas: P (0,5).** A Seção II (pp. 99481–99483, Figuras 1–4) apresenta um caso **hipotético/simplificado** de atendimento de pedidos e demonstra modelos de processo e uma execução ilustrativa de simulação AnyLogic. Pela rubrica fornecida, *toy example* recebe P. Não há ensaio comparativo nem medição empírica de eficácia do ASM com métricas de desempenho. Essa nota não deve ser interpretada como validação industrial.

**QA4 — Conclusões coerentes: Y (1,0).** A Seção VI (p. 99492) apresenta ASM explicitamente como uma **visão**, retoma o exemplo ilustrativo e identifica trabalho futuro para implementar algoritmos e avaliar qualidade e benefícios. A Seção IV.D (pp. 99489–99490) desenvolve limitações técnicas. As conclusões permanecem alinhadas ao caráter propositivo do estudo e não afirmam comprovação quantitativa dos benefícios.

**Interpretação da banda:** a pontuação **Alta (3,0)** decorre estritamente da soma dos quatro quesitos desta rubrica, principalmente clareza e coerência. Ela **não significa evidência empírica robusta**, prontidão de produção ou aderência direta a resposta a incidentes. QA2 e QA3 permanecem apenas parciais.

## Parecer final do revisor

O artigo fornece fundamentação consistente para representação de processos complexos como comportamentos emergentes de agentes distribuídos, com apoio de logs de eventos e modelos executáveis. O framework ASM explicita atividades de descoberta, integração, diagnóstico e verificação relevantes para a engenharia de sistemas multiagentes. Sua contribuição à RSL sobre copilotos agênticos de resposta a incidentes é **indireta e conceitual**: não aborda LLMs, copilotos operacionais, automação de incidentes ou resultados de MTTD, MTTR e carga cognitiva. A qualidade formal alcança **3,0/4,0**, mas o suporte empírico à proposta é limitado a um exemplo ilustrativo, sem métricas comparativas.

**Recomendação: INCLUIR COM RESSALVAS.** Preservar o estudo no corpus fundacional herdado, com uso prioritário na fundamentação de MAS, descoberta orientada por eventos e engenharia de modelos. Não apresentá-lo como evidência de eficácia de Agentic AI em resposta a incidentes, nem como validação experimental de um copiloto baseado em LLMs.

### Pendências de verificação externa

1. **Citações recebidas pelo artigo [VERIFICAR]:** consultar base indexadora bibliométrica (Scopus, Web of Science ou outra definida pelo protocolo), na data de referência da RSL.
2. **Quartil SJR [VERIFICAR]:** confirmar Q1/Q2 na **SCImago Journal Rank**, registrando o ano de referência utilizado.
3. **Qualis CAPES [VERIFICAR]:** confirmar A1/A2 na **Plataforma Sucupira / Qualis CAPES**, especificando quadriênio e área de avaliação.

O prompt do estudo registra anteriormente **Q1** e **A1** como verificações externas; estes valores não foram refeitos nem atestados a partir do PDF, conforme a regra de fonte exclusiva.

---

## Resumo para transcrição nas tabelas da RSL

- **Tabela 3:** P19; IEEE Access; 2021; citações/SJR/Qualis [VERIFICAR]; artigo de visão/framework conceitual; DOI 10.1109/ACCESS.2021.3095464.
- **Tabela 5:** RQ1=P; RQ2=P; RQ3=P; RQ4=P; RQ5=P; **SCORE_RQ=2,5/5,0**.
- **Tabela 7:** QA1=Y; QA2=P; QA3=P; QA4=Y; **SCORE_QA=3,0/4,0 (Alta)**.
- **Decisão:** **INCLUIR COM RESSALVAS**, preservando sua posição de estudo fundacional.
