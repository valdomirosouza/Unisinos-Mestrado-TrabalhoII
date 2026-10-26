# PROTOCOLO DE AVALIAÇÃO RSL — CICLO 2 (ESTUDO P55)

---

## 1. ESPECIFICAÇÃO DO PROMPT E DIRETRIZES DA RSL

### PAPEL
Atuação como pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por um professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, seguindo rigorosamente as diretrizes de Kitchenham (2009) no paper/artigo *"Systematic literature reviews in software engineering – A systematic literature review"*. A avaliação de qualidade espelha estritamente a lógica dos critérios DARE (QA1–QA4) descritos naquele trabalho.

### CONTEXTO DA RSL
Esta avaliação integra o artigo **"Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura"**, em seu Ciclo 2 de atualização. O corpus prévio cobre P01–P40 (33 estudos incluídos). Cada novo estudo candidato do ciclo 2 é avaliado individualmente com ID sequencial informado (a partir de P41), de modo que os resultados possam ser anexados diretamente às Tabelas 3, 5 e 7 da RSL existente.

### INSUMOS DO ESTUDO
- **ID**: P55
- **Artigo**: *Telemetry and Agentic AI: Foundations for Optical Network Automation*
- **Arquivo**: `P55_Telemetry_and_Agentic_AI_Foundations_for_Optical_Network_Automation.pdf`
- **Qualis**: A1 (derivado do percentil Scopus 91.0%, regra CAPES 2025-2028)
- **SJR Quartile**: Q1
- **Ressalvas de Triagem**: Aprovado na triagem; estudo de mapeamento/survey

### REGRAS INVIOLÁVEIS (ANTIFABRICAÇÃO)
1. Avaliação EXCLUSIVA do conteúdo presente no PDF anexado, sem uso de suposições ou conhecimento externo não fundamentado.
2. Não fabricação de métricas, números de página, citações, DOI, quartil SJR, estrato Qualis ou contagem de citações.
3. Dados não verificáveis no PDF (quartil SJR, estrato Qualis CAPES, número de citações) são explicitamente marcados como `[VERIFICAR]`, apontando a fonte externa cabível.
4. Toda classificação (T/P/N e Y/P/N) é ancorada em evidência textual concreta (seção, figura, tabela ou página). Sem evidência localizável, a classificação é N.

### CRITÉRIOS DE EXTRAÇÃO E CLASSIFICAÇÃO

#### Questões de Pesquisa (RQs) — Escala T (1.0) / P (0.5) / N (0.0):
- **RQ1 — Context Definitions**: Quais capacidades e níveis de autonomia (planejamento, memória, uso de ferramentas e supervisão humana) caracterizam Agentic AI e como afetam a tomada de decisão em ambientes complexos?
  - *Subdimensões*: a) Autonomy definition; b) Core characteristics; c) Decision-making model.
- **RQ2 — Engineering Architecture**: Quais arquiteturas e mecanismos (orquestração, memória, ferramentas, guardrails, observabilidade) sustentam Agentic AI em produção?
  - *Subdimensões*: a) Architecture type; b) Tools/frameworks; c) Advanced capabilities.
- **RQ3 — Evidence Benefits**: Quais evidências (quanti/quali) reportam benefícios e quais métricas são usadas (tempo de resposta, qualidade de decisão, carga operacional), especialmente em IR?
  - *Subdimensões*: a) Qualitative benefits; b) Quantitative benefits / metrics; c) Evidence level.
- **RQ4 — Challenges & Ethics**: Quais riscos e desafios (segurança, robustez, governança, accountability) limitam o uso responsável em sistemas críticos?
  - *Subdimensões*: a) Technical challenges; b) Ethical/governance challenges; c) Governance mechanisms.
- **RQ5 — Research Gaps**: Quais lacunas e direções futuras (avaliação/benchmarking, threat models, governança, observabilidade, alinhamento) são apontadas?

#### Avaliação de Qualidade (QA / Critérios DARE) — Escala Y (1.0) / P (0.5) / N (0.0):
- **QA1 Objetivos Claros**: O problema (ex.: fadiga de alertas, complexidade de logs) e a solução agêntica são explícitos?
- **QA2 Metodologia Replicável**: Arquitetura, tecnologias, parâmetros e cenário experimental são detalhados o suficiente para replicação?
- **QA3 Base de Evidências Sólidas**: Há validação empírica (experimento, estudo de caso industrial, simulação com métricas)? (Toy example = P; teórico = N).
- **QA4 Conclusões Coerentes**: As conclusões derivam das evidências e as limitações são discutidas?
- **Banda de Qualidade**: Alta $\ge 3.0$ | Média $1.5 \text{ a } 2.5$ | Baixa $< 1.5$.

