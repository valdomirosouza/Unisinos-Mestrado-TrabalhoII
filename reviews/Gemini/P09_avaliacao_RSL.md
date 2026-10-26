# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P09
- **Arquivo PDF avaliado:** `P09-A1-AI Agents vs. Agentic AI A Conceptual taxonomy applications and challenges.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo apresenta uma taxonomia conceitual, arquitetural e operacional de referência distinguindo rigorosamente quatro paradigmas pós-ChatGPT — **Generative AI**, **AI Agents**, **Generative Agents (Inferred)** e **Agentic AI** —, analisando a evolução arquitetural de agentes isolados aumentados por ferramentas (*ReAct*, *LangChain*, *Anthropic Computer Use*) para ecossistemas multiagentes orquestrados (*AutoGen*, *CrewAI*, *MetaGPT*, *ChatDev*, protocolo *Google A2A*), incluindo um caso de uso explícito de **resposta autônoma a incidentes de cibersegurança e operações de TI** (Seção 4.0.2, Fig. 11d, p. 16–17; Tabela 11, p. 19), além de mapear desafios de cascata de erros, segurança adversarial e governança.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *Information Fusion* (Elsevier), Volume 126 (2026), Artigo 103599, pp. 1–30 (Recebido em 29 de maio de 2025; Revisado em 25 de julho de 2025; Aceito em 30 de julho de 2025; Disponível online em 22 de agosto de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo completo publicado em periódico científico de altíssimo impacto com revisão por pares (*Information Fusion*, Elsevier), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 30 páginas em inglês com 233 referências e 11 tabelas comparativas.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Desambiguação taxonômica em quatro níveis: *Generative AI* $\to$ *AI Agents* $\to$ *Generative Agents* $\to$ *Agentic AI* (Seções 1–3, Fig. 2–8, Tabelas 1–9, pp. 1–12):** O artigo estabelece a taxonomia conceitual mais detalhada do corpus para diferenciar agentes singulares de sistemas agênticos:
    - **Generative AI (Seção 2.0.3, p. 6):** Sistemas reativos, dependentes de *prompt* e *stateless* (*Prompt $\to$ LLM/LIM $\to$ Output*);
    - **AI Agents (Seção 2, Fig. 4, pp. 4–7):** Entidades modulares de agente único orientadas a tarefas específicas mediante invocação de ferramentas externas/APIs, *function calling* e raciocínio sequencial (*Prompt $\to$ Tool Call $\to$ LLM $\to$ Output*), caracterizadas pela tríade *Autonomy, Task-Specificity, Reactivity* (exemplificadas pelo projeto *Anthropic Computer Use* com *Claude*, p. 4);
    - **Inferred Generative Agents (Tabelas 2–9, pp. 9–12):** Agentes modulares com memória e planejamento comportamental que executam subtarefas gerativas dentro de fluxos maiores;
    - **Agentic AI (Seção 3, Fig. 7–8, Tabelas 1–9, pp. 7–13):** Ecossistemas multiagentes colaborativos caracterizados por decomposição dinâmica de objetivos (*Goal $\to$ Agent Orchestration $\to$ Output*), memória persistente compartilhada, coordenação hierárquica ou descentralizada e autonomia emergente em nível de sistema (ilustrada pela analogia do termostato inteligente isolado vs. ecossistema *smart home* multiagente na Fig. 7, p. 8).
  - **Importância de Engenharia da Distinção Taxonômica (Seção 1, p. 2):** Demonstra que a distinção formal evita tanto o *under-engineering* de cenários complexos que exigem coordenação multiagente quanto o *over-engineering* de tarefas simples resolvíveis por um único *AI Agent*.
- **Justificativa:** Oferece uma fundamentação conceitual e taxonômica exaustiva (nove tabelas comparativas estruturadas nas pp. 9–12) sobre a evolução da IA generativa até sistemas multiagentes autônomos (`T = 1.0`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Evolução Arquitetural dos Módulos de *AI Agents* para *Agentic AI* (Seção 3.1, Fig. 8, pp. 10–13):**
    - Detalha os 4 subsistemas clássicos de *AI Agents* (Seção 3.1.1, pp. 10, 12): *Perception Module*, *Knowledge Representation and Reasoning (KRR) Module*, *Action Selection and Execution Module* e *Basic Learning and Adaptation*;
    - Especifica os 4 pilares arquiteturais de **Agentic AI** (Seção 3.1.2, Fig. 8, pp. 12–13): (1) *Ensemble of Specialized Agents* (agentes *role-bound* comunicando-se via filas de mensagens assíncronas, *blackboards* ou memória compartilhada, ex.: *MetaGPT*); (2) *Advanced Reasoning and Planning* (*ReAct*, *Chain-of-Thought*, *Tree of Thoughts*); (3) *Persistent Memory Architectures* (memória episódica, semântica e vetorial para *RAG*, *scratchpads* no *AutoGen*); e (4) *Orchestration Layers / Meta-Agents* (meta-agentes supervisores que alocam subtarefas, gerenciam dependências e resolvem conflitos, ex.: *CEO agent* no *ChatDev*).
  - **Protocolos de Interoperabilidade e Frameworks Industriais (Seção 1, p. 2; Seção 2.1.2, p. 6; Tabelas 10 e 11, pp. 18–19; Seção 6.1, pp. 22–24):** Analisa o protocolo **Google Agent-to-Agent (A2A)** anunciado em 2025 (baseado em cinco princípios: capacidades agênticas, padrões existentes, segurança por padrão, suporte a tarefas de longa duração e agnosticismo de modalidade, p. 2) e cita o **Model Context Protocol (MCP)** (ref. [65], p. 27), além de comparar frameworks e produtos como *AutoGen*, *CrewAI*, *LangGraph*, *MetaGPT*, *ChatDev*, *AutoGPT*, *BabyAGI*, *EasyTool*, *Gentopia*, *ToolFiVe*, *OpenAI Operator*, *Claude 3.5 Agent*, *Microsoft Copilot Studio (Agentic Mode)* e **Atera AI Copilot** (para *IT Operations*).
  - **Arquitetura de Resposta Autônoma a Incidentes de Cibersegurança (Seção 4.0.2, item 4, Fig. 11d, pp. 16–17):** Descreve um pipeline multiagente em ambientes corporativos de TI no qual, diante de um alerta de acesso anormal ou exfiltração de dados, quatro agentes especializados atuam em paralelo sob um **Workflow Orchestrator**: (1) agente de classificação de ameaças em tempo real; (2) agente de consulta e correlação de logs entre nós de rede; (3) agente de conformidade regulatória (*GDPR/HIPAA*); e (4) agente de simulação de estratégias de mitigação e previsão de risco operacional, integrados por memória compartilhada e loop de *feedback*.
- **Justificativa:** Cobre com profundidade excepcional as arquiteturas de memória, orquestração por meta-agentes, protocolos de interoperabilidade (*A2A*, *MCP*) e pipelines multiagentes para resposta a incidentes de cibersegurança e operações de TI (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Mapeamento comparativo de 26 sistemas industriais e acadêmicos (Seção 4, Figs. 9–11, Tabelas 10 e 11, pp. 13–19):** Cataloga 14 *AI Agents* representativos de 2023–2025 na Tabela 10 (p. 18: *ChatGPT Deep Research, OpenAI Operator, Google Agentspace, NotebookLM Plus, Amazon Nova Act, Manus Agent, Harvey AI, Otter, ClickUp Brain, Agentforce, Microsoft Copilot, Project Astra, Claude 3.5 Agent*) e 12 modelos de *Agentic AI* na Tabela 11 (p. 19: *Auto-GPT, GPT Engineer, MetaGPT, BabyAGI, Voyager, CAMEL, Salesforce Einstein Copilot, Microsoft Copilot Studio Agentic Mode, Atera AI Copilot* para diagnóstico e resolução de incidentes de TI, *AES Safety Audit Agent, DeepMind Gato, GPT-4o + Plugins*).
  - **Critérios de Avaliação por Paradigma (Tabela 3, p. 10; Seção 4.0.2, p. 16):** Distingue o foco avaliativo de *AI Agents* (*Accuracy, latency*) frente a *Agentic AI* (*Engagement, adaptability*, redução de latência decisória e redução de falsos positivos em resposta a incidentes cibernéticos, p. 16).
  - **Limitação:** Conforme declarado na seção *Data availability* (p. 26: *"No data was used for the research described in the article"*) e na crítica da Seção 5.1 (p. 22), o estudo realiza uma síntese conceitual e qualitativa da literatura sem conduzir experimentos quantitativos próprios nem reportar tabelas numéricas de *benchmarks* operacionais.
- **Justificativa:** Documenta amplo conjunto de sistemas reais em operação (incluindo *Atera AI Copilot* para ITOps e fluxos de resposta a incidentes cibernéticos), mas sem métricas quantitativas experimentais primárias (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Diagnóstico Sistemático de Limitações de *AI Agents* vs. *Agentic AI* (Seção 5.0.1–5.0.2, Fig. 12a–b, pp. 16–22):**
    - **Cinco limitações de *AI Agents* (Seção 5.0.1, Fig. 12a, pp. 16–20):** (1) *Lack of Causal Understanding* (confusão entre correlação estatística e causalidade, incapacidade de raciocínio contrafactual e fragilidade sob *distributional shift*, notando que mesmo modelos como *DeepSeek-R1* produzem cadeias *CoT* linguisticamente persuasivas, mas não formalmente válidas como raciocinadores OWL/*Pellet*); (2) *Inherited Limitations from LLMs* (alucinações, fragilidade a variações de *prompt*, latência e custo de múltiplas chamadas LLM); (3) *Incomplete Agentic Properties* (autonomia parcial dependente de *scaffolding* humano, baixa proatividade e habilidade social engessada); (4) *Limited Long-Horizon Planning and Recovery* (ausência de recuperação sistemática de falhas); e (5) *Reliability and Safety Concerns* (falta de verificação formal).
    - **Oito gargalos críticos e riscos de *Agentic AI* (Seção 5.0.2, Fig. 12b, pp. 20–21):**
      1. *Amplified Causality Challenges:* **mudança de distribuição inter-agentes (*inter-agent distributional shift*)** e **cascatas de erro (*error cascades*)**, onde a alucinação de um agente verificador corrompe todos os agentes *downstream*;
      2. *Communication and Coordination Bottlenecks:* deriva contextual em trocas em linguagem natural e contenção de recursos (*race conditions*);
      3. *Emergent Behavior and Predictability:* loops infinitos de planejamento, *deadlocks* de ação e comportamentos contraditórios;
      4. *Scalability and Debugging Complexity:* **não-composicionalidade (*non-compositionality*)** — adicionar mais agentes aumenta ruído e sobrecarga de coordenação — e dificuldade de depurar cadeias aninhadas *black-box*;
      5. *Trust, Explainability, and Verification:* opacidade composta entre memórias distribuídas e inexistência de *model checking* formal para MAS baseados em LLMs;
      6. *Security and Adversarial Risks:* **ponto único de comprometimento (*single point of compromise*)** — a infecção de um único agente via *prompt injection*, *model poisoning* ou manipulação adversarial de ferramentas propaga estados corrompidos por toda a memória compartilhada —, além de indução de *deadlocks* e exaustão de recursos;
      7. *Ethical and Governance Challenges:* *accountability gaps*, amplificação mútua de vieses entre agentes e *value drift* em horizontes longos;
      8. *Immature Foundations and Research Gaps:* fragmentação arquitetural e ausência de padrões de segurança.
- **Justificativa:** Apresenta uma análise técnica magistral dos modos de falha multiagentes (*error cascades*, *inter-agent distributional shift*, *non-compositionality*, *single point of compromise* via *prompt injection* e *deadlocks*) e dos desafios de governança e verificação (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Dez Soluções Arquiteturais e Algorítmicas (Seção 6.1, Fig. 13, pp. 22–24):** Propõe e detalha dez mecanismos estruturantes para superar as limitações atuais: (1) *Shared Agentic RAG*; (2) *Tool-Augmented Reasoning (Function Calling)* com verificação de esquema (*WaitGPT*); (3) *Agentic Loop (ReAct)* reconciliado via memória compartilhada; (4) *Memory Architectures (Episodic, Semantic, Vector)* sincronizadas; (5) *Multi-Agent Orchestration with Role Specialization* (isolando traços de raciocínio e contendo falhas); (6) *Reflexive and Self-Critique Mechanisms* (*inter-agent evaluation* e *Reflexion*); (7) *Programmatic Prompt Engineering Pipelines*; (8) *Causal Modeling and Simulation-Based Planning* (integrando grafos causais, inferência bayesiana e planejadores formais como **STRIPS** e **PDDL**); (9) *Monitoring, Auditing, and Explainability Pipelines* (trilhas de auditoria entre agentes e *dialogue replays*); e (10) *Governance-Aware Architectures (Accountability and Role Isolation)* (implementando *RBAC*, *sandboxing* e resolução de identidade para conter agentes comprometidos).
  - **Roadmap Futuro e Paradigma *Absolute Zero (AZR)* (Seção 6.2, Fig. 14, pp. 24–25):** Contrasta a evolução futura de *AI Agents* vs. *Agentic AI* (Fig. 14, p. 25) e destaca o framework **Absolute Zero: Reinforced Self-play Reasoning with Zero Data (AZR)** [173] como fronteira transformadora na qual coletivos de agentes geram, validam e resolvem suas próprias tarefas via *self-play* e feedback verificável (ex.: execução de código) sem depender de corpora estáticos anotados por humanos.
- **Justificativa:** Oferece um roteiro futuro completo, conectando diretamente cada limitação diagnosticada a dez mecanismos arquiteturais concretos (Fig. 13) e a novos paradigmas de aprendizado autoevolutivo (*AZR*) (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 1.0 + 0.5 + 1.0 + 1.0 = 4.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P09 |
| **Autores** | Ranjan Sapkota; Konstantinos I. Roumeliotis; Manoj Karkee |
| **Ano** | 2026 *(Disponível online em agosto de 2025; Volume 126 datado de 2026)* |
| **Título** | *AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges* |
| **Periódico / Fonte** | *Information Fusion* (Elsevier), Vol. 126, Art. 103599, pp. 1–30 |
| **DOI** | `10.1016/j.inffus.2025.103599` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Artigo de Revisão e Taxonomia Conceitual/Arquitetural (233 referências) |
| **Domínio Principal** | Taxonomia Comparativa entre *Generative AI*, *AI Agents*, *Generative Agents* e *Agentic AI*: Arquiteturas, Orquestração Multiagente, Aplicações e Riscos |
| **Tecnologias / Frameworks Analisados** | *AutoGen*, *CrewAI*, *LangGraph*, *MetaGPT*, *ChatDev*, *LangChain*, *AutoGPT*, *BabyAGI*, *Anthropic Computer Use (Claude 3.5)*, *OpenAI Operator*, *Atera AI Copilot*, *ReAct*, *Tree of Thoughts*, *Reflexion*, protocolo **Google A2A (Agent-to-Agent)**, *MCP*, *STRIPS/PDDL*, *Absolute Zero (AZR)* |
| **Escopo de Aplicação** | Automação corporativa e suporte ao cliente, assistentes de pesquisa multiagentes, coordenação robótica, suporte à decisão médica em UTI e **automação adaptativa de fluxos de trabalho e resposta a incidentes de cibersegurança/TI** (Seção 4.0.2, Fig. 11d, Tabelas 10–11) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Taxonomia em 4 arquétipos (*Generative AI, AI Agents, Inferred Generative Agents, Agentic AI*) detalhada ao longo de 9 tabelas comparativas (Tabelas 1–9, pp. 9–12) e na analogia termostato vs. *smart home* (Fig. 7, p. 8). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Evolução arquitetural (Seção 3.1, Fig. 8, pp. 10–13): *Ensemble of Specialized Agents*, raciocínio *ReAct/CoT/ToT*, memória persistente (episódica, semântica, vetorial) e *Orchestration Layers / Meta-Agents*; protocolo **Google A2A** (p. 2); pipeline multiagente de resposta a incidentes de cibersegurança (Fig. 11d, pp. 16–17). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Mapeamento funcional de 14 *AI Agents* (Tabela 10, p. 18) e 12 sistemas de *Agentic AI* (Tabela 11, p. 19, incluindo *Atera AI Copilot* para ITOps); distinção de métricas de avaliação (Tabela 3, p. 10) e benefícios qualitativos em resposta a incidentes (redução de latência decisória e falsos positivos, p. 16). Sem experimentos quantitativos próprios. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Análise profunda de 5 limitações de *AI Agents* (Seção 5.0.1, Fig. 12a) e 8 gargalos de *Agentic AI* (Seção 5.0.2, Fig. 12b, pp. 16–22): *inter-agent distributional shift*, *error cascades*, *non-compositionality*, *deadlocks*, ponto único de comprometimento via *prompt injection / tool manipulation*, *accountability gaps* e *value drift*. |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Dez soluções arquiteturais (Seção 6.1, Fig. 13, pp. 22–24: *Agentic RAG, Function Calling, ReAct, Memory, Role Specialization, Reflexion, Programmatic Prompting, Causal/PDDL Planning, Audit Pipelines, Governance RBAC/Role Isolation*) e *roadmap* futuro incluindo *Absolute Zero (AZR)* (Seção 6.2, Fig. 14, pp. 24–25). |
| **Total (`SCORE_RQ`)** | — | **4.5 / 5.0** | **Aderência Excepcional (90,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | A Seção 1.1 e a Figura 3 (pp. 3–4) definem um pipeline metodológico claro em 8 estágios sequenciais e estabelecem os critérios de inclusão da literatura na Seção 1.1.1 (p. 4): relevância em termos de novidade conceitual, avaliação empírica, contribuição arquitetural e impacto de citações. |
| **QA2 — Busca e transparência metodológica** | `P` | `0.5` | A Seção 1.1.1 (p. 4) documenta uma estratégia de busca híbrida consultando **12 plataformas** (7 bases acadêmicas: *Google Scholar, IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, arXiv*; e 5 plataformas de descoberta assistidas por IA: *ChatGPT, Perplexity.ai, DeepSeek, Hugging Face Search, Grok*) e informa as combinações booleanas de termos utilizadas, mas não apresenta fluxograma PRISMA com o número exato de registros triados e excluídos em cada etapa. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `Y` | `1.0` | Sintetiza 233 referências com extraordinário rigor analítico em 11 tabelas comparativas multidimensionais (Tabelas 1–11) e 14 figuras conceituais/arquiteturais, além de incluir uma seção crítica explícita (*Section 5.1: Balanced critique and field-wide limitations*, p. 22) que avalia os vieses metodológicos e a falta de validação empírica em ambientes reais nos estudos primários da área. |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões e o *roadmap* da Seção 6–7 (pp. 22–25) decorrem diretamente da matriz de comparação taxonômica (Tabelas 1–9) e do diagnóstico de limitações (Seção 5), mantendo total consistência lógica e transparência (incluindo declaração explícita do uso de ferramentas de apoio na p. 25). |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **3.5 / 4.0** | **Qualidade Metodológica Alta (87,5%)** |

---

## Parecer Final do Revisor

O artigo **P09** (Sapkota, Roumeliotis & Karkee, 2026), publicado na *Information Fusion* e integrante do **Corpus Fundacional** do Trabalho I, é um estudo de referência de altíssimo nível (`SCORE_QA = 3.5 / 4.0`, banda **Alta**; `SCORE_RQ = 4.5 / 5.0`). Ele oferece a espinha dorsal taxonômica ideal para a Seção de Fundamentação e Arquitetura da nossa RSL ao formalizar, em nove tabelas comparativas (Tabelas 1–9), a progressão entre **Generative AI**, **AI Agents**, **Generative Agents** e **Agentic AI**. Além disso, documenta diretamente o protocolo **Google A2A**, um pipeline arquitetural completo de **resposta multiagente a incidentes de cibersegurança** (Fig. 11d, pp. 16–17), uma análise rigorosa de falhas sistêmicas em enxames de agentes (*inter-agent distributional shift*, *error cascades*, *non-compositionality* e *single point of compromise*) e dez padrões arquiteturais de mitigação e governança (*role isolation*, *RBAC*, *sandboxing*, *PDDL/causal planning* e trilhas de auditoria inter-agentes).
