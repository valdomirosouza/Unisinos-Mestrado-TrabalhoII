# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P10
- **Arquivo PDF avaliado:** `P10-A1-Agentic AI Autonomous Intelligence for Complex Goals - A Comprehensive Survey.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo apresenta um *survey* abrangente sobre **Agentic AI** voltada a objetivos complexos (*Autonomous Intelligence for Complex Goals*), contrastando sistematicamente *Traditional AI*, *Classical Agents*, *Reinforcement Learning Agents* e *Agentic AI* (Tabelas 1–3, pp. 3–7), detalhando arquiteturas multiagentes (*MAS*), aprendizado por reforço hierárquico (*HRL*), arquiteturas modulares orientadas a metas, raciocínio e uso de ferramentas (Seção IV, Fig. 1–3, pp. 4–10), aplicações em **sistemas de software adaptativos ("living software systems")** e detecção adaptativa de ameaças de cibersegurança (Seção V.C, Tabela 7, pp. 10–11), e dedicando três seções inteiras a desafios técnicos, implicações éticas/regulatórias, governança (**Human-in-the-Loop — HITL** vs. **Human-on-the-Loop — HOTL**, protocolos de *override*, trilhas de auditoria) e um *roadmap* de pesquisa em dez eixos (Seções VII–X, Tabelas 10–14, pp. 13–22).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *IEEE Access*, Volume 13, pp. 18912–18936, 2025 (Recebido em 1 de janeiro de 2025; Aceito em 19 de janeiro de 2025; Data de publicação em 22 de janeiro de 2025; Data da versão atual em 29 de janeiro de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo completo publicado em periódico científico com revisão por pares (*IEEE Access*, IEEE), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 25 páginas em inglês com 101 referências, 14 tabelas e 3 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Tríade de Matrizes Comparativas de Evolução de Agentes (Seções II.B–C e III.D, Tabelas 1, 2 e 3, pp. 3–7):** O artigo estrutura a transição histórica e funcional da inteligência artificial até a *Agentic AI* em três tabelas comparativas complementares:
    - **Tabela 1 (*Traditional AI vs. Agentic AI*, p. 4):** Contrasta foco primário (*task-specific automation* vs. *goal-oriented autonomy*), adaptabilidade (limitada aos dados de treino vs. alta adaptação em tempo real), tomada de decisão (regras pré-programadas/estáticas vs. autônoma orientada por contexto e objetivos), nível de autonomia (baixo, com supervisão humana constante vs. alto, operando independentemente) e escopo de aplicação;
    - **Tabela 2 (*Classical Agents vs. Reinforcement Learning Agents vs. Agentic AI*, p. 4):** Compara os três paradigmas quanto a tomada de decisão (*predefined rules* $\to$ *trial-and-error reward maximization* $\to$ *goal-oriented dynamic adaptation*), adaptabilidade, autonomia e limitações-chave;
    - **Tabela 3 (*Traditional Agents vs. Agentic AI*, p. 7):** Compara seis dimensões operacionais: *Autonomy*, *Adaptability*, *Goal Complexity*, *Learning Approach* (supervisionado/estático vs. contínuo, *RL*, *meta-learning*), *Decision-Making* e *Transparency (XAI)*.
  - **Três Pilares Definidores de *Agentic AI* (Seção III.A–C, Tabelas 4 e 5, pp. 4–6):** Formaliza as propriedades centrais da IA agêntica: (1) *Autonomy and Goal Complexity* (capacidade de decompor objetivos de longo prazo conflitantes ou mutáveis em subtarefas dinâmicas sem intervenção humana); (2) *Environmental and Operational Complexity* (atuação sob incerteza, dados ruidosos/incompletos e múltiplos *stakeholders*, Tabela 5, p. 6); e (3) *Independent Decision-Making and Adaptability* (inferência probabilística, aprendizado contínuo e auto-otimização).
  - **Paradigmas de Supervisão Humana — *HITL* vs. *HOTL* (Seção IX.B, p. 16):** Formaliza a distinção operacional entre **Human-in-the-Loop (HITL)** (onde operadores humanos interagem diretamente com o agente e aprovam ações em momentos críticos) e **Human-on-the-Loop (HOTL)** (onde o sistema opera de forma autônoma sob monitoramento humano contínuo, com intervenção acionada apenas via **protocolos de *override* / sistemas de última linha** quando desvios ou emergências ocorrem).
- **Justificativa:** Oferece uma caracterização conceitual abrangente da transição de agentes clássicos e de *RL* para *Agentic AI*, além de formalizar os regimes de controle *HITL* e *HOTL* (`T = 1.0`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Fundamentos Arquiteturais e Controle Adaptativo (Seção II.D, Fig. 1, pp. 4–5; Seção IV.A, Fig. 3, pp. 6, 9):** Descreve a convergência de três pilares técnicos (Fig. 1, p. 5: *Reinforcement Learning*, *Goal-Oriented Architectures* e *Adaptive Control Mechanisms*) e analisa três paradigmas arquiteturais na Seção IV.A (Fig. 3, p. 9):
    1. **Multi-Agent Systems (MAS):** Coordenação descentralizada ou cooperativa de múltiplos agentes autônomos para decomposição de problemas complexos;
    2. **Hierarchical Reinforcement Learning (HRL):** Decomposição de objetivos complexos em hierarquias de políticas gerenciais (*high-level*) e operacionais (*low-level*);
    3. **Goal-Oriented Modular Architectures:** Separação modular entre percepção, planejamento, memória e execução para facilitar manutenção e adaptação.
  - **Avanços Metodológicos em Agentes Baseados em LLMs e Ferramentas (Seção IV.C–E, Fig. 2, Tabela 6, pp. 6–8, 10):** Sintetiza capacidades modernas de agentes (Fig. 2, p. 7 e Tabela 6, p. 10), incluindo *Reasoning and Planning*, *Tool Use and Integration*, *Memory Architectures (Episodic & Semantic)*, *Retrieval-Augmented Generation (RAG)* e *Instruction Fine-Tuning*, além de listar plataformas e bibliotecas de desenvolvimento na Seção IV.E (pp. 7–8): *OpenAI Gym*, *Unity ML-Agents*, *TensorFlow Agents*, *PyMARL* e *Rasa*.
  - **Sistemas de Software Adaptativos ("Living Software Systems") e Cibersegurança (Seção V.C, Tabela 7, pp. 10–11):** Discute o emprego de *Agentic AI* na construção de sistemas de software autoadaptativos capazes de reconfigurar parâmetros, alocar recursos em nuvem e detectar/mitigar ameaças de cibersegurança em tempo real.
  - **Limitação:** Embora aborde arquiteturas conceituais (*MAS, HRL*, memória episódica/semântica, *RAG*) e plataformas de simulação de *RL* (*OpenAI Gym, PyMARL*), o artigo não analisa em profundidade os frameworks contemporâneos de orquestração multiagente baseados em LLMs (como *AutoGen, LangGraph, CrewAI* ou *MetaGPT*) nem protocolos de comunicação inter-agentes (*MCP, A2A*).
- **Justificativa:** Apresenta boa cobertura conceitual das arquiteturas *MAS/HRL* e módulos cognitivos, mas com detalhamento técnico superficial dos frameworks e protocolos modernos de orquestração de agentes LLM (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Taxonomia de Seis Métricas de Avaliação de *Agentic AI* (Seção VI.A, Tabela 8, pp. 11–12):** Define seis dimensões formais para comparação de sistemas agênticos: (1) *Adaptability* (velocidade e eficácia de ajuste a mudanças ambientais); (2) *Goal Achievement Efficiency* (taxa de sucesso, tempo de conclusão e consumo de recursos); (3) *Learning Rate and Convergence* (eficiência amostral e estabilidade de convergência); (4) *Robustness and Resilience* (tolerância a ruído, falhas de hardware/software e perturbações adversariais); (5) *Scalability* (capacidade de escalar número de agentes, tarefas e volume de dados); e (6) *User Satisfaction and Human-AI Collaboration Efficiency*.
  - **Estudos de Caso Qualitativos e Catálogo de *Benchmarks* (Seção VI.B–C, Tabela 9, pp. 11–14):** Analisa qualitativamente quatro domínios de aplicação na Seção VI.B (monitoramento de saúde em tempo real, *algorithmic trading*, suporte ao cliente em *e-commerce* e manutenção preditiva na manufatura inteligente) e cataloga na Tabela 9 (p. 14) os principais *datasets* e ambientes de *benchmark* por domínio: *MIMIC-III* e *PhysioNet* (saúde), *Yahoo Finance / NASDAQ Historical Data* (finanças), *CARLA* e *OpenAI Gym* (sistemas autônomos/robótica), *MultiWOZ* e *Amazon Customer Reviews* (atendimento ao cliente) e *NASA Prognostics Data Repository* (manutenção preditiva industrial).
  - **Limitação:** Por se tratar de uma revisão narrativa da literatura, o artigo não executa experimentos próprios nem reporta resultados numéricos comparativos (taxas de acerto, latência ou *throughput*) extraídos dos estudos primários.
- **Justificativa:** Sistematiza métricas de avaliação (Tabela 8) e *benchmarks* de referência (Tabela 9), mas carece de dados quantitativos empíricos (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Desafios Técnicos e Operacionais (Seção VII, Tabela 10, pp. 13–15):** Analisa quatro classes de limitações técnicas: (1) *Goal Alignment and Complexity* (especificação incorreta de recompensas, *reward hacking*, conflitos entre subobjetivos de curto e longo prazo); (2) *Environmental and Situational Adaptability* (*distributional shift* e eventos *black swan*); (3) *Resource Constraints* (alto custo computacional e energético de inferência e treinamento contínuo em borda); e (4) *Scalability* (sobrecarga exponencial de comunicação e coordenação em sistemas multiagentes).
  - **Implicações Éticas, Legais, de Privacidade e Cibersegurança (Seção VIII, Tabela 11, pp. 14–16):**
    - *Accountability and Responsibility:* O problema da **cadeia de responsabilidade da IA (*AI responsibility chain*)** quando decisões autônomas causam danos físicos ou financeiros (envolvendo desenvolvedores, operadores e proprietários);
    - *Bias, Fairness, and Transparency:* Opacidade de modelos profundos e amplificação de vieses históricos em loops autônomos;
    - *Privacy and Security Issues:* Vulnerabilidade de sistemas agênticos conectados a infraestruturas críticas contra **ataques cibernéticos, envenenamento de dados e manipulação adversarial**, propondo o uso de **privacidade diferencial (*differential privacy*)** e **computação segura multipartidária (*secure multi-party computation — MPC*)**;
    - *Regulatory and Legal Perspectives:* Aponta que marcos regulatórios atuais como o **GDPR** não foram projetados para decisões autônomas adaptativas em tempo real, exigindo avaliações de risco contínuas, auditorias periódicas e certificações de conformidade.
  - **Frameworks de Governança, Segurança e Controle Humano (Seção IX, Tabela 12, pp. 15–17):** Propõe diretrizes estruturadas para desenvolvimento seguro de *Agentic AI*:
    - *Goal Safety Protocols, Fail-Safe Mechanisms & Ethical Guardrails* (limites operacionais rígidos e desligamento seguro em caso de violação de restrições);
    - Supervisão **HITL** e **HOTL** combinada com **Override Protocols / Last-Line Defense Systems** (Seção IX.B, p. 16);
    - *Explainable AI (XAI)*, **trilhas de auditoria imutáveis (*audit trails*)** e **algoritmos autodocumentados (*self-documenting algorithms*)** para rastreabilidade pós-incidente (Seção IX.C, p. 16);
    - Análise de quatro frameworks institucionais na Seção IX.D (pp. 16–17): *Microsoft Responsible AI Standard & Aether Committee*, *Google AI Principles & Model Cards*, *OpenAI Charter & Safety Standards* e *IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems*.
- **Justificativa:** Oferece uma discussão muito completa sobre riscos técnicos (*reward hacking*, escalabilidade), segurança/privacidade (*MPC*, privacidade diferencial), lacunas regulatórias (*GDPR*, cadeia de responsabilidade) e mecanismos de governança (*HITL/HOTL*, *override protocols*, *audit trails* e padrões da indústria) (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Agenda de Pesquisa Futura em Dez Eixos (Seção X.A–J, Tabelas 13 e 14, pp. 17–22):** Constrói um *roadmap* detalhado para a evolução da *Agentic AI*:
    1. *Meta-Learning and Transfer Learning:* Adaptação rápida (*few-shot*) a novos domínios sem retreinamento completo;
    2. *Value Alignment via Inverse Reinforcement Learning (IRL) & Cooperative IRL (CIRL):* Inferência dinâmica de valores e preferências humanas a partir de demonstrações colaborativas;
    3. **Mecanismos de Autorrecuperação (*Self-Recovery Mechanisms*) e Aprendizado em Tempo Real:** Destaca arquiteturas resilientes a falhas de hardware/software (citando a técnica **STRAIT** para tolerância a falhas em aceleradores de IA, p. 18) e adaptação em tempo real para **defesa em guerra cibernética (*cyber warfare*)** e mercados financeiros de alta frequência;
    4. *Context-Aware and Multi-Modal Learning:* Fusão de visão, áudio, linguagem e telemetria de sensores;
    5. *Hierarchical and Decentralized / Swarm Control:* Coordenação de enxames multiagentes resilientes sem ponto único de falha;
    6. *Edge AI, Quantization, and Neuromorphic Hardware:* Execução de agentes autônomos com baixa potência em dispositivos de borda;
    7. *Global AI Coordinating Entity & Adaptive Regulatory Regimes:* Criação de órgãos internacionais de governança e padrões dinâmicos de certificação;
    8. **Avanços Teóricos em Agência de IA (Seção X.J, pp. 21–22):** Investigação de **curiosidade intrínseca (*intrinsic motivation*)**, procedimentos de **autorrecompensa (*self-rewarding procedures*)**, raciocínio moral computacional, **autoconsciência operacional (*self-awareness*)**, **metacognição** e modelos matemáticos formais de agência.
- **Justificativa:** Apresenta um *roadmap* prospectivo extenso (Tabelas 13 e 14), abrangendo desde tolerância a falhas em nível de hardware (*STRAIT*) e defesa cibernética autônoma até alinhamento cooperativo (*CIRL*) e metacognição (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 0.5 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P10 |
| **Autores** | Deepak Bhaskar Acharya; Karthigeyan Kuppan; B. Divya |
| **Ano** | 2025 |
| **Título** | *Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 13, pp. 18912–18936 |
| **DOI** | `10.1109/ACCESS.2025.3532853` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | *Survey* / Revisão Abrangente da Literatura (101 referências, 14 tabelas) |
| **Domínio Principal** | Inteligência Artificial Agêntica (*Agentic AI*): Fundamentos, Arquiteturas, Governança (*HITL/HOTL*), Ética e Direções Futuras |
| **Tecnologias / Frameworks Analisados** | *Multi-Agent Systems (MAS)*, *Hierarchical Reinforcement Learning (HRL)*, *Inverse RL (IRL) / Cooperative IRL (CIRL)*, *RAG*, Memória Episódica e Semântica, *OpenAI Gym*, *Unity ML-Agents*, *TensorFlow Agents*, *PyMARL*, *Rasa*, *STRAIT* (tolerância a falhas), *Differential Privacy*, *Secure Multi-Party Computation (MPC)* |
| **Escopo de Aplicação** | Sistemas de software adaptativos (*"living software systems"*) e detecção adaptativa de ameaças cibernéticas (Seção V.C, Tabela 7), saúde (*MIMIC-III*), finanças, robótica/veículos autônomos (*CARLA*) e manufatura inteligente (*NASA Prognostics*) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Três matrizes comparativas (Tabelas 1–3, pp. 4, 7: *Traditional AI vs. Agentic AI*, *Classical vs. RL vs. Agentic AI* e *Traditional Agents vs. Agentic AI*); três pilares de complexidade (Seção III, Tabelas 4–5); distinção entre supervisão **HITL** e **HOTL** (Seção IX.B, p. 16). |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Arquiteturas *MAS*, *HRL* e modulares orientadas a metas (Seção IV.A, Fig. 3, p. 9); módulos de raciocínio, uso de ferramentas, memória episódica/semântica e *RAG* (Fig. 2, Tabela 6, pp. 7, 10); ferramentas de simulação (*OpenAI Gym, PyMARL, TF Agents*, pp. 7–8) e *living software systems* (Seção V.C, p. 10). Sem análise detalhada de frameworks LLM modernos (*AutoGen/LangGraph*) ou protocolos (*MCP/A2A*). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Definição de 6 métricas comparativas de avaliação (Tabela 8, p. 12: *Adaptability, Goal Achievement Efficiency, Learning Rate, Robustness, Scalability, User Satisfaction*) e catálogo de *benchmarks* por domínio (Tabela 9, p. 14: *MIMIC-III, CARLA, MultiWOZ, NASA Prognostics*). Sem experimentos ou dados quantitativos primários. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Desafios técnicos (Seção VII, Tabela 10: desalinhamento de metas, restrições de recursos, escalabilidade); implicações éticas, cibersegurança (*MPC*, privacidade diferencial) e limites do *GDPR* (Seção VIII, Tabela 11); frameworks de governança com **HITL/HOTL**, **override protocols**, **audit trails**, *self-documenting algorithms* e padrões *Microsoft/Google/OpenAI/IEEE* (Seção IX, Tabela 12, pp. 15–17). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | *Roadmap* em 10 eixos (Seção X, Tabelas 13–14, pp. 17–22): *meta/transfer learning*, alinhamento de valores via *IRL/CIRL*, **autorrecuperação (*self-recovery*, *STRAIT*)** e resposta em tempo real para guerra cibernética, controle de enxames, *Edge AI*/hardware neuromórfico, regulação global e teoria de agência (motivação intrínseca, *self-rewarding*, metacognição). |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Alta Aderência (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `P` | `0.5` | Define claramente os objetivos e o escopo temático do *survey* na Seção I.C (p. 2), mas não explicita critérios formais de inclusão e exclusão bibliográfica. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | Revisão narrativa tradicional: não documenta bases de dados consultadas, *strings* de busca booleana, período de coleta nem fluxograma de seleção (PRISMA). |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza 101 referências por meio de **14 tabelas estruturadas** (Tabelas 1–14) e apresenta uma análise crítica qualitativa de sucessos, limitações e lições aprendidas na Seção VI.D (p. 13), mas não aplica avaliação formal de qualidade metodológica aos estudos primários. |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | As conclusões são consistentes com a revisão narrativa apresentada, porém o artigo apresenta repetição estrutural parcial de subtópicos entre as Seções X.A–E e X.F–I (pp. 17–21), indicando menor rigor de edição na seção final. |
| **Total (`SCORE_QA`)** | **Banda: Baixa** | **1.5 / 4.0** | **Qualidade Metodológica de Revisão Narrativa (37,5%)** |

---

## Parecer Final do Revisor

O artigo **P10** (Acharya, Kuppan & Divya, 2025), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, apresenta alta aderência temática às questões de pesquisa da RSL (`SCORE_RQ = 4.0 / 5.0`), embora possua pontuação metodológica DARE na banda **Baixa** (`SCORE_QA = 1.5 / 4.0`) por constituir um *survey* narrativo sem protocolo sistemático de busca e seleção. Sua principal contribuição para a nossa revisão reside nas **três tabelas comparativas de evolução de agentes** (Tabelas 1–3, pp. 4, 7), na discussão sobre **sistemas de software adaptativos ("living software systems")** (Seção V.C, p. 10), e, sobretudo, na sistematização dos mecanismos de **governança e segurança operacional** (Seções VIII–IX, Tabelas 11–12), incluindo a distinção formal entre **Human-in-the-Loop (HITL)** e **Human-on-the-Loop (HOTL)** com **protocolos de *override* de última linha**, **trilhas de auditoria (*audit trails*)**, **algoritmos autodocumentados** e mecanismos de **autorrecuperação (*self-recovery*, *STRAIT*)** (Seção X.C, p. 18).
