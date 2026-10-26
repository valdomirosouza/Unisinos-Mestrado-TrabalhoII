# Avaliação Individual na Revisão Sistemática da Literatura (RSL) — Estudo P18

## 1. Identificação do Estudo
- **ID do Estudo:** P18
- **Arquivo PDF:** `P18-A2-An architecture for model-based and intelligent automation in DevOps.pdf`
- **Título:** *An architecture for model-based and intelligent automation in DevOps*
- **Autores:** Romina Eramo, Bilal Said, Marc Oriol, Hugo Bruneliere, Sergio Morales
- **Ano de Publicação:** 2024 (Recebido em 22 de dezembro de 2023; Revisado em 4 de maio de 2024; Aceito em 30 de julho de 2024; Disponível online em 2 de agosto de 2024)
- **Veículo de Publicação:** *The Journal of Systems & Software* (Elsevier), Vol. 217, Art. 112180, pp. 1–21
- **DOI:** `10.1016/j.jss.2024.112180` (Dataset suplementar aberto no Zenodo: `10.5281/zenodo.7825177`)
- **Status na RSL:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**
- **Classificação Pré-Verificada:** Qualis **A2** | Quartil SJR **Q1**

---

## 2. Etapa 0 — Elegibilidade (Padronização Retroativa do Corpus Fundacional)

> **Nota Metodológica:** O artigo **P18** integra o corpus fundacional herdado do *Trabalho I*, cuja inclusão já foi estabelecida na linha de base da pesquisa. Esta Etapa 0 cumpre papel de **padronização retroativa e verificação de rastreabilidade** segundo o protocolo PRISMA 2020 (Page et al., 2021) e Kitchenham & Charters (2007).

### E1 — Aderência ao Escopo Semântico
- **Avaliação:** **Atendido Integralmente.**
- **Justificativa Baseada em Evidências:** O estudo apresenta a arquitetura de referência do grande projeto europeu **ECSEL-JU H2020 AIDOaRt** (*AI-augmented automation for DevOps, a model-based framework for continuous development in Cyber-Physical Systems*, Grant No. `101007350`), unindo **Engenharia Dirigida por Modelos (MDE)**, **DevOps** e **Inteligência Artificial / Machine Learning (AIOps e AI DevOps)** (Seções 1–3, Figuras 1–3, pp. 1–7). No contexto de resposta a incidentes e automação inteligente de operações, o subsistema **AIOps Engineering** (Seção 3.3, Figura 2, pp. 6–7) estrutura explicitamente capacidades de ingestão de telemetria em tempo real, detecção de anomalias (*AI/ML for Anomaly Detection*), análise de causa-raiz (*Insights analysis for root cause analysis — RCA*), sincronização de incidentes entre ambientes (*Collaboration services*) e automação proativa de mitigação e autorrecuperação (**Remediation** e **Response Automation**), além de serviços transversais de **Accountability** e **Explainability** (Seção 3.2, pp. 5–6).

### E2 — Janela Temporal (2023–2026)
- **Avaliação:** **Atendido Integralmente (Publicado em 2024).**
- **Justificativa:** Submetido em dezembro de 2023 e publicado no volume 217 do periódico *The Journal of Systems & Software* em agosto de 2024, enquadrando-se diretamente na janela temporal de 2023–2026 da RSL.

### E3 — Revisão por Pares e Qualidade do Veículo
- **Avaliação:** **Atendido Integralmente.**
- **Justificativa:** Artigo original avaliado por pares em periódico de excelência em Engenharia de Software (*The Journal of Systems & Software* — Elsevier, ISSN `0164-1212`), classificado como **Qualis A2** e **SJR Q1**, resultado de consórcio industrial-acadêmico europeu composto por **32 organizações parceiras** de 7 países (`7` grandes empresas, `12` PMEs e `13` universidades/institutos de P&D).

### E4 — Critérios de Exclusão
- **Avaliação:** **Nenhum critério de exclusão aplicável.**
- **Justificativa:** Trata-se de estudo primário completo (21 páginas) com validação empírica sobre **10 estudos de caso industriais reais** e **54 soluções tecnológicas**, acompanhado de pacote de replicação aberto no Zenodo (`10.5281/zenodo.7825177`).