---

## 2. RELATÓRIO DE EXTRAÇÃO E PARECER TÉCNICO DETALHADO

### ETAPA 0 — EXTRAÇÃO BIBLIOMÉTRICA
- **ID**: P55
- **Título**: Telemetry and Agentic AI: Foundations for Optical Network Automation
- **Autor**: Sergio Cruzes
- **Afiliação**: Optical Network Engineering, Ciena Office Brazil, Ciena Corporation, São Paulo, Brazil
- **Periódico**: IEEE Access (Volume 14, 2026, pp. 8800–8838)
- **Data de Publicação**: Recebido em 11 de dezembro de 2025; aceito em 24 de dezembro de 2025; publicado em 30 de dezembro de 2025; versão corrente em 20 de janeiro de 2026
- **DOI**: 10.1109/ACCESS.2025.3649768
- **Tipo de Estudo**: Survey / Secondary Study (Mapeamento sistemático de literatura e síntese arquitetural)
- **Citações**: `[VERIFICAR]` (Fonte: Scopus / Google Scholar / Web of Science)
- **SJR (Quartil)**: Q1 `[VERIFICAR]` (Fonte: Scimago Journal & Country Rank)
- **Qualis CAPES (Estrato)**: A1 `[VERIFICAR]` (Fonte: Plataforma Sucupira / CAPES 2025–2028)

---

### ETAPA 1 — TRIAGEM DE ELEGIBILIDADE
- **Ano $\ge 2020$**: Aprovado (Ano de publicação: 2026).
- **Publicação $\ne$ NULL**: Aprovado (IEEE Access, periódico internacional indexado).
- **Citações $\ge 1$**: `[VERIFICAR]` (Artigo recentemente publicado no volume de 2026; verificar bases indexadoras).
- **SJR Q1–Q2**: Aprovado (Q1 indicado nos metadados, sujeito a checagem no Scimago).
- **Qualis A1–A2**: Aprovado (A1 indicado nos metadados, percentil Scopus 91.0%, sujeito a confirmação na CAPES).
- **Resultado da Triagem**: **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (aprovado para prosseguimento da extração técnica).

---

### ETAPA 2 — EXTRAÇÃO E CLASSIFICAÇÃO DAS RQs

#### RQ1 — Context Definitions: Respondida Plenamente (T = 1.0)
- **a) Definição de Autonomia**: O artigo adota explicitamente o modelo padronizado pelo TM Forum em seis níveis (Níveis L0 a L5, Tabela 8, Fig. 13, Seção VII-E, pp. 8824–8826), detalhando a transição desde operações manuais com monitoramento ad-hoc (L0), automação assistida por scripts estáticos (L1), automação parcial (L2), automação condicional com loops fechados rotineiros (L3), alta autonomia com orquestração entre domínios e interfaces dirigidas a intenção (L4), até autonomia plena (*zero-touch* com *self-configuration*, *self-healing*, *self-optimization* e *self-learning*, L5).
- **b) Características Centrais dos Agentes**: Estrutura as competências centrais em uma taxonomia formal (Seção VI-G, Fig. 9 e Tabela 7, pp. 8818–8823):
  1. *Role*: Função delimitada e especialização de domínio;
  2. *Perception*: Ingestão contínua de telemetria, logs e eventos de controle;
  3. *Reasoning*: Motor de inferência (baseado em regras, LLMs ou reinforcement learning);
  4. *Memory*: Memória de curto prazo (contexto de incidentes) e longo prazo (histórico de eventos e políticas);
  5. *Action*: Comandos disparados para controladores SDN e orquestradores;
  6. *Learning*: Refinamento via feedback de gêmeos digitais e intervenções humanas.
- **c) Modelo de Tomada de Decisão**: Compara e formaliza na Tabela 6 (p. 8816) a mudança de paradigma da automação clássica orientada por regras fixas (*rule-based*) para o modelo agêntico dirigido por objetivos (*goal-driven*), operando com decomposição hierárquica de metas, raciocínio contextual e adaptação dinâmica.

