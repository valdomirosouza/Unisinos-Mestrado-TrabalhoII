# Avaliação de Estudo Candidato (RSL - Ciclo 2)

**Estudo**: P82 — *Artificial Intelligence Agent-Enabled Predictive Maintenance: Conceptual Proposal and Basic Framework*  
**Revisor**: Pesquisador em Computação Aplicada (PPGCA / Unisinos)  
**Data da Avaliação**: 2026-10-25  
**Diretrizes Metodológicas**: Kitchenham (2009) / Critérios DARE  

---

## 1. Contexto e Protocolo da RSL

Esta avaliação integra o processo de extração e síntese do artigo *"Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura"*, inserido no ciclo 2 de atualização (estudos P41+). O objetivo é avaliar a elegibilidade, mapear contribuições em relação às cinco Questões de Pesquisa (RQs) e quantificar a qualidade metodológica (critérios QA1–QA4) com base estrita no texto publicado.

---

## 2. Insumos e Metadados do Estudo

- **ID Atribuído**: P82
- **Título**: *Artificial Intelligence Agent-Enabled Predictive Maintenance: Conceptual Proposal and Basic Framework*
- **Autores**: Wenyu Jiang, Fuwen Hu
- **Afiliação**: Brunel London School, North China University of Technology, Beijing, China
- **Periódico**: *Computers* (MDPI), Vol. 14, Artigo 329
- **Datas**: Recebido em 16/07/2025; Revisado em 09/08/2025; Aceito em 12/08/2025; Publicado em 15/08/2025
- **DOI**: `10.3390/computers14080329`
- **Qualis CAPES**: A2 (Derivado do percentil Scopus 86.0%, regra CAPES 2025–2028) — `[VERIFICAR formalmente na Plataforma Sucupira]`
- **SJR Quartile**: Q1 — `[VERIFICAR formalmente no Scimago Journal Rank]`
- **Citações**: `[VERIFICAR nas bases Scopus / Web of Science / Google Scholar]`
- **Tipo de Estudo**: Proposta conceitual e arquitetural com protótipo de prova de conceito (*Proof-of-Concept / Toy Example*)
- **Ressalvas de Triagem**: Aprovado na triagem; proposta conceitual agêntica sem validação empírica em ambiente de produção; domínio centrado em manutenção industrial/preditiva.

---

## 3. Triagem de Elegibilidade (Critérios RSL / PRISMA)

| Critério | Exigência | Situação do Estudo P82 | Status |
| :--- | :--- | :--- | :--- |
| **Ano** | $\ge 2020$ | Publicado em Agosto de 2025 | Atendido |
| **Veículo de Publicação** | Não nulo e identificável | *Computers* (MDPI) | Atendido |
| **Citações** | $\ge 1$ | Publicação de 2025 | Pendente de verificação |
| **SJR** | Q1–Q2 | Indicado como Q1 | Pendente de verificação |
| **Qualis** | A1–A2 | Calculado como A2 (percentil 86.0%) | Pendente de verificação |

**Veredito da Triagem**: **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (requer conferência da contagem de citações e homologação cadastral no Qualis Sucupira e SJR). Seguindo o protocolo Kitchenham, procede-se à extração completa de dados.

---

## 4. Extração e Classificação por Questões de Pesquisa (RQs)

### RQ1 — Context Definitions
> *Quais capacidades e níveis de autonomia (planejamento, memória, uso de ferramentas e supervisão humana) caracterizam Agentic AI e como afetam a tomada de decisão em ambientes complexos?*
> *(a) Definição de autonomia; (b) Características centrais; (c) Modelo de tomada de decisão.*