### Decisão Final da Etapa 0
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**

---

## 3. Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1 a RQ5)

### RQ1 — Fundamentos Conceituais, Taxonomias e Paradigmas (AIOps, MDE e Automação Inteligente em DevOps)
- **Pontuação:** **P (0.5 — Cobertura Parcial)**
- **Evidências Extraídas do Texto:**
  - **Tríade Sinérgica MDE + DevOps + AI/ML (AIOps) (Seções 1 e 2.1, Figura 1, pp. 1–4):** Os autores conceituam a transição de pipelines de DevOps locais e fragmentados para uma arquitetura contínua de engenharia de sistemas ciberfísicos (*Cyber-Physical Systems — CPSs*) na qual **modelos** (incluindo *Digital Twins*, modelos de tempo de execução e *Mega-Models*) atuam como artefatos de primeira classe que alimentam e são retroalimentados por técnicas de IA/ML e AIOps (Figura 1, p. 2).
  - **Taxonomia de Desafios Arquiteturais e Técnicos (Seção 2.2, p. 3):** O estudo formaliza sete desafios fundamentais divididos em duas dimensões:
    1. *Desafios Arquiteturais (`A1–A4`):* **A1. Heterogeneity** (integração de múltiplas fases, domínios de CPS e padrões heterogêneos), **A2. Flexibility** (extensibilidade modular e interoperabilidade aberta), **A3. Integration** (orquestração horizontal de cadeias de ferramentas em pipelines DevOps) e **A4. Collaboration** (alinhamento entre provedores de desafios industriais e provedores de ferramentas de P&D);
    2. *Desafios Técnicos (`T1–T3`):* **T1. Data management** (coleta, limpeza, fusão e rastreabilidade de dados de tempo de design e de execução), **T2. Modeling support** (gerenciamento de modelos em larga escala, abstração e rastreabilidade) e **T3. AI-powered DevOps** (aplicação de IA/ML para lidar com a complexidade de eventos históricos e de *runtime*, previsão de falhas e geração automatizada de artefatos).
  - **Paradigmas de IA/ML Incorporados ao Ecossistema (Seção 2.1, p. 2):** A fundamentação abrange *Heterogeneous Graph Neural Networks (HGNNs)* para recomendação de modelagem, *DBSCAN* para detecção de logs de falha, *Learning-Based Testing (LBT)* para geração automática de testes, *Generative AI* para síntese de cenários de teste e *Large Language Models (LLMs)* para verificação formal de requisitos funcionais.
- **Justificativa da Nota (`P = 0.5`):** O artigo estabelece uma sólida fundamentação conceitual para a convergência entre MDE, DevOps e AIOps, bem como uma taxonomia clara de desafios (`A1–A4`, `T1–T3`), mas não tem como foco principal a distinção taxonômica entre arquiteturas de *Agentic AI* autônomas baseadas em LLMs e agentes reativos clássicos.

---

### RQ2 — Arquiteturas, Componentes, Padrões de Mediação e Orquestração de Ferramentas
- **Pontuação:** **T (1.0 — Cobertura Total)**
- **Evidências Extraídas do Texto:**
  - **Arquitetura de Componentes UML em Três Camadas do AIDOaRt (Seções 3.1 a 3.4, Figuras 2 e 3, pp. 3–7):** A arquitetura global (Figura 2, p. 4) consome dados de *Historical Sources*, *Real-Time Sources* (eventos, logs, rastros de execução, métricas de sensores) e *Contextual Sources* (topologias de rede, configurações), organizando-se em três *Tool Sets* principais:
    1. **Data Engineering Tool Set (Seção 3.1, Figuras 4 e 5, pp. 4–5):** Composto por *Data Collection*, *Data Management* (filtragem, harmonização, transformação e agregação) e *Data Representation*. Esta representação apoia-se em um **UML Mega-Model em duas camadas** (Figura 4, p. 5): a *camada azul* (modelos de dados concretos dos estudos de caso) e a *camada laranja* (conceitos genéricos abstratos distribuídos em 5 pacotes: *Requirements Engineering, Modeling, Coding, Testing, Monitoring*, detalhados nas Figuras 5, 11 e 16).
    2. **Core Tool Set (Seção 3.2, Figura 2, pp. 4–6):** Estruturado em *Infrastructure* (*Storage Capabilities* para persistência relacional/NoSQL/grafos e *Computation Capabilities* para execução em nuvem/HPC), *Data and Modeling* (*Data Handling Capabilities* e *Model-Based Capabilities* — transformação de modelos, federação de visões via **EMF Views**, geração de código e *Modeling Process Tracing*) e *Generic Services* (**Accountability** e **Explainability**).
    3. **AI-Augmented Tool Set (Seção 3.3, Figura 2, pp. 6–7):** Subdividido em dois grandes subsistemas:
       - **AIOps Engineering:**
         - *(a) Ingestion & Handling:* monitoramento histórico/tempo real, balanceamento de datasets, *Bug Pattern Discovery* e *API and Code Patterns Discovery*;
         - *(b) Engagement & Analysis:* **Insights analysis** (inferência, verificação e **análise de causa-raiz [RCA]**), **Predictive analysis**, **Collaboration services** (sincronização de informações de incidentes entre múltiplos ambientes), **AI/ML for Anomaly Detection** em séries temporais, *ML-based Prediction for HMI*, *Object Detection*, *Equivalence Class Prediction* e *Prediction for Performance and Resource Utilization* (latência, área de FPGA, memória);
         - *(c) Automation:* **Remediation** (capacidades de autorrecuperação e ação proativa orientadas por prescrições analíticas) e **Response Automation** (codificação de conhecimento de domínio humano para tratamento automatizado de incidentes e mitigação de ameaças, p. 6).
       - **AI DevOps Engineering:** *AI for Requirements Engineering* (verificação de ambiguidade via NLP, similaridade semântica, classificação, alocação automática, *zero/few-shot learning* com *RLHF*, verificação de consistência formal), *AI for Modeling* (GNNs para assistência de modelagem e sincronização visão-modelo, exploração de espaço de design, *model learning*), *AI for Code* (recomendação de snippets, geração de código C/C++/SystemC, *mocking*), *AI for Testing* (geração de suítes/modelos de teste, *Learning-Based Testing*, redução de casos de teste) e *AI for Monitoring* (*AI for Text Analytics* sobre logs de sistema, *Functional/Performance Bug Detection* e *AI/ML for Anomaly Detection*, p. 7).
  - **Engenharia de Requisitos Baseada em Modelos (MBRE) Ágil e 4 Padrões de Mediação Arquitetural (Seções 2.3 e 4.1–4.4, Figuras 6–8, pp. 3, 7–8):** O processo de engenharia utiliza um repositório compartilhado **Modelio SaaS** como fonte única da verdade (*Single Source of Truth*) e define quatro padrões de integração (*Mediation Patterns*):
    1. *Generic requirements mediation pattern* (alinhamento entre requisitos concretos de estudos de caso e requisitos genéricos de soluções);
    2. *AIDOaRt components mediation pattern* (mapeamento entre requisitos genéricos e componentes arquiteturais);
    3. *Data engineering mediation pattern* (interoperabilidade semântica via o Mega-Model UML em duas camadas);
    4. *Case study's environment extensions* (integração horizontal de cadeias de ferramentas em pipelines DevOps reais, exemplificada na Figura 6, p. 7, pela orquestração entre **Keptn**, **HEPSYCODE** e **DataAggregator**, além de cadeias envolvendo **AsyncAPI Toolkit**, **TWIMO**, **AALpy**, **RAC**, **VARA**, **NLP4RE**, **AutomationML**, **MER** e **MORGAN**, Seções 5 e 6, pp. 8–15).
- **Justificativa da Nota (`T = 1.0`):** O trabalho detalha exaustivamente a arquitetura de referência em múltiplas camadas, seus componentes internos de AIOps/DevOps, o metamodelo de dados (*Mega-Model*) e os padrões formais de mediação e encadeamento de ferramentas.

---

### RQ3 — Evidências Empíricas, Estudos de Caso Industriais e Métricas de Avaliação
- **Pontuação:** **T (1.0 — Cobertura Total)**
- **Evidências Extraídas do Texto:**
  - **Consolidação Quantitativa em 10 Estudos de Caso Industriais e 54 Soluções Tecnológicas (Seções 5, 6.1 e 6.3, Tabelas 1–4, Figuras 19–22, pp. 8, 10, 16–18):**
    - A validação empírica abrange **10 estudos de caso industriais** de múltiplos domínios de CPS (`ABI` [Abinsula], `AVL` [AVL List], `BT/Alstom` [Bombardier/Alstom Transport], `CAM` [Camea], `CSY` [ClearSy], `HIB` [Hiberus], `PRO` [Prodevelop], `TEK` [Tekne], `VCE` [Volvo Construction Equipment] e `WMO` [Westermo Network Technologies], Tabela 1, p. 8);
    - Foram elicitados **128 requisitos concretos** (`126` mapeados), abstraídos em **47 requisitos genéricos** (`30` centrais), atendidos por **54 soluções tecnológicas** fornecidas por `22` organizações parceiras (oferecendo `113` serviços e totalizando `136` mapeamentos de soluções, Seção 6.3, p. 16);
    - **Cobertura Quantitativa por Componente Arquitetural (Tabelas 2, 3 e 4, p. 17):**
      - *Data Engineering Tool Set (Tabela 2):* Data Collection (`11` soluções / `36` requisitos mapeados), Data Management (`10` soluções / `27` requisitos), Data Representation (`10` soluções / `11` requisitos);
      - *Core Tool Set (Tabela 3):* Storage (`3` / `21`), Computation (`9` / `9`), Data Handling (`10` / `12`), Model-based (`19` / `9`), Accountability (`1` / `5`) e Explainability (`5` / `7`);
      - *AI-Augmented Tool Set (Tabela 4):* Ingestion & Handling (`7` / `12`), Engagement & Analysis (`16` / `39`), Automation (`13` / `13`), AI for Requirements (`7` / `5`), AI for Monitoring (`4` / `19`), AI for Modeling (`13` / `24`), AI for Coding (`6` / `3`) e AI for Testing (`17` / `16`).
    - **Precisão na Descoberta de Colaborações via Arquitetura (`A4`, Seção 6.3.1, Figura 22, pp. 16, 18):** A análise de mapas de calor (*heat maps*) de acoplamento indireto mediado pela arquitetura identificou com sucesso **91% das colaborações reais** estabelecidas entre provedores de estudos de caso e provedores de soluções tecnológicas.
  - **Métricas Empíricas nos Três Estudos de Caso Detalhados (Seções 6.2.1 a 6.2.3, Figuras 9–18, pp. 10–15):**
    1. *Caso 1 — AVL (Engenharia Automotiva / Emissões Reais de Direção — RDE, Seção 6.2.1, Figuras 9–12, pp. 10–12):* Integração das ferramentas **TWIMO** (predição explicável baseada em *Random Forest*) e **AALpy** (aprendizado passivo de autômatos que infere *Markov Decision Processes — MDPs* a partir de telemetria veicular), superando significativamente a fidelidade do modelo paramétrico baseado em regras legado da AVL na simulação de perfis de velocidade de motoristas em rodovias;
    2. *Caso 2 — Alstom / BT (Sistemas de Tração Ferroviária, Seção 6.2.2, Figuras 13–14, pp. 12–14):* Avaliação quantitativa no pipeline de análise de requisitos ferroviários: a ferramenta **RAC** (*Requirements Ambiguity Checker*) atingiu **80% de acurácia** na detecção de requisitos ambíguos; a ferramenta **VARA** alcançou **71% de acurácia** na análise de similaridade via NLP para reúso de componentes e artefatos; e o módulo **Modelio NLP4RE** obteve **60% de acurácia** na identificação de requisitos similares;
    3. *Caso 3 — Volvo Construction Equipment (VCE, Seção 6.2.3, Figuras 15–18, pp. 14–15):* Encadeamento de **AutomationML Modeling (CAEX)** + **MER** (*Modeling Process Mining Tool*) + **EMF Views** (interconectando modelos SysML, AutomationML e modelos de simulação de tempo de execução *FMU*) + **MORGAN** (recomendador de modelagem baseado em *graph kernels*), validado em estudo com usuários junto a **4 perfis de engenharia sênior da VCE** (sessões de `1,5 hora`), demonstrando satisfação positiva e aceleração na velocidade de modelagem de sistemas.
- **Justificativa da Nota (`T = 1.0`):** Apresenta validação empírica robusta em escala industrial europeia (10 estudos de caso, 54 soluções, 128 requisitos), combinando métricas de cobertura arquitetural, acurácia de descoberta de colaboração (`91%`) e métricas de acurácia de ferramentas de IA (`80%`, `71%`, `60%`).

---

### RQ4 — Governança, Explicabilidade, Accountability, Riscos e Limitações
- **Pontuação:** **P (0.5 — Cobertura Parcial)**
- **Evidências Extraídas do Texto:**
  - **Accountability e Explainability como Serviços Genéricos de Primeira Classe (Seção 3.2, Figura 2, Tabela 3, pp. 4–6, 17):** A arquitetura AIDOaRt incorpora explicitamente no *Core Tool Set* dois componentes de governança algorítmica:
    1. **Accountability Services:** garantem auditabilidade, rastreabilidade de decisões e conformidade ao longo do ciclo DevOps (`1` solução dedicada mapeada para `5` requisitos genéricos, Tabela 3, p. 17);
    2. **Explainability Services (XAI):** fornecem transparência e interpretabilidade humana sobre modelos de IA/ML opacos (`5` soluções dedicadas mapeadas para `7` requisitos genéricos, Tabela 3, p. 17; exemplificado no Caso AVL pelo uso do *TWIMO* para explicar predições de comportamento de condução e transições de estados em MDPs com *AALpy*, pp. 10–12).
  - **Análise Sistemática de Ameaças à Validade e Barreiras Organizacionais (Seções 7.1–7.4 e 8, pp. 17–18):** Os autores discutem rigorosamente ameaças de validade de *Constructo* (subjetividade no mapeamento de requisitos mitigada por revisões cruzadas), *Interna* (consistência da modelagem no Modelio SaaS), *Externa* (generalização para além de CPS via abstração no Mega-Model) e *Conclusão*, além de reportarem desafios práticos de curva de aprendizado organizacional com MDE/IA e usabilidade da ferramenta Modelio entre múltiplos parceiros (Seção 8, p. 18).
  - **Limitação de Avaliação de Atributos de Qualidade Arquitetural (Seção 10, p. 19):** Os próprios autores reconhecem a ausência de uma avaliação formal de *trade-offs* arquiteturais baseada em métodos como o **ATAM (*Architecture Tradeoff Analysis Method*)**.
- **Justificativa da Nota (`P = 0.5`):** Embora integre *Accountability* e *Explainability* na arquitetura central e discuta ameaças à validade com rigor, o artigo não aprofunda riscos específicos de segurança cibernética ou ataques adversariais contra agentes de IA (como *prompt injection* ou alucinações em cascata).

---

### RQ5 — Lacunas de Pesquisa, Tendências e Direções Futuras
- **Pontuação:** **P (0.5 — Cobertura Parcial)**
- **Evidências Extraídas do Texto:**
  - **Descoberta Recomendada de Colaborações Interdomínios (Seções 6.3.1 e 8, Figura 22, pp. 16, 18):** Explorar os vínculos indiretos revelados pelos mapas de calor da arquitetura para recomendar automaticamente novas integrações de ferramentas e parcerias entre domínios industriais distintos (automotivo, ferroviário, construção, telecomunicações).
  - **Avaliação Formal de Arquitetura via ATAM e Métricas de Qualidade (Seção 10, p. 19):** Conduzir avaliações formais da arquitetura AIDOaRt utilizando o método **ATAM** (Kazman et al., 2000) e métricas quantitativas de manutenibilidade, escalabilidade e acoplamento arquitetural (Silva et al., 2023).
  - **Expansão de Gêmeos Digitais (*Digital Twins*) Federados e Automação Fechada em Tempo de Execução (Seções 1, 6.2.3 e 10, pp. 1, 15, 19):** Ampliar os estudos com usuários na VCE e a federação de modelos de tempo de design (SysML, AutomationML) com modelos de simulação e *runtime* (*Functional Mock-up Units — FMUs*), evoluindo os mecanismos de AIOps para monitoramento contínuo, alerta precoce e autorremediação confiável em ambientes industriais críticos.