#### RQ2 — Engineering Architecture: Respondida Plenamente (T = 1.0)
- **a) Tipo de Arquitetura**: Define uma arquitetura de referência em quatro camadas (Seção VI-K, Fig. 9, p. 8820):
  - *Camada 1 (Data Streaming & EDA)*: Barramento orientado a eventos desacoplado (*Event-Driven Architecture*) com Apache Kafka e Spark Streaming;
  - *Camada 2 (Multi-Agent System - MAS)*: Colaboração orquestrada suportando padrões *orchestrator-worker*, hierárquico e *blackboard/shared space* (Fig. 10, p. 8822);
  - *Camada 3 (LLM Integration)*: Raciocínio semântico, tradução de intenções (*intent parsing*) e interface em linguagem natural;
  - *Camada 4 (Control & Validation Infrastructure)*: Validação prévia de segurança em Gêmeos Digitais (DT) e execução em controladores SDN.
- **b) Ferramentas e Frameworks**: Mapeia o ecossistema tecnológico (Seções III, IV e VI): Apache Kafka, Telegraf, InfluxDB, Redis (pub-sub e cache em memória), gRPC com Protocol Buffers, padrões YANG, NETCONF, RESTCONF, T-API, GNPy (simulador de camada física para Gêmeos Digitais), LLaMA2, GPT-4, bibliotecas LangChain e adaptadores LoRA/QLoRA.
- **c) Capacidades Avançadas e Guardrails**: Apresenta salvaguardas detalhadas na Seção VI-E (pp. 8817–8818):
  - *Action Locking* por recurso e arbitragem por prioridade para resolver decisões conflitantes entre agentes;
  - *Timestamps* e limiares de expiração (*staleness thresholds*) para rejeição de ações baseadas em telemetria defasada;
  - Reconciliação periódica entre KPIs simulados e medidos para prevenir a dessincronização do Gêmeo Digital;
  - *Tool Gating*, validação de esquemas e isolamento do LLM (restringido ao planejamento e explicação) para mitigar alucinações;
  - *Cool-down timers* e limites de taxa de ação para barrar falhas em cascata.

#### RQ3 — Evidence Benefits: Parcialmente Respondida (P = 0.5)
- **a) Benefícios Qualitativos**: Destaca a redução drástica do esforço operacional na triagem de incidentes, resolução de anomalias sem interrupção de tráfego, automação de diagnóstico de causa raiz (*Root Cause Analysis* - RCA) e capacidade de explicabilidade em linguagem natural para engenheiros de rede (Seções VI-B, VII-B, pp. 8815, 8819–8822).
- **b) Benefícios Quantitativos e Métricas**: Compila resultados experimentais da literatura (Tabelas 4 e 10, pp. 8810, 8828–8829):
  - Redução de $> 99\%$ no volume de telemetria bruta via compressão/autoencoders (de 541 GB/dia para 0,21 GB/dia);
  - Latência ponta a ponta inferior a 50 ms com taxa de até 4.000 mensagens/segundo em pipelines Kafka;
  - Compressão de 30% a 85% de fluxos de alarmes com tempo de processamento de ~4 s e acurácia de 88% na predição de falhas (AlarmGPT);
  - Acurácia de 96,8% no agrupamento e resolução de 2.500 alarmes ópticos complexos;
  - F1-score de 0,97 na detecção de anomalias em logs reais de campo via LLaMA2 instruído;
  - Redução de latência de decisão entre 3× e 5× em pipelines híbridos distribuídos frente a sistemas centralizados.
- **c) Nível de Evidência**: Trata-se de um estudo secundário de mapeamento e levantamento da literatura (*survey*); o paper não conduz testes ou experimentos de bancada primários próprios com seu próprio framework (p. 8801).

#### RQ4 — Challenges & Ethics: Respondida Plenamente (T = 1.0)
- **a) Desafios Técnicos**: Seção VIII (pp. 8827–8830) analisa exaustivamente a inconsistência de dados (ruído, desbalanceamento, amostragem irregular), interoperabilidade em redes *multi-vendor* decorrente de modelos proprietários fechados, latência de inferência não determinística dos LLMs frente a requisitos de tempo real (sub-segundo) e sobrecarga computacional/custo de tokens em pipelines de alta frequência.
- **b) Desafios Éticos e de Governança**: Discute a opacidade de redes neurais profundas (*black-box models*), responsabilização jurídica/regulatória por decisões automatizadas incorretas, resistência cultural e alinhamento com operadores humanos.
- **c) Mecanismos de Governança**: Recomenda conformidade com o padrão *IEEE Ethically Aligned Design*, implementação obrigatória de supervisão *Human-in-the-Loop* (HITL) para ações de alto risco/impacto, trilhas de auditoria imutáveis (*logs* e *replayability*) e bloqueio rígido de comandos que não tenham sido validados com sucesso pelo Gêmeo Digital.

