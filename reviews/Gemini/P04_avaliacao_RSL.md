# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P04
- **Arquivo PDF avaliado:** `P04-A2-LLM-Based Multi-Agent Systems for Software Engineering Literature Review Vision and the Road Ahead.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A2
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O estudo investiga de forma sistemática os *LLM-Based Multi-Agent (LMA) Systems* aplicados à Engenharia de Software (*Software Engineering 2.0*), formalizando a definição de agentes autônomos baseados em LLMs e plataformas de orquestração multiagente, mapeando 71 estudos primários ao longo do ciclo de vida de software — incluindo detecção de vulnerabilidades, localização de falhas (*RCAgent*, *AgentFL*), depuração automatizada e reparo de incidentes/bugs —, executando dois estudos de caso empíricos com o framework *ChatDev* e propondo uma agenda de pesquisa em duas fases.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em maio de 2025 no periódico *ACM Transactions on Software Engineering and Methodology (TOSEM)*, Volume 34, Número 5, Artigo 124 (Recebido em 2 de abril de 2024; Revisado em 16 de dezembro de 2024; Aceito em 18 de dezembro de 2024; Publicado em maio de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão sistemática publicado em periódico de excelência revisado por pares (*ACM TOSEM*), classificado como **Qualis A2** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 30 páginas em inglês com protocolo sistemático completo e estudos de caso empíricos.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Formalização matemática de Agentes Autônomos Baseados em LLMs (Seção 2.1–2.2, pp. 3–4):** Define formalmente um agente autônomo baseado em LLM pela sêxtupla $\langle L, O, M, P, A, R \rangle$, na qual $L$ representa o *LLM* (núcleo cognitivo), $O$ o *Objective* (meta estratégica que guia o planejamento e a decomposição de tarefas), $M$ a *Memory* (estados históricos, estado atual e *feedback* externo), $P$ a *Perception* (interpretação multimodal do ambiente), $A$ a *Action* (uso de ferramentas externas e comunicação inter-agentes) e $R$ o *Rethink* (processo reflexivo pós-ação que avalia resultados e orienta ações subsequentes).
  - **Transição de agentes singulares e *Mixture of Experts (MoE)* para Sistemas Multiagentes (LMA) rumo à *Software Engineering 2.0* (Seção 1, p. 2; Seção 6.1, p. 22):** Justifica a transição de agentes LLM isolados para sistemas multiagentes colaborativos (*LMA systems*) com base em três propriedades emergentes: (1) *Autonomous Problem-Solving*, (2) *Robustness and Fault Tolerance* (mitigação de alucinações via debate e validação cruzada entre agentes) e (3) *Scalability to Complex Systems*. Na Seção 6.1 (p. 22), contrasta formalmente o paradigma *MoE* (roteamento interno estático sem comunicação entre especialistas) com sistemas *LMA* (fluxos colaborativos com comunicação ativa, integração de ferramentas externas como compiladores/analisadores estáticos e intervenção contínua *human-in-the-loop*).
- **Justificativa:** Oferece formalização conceitual rigorosa ($\langle L, O, M, P, A, R \rangle$) e fundamenta claramente a evolução de LLMs singulares para sistemas multiagentes autônomos com colaboração humana.

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Arquitetura de Plataformas de Orquestração e Grafo de Interação (Seção 2.3, p. 4):** Modela o sistema multiagente como um grafo $G(V, E)$ composto por dois subsistemas: (i) **Orchestration Platform**, caracterizada por *Coordination Models* (cooperativo, competitivo, hierárquico ou misto), *Communication Mechanisms* (centralizado, descentralizado ou hierárquico, trocando trechos de código, *commits*, relatórios de bugs e relatórios de vulnerabilidades) e *Planning and Learning Styles* (*Centralized Planning / Decentralized Execution* vs. *Decentralized Planning / Decentralized Execution*); e (ii) **LLM-Based Agents**, classificados como *Predefined vs. Dynamically Generated* e *Homogeneous vs. Heterogeneous*.
  - **Mapeamento arquitetural ao longo do SDLC e modelos de processo (Seção 3.1–3.5, Fig. 1, pp. 6–10):** Analisa arquiteturas de especialização de papéis (*Orchestrator, Programmer, Reviewer, Tester, Information Retriever*) e votação por consenso (*Agent Forest*, p. 7), além de classificar sistemas *end-to-end* segundo modelos **Waterfall** (*MetaGPT*, *ChatDev*, *CodePori*, *CODES*, *L2MAC*, Fig. 1, p. 9), **Agile** (*AgileCoder*, *AgileGen*, pp. 9–10), **Dynamic Process Generation** (*Think-on-Process — ToP*, *MegaAgent*, p. 10) e **Experiential Co-Learning** (p. 10).
  - **Arquiteturas para QA, Detecção de Vulnerabilidades, Localização de Causa Raiz e Depuração (Seção 3.3–3.4, pp. 7–8):** Detalha sistemas multiagentes diretamente ligados à confiabilidade e diagnóstico de falhas: *PentestGPT* (teste de penetração, p. 7), *GPTLens* (auditores + agente crítico para vulnerabilidades em *smart contracts*, p. 7), *MuCoLD* (consenso multi-papel para vulnerabilidades, p. 7), *ICAA* (agente de relatório + *False-Positive Pruner* com ferramentas de análise estática, p. 8), **RCAgent** (análise de causa raiz em nuvem coletando logs e dados de sistema, p. 8), **AgentFL** (localização de falhas em três fases: *Comprehension*, *Navigation* e *Confirmation Agent*, p. 8), *MASAI*, *MarsCode*, *AutoSD*, *FixAgent*, *AutoCodeRover*, *SpecRover*, *ACFIX* (reparo de vulnerabilidades RBAC), *SWE-Search* (MCTS + debate) e *CodeAgent* (p. 8).
- **Justificativa:** Descreve em profundidade os mecanismos de coordenação, topologias de comunicação e dezenas de frameworks multiagentes concretos para engenharia de software, detecção de vulnerabilidades, *root cause analysis* e reparo automatizado.

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Dois Estudos de Caso Empíricos com o framework *ChatDev* (Seção 4, Figs. 2–3, pp. 10–12):** Os autores executam experimentos práticos utilizando o *ChatDev* (estruturado nas fases de *designing, coding, testing* com os papéis *CEO, CTO, programmer, reviewer, tester* sobre o modelo `GPT-3.5-turbo` com `temperature = 0.2`):
    1. **Estudo de Caso 1 — Jogo *Snake* (Seção 4.1, Fig. 2, p. 11):** A primeira tentativa falhou; na **2ª tentativa**, o *ChatDev* gerou uma versão totalmente funcional e aderente a todos os requisitos do *prompt*, acompanhada de manual de usuário, com tempo médio de execução de **`76 segundos`** e custo médio de **`US$ 0,019`** por tentativa.
    2. **Estudo de Caso 2 — Jogo *Tetris* (Seção 4.2, Fig. 3, pp. 11–12):** O *ChatDev* falhou em produzir jogabilidade funcional nas **primeiras 9 tentativas**; apenas na **10ª tentativa** gerou um jogo executável, mas ainda **sem a funcionalidade central de remover linhas completas**, com tempo médio de **`70 segundos`** e custo de **`US$ 0,020`** por execução.
  - **Limitação:** Os estudos de caso demonstram empiricamente tempo, custo e taxa de sucesso/falha em geração de software de complexidade baixa a moderada, mas o artigo não reporta tabelas quantitativas comparativas de métricas operacionais de resposta a incidentes (como *MTTR* ou precisão de diagnóstico em produção).
- **Justificativa:** Contém evidência experimental primária própria (tempo em segundos, custo em dólares e número de tentativas até convergência no *ChatDev*), porém restrita à geração de artefatos de software simples e sem métricas quantitativas de operações/incidentes (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Limitações técnicas e de escalabilidade (Seção 4.2, p. 12; Seção 5.1.1, p. 13; Seção 5.2.3, p. 19; Seção 5.2.5, p. 21):** Evidencia empiricamente a falha de raciocínio lógico em tarefas complexas (*Tetris*), aponta deficiências de LLMs generalistas na detecção e reparo de vulnerabilidades de segurança (Seção 5.1.1, p. 13), analisa gargalos de comunicação, sobrecarga de memória, conflitos de informação compartilhada e o risco de **loops infinitos** ou parada prematura por falta de condições de terminação eficazes (Seção 5.2.5, p. 21).
  - **Privacidade, silos de dados interorganizacionais e governança (Seção 5.2.6, p. 21):** Examina os riscos de vazamento de dados proprietários e falta de transparência em projetos multi-organizacionais, propondo o uso estendido de *RBAC* e *ABAC* para sistemas multiagentes dinâmicos, técnicas de preservação de privacidade (*Differential Privacy*, *Secure Multi-Party Computation*, *Federated Learning*, *Homomorphic Encryption*), conformidade com **GDPR** e **CCPA** (*privacy-by-design*, direito ao esquecimento) e registro imutável de transações e acessos de agentes via *blockchain* / *distributed ledgers*.
- **Justificativa:** Discute com propriedade limitações de escalabilidade, loops infinitos, controle de acesso (*RBAC/ABAC*), privacidade criptográfica e conformidade (*GDPR/CCPA*), embora não modele ataques adversariais contra agentes (como *prompt injection* ou *tool poisoning*) (`P = 0.5`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Agenda de Pesquisa Estruturada em Duas Fases e Oito Questões Abertas (Seção 5, Fig. 4, pp. 12–21):** Propõe um *roadmap* detalhado para a evolução rumo à *Software Engineering 2.0*:
    - **Fase 1 — Aprimoramento das Capacidades Individuais dos Agentes (Seção 5.1, pp. 12–17):**
      1. *Refining Role-Playing Capabilities in SE* (Seção 5.1.1, pp. 12–16): metodologia em 3 etapas (*Market Analysis, Stakeholder Engagement, Value Addition Modeling* $\to$ *Competency Mapping, Performance Evaluation, Gap Analysis* $\to$ *Curating Specialized Data, PEFT Fine-Tuning, Customized Prompts, Continuous Learning*);
      2. *Advancing Prompts through Agent-Oriented Programming (AOP) Paradigms* (Seção 5.1.2, pp. 16–17): criação de linguagens de *prompting* orientadas a agentes e multiagentes (*AOP/MAOP*) que tratem o LLM como audiência primária para reduzir ambiguidade da linguagem natural.
    - **Fase 2 — Otimização da Sinergia entre Agentes (Seção 5.2, pp. 17–21):**
      1. *Human-Agent Collaboration* (Seção 5.2.1): diretrizes de pontos críticos de intervenção humana, interfaces adaptadas por papel e modelos preditivos para a razão ótima humano-agente;
      2. *Evaluating LMA Systems* (Seção 5.2.2): novos *benchmarks* e *sandboxes* que avaliem design colaborativo, delegação, detecção/negociação de conflitos e pedidos proativos de esclarecimento;
      3. *Scaling Up for Complex Projects* (Seção 5.2.3): decomposição hierárquica, sumarização de mensagens, repositórios *blackboard* centralizados e algoritmos de consenso modular;
      4. *Leveraging Industry Principles* (Seção 5.2.4): adoção de *Domain-Driven Design (DDD)*, *Behavior-Driven Development (BDD)*, *Value Stream Mapping* e *Team Topologies*;
      5. *Dynamic Adaptation* (Seção 5.2.5): geração e remoção dinâmica de agentes e papéis em tempo de execução e predição de condições ótimas de parada via ML;
      6. *Privacy and Partial Information* (Seção 5.2.6): *RBAC/ABAC* dinâmico, aprendizado federado/MPC e auditoria via *distributed ledgers*.
- **Justificativa:** Dedica dez páginas (Seção 5, pp. 12–21) a uma agenda de pesquisa altamente estruturada, acionável e diretamente alinhada aos desafios de engenharia, avaliação, colaboração humano-agente e governança de sistemas multiagentes (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 1.0 + 0.5 + 0.5 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P04 |
| **Autores** | Junda He; Christoph Treude; David Lo |
| **Ano** | 2025 |
| **Título** | *LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead* |
| **Periódico / Fonte** | *ACM Transactions on Software Engineering and Methodology (TOSEM)*, Vol. 34, No. 5, Art. 124, pp. 124:1–124:30 |
| **DOI** | `10.1145/3712003` |
| **Qualis** | A2 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão Sistemática da Literatura (71 estudos primários) combinada com 2 Estudos de Caso Empíricos e Agenda de Pesquisa |
| **Domínio Principal** | Sistemas Multiagentes Baseados em LLMs (*LMA Systems*) para Engenharia de Software (*SDLC*, *QA*, Detecção de Vulnerabilidades, Localização de Causa Raiz e Depuração) |
| **Tecnologias / Frameworks Analisados** | *ChatDev* (avaliado empiricamente com `GPT-3.5-turbo`), *MetaGPT*, *AgileCoder*, *AgileGen*, *Think-on-Process (ToP)*, *MegaAgent*, *RCAgent*, *AgentFL*, *GPTLens*, *PentestGPT*, *MASAI*, *MarsCode*, *AutoCodeRover*, *SpecRover*, *SWE-Search*, *AutoGen*, *LangChain*, *DSPy* |
| **Escopo de Aplicação** | Engenharia de Requisitos, Geração de Código, Garantia de Qualidade (*Testing*, *Vulnerability Detection*, *Bug Detection*, *Fault Localization* / *RCA*), Manutenção de Software (*Debugging*, *Code Review*) e Desenvolvimento *End-to-End* |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Formalização do agente LLM como a tupla $\langle L, O, M, P, A, R \rangle$ (Seção 2.2, pp. 3–4); benefícios de sistemas *LMA* sobre LLMs isolados (Seção 1, p. 2); comparação estrutural com *Mixture of Experts (MoE)* (Seção 6.1, p. 22). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Modelo de plataforma de orquestração (coordenação, comunicação, planejamento centralizado/descentralizado) e grafo $G(V,E)$ (Seção 2.3, p. 4); síntese de 71 sistemas multiagentes no *SDLC*, incluindo *RCAgent*, *AgentFL*, *GPTLens*, *AutoCodeRover*, *SWE-Search*, *MetaGPT*, *ChatDev*, *AgileCoder*, *ToP* e *MegaAgent* (Seção 3, pp. 6–10). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Dois estudos de caso empíricos com *ChatDev* (`GPT-3.5-turbo`, Seção 4, pp. 10–12): *Snake* concluído na 2ª tentativa (`76 s`, `US$ 0,019`); *Tetris* parcialmente funcional apenas na 10ª tentativa (`70 s`, `US$ 0,020`, falhando em remover linhas completas). Sem tabelas comparativas de *benchmarks* dos 71 estudos. |
| **RQ4** (Riscos, Segurança e Governança) | `P` | `0.5` | Limitações na detecção de vulnerabilidades por LLMs generalistas (p. 13); gargalos de comunicação, perda de memória e risco de loops infinitos (pp. 19–21); governança de dados interorganizacionais via *RBAC/ABAC*, *Differential Privacy*, *MPC*, *Federated Learning*, *GDPR/CCPA* e *blockchain* (Seção 5.2.6, p. 21). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Agenda de pesquisa em 2 fases e 8 questões (Seção 5, Fig. 4, pp. 12–21): especialização de papéis, *prompting* baseado em *Agent-Oriented Programming (AOP)*, colaboração humano-agente, *benchmarks* cooperativos, escalabilidade via *blackboard*, práticas industriais (*DDD*, *BDD*), adaptação dinâmica e privacidade. |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Aderência Muito Forte (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | A Seção 3 (pp. 5–6) explicita 3 critérios de inclusão (inglês, texto completo acessível, uso de sistemas multiagentes baseados em LLMs para tarefas de Engenharia de Software) e 8 critérios de exclusão (artigos $<5$ páginas, duplicatas, literatura cinzenta/surveys, abordagens de agente único ou modelos sem capacidade de planejamento como *CodeBERT*, publicações anteriores a novembro de 2022 e artigos sem resultados experimentais). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | A estratégia de busca (Seção 3, pp. 5–6) documenta as *queries* booleanas por fase do *SDLC* executadas na base *DBLP* em 14 de novembro de 2024 (identificando `41` estudos primários), complementadas por *snowballing* bidirecional (*backward* e *forward*) até ponto fixo de fecho transitivo (`+30` estudos, totalizando **`71` estudos primários**), além de discutir ameaças à validade na Seção 6.2 (p. 22). |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Embora exija a presença de resultados experimentais como critério de elegibilidade (critério de exclusão 8, p. 5) e complemente a revisão com dois estudos de caso próprios no *ChatDev* (Seção 4), o artigo descreve os 71 estudos primários de forma qualitativa/narrativa ao longo da Seção 3, sem aplicar um instrumento formal de pontuação de qualidade metodológica individual nem tabular comparativamente os resultados empíricos dos 71 estudos. |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões e a agenda de pesquisa da Seção 5 (pp. 12–23) derivam diretamente tanto das lacunas observadas nos 71 estudos revisados quanto das falhas empíricas constatadas no estudo de caso do jogo *Tetris* (dificuldade de escalabilidade lógica em projetos mais complexos). |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **3.5 / 4.0** | **Qualidade Metodológica Alta (87,5%)** |

---

## Parecer Final do Revisor

O artigo **P04** (He, Treude & Lo, 2025), publicado na *ACM TOSEM* e integrante do **Corpus Fundacional** do Trabalho I, possui alta qualidade metodológica (`SCORE_QA = 3.5 / 4.0`, banda **Alta**) e excelente aderência às questões de pesquisa da RSL (`SCORE_RQ = 4.0 / 5.0`). O trabalho fornece à nossa revisão: (i) uma formalização matemática elegante de agentes baseados em LLMs ($\langle L, O, M, P, A, R \rangle$) e de plataformas de orquestração multiagente; (ii) a catalogação sistemática de 71 arquiteturas multiagentes no ciclo de vida de software, incluindo ferramentas diretamente voltadas a diagnóstico de causa raiz em nuvem (*RCAgent*), localização de falhas (*AgentFL*), auditoria de vulnerabilidades (*GPTLens*, *MuCoLD*) e reparo automatizado (*AutoCodeRover*, *SpecRover*, *SWE-Search*); (iii) evidência empírica direta dos limites de confiabilidade de sistemas multiagentes atuais (*ChatDev* resolvendo *Snake* na 2ª tentativa por `US$ 0,019`, mas falhando em concluir os requisitos completos de *Tetris* mesmo após 10 tentativas); e (iv) uma agenda de pesquisa de duas fases que fundamenta o avanço rumo à *Software Engineering 2.0*.
