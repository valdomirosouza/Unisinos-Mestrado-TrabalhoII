# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P17
- **Arquivo PDF avaliado:** `P17-A1-A_Review_of_Trustworthy_and_Explainable_Artificial_Intelligence_XAI.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido (Escopo Fundacional de Confiabilidade, Explicabilidade e Governança — TAI & XAI).** O artigo realiza uma revisão abrangente sobre **Trustworthy Artificial Intelligence (TAI)** e **Explainable Artificial Intelligence (XAI)**, examinando os sete princípios da Comissão Europeia para IA confiável mapeados ao **GDPR** (Tabela 1, p. 3), os três regimes de supervisão humana (**HITL, HOTL e HIC**, Seção II.A.2, p. 4), a tríade relacional de **Accountability** (*Responsibility, Answerability, Sanctionability*, Seção II.G, p. 7), métodos de design transparente e explicabilidade *post-hoc* (Seções III.E e IV, Figs. 8–11, pp. 9–13) e normas de segurança para sistemas autônomos (**ISO 21448, ISO 26262, ISO/TC 204**, Seção V.C, pp. 15–19).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *IEEE Access*, Volume 11, pp. 78994–79015, julho de 2023 (Recebido em 18 de junho de 2023; Aceito em 25 de junho de 2023; Data de publicação em 20 de julho de 2023; Versão atual em 2 de agosto de 2023).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão publicado em periódico científico revisado por pares (*IEEE Access*, IEEE), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 22 páginas em inglês com 103 referências, 2 tabelas e 13 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Transição de Máquinas Determinísticas para Sistemas Autônomos e a "Síndrome da Caixa-Preta" (Seções I e II, pp. 1–4):** O artigo analisa como a evolução de algoritmos determinísticos (que apenas executavam regras codificadas e gozavam de confiança absoluta) para sistemas de Aprendizado de Máquina e *Deep Learning* capazes de operar de forma totalmente autônoma sem intervenção humana (exemplificados por *AlphaGo Zero*, *MuZero*, veículos autônomos e **agentes autônomos de negociação financeira — *autonomous trading agents***, pp. 2, 6) rompeu a relação de confiança humana devido à opacidade decisória (*"black-box syndrome"*).
  - **Tríade de Regimes de Supervisão Humana — *HITL*, *HOTL* e *HIC* (Seção II.A.2, p. 4):** Com base nas diretrizes do *Joint Research Centre (JRC)* da Comissão Europeia [14] e em Fanni et al. [16], formaliza os três níveis de governança e controle humano sobre sistemas autônomos:
    1. **Human-in-the-Loop (HITL):** Capacidade de intervenção humana em cada fase de decisão do sistema (ressaltando que, em operações de alta velocidade, isso frequentemente não é viável nem desejável);
    2. **Human-on-the-Loop (HOTL):** Capacidade de interferência humana durante o estágio conceitual/projeto do sistema combinada ao monitoramento contínuo de seu funcionamento em operação;
    3. **Human-in-Command (HIC):** Autoridade superior para supervisionar a totalidade das atividades do sistema de IA e decidir **quando e como empregá-lo** (ou desativá-lo) em qualquer circunstância específica.
  - **Limitação:** O estudo concentra-se em sistemas de ML/DL tradicionais e visão computacional, sem abordar agentes baseados em *Large Language Models (LLMs)* ou arquiteturas generativas agênticas.
- **Justificativa:** Fundamenta com clareza os regimes de supervisão humana (**HITL, HOTL e HIC**) e o impacto da autonomia opaca na confiança humana, embora não trate especificamente da transição para *Agentic AI* baseada em LLMs (`P = 0.5`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Arquitetura de Sistemas Explicáveis (*XAI*) — *Transparent Design* vs. *Post-Hoc Explainability* (Seções III.E e IV.A–B, Figs. 8, 10 e 11, pp. 9–13):**
    - Contrasta na Figura 8 (p. 10) a arquitetura genérica de ML (*Training Dataset $\to$ ML Processes $\to$ Learned Function $\to$ Outcome/Decision* sem resposta às dúvidas do usuário) com a **arquitetura XAI** (*Training Dataset $\to$ ML Processes $\to$ Explainable Model $\to$ Explainable Interface $\to$ Users*), complementada pelo framework conceitual de avaliação cognitiva na Figura 10 (p. 12: *Prime Specification $\to$ System Explanation $\to$ Users' Mental Simulation/Interpretation $\to$ Enhanced Performance*);
    - **Três Graus de *Transparent Design* (Seção IV.A, p. 11):** (1) *Simulatability* (capacidade de um operador humano simular mentalmente cada etapa do cálculo em tempo aceitável); (2) *Decomposability* (capacidade de dissecar entradas, variáveis e operações individuais); e (3) *Computational Transparency* (compreensão estatística e paramétrica dos passos algorítmicos, como em *Decision Trees*, *RuleFit* [43] e *Generalized Additive Models — GAMs* baseados em *splines*, pp. 9, 11);
    - **Métodos *Post-Hoc* Globais e Locais (Seção III.E e IV.B, pp. 9–13):**
      - *Globais:* **Model Extraction / Global Surrogate** via **Destilação de Conhecimento (*Knowledge Distillation*, Hinton et al. [59])** otimizando a perda com temperatura $T$ ($\text{Loss} = \sum p_i \log y_i(T=1) - \sum x_i(T=t)\log y_i(T=t)$, p. 12) para condensar redes caixa-preta em árvores de decisão suaves; e **Feature-Based Methods** usando Algoritmos Genéticos, **MSPSO / Intelligent Dynamic Swarm (IDS)** [58], **Importância de Atributos por Permutação ($PFI_d = \mathbb{E}(P(\tilde{f}(\tilde{X}_d, X_s), Y)) - \mathbb{E}(P(\tilde{f}(\tilde{X}), Y))$)**, *Partial Dependence Plot (PDP)*, *Accumulated Local Effect (ALE)* e *H-Statistic* (pp. 9, 12–13);
      - *Locais:* *Individual Conditional Expectation (ICE)*, **LIME** (*Local Interpretable Model-agnostic Explanations*), aproximação local e métodos baseados em propagação como **VisualBackProp** [93] e *Attention Gates* em redes *U-Net / U-Net++* (pp. 9–10, 13–14, 18).
  - **Estimativa de Incerteza Preditiva com Alerta Humano e Arquiteturas de Privacidade (Seção II.B–C, Figs. 5 e 6, pp. 5–6):**
    - Descreve um mecanismo de segurança operacional (Fig. 5, p. 5) no qual cada previsão do modelo é acompanhada por uma **estimativa probabilística de incerteza/ambiguidade (*predicted uncertainty estimation*)**, notificando automaticamente o operador humano para assumir o controle sempre que o modelo expressa ceticismo sobre a veracidade de seu prognóstico;
    - Sistematiza na Figura 6 (p. 6) cinco blocos arquiteturais de preservação de privacidade: **Confidential Computing** (*Homomorphic Encryption*, *Trusted Execution Environment — TEE* e *Secure Multi-Party Computation*), **Federated Learning** e **Differential Privacy**.
  - **Limitação:** Não aborda arquiteturas de orquestração multiagente, memória episódica/vetorial ou invocação de ferramentas (*tool calling*) em LLMs.
- **Justificativa:** Detalha arquiteturas formais de explicabilidade (*Transparent Design* em 3 níveis, *Knowledge Distillation*, *LIME/ALE/PDP/ICE*), transferência de controle baseada em incerteza bayesiana (Fig. 5) e computação confidencial (Fig. 6), embora sem cobrir orquestração agêntica (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Evidências Quantitativas sobre Desconfiança Pública na IA (Seção I, Fig. 2, p. 2):** Reporta os dados consolidados do estudo multinacional da *University of Queensland / KPMG* (2021) [10] (Fig. 2, p. 2), revelando que **mais de `70%` dos indivíduos têm confiança neutra ou nenhuma confiança em sistemas de IA**:
    - *Overall AI systems:* apenas **`28%` dispostos a confiar (*willing*)**, `35%` neutros e `37%` indispostos (*unwilling*);
    - *Medical AI systems:* `37%` dispostos, `32%` neutros e `31%` indispostos;
    - *HR AI systems:* apenas **`23%` dispostos**, `32%` neutros e **`45%` indispostos**.
  - **Trade-off Acurácia Preditiva vs. Explicabilidade e Indicador *Bitrate* de Fidelidade (Seção IV, Fig. 9, p. 11; Seção V.A.3, p. 14):**
    - Apresenta o gráfico do programa **DARPA XAI** (Fig. 9, p. 11) demonstrando a correlação inversa entre acurácia preditiva e explicabilidade (desde *Decision Trees* e *Random Forests* no topo da explicabilidade até *Deep Learning Models* no topo da acurácia preditiva);
    - Documenta o **indicador *bitrate*** (Markus et al. [4]; Lakkaraju et al. [67], p. 14) para quantificar a fração de previsões comparáveis e medir a autenticidade como o grau de concordância/discordância entre o modelo caixa-preta e a justificativa *post-hoc*.
  - **Indicadores Setoriais e de Sistemas Autônomos (Seções I, III.A, V.C–D, Tabela 2, pp. 1, 7, 15–18):**
    - Em segmentação semântica explicável para direção autônoma no dataset *CityScapes* (Hofmarcher et al. [84], p. 18): alcançou **mais de `50%` de *Intersection over Union (IoU)* médio por classe e mais de `80%` de *IoU* médio por categoria**, superando *ENet* e *SegNet* [71, 101] e permitindo depuração de rede (*network debugging*);
    - Projeção da Intel [79, 80] de que veículos automatizados economizarão **`250 milhões de horas` anuais de deslocamento** e salvarão **mais de `500.000 vidas`** nos EUA entre 2035 e 2045 (p. 15), contrastada com as falhas catastróficas do sistema *MCAS* da Boeing que resultaram em dois acidentes com **`157` e `189` fatalidades** [82, 83] (p. 16);
    - Potencial da IA para atender `20%` de todas as demandas clínicas em poucos anos [29] (p. 7) e crescimento do mercado global de software de IA de `US$ 37,5 bilhões` (2019) para `US$ 97,9 bilhões` (2023) e `> US$ 126 bilhões` até 2025 (Fig. 1, pp. 1–2).
- **Justificativa:** Compila dados empíricos importantes sobre percepção de confiança humana (Fig. 2), métricas de fidelidade *post-hoc* (*bitrate*, $PFI_d$) e *benchmarks* de visão explicável (*CityScapes IoU* `>80%`), mas sem experimentos primários próprios em resposta a incidentes (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Mapeamento Sistemático dos 7 Princípios de *Trustworthy AI* aos Direitos e Artigos do *GDPR* (Seções I e II.A–G, Tabela 1, Fig. 4, pp. 2–7):** Na Tabela 1 (p. 3), vincula cada requisito da Comissão Europeia diretamente aos dispositivos legais do **GDPR**:
    1. **Human Agency and Oversight (*Recital 71, Art. 22* — direito de obter intervenção humana):** Alerta na Seção II.A.1 (p. 4) contra técnicas subconscientes de manipulação do comportamento humano pela IA, incluindo **persuasão antiética, engano (*deceit*), enxameamento (*swarming*) e doutrinação**, propondo a criação de **agências locais de supervisão** dentro das grandes criadoras de IA (*Google, Meta*) fiscalizadas por uma **agência global independente de supervisão**;
    2. **Robustness and Safety (*Art. 22* — direito de contestar decisões puramente automatizadas):** Exige resiliência proativa contra instâncias adversariais, mudanças ambientais e **agentes antagônicos (humanos ou máquinas)** (Seção II.B, p. 5);
    3. **Privacy and Data Governance (*Arts. 13, 14, 15* e *CCPA 2018* — direito de notificação e acesso à lógica do processamento automatizado):** Analisa o risco de data centers centralizados se tornarem funis de vazamento massivo quando invadidos e as vulnerabilidades persistentes mesmo em *Federated AI* (Seção II.C, p. 6; Seção III.C, p. 8);
    4. **Transparency (*Recital 71* — direito de obter uma explicação):** Propõe o uso de **sistemas de prova multinível (*multi-level proof systems*)** e órgãos independentes para auditar registros de IA e **impedir que empresas falsifiquem relatórios de auditoria** (Seção II.D, p. 6);
    5. **Diversity and Fairness (*Art. 22* — direito de não se sujeitar a decisão puramente automatizada):** Discute discriminação racial/demográfica, vigilância não consentida (*ClearView AI*) e risco de monopólio e perdas econômicas descontroladas por agentes financeiros autônomos (pp. 2, 6, 8);
    6. **Societal and Environmental Well-being (*Arts. 13, 14, 15*):** Auditoria do consumo energético e de recursos durante o treinamento e distribuição da IA (Seção II.F, p. 7);
    7. **Accountability (*Arts. 13, 14* — direito de ser notificado sobre decisões automatizadas):** Na Seção II.G.1–3 (p. 7), define *accountability* como uma condição relacional inseparável entre múltiplos agentes, decomposta em três pilares formais: **Responsibility** (responsabilidade moral e legal pelos atos e decisões), **Answerability** (competência/disposição para explicar razões a uma contraparte e direito desta de exigir tais fundamentos) e **Sanctionability** (capacidade efetiva de aplicar sanções à parte responsável e monitoradora, exigindo que o sistema **não prossiga** caso não seja possível estabelecer *trade-offs* moralmente aceitáveis).
  - **Normas ISO e Governança de Segurança em Sistemas Autônomos (Seção V.C.1–3, Fig. 13, pp. 16–17):** Mapeia os quatro grupos de *stakeholders* na Figura 13 (p. 17: *Roadway Commuters, Autonomous Systems' Developers, Regulatory Bodies & Insurance Companies, Executives and Supervisors*) e analisa as normas internacionais de segurança funcional e operacional: **ISO 21448 (SOTIF — *Protection of the Intentional Features and functions*)**, **ISO 26262 (*Road transport — Operational protection* para sistemas elétricos/eletrônicos)**, **ISO/TC 204 (ITS)**, o manifesto de 9 critérios da *NACTO* e as diretrizes da *NHTSA*, *SAE International* e *FDA* (pp. 15–16).
- **Justificativa:** Apresenta um arcabouço regulatório, ético e de governança excepcionalmente rico (Tabela 1 mapeando o *GDPR*, tríade *Responsibility–Answerability–Sanctionability*, regimes *HITL/HOTL/HIC*, sistemas de prova contra falsificação de relatórios e normas *ISO 21448 / ISO 26262*) (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Quatro Restrições Abertas para Padronização de *TAI* e *XAI* (Seção VI, p. 19):** Na conclusão do estudo, os autores sintetizam as quatro principais lacunas científicas que ainda impedem a adoção confiável em larga escala:
    1. Falta de **replicabilidade e estabilidade das metodologias de explicabilidade *post-hoc***;
    2. **Ausência de um entendimento unificado, de um conjunto padronizado de critérios e de métricas universais** para quantificar a interpretabilidade de sistemas inteligentes;
    3. O atrito estrutural (*friction*) entre **eficiência/acurácia preditiva e previsibilidade/explicabilidade** (evidenciado no paradoxo da Fig. 9, p. 11);
    4. Limitações fundamentais na explicação de **redes neurais profundas (*deep neural networks*)** em ambientes críticos de tempo real.
- **Justificativa:** Aponta lacunas reais sobre padronização de métricas de interpretabilidade, replicabilidade *post-hoc* e o *trade-off* acurácia-explicabilidade (Seção VI, p. 19), embora de forma sucinta e sem um *roadmap* técnico detalhado para agentes (`P = 0.5`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 0.5 + 0.5 + 0.5 + 1.0 + 0.5 = 3.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P17 |
| **Autores** | Vinay Chamola; Vikas Hassija; A Razia Sulthana; Debshishu Ghosh; Divyansh Dhingra; Biplab Sikdar |
| **Ano** | 2023 |
| **Título** | *A Review of Trustworthy and Explainable Artificial Intelligence (XAI)* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 11, pp. 78994–79015 |
| **DOI** | `10.1109/ACCESS.2023.3294569` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | *Survey* / Revisão da Literatura (103 referências, 2 tabelas, 13 figuras) |
| **Domínio Principal** | Inteligência Artificial Confiável (*Trustworthy AI — TAI*) e Explicável (*Explainable AI — XAI*): Princípios Éticos/Legais, Métodos de Explicabilidade e Governança |
| **Tecnologias / Frameworks Analisados** | *Transparent Design* (*Decision Trees, RuleFit, GAMs/splines*), Métodos *Post-Hoc* (*Knowledge Distillation*, *PDP, ALE, H-Statistic, ICE, LIME*, *Permutation Feature Importance — $PFI_d$*, *MSPSO/IDS*, *VisualBackProp*), *U-Net / U-Net++ com Attention Gates*, *IBM AutoAI / AutoAI-TS*, *Confidential Computing* (*Homomorphic Encryption, TEE, SMPC*), *Federated Learning*, *Differential Privacy*, normas **GDPR, CCPA, ISO 21448, ISO 26262, ISO/TC 204** |
| **Escopo de Aplicação** | Saúde e diagnóstico médico (*EHR, OMOP*), setor bancário e financeiro, *Internet of Things (IoT)*, robótica e veículos/sistemas autônomos (Tabela 2, pp. 18–19) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `P` | `0.5` | Análise da transição de máquinas determinísticas para sistemas autônomos caixa-preta (Seções I–II, pp. 1–4) e formalização dos três níveis de supervisão humana: **HITL (*human-in-the-loop*), HOTL (*human-on-the-loop*) e HIC (*human-in-command*)** (Seção II.A.2, p. 4). Não aborda agentes LLM. |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Arquitetura XAI em 3 níveis de *Transparent Design* (*Simulatability, Decomposability, Computational Transparency*) e métodos *Post-Hoc* globais/locais (*Knowledge Distillation*, $PFI_d$, *PDP, ALE, H-Statistic, ICE, LIME*, Figs. 8, 10, 11, pp. 9–13); transferência de controle humano guiada por **estimativa probabilística de incerteza** (Fig. 5, p. 5) e 5 técnicas de privacidade (Fig. 6, p. 6). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Dados de confiança pública (Fig. 2, p. 2: **`>70%` neutros ou sem confiança em IA**, apenas `28%` confiam em geral e `23%` em RH); curva de *trade-off* acurácia vs. explicabilidade da **DARPA** (Fig. 9, p. 11); métrica **bitrate** de fidelidade *post-hoc* (p. 14); e `>80%` *IoU* por categoria no *CityScapes* para depuração visual (p. 18). Sem experimentos primários próprios. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Mapeamento dos **7 princípios de *Trustworthy AI* aos artigos do GDPR** (Tabela 1, p. 3: *Recital 71, Arts. 13, 14, 15, 22*); alerta contra persuasão subconsciente e *swarming* com proposta de agências locais e global de supervisão (p. 4); sistemas de prova multinível contra falsificação de relatórios (p. 6); tríade formal de **Accountability (*Responsibility, Answerability, Sanctionability*, p. 7)**; e normas **ISO 21448, ISO 26262 e ISO/TC 204** (p. 16). |
| **RQ5** (Lacunas e Direções Futuras) | `P` | `0.5` | Quatro desafios abertos na Seção VI (p. 19): replicabilidade de explicações *post-hoc*, ausência de critérios e métricas padronizadas de interpretabilidade, atrito entre eficiência e previsibilidade e explicação de *DNNs*. |
| **Total (`SCORE_RQ`)** | — | **3.0 / 5.0** | **Aderência Moderada-Alta (60,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `P` | `0.5` | Explicita o escopo e a estrutura organizacional da revisão na Seção I e na Figura 3 (pp. 3–5), cobrindo os 7 pilares de TAI, técnicas de XAI e 4 setores verticais, mas não define critérios formais de inclusão ou exclusão bibliográfica. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | Revisão narrativa tradicional: não informa bases científicas consultadas, *strings* de busca, período de seleção nem fluxograma PRISMA para as 103 referências. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza 103 referências com apoio de 13 figuras conceituais, mapeia os requisitos de TAI ao *GDPR* na Tabela 1 (p. 3) e resume 9 estudos de XAI em direção autônoma na Tabela 2 (p. 18), incluindo formulações matemáticas de *Knowledge Distillation* e $PFI_d$ (pp. 12–13), mas sem avaliação formal de qualidade dos estudos primários. |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | As conclusões da Seção VI (p. 19) são coerentes com as seções anteriores, porém o texto apresenta marcas evidentes de paráfrase automatizada ou revisão linguística deficiente em diversos trechos (ex.: *"solicitation of models' post-maneuver"* na p. 11, *"autonomous pastiche technologies"* e *"sentient inference"* na p. 13, *"numerous quatrefoil techniques"* na p. 14, além de discrepância na numeração das seções entre o texto da p. 4, a Fig. 3 da p. 5 e os cabeçalhos reais do artigo). |
| **Total (`SCORE_QA`)** | **Banda: Baixa** | **1.5 / 4.0** | **Qualidade Metodológica de Revisão Narrativa (37,5%)** |

---

## Parecer Final do Revisor

O artigo **P17** (Chamola et al., 2023), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, apresenta aderência moderada-alta às questões da RSL (`SCORE_RQ = 3.0 / 5.0`), situando-se na banda **Baixa** de qualidade metodológica DARE (`SCORE_QA = 1.5 / 4.0`) por constituir uma revisão narrativa sem protocolo sistemático de busca e com ruídos editoriais de redação. No contexto do corpus fundacional, **P17** cumpre o papel de referência de base para **Explicabilidade (XAI), Confiabilidade (TAI) e Governança Legal (RQ4)**: fornece o mapeamento direto entre os **7 princípios da Comissão Europeia e os artigos/recitais do GDPR** (Tabela 1, p. 3), a distinção entre os três regimes de supervisão humana (**HITL, HOTL e HIC**, p. 4), a decomposição formal de **Accountability em *Responsibility, Answerability e Sanctionability*** (p. 7), o mecanismo de **transferência de controle ao operador humano guiado por incerteza preditiva** (Fig. 5, p. 5) e a taxonomia de métodos *Transparent Design* vs. *Post-Hoc* (*Knowledge Distillation, LIME, PDP, ALE, ICE* e indicador *bitrate*).