#### RQ5 — Research Gaps: Respondida Plenamente (T = 1.0)
- Sistematiza na Seção IX e na Tabela 11 (pp. 8830–8833) seis linhas centrais de pesquisa futura:
  1. *Ecossistemas dinâmicos de agentes cooperativos*: Transição para *marketplaces* descentralizados de agentes com computação distribuída borda-nuvem;
  2. *Compressão semântica de telemetria*: Aplicação de arquiteturas preditivas baseadas em embeddings conjuntos (JEPA) para representações latentes ultracompactas de sinais físicos;
  3. *Gêmeos Digitais Distribuídos*: Particionamento de modelos entre borda (avaliação rápida) e núcleo (alta fidelidade física);
  4. *Salvaguardas avançadas com IA Causal*: Uso de grafos de conhecimento e *Causal AI* para raciocínio causa-efeito, associados a DRL com restrições de segurança estritas;
  5. *Padronização de telemetria multi-vendor*: Convergência de esquemas abertos (YANG, T-API, streaming) combinada a técnicas de aprendizado federado (*Federated Learning*);
  6. *Integração com novas malhas ópticas*: Alinhamento de automação agêntica com modulações flexíveis e requisitos de sustentabilidade e eficiência energética.

---

### ETAPA 3 — AVALIAÇÃO DE QUALIDADE (DARE / QA)

- **QA1 (Objetivos Claros)**: **Y = 1.0**. Os desafios operacionais em incidentes e anomalias de redes ópticas e a proposta de uma arquitetura agêntica unificada são claramente justificados e formulados (Seções I e II, pp. 8800–8802).
- **QA2 (Metodologia Replicável)**: **P = 0.5**. O fluxo operacional, as interfaces, os protocolos e as interações entre camadas e ferramentas são minuciosamente descritos (Figs. 1, 9, 10; Seções III, IV e VI). Entretanto, como estudo teórico-conceitual, não disponibiliza repositório de código, dados abertos ou parâmetros de simulação próprios para replicação experimental imediata.
- **QA3 (Base de Evidências Sólidas)**: **N = 0.0**. O próprio artigo declara explicitamente na Seção I: *"No new protocol, algorithm, or control mechanism is proposed. The contribution of this work lies in the synthesized framework..."* (p. 8801). Por se tratar de um estudo estritamente conceitual e de revisão sistemática/survey, sem experimento primário conduzido pelos autores, recebe pontuação 0.0 conforme a rubrica estabelecida para a RSL (estudos teóricos = N).
- **QA4 (Conclusões Coerentes)**: **Y = 1.0**. As conclusões são perfeitamente respaldadas pelo corpo da literatura analisada, debatendo honestamente as limitações inerentes aos agentes LLM (latência, alucinação, custo de inferência) e delineando barreiras técnicas e operacionais reais (Seções VIII e XI, pp. 8827–8834).

**Pontuação QA Final**: $1.0 + 0.5 + 0.0 + 1.0 = \mathbf{2.5 \,/\, 4.0}$  
**Banda de Qualidade**: **Média** ($1.5 \le \text{Score} \le 2.5$).

---

## 3. TABELAS DE SÍNTESE DA RSL

### Tabela A — Extração Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo de Estudo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P55** | IEEE Access | 2026 | [VERIFICAR] | Q1 [VERIFICAR] | A1 [VERIFICAR] | Survey / Mapeamento Sistemático | 10.1109/ACCESS.2025.3649768 |

---

