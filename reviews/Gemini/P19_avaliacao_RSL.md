# Avaliação Individual na Revisão Sistemática da Literatura (RSL) — Estudo P19

## 1. Identificação do Estudo
- **ID do Estudo:** P19
- **Arquivo PDF:** `P19-A1-Agent_System_Mining_Vision_Benefits_and_Challenges.pdf`
- **Título:** *Agent System Mining: Vision, Benefits, and Challenges*
- **Autores:** Andrei Tour, Artem Polyvyanyy, Anna Kalenkova
- **Ano de Publicação:** 2021 (Recebido em 16 de junho de 2021; Aceito em 1 de julho de 2021; Publicado em 8 de julho de 2021; Versão final em 20 de julho de 2021)
- **Veículo de Publicação:** *IEEE Access*, Vol. 9, pp. 99480–99494
- **DOI:** `10.1109/ACCESS.2021.3095464` (Datasets abertos no Melbourne Figshare: Log de eventos em `10.26188/14401400` e Lista dos 149 artigos da RSL em `10.26188/14708772`)
- **Status na RSL:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**
- **Classificação Pré-Verificada:** Qualis **A1** | Quartil SJR **Q1**

---

## 2. Etapa 0 — Elegibilidade (Padronização Retroativa do Corpus Fundacional)

> **Nota Metodológica:** O artigo **P19** integra o corpus fundacional herdado do *Trabalho I*, cuja inclusão já foi consolidada na linha de base da pesquisa. Esta Etapa 0 executa a **padronização retroativa e verificação de rastreabilidade** segundo as diretrizes PRISMA 2020 (Page et al., 2021) e Kitchenham & Charters (2007).

### E1 — Aderência ao Escopo Semântico
- **Avaliação:** **Atendido Integralmente.**
- **Justificativa Baseada em Evidências:** O artigo inaugura a área de pesquisa de **Agent System Mining (ASM)** — uma síntese entre **Process Mining (Mineração de Processos)** sobre logs de eventos de sistemas de informação e **Agent-Based Modeling (ABM) / Multi-Agent Systems (MAS)** (Seções I–IV, Figuras 1–8, pp. 1–11). O estudo resolve o problema crítico dos *"spaghetti process models"* (modelos de processos emaranhados e ininteligíveis gerados pela mineração de processos clássica diante de eventos concorrentes e distribuídos, Figura 3, p. 5) ao descobrir modelos de agentes autônomos de nível micro (*agent sub-models*, *environment sub-model* e *interactions sub-model*) cujas interações locais explicam os comportamentos e gargalos emergentes de nível macro. Essa capacidade de inferir modelos multiagentes verificáveis e auditáveis diretamente a partir de logs operacionais (*event logs*) é um alicerce teórico direto para a observabilidade, diagnóstico de causa-raiz e coordenação multiagente em resposta a incidentes.

### E2 — Janela Temporal (Exceção Seminal do Corpus Fundacional — 2021)
- **Avaliação:** **Atendido por Pertencimento ao Corpus Fundacional (Trabalho I).**
- **Justificativa:** Embora publicado em julho de 2021 (anteriormente ao recorte 2023–2026 aplicado a novos candidatos), **P19** é mantido integralmente por constituir um estudo fundacional pré-aprovado no *Trabalho I*, responsável por introduzir o paradigma de *Agent System Mining* e o ciclo de vida em modelo V para descoberta e validação de sistemas multiagentes baseados em logs.

### E3 — Revisão por Pares e Qualidade do Veículo
- **Avaliação:** **Atendido Integralmente.**
- **Justificativa:** Artigo revisado por pares publicado no periódico *IEEE Access* (ISSN `2169-3536`), classificado como **Qualis A1** e **SJR Q1**, conduzido por pesquisadores da *School of Computing and Information Systems, The University of Melbourne* (Austrália).

### E4 — Critérios de Exclusão
- **Avaliação:** **Nenhum critério de exclusão aplicável.**
- **Justificativa:** Estudo completo (15 páginas) que combina fundamentação teórica em Teoria Geral de Sistemas e Cibernética, estudo de caso motivador executável em simulador multiagente (*AnyLogic*) e uma Revisão Sistemática da Literatura embutida sobre `2.094` registros (`149` estudos primários analisados), com dados abertos publicados no repositório *Figshare*.

### Decisão Final da Etapa 0
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**

---

## 3. Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1 a RQ5)

### RQ1 — Fundamentos Conceituais, Taxonomias e Paradigmas (Sistemas Socio-Técnicos, MAS e Agent System Mining)
- **Pontuação:** **T (1.0 — Cobertura Total)**
- **Evidências Extraídas do Texto:**
  - **Sistemas Socio-Técnicos Auto-Organizáveis e Comportamento Emergente Micro vs. Macro (Seções I e III.A–D, Figura 5, pp. 1–7):** Apoiando-se na Teoria Geral de Sistemas de Bertalanffy [20] e na Cibernética de Wiener [21], os autores conceituam organizações e seus sistemas de TI como **sistemas socio-técnicos auto-organizáveis** (*self-organizing socio-technical systems*). Nesses sistemas, o comportamento global do processo observado no **nível macro** emerge de baixo para cima (*bottom-up*) a partir das decisões autônomas e interações locais executadas por agentes no **nível micro** (Figura 5, pp. 6–7).
  - **Quatro Propriedades Fundamentais de Agentes em MAS (Seção III.D, p. 6, fundamentado em Wooldridge & Jennings / Metodologia Gaia [25]):**
    1. **Autonomy (Autonomia):** os agentes operam seguindo seus próprios fluxos de execução internos, independentemente de controle centralizado externo;
    2. **Situatedness (Situacionalidade):** os agentes estão imersos em um ambiente heterogêneo e dinâmico, percebendo mudanças e atuando sobre ele;
    3. **Proactivity (Proatividade):** os agentes não apenas reagem a estímulos do ambiente, mas planejam e iniciam atividades proativamente para atingir objetivos;
    4. **Sociality (Sociabilidade):** os agentes interagem e cooperam com outros agentes para realizar objetivos compartilhados.
  - **Mudança de Paradigma: Process Mining Top-Down vs. Agent System Mining Bottom-Up (Seções I e II, Figuras 2–4, pp. 1–6):** Os autores demonstram que a mineração de processos clássica assume três restrições rígidas: (i) noção de caso único (*single case notion*), (ii) fluxo de controle único (*single control flow*) e (iii) atividades agnósticas à localização (*location-agnostic activities*). Quando abordagens como *Object-Centric Process Mining (OCPM)* ou *Queue Mining (QM)* tentam relaxar essas restrições mantendo uma visão *top-down*, os algoritmos produzem **"spaghetti process models"** indecifráveis (Figura 3, p. 5). O paradigma **Agent System Mining (ASM)** resolve esse impasse aplicando o princípio de Wolfram [15] (regras locais simples geram comportamentos emergentes complexos): em vez de minerar um grafo monolítico global, o ASM infere *statecharts* compactos por tipo de agente e regras de interação (Figura 4a–b, p. 6).
- **Justificativa da Nota (`T = 1.0`):** Fornece uma fundamentação conceitual exemplar que articula Teoria de Sistemas, propriedades formais de agentes autônomos (*Autonomy, Situatedness, Proactivity, Sociality*) e o contraste epistemológico entre mineração de processos *top-down* e inferência de sistemas multiagentes *bottom-up*.

---

### RQ2 — Arquiteturas, Metamodelos, Ciclo de Vida em Modelo V e Algoritmos de Descoberta
- **Pontuação:** **T (1.0 — Cobertura Total)**
- **Evidências Extraídas do Texto:**
  - **Decomposição Estrutural e Metamodelo UML de um Sistema Multiagente em ASM (Seção IV.A–B, Figuras 6 e 8, pp. 6–7, 10):** O estudo define que um **MAS Model** completo inferido a partir de dados de eventos é composto por três tipos de submodelos acoplados (Seção IV.B, p. 7; Metamodelo UML na Figura 8, p. 10):
    1. Múltiplos **Agent Sub-Models** (um modelo comportamental/máquina de estados por tipo de agente, capturando *Micro State* e regras de decisão);
    2. Um único **Environment Sub-Model** (representando a topologia espacial/lógica, recursos e variáveis de estado do ambiente);
    3. Um único **Interactions Sub-Model** (especificando os protocolos de comunicação síncrona/assíncrona e coordenação entre agentes e ambiente).
  - **Framework de Ciclo de Vida ASM em Modelo V (Seção IV.B, Figura 7, pp. 7–9):** O framework arquitetural de engenharia de sistemas multiagentes orientados por dados é estruturado em **5 Fases** e **3 Pontos de Vista** (*Model User*, *Whole-of-Model Developer* e *Component-Level Developer*, Figura 7, p. 8), automatizado por **7 atividades nucleares de ASM**:
    1. **Phase 1 — Motivate (*Model User*):** identificação manual de problemas operacionais e formulação dos objetivos de modelagem;
    2. **Phase 2 — Plan (*Whole-of-Model Developer*):** definição do *MAS Metamodel*, do *Model Frame* (contexto, escopo, entradas, saídas e variáveis de estado macro), dos *In-Scope Event Logs* e dos *In-Scope Models*, apoiada pelas atividades automatizadas de **search** (busca de eventos relevantes em repositórios distribuídos) e **project** (projeção e filtragem de logs para o escopo dos submodelos);
    3. **Phase 3 — Develop (*Component-Level Developer*):** inferência dos *agent sub-models*, do *environment sub-model* e do *interactions sub-model* a partir dos logs projetados e sua montagem em um modelo MAS executável, automatizada pelas atividades de **discover** (descoberta de modelos a partir de logs), **enhance** (enriquecimento de modelos pré-existentes com telemetria de logs) e **integrate** (integração dos submodelos descobertos no modelo MAS unificado);
    4. **Phase 4 — Evaluate (*Whole-of-Model Developer*):** verificação e validação dos submodelos e do modelo MAS integrado mediante comparação entre os logs de eventos reais e os logs gerados por simulação (*log-to-log*, *model-to-model* e *log-to-model*), automatizada pelas atividades de **diagnose** (diagnóstico no nível de submodelos individuais) e **check** (verificação de conformidade sistêmica do modelo MAS completo);
    5. **Phase 5 — Use (*Model User*):** execução de simulações multiagentes (ex.: no motor **AnyLogic** [16, 18]) e análise estática para auditoria, detecção de gargalos, *what-if analysis* e redesenho do sistema.
  - **Catálogo de Formalismos de Modelagem MAS e Algoritmos de Inferência (Seção V.C.1–2, pp. 12–13):** A revisão sistemática embutida mapeia:
    - *Formalismos de negócios e agentes:* **S-BPM** (*Subject-Oriented BPM* [31, 47]), **MABPMNDF** [32], **agileBPM** [33], **DEMO + ontologia REA** [48], **IPO**, **Gaia** [25], **Tropos** [50], **MaSE** [51], **BDI metamodel** [52] e **Nested Petri Nets (NP-nets)** [53];
    - *Algoritmos de descoberta a partir de rastros/logs:* **Hierarchical Markov Models** para descoberta de comportamento de agentes no nível micro [54], **Probabilistic Goal Recognition** para inferência de comportamentos racionais e irracionais de agentes autônomos [55], mineração de dados sobre conversações entre agentes [56], descoberta de protocolos de interação [57] e aplicação do **$\alpha$-algorithm** para minerar redes de Petri de agentes individuais em sistemas multiagentes [58].
- **Justificativa da Nota (`T = 1.0`):** Propõe um framework arquitetural completo (o Modelo V de ASM com 5 fases, 3 níveis de abstração e 7 operadores formais: *search, project, discover, enhance, integrate, diagnose, check*), um metamodelo UML explícito e um catálogo abrangente de formalismos e algoritmos de descoberta multiagente.

---

### RQ3 — Evidências Empíricas, Estudo de Caso de Simulação e Quantificação Bibliométrica
- **Pontuação:** **P (0.5 — Cobertura Parcial)**
- **Evidências Extraídas do Texto:**
  - **Estudo de Caso Motivador de Cadeia de Suprimentos com Logs de Eventos Abertos (Seção II, Figuras 1–4, pp. 2–6):**
    - Utiliza um dataset de eventos de atendimento de pedidos (*Order Fulfillment Process*) distribuído geograficamente na França (*Montpellier, Lyon, Paris, Limoges*, Figura 1, p. 3), disponibilizado publicamente no repositório *Melbourne Figshare* (`10.26188/14401400`);
    - Demonstra experimentalmente na ferramenta comercial **Disco** [17] que o *Directly-Follows Multigraph (DFM)* agnóstico à localização (Figura 2, p. 4) oculta a dinâmica espacial e de transporte, enquanto o DFM sensível à localização (Figura 3, p. 5) degenera em um modelo *"spaghetti"* ilegível mesmo contendo apenas `2` clientes, `1` varejista, `1` distribuidor e `1` veículo;
    - Contrasta esse resultado com a implementação do **Modelo MAS de 3 tipos de agentes** (*Retailer Agent*, *Vehicle Agent* e *Distributor Agent*, representados por *statecharts* concisos na Figura 4a e regras de interação textual na Figura 4b, p. 6) executado no simulador **AnyLogic** [16, 18]. A inspeção do *statechart* do *Retailer Agent* revela imediatamente uma regra operacional crítica invisível nos grafos DFM tradicionais: o varejista interrompe o recebimento de novos pedidos de clientes sempre que seu estoque cai abaixo do limite mínimo, aguardando o reabastecimento pelo veículo (Seção II.B, p. 4).
  - **Quantificação Bibliométrica da Revisão Sistemática da Literatura Embutida (Seção V.B, Figura 10, p. 12):**
    - Execução em `16 de fevereiro de 2021` de 3 consultas booleanas (`Q1: agent AND "business process"`, `Q2: agent AND "data mining"`, `Q3: agent AND "process mining"`) nas bases **Scopus** (`414`, `1.260` e `37` resultados) e **Web of Science** (`228`, `476` e `24` resultados) para artigos publicados a partir de 2010;
    - Funil de seleção PRISMA/SLR (Figura 10, p. 12): **2.094 publicações únicas** após deduplicação $\to$ exclusão de `1.563` pelo título (`531` restantes) $\to$ exclusão de `384` pelo resumo $\to$ **149 artigos relevantes analisados** na íntegra (lista completa publicada em `10.26188/14708772`), com distribuição temporal por consulta apresentada no gráfico de barras da Figura 10 (2010–2020).
- **Justificativa da Nota (`P = 0.5`):** O artigo apresenta uma demonstração prática convincente comparando *Disco* vs. *AnyLogic* em um log de eventos aberto e uma síntese bibliométrica rigorosa de 149 estudos, mas, por tratar-se de um artigo de visão (*Vision Paper*), não realiza experimentos quantitativos de *benchmark* de tempo de execução, precisão ou escalabilidade de um novo algoritmo automatizado de ASM.

---

### RQ4 — Governança, Conformidade, Privacidade e Desafios Técnicos/Metodológicos
- **Pontuação:** **P (0.5 — Cobertura Parcial)**
- **Evidências Extraídas do Texto:**
  - **Oito Desafios Técnicos e Metodológicos do Agent System Mining (Seção IV.D.1–8, Figura 8, pp. 10–11):**
    1. **MAS Metamodel Selection (Seção IV.D.1, Figura 8):** dificuldade de reconciliar estados micro, estados macro e propriedades de interação heterogêneas em um metamodelo único sem perder generalidade entre domínios;
    2. **MAS Model Scope Definition (Seção IV.D.2):** definição rigorosa do *Model Frame* além das dimensões físicas de espaço 3D e tempo;
    3. **MAS Simulation and Static Analysis Support (Seção IV.D.3):** *trade-off* crítico entre a legibilidade/interpretabilidade humana dos modelos descobertos e sua executabilidade direta em motores de simulação multiagente;
    4. **MAS Model Validation (Seção IV.D.4):** necessidade de novas métricas formais de conformidade (*log-to-log*, *model-to-model* e *log-to-model*) capazes de validar simultaneamente fidelidade no nível micro (comportamento individual do agente) e no nível macro (propriedades emergentes do sistema);
    5. **Event Data Selection and Privacy (Seção IV.D.5, p. 11):** tratamento de logs de eventos incompletos, distribuídos e enviesados pelo contexto, somado ao desafio de **preservação de privacidade e confidencialidade em mineração de processos interorganizacionais** (citando Elkoumy et al. [36]);
    6. **Agent Type Discovery (Seção IV.D.6):** definição de métricas de similaridade comportamental para agrupar instâncias de agentes em tipos (*agent types*) evitando **overfitting** (um modelo por instância) ou generalização excessiva;
    7. **Sub-Model Discovery (Seção IV.D.7):** atribuição correta de eventos multiagentes e eventos ambientais nos logs brutos;
    8. **Modeling Language Selection (Seção IV.D.8):** representação precisa de padrões de comunicação síncrona vs. assíncrona e garantias de entrega de mensagens (*best-effort* vs. entrega garantida), assegurando consistência e completude formal.
  - **Auditoria de Conformidade (*Conformance & Compliance*) e Responsabilidade de Agentes (Seções IV.C.3 e V.C.1, pp. 10, 12):** O estudo destaca que o ASM viabiliza auditorias de *compliance* mais granulares (verificando se agentes humanos ou de software violaram políticas locais, Seção IV.C.3, p. 10) e revisa abordagens que modelam explicitamente **responsabilidades, *accountabilities* e interações conscientes de risco (*risk-aware interactions*)** em sistemas multiagentes [43, 44] (Seção V.C.1, p. 12).
- **Justificativa da Nota (`P = 0.5`):** O artigo mapeia com profundidade 8 desafios metodológicos/técnicos (incluindo privacidade interorganizacional, *overfitting* na descoberta de agentes e validação multi-nível) e benefícios para auditoria de *compliance*, mas não aborda ameaças de segurança de IA generativa/LLMs.

---

### RQ5 — Lacunas de Pesquisa, Tendências e Direções Futuras
- **Pontuação:** **T (1.0 — Cobertura Total)**
- **Evidências Extraídas do Texto:**
  - **Constatacão da Lacuna Central na Literatura de 149 Artigos (Seção V.C.2, p. 13):** A revisão sistemática demonstra que, embora existam algoritmos isolados para minerar partes específicas de comportamentos ou conversações de agentes [54–58], **nenhum método existente na literatura é capaz de realizar o ciclo completo de ASM** (descoberta conjunta e integração de *agent sub-models*, *environment sub-model* e *interactions sub-model* em um modelo MAS executável e validado).
  - **Agenda de Pesquisa Fundacional em Três Pilares (Seção VI, p. 13):** Os autores estabelecem um roteiro de pesquisa estruturado em três frentes prioritárias para a comunidade científica:
    1. **Metamodelos e Formalismos para ASM:** desenvolvimento de metamodelos formais e linguagens de modelagem capazes de representar sistemas multiagentes descobertos a partir de dados de eventos operacionais mantendo interpretabilidade humana e semântica de execução;
    2. **Algoritmos End-to-End de Descoberta, Enriquecimento e Integração (*Discover, Enhance, Integrate*):** criação de algoritmos automatizados para inferir tipos de agentes, máquinas de estados internas, topologia de ambiente e protocolos de interação diretamente de logs distribuídos;
    3. **Técnicas e Métricas de Avaliação de Qualidade e Validação (*Diagnose & Check*):** formulação de métricas rigorosas de precisão, revocação (*recall*), simplicidade e generalização que comparem o comportamento emergente simulado com o comportamento real registrado nos logs tanto no nível micro quanto no nível macro.
- **Justificativa da Nota (`T = 1.0`):** Como um *Vision Paper* seminal, **P19** cumpre exemplarmente o papel de diagnosticar uma lacuna científica aberta sobre 149 estudos e estruturar uma agenda de pesquisa completa e acionável para a engenharia de sistemas multiagentes orientados por logs.

---

### Síntese Quantitativa das Questões de Pesquisa (SCORE_RQ)
$$\text{SCORE\_RQ} = \text{RQ1 } (1.0) + \text{RQ2 } (1.0) + \text{RQ3 } (0.5) + \text{RQ4 } (0.5) + \text{RQ5 } (1.0) = \mathbf{4.0\text{ / }5.0}$$

---

## 4. Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização do Estudo (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
| :--- | :--- |
| **ID** | P19 |
| **Autores e Ano** | Tour, Polyvyanyy & Kalenkova (2021) |
| **Título** | *Agent System Mining: Vision, Benefits, and Challenges* |
| **Veículo** | *IEEE Access*, Vol. 9, pp. 99480–99494 |
| **DOI** | `10.1109/ACCESS.2021.3095464` |
| **Qualis / SJR** | **A1** / **Q1** |
| **Citações / Fator de Impacto** | `[VERIFICAR]` (Métricas bibliométricas dinâmicas externas ao PDF) |
| **Tipo de Estudo** | Artigo de Visão (*Vision & Conceptual Framework Paper*) com Estudo de Caso de Simulação e Revisão Sistemática da Literatura Embutida (`149` artigos analisados) |
| **Domínio de Aplicação** | *Agent System Mining (ASM)*, Mineração de Processos (*Process Mining*), Modelagem e Simulação Baseada em Agentes (*ABM / MAS*) para Sistemas de Informação Socio-Técnicos |
| **Técnicas / Tecnologias Chave** | **Framework ASM em Modelo V** (5 fases: *Motivate, Plan, Develop, Evaluate, Use*; 7 atividades: *search, project, discover, enhance, integrate, diagnose, check*), Metamodelo UML MAS (*Agent, Environment, Interactions sub-models*), **Disco** (DFMs), **AnyLogic** (*Statecharts* multiagentes), *Hierarchical Markov Models*, *Probabilistic Goal Recognition*, *Nested Petri Nets*, *$\alpha$-algorithm* |
| **Principais Resultados Quantitativos** | RSL sobre **2.094 registros únicos** (*Scopus* + *Web of Science*, 2010–2021) $\to$ `531` filtrados por título $\to$ **149 estudos primários analisados**; demonstração em log de eventos aberto (`10.26188/14401400`) superando o problema do modelo *"spaghetti"* via 3 *statecharts* de agentes executáveis no **AnyLogic** |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Nota | Símbolo | Síntese da Evidência no Artigo |
| :--- | :---: | :---: | :--- |
| **RQ1** (Fundamentos e Taxonomias) | `1.0` | **T** | Fundamenta sistemas socio-técnicos auto-organizáveis (Bertalanffy/Wiener), comportamento emergente **micro vs. macro** (Figura 5, p. 6), 4 propriedades de agentes (**Autonomy, Situatedness, Proactivity, Sociality**) e a transição do *Process Mining top-down* para o **ASM bottom-up**. |
| **RQ2** (Arquiteturas e Orquestração) | `1.0` | **T** | Propõe o **Framework ASM em Modelo V** (5 fases, 3 pontos de vista e 7 operadores formais, Figura 7, p. 8), o **Metamodelo UML MAS** (*agent, environment, interactions sub-models*, Figura 8, p. 10) e cataloga formalismos e algoritmos de inferência multiagente (Seção V.C, pp. 12–13). |
| **RQ3** (Avaliação Empírica e Métricas) | `0.5` | **P** | Apresenta estudo de caso comparando grafos DFM no **Disco** (Figuras 2–3) contra um modelo MAS de 3 agentes no **AnyLogic** (Figura 4, pp. 2–6) sobre log aberto (`10.26188/14401400`), além da síntese bibliométrica de **2.094 $\to$ 149 artigos** (Figura 10, p. 12). |
| **RQ4** (Governança, Riscos e XAI) | `0.5` | **P** | Sistematiza **8 desafios técnicos e metodológicos** do ASM (incluindo validação multi-nível, *overfitting* de tipos de agentes e **privacidade interorganizacional**, Seção IV.D.1–8, pp. 10–11) e benefícios para auditoria de *compliance* e *accountability* (pp. 10, 12). |
| **RQ5** (Lacunas e Agenda Futura) | `1.0` | **T** | Identifica a inexistência de algoritmos *end-to-end* de ASM nos 149 estudos revisados (Seção V.C.2, p. 13) e define uma agenda de pesquisa em 3 pilares: metamodelos MAS, algoritmos de descoberta/integração e métricas de validação micro/macro (Seção VI, p. 13). |
| **SCORE_RQ Total** | **4.0 / 5.0** | — | **80,0% de cobertura global das Questões de Pesquisa da RSL** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1 a QA4)