- **Classificação**: **Respondida Plenamente (T = 1.0)**
- **Evidências no Texto**:
  - *a) Autonomia*: Define agentes de IA como entidades autônomas capazes de compreender e responder a entradas humanas, perceber ambientes, tomar decisões e executar ações em domínios físicos, virtuais ou mistos para atingir metas predefinidas. Destaca o salto evolutivo da automação simples de tarefas para resolução proativa de problemas e tomada estratégica de decisão (Seção 1, p. 1; Seção 1.2, p. 3).
  - *b) Características centrais*: Decomposição de tarefas em 5 módulos sinérgicos: planejamento (*planning*), memória de curto e longo prazo (*memory*), ação via ferramentas/APIs (*action*), interação colaborativa humano-máquina/ambiente (*interaction*) e segurança/governança ética (*security*) (Seção 1.2, p. 3; Seção 2.2, p. 6).
  - *c) Tomada de decisão*: Modelo híbrido/neurosimbólico composto por LLMs de raciocínio profundo (*DeepSeek*), base de conhecimento/RAG (*RAGFlow*), verificação contrafactual via simulação de Gêmeo Digital (*Digital Twin*) e consolidação em matriz de decisão ponderada por incerteza (*Uncertainty-Weighted Decision*) (Seção 3.2–3.3, p. 6–8, Figuras 2 e 3).

---

### RQ2 — Engineering Architecture
> *Quais arquiteturas e mecanismos (orquestração, memória, ferramentas, guardrails, observabilidade) sustentam Agentic AI em produção?*
> *(a) Tipo de arquitetura; (b) Ferramentas/frameworks; (c) Capacidades avançadas.*

- **Classificação**: **Respondida Plenamente (T = 1.0)**
- **Evidências no Texto**:
  - *a) Tipo de arquitetura*: Arquitetura hierárquica multi-tier distribuída em três camadas (*Edge-Fog-Cloud*). O Edge executa filtragem de ruído, compressão e FFT em tempo real; o Fog gerencia detecção de anomalias zonal com orquestração local (Dify/AutoGen); e o Cloud concentra diagnósticos complexos com LLMs, planejamento global e simulações pesadas (Seção 4.1, p. 8–10, Figura 4).
  - *b) Ferramentas e frameworks*: Pirâmide de engenharia em 3 níveis: L1 Low-Code (Dify, Coze, Bubble), L2 API-Driven (OpenAI Assistants, Claude Kit, LangSmith) e L3 Full-Code (LangChain, AutoGen, Haystack, CrewAI, LangGraph) (Seção 2.1–2.2, p. 4–6, Tabela 1). O protótipo específico integra Dify, RAGFlow, InfluxDB e modelos DeepSeek (Seção 4.2, p. 10–11).
  - *c) Capacidades avançadas*: Pipeline de LLMOps cobrindo monitoramento de drift, rastreamento de custo/latência (LangSmith/AgentOps), controle de fluxo estruturado em RAG (RAGFlow) e interoperabilidade padronizada via protocolos de contexto (*Model Context Protocol* - MCP) e colaboração inter-agente (*Agent-to-Agent* - A2A) (Seção 2.1–2.2, p. 5–6; Seção 4.1, p. 9–10).

---

### RQ3 — Evidence Benefits
> *Quais evidências (quanti/quali) reportam benefícios e quais métricas são usadas (tempo de resposta, qualidade de decisão, carga operacional), especialmente em IR?*
> *(a) Benefícios qualitativos; (b) Benefícios quantitativos / métricas; (c) Nível de evidência.*

- **Classificação**: **Parcialmente Respondida (P = 0.5)**
- **Evidências no Texto**:
  - *a) Benefícios qualitativos*: Superação dos silos operacionais, transição de estratégias reativas para manutenção preditiva/prescritiva em malha fechada, redução da fadiga operacional e sobremanutenção, além de alta explicabilidade nos relatórios diagnósticos gerados (Seção 1, p. 1–2; Seção 4.3, p. 12, Tabela 2).
  - *b) Benefícios quantitativos / métricas*: Menciona genericamente 95% de precisão nos classificadores de anomalia na camada Fog (p. 9) e redução do tempo de desenvolvimento de aplicações agênticas de "semanas para horas" com Dify (p. 10). Contudo, inexistem medições formais de MTTD (*Mean Time to Detect*), MTTR (*Mean Time to Repair*), precisão diagnóstica comparativa ou ganho de disponibilidade sobre sistemas reais (Seção 4.2, p. 10–11).
  - *c) Nível de evidência*: Nível baixo a intermediário — Prova de Conceito básica (*toy example* / protótipo de bancada) baseada em simulação sintética de rolamentos de turbina eólica, sem validação empírica em planta produtiva real (Seção 4.2, p. 10–11; Seção 5, p. 12–13).

---