### Tabela B — Classificação das Questões de Pesquisa (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência Textual | Parecer Técnico do Revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **P55** | Cruzes (2026) | RQ1 | Respondida Plenamente | **T** | Seções VI-A, VI-G, VII-E; Tabela 8; Figs. 9 e 13 (pp. 8814–8818, 8824–8826) | Caracteriza os níveis de autonomia L0–L5 baseados no TM Forum e discrimina as capacidades agênticas fundamentais (Role, Perception, Reasoning, Memory, Action, Learning). |
| **P55** | Cruzes (2026) | RQ2 | Respondida Plenamente | **T** | Seções III-B, III-C, VI-A, VI-C, VI-E, VI-H, VI-K; Figs. 1, 9, 10 (pp. 8802–8806, 8814–8820) | Detalha arquitetura de 4 camadas orientada a eventos (EDA via Kafka), padrões MAS (orchestrator-worker, hierárquico, blackboard) e guardrails rigorosos (tool gating, action locking, validação em Gêmeo Digital). |
| **P55** | Cruzes (2026) | RQ3 | Parcialmente Respondida | **P** | Seções VI-B, VII-B; Tabelas 4 e 10 (pp. 8810, 8815, 8819–8822, 8828–8829) | Aborda exaustivamente métricas e ganhos compilados de trabalhos anteriores em resposta a incidentes/alarmes, mas carece de experimento ou validação empírica primária original do autor. |
| **P55** | Cruzes (2026) | RQ4 | Respondida Plenamente | **T** | Seções VI-E, VIII-A a VIII-G (pp. 8817, 8827–8830) | Analisa a fundo vulnerabilidades críticas (alucinações, cascateamento de falhas, latência de tempo real) e propõe governança com HITL, auditoria ponta a ponta e padrões éticos IEEE. |
| **P55** | Cruzes (2026) | RQ5 | Respondida Plenamente | **T** | Seção IX; Tabela 11 (pp. 8830–8832) | Identifica e mapeia seis lacunas estruturantes: ecossistemas agênticos híbridos borda-nuvem, compressão JEPA, gêmeos distribuídos, IA Causal com DRL seguro, modelos multi-vendor e tecidos sustentáveis. |
| **P55** | **SCORE_RQ** | — | — | — | — | **4.5 / 5.0** |

---

### Tabela C — Avaliação de Qualidade DARE (Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 (Objetivos) | QA2 (Metodologia) | QA3 (Evidências) | QA4 (Conclusões) | SCORE_QA | Banda de Qualidade |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P55** | Survey / Mapping Study | 1.0 (Y) | 0.5 (P) | 0.0 (N) | 1.0 (Y) | **2.5 / 4.0** | **Média** |

---

## 4. PARECER FINAL DO REVISOR

### Síntese de Aderência
O estudo **P55** investiga a convergência entre telemetria de alta resolução, processamento em borda, sistemas multiagente orientados a eventos (EDA), Gêmeos Digitais (DT) e Large Language Models para automação, detecção e mitigação de anomalias/incidentes em infraestruturas ópticas complexas. Possui excelente aderência ao escopo da RSL no que tange a taxonomias agênticas, padrões arquiteturais de orquestração, mecanismos de guardrail (rejeição de telemetria desatualizada e validação pré-execução em simulador) e governança em sistemas críticos.

### Recomendação
**INCLUIR COM RESSALVAS**

#### Justificativa:
1. **Mérito Teórico-Arquitetural**: O trabalho fornece uma das formalizações mais claras e estruturadas da literatura recente sobre a divisão de papéis entre telemetria sensória, orquestração multiagente, modelos LLM e validação em Gêmeos Digitais para resolução autônoma de incidentes, cobrindo integralmente quatro das cinco RQs (SCORE_RQ = 4.5/5.0).
2. **Ressalva Metodológica (QA3 = 0.0)**: Por consistir em um artigo de revisão sistemática e síntese conceitual (*survey*), o autor não conduz experimento primário de bancada com protótipo próprio inédito. As evidências quantitativas apresentadas em resposta a incidentes/alarmes decorrem de estudos de terceiros catalogados na Seção VIII e Tabela 10. Assim, sua inclusão é recomendada primariamente para subsidiar as discussões qualitativas, taxonômicas e arquiteturais da RSL.

### Pendências de Verificação Externa
1. **Contagem de Citações**: Checar a contagem atualizada em base de dados internacional (Scopus ou Web of Science) devido à data recente de circulação (2026).
2. **Quartil SJR**: Confirmar o quartil no portal Scimago Journal Rank para o periódico *IEEE Access* (indicado como Q1).
3. **Qualis CAPES**: Verificar na Plataforma Sucupira o enquadramento final de *IEEE Access* segundo o regulamento do quadriênio 2025–2028 (estimado como A1 pelo percentil Scopus 91.0%).