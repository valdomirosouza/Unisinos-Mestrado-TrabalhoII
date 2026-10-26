# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P15
- **Arquivo PDF avaliado:** `P15-A2-The Rise of Agentic AI A Review of Definitions Frameworks Architectures Applications Evaluation Metrics and Challenges.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A2
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido (Core Match Integral).** O artigo realiza uma revisão sistemática e abrangente de **143 estudos primários** (e 21 *surveys* correlatos) sobre **Agentic AI**, estruturando sete questões de pesquisa que cobrem: (1) definições conceituais e diferenciação frente a *Generative AI*, *Multi-Agent Systems (MAS)* e *Autonomic Computing*; (2) comparação de frameworks baseados em LLMs (*LangChain, AutoGPT, BabyAGI, OpenAgents, AutoGen, CAMEL, MetaGPT, SuperAGI, TB-CSPN*) e sistemas não baseados em LLMs; (3) seis componentes funcionais e cinco modelos arquiteturais de orquestração (*ReAct, Supervisor/Hierarchical, Hybrid Reactive–Deliberative, BDI, Layered Neuro-Symbolic*); (4) aplicações multissetoriais incluindo **Agentic SOC Automation**, **Autonomous IT Operations** para detecção/resolução de incidentes em tempo real e **Moving-Target Defense em Kubernetes**; (5) taxonomia de transformações de entrada/saída (incluindo servidores **MCP**, *logs/audit events* e alertas *Tier 1/Tier 2*); (6) métodos de teste e métricas qualitativas/quantitativas de avaliação; e (7) desafios técnicos, de coordenação multiagente, segurança e governança.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *Future Internet* (MDPI), Volume 17, Número 9, Artigo 404, pp. 1–50, setembro de 2025 (Recebido em 18 de agosto de 2025; Revisado em 1 de setembro de 2025; Aceito em 1 de setembro de 2025; Publicado em 4 de setembro de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão extenso (50 páginas) publicado em periódico científico revisado por pares (*Future Internet*, MDPI), classificado como **Qualis A2** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 50 páginas em inglês com 170 referências, 10 tabelas (6 no corpo e 4 nos Apêndices A e B) e 11 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Distinção Operacional entre *AI Agents* e *Agentic AI* (Seção 1, Fig. 1, pp. 1–2; Seção 3.1, pp. 7–8):** Define um **AI Agent** como uma entidade de software autônoma que percebe, raciocina e age para cumprir tarefas específicas adaptativamente direcionadas, ao passo que **Agentic AI** refere-se a sistemas multiagentes coordenados por uma camada de orquestração (*orchestration layer*) nos quais agentes especializados definem submetas, selecionam ferramentas, executam ações multi-etapas e verificam resultados em malha fechada com supervisão humana mínima (ilustrado na Fig. 1, p. 2, contrastando um agente único buscador de voos com um ecossistema agêntico completo de planejamento de viagens).
  - **Matriz Comparativa *MAS* vs. *Generative AI* vs. *Agentic AI* (Seção 3.1, Tabela 2, pp. 8–9):** Compara sistematicamente os três paradigmas ao longo de **11 dimensões estruturais**: *Primary Function*, *Decision-Making*, *Task Scope*, *Learning Approach*, *Architecture*, *Adaptability*, *Human Intervention*, *Goal Orientation*, *Workflow Management*, *Memory Systems*, *Real-time Adaptation* e *Use Cases*.
  - **Taxonomia em Diagrama de Venn Incluindo *Autonomic Computing* (Seção 3.1, Fig. 3, p. 9):** Posiciona visualmente a **Agentic AI** na interseção entre **LLMs** (comunicação, conhecimento e raciocínio em linguagem natural), **Reinforcement Learning — RL** (aprendizado contínuo por tentativa e erro a partir da experiência), **Multi-Agent Systems — MAS** (cooperação, negociação e competição distribuída) e **Autonomic Computing** (sistemas autogerenciáveis capazes de auto-configuração, auto-cura/*self-healing*, auto-otimização e auto-proteção em infraestrutura de TI).
- **Justificativa:** Oferece uma fundamentação conceitual completa e original, destacando-se por conectar explicitamente *Agentic AI* à tradição de *Autonomic Computing* e *MAS* (Tabela 2 e Fig. 3, pp. 8–9) (`T = 1.0`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Análise Comparativa de 9 Frameworks Baseados em LLMs e Sistemas Não-LLM (Seção 3.2.1–3.2.2, Tabela 3, pp. 10–12):**
    - Na Tabela 3 (p. 10), compara propósito, capacidades agênticas e LLMs subjacentes de: **LangChain**, **AutoGPT**, **BabyAGI**, **OpenAgents**, **AutoGen**, **CAMEL**, **MetaGPT**, **SuperAGI** (destacado pelos controles de recursos e monitoramento voltados à produção corporativa, p. 12) e o framework híbrido neuro-simbólico **TB-CSPN (*Task-Based Cognitive Sequential Planning Network*)** [86], que restringe o LLM à extração semântica de tópicos e utiliza **Redes de Petri Coloridas (*Colored Petri Nets*)** para planejamento e execução determinísticos e auditáveis (p. 12);
    - Na Seção 3.2.2 (p. 12), analisa sistemas agênticos não baseados em LLMs: motores de regras (*CLIPS, Drools, JADE*), agentes de RL (*Q-learning, DQN, Policy Gradient*), planejadores simbólicos (**STRIPS** e **PDDL** [92]), simuladores baseados em agentes (*NetLogo, MASON*) e arquiteturas robóticas de subsunção.
  - **Seis Componentes Funcionais Reutilizáveis (Seção 3.3.1, Fig. 4, pp. 13–14):** Formaliza a pilha modular de sistemas agênticos: (1) *Perception and World Modeling* (normalização multimodal e simulação contrafactual); (2) *Memory (Short-Term, Long-Term, Episodic)* com regras de recuperação e promoção (*retrieval/promotion rules*); (3) *Planning, Reasoning, and Goal Decomposition*; (4) *Execution and Actuation* (com verificação de esquemas, limites de orçamento/latência e *retries*); (5) *Reflection and Evaluation* (autocrítica, verificação assistida por ferramentas e papéis de *critic* aninhados); e (6) *Communication, Orchestration, and Autonomy*.
  - **Cinco Modelos Arquiteturais e de Fluxo de Controle (Seção 3.3.2–3.3.5, Figs. 5–9, Tabela 4, pp. 14–21):**
    1. **ReAct Single-Agent (Fig. 5, pp. 14–15):** Loop compacto *Perception $\to$ Reason/Plan $\to$ Act/Execute $\to$ Evaluation $\to$ Memory (STM/LTM)* sem supervisor externo;
    2. **Supervisor / Hierarchical (Fig. 6, pp. 15–16):** Orquestrador/supervisor central que decompõe metas e delega subtarefas a subagentes especializados (*Sub Agent 1..N*), cada qual executando um loop *ReAct* local sincronizado via *Shared Global Memory*;
    3. **Hybrid Reactive–Deliberative (Fig. 7, pp. 16–17):** Executa em paralelo um **loop reativo rápido** (com *safety/guard checks* embutidos para eventos críticos de baixa latência) e um **loop deliberativo lento** (planejamento de longo horizonte), mediados por um **Arbitrator** sobre memória compartilhada;
    4. **Belief–Desire–Intention — BDI (Fig. 8, pp. 17–18):** Ciclo deliberativo explícito (*Beliefs/World State $\to$ Desires/Options $\to$ Intentions/Committed Goals $\to$ Act/Execute*) ideal para auditabilidade e casos de segurança (*safety cases*);
    5. **Layered Decision / Neuro-Symbolic (Fig. 9, pp. 18–19):** Combina percepção neural e inferência probabilística calibrada com um **Symbolic Planner** e roteador de ferramentas (*Act/Execute Tool Router*);
    - Na Seção 3.3.3–3.3.4 (pp. 19–21), detalha orquestração centralizada vs. descentralizada, protocolos de mensagens estruturadas em **JSON** (contendo intenções, *snapshots* de estado e resultados de ferramentas para *replay* e linhagem), grafos de execução (**DAGs / máquinas de estado**) com *hooks* avaliadores e *policy guards* de entrada/saída para garantir **efeitos colaterais idempotentes (*idempotent side effects*)** (p. 20).
  - **Aplicações e Transformações de E/S em Cibersegurança, SOC e Operações de TI (Seção 3.4–3.5, Tabelas 5 e 6, pp. 22–33):** Mapeia explicitamente na Tabela 5 (p. 23) e na Seção 3.4.2/3.4.4 (pp. 24–25): **Agentic SOC Automation** [117] (detecção, mitigação e resposta proativa a ameaças), **Autonomous IT Operations and Automation** [49, 118] (detecção, predição e resolução colaborativa de incidentes em tempo real), **SLM-based software and IT task automation** [111], **Fault-Tolerant Multi-Agent Software Systems** [62] e **AI Workloads and Infrastructure Defense (ADA)** [120] (defesa de alvo móvel automatizada via rotação efêmera de infraestrutura em Kubernetes), além de catalogar na Tabela 6 (pp. 28–29) o uso de **MCP servers** [120], loops **MAPE-K** [121, 123], ingestão de **Logs/audit events** [40] e triagem autônoma de **Alertas Tier 1/Tier 2** [161].
- **Justificativa:** Apresenta uma das sínteses arquiteturais mais completas da literatura, detalhando diagramas de fluxo de controle para cinco famílias arquiteturais (Figs. 5–9), matrizes de componentes e riscos (Tabela 4), orquestração por grafos DAG com *policy guards* e mapeamento direto para automação de SOC e ITOps (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia de 18 Métodos de Teste e 17 Métricas de Avaliação (Seção 3.6.1–3.6.2, Fig. 11, pp. 33–38):**
    - **Métodos de Teste em 9 Categorias (Fig. 11, pp. 34–35):** (1) *Ensure Correctness* (*Automated Test Generation* via *CodeT, Reflexion, ClarifyGPT* [110] e *Formal Verification* [95]); (2) *Performance Monitoring* (**Runtime Monitoring** com *rollback* e remediação antes de falha crítica [51] e **Heartbeat Monitoring** [123]); (3) *Functional Evaluation* (*Benchmark Testing, Stress Testing, A/B Testing*); (4) *Failure Tolerance* (**Fault Injection** [123] e **Automated Recovery** [150]); (5) *Adaptability Across Domains* (testes em *MineDojo, ALFRED, ScienceWorld* e o benchmark multimodal **CRAB — Cross-Platform Agent Benchmark** [75]); (6) *Behavior in Virtual Environment* (*Simulations* [162] e **Digital Twins** para predição de falhas [163]); (7) *User Response* (*Human-in-the-loop Verification* [45] e *UAT* [104]); (8) *Safety and General Evaluation* (*Testing for Harmful Capabilities* [46] e *Heuristic AGI Test* [134]); e (9) *System-level and Workflow* (*Workflow-centric evaluation* [50] e *Independent Testing of Subtasks* [46]).
    - **Métricas Qualitativas (Seção 3.6.2, p. 36):** *Explainability* (*CAM* [44]), *Transparency* (*AMBY, Drawcto, Constitutional AI*), *User Satisfaction* (*BiLLP* [132]), *Fairness* (*SHAP* e análise contrafactual [101]), *Bias Mitigation*, *Co-operative Behavior* (*MAAC* [70]), *Adaptability* (operacionalização formal com *Petri Nets* [154]) e *Robustness* (execução em *sandbox*, rastreabilidade, *rollback* [51] e avaliação contra comportamento adversarial no **AgentHarm Benchmark** [136]).
    - **Métricas Quantitativas e Indicadores Numéricos Extraídos (Seção 3.6.2, pp. 36–38):**
      - **Accuracy:** Frameworks **LangGraph** e **CrewAI** demonstram cerca de **`94%` de acurácia** na execução de tarefas complexas [53]; modelos **Claude 3.5** e **LLaMA-3.2** atingem **`96%` de acurácia** com *plan caching* eficiente e recuperação baseada em palavras-chave [138]; *ECG AI* atinge `96–97%` [164] e *Organa* `>90%` [150];
      - **Graph Edit Distance (GED):** Mede a similaridade estrutural (número mínimo de edições em nós e arestas) entre o grafo de tarefas gerado pelo agente (`gpt-4-0613`) e o grafo *ground-truth* de especialistas para quantificar a precisão do planejamento *multi-hop* e uso de ferramentas [52, 105] (p. 37);
      - **Rule Fidelity:** Os frameworks *Neuro-Symbolic Agent* [161], *AutoML Agent* [54] e *Agentic Planner* [54] alcançam aproximadamente **`94%` de fidelidade de regras (*rule fidelity*)** na conversão de modelos aprendidos em regras simbólicas legíveis por humanos (p. 37);
      - **Task Completion Time (TCT):** Implementações com **LangGraph** [58], **AutoGen** [151] e **GoEX** [53] registraram um **tempo médio de conclusão de tarefa (*TCT*) de `12 ± 2 minutos`**, representando uma **melhoria de `34,2%`** em relação a sistemas de IA tradicionais (p. 37);
      - **Precision, Recall, F1 Score, Click-Through Rate (CTR) e Gross Merchandise Value (GMV)** (p. 37).
- **Justificativa:** Dedica uma seção inteira (Seção 3.6, Fig. 11, pp. 33–38) à sistematização de métodos de teste de resiliência (*fault injection, runtime monitoring, rollback, CRAB, AgentHarm*) e métricas quantitativas específicas de agentes (*Graph Edit Distance, Rule Fidelity* de `94%`, *TCT* de `12 ± 2 min` com ganho de `34,2%`, e acurácia de `94–96%`) (`T = 1.0`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Riscos Arquiteturais por Família de Orquestração (Seção 3.3.2–3.3.5, Tabela 4, pp. 15–21):** Mapeia os riscos salientes de cada padrão: fragilidade sob alta incerteza em *BDI*; **gargalo no supervisor e ponto único de falha (*single point of failure*)** em arquiteturas *Hierarchical*; baixa paralelização e fragilidade na seleção de ferramentas em larga escala no *ReAct Single-Agent*; **instabilidade ou *"thrash"* de arbitragem** entre o loop rápido e o loop lento no modelo *Hybrid Reactive–Deliberative*; e sobrecarga de alinhamento de representação no *Layered Neuro-Symbolic*.
  - **Seis Eixos de Desafios Técnicos, de Coordenação, Éticos e de Segurança (Seção 3.7, pp. 38–40):**
    1. *Architectural/Technical Challenges:* Rigidez estrutural, falhas em planejamento estratégico de longo prazo e sobrecarga dos 4Vs de dados;
    2. *Ethical/Societal/Governance Limitations:* Evidencia que **quase `78%` das organizações relataram problemas com segurança de dados (*data safety*)** ao utilizar sistemas agênticos [53] (p. 39); lacunas severas de *accountability* (mesmo desenvolvedores não conseguem explicar escolhas emergentes de agentes treinados com RL [157]); e propagação de decisões enviesadas por falhas de comunicação;
    3. *Performance/Tool Integration Issues:* Latência computacional durante invocação simultânea de múltiplas ferramentas externas em tempo real e **ausência de interfaces padronizadas** para integração com fluxos comerciais [53, 105];
    4. *Multi-Agent Coordination:* Inconsistência no acesso a dados, latência de comunicação, falha no compartilhamento de contexto e **suscetibilidade a falhas correlacionadas que resultam em conluio emergente (*collusion*) mesmo sem intenção maliciosa**, degradando robustez e transparência [135] (p. 39);
    5. *Human–AI Interaction:* Protocolos rígidos de comunicação e desalinhamento moral e de intenção humana em tarefas críticas [162];
    6. *Security (p. 40):* Vulnerabilidade a **ataques adversariais, envenenamento de dados (*data poisoning*), uso indevido de ferramentas/APIs externas** e ausência de pipelines verificáveis para fontes externas de conhecimento, exigindo princípios *secure-by-design*, auditorias contínuas e *guardrails* de contenção [53, 105, 135].
- **Justificativa:** Analisa com grande profundidade tanto os modos de falha arquiteturais (Tabela 4 e falhas correlacionadas/conluio emergente entre agentes) quanto riscos de segurança, governança e o dado empírico de que `78%` das organizações enfrentam problemas de segurança de dados (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Lacunas Identificadas na Comparação de 21 *Surveys* (Seção 2, Tabela 1, pp. 5–7):** Demonstra que as revisões anteriores negligenciaram a padronização de *benchmarks*, a avaliação de desempenho e a modelagem formal de transformações de entrada/saída (*input–output modeling*).
  - **Subdesenvolvimento de Métricas de Recuperação de Erros e *Self-Healing* (Seção 3.6.2, p. 38; Seção 3.7, pp. 39–40):** Aponta que **métricas para recuperação de erros (*metrics for error recovery*) permanecem subdesenvolvidas**, com sistemas atuais falhando diante de erros conceituais, **falhas em cascata (*cascading faults*)** e *edge cases* complexos [105, 136, 165]. Propõe como direções futuras: (1) arquiteturas tolerantes a falhas e *self-healing* com replanejamento dinâmico, verificação cruzada multiagente (*multi-agent cross-verification*), reexecuções baseadas em confiança (*confidence-based reruns*) e loops *actor–critic* [33, 49, 65, 66, 166]; (2) formulação de uma **teoria de sistemas formal para IA agêntica (*systems theory for agentic AI*, [167])** com protocolos escaláveis de coordenação e garantias de segurança (p. 39); e (3) *toolchains* padronizadas e pipelines verificáveis *secure-by-design* para conexão segura com APIs e bases de conhecimento externas (pp. 39–40).
- **Justificativa:** Identifica lacunas altamente relevantes para a engenharia de sistemas agênticos (métricas de recuperação de falhas em cascata, verificação cruzada multiagente, teoria de sistemas agênticos e padronização de interfaces de ferramentas) (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 1.0 + 1.0 + 1.0 + 1.0 = 5.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P15 |
| **Autores** | Ajay Bandi; Bhavani Kongari; Roshini Naguru; Sahitya Pasnoor; Sri Vidya Vilipala |
| **Ano** | 2025 |
| **Título** | *The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges* |
| **Periódico / Fonte** | *Future Internet* (MDPI), Vol. 17, No. 9, Art. 404, pp. 1–50 |
| **DOI** | `10.3390/fi17090404` |
| **Qualis** | A2 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão Sistemática da Literatura (143 estudos primários analisados + 21 *surveys* comparados; 170 referências) |
| **Domínio Principal** | *Agentic AI*: Definições, Frameworks, Modelos Arquiteturais de Orquestração, Transformações de E/S, Métodos de Teste, Métricas de Avaliação e Desafios |
| **Tecnologias / Frameworks Analisados** | *LangChain, AutoGPT, BabyAGI, OpenAgents, AutoGen, CAMEL, MetaGPT, SuperAGI*, **TB-CSPN** (*Colored Petri Nets*), *LangGraph, CrewAI, GoEX*, **MCP servers**, *STRIPS, PDDL, CLIPS, Drools, JADE*, arquiteturas **ReAct, Supervisor/Hierarchical, Hybrid Reactive–Deliberative, BDI, Layered Neuro-Symbolic**, *CRAB*, *AgentHarm Benchmark*, *MAPE-K* |
| **Escopo de Aplicação** | Multissetorial (13 domínios na Tabela 5, pp. 22–24), destacando em Software e Segurança: **Agentic SOC Automation** [117], **Autonomous IT Operations** para detecção e resolução de incidentes [49, 118], **Moving-Target Defense (ADA) em Kubernetes** [120], sistemas multiagentes tolerantes a falhas [62] e resposta a alertas *Tier 1/Tier 2* [161] |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Distinção entre *AI Agents* e *Agentic AI* (Fig. 1, pp. 1–2); comparação estruturada entre *MAS*, *GenAI* e *Agentic AI* em 11 dimensões (Tabela 2, pp. 8–9); diagrama de Venn integrando *LLMs, RL, MAS* e **Autonomic Computing** (Fig. 3, p. 9). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Comparação de 9 frameworks LLM (*LangChain, AutoGPT, BabyAGI, OpenAgents, AutoGen, CAMEL, MetaGPT, SuperAGI, TB-CSPN*, Tabela 3, pp. 10–12) e sistemas não-LLM; 6 componentes funcionais (Fig. 4); **5 modelos arquiteturais detalhados** (*ReAct, Supervisor/Hierarchical, Hybrid Reactive–Deliberative, BDI, Layered Neuro-Symbolic*, Figs. 5–9, Tabela 4, pp. 14–21); e mapeamento de **Agentic SOC Automation**, **Autonomous IT Operations**, **MCP servers** e **Kubernetes Moving-Target Defense** (Tabelas 5–6, pp. 22–32). |
| **RQ3** (Evidências Empíricas e Métricas) | `T` | `1.0` | Taxonomia de **18 métodos de teste** (*Runtime/Heartbeat Monitoring, Fault Injection, Automated Recovery, CRAB, Digital Twins*, Fig. 11, pp. 34–35) e **17 métricas qualitativas/quantitativas** (pp. 36–38): **acurácia de `94%` (*LangGraph/CrewAI*) e `96%` (*Claude 3.5/LLaMA-3.2* com *plan caching*)**, **Graph Edit Distance (GED)**, **Rule Fidelity de `~94%`** e **Task Completion Time (TCT) de `12 ± 2 min` (`+34,2%` sobre IA tradicional)**. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Riscos específicos por arquitetura (Tabela 4, p. 21: *supervisor bottleneck/SPOF, arbitration thrash*); 6 categorias de desafios (Seção 3.7, pp. 38–40): **`78%` das organizações com problemas de segurança de dados** [53], opacidade de RL, **conluio emergente (*collusion*) e falhas correlacionadas** em MAS cooperativos [135], ataques adversariais, *data poisoning* e uso indevido de ferramentas/APIs externas. |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Matriz de lacunas em 21 *surveys* (Tabela 1, pp. 6–7); subdesenvolvimento de **métricas de recuperação de erros** frente a falhas em cascata (p. 38); necessidade de verificação cruzada multiagente, *confidence-based reruns*, **teoria de sistemas para IA agêntica** [167] e pipelines verificáveis *secure-by-design* (pp. 38–41). |
| **Total (`SCORE_RQ`)** | — | **5.0 / 5.0** | **Aderência Máxima (100,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | Define sete questões de pesquisa explícitas (RQ1–RQ7, Seção 1.2, pp. 3–4) e explicita na Seção 2 (p. 5) os critérios de inclusão (estudos que discutem conceitos, sistemas ou desafios de *Agentic AI* usando estudos de caso, *surveys* e métodos experimentais, com remoção de duplicatas e triagem de títulos/resumos/conclusões). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | Documenta na Seção 2 (p. 5) as 5 bases pesquisadas (*Library Search, ACM Digital Library, ScienceDirect, Google Scholar, Semantic Scholar*), a *string* booleana exata de busca, a busca reversa nas referências (*snowballing*) e disponibiliza no **Apêndice A (Tabelas A1, A2 e A3, pp. 41–43)** a distribuição completa e rastreável dos **143 estudos primários** por ano (1999–2025, com `90%+` em 2024–2025), tipo de publicação (`70` periódicos, `38` *preprints*, `26` conferências) e veículo exato de publicação com os respectivos códigos de referência. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Avalia comparativamente 21 *surveys* anteriores mediante rubrica estruturada (`L, M, H, NA`) em seis dimensões na Tabela 1 (pp. 6–7) e sintetiza os 143 estudos primários em tabelas analíticas densas (Tabelas 2–6) e 11 figuras, mas não aplica pontuação individual de qualidade metodológica aos 143 estudos primários (incluindo `28%` de *preprints* do *arXiv/SSRN*). |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | Todas as sete questões de pesquisa formuladas na Seção 1.2 são respondidas de forma sistemática, detalhada e perfeitamente ancorada nas tabelas e diagramas da Seção 3 (pp. 7–40) e sintetizadas na Seção 4 (pp. 40–41). |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **3.5 / 4.0** | **Qualidade Metodológica Alta (87,5%)** |

---

## Parecer Final do Revisor

O artigo **P15** (Bandi et al., 2025), publicado na *Future Internet* (MDPI) e integrante do **Corpus Fundacional** do Trabalho I, atinge a pontuação máxima de cobertura das questões de pesquisa da RSL (`SCORE_RQ = 5.0 / 5.0`) e alta qualidade metodológica (`SCORE_QA = 3.5 / 4.0`, banda **Alta**). Com 50 páginas e 143 estudos primários mapeados, **P15** é uma referência estruturante para todas as seções da nossa revisão: (i) conecta conceitualmente **Agentic AI** a **Autonomic Computing**, **MAS** e **RL** (Fig. 3, Tabela 2); (ii) formaliza os diagramas de fluxo de controle e os riscos de **cinco arquiteturas canônicas** (*ReAct, Supervisor/Hierarchical, Hybrid Reactive–Deliberative* com árbitro, *BDI* e *Layered Neuro-Symbolic*, Figs. 5–9, Tabela 4), além do framework **TB-CSPN** baseado em Redes de Petri Coloridas; (iii) mapeia diretamente aplicações de **Agentic SOC Automation**, **Autonomous IT Operations**, servidores **MCP** e resposta a alertas **Tier 1/Tier 2** (Tabelas 5 e 6); e (iv) fornece uma taxonomia completa de **18 métodos de teste** (*fault injection, runtime monitoring, rollback, CRAB*) e **17 métricas de avaliação**, incluindo **Graph Edit Distance (GED)**, **Rule Fidelity (`94%`)** e **Task Completion Time (`12 ± 2 min`, `-34,2%`)** (Fig. 11, pp. 34–38).