### RQ4 — Challenges & Ethics
> *Quais riscos e desafios (segurança, robustez, governança, accountability) limitam o uso responsável em sistemas críticos?*
> *(a) Desafios técnicos; (b) Desafios éticos/governança; (c) Mecanismos de governança.*

- **Classificação**: **Respondida Plenamente (T = 1.0)**
- **Evidências no Texto**:
  - *a) Desafios técnicos*: Alucinações de modelos generativos (intoleráveis em cenários de missão crítica), degradação e deriva de modelos decorrentes de envelhecimento de componentes mecânicos, escassez severa de dados históricos de falhas catastróficas raras e restrições de latência/largura de banda em borda (Seção 1, p. 2; Seção 1.1, p. 3; Seção 4.1, p. 8–9; Seção 5, p. 13).
  - *b) Desafios éticos e governança*: Questões de privacidade de dados em redes industriais distribuídas multi-fábrica, governança de decisões autônomas, confiabilidade de modelos de caixa preta e centralidade humana (*Human-in-the-Loop* alinhado aos princípios da Indústria 5.0) (Seção 1, p. 2; Seção 2.1, p. 4; Seção 5, p. 13).
  - *c) Mecanismos de governança*: Emprego de restrições de IA Constitucional (*Constitutional AI constraints*), validação e pré-teste contrafactual de planos de manutenção no Gêmeo Digital antes do despacho para sistemas CMMS/ERP, além de controle de acesso corporativo por função (RBAC/SSO) (Seção 2.1, p. 5; Seção 3.2, p. 6; Seção 4.1, p. 10).

---

### RQ5 — Research Gaps
> *Quais lacunas e direções futuras (avaliação/benchmarking, threat models, governança, observabilidade, alinhamento) são apontadas?*

- **Classificação**: **Respondida Plenamente (T = 1.0)**
- **Evidências no Texto**:
  - O próprio trabalho estabelece explicitamente suas limitações nas conclusões (p. 12–13): falta de evidência empírica comprovando que a arquitetura agêntica complexa supera soluções tradicionais mais simples; gargalos de otimização para execução de modelos em dispositivos de borda com baixa capacidade computacional; necessidade de mecanismos de geração de dados sintéticos fisicamente informados; implementação de arquiteturas de Aprendizado Federado (*Federated Learning*) para viabilizar colaboração multi-fábrica sem violar requisitos estritos de privacidade industrial; e consolidação de protocolos universais de comunicação multiagente (MCP e A2A) (Seção 5, p. 12–13).

---

## 5. Avaliação de Qualidade Metodológica (Critérios DARE / Kitchenham)

- **QA1 (Objetivos Claros)**: **Y (1.0)**  
  O trabalho explicita o problema industrial (falhas de integração, silos de dados, modelos estáticos e inacessibilidade da manutenção preditiva clássica) e propõe formalmente uma arquitetura de referência baseada em agentes autônomos, BaaS e LLMOps (Seção 1, p. 1–3).
- **QA2 (Metodologia Replicável)**: **P (0.5)**  
  A arquitetura conceitual e os fluxos de trabalho no Dify são ilustrados detalhadamente (Figuras 5 e 6). Todavia, não há repositório aberto com o código das integrações em Python, esquemas de banco de dados, prompts de raciocínio ou parâmetros de acoplamento do Digital Twin, impossibilitando a replicação exata.
- **QA3 (Base de Evidências Sólidas)**: **P (0.5)**  
  A validação apresentada restringe-se a uma prova de conceito ilustrativa com dados simulados de rolamentos de turbina eólica (*toy example*), sem experimentos estatísticos, dados reais de campo ou comparações controladas com baselines convencionais (Seção 4.2 e 5).
- **QA4 (Conclusões Coerentes)**: **Y (1.0)**  
  As conclusões derivam com sobriedade da proposta. Os autores reconhecem expressamente que o trabalho constitui um *blueprint* conceitual de alto nível e que estudos futuros precisam demonstrar se a complexidade agregada pelo ecossistema agêntico de fato supera abordagens convencionais (Seção 5, p. 12–13).

---

## 6. Tabelas Consolidadas da RSL

### Tabela A — Extração Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conferência | Ano | Citações | SJR (Quartil) | Qualis CAPES | Tipo de Estudo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P82** | *Computers* (MDPI) | 2025 | `[VERIFICAR]` | Q1 `[VERIFICAR]` | A2 `[VERIFICAR]` | Proposta Conceitual / Protótipo PoC | `10.3390/computers14080329` |

