# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P06
- **Arquivo PDF avaliado:** `P06-A1-Agentic AI A Comprehensive Survey of Technologies Applications and Societal Implications.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo apresenta um *survey* abrangente sobre **Agentic AI**, diferenciando-a tanto da IA tradicional/assistiva quanto de agentes de IA isolados (*AI agents vs. Agentic AI*), detalhando o ciclo operacional em quatro fases (*Data collection, Decision-making, Learning, Collaboration*), a classificação de agentes por arquitetura, interação e domínio (incluindo *Tactical AI agents* para resposta a emergências e *Orchestrator AI agents*), arquiteturas cognitivas (*BDI, SOAR, ACT-R*), aplicações em TI e Cibersegurança, impactos socioeconômicos e desafios de escalabilidade, interpretabilidade e segurança.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em julho de 2025 no periódico *IEEE Access*, Volume 13, pp. 151824–151837 (Recebido em 1 de junho de 2025; Aceito em 30 de junho de 2025; Publicado em 3 de julho de 2025; Versão atual de 4 de setembro de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão publicado em periódico científico com revisão por pares (*IEEE Access*), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 14 páginas em inglês com análise conceitual, metodológica, aplicacional e ética de *Agentic AI*.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Distinção entre IA Tradicional/Assistiva e *Agentic AI* (Seção I.A, Tabela 1, pp. 1–2):** Define a transição da IA assistiva (ex.: CNNs que classificam imagens sob supervisão e retreinamento humano manual) para a *Agentic AI* caracterizada pela **proatividade** (*proactivity*) — capacidade de antecipar, iniciar e agir autonomamente rumo a objetivos. A Tabela 1 (p. 2) contrasta *Traditional AI* e *Agentic AI* em seis dimensões: *Task assignment* (executa tarefa atribuída vs. resolve a tarefa em lugar do humano), *Autonomy*, *Learning capability* (limitada aos dados de treino vs. contínua e evolutiva), *Behavior* (reativo vs. proativo), *Input dependency* (entrada manual vs. autoiniciada) e *Scope* (tarefa única vs. fluxos de trabalho orquestrados).
  - **Desambiguação hierárquica entre *AI Agents* e *Agentic AI* (Seção I.B, Tabela 2, p. 2):** Utiliza a metáfora arquitetural de *"tijolos vs. a casa inteira"* (*"Think of AI agents as bricks and agentic AI as the entire house"*): enquanto agentes de IA são componentes especializados em tarefas únicas e isoladas, a *Agentic AI* é o sistema autônomo unificado que orquestra dinamicamente múltiplos agentes e interage com usuários humanos. A Tabela 2 (p. 2) sistematiza essa diferença em *Task complexity*, *System Architecture*, *Autonomy level*, *Coordination strategy* e *Learning Mechanism*.
  - **Tríade Fundamental e Ciclo Operacional em 4 Fases (Seção III.A–B, Figs. 1–2, pp. 4–5):** Formaliza a tríade central da IA agêntica (*Autonomy, Adaptability, Goal-Directedness*, Fig. 1, p. 4) e seu loop autossustentável de quatro fases (Fig. 2, p. 5): *Step 1: Data collection* $\to$ *Step 2: Decision Making* $\to$ *Step 3: Learning* $\to$ *Step 4: Collaboration* (sinergia multiagente e humano-IA).
- **Justificativa:** Estabelece com clareza didática e tabelas comparativas (Tabelas 1 e 2) os fundamentos conceituais de *Agentic AI*, a distinção frente a agentes singulares e o papel da colaboração humano-IA.

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Taxonomia tripla de classificação de agentes (Seção III.C, Fig. 3, pp. 5–6):** Classifica os agentes em três eixos: (1) *Architecture-based* (*Reflex, Model-based, Goal-based, Utility-based, Learning* e *Meta-reasoning agents*); (2) *Interaction-based* (*Simple independent agents, Multi-Agent Systems [MAS] hierárquicos ou peer-to-peer, Swarm Agents* e *Human-AI collaborative agents*); e (3) *Application-based* (*Industrial, Social, Tactical AI agents* — voltados a resposta rápida a emergências e defesa/segurança em coordenação com operadores humanos —, *Orchestrator agents* e *Scientific AI agents*).
  - **Tecnologias habilitadoras e arquiteturas cognitivas clássicas (Seção IV.A–B, pp. 6–7):** Revisa o papel de *NLP/LLMs* (*Claude*, *Whisper*), *RL*, *Inverse Reinforcement Learning (IRL)*, *Imitation Learning* (*Behavioral Cloning* e *DAgger*), *MAS/Swarm* (*JADF*, *ACO*, *PSO*), integração neuro-simbólica, grafos de conhecimento, planejamento clássico (*STRIPS*, *HTN*) e arquiteturas cognitivas formais (**BDI**, **SOAR** e **ACT-R**), além de ambientes de simulação (*Unity ML-Agents*, *OpenAI Gym*, *Mesa*).
  - **Limitação:** Embora mencione nominalmente frameworks modernos na revisão de literatura (ex.: *LangGraph*, *AutoGen*, *OpenAI Swarm* ao citar Joshi [13] na p. 3, e *BabyAGI* na p. 11), a análise técnica da Seção IV concentra-se em arquiteturas cognitivas clássicas (*BDI, SOAR, ACT-R*) e RL, sem detalhar protocolos modernos de orquestração de agentes baseados em LLMs.
- **Justificativa:** Apresenta boa taxonomia arquitetural (Fig. 3) e revisão de arquiteturas cognitivas (*BDI, SOAR, ACT-R*), mas aborda superficialmente as arquiteturas modernas de orquestração multiagente baseadas em LLMs (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Indicadores quantitativos secundários e métricas conceituais (Seção I.A, p. 2; Seção IV.B.3, p. 7; Seção VI.A, p. 9):**
    - Cita na Seção I.A (p. 2, ref. [2]) dados coletados junto a cerca de `500 organizações` indicando que sistemas de *Agentic AI* proporcionam **`34,2%` de redução no tempo de conclusão de tarefas**, **`7,7%` de aumento na acurácia** e **`13,6%` de melhoria na utilização de recursos** em comparação à IA convencional;
    - Define cinco categorias conceituais de métricas de avaliação na Seção IV.B.3 (p. 7): *Robustness*, *Scalability*, *Safety*, *Task completion rate* e *Communication efficiency* (largura de banda e latência na coordenação);
    - Na Seção V.D (pp. 8–9), descreve aplicações em **TI e Cibersegurança** (monitoramento contínuo de ameaças, bloqueio proativo de transações fraudulentas, manutenção preditiva de falhas de hardware/software e resposta automatizada a ameaças cibernéticas via *Agentic AI* e *RL*, citando Kshetri [43] e Katnapally et al. [44]);
    - Cita estatísticas de impacto laboral na Seção VI.A.1 (p. 9, refs. [25, 95]): `10,6%` dos trabalhadores sob alto risco de automação e `44,4%` das mulheres na força de trabalho remunerada sob risco moderado a alto de transformação ocupacional.
  - **Limitação:** Não conduz experimentos primários nem apresenta tabelas comparativas de desempenho empírico de sistemas de resposta a incidentes.
- **Justificativa:** Reporta métricas agregadas secundárias relevantes (`-34,2%` no tempo de tarefa, `+7,7%` em acurácia, `+13,6%` em uso de recursos) e define métricas conceituais de avaliação, mas sem validação experimental própria (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Riscos éticos, perda de controle humano e lacuna de responsabilização (Seção VI.B, pp. 9–10):** Analisa a amplificação de vieses em agentes auto-aperfeiçoáveis (*self-improving agents*), o dilema jurídico da **lacuna de responsabilização (*accountability gap*)** quando decisões autônomas causam danos (desenvolvedor, implantador, usuário ou agente) e o risco de perda de controle humano devido a decisões finais tomadas em microssegundos sem supervisão.
  - **Escalabilidade, opacidade (*black-box*) e atribuição de culpa em MAS (Seção VII.A, p. 10):** Examina a complexidade computacional e de coordenação em enxames de agentes e destaca o problema de **interpretabilidade e rastreabilidade em sistemas multiagentes**: quando múltiplos agentes interagem como caixas-pretas (*DL/RL*), torna-se difícil rastrear a cadeia causal e identificar qual agente específico é responsável por uma decisão errônea.
  - **Ameaças de segurança e mecanismos de governança/auditoria (Seção VII.A–B, pp. 10–11):** Discute ataques adversariais, vazamento de dados confidenciais e o risco de a própria autonomia do agente contornar controles de segurança (*bypass security measures*) ao acessar bancos de dados diretamente. Como contramedidas de governança, destaca: defesas em múltiplas camadas, trilhas de auditoria imutáveis baseadas em **blockchain** para decisões de IA (citando Kulothungan [123]), kits de equidade como *IBM AI Fairness 360* [103], *Explainable Security* [109] e o conceito de **AI Guardians** (agentes supervisores dedicados a monitorar e fiscalizar o comportamento de outros agentes autônomos, citando Kolluri [110], p. 11).
- **Justificativa:** Cobre de forma abrangente os riscos éticos, laborais, de segurança (contorno autônomo de barreiras, acesso direto a bancos de dados), opacidade multiagente e mecanismos de governança (*blockchain audit trails*, *AI Guardians*, *XRL*) (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Oito Problemas Abertos e Tendências Emergentes (Seção VII.B, pp. 10–11):** Estrutura uma agenda clara de pesquisa futura:
    1. *Transparent Agentic AI* (modelagem de relações causais verdadeiras causa-efeito);
    2. *Neuro-symbolic Hybrid Agents* (integração de redes neurais com lógica simbólica para raciocínio interpretável, ex.: *LogiCity*);
    3. *Multi-agent Cooperation and Negotiation* (otimização de comunicação em redes cooperativas-competitivas mistas);
    4. *Human-AI Collaboration* (agentes adaptativos ao *feedback*, comportamento e emoção humana);
    5. *Energy-efficient Agent Architectures* (*Edge AI*, *AdderNet*);
    6. *Simulation-to-Real Transfer (Sim2Real)*;
    7. *Quantum Computing* (*Quantum MARL* para escalabilidade);
    8. *Robustness against Adversarial Attacks*, complementada por *Decentralised Autonomous Organisations (DAOs)*, *AI-as-a-Service (AIaaS)*, *Explainable Reinforcement Learning (XRL)* e *AI Guardians*.
- **Justificativa:** Mapeia de maneira sistemática as lacunas da literatura existente (Tabela 3, p. 3) e articula oito direções tecnológicas claras para a evolução segura de sistemas agênticos (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 0.5 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P06 |
| **Autores** | Ashis Kumar Pati |
| **Ano** | 2025 |
| **Título** | *Agentic AI: A Comprehensive Survey of Technologies, Applications, and Societal Implications* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 13, pp. 151824–151837 |
| **DOI** | `10.1109/ACCESS.2025.3585609` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Artigo de Revisão (*Comprehensive Survey* / Revisão Conceitual e Taxonômica com 129 referências) |
| **Domínio Principal** | *Agentic AI*: Fundamentos, Tecnologias Habilitadoras, Aplicações Multissetoriais (incluindo TI/Cibersegurança) e Implicações Societais/Éticas |
| **Tecnologias / Frameworks Analisados** | Arquiteturas cognitivas (*BDI*, *SOAR*, *ACT-R*), *RL* / *IRL* / *Imitation Learning (Behavioral Cloning, DAgger)*, *JADF*, *Unity ML-Agents*, *OpenAI Gym*, *Mesa*, *STRIPS*, *HTN*, *IBM AI Fairness 360*, *AI Guardians*, menção a *LangGraph*, *AutoGen*, *OpenAI Swarm*, *Claude*, *Whisper* e *BabyAGI* |
| **Escopo de Aplicação** | Robótica e *cobots*, saúde e diagnóstico, veículos autônomos, finanças, educação, suporte ao cliente, **TI e Cibersegurança** (monitoramento e resposta automatizada a ameaças, Seção V.D) e cadeia de suprimentos |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Diferenciação entre *Traditional/Assistive AI* e *Agentic AI* (Seção I.A, Tabela 1, p. 2) e entre *AI Agents* ("tijolos") e *Agentic AI* ("casa inteira", Seção I.B, Tabela 2, p. 2); tríade *Autonomy, Adaptability, Goal-Directedness* (Fig. 1, p. 4) e loop em 4 fases (Fig. 2, pp. 4–5). |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Classificação de agentes por arquitetura, interação (*MAS*, *Swarm*, *Human-AI*) e aplicação (*Tactical*, *Orchestrator*, Fig. 3, pp. 5–6); análise de arquiteturas cognitivas (*BDI, SOAR, ACT-R*) e simuladores (*Unity ML, OpenAI Gym, Mesa*, Seção IV, pp. 6–7). Cobertura superficial de frameworks modernos baseados em LLMs. |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Citação de estudo em `~500 organizações` com `-34,2%` no tempo de conclusão de tarefas, `+7,7%` em acurácia e `+13,6%` em utilização de recursos (p. 2); definição de métricas de avaliação (p. 7); discussão qualitativa de resposta a ameaças em TI/Cibersegurança (pp. 8–9). |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Riscos éticos, viés, deslocamento laboral e *accountability gap* (Seção VI, pp. 9–10); dificuldade de rastrear culpa entre múltiplos agentes *black-box*, risco de autonomia contornar barreiras de segurança e expor bancos de dados, auditoria via *blockchain* e *AI Guardians* (Seção VII.A–B, pp. 10–11). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Comparação de lacunas em 11 *surveys* prévios (Tabela 3, p. 3) e agenda de 8 frentes abertas: *Transparent/Causal Agentic AI*, *Neuro-symbolic agents*, *MAS negotiation*, *Human-AI collaboration*, *Energy-efficient architectures*, *Sim2Real*, *Quantum MARL* e *Adversarial robustness* / *AI Guardians* (Seção VII.B, pp. 10–11). |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Aderência Muito Forte (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `P` | `0.5` | A Seção I.C (p. 2) e a Seção II.A (pp. 2–4) delimitam claramente as cinco lentes temáticas do estudo (fundamentos, metodologias, aplicações, impacto societal e desafios/oportunidades) e comparam o escopo do artigo frente a 11 revisões recentes (2023–2025) na Tabela 3 (p. 3), mas não definem critérios formais de inclusão/exclusão bibliográfica. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | Trata-se de uma revisão narrativa/conceitual que não explicita as bases de dados consultadas, as *strings* de busca utilizadas, o período de coleta nem o processo de triagem das 129 referências. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Avalia comparativamente 11 *surveys* concorrentes atribuindo níveis qualitativos de cobertura (`ID` = *In-Depth*, `BC` = *Basic Coverage*, `ND` = *Not Discussed*) ao longo de 10 dimensões na Tabela 3 (p. 3) e sintetiza 129 referências, porém sem avaliação formal da qualidade metodológica dos estudos primários e com algumas referências secundárias incompletas (ex.: ref. [2] na p. 11 sem periódico/conferência). |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões e a síntese de contribuições (Seções VIII e IX, p. 11) são consistentes com a análise conceitual, taxonômica e socioética desenvolvida ao longo do artigo. |
| **Total (`SCORE_QA`)** | **Banda: Média** | **2.0 / 4.0** | **Qualidade Metodológica Moderada (50,0%)** |

---

## Parecer Final do Revisor

O estudo **P06** (Pati, 2025), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, apresenta forte aderência temática às questões de pesquisa da RSL (`SCORE_RQ = 4.0 / 5.0`) e qualidade metodológica moderada segundo os critérios DARE (`SCORE_QA = 2.0 / 4.0`, banda **Média**, típica de *surveys* conceituais sem protocolo PRISMA). Suas contribuições mais valiosas para a nossa revisão concentram-se na desambiguação conceitual entre *Traditional AI*, *AI Agents* e *Agentic AI* (Tabelas 1 e 2, p. 2), na classificação de agentes táticos e orquestradores (Fig. 3, p. 5) e na análise dos riscos de perda de rastreabilidade causal em sistemas multiagentes *black-box*, contorno autônomo de controles de segurança e uso de **AI Guardians** e trilhas de auditoria em *blockchain* para governança de agentes autônomos (Seção VII, pp. 10–11).
