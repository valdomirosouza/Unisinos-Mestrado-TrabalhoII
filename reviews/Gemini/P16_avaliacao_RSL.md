# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P16
- **Arquivo PDF avaliado:** `P16-A1-A Joint Study of the Challenges Opportunities and Roadmap of MLOps and AIOps - A Systematic Survey.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido (Escopo Fundacional de Operacionalização de IA em Operações de TI — AIOps e MLOps).** O artigo realiza uma Revisão Sistemática da Literatura (RSL) conjunta sobre **MLOps (*Machine Learning Operations*)** e **AIOps (*AI for IT Operations*)** seguindo rigorosamente Kitchenham (2007) e PRISMA 2020 (`44.903` registros identificados $\to$ `93` estudos primários avaliados), investigando os desafios de engenharia, orquestração, monitoramento de *concept/data drift*, detecção de anomalias em tempo de execução, análise de causa raiz (*RCA*) via logs, triagem proativa de incidentes e criação de aplicações e infraestruturas de TI **auto-aprendizes e auto-regenerativas (*self-learning and self-healing*)**.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *ACM Computing Surveys (CSUR)*, Volume 56, Número 4, Artigo 84, pp. 84:1–84:30, outubro de 2023 (Recebido em 19 de dezembro de 2022; Revisado em 5 de setembro de 2023; Aceito em 18 de setembro de 2023; Data de publicação em outubro de 2023).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão sistemática publicado no periódico de maior prestígio em *surveys* da Ciência da Computação (*ACM Computing Surveys*), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 30 páginas em inglês com 129 referências, 9 tabelas e 7 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Framework Comparativo entre os Paradigmas *MLOps* e *AIOps* (Seção 1.1, Tabela 1, pp. 2–3):** O artigo formaliza a distinção e a sinergia entre as duas disciplinas emergentes da operacionalização de IA (além de variantes especializadas como **LAOps** [83] para *learning analytics* com preservação de privacidade e **RLOps** [72] para ciclo de vida de *Reinforcement Learning* em *Open RAN*):
    - **MLOps (Incepção científica em 2020):** Focado na criação de produtos estáveis a partir de protótipos de ML mediante princípios de *CI/CD*, orquestração, reprodutibilidade (versionamento integrado de dados, modelos e código), colaboração interdisciplinar e monitoramento contínuo;
    - **AIOps (Incepção científica em 2019):** Focado especificamente em **Operações de Tecnologia da Informação (IT Operations)** para lidar com a complexidade crescente de infraestruturas modernas, **reduzir a intervenção humana** e construir **aplicações e infraestruturas auto-aprendizes e auto-regenerativas (*self-learning and self-healing*)**, apoiado nos três pilares habilitadores de *Big Data*, *cloud computing* e **observabilidade (*observability*)** (Tabela 1, p. 3).
  - **Visão Industrial dos Provedores de Nuvem (Seção 1.1, p. 3):** Sintetiza as definições operacionais de *IBM* (escalabilidade de desempenho, maximização de *uptime* e gestão de picos de demanda [55]), *AWS* e *Microsoft* (redução da intervenção humana em processos de operações de TI com alta qualidade e eficiência [79]) e *Google/Forrester* (resolução de desafios de operações em nuvem [27]).
  - **Limitação:** Por cobrir a literatura publicada entre 2018 e o início de 2023, o artigo antecede a explosão dos frameworks de *Agentic AI* baseados em LLMs (embora já aponte o crescimento dos **Large Language Models (LLMs)** e **agentes conversacionais** nas Seções 4.1.4, 4.1.5, 4.2.2, 4.5.1 e 6, pp. 12–14, 19, 22).
- **Justificativa:** Estabelece os fundamentos conceituais da operacionalização de IA em produção (*MLOps/AIOps*, *observability* e sistemas *self-healing* com redução de intervenção humana), mas sem abranger a taxonomia contemporânea de agentes autônomos baseados em LLMs (`P = 0.5`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia de Frameworks e Arquiteturas de *MLOps* e *AIOps* em Três Camadas (Seção 4.4.1–4.4.4, Tabela 6, pp. 16–18):** Classifica sistematicamente os 93 estudos primários ao longo de três eixos arquiteturais na Tabela 6 (p. 17):
    1. **Infrastructure Management (Seção 4.4.2, p. 17):**
       - *HPC & Containers:* Implantação de redes de IA em escala *petaflop* com isolamento seguro via contêineres [16, 17];
       - *Edge, Fog & TinyML:* Arquiteturas para dispositivos de borda e *IoT* com restrição severa de memória e energia, incluindo **DORY** [18] (implantação ponta a ponta automatizada de *DNNs* em microcontroladores IoT de baixo custo), **ALOHA** [78], **Cloud2edge** [44], **EBI-PAI** [123], **OODIn** [116], **TMLaaS** [125], **TinyMLOps** [71], *TensorFlow Lite* [110] e *Core ML* [58];
       - *Cloud Generic, Serverless & AIaaS:* Destaca o framework de AIOps orientado a objetivos **Orfeon** [36] (operacionalização dirigida a metas de pipelines analíticos distribuídos no *cloud continuum*), **ModelOps** [54] (gestão de ciclo de vida confiável em nuvem), **Pangea** [80] (geração automática de infraestrutura em camadas *edge/fog/cloud*), **Cirrus** [22] (framework *serverless/FaaS* para workflows de ML ponta a ponta), **STRATUM** [14] (*BigData-as-a-Service*), **AFLOW-ML** [43] e **DAIaaS** [59] (IA distribuída como serviço para ambientes 6G);
       - *Networking / SDN / 5G-6G:* Orquestração de *network slices* em 5G/B5G [29, 68] e controladores **Software-Defined Networking (SDN)** acoplados a **Deep Reinforcement Learning (DRL)** e redes convolucionais em grafos (**SmartTRO** [95]) para otimizar robustez topológica contra falhas de rede e ataques maliciosos (Seção 4.3.2, p. 16);
    2. **Data Management & Log Analytics (Seção 4.4.1, pp. 16–17):** Inclui **K2E** [126] (governança e rastreamento de versão de catálogos de dados e modelos), **StreamFlow** [12], **Microlearner** [62] (otimizador da Microsoft para cargas de *Big Data*), **ML4IoT** [4], **LogLAB** [121] (rotulagem automatizada baseada em atenção para anomalias em logs via supervisão fraca), **LogRule** [86] (mineração estruturada de logs para *Root Cause Analysis — RCA*) e o pipeline de **triagem e remediação proativa de incidentes a partir de anomalias de logs** de Mahindru et al. [76];
    3. **Lifecycle Management & Runtime Monitoring (Seção 4.4.3–4.4.4, pp. 17–18):** Abrange **DIANNE** [31], **SemFE** [129] (pipeline semântico), linguagens específicas de domínio (**PADL** [35] e **DSL4hDNCS** [118] para reimplantação de algoritmos inteligentes em sistemas de produção ciberfísicos), aprendizado *on-device* (**MiniLearn** [98]) e arquiteturas de monitoramento e detecção de anomalias em tempo de execução: **CL-MMAD** [67] (detecção multimodal de anomalias de *runtime* baseada em aprendizado contrastivo para falhas funcionais e de desempenho), **Monitorless** [45] (inferência automatizada de degradação de KPIs de aplicações sem conhecimento prévio específico da aplicação), **ProGAN** [53] (monitoramento de processos via GANs) e pipelines de monitoramento contra *concept drift* em AIOps [96].
- **Justificativa:** Oferece uma taxonomia arquitetural extremamente sólida (Tabela 6, pp. 16–18) cobrindo orquestração no *cloud-edge continuum*, *serverless/FaaS*, *SDN+DRL*, mineração de logs para RCA (*LogRule, LogLAB*), inferência de degradação de KPIs (*Monitorless, CL-MMAD*) e remediação proativa de incidentes (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Métricas Bibliométricas e Avaliação Quantitativa de Qualidade de `93` Estudos Primários (Seções 2.4, 3.1–3.3, Figs. 3–5, Tabelas 4, 5 e 9, pp. 6–10, 22–24):**
    - Executa uma filtragem quantitativa em 5 estágios detalhada por editora (*ACM, Elsevier, Springer, IEEE, MDPI, Others*) na Tabela 5 e na Fig. 3 (pp. 7–8): **`44.903` registros identificados** via `600` consultas no Scopus $\to$ **`23.543` após filtros automáticos** $\to$ **`1.574` após triagem de título** $\to$ **`462` após triagem de resumo** $\to$ **`93` estudos incluídos após leitura integral** (`50` da IEEE, `10` da ACM, `10` da Springer, `9` da Elsevier, `7` da MDPI e `7` de outros);
    - Aplica um sistema formal de **7 métricas ponderadas de qualidade (`M1` a `M7`, pontuação de `0` a `10`, Tabela 4, p. 7)** a todos os 93 artigos no **Apêndice A (Tabela 9, pp. 22–24)**, destacando na Seção 3.3 (p. 10) os cinco estudos de maior pontuação técnica: **DORY [18] (`7,2 / 10`)**, **DAIaaS em 6G [59] (`6,8 / 10`)**, **ML para Classificação de Tráfego de Rede [90] (`6,8 / 10`)**, **DSL4hDNCS [118] (`6,5 / 10`)** e **Orquestração de Slices 5G [29] (`6,1 / 10`)**;
    - Distribuição geográfica e tipológica (Seção 3.3, Fig. 4, p. 9; Fig. 7, p. 14): Europa concentra **`~51%` (`49` artigos)**, América do Norte **`~23%` (`22` artigos)**, Ásia **`~20%` (`19` artigos)** e Oceania **`3` artigos** (`0` da América do Sul e África); `~57%` são artigos de conferência e `~41%` artigos de periódicos; na distribuição temática de MLOps (Fig. 7, p. 14), **`24%` focam em *Cloud Continuum***, **`20%` em *AI Lifecycle***, **`14%` em *Data Management***, **`14%` em *Networking*** e `28%` em outros.
  - **Evidências Qualitativas em Gestão de Serviços de TI (*ITSM*) e Resiliência de *SRE* (Seções 4.3.1 e 4.5.2, pp. 15, 20):** Documenta ganhos qualitativos na previsão e resolução rápida de incidentes de TI em *ITSM* [1], na resiliência unificada de *data lakehouses* para *Site Reliability Engineering (SRE)* (recuperação de desastres, *backup* e *restore* [61], p. 15) e na otimização multiobjetivo de custo, desempenho, resiliência e energia no *edge-cloud* [36, 52].
  - **Limitação:** Embora apresente rigorosa quantificação bibliométrica e de qualidade metodológica (Tabela 9), o artigo não extrai nem tabula métricas numéricas de desempenho operacional (como valores percentuais de *F1-score*, *MTTR* ou latência em milissegundos) dos 93 estudos primários.
- **Justificativa:** Fornece avaliação quantitativa rigorosa do corpus literário (`44.903 -> 93` estudos puntuados de 0 a 10 na Tabela 9) e mapeamento qualitativo de benefícios em *SRE* e *ITSM*, mas sem tabulação de métricas experimentais de execução (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia de Desafios e Riscos em Cinco Categorias (Seção 4.1.1–4.1.5, Fig. 6, pp. 10–13):**
    1. **Computer Engineering (Seção 4.1.1, p. 11):** Assimetria de formação entre cientistas de dados, desenvolvedores de software e engenheiros de operações; **desconfiança de profissionais experientes de TI quanto à eficiência de soluções de ML devido à falta de explicabilidade (*lack of explainability*)** [1, 99]; inadequação de ferramentas tradicionais de versionamento de código (*Git/GitHub Actions* [20]) frente ao acoplamento entre código, modelos e dados; e ausência de **governança de dados, modelos e metainformação** [126];
    2. **Data Management (Seção 4.1.2, p. 11):** Escassez de dados rotulados, custo de preparação/validação e complexidade de movimentação e distribuição de tarefas em ecossistemas de *Big Data*;
    3. **Orchestrating the ML Lifecycle (Seção 4.1.3, p. 12):** Sobrecarga de tráfego, largura de banda e atrasos de latência em implantações distribuídas; escassez severa de memória/armazenamento e alto consumo energético de GPUs na borda; **complexidade de proteger a propriedade intelectual e a integridade dos modelos implantados em dispositivos de borda distribuídos e não confiáveis** [52, 70]; riscos de segurança e privacidade em *IoT* [42, 125]; e necessidade de garantir **isolamento *multitenancy*** em nuvem [88];
    4. **Hardware and Architectures (Seção 4.1.4, p. 12):** Heterogeneidade de plataformas de hardware, incompatibilidades entre bibliotecas de ML [124], avaliação de isolamento entre componentes do workflow [88] e o **desafio emergente da confiabilidade (*trustworthiness*) dos resultados gerados por Large Language Models (LLMs) e agentes conversacionais** [101];
    5. **Monitoring, Drift, Viés e Saúde Mental no Loop Humano (Seção 4.1.5, pp. 12–13):** Degradação de modelos estáticos por desgaste e envelhecimento de componentes (*component wear and aging* [94]), vieses de dados e **deriva de conceito (*concept drift*)** [96]; riscos de **viés e falta de equidade (*fairness*) em aplicações de LLMs** treinadas com dados duvidosos; e **riscos à saúde mental (*mental health risks*) associados à participação humana contínua no ciclo de MLOps** [51] (p. 13).
- **Justificativa:** Sistematiza de forma exemplar os gargalos sociotécnicos, de governança de dados/modelos, isolamento *multitenancy*, integridade de modelos em borda, *concept/data drift* e riscos de confiabilidade e saúde mental humana em ciclos com LLMs (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Diagnóstico de Sub-representação Científica do *AIOps* e da Automação de Remediação (Resumo, p. 1; Seção 4.4.4, p. 18; Seção 5, p. 21):** O artigo comprova empiricamente duas lacunas estruturais críticas da literatura:
    1. Enquanto o *MLOps* recebe ampla atenção no estágio de implantação (*deployment*), **o *AIOps* permanece fortemente sub-representado nas fases de gerenciamento de infraestrutura, treinamento e implantação de modelos**, concentrando-se excessivamente apenas em ingestão de dados (Tabela 6, pp. 17–18);
    2. Citando Cheng et al. [25] na Seção 5 (p. 21), evidencia que a maioria das soluções de AIOps restringe-se à detecção de anomalias e à análise de causa raiz (*RCA*), mas **a automação efetiva de ações de resposta e remediação ainda é limitada (*"automation is still limited"*)**.
  - **Roadmap Tecnológico para *MLOps* e *AIOps* (Seções 4.2, 4.3, 4.5 e 6, Fig. 7, Tabela 7, pp. 13–22):** Delimita as fronteiras futuras de investigação: (1) **expansão dos Large Language Models (LLMs) e *Transformers* para os ciclos de vida de MLOps e AIOps** (destacada explicitamente na Seção 4.2.2, p. 14, Seção 4.3, p. 15, e na Conclusão, p. 22); (2) convergência com **redes 5G e 6G** (*slice orchestration*, *MEC task offloading* e *DAIaaS* [29, 59, 66, 123]) e **SDN + DRL** para resiliência contra falhas e ataques [95]; (3) adoção de arquiteturas **Serverless / Function-as-a-Service (FaaS)** orientadas a eventos e **FPGAs / TinyML** no *cloud-edge continuum* (Fig. 7, pp. 14–15); (4) inferência automatizada de KPIs sem conhecimento específico de aplicação para monitoramento de *concept drift* e retreinamento contínuo [45, 60, 96]; e (5) avanço da mineração estruturada de logs e rotulagem fracamente supervisionada para *IT Service Management (ITSM)* e remediação proativa de incidentes [1, 76, 86, 121] (Tabela 7, pp. 19–20).
- **Justificativa:** Oferece um *roadmap* muito bem fundamentado (Seções 4.2, 4.3, 4.5 e 6), diagnosticando com precisão a lacuna entre detecção/RCA e automação de remediação em AIOps e antecipando a incorporação de LLMs ao ciclo de operações de TI (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 0.5 + 1.0 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P16 |
| **Autores** | Josu Diaz-de-Arcaya; Ana I. Torre-Bastida; Gorka Zárate; Raúl Miñón; Aitor Almeida |
| **Ano** | 2023 |
| **Título** | *A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey* |
| **Periódico / Fonte** | *ACM Computing Surveys (CSUR)*, Vol. 56, No. 4, Art. 84, pp. 84:1–84:30 |
| **DOI** | `10.1145/3625289` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão Sistemática da Literatura — RSL (`44.903` registros identificados $\to$ `93` estudos incluídos; 129 referências) |
| **Domínio Principal** | Operacionalização de Inteligência Artificial e Aprendizado de Máquina: Desafios, Arquiteturas e *Roadmap* Conjunto de **MLOps** e **AIOps** |
| **Tecnologias / Frameworks Analisados** | **Orfeon** (AIOps goal-driven), **Pangea**, **ModelOps**, **Cirrus** (serverless), **STRATUM**, **DORY** (IoT MCUs), **K2E** (governança), **LogRule** (RCA em logs), **LogLAB** (rotulagem de anomalias com atenção), **CL-MMAD** (anomalias multimodais de runtime), **Monitorless** (inferência de KPIs), **SmartTRO** (SDN + DRL + GCN), **PADL**, **DSL4hDNCS**, **DAIaaS**, *TensorFlow Lite, Core ML, Docker, FaaS, FPGAs* |
| **Escopo de Aplicação** | Operações de TI (*ITSM*, análise de logs para *RCA* e remediação proativa de incidentes, gestão de falhas, resiliência de *SRE* em *data lakehouses*), telecomunicações (**5G, B5G, 6G, SDN, MEC**), indústria 4.0, veículos autônomos, saúde, energia e exploração espacial (Tabela 7, p. 19) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `P` | `0.5` | Quadro comparativo formal entre **MLOps** e **AIOps** (Tabela 1, p. 3: conceitos, metas de sistemas *self-learning/self-healing* com menor intervenção humana e habilitadores *Big Data, cloud, observability*), além de *LAOps* e *RLOps* (p. 2). Antecede a taxonomia de *Agentic AI* pós-2024. |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Taxonomia arquitetural dos 93 estudos em 3 camadas (Seção 4.4, Tabela 6, pp. 16–18): *Infrastructure Management* (*HPC, Edge/TinyML, Cloud, Serverless/FaaS, AIaaS, Networking/SDN*), *Data Management* (*DataOps/K2E, LogLAB, Big Data*) e *Lifecycle Management* (*Monitoring/CL-MMAD/Monitorless, LogRule, Orfeon, PADL, MiniLearn*). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Filtragem PRISMA em 5 estágios (`44.903 -> 23.543 -> 1.574 -> 462 -> 93`, Tabela 5, Fig. 3, pp. 7–8); avaliação quantitativa dos 93 artigos sob 7 métricas ponderadas (`M1–M7`, máx. `10,0`, Tabela 4 e Apêndice Tabela 9, pp. 7, 22–24, com destaque para *DORY* `7,2` e *DAIaaS/Traffic Classification* `6,8`); distribuição geográfica (Europa `51%`, América do Norte `23%`, Ásia `20%`, Fig. 4) e temática (Fig. 7). Sem tabela de métricas operacionais primárias (*MTTR/F1*). |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Taxonomia de desafios em 5 eixos (Seção 4.1, Fig. 6, pp. 10–13): lacuna interdisciplinar entre *Data Science/SE/Ops*, falta de explicabilidade, **concept/data drift**, ausência de governança de dados/modelos, isolamento *multitenancy*, proteção de IP e integridade de modelos na borda, **confiabilidade e viés em LLMs** e **riscos à saúde mental humana** no loop de MLOps [51]. |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Comprovação da sub-representação do *AIOps* em infraestrutura e *deployment* (Tabela 6, p. 17) e da limitação atual da automação de remediação além da detecção/RCA (p. 21); *roadmap* abrangendo integração de **LLMs e Transformers em MLOps/AIOps** (pp. 14, 15, 22), redes **5G/6G e SDN+DRL**, *Serverless/FaaS*, *TinyML/FPGAs* e inferência automatizada de KPIs. |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Alta Aderência (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | Formula cinco questões de pesquisa explícitas e motivadas na Tabela 2 (p. 4) e define critérios formais e objetivos de inclusão (`I1–I4`) e exclusão (`E1–E5`, incluindo filtro de citações escalonado por ano para preservar artigos recentes de 2022–2023) na Seção 2.3 e Tabela 3 (p. 6). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | Transparência e reprodutibilidade exemplares: executa busca programática via API do *Scopus* combinando três colunas conceituais em **`600` *strings* de busca** (Fig. 1, p. 5) complementadas por uma *string* específica para *AIOps* (Fig. 2, p. 5: `'AIOps' AND ('Failure Prevention' OR ... OR 'Root Cause Analysis' OR 'Remediation' OR ...)`), disponibiliza o **código-fonte do cliente de busca e documentação no GitHub** [34] (p. 4) e apresenta o fluxograma **PRISMA 2020** completo (Fig. 3, p. 8) e a tabela de triagem por editora em 5 estágios (Tabela 5, p. 8). |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `Y` | `1.0` | Define sete métricas formais e ponderadas de avaliação de qualidade (`M1` a `M7`, pontuação máxima de `10`, Tabela 4, p. 7), publica a matriz individual completa de pontuação dos **93 artigos incluídos no Apêndice A (Tabela 9, pp. 22–24)**, discute explicitamente ameaças à validade e risco de viés na Seção 3.2 (p. 9) e compara sua RSL frente a 7 revisões anteriores na Tabela 8 (p. 21). |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões, quadros-resumo e taxonomias (Tabelas 6 e 7, Fig. 6 e 7, Seções 4 e 6) respondem com precisão a todas as questões de pesquisa e derivam diretamente das evidências extraídas dos 93 estudos primários. |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **4.0 / 4.0** | **Qualidade Metodológica Máxima (100,0%)** |

---

## Parecer Final do Revisor

O artigo **P16** (Diaz-de-Arcaya et al., 2023), publicado no *ACM Computing Surveys* e integrante do **Corpus Fundacional** do Trabalho I, alcança a nota máxima de rigor metodológico DARE (`SCORE_QA = 4.0 / 4.0`, banda **Alta**) e alta aderência às questões da RSL (`SCORE_RQ = 4.0 / 5.0`). Assim como **P05** (Zhang et al., 2025), **P16** constitui um pilar metodológico e arquitetural para o eixo de **AIOps e MLOps** da nossa revisão: estabelece o quadro comparativo formal entre *MLOps* e *AIOps* (Tabela 1, p. 3), organiza uma taxonomia de referência para **93 estudos primários** nas camadas de infraestrutura, dados e ciclo de vida (Tabela 6, p. 17, incluindo **Orfeon, LogRule, LogLAB, CL-MMAD, Monitorless** e **SmartTRO**), sistematiza os cinco grandes desafios de operacionalização em produção (Fig. 6, p. 13: *concept/data drift*, isolamento *multitenancy*, governança de modelos e proteção em borda) e comprova empiricamente a lacuna crítica entre detecção/RCA e **automação efetiva de remediação e implantação em AIOps**.