---

### Tabela B — Classificação das Questões de Pesquisa (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência Principal | Parecer Técnico do Revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **P82** | Jiang & Hu (2025) | RQ1 | Respondida Plenamente | **T** | Seções 1, 1.2, 2.2, 3.2–3.3 | Conceitua autonomia, capacidades centrais (percepção, memória, ação, planejamento, segurança) e decisão híbrida (LMs + Digital Twin + Knowledge Graphs). |
| **P82** | Jiang & Hu (2025) | RQ2 | Respondida Plenamente | **T** | Seções 2.1–2.2, 4.1–4.2, Tabs. 1–2 | Detalha arquitetura Edge-Fog-Cloud em 3 camadas, taxonomia L1–L3 de plataformas e integração de Dify, RAGFlow, DeepSeek e protocolos MCP/A2A. |
| **P82** | Jiang & Hu (2025) | RQ3 | Parcialmente Respondida | **P** | Seções 1, 4.1–4.2, 5 | Foco em benefícios qualitativos; evidência experimental baseada exclusivamente em dados simulados de bancada (*toy example*), sem métricas de MTTD/MTTR em produção. |
| **P82** | Jiang & Hu (2025) | RQ4 | Respondida Plenamente | **T** | Seções 1, 2.1, 3.2, 5 | Mapeia alucinações, drift temporal, desafios de privacidade em colaboração multi-fábrica e uso de simulação prévia em Gêmeo Digital como salvaguarda operacional. |
| **P82** | Jiang & Hu (2025) | RQ5 | Respondida Plenamente | **T** | Seção 5 (Conclusões) | Aponta lacunas de eficiência computacional em borda, Federated Learning com privacidade e a necessidade premente de validações empíricas comparativas rigorosas. |
| **TOTAL**| | | | **4.5 / 5.0** | | |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 (Objetivos) | QA2 (Metodologia) | QA3 (Evidências) | QA4 (Conclusões) | SCORE_QA | Banda de Qualidade |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P82** | Proposta Conceitual / Protótipo PoC | **1.0** (Y) | **0.5** (P) | **0.5** (P) | **1.0** (Y) | **3.0 / 4.0** | **Alta** ($\ge 3.0$) |

---

## 7. Parecer Final do Revisor

### Síntese Crítica
O artigo P82 introduz um framework de referência abrangente e inovador para a integração de agentes de inteligência artificial em manutenção preditiva e resposta a falhas industriais. A contribuição técnica central reside na estruturação de uma arquitetura hierárquica em três camadas (*Edge-Fog-Cloud*) articulada a um fluxo de trabalho com quatro agentes especializados: detecção de anomalias, classificação por RAG, raciocínio diagnóstico e simulação contrafactual por Gêmeo Digital (*Digital Twin*). A organização das plataformas agênticas em pirâmide de maturidade (L1 a L3) e o uso de protocolos abertos (MCP e A2A) oferecem padrões conceituais de engenharia altamente transferíveis para sistemas de *Incident Response* em Engenharia de Software e infraestrutura de TI / SRE.

### Recomendação Final
**INCLUIR COM RESSALVAS**

- **Justificativa**: O estudo obtém pontuação elevada nas RQs conceituais e arquiteturais ($\text{SCORE\_RQ} = 4.5/5.0$) e atinge a banda de qualidade metodológica **Alta** ($\text{SCORE\_QA} = 3.0/4.0$). No entanto, as evidências de benefício (RQ3) derivam exclusivamente de um protótipo ilustrativo com dados sintéticos (*toy example*). O artigo deve, portanto, ser categorizado e sintetizado na RSL como um modelo conceitual/arquitetural de referência, ressalvando-se categoricamente a ausência de validação empírica de desempenho em ambiente industrial ou operacional real.

### Pendências de Verificação Externa
1. **Citações**: Consultar a contagem exata de citações do artigo nas bases indexadoras Scopus e Web of Science.
2. **Homologação Qualis / SJR**: Confirmar a classificação oficial do periódico *Computers* (MDPI, ISSN 2073-431X) no Qualis Sucupira (quadriênio 2025–2028) e no ranking oficial do SCImago Journal Rank.