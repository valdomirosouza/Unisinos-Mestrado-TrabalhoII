# Avaliação do Estudo P82 — Ciclo 2 da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P82  
**Título:** Artificial Intelligence Agent-Enabled Predictive Maintenance: Conceptual Proposal and Basic Framework  
**Autores:** Wenyu Jiang; Fuwen Hu  
**Fonte analisada:** PDF fornecido, 15 páginas.  
**Escopo metodológico:** avaliação documental baseada exclusivamente no artigo, segundo a rubrica fornecida no `prompt-P82.md`. Não foi realizada pesquisa externa.

## Etapa 0 — Tabela A: Extração bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P82 | *Computers*, v. 14, art. 329 | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado na triagem, não comprovado no PDF) | [VERIFICAR] (A2 informado na triagem, não comprovado no PDF) | Proposta conceitual/arquitetural com demonstração exploratória de protótipo (PoC) | https://doi.org/10.3390/computers14080329 |

**Evidências:** identificação bibliográfica e DOI na p. 1; proposta arquitetural nas seções 3–4 (pp. 6–11); caracterização como proposta conceitual e reconhecimento da insuficiência de evidência comparativa na conclusão (pp. 12–13).

**Distinção importante:** os valores preliminares **SJR Q1** e **Qualis A2** constam dos insumos de triagem, mas não são verificáveis no corpo do artigo; não devem ser registrados como validados. Não há contagem verificável de citações do próprio artigo no PDF.

## Etapa 1 — Triagem de elegibilidade (PRISMA)

| Critério | Resultado | Evidência / condição |
|---|---|---|
| Ano ≥ 2020 | Atende | Publicado em 15 de agosto de 2025 (p. 1). |
| Publicação identificável | Atende | *Computers*, 14, 329 (p. 1). |
| Citações ≥ 1 | [VERIFICAR] | O PDF não informa a contagem atual de citações recebidas pelo artigo. |
| SJR Q1–Q2 | [VERIFICAR] | Q1 fornecido na triagem, não verificável no PDF. |
| Qualis A1–A2 | [VERIFICAR] | A2 fornecido na triagem, não verificável no PDF. |

**Resultado formal:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR, Qualis)**. A extração e avaliação prosseguem, conforme a regra expressa para estudos com elegibilidade pendente. A aprovação na triagem inicial não substitui a comprovação dos três critérios bibliométricos.

## Etapa 2 — Tabela B: Classificação das questões de pesquisa (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P82 | Jiang e Hu (2025) | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | Seção 1, pp. 3–4; seção 3.3, p. 7; seção 4.1, p. 10 | Define agentes com percepção, decisão e ação orientada a objetivos; descreve planejamento, memória, ferramentas, interação e segurança, além de um fluxo de tomada de decisão. O grau efetivo de autonomia e a intervenção humana não são operacionalmente quantificados; a cobertura é conceitual, fora do domínio de IR. |
| P82 | Jiang e Hu (2025) | RQ2 — Engineering Architecture | Respondida Plenamente | **T (1,0)** | Seções 2.1–2.2, pp. 4–6, Figura 1 e Tabela 1; seções 3–4.2, pp. 6–11, Figuras 2–6 | Detalha arquitetura edge–fog–cloud, módulos de percepção/raciocínio/ação/aprendizagem, funções dos agentes, RAG, digital twin, LLMOps, protocolos MCP/A2A e tecnologias como Dify, RAGFlow e DeepSeek. Traz capacidades avançadas arquiteturais, mas não comprova guardrails e observabilidade operacionais em produção. |
| P82 | Jiang e Hu (2025) | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | Resumo, p. 1; seção 4.1, p. 9; seção 4.2, pp. 10–11; discussão e conclusão, pp. 12–13 | Apresenta benefícios qualitativos esperados e uma demonstração exploratória. Menciona acurácia de 95% para classificadores e redução de desenvolvimento de semanas para horas, mas não apresenta desenho experimental, dados, amostras, baselines ou método de mensuração que sustentem essas afirmações. Não mede MTTD, MTTR, carga cognitiva ou ganhos em resposta a incidentes de TI. |
| P82 | Jiang e Hu (2025) | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | Seção 1, pp. 2–3; seção 2.1, p. 4; seção 2.2, p. 6; conclusão, pp. 12–13 | Discute qualidade e escassez dos dados, alucinações, privacidade, segurança, degradação de modelos e restrições do edge; menciona módulo de segurança e conformidade ética. Não especifica mecanismos verificáveis de accountability, aprovação humana, auditoria, governança de decisões ou controles de risco em um deployment real. |
| P82 | Jiang e Hu (2025) | RQ5 — Research Gaps | Respondida Plenamente | **T (1,0)** | Seção 4.3, p. 12; seção 5, pp. 12–13 | Reconhece expressamente a falta de evidência de superioridade sobre abordagens mais simples e aponta dados sintéticos, aprendizagem federada, otimização edge e padronização de protocolos como direções futuras. As lacunas são claras para manutenção industrial, embora não incluam benchmarks, threat models ou avaliação de carga cognitiva específicos de IR. |
| **P82** | **TOTAL** | **SCORE_RQ** | **4,0 de 5,0** | **T=3; P=2; N=0** | **Consolidação da avaliação documental** | **Alta relevância como referência arquitetural; evidência de benefícios limitada e transferência para IR indireta.** |

