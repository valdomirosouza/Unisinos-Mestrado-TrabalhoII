# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P03
- **Arquivo PDF avaliado:** `P03-A2-A Research Landscape of Agentic AI and Large Language Models Applications, Challenges and Future Directions.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A2
- **Quartil SJR (pré-verificado no protocolo):** Q2

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo investiga de forma sistemática a convergência entre *Large Language Models (LLMs)* e *Agentic AI*, estruturando o ciclo fechado de operação agêntica (*perception, reasoning, action, learning, collaboration*), aplicações setoriais (incluindo cibersegurança e automação de *SOC*), desafios herdados dos LLMs versus desafios exclusivos de sistemas agênticos, e uma taxonomia de oito direções futuras de pesquisa.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em agosto de 2025 no periódico *Algorithms* (MDPI), Volume 18, Artigo 499 (Recebido em 1 de julho de 2025; Revisado em 4 de agosto de 2025; Aceito em 6 de agosto de 2025; Publicado em 11 de agosto de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão de escopo (*scoping review*) publicado em periódico científico revisado por pares (*Algorithms*, MDPI), classificado como **Qualis A2** e **SJR Q2** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 29 páginas em inglês com protocolo metodológico documentado e análise técnica approfondada.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Distinção conceitual entre LLMs isolados e *Agentic AI* baseada em LLMs (Seção 1, pp. 2–4; Seção 3, p. 9):** O estudo estabelece que, enquanto os LLMs tradicionais operam como motores passivos de geração textual baseados em *prompts*, os sistemas de *Agentic AI* utilizam o LLM como núcleo cognitivo de raciocínio (*LLM Reasoning Core*) integrado a memória persistente, planejamento, decomposição de subtarefas, invocação de ferramentas externas/APIs e aprendizado contínuo em malha fechada (*perceive, reason, act, learn, collaborate*).
  - **Fluxo de interação *Human-in-the-Loop* e decomposição de objetivos (Seção 1, Fig. 3, p. 3):** Demonstra arquiteturalmente como um objetivo de alto nível do usuário passa pelo orquestrador agêntico e pelo núcleo de raciocínio LLM, que solicita esclarecimentos ao humano (*human-in-the-loop clarification*) quando há ambiguidade antes de delegar subtarefas a agentes executores especializados.
  - **Progressão de *Co-pilot* para *Autopilot* e controle de iniciativa mista (Seção 3.4, p. 11; Seção 5.4, p. 23):** Analisa a evolução gradual de sistemas assistivos (*co-pilots*) para sistemas autônomos (*autopilots*) e formaliza o paradigma de **Mixed-Initiative Systems** (*Collaborative Agents*), nos quais o controle decisório é compartilhado e transferido dinamicamente entre agentes e operadores humanos conforme o risco e a incerteza da tarefa.
- **Justificativa:** Caracteriza com precisão teórica e diagramática o acoplamento entre LLMs e arquiteturas agênticas, bem como os mecanismos de supervisão humana e transição *co-pilot* $\to$ *autopilot*.

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Arquitetura em camadas para execução agêntica (Seção 1, Fig. 3, p. 3):** Apresenta uma arquitetura de referência estruturada em cinco níveis: (1) *User Layer* (definição de metas e esclarecimento interativo); (2) *Agentic AI Orchestrator Layer* (gerenciamento de contexto, memória local e coordenação); (3) *LLM Reasoning Core Layer* (interpretação semântica, planejamento e decomposição de tarefas); (4) *Agentic Execution Layer* (agentes especializados operando em paralelo/sequência: *Search Agent*, *Filtering Agent*, *Booking Agent*, *Agent...N*); e (5) *External Services Layer* (integração com APIs, serviços web, ferramentas e fontes de dados).
  - **Infraestrutura de memória e integração corporativa (Seção 3.6, p. 12; Seção 5.5, p. 24):** Discute a integração de agentes com bancos de dados vetoriais (*Pinecone*, *Elasticsearch*) e plataformas corporativas de CRM (*Salesforce*), além de especificar componentes arquiteturais para *Memory-Aware Agents* (redes neurais aumentadas por memória, bancos vetoriais e arquiteturas híbridas de memória de curto e longo prazo, p. 24) e *Trustworthy Agents* (execução em *sandbox*, credenciais com escopo restrito e verificação em tempo de execução, pp. 21–22).
  - **Limitação:** Não analisa nem compara diretamente frameworks de engenharia de agentes (como *LangGraph*, *CrewAI*, *AutoGen*) nem protocolos padronizados de comunicação inter-agentes (como *MCP* ou *A2A*).
- **Justificativa:** Fornece uma arquitetura conceitual em camadas clara e discute memória híbrida e *sandboxing*, mas sem detalhamento de frameworks ou protocolos de implementação (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Aplicações em Cibersegurança e resposta autônoma a incidentes (Seção 3.3, p. 10):** Analisa o emprego de *Agentic AI* em operações de segurança cibernética para detecção de ameaças em tempo real, avaliação de incidentes, priorização de riscos e contenção/remediação automatizada (revogação autônoma de credenciais comprometidas, isolamento de ativos e aplicação de *patches* de vulnerabilidade), destacando implementações industriais da **ReliaQuest** e da **CrowdStrike** para automação de triagem de alertas e redução da fadiga de analistas em *SOCs*.
  - **Outras aplicações setoriais e métricas secundárias (Seção 3.1–3.6, pp. 9–12):** Documenta aplicações em saúde (citando o modelo *Med-Flamingo* com ganho de até `20%` na acurácia diagnóstica clínica, Seção 3.2, p. 10), educação (*Khanmigo*, Seção 3.1), veículos autônomos (Seção 3.4), comércio eletrônico (Seção 3.5) e atendimento ao cliente (Seção 3.6).
  - **Demonstrações empíricas qualitativas com *GPT-4o* e *DeepSeek-R1* (Seção 4.2, Figs. 9–14, pp. 13–16; Seção 4.4, Figs. 15–20, pp. 18–20):** Os autores conduzem testes exploratórios longitudinais (3 dias consecutivos: 23–25 de maio de 2025 e 15–17 de junho de 2025) comparando respostas do *GPT-4o* e do *DeepSeek-R1* a *prompts* sobre disputas geopolíticas e inclusão cultural, evidenciando variações de enquadramento e viés. Contudo, não há *benchmarks* quantitativos de desempenho operacional em resposta a incidentes.
- **Justificativa:** Inclui discussão direta de resposta automatizada a incidentes cibernéticos (*ReliaQuest*, *CrowdStrike*) e demonstrações empíricas qualitativas sobre comportamento de LLMs, mas sem métricas primárias de eficiência operacional ou *MTTR* (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia em dois níveis de riscos — Desafios herdados dos LLMs vs. Desafios exclusivos de *Agentic AI* (Seções 4 e 5, Tabelas 1 e 2, pp. 12–25):** O artigo realiza uma separação analítica rigorosa entre vulnerabilidades do modelo base e riscos emergentes da autonomia agêntica:
    1. **Cinco desafios fundamentais dos LLMs (Seção 4, Tabela 1, pp. 12–21):**
       - *Security, Privacy, and Trust* (Seção 4.1, pp. 12–13): extração de dados de treinamento, vazamento de *system prompts* (*PLeak*), *prompt injection*, ataques de evasão, envenenamento de dados (*data poisoning*) e lacunas regulatórias no *EU AI Act* e *NIST AI RMF*;
       - *Misinformation, Misuse, and Bias* (Seção 4.2, pp. 13–17): alucinações, viés sociopolítico demonstrado empiricamente em *GPT-4o* vs. *DeepSeek-R1* e viés demográfico em triagem de currículos (citando preferência de `85%` por nomes associados a candidatos brancos e apenas `11%` de seleção feminina em [61], p. 16);
       - *Energy Demands* (Seção 4.3, pp. 17–18): consumo energético de treinamento (ex.: *GPT-3 175B* consumindo `1.287 MWh` e emitindo `552 toneladas métricas de CO2e`) agravado pela inferência contínua multiagente;
       - *Value Misalignment & Exclusion* (Seção 4.4, pp. 18–20): homogeneização cultural ocidental e exclusão linguística;
       - *Explainability & Transparency Gaps* (Seção 4.5, pp. 20–21): infidelidade de cadeias de pensamento (*Chain-of-Thought*), citando Turpin et al. [75] e o estudo da Apple *“The Illusion of Thinking”* de Shojaee et al. [77] sobre colapso de raciocínio em alta complexidade.
    2. **Oito desafios críticos de *Agentic AI* (Seção 5, Tabela 2, pp. 21–25):** (i) *Security, Privacy & Trust* (abuso de ferramentas externas, exfiltração de dados via APIs e propagação de falhas entre agentes); (ii) *Goal Misalignment* (*reward hacking* e interpretação literal perigosa de metas); (iii) *Opaque Decision-Making* (opacidade em políticas de ação multi-etapas); (iv) *Limited Human Oversight* (perda de controle em loops autônomos rápidos); (v) *Context Management* (esquecimento catastrófico e perda de estado em horizontes longos); (vi) *Multi-Agent Coordination* (conflitos de metas, *deadlocks* e comportamentos emergentes instáveis); (vii) *Long-Term Safety* (deriva comportamental ao longo do tempo); e (viii) *Ethical and Legal Accountability* (lacuna de responsabilidade jurídica em ações autônomas).
- **Justificativa:** Oferece uma das análises mais completas e bem estruturadas do corpus sobre riscos técnicos, segurança, infidelidade de raciocínio (*CoT*), desalinhamento de metas e governança de agentes autônomos (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Mapa estruturado de oito direções futuras de pesquisa (Fig. 4, p. 5; Tabela 1, p. 13; Tabela 2, p. 22; Seção 5.1–5.8, pp. 21–25):** Para cada desafio agêntico identificado, o artigo define uma classe correspondente de agentes de próxima geração e seus requisitos técnicos de pesquisa:
    1. **Trustworthy Agents (Seção 5.1):** ambientes de execução isolados (*sandboxing*), autenticação com escopo mínimo (*scoped credentials*), criptografia homomórfica/MPC e verificação formal em tempo de execução;
    2. **Aligned Agents (Seção 5.2):** *Inverse Reinforcement Learning (IRL)*, modelagem dinâmica de recompensas e *feedback* humano em tempo real;
    3. **Explainable Agents (Seção 5.3):** geração de justificativas em linguagem natural auditáveis, mapas de saliência e trilhas causais de decisão;
    4. **Collaborative Agents (Seção 5.4):** arquiteturas de iniciativa mista (*mixed-initiative*), *override* humano imediato e interfaces adaptativas de supervisão;
    5. **Memory-Aware Agents (Seção 5.5):** arquiteturas híbridas de memória episódica/semântica de curto e longo prazo com bancos vetoriais;
    6. **Cooperative Agents (Seção 5.6):** protocolos de negociação descentralizada, resolução de conflitos e governança compartilhada em enxames multiagentes;
    7. **Safe Agents (Seção 5.7):** aprendizado baseado em restrições (*constraint-based RL*), *benchmarks* de segurança de longo prazo e monitoramento contínuo de deriva;
    8. **Accountable Agents (Seção 5.8):** *logging* imutável de ações, proveniência de decisão (*decision provenance*) e modelos jurídicos de responsabilidade distribuída.
- **Justificativa:** Apresenta uma taxonomia prospectiva exaustiva, diretamente mapeada problema-a-solução nas Tabelas 1 e 2 (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 0.5 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P03 |
| **Autores** | Sarfraz Brohi; Qurat-ul-ain Mastoi; N. Z. Jhanjhi; Thulasyammal Ramiah Pillai |
| **Ano** | 2025 |
| **Título** | *A Research Landscape of Agentic AI and Large Language Models: Applications, Challenges and Future Directions* |
| **Periódico / Fonte** | *Algorithms* (MDPI), Vol. 18, Art. 499, pp. 1–29 |
| **DOI** | `10.3390/a18080499` |
| **Qualis** | A2 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q2 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão de Escopo (*Structured Scoping Review*) com análise bibliométrica (*VOSviewer*) e demonstrações empíricas exploratórias |
| **Domínio Principal** | *Agentic AI* e *Large Language Models (LLMs)*: Arquitetura Conceitual, Cibersegurança e Aplicações Setoriais, Segurança/Riscos e Agenda de Pesquisa |
| **Tecnologias / Frameworks Analisados** | *GPT-4o*, *DeepSeek-R1*, *GPT-3*, *Med-Flamingo*, *Khanmigo*, plataformas de *SOC* agêntico (*ReliaQuest*, *CrowdStrike*), bancos vetoriais (*Pinecone*, *Elasticsearch*), *Salesforce CRM*, *VOSviewer 1.6.20* |
| **Escopo de Aplicação** | Cibersegurança e resposta a incidentes (Seção 3.3), saúde (Seção 3.2), educação (Seção 3.1), veículos autônomos (Seção 3.4), e-commerce (Seção 3.5) e atendimento ao cliente (Seção 3.6) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Distinção entre LLMs isolados e *Agentic AI* operando em ciclo fechado (*perceive, reason, act, learn, collaborate*, Seções 1 e 3, pp. 2–4, 9); esclarecimento *human-in-the-loop* (Fig. 3, p. 3); transição *co-pilot* $\to$ *autopilot* e controle de iniciativa mista (Seções 3.4 e 5.4, pp. 11, 23). |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Arquitetura em 5 camadas com *Orchestrator Layer*, *LLM Reasoning Core* e *Agentic Execution Layer* (Fig. 3, p. 3); integração com bancos vetoriais (*Pinecone*, *Elasticsearch*, p. 12); diretrizes arquiteturais para memória híbrida e *sandboxing* (Seções 5.1 e 5.5, pp. 21–24). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Análise de automação de resposta a incidentes cibernéticos com *ReliaQuest* e *CrowdStrike* (Seção 3.3, p. 10); métricas secundárias (ex.: `+20%` acurácia diagnóstica com *Med-Flamingo*, p. 10); testes qualitativos longitudinais comparando *GPT-4o* e *DeepSeek-R1* (Figs. 9–20, pp. 14–20). |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Mapeamento sistemático de 5 desafios de LLMs (Tabela 1, pp. 12–21: *PLeak*, *prompt injection*, viés demográfico `85%` vs. `11%`, custo energético `1.287 MWh`, colapso de raciocínio *CoT*) e 8 desafios exclusivos de *Agentic AI* (Tabela 2, pp. 21–25: abuso de ferramentas, *goal misalignment*, opacidade, perda de supervisão humana, perda de contexto, conflitos multiagentes, segurança de longo prazo e responsabilidade legal). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Taxonomia de 8 classes de agentes futuros (Fig. 4, p. 5; Tabelas 1 e 2; Seção 5.1–5.8, pp. 21–25): *Trustworthy*, *Aligned*, *Explainable*, *Collaborative*, *Memory-Aware*, *Cooperative*, *Safe* e *Accountable Agents*. |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Aderência Muito Forte (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | A Seção 2 (pp. 5–7) define explicitamente os critérios de inclusão (estudos em inglês publicados entre 2020 e 2025 sobre LLMs, *Agentic AI*, desafios éticos/técnicos e aplicações) e de exclusão (artigos sem texto completo, fora do escopo ou sem rigor técnico/conceitual). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | A Seção 2 e as Figuras 5–8 (pp. 5–8) documentam de forma transparente um protocolo de revisão de escopo em 4 fases nas bases *Google Scholar*, *Scopus* e *arXiv* (2020–2025), detalhando as palavras-chave booleadas, o fluxo de seleção (`327` registros iniciais $\to$ `71` retidos após triagem de qualidade + `13` fontes manuais complementares = `84` fontes finais), a análise bibliométrica de coocorrência no *VOSviewer 1.6.20* (Fig. 6) e a distribuição temporal/tipológica do corpus (Figs. 7 e 8). |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | As 84 fontes são sintetizadas de maneira estruturada nas Tabelas 1 e 2 e ao longo das Seções 3–5. Os autores incluem ainda demonstrações empíricas próprias em *GPT-4o* e *DeepSeek-R1* (Figs. 9–20), reconhecendo explicitamente nas pp. 13 e 18 que tais testes têm caráter ilustrativo/exploratório e não constituem experimentos estatisticamente controlados; tampouco há escore individual de qualidade atribuído a cada um dos 84 estudos incluídos. |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões (Seção 6, p. 25) refletem fielmente as evidências mapeadas nas Tabelas 1 e 2, discutindo de forma equilibrada as limitações metodológicas de uma revisão de escopo e conectando diretamente os desafios identificados às oito frentes de pesquisa propostas. |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **3.5 / 4.0** | **Qualidade Metodológica Alta (87,5%)** |

---

## Parecer Final do Revisor

O estudo **P03** (Brohi et al., 2025), pertencente ao **Corpus Fundacional** do Trabalho I, apresenta alta qualidade metodológica (`SCORE_QA = 3.5 / 4.0`, banda **Alta**) e forte aderência às questões de pesquisa da RSL (`SCORE_RQ = 4.0 / 5.0`). Seu valor central para a nossa revisão reside na distinção analítica rigorosa entre vulnerabilidades herdadas dos LLMs de base (Seção 4, Tabela 1) e riscos emergentes exclusivos da autonomia agêntica (Seção 5, Tabela 2) — cobrindo RQ4 de forma integral (`T = 1.0`) — e no seu desdobramento direto em uma agenda estruturada de oito famílias de agentes futuros (*Trustworthy, Aligned, Explainable, Collaborative, Memory-Aware, Cooperative, Safe* e *Accountable Agents*), atendendo plenamente à RQ5 (`T = 1.0`), além de documentar o uso prático de IA agêntica em resposta a incidentes cibernéticos (*ReliaQuest* e *CrowdStrike*, Seção 3.3).
