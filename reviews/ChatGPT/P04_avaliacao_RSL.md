# Avaliação do artigo P04 — Corpus fundacional da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P04  
**Título:** *LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead*  
**Autores:** Junda He, Christoph Treude e David Lo  
**Natureza:** avaliação retroativa de estudo fundacional, sem reabrir a decisão histórica de inclusão.

## Escopo e método da avaliação

Esta ficha aplica a rubrica do arquivo `prompt-P04.md`, fundamentando as classificações somente no PDF fornecido. As referências a páginas são às páginas numeradas do artigo (124:1 a 124:30). Não se confundem resultados dos estudos primários sintetizados na revisão com resultados experimentais produzidos pelos próprios autores. Indicadores bibliométricos não verificáveis no PDF permanecem identificados como **[VERIFICAR]**, ainda que o protocolo de entrada registre classificações previamente conferidas.

## Etapa 0 — Tabela A: extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P04 | *ACM Transactions on Software Engineering and Methodology*, v. 34, n. 5, art. 124 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão sistemática da literatura com dois estudos de caso exploratórios | https://doi.org/10.1145/3712003 |

**Evidência:** referência bibliográfica e metadados na p. 1; descrição da revisão e dos estudos de caso no resumo (p. 1), Introdução (pp. 2–3), seção 3 (pp. 4–6) e seção 4 (pp. 10–12).

**Registro de entrada, sem validação independente no PDF:** `sjr_quartile=Q1`; `qualis=A2` (informação do protocolo, associada a `papers.csv`, 27/07/2026). Estes valores não são transferidos para a tabela de dados *extraídos do PDF* como se tivessem sido verificados nesta avaliação.

## Etapa 1 — Triagem de elegibilidade

| Critério | Verificação no PDF | Resultado |
|---|---|---|
| Publicação em 2020 ou depois | 2025, p. 1 | Atende |
| Veículo de publicação identificado | *ACM Transactions on Software Engineering and Methodology*, p. 1 | Atende |
| Pelo menos uma citação | Contagem de citações do próprio artigo não informada no PDF | [VERIFICAR] |
| SJR Q1 ou Q2 | Não verificável no PDF; protocolo informa Q1 | [VERIFICAR] |
| Qualis A1 ou A2 | Não verificável no PDF; protocolo informa A2 | [VERIFICAR] |

**Resultado da triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis)**. O artigo já integra o corpus fundacional herdado do Trabalho I; esta checagem não implica exclusão automática nem reabertura da inclusão.

## Etapa 2 — Tabela B: aderência às questões de pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P04 | He, Treude e Lo (2025) | RQ1 — Context Definitions | Respondida Plenamente | T (1,0) | §§ 2.1–2.3, pp. 3–4; § 5.2.1, pp. 17–18 | Define autonomia, percepção, objetivos, memória, ação, reflexão, coordenação e decisão colaborativa; discute intervenção humana. |
| P04 | He, Treude e Lo (2025) | RQ2 — Engineering Architecture | Respondida Plenamente | T (1,0) | § 2.3, p. 4; §§ 3.2–3.5, pp. 6–10; §§ 5.2.3–5.2.6, pp. 19–21 | Caracteriza orquestração, modelos de coordenação/comunicação, papéis especializados, frameworks, ferramentas, memória, adaptação e monitoramento como direção de pesquisa. Não oferece arquitetura de produção SRE integrada e validada. |
| P04 | He, Treude e Lo (2025) | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | §§ 4–4.2, pp. 10–12; § 5.2.2, pp. 18–19 | Há resultados qualitativos e métricas quantitativas de dois protótipos, mas não demonstra efeito sobre MTTD/MTTR, qualidade de decisões em incidentes ou carga cognitiva operacional. |
| P04 | He, Treude e Lo (2025) | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | §§ 5.1.1, 5.2.1, 5.2.3–5.2.6, pp. 13–21 | Identifica limitações técnicas e questões de privacidade, governança e supervisão humana; propõe controle de acesso, privacidade por desenho e proteção de dados. Medidas são predominantemente propostas, não mecanismos empiricamente validados no estudo. |
| P04 | He, Treude e Lo (2025) | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | § 5, pp. 12–21, especialmente § 5.2.2, pp. 18–19; § 7, pp. 22–23 | Apresenta agenda explícita para especialização, cooperação humano-agente, benchmarks colaborativos, escalabilidade, adaptação dinâmica e privacidade. |
| **P04** | | **SCORE_RQ** | | **4,5 / 5,0** | | **Elevada pertinência arquitetural e conceitual, evidência operacional indireta.** |

### Fundamentação detalhada por RQ

**RQ1 — T (1,0).** A seção 2.1 define explicitamente agente autônomo por autonomia, percepção, orientação a objetivos, capacidade social e aprendizagem (p. 3). A seção 2.2 representa o agente LLM pela tupla **⟨L, O, M, P, A, R⟩**, envolvendo modelo, objetivo, memória, percepção, ação e reflexão (pp. 3–4). A seção 2.3 descreve modelos cooperativos, competitivos e hierárquicos, centralização/descentralização e planejamento coordenado (p. 4). A seção 5.2.1 examina colaboração humano-agente e pontos de intervenção (pp. 17–18). **Subdimensões:** (a) definição de autonomia: presente; (b) características centrais: presente; (c) modelo de tomada de decisão: presente.

**RQ2 — T (1,0).** A arquitetura descrita combina uma **plataforma de orquestração** com **agentes baseados em LLM**, incluindo coordenação, comunicação, planejamento e aprendizagem (§ 2.3, p. 4). A revisão apresenta frameworks como PairCoder, MetaGPT, ChatDev, AgileCoder, RCAgent e AgentFL, além de agentes que interagem com compiladores, testes, ferramentas de depuração, análise estática e bases de conhecimento (§§ 3.2–3.5, pp. 6–10). A agenda aborda memória, alocação de recursos, reconfiguração dinâmica de papéis e monitoramento de progresso (§ 5.2.5, pp. 20–21). **Subdimensões:** (a) tipos arquiteturais: presente; (b) ferramentas e frameworks: presente; (c) capacidades avançadas: presente. **Limite de transferência:** não há demonstração de *guardrails* completos nem de observabilidade de produção baseada em logs, métricas e traces aplicada a um copilot SRE.

**RQ3 — P (0,5).** Os autores executam dois estudos de caso com ChatDev e GPT-3.5-turbo, temperatura **0,2**, para geração dos jogos Snake e Tetris (§ 4, p. 10). Snake exigiu duas tentativas para sucesso, com **76 segundos** e **US$ 0,019** por tentativa, em média (§ 4.1, p. 11). Tetris chegou a uma versão jogável na décima tentativa, mas sem remover linhas completas, com **70 segundos** e **US$ 0,020** por tentativa, em média (§ 4.2, pp. 11–12). Isso demonstra capacidade e limitações em prototipagem simples, não resultados de resposta a incidentes. **Subdimensões:** (a) benefícios qualitativos: presente; (b) benefícios quantitativos/métricas: presente, mas só para protótipos; (c) nível de evidência: estudos de caso exploratórios/toy examples, não experimentos industriais de IR. Não converter os tempos de geração em MTTD/MTTR.

**RQ4 — T (1,0).** O artigo discute falhas de raciocínio, insuficiência de conhecimento especializado e dificuldades para ampliar os sistemas (§§ 5.1.1 e 5.2.3, pp. 13 e 19–20). A supervisão humana, inclusive em decisões éticas e ambiguidades, é discutida em § 5.2.1 (pp. 17–18). A seção 5.2.6 (p. 21) aborda silos de dados, conformidade, privacidade, transparência, controle fino de acesso e propostas como RBAC/ABAC, *differential privacy*, computação multipartidária segura, aprendizado federado e criptografia homomórfica. **Subdimensões:** (a) desafios técnicos: presente; (b) governança/ética: presente; (c) mecanismos: presente como propostas. Não confundir recomendações de governança com evidência de implementação eficaz em produção.

**RQ5 — T (1,0).** A seção 5 e a Figura 4 estruturam a agenda em **(1) aprimorar capacidades individuais** e **(2) otimizar sinergia entre agentes** (pp. 12–13). A seção 5.2.2 (pp. 18–19) pede benchmarks para colaboração, delegação, resolução de conflitos, revisão cruzada e esclarecimento de ambiguidades, e propõe métricas de comunicação e sucesso do projeto. Outras lacunas incluem intervenção humana, escalabilidade, adaptação, privacidade e segurança (§§ 5.2.1–5.2.6). A falta de avaliação de MTTD/MTTR e de carga cognitiva em IR é **lacuna inferida na aplicação ao escopo desta RSL**, não uma lacuna explicitamente testada pelos autores.

