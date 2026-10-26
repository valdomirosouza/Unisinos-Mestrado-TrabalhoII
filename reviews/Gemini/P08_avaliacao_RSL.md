# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P08
- **Arquivo PDF avaliado:** `P08-A1-Applications_Challenges_and_Future_Directions_of_Human-in-the-Loop_Learning.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido (Escopo Fundacional de Supervisão Humana e Colaboração Humano-IA — HITL).** O artigo realiza uma revisão abrangente sobre **Human-in-the-Loop (HITL) Learning**, examinando a transição da *Industry 4.0* (baseada em *Black-Box AI* com controle humano limitado) para a *Industry 5.0* e *Operator 5.0* (colaboração simbiótica humano-máquina para resiliência operacional, transparência e responsabilização), detalhando as metodologias de *Active Learning (AL)*, *HITL Reinforcement Learning / RLHF* e *Explainable AI (XAI)*, além de aplicações em raciocínio e gestão de anomalias (*ALARM1*), veículos autônomos, processamento de linguagem natural e serviços financeiros.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em maio de 2024 no periódico *IEEE Access*, Volume 12, pp. 75735–75760 (Recebido em 28 de abril de 2024; Aceito em 12 de maio de 2024; Publicado em 15 de maio de 2024; Versão atual de 4 de junho de 2024).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão publicado em periódico científico revisado por pares (*IEEE Access*), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 26 páginas em inglês com 207 referências.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Paradigma *Human-in-the-Loop (HITL)* e transição *Industry 4.0* $\to$ *Industry 5.0 / Operator 5.0* (Seção I, Fig. 1, pp. 1–3):** O artigo fundamenta o papel da supervisão e intervenção humana nos três estágios do pipeline de aprendizado (*data pre-processing, data modeling, process modification*, Fig. 1, p. 2) e contrasta a **Industry 4.0** (dependente de *Black-Box AI* com controle humano restrito) com a visão da **Industry 5.0** e **Operator 5.0**, que prioriza a resiliência da força de trabalho e a resiliência do sistema (*system resilience*) por meio de colaboração transparente e simbiótica entre operadores humanos e agentes inteligentes (p. 2).
  - **Espectro entre Agência Humana Completa e Automação Total e o *White-Box Paradox* (Seção III.C, pp. 9–10):** Analisa o contínuo entre agência humana total e automação completa (citando Lai & Tan [100], p. 9), demonstrando como diferentes níveis de assistência de máquina e protocolos de colaboração (*AI-first* vs. *human-first*, citando Cabitza et al. [109], p. 10) moldam os modelos mentais das equipes humano-IA, as fronteiras de erro (*error boundaries*: parcimônia e estocasticidade, citando Bansal et al. [101], p. 9) e o risco do **paradoxo da caixa-branca (*white-box paradox*)**, no qual explicações mal desenhadas podem produzir efeitos neutros ou contraproducentes na tomada de decisão conjunta.
- **Justificativa:** Fundamenta de forma sólida os modelos teóricos de colaboração humano-IA (*HITL*, *Operator 5.0*, *AI-first vs. human-first*, modelos mentais de fronteira de erro e calibração de agência humana), essenciais para compreender a transição e coexistência entre supervisão humana e autonomia.

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Três Arquiteturas Metodológicas de *HITL* (Seção II.A–C, Figs. 2–4, pp. 3–5):**
    1. **HITL Active Learning Framework (Seção II.A, Fig. 2, pp. 3–4):** Loop iterativo formalizado por $D^L_{t+1} = D^L_t \cup X_t$ e $D^U_{t+1} = D^U_t - X_t$ mediante estratégia de consulta $S_q$ a um oráculo humano, integrando amostragem por incerteza/diversidade e *crowdsourcing*;
    2. **HITL Reinforcement Learning Framework (Seção II.B, Fig. 3, pp. 4–5):** Arquitetura em que o agente interage com o ambiente via *State Selector* e aciona *State Queries* para que o operador humano forneça novas ações (*New Actions*) e *Action Timings*, incluindo *Human-in-the-Loop Low-Shot Learning (HILL)* [49], *Regret Preference Modeling* [50] e **RLHF** para alinhamento de LLMs (com redes de recompensa e política segregadas, Seção III.D, pp. 11–12);
    3. **HITL in Explainable AI — XAI (Seção II.C, Fig. 4, p. 5):** Ciclo em malha fechada (*Explainability $\to$ Evaluation $\to$ Close the Loop*) com atribuição de atributos e explicações em linguagem natural.
  - **Arquiteturas Aplicadas de Gestão de Anomalias e Aprendizado Distribuído (Seção III.D–E, pp. 12–13):** Destaca o algoritmo **NANO** (*Nested HITL Reward Learning* com busca em árvore em loop interno e feedback humano em loop externo, p. 12), o **HBSL** (*HITL-based Swarm Learning* em três estágios: aprendizado local, atualização de pesos no nó primário e feedback humano descentralizado, p. 12), o **MArBLE** (*hierarchical multi-armed bandit* para expansão de conjuntos com especialista humano no loop, p. 13) e o **ALARM1** (*Analyst-in-the-Loop Anomaly Reasoning and Management*, framework *end-to-end* que integra detecção autônoma de anomalias, explicação visual e formulação interativa de novas regras de detecção por analistas, p. 13).
  - **Limitação:** O artigo foca em pipelines *human-in-the-loop* sobre modelos de ML/DL/RL e não detalha arquiteturas modernas de orquestração multiagente autônoma baseadas em LLMs (como *LangGraph*, *AutoGen* ou *CrewAI*).
- **Justificativa:** Descreve com clareza os diagramas arquiteturais de *Active Learning*, *HITL-RL*, *XAI*, *Swarm Learning (HBSL)* e gestão de anomalias com analista no loop (*ALARM1*), mas sem cobrir frameworks de orquestração multiagente agêntica (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Síntese de resultados quantitativos de estudos primários de *HITL* (Seção III.A–E, pp. 6–13):**
    - Em controle compartilhado de veículos autônomos (*HCFC/HCSS*, ref. [55], p. 6): ganho de `~7%` no desempenho de tarefa, acompanhado de **redução de `~35%` na carga física e de `~50%` na carga de trabalho mental (*mental workload*)** do operador humano;
    - Em suporte de IA com explicações e rótulos preditos (ref. [100], p. 9): melhoria relativa superior a **`20%`** no desempenho humano de detecção;
    - No agente *AI-in-the-loop* **HAILEY** avaliado em ensaio clínico randomizado com `300 participantes` (ref. [108], p. 10): aumento de **`19,6%`** na empatia conversacional geral e de **`38,9%`** entre operadores com dificuldade prévia;
    - No framework **H-COAL** (*Human Correction of AI-Generated Labels*, ref. [112], p. 11): fechamento de até **`86%` da lacuna de desempenho** entre rótulos gerados por IA e rótulos humanos com apenas **`20%` de correção humana seletiva** baseada em escores de confiança;
    - Em anotação semiautomática assistida por máquina no *dataset RUN* (refs. [135, 137], p. 13): acurácia de `0.95` em confiabilidade, `0.78` em veracidade e **redução de até `64%` no tempo de anotação** frente ao processo manual;
    - Na ferramenta industrial **DaME** (*Data Mapping Engine*, ref. [138], p. 13): elevação da acurácia de mapeamento de `34%` (estado da arte anterior) para **`69%`**, economizando **`14.000 horas` de trabalho manual** ao longo de `10 meses`.
  - **Limitação:** Como revisão narrativa, reporta métricas extraídas de estudos individuais sem conduzir experimentos próprios ou meta-análise estatística em resposta a incidentes de TI.
- **Justificativa:** Compila evidências quantitativas valiosas sobre redução de carga cognitiva (`-50%`), economia de horas de engenharia (`14.000 h`) e eficiência de intervenção seletiva (`86%` de ganho com `20%` de revisão humana), mas de forma secundária e multissetorial (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia de 9 Desafios Críticos em Sistemas *HITL* (Seção IV.A–I, Fig. 6, pp. 13–17):** O artigo dedica uma seção inteira (Fig. 6, p. 14) à análise sistemática das vulnerabilidades e gargalos da interação humano-IA:
    1. *Human Factors (Seção IV.A, pp. 13–14):* introdução de viés humano, subjetividade, fadiga, inconsistência entre anotadores e gargalo de escalabilidade humana conforme o volume de dados cresce;
    2. *Cost (Seção IV.B, p. 14):* alto custo financeiro de especialistas de domínio, custo de treinamento de operadores e latência introduzida pelo tempo de resposta humana;
    3. *Complexity (Seção IV.C, pp. 14–15):* dificuldade de recrutamento/retenção de especialistas e **reconciliação de *feedbacks* conflitantes** entre múltiplos especialistas ou usuários finais;
    4. *Quality of the Data (Seção IV.D, p. 15):* propagação de estereótipos e rótulos ruidosos;
    5. *Interpretability (Seção IV.E, p. 15):* opacidade de redes profundas frente a modelos auditáveis;
    6. *Online Learning (Seção IV.F, pp. 15–16):* necessidade de adaptação contínua a novas ameaças em **detecção de fraudes e cibersegurança**;
    7. *Human-Machine Interaction (Seção IV.G, p. 16):* incerteza sobre o modo ótimo de fusão entre atributos extraídos por máquina e atributos indicados por humanos e sobre a transição de controle;
    8. *Validation (Seção IV.H, p. 16):* ausência de *ground truth* absoluto para entradas humanas subjetivas e deriva dos critérios de validação ao longo do tempo;
    9. *Ethical and Legal Issues (Seção IV.I, pp. 16–17):* exposição de dados sensíveis a anotadores humanos (mitigada via **Differential Privacy**), eliminação da *"black box defense"* mediante regimes regulatórios de responsabilidade pessoal com supervisão humana (citando Buckley et al. [141] e Zetzsche et al. [142], p. 13) e o risco de **envenenamento malicioso via feedback humano** (na Seção V, p. 17, alerta que indivíduos mal-intencionados podem explorar o loop de feedback humano para treinar LLMs visando manipular crenças, instilar ideias radicais ou cometer fraudes).
- **Justificativa:** Analisa de forma exaustiva os riscos técnicos, cognitivos, de validação, regulatórios e de segurança (incluindo *feedback poisoning* malicioso e privacidade diferencial) inerentes a sistemas com humano no loop (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Agenda de Pesquisa Futura (Seção V, pp. 17–20):** Lista 25 pontos de pesquisa futura abrangendo: determinação automática do **momento exato para intervenção artificial/humana (*right time for intervention*)** em tarefas de alta criticidade de segurança (p. 17); coleta de *feedback* humano de granularidade fina (reescrita parcial e avaliação estruturada para LLMs além de GPT-3, p. 17); criação de um **sistema de IA gêmeo explicável (*explainable twin AI system*)** operando em paralelo a sistemas DL e mecanismos de defesa contra ataques direcionados a motores de DL e XAI (p. 19); descoberta causal escalável em GPU (*Fast Causal Inference — FCI*, *cuPC*, *F-GES*) combinada com auditoria de logs de sistema para responsabilização de usuários (p. 19); integração de Fatores Humanos e Ergonomia (*HF/E*: consciência situacional, *automation bias*, carga de trabalho, p. 19); e alinhamento de valores via *Democratic AI* prevenindo a *"tirania da maioria"* (pp. 19–20).
  - **Limitação:** A Seção V é apresentada como uma longa lista não hierarquizada de 25 tópicos heterogêneos (misturando reabilitação motora, exoesqueletos, oftalmologia e LLMs), carecendo de síntese taxonômica estruturada.
- **Justificativa:** Contém direções futuras relevantes (momento ótimo de intervenção, *explainable twin AI*, defesa de motores XAI, inferência causal e mitigação de *automation bias*), mas organizadas de maneira fragmentada e pouco coesa (`P = 0.5`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 0.5 + 0.5 + 1.0 + 0.5 = 3.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P08 |
| **Autores** | Sushant Kumar; Sumit Datta; Vishakha Singh; Deepanwita Datta; Sanjay Kumar Singh; Ritesh Sharma |
| **Ano** | 2024 |
| **Título** | *Applications, Challenges, and Future Directions of Human-in-the-Loop Learning* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 12, pp. 75735–75760 |
| **DOI** | `10.1109/ACCESS.2024.3401547` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Artigo de Revisão (*Survey* narrativo com 207 referências) |
| **Domínio Principal** | Aprendizado *Human-in-the-Loop (HITL)*, Colaboração Humano-IA, *Active Learning*, *RLHF* e Explicabilidade (*XAI*) |
| **Tecnologias / Frameworks Analisados** | *Active Learning (AL)*, *HITL Reinforcement Learning (RLHF, HILL, Regret Preference Modeling)*, *Explainable AI (XAI, TCAV, LIME)*, **ALARM1** (*Analyst-in-the-Loop Anomaly Reasoning and Management*), **H-COAL**, **MArBLE**, **NANO**, **HBSL** (*HITL-based Swarm Learning*), **HAILEY**, **DaME**, **MARTA** |
| **Escopo de Aplicação** | Veículos autônomos e controle compartilhado, visão computacional, saúde e diagnóstico clínico, PLN e alinhamento de LLMs, serviços financeiros e detecção/gestão de anomalias e fraudes |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Fundamentação do paradigma *HITL* e transição *Industry 4.0* (*Black-Box AI*) $\to$ *Industry 5.0 / Operator 5.0* focada em resiliência operacional (Seção I, Fig. 1, pp. 1–2); espectro de agência humana vs. automação total, fronteiras de erro e *white-box paradox* em protocolos *AI-first* vs. *human-first* (Seção III.C, pp. 9–10). |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Arquiteturas de *HITL Active Learning* (Fig. 2, pp. 3–4), *HITL Reinforcement Learning* (Fig. 3, pp. 4–5) e *HITL-XAI* (Fig. 4, p. 5); frameworks **ALARM1** (gestão de anomalias com analista no loop, p. 13), **HBSL** (*swarm learning*, p. 12), **NANO** (p. 12) e **MArBLE** (p. 13). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Compilação de métricas secundárias de eficácia *HITL*: `-35%` carga física e `-50%` carga mental em controle compartilhado (p. 6); `+20%` ganho relativo com predições/explicações (p. 9); `+19,6%` a `+38,9%` empatia com agente *HAILEY* (p. 10); `86%` de fechamento de lacuna com `20%` de correção humana no *H-COAL* (p. 11); `-64%` tempo de anotação (p. 13); acurácia de `34%` $\to$ `69%` e economia de `14.000 h` em 10 meses no *DaME* (p. 13). |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Taxonomia de 9 desafios críticos (Seção IV.A–I, Fig. 6, pp. 13–17): viés e inconsistência humana, custo e latência de supervisão, conflito entre múltiplos especialistas, ausência de *ground truth*, aprendizado online para fraudes/cibersegurança, privacidade diferencial, responsabilidade regulatória (*eliminating the black-box defense*, p. 13) e envenenamento malicioso de feedback humano (p. 17). |
| **RQ5** (Lacunas e Direções Futuras) | `P` | `0.5` | 25 direções futuras (Seção V, pp. 17–20), incluindo escolha do momento ótimo de intervenção em tarefas críticas de segurança (p. 17), *explainable twin AI* e defesa contra ataques a motores DL/XAI (p. 19), inferência causal em GPU (*FCI, cuPC, F-GES*) com auditoria de logs (p. 19) e ergonomia de fatores humanos (*automation bias*, p. 19), porém listadas de forma desestruturada. |
| **Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Aderência Forte (70,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `P` | `0.5` | A Seção I (p. 3) formula 10 questões norteadoras sobre o papel do conhecimento humano, métodos de integração, impacto ético/privacidade e escalabilidade no pipeline de ML, mas não define critérios formais de inclusão ou exclusão bibliográfica. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | O artigo não apresenta seção de metodologia de revisão: não informa bases de dados pesquisadas, *strings* de busca, período de coleta nem fluxograma de seleção das 207 referências. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza um amplo volume de literatura (207 referências) ao longo de três metodologias (Seção II), cinco domínios de aplicação (Seção III) e nove categorias de desafios (Seção IV), mas sem tabelas comparativas estruturadas e com trechos na Seção V (pp. 18–20) que apenas parafraseiam ou copiam literalmente parágrafos de trabalhos futuros de artigos individuais (ex.: *"The authors note that..."*, *"Future research work mentioned in the given paragraph is..."* na p. 18). |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | As conclusões gerais (Seção VI, p. 20) e a taxonomia de desafios da Seção IV são coerentes com a literatura revisada, mas a falta de curadoria editorial na Seção V reduz a coesão argumentativa da agenda futura. |
| **Total (`SCORE_QA`)** | **Banda: Baixa** | **1.5 / 4.0** | **Qualidade Metodológica Moderada-Baixa (37,5%)** |

---

## Parecer Final do Revisor

O artigo **P08** (Kumar et al., 2024), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, apresenta boa aderência às questões de pesquisa da RSL no eixo de supervisão humana e governança (`SCORE_RQ = 3.5 / 5.0`), embora exiba limitações metodológicas como revisão de literatura segundo os critérios DARE (`SCORE_QA = 1.5 / 4.0`, banda **Baixa**, devido à ausência de protocolo de busca e à compilação pouco filtrada da Seção V). Na arquitetura conceitual da RSL, o estudo **P08** fornece a fundamentação essencial para o paradigma **Human-in-the-Loop (HITL)** e **Operator 5.0**, documentando: (i) como a intervenção seletiva baseada em confiança (*H-COAL*, alcançando `86%` do ganho de desempenho com apenas `20%` de revisão humana) e os frameworks com analista no loop (*ALARM1* e *DaME*) viabilizam a colaboração humano-IA em escala; (ii) o fenômeno do *white-box paradox* e a importância de protocolos *AI-first* na tomada de decisão diagnóstica; e (iii) os nove desafios estruturais da supervisão humana (Fig. 6), incluindo gargalos de latência humana, divergência entre múltiplos especialistas, *feedback poisoning* adversarial e eliminação da *"black-box defense"* regulatória.