### Fundamentação por questão de pesquisa

**RQ1 — Autonomia, características centrais e decisão.** Na seção introdutória (p. 3), os autores caracterizam agentes como entidades capazes de perceber ambientes, decidir e executar ações orientadas a objetivos. Enumeram cinco módulos: planejamento, memória, ação, interação e segurança. A seção 3.3 (p. 7) transforma esses conceitos em uma cadeia de percepção, motor de raciocínio, planejador de ações e aprendizagem. A seção 4.1 (p. 10) descreve a colaboração orientada por mensagens entre agentes de diagnóstico, agendamento, avaliação e simulação. A classificação T corresponde à cobertura explícita das três subdimensões da rubrica, **não** a evidência de autonomia plena em operação real.

**RQ2 — Arquitetura de engenharia.** A Figura 1 e a Tabela 1 (pp. 4–5) organizam ferramentas em níveis L1 (low-code), L2 (API) e L3 (full-code). A Figura 2 (p. 7) situa o núcleo agêntico entre telemetria, digital twin, grafos de conhecimento e sistemas de manutenção; a Figura 4 (p. 9) descreve a divisão edge, fog e cloud. As Figuras 5 e 6 (p. 11) ilustram fluxo de manutenção e orquestração visual no Dify. O artigo também descreve conceitos de LLMOps, RAG e interoperabilidade MCP/A2A (pp. 4–6). Isso sustenta T para especificação de arquitetura, ferramentas e capacidades avançadas no plano conceitual. **Não deve ser confundido com validação de produção.**

**RQ3 — Benefícios e evidências.** O artigo alega que classificadores detectam anomalias com **95% de acurácia** (p. 9) e que o Dify reduz o tempo de construção de aplicativos LLM de semanas para horas (p. 10). Essas são **afirmações dos autores**, não resultados empíricos auditáveis no texto: faltam caracterização dos conjuntos de dados, denominadores, intervalos de confiança, procedimentos, comparação ou apresentação de resultados tabulados. A PoC com dados simulados para rolamentos de turbinas eólicas (pp. 10–11) demonstra integração, não efetividade operacional. O próprio artigo reconhece na conclusão (pp. 12–13) a necessidade de investigar se a arquitetura supera alternativas simples. Assim, não há evidência empírica sólida de benefício; a pontuação P registra apenas alegações qualitativas e a demonstração exploratória.

**RQ4 — Desafios, ética e governança.** A seção 1 (pp. 2–3) menciona integração, disponibilidade/qualidade de dados, lacunas de competências e risco de alucinação; na p. 3, um módulo de segurança aparece como parte da arquitetura conceitual de agentes. A seção 2.1 (p. 4) menciona monitoring de LLMOps e preocupações com ética, latência e drift. Na conclusão (p. 13) constam privacidade na cooperação distribuída entre fábricas e restrições computacionais no edge. Isso não substitui especificações de autorização, supervisão humana, rastreabilidade, auditoria ou responsabilização.

**RQ5 — Lacunas.** A conclusão (pp. 12–13) admite que o trabalho é um *conceptual blueprint* e afirma que os obstáculos práticos e a demonstração de superioridade frente a abordagens simples permanecem abertos. Propõe dados sintéticos baseados em física, aprendizado federado, algoritmos otimizados para edge e protocolos padronizados. Essas linhas futuras são explícitas e suficientemente delimitadas para o contexto do artigo; extrapolações para resposta a incidentes de TI precisam ser tratadas como hipóteses da RSL, e não como resultado dos autores.

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---:|---|
| P82 | Proposta conceitual com PoC exploratória baseada em dados simulados | **Y (1,0)** | **P (0,5)** | **P (0,5)** | **P (0,5)** | **2,5/4,0** | **Média** |

### Justificativas da qualidade

- **QA1 — Y (1,0), objetivos claros:** o resumo (p. 1) e a introdução (pp. 2–4) estabelecem os problemas de integração, dados, dependência de modelos isolados e o propósito de propor uma arquitetura multiagente para PdM. O objetivo e a solução são explícitos.
- **QA2 — P (0,5), metodologia parcialmente replicável:** arquiteturas, componentes, plataformas, fluxo e cenário de rolamentos eólicos constam das seções 3 e 4 (pp. 6–11) e das Figuras 2–6; faltam especificações suficientes dos dados simulados, configuração de modelos, prompts, parâmetros, implementação dos agentes, ambiente de execução e procedimento de avaliação para reprodução científica independente.
- **QA3 — P (0,5), evidências limitadas:** a seção 4.2 (pp. 10–11) apresenta uma demonstração de protótipo com dados simulados, enquadrável como exemplo exploratório/toy example na rubrica fornecida. Não apresenta estudo de campo nem experimento comparativo com métricas verificáveis. Os valores declarados de 95% e semanas/horas **não** bastam para classificar a evidência como sólida.
- **QA4 — P (0,5), conclusões parcialmente coerentes:** a conclusão (pp. 12–13) reconhece explicitamente o caráter conceitual, a dependência de dados e a ausência de prova de superioridade. Entretanto, formula benefícios e avanços em linguagem forte que excede o suporte experimental da PoC. A transparência das limitações é um mérito; a inferência de eficácia permanece insuficiente.

**SCORE_QA = 1,0 + 0,5 + 0,5 + 0,5 = 2,5/4,0. Banda: MÉDIA** (conforme corte 1,5–2,5 definido no roteiro).

## Parecer final do revisor

**Síntese:** O artigo apresenta uma arquitetura multiagente de manutenção preditiva com orquestração por fluxos, raciocínio aumentado por recuperação, bases de conhecimento e gêmeos digitais. Responde especialmente às RQ1, RQ2 e RQ5, com contribuições úteis para conceber um copiloto agêntico que conecte monitoramento, diagnóstico, planejamento de ações e realimentação. Contudo, o domínio empírico é manutenção industrial, e não resposta a incidentes de infraestrutura ou segurança de TI. A demonstração de protótipo não fornece evidência robusta de melhoria em MTTD, MTTR, qualidade decisória ou carga cognitiva, e as questões de governança permanecem pouco operacionalizadas.

**Recomendação: INCLUIR COM RESSALVAS**, **condicionada à confirmação da elegibilidade bibliométrica**. Registrar o estudo como **contribuição arquitetural e conceitual indireta**, não como evidência experimental de benefícios de agentes em resposta a incidentes de TI. Sua inclusão é justificável para discussões de arquitetura, papéis de agentes, RAG, digital twins, interoperabilidade e lacunas de validação. A conclusão sobre eficiência e desempenho não deve ser transferida ao domínio de IR sem novos testes.

### Pendências de verificação externa

1. **Citações [VERIFICAR]:** confirmar se o artigo P82 recebeu pelo menos uma citação, consultando uma base indexadora (por exemplo, Scopus ou outra base adotada no protocolo da RSL), com data da consulta e critério de contagem.
2. **SJR [VERIFICAR]:** confirmar o quartil Q1–Q2 do periódico *Computers* no **SCImago Journal Rank**, observando o ano e a categoria relevantes ao protocolo. O Q1 informado no insumo não constitui confirmação documental.
3. **Qualis [VERIFICAR]:** confirmar o estrato A1–A2 na **Plataforma Sucupira / Qualis CAPES**, registrando a classificação aplicável ao enquadramento da RSL. O A2 e a regra de percentil fornecidos na triagem não são comprovados pelo PDF.

### Observação para consolidação da RSL

A pontuação das RQs identifica **cobertura textual dos temas**, não mede nível de comprovação experimental. A pontuação QA separa essa cobertura de qualidade metodológica. O estudo é especialmente adequado à categoria de **framework conceitual/PoC exploratória**, evitando sua agregação a estudos empíricos que reportem ganhos operacionais mensurados.

---

**Referência do estudo avaliado:** Jiang, W.; Hu, F. *Artificial Intelligence Agent-Enabled Predictive Maintenance: Conceptual Proposal and Basic Framework*. *Computers*, 14, 329, 2025. DOI: 10.3390/computers14080329. Referência extraída da p. 1 do artigo.