| Critério DARE | Nota | Símbolo | Justificativa Baseada em Evidências |
| :--- | :---: | :---: | :--- |
| **QA1 — Clareza dos critérios de inclusão/exclusão da revisão** | `1.0` | **Y** | A revisão sistemática embutida (Seção V.A–B, Figura 9, pp. 11–12) estrutura seu protocolo rigorosamente segundo a **Taxonomia de Revisões de Literatura de Cooper** [38] e o framework de **vom Brocke et al.** [37], definindo 3 questões de pesquisa (`RQ1–RQ3`) e critérios explícitos de inclusão (foco na interseção entre ABM/MAS, BPM e Process/Data Mining a partir de 2010). |
| **QA2 — Adequação e abrangência da estratégia de busca e ciência aberta** | `1.0` | **Y** | Transparência metodológica exemplar: reporta as strings exatas (`Q1`, `Q2`, `Q3`), a data exata de execução (`16 February 2021`), a contagem exata de *hits* por consulta no **Scopus** e na **Web of Science**, o fluxo de triagem em duas etapas (`2.094 -> 531 -> 149`, Figura 10, p. 12) e publica abertamente no **Figshare** tanto o log de eventos (`10.26188/14401400`) quanto a lista completa dos 149 artigos selecionados (`10.26188/14708772`). |
| **QA3 — Avaliação de qualidade e validação dos estudos incluídos** | `0.5` | **P** | Os 149 artigos selecionados são categorizados e analisados criticamente em duas grandes correntes (*ABM in BPM* e *Inference of MAS from Event Data*, Seção V.C.1–2, pp. 12–13), porém o artigo não aplica uma matriz individualizada de pontuação de qualidade metodológica para cada um dos 149 estudos primários. |
| **QA4 — Síntese dos resultados e sustentação das conclusões nos dados** | `1.0` | **Y** | A síntese conceitual, o ciclo de vida em Modelo V e a agenda de pesquisa são perfeitamente sustentados tanto pela demonstração empírica no *Disco*/*AnyLogic* quanto pelas evidências extraídas dos 149 artigos revisados. |
| **SCORE_QA Total** | **3.5 / 4.0** | **Alta** | **Qualidade Metodológica Alta (Banda: 3.0–4.0)** |

---

## 5. Parecer Final do Revisor

O estudo **P19 (Tour, Polyvyanyy & Kalenkova, 2021)**, publicado no periódico *IEEE Access* (**Qualis A1 / SJR Q1**), desempenha um papel teórico e metodológico singular no corpus fundacional do *Trabalho I / Trabalho II*. Ao introduzir o paradigma de **Agent System Mining (ASM)**, os autores fornecem a ponte formal entre a análise de logs de eventos operacionais (*Process Mining*) e a modelagem de sistemas multiagentes autônomos (*MAS*). Em ambientes modernos de nuvem e microsserviços, incidentes graves manifestam-se exatamente como o problema dos *"spaghetti models"* descrito no artigo: milhares de eventos entrelaçados que derrotam abordagens monolíticas de correlação. A decomposição proposta pelo ASM — separando **submodelos de agentes individuais**, **submodelo de ambiente** e **submodelo de interações** dentro de um ciclo de vida rigoroso em **Modelo V** (*search, project, discover, enhance, integrate, diagnose, check*) — oferece ao projeto de um *Agentic AI Copilot para Resposta a Incidentes* uma arquitetura formal para minerar comportamentos de agentes, validar simulações *what-if* de mitigação (*log-to-log* e *log-to-model*) e auditar a conformidade (*compliance*) de decisões autônomas em nível micro e macro.