## Etapa 3 — Tabela C: qualidade DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P04 | Revisão sistemática + dois estudos de caso exploratórios | Y (1,0) | P (0,5) | P (0,5) | Y (1,0) | **3,0 / 4,0** | **Alta** |

### Justificativas de qualidade

**QA1 — Y (1,0), objetivos claros.** O resumo e a Introdução (pp. 1–3) delimitam o problema dos sistemas multiagentes LLM na Engenharia de Software e apresentam três contribuições: revisão de estudos primários, dois casos ilustrativos e agenda de pesquisa. O foco não é fadiga de alertas nem resposta a incidentes SRE, mas o objetivo do próprio estudo é explícito.

**QA2 — P (0,5), replicabilidade parcial.** A estratégia da revisão especifica DBLP, grupos de palavras-chave, combinação com operadores, critérios de exclusão, revisão de texto completo, *snowballing*, data de busca (**14/11/2024**) e corpus final de **71 estudos** (41 na seleção inicial mais 30 via snowballing, pp. 3, 5–6). Os casos apresentam ChatDev, modelo GPT-3.5-turbo, temperatura, prompts e tentativas (§ 4, pp. 10–12). Contudo, não há protocolo experimental suficientemente completo para repetir controladamente todos os resultados (por exemplo, configuração integral de execução e controle de variabilidade). A classificação considera conjuntamente revisão e estudos de caso, segundo a rubrica fornecida.

**QA3 — P (0,5), base empírica limitada.** A revisão compila **71 estudos primários**, mas a validação própria consiste em **dois casos demonstrativos** de desenvolvimento de jogos (§ 4, pp. 10–12). Pela regra do protocolo, exemplos simplificados (*toy examples*) recebem **P**, não **Y**. Não há avaliação em operação industrial de incidentes.

**QA4 — Y (1,0), coerência e limitações.** Os resultados sustentam a conclusão com ressalvas de que sistemas multiagentes são promissores, porém ainda limitados em tarefas mais complexas (§ 4.2, p. 12). A seção **6.2 — Threat to Validity** (p. 22) explicita o risco de omissão de estudos na busca e descreve mitigação por busca DBLP e *snowballing*. A discussão de Tetris reconhece uma funcionalidade central ausente, evitando apresentar sucesso integral.

## Parecer final do revisor

**Síntese.** O P04 é um estudo fundacional de forte utilidade para definir autonomia e explicar arquiteturas multiagentes com LLM, orquestração, colaboração, especialização e realimentação. Conecta Engenharia de Software e ambientes em nuvem ao citar agentes para análise de causa raiz e diagnóstico em logs (RCAgent, § 3.3, p. 8), mas não apresenta experimento próprio sobre incidentes operacionais. Seus resultados originais de tempo e custo dizem respeito a jogos gerados com ChatDev, sem demonstrar redução de MTTD, MTTR ou carga cognitiva. A agenda de governança, avaliação colaborativa e supervisão humana fundamenta o desenho e futuras avaliações do Copiloto Agêntico.

**Recomendação: INCLUIR COM RESSALVAS.** Manter no corpus fundacional herdado, para síntese conceitual, arquitetural e de lacunas. Ao analisar benefícios de *incident response*, evitar contabilizar seus experimentos como validação operacional; separar métricas de prototipagem de métricas de confiabilidade/SRE. A qualidade metodológica recebe **3,0/4,0 (Alta)** e a aderência global, **4,5/5,0**, com evidência direta insuficiente para RQ3 no contexto específico de IR.

**Pendências de verificação externa:**

1. **Citações [VERIFICAR]:** conferir número de citações em base indexadora com data de consulta registrada.
2. **SJR [VERIFICAR]:** conferir quartil e período no *SCImago Journal Rank*. O protocolo informa Q1, não comprovado pelo PDF.
3. **Qualis [VERIFICAR]:** conferir estrato e quadriênio na *Plataforma Sucupira / Qualis CAPES*. O protocolo informa A2, não comprovado pelo PDF.

**Nota de rastreabilidade:** toda pontuação e resultado científico acima decorrem do PDF anexado, salvo as informações explicitamente identificadas como valores prévios do protocolo ou inferências de transferência para o objetivo da RSL. Não foi realizada verificação bibliométrica externa.