- **Justificativa da Nota (`P = 0.5`):** O artigo delineia passos futuros claros para evolução arquitetural, federação de modelos e avaliação ATAM, mas não formula uma agenda de pesquisa voltada especificamente a sistemas multiagentes autônomos ou *Agentic AI Copilots*.

---

### Síntese Quantitativa das Questões de Pesquisa (SCORE_RQ)
$$\text{SCORE\_RQ} = \text{RQ1 } (0.5) + \text{RQ2 } (1.0) + \text{RQ3 } (1.0) + \text{RQ4 } (0.5) + \text{RQ5 } (0.5) = \mathbf{3.5\text{ / }5.0}$$

---

## 4. Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização do Estudo (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
| :--- | :--- |
| **ID** | P18 |
| **Autores e Ano** | Eramo et al. (2024) |
| **Título** | *An architecture for model-based and intelligent automation in DevOps* |
| **Veículo** | *The Journal of Systems & Software* (Elsevier), Vol. 217, Art. 112180 |
| **DOI** | `10.1016/j.jss.2024.112180` |
| **Qualis / SJR** | **A2** / **Q1** |
| **Citações / Fator de Impacto** | `[VERIFICAR]` (Métricas bibliométricas dinâmicas externas ao PDF) |
| **Tipo de Estudo** | Artigo Primário de Arquitetura de Referência e Avaliação em Múltiplos Estudos de Caso Industriais (Projeto Europeu H2020 **AIDOaRt**) |
| **Domínio de Aplicação** | Automação Inteligente em DevOps, Engenharia Dirigida por Modelos (MDE) e AIOps para Sistemas Ciberfísicos (*Cyber-Physical Systems — CPSs*: automotivo, ferroviário, equipamentos de construção, redes industriais) |
| **Técnicas / Tecnologias Chave** | Arquitetura UML em 3 Camadas (*Data Engineering, Core, AI-Augmented Tool Sets*), UML Mega-Model em 2 camadas, **Modelio SaaS**, **EMF Views**, **Keptn**, **HEPSYCODE**, **TWIMO** (*Random Forest* XAI), **AALpy** (inferência de MDPs), **RAC**, **VARA**, **NLP4RE**, **AutomationML**, **MER**, **MORGAN** (GNN/graph-kernel) |
| **Principais Resultados Quantitativos** | Validação em **10 estudos de caso industriais** e **54 soluções tecnológicas** (`128` requisitos concretos $\to$ `47` genéricos; `136` mapeamentos); **91%** de precisão na identificação de colaborações reais via arquitetura; acurácias no caso Alstom de **80%** (**RAC**), **71%** (**VARA**) e **60%** (**Modelio NLP4RE**) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Nota | Símbolo | Síntese da Evidência no Artigo |
| :--- | :---: | :---: | :--- |
| **RQ1** (Fundamentos e Taxonomias) | `0.5` | **P** | Conceitua a sinergia **MDE + DevOps + AI/ML (AIOps)** (Figura 1, p. 2) e formaliza 4 desafios arquiteturais (`A1–A4`) e 3 desafios técnicos (`T1–T3`, Seção 2.2, p. 3). |
| **RQ2** (Arquiteturas e Orquestração) | `1.0` | **T** | Define a arquitetura **AIDOaRt** em 3 camadas (*Data Engineering, Core, AI-Augmented Tool Sets*, Figura 2, pp. 4–7), o **Mega-Model UML** em 2 camadas (Figura 4, p. 5) e **4 padrões de mediação** com cadeias de ferramentas (*Keptn, TWIMO, AALpy, EMF Views, MORGAN*). |
| **RQ3** (Avaliação Empírica e Métricas) | `1.0` | **T** | Avalia **10 casos industriais** e **54 soluções** (Tabelas 1–4, pp. 8, 17); obtém **91%** de descoberta de colaborações (Figura 22, p. 18) e acurácias de **80% (RAC)**, **71% (VARA)** e **60% (NLP4RE)** no estudo de caso ferroviário da Alstom (pp. 12–14). |
| **RQ4** (Governança, Riscos e XAI) | `0.5` | **P** | Incorpora serviços dedicados de **Accountability** (`1` solução / `5` reqs.) e **Explainability** (`5` soluções / `7` reqs.) no *Core Tool Set* (Seção 3.2, Tabela 3, pp. 5–6, 17) e analisa ameaças à validade (Seção 7, pp. 17–18). |
| **RQ5** (Lacunas e Agenda Futura) | `0.5` | **P** | Propõe recomendação automatizada de colaborações via arquitetura, avaliação formal de *trade-offs* via **ATAM** (Seção 10, p. 19) e federação de *Digital Twins* em tempo de execução (*FMUs*). |
| **SCORE_RQ Total** | **3.5 / 5.0** | — | **70,0% de cobertura global das Questões de Pesquisa da RSL** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1 a QA4)

| Critério DARE | Nota | Símbolo | Justificativa Baseada em Evidências |
| :--- | :---: | :---: | :--- |
| **QA1 — Clareza dos critérios de inclusão/exclusão ou escopo de avaliação** | `1.0` | **Y** | Os autores definem explicitamente na Seção 2.2 (p. 3) os critérios estruturados de avaliação arquitetural (`A1. Heterogeneity`, `A2. Flexibility`, `A3. Integration`, `A4. Collaboration`) e técnica (`T1. Data management`, `T2. Modeling support`, `T3. AI-powered DevOps`), além do protocolo MBRE em 4 etapas (Seção 2.3, p. 3). |
| **QA2 — Adequação da busca, transparência metodológica e rastreabilidade** | `1.0` | **Y** | Elevada transparência metodológica e ciência aberta: toda a arquitetura UML, os requisitos concretos/genéricos e os mapeamentos das 54 soluções estão publicados abertamente em repositório **Zenodo** (`10.5281/zenodo.7825177`, Eramo et al., 2023, p. 20), acompanhados de discussão explícita das ameaças à validade (Seção 7, pp. 17–18). |
| **QA3 — Avaliação de qualidade e validação empírica dos artefatos/estudos** | `0.5` | **P** | Apresenta validação quantitativa abrangente de cobertura arquitetural em 10 casos industriais e 54 soluções (Tabelas 1–4, Figuras 19–22) e métricas empíricas em 3 estudos de caso detalhados (AVL, Alstom e VCE), mas não aplica um método formal de avaliação de atributos de qualidade arquitetural como o *ATAM* (reconhecido como limitação na Seção 10, p. 19) nem reporta métricas operacionais de *MTTR* em produção. |
| **QA4 — Síntese dos resultados e sustentação das conclusões nos dados** | `1.0` | **Y** | As lições aprendidas (Seção 8, p. 18) e conclusões (Seção 10, p. 19) são rigorosamente fundamentadas nos dados empíricos coletados ao longo dos 3 anos do consórcio europeu AIDOaRt. |
| **SCORE_QA Total** | **3.5 / 4.0** | **Alta** | **Qualidade Metodológica Alta (Banda: 3.0–4.0)** |

---

## 5. Parecer Final do Revisor

O estudo **P18 (Eramo et al., 2024)**, publicado no periódico *The Journal of Systems & Software* (**Qualis A2 / SJR Q1**), constitui uma referência arquitetural e empírica de alto valor no corpus fundacional da RSL. Desenvolvido no âmbito do projeto europeu **H2020 AIDOaRt** (32 parceiros industriais e acadêmicos), o trabalho demonstra como a **Engenharia Dirigida por Modelos (MDE)** pode estruturar formalmente pipelines de **DevOps e AIOps** através de uma arquitetura em três camadas (*Data Engineering, Core e AI-Augmented Tool Sets*) e de um **Mega-Model UML em duas camadas**. Para a proposta de um *Agentic AI Copilot para Resposta a Incidentes*, **P18** oferece três contribuições diretas: (1) a decomposição arquitetural explícita do subsistema de **AIOps Engineering** em *Ingestion & Handling*, *Engagement & Analysis* (com análise de causa-raiz e detecção de anomalias) e *Automation* (**Remediation** e **Response Automation**); (2) a elevação de **Accountability** e **Explainability (XAI)** à condição de serviços genéricos obrigatórios do *Core Tool Set*; e (3) a demonstração empírica, sobre **10 estudos de caso industriais** e **54 ferramentas**, de padrões de mediação capazes de orquestrar ferramentas heterogêneas de IA/ML, mineração de processos e verificação formal em ambientes críticos.
