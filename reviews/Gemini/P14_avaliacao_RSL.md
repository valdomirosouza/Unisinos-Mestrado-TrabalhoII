# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P14
- **Arquivo PDF avaliado:** `P14-A1-Transforming Cybersecurity with Agentic AI to Combat Emerging Cyber Threats.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido (Core Match Integral em Cibersegurança e Operações de SOC).** O artigo investiga diretamente o potencial transformador e os riscos da **Agentic AI** em cibersegurança e **Security Operations Centers (SOCs)**, analisando a automação de triagem de alertas, detecção de ameaças, resposta a incidentes e correção proativa de vulnerabilidades no ciclo de vida de software (*SDLC* via *Code Property Graphs*), documentando cinco plataformas comerciais de agentes de segurança (**CrowdStrike Charlotte AI**, **ReliaQuest GreyMatter**, **Twine Alex**, **Darktrace/ENDPOINT** e **Microsoft Security Copilot** com 11 agentes, Tabela 1, pp. 3–4), propondo um **Risk Management Framework (RMF)** para IA agêntica (Tabela 2, p. 5) e examinando o potencial ofensivo em crimes cibernéticos e diretrizes de governança (Seções 4–6, pp. 5–10).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *Telecommunications Policy* (Elsevier), Volume 49, Artigo 102976, pp. 1–12, 2025 (Recebido em 26 de fevereiro de 2025; Revisado em 18 de abril de 2025; Aceito em 18 de abril de 2025; Disponível online em 22 de abril de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo publicado em periódico científico internacional com revisão por pares (*Telecommunications Policy*, Elsevier), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 12 páginas em inglês com 68 referências e 2 tabelas analíticas.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Diferenciação Funcional e Evolutiva entre *AI Agents* e *Agentic AI* (Seção 2, pp. 2–3):** O artigo traça a evolução histórica desde agentes de software dos anos 1990 até a chamada **"terceira onda da IA" (*Agentic AI / AI super-agents*)** impulsionada por LLMs:
    - **AI Agents:** Sistemas específicos de tarefa (*task-specific*), reativos e restritos a regras predefinidas para atividades rotineiras (ex.: agendamento ou respostas padrão), exigindo reprogramação manual quando o contexto muda;
    - **Agentic AI:** Sistemas com grau superior de autonomia capazes de navegar em ambientes complexos, perseguir metas de longo prazo, empregar **raciocínio adaptativo e planejamento iterativo**, aprender continuamente com a experiência e responder proativamente a mudanças sem intervenção humana constante (pp. 2–3).
  - **Decomposição Modular em Cinco Componentes Cognitivos e Operacionais (Seção 2, p. 2):** Especifica os cinco módulos interconectados que estruturam a operação de um agente: (1) **Interfaces** (comunicação com usuários, sistemas e bancos de dados); (2) **Memory Module** (armazenamento de contexto de curto prazo e conhecimento de longo prazo de interações passadas); (3) **Profile Module** (definição de objetivos, papéis e comportamentos do agente); (4) **Planning Module** (desenvolvimento de planos acionáveis); e (5) **Action Module** (integração de APIs e invocação autônoma de ferramentas como buscas web, execução de código e comandos de recuperação de dados).
  - **Transição de *Chatbots* para *Agent-Driven Cybersecurity* nos SOCs e *vCISO* (Seção 1, pp. 1–2):** Contextualiza a transição operacional nos Centros de Operações de Segurança (*SOCs*) diante de dois fatores críticos: o **tempo de *breakout* de adversários reduzido a apenas `2 minutos e 7 segundos`** e o déficit global de quase **`4 milhões` de profissionais de cibersegurança** (p. 1–2), impulsionando a delegação autônoma de triagem, contenção em tempo real (quarentena de dispositivos e bloqueio de transferências anômalas) e a ascensão de **virtual CISOs (vCISO)** apoiados por agentes.
- **Justificativa:** Cobre integralmente a distinção conceitual entre *AI Agents* e *Agentic AI*, a arquitetura modular em cinco componentes (*Interfaces, Memory, Profile, Planning, Action*) e o modelo decisório autônomo em *SOCs* (`T = 1.0`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Análise de Cinco Plataformas e Arquiteturas Comerciais de *Agentic AI* em SOCs (Seção 3.1–3.6, Tabela 1, pp. 3–4):**
    1. **ReliaQuest GreyMatter (Seção 3.2, p. 4):** Arquitetura multiagente e multimodelo que automatiza tarefas de SOC de **Tier 1 e Tier 2** operando em ambientes privados e segmentados com dados específicos do cliente em tempo real para eliminar alucinações e garantir transparência decisória (implantada em `> 1.000` empresas);
    2. **CrowdStrike Falcon Agent & Charlotte AI Detection Triage (Seção 3.3, p. 4):** Agente de *endpoint* ultraleve (`< 20 MB`) integrado à *CrowdStrike Security Cloud*, combinando modelos **Llama Nemotron** e microsserviços **Nvidia NIM** para triagem autônoma de detecções, *threat hunting* e priorização de vulnerabilidades com reduzida demanda de GPU;
    3. **Twine "Alex" (Seção 3.4, p. 4):** "Funcionário digital" em plataforma *SaaS* voltado a Gestão de Identidade e Acesso (*IAM*) que conecta-se aos sistemas corporativos, cria planos de tarefas, solicita aprovação humana (*human-in-the-loop*) e executa ações de bloqueio com visibilidade total;
    4. **Darktrace / ENDPOINT & Enterprise Immune System (Seções 1 e 3.5, pp. 1, 4):** Agentes leves de autoaprendizado implantados localmente (*on-premise/endpoint*, sem dependência de nuvem) que analisam cada pacote de rede e conexão em tempo real para aprender o comportamento normal da rede e conter ameaças *zero-day*, ataques à cadeia de suprimentos e ameaças internas (*insider threats*);
    5. **Microsoft Security Copilot (Seção 3.6, p. 4):** Ecossistema orquestrado de **11 agentes de IA especializados por tarefa** (`6` desenvolvidos pela Microsoft integrados ao *Defender, Purview Data Security Investigations — DSI, Entra* e *Intune*, e `5` desenvolvidos por parceiros — *OneTrust, Aviatrix, BlueVoyant, Tanium, Fletch* — para notificação de vazamentos, diagnóstico de rede, avaliação de controles de SOC e previsão de ameaças).
  - **Mecanismos Avançados: *AppSec* com *Code Property Graph (CPG)*, *Agentic RAG* e Arquitetura Híbrida *Agent + Agentless* (Seção 3, p. 3; Seção 4.1, p. 6; Seção 6.1, p. 9):**
    - Descreve o uso de agentes no ciclo de vida de software (*SDLC*) que constroem um **Code Property Graph (CPG)** agnóstico de linguagem para identificar falhas pelo seu impacto estrutural e **gerar correções automáticas sensíveis ao contexto e *non-breaking*** (Seção 3, p. 3);
    - Diferencia o *RAG* convencional do **Agentic RAG** (Seção 4.1, p. 6), no qual múltiplos subagentes gerenciam conjuntos distintos de documentos, refinam consultas iterativamente, avaliam a confiabilidade das fontes e fornecem rastreabilidade explícita da origem dos dados (*document searches, web queries, databases*);
    - Propõe na Seção 6.1 (p. 9) uma arquitetura híbrida combinando **soluções baseadas em agentes** (para proteção profunda de bancos de dados sensíveis) e **soluções *agentless*** (para visibilidade rápida e escalabilidade em cargas efêmeras de nuvem, como contêineres e funções *serverless*).
  - **Limitação:** Por se tratar de um estudo de políticas e gestão estratégica de cibersegurança, não apresenta diagramas de arquitetura de software, protocolos formais de comunicação inter-agentes nem pseudocódigos.
- **Justificativa:** Documenta com riqueza as arquiteturas comerciais de *Agentic SOC* (*GreyMatter, Charlotte AI + Nvidia NIM, Darktrace, Microsoft 11-agent Security Copilot*), *Code Property Graphs* e *Agentic RAG*, mas sem especificação técnica de baixo nível (`P = 0.5`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Indicadores Quantitativos Operacionais de Resposta a Incidentes e Triagem em SOCs (Seção 1, p. 1; Seção 3.1–3.6, Tabela 1, pp. 3–4):**
    - **CrowdStrike Charlotte AI Detection Triage:** Acurácia superior a **`98%` na triagem de detecções de segurança**, automatizando **mais de `40 horas` semanais de trabalho manual** nas operações de SOC (Tabela 1, pp. 3–4);
    - **ReliaQuest GreyMatter:** Processa alertas de segurança **`20 vezes` mais rápido** que métodos tradicionais, **aumenta a acurácia de detecção de ameaças em `30%`** (Seção 3.2, p. 4), **automatiza `98%` dos alertas de segurança** e reduz o **tempo de contenção de ameaças (*threat containment time*) para menos de `5 minutos`** em mais de `1.000` empresas (Tabela 1, pp. 3–4);
    - **Darktrace / ENDPOINT:** **Reduz o tempo de triagem (*triage time*) em `90%`** (Tabela 1, p. 3);
    - **Microsoft Security Copilot (11 agentes):** **Redução de `30%` no Tempo Médio de Resposta (*Mean Time to Respond — MTTR*)** a incidentes de segurança; profissionais em início de carreira tornam-se **`26%` mais rápidos e `35%` mais precisos** no tratamento de ameaças, enquanto profissionais experientes tornam-se **`22%` mais rápidos e `7%` mais precisos** (Tabela 1, p. 3);
    - **Indicadores Macroeconômicos e Organizacionais (Seções 1 e 6.1, pp. 1, 7–8):** Previsão do Gartner de que a IA aumentará a **eficiência dos SOCs em `40%` até 2026** (p. 1); salário anual mediano de analistas de segurança nos EUA de **`US$ 120.360`** em 2023 contrastado com a previsão da Forrester de que **`75%` dos projetos internos (*in-house*) de agentes de IA falharão** devido à subestimação dos custos contínuos de manutenção, monitoramento e otimização (pp. 7–8).
  - **Limitação:** Todas as métricas de desempenho (Tabela 1) provêm de relatórios da indústria e comunicados de fornecedores (*CrowdStrike, ReliaQuest, Darktrace, Microsoft, Gartner, Forrester*), sem validação experimental independente conduzida pelo autor.
- **Justificativa:** Fornece métricas diretamente alinhadas à nossa RSL (*MTTR* `-30%`, tempo de contenção `< 5 min`, redução de triagem em `-90%`, acurácia `>98%` e economia de `>40h/semana`), porém baseadas em dados secundários de fornecedores (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Framework de Gestão de Riscos para *Agentic AI* — *Threat + Vulnerability + Potential Impact* (Seção 4.1–4.3, Tabela 2, pp. 5–7):** Adapta o **NIST Risk Management Framework (NIST SP 800-37r2)** em três dimensões analíticas (Tabela 2, p. 5):
    1. **Threats (Seção 4.1, pp. 5–6):** Expansão da superfície de ataque ao longo de toda a cadeia invisível de interações iniciadas por agentes; risco de **"Shadow AI"** (funcionários implantando agentes públicos ou assistentes de código como *GitHub Copilot* sem autorização, vazando dados ou inserindo código vulnerável); propagação em cascata de compromissos em sistemas multiagentes interconectados; aplicação do conceito biológico de **"Rare Enemy Syndrome"** (Dawkins, 1982) para explicar a vulnerabilidade a vetores inéditos como **Prompt Probing** (sondagem sistemática para *jailbreak* ou aprovação de transações fraudulentas) e falhas de infraestrutura em **Agentic RAG** (incluindo múltiplos **CVEs não corrigidos no *Ollama* e servidores mal configurados executando *llama.cpp* e *ChromaDB***, expondo milhares de LLMs a roubo de dados e sabotagem, p. 6);
    2. **Vulnerabilities (Seção 4.2, p. 6):** Distingue **vulnerabilidade objetiva** (falhas de software/hardware e provedores terceirizados expondo PII) de **vulnerabilidade subjetiva** (subestimação do risco e uso descuidado de agentes que operam sem rastreabilidade total), destacando o efeito multiplicador de agentes de logística ou TI comprometidos que propagam comandos maliciosos para toda a cadeia de suprimentos;
    3. **Potential Impact (Seção 4.3, pp. 6–7):** Escalonamento abrupto de taxas de falha (de `2%` gerenciáveis para `100%`, causando paradas sistêmicas catastróficas), transformação de assistentes pessoais em ferramentas de vigilância e perfilamento de PII, danos físicos em veículos autônomos e sanções sob **GDPR**, **CCPA** e **HIPAA**.
  - **Potencial Malicioso em Crimes Cibernéticos e Assimetria Econômica (Seção 5, p. 7):** Demonstra que o envenenamento de apenas `0,01%` de *datasets* massivos (*LAION-400M* ou *COYO-700M*) custou aos atacantes apenas **`US$ 60`**, gerando impacto desproporcional; documenta o **aumento de `45%` em fraudes de identidade sintética (*synthetic identity fraud*)** em *fintechs* em 2024 impulsionado por IA generativa/agêntica; e analisa campanhas de *phishing* autoaperfeiçoadas e operações multi-estágio combinando *deepfakes* e *ransomware*.
  - **Mecanismos de Governança, *Guardrails* e Controles de Segurança (Seção 6.1, pp. 8–9):** Propõe uma arquitetura de defesa em múltiplas camadas:
    - Combinação de salvaguardas dos provedores (*OpenAI, Anthropic, Google*) com **AI Gateways corporativos**, **guardrails internos de entrada/saída**, filtragem de *prompts* e **aplicação estrita de políticas sobre as ações (*policy enforcement for actions*)**, ressaltando que **sistemas multiagentes com papéis bem definidos e ações restritas são mais fáceis de proteger do que um único LLM monolítico complexo** (p. 9);
    - Governança de **onboarding/offboarding de agentes** integrada aos sistemas de RH e IAM corporativos com permissões explícitas, **acesso de privilégio mínimo (*least-privilege access*)**, **separação entre zonas confiáveis e não confiáveis**, **trilhas de auditoria (*audit trails*)**, **isolamento e contenção de brechas** para impedir cascatas entre agentes e **restrição do nível de autonomia baseada em risco** (p. 8);
    - Uso de **Privacy-Enhancing Technologies (PETs)**, revisão de políticas de **BYOD** em favor de dispositivos gerenciados pela empresa e políticas formais de aquisição e orçamento cobrindo todo o ciclo de vida pós-implantação (p. 8–9).
- **Justificativa:** Oferece uma análise exemplar dos riscos técnicos (*Shadow AI, Prompt Probing*, CVEs em *Ollama/llama.cpp/ChromaDB*, envenenamento de dados a `US$ 60`, fraude sintética `+45%`), desafios regulatórios (*GDPR, CCPA, HIPAA*) e controles de governança corporativa para sistemas multiagentes (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Agenda de Pesquisa Futura em Cibersegurança Agêntica (Seção 6.2, pp. 9–10):** Propõe três direções estratégicas e teóricas originais para investigação futura:
    1. **Dinâmica Organizacional do Cibercrime e *Ransomware-as-a-Business (RaaB)*:** Investigar como organizações cibercriminosas — que historicamente espelham modelos de negócios corporativos legítimos — adotarão agentes autônomos de IA e como se dará a corrida armamentista contínua entre empresas de segurança de TI e sindicatos de *ransomware*;
    2. **Limiares Técnicos de Autonomia Ofensiva Total e Mudança na Assimetria Atacante-Defensor:** Determinar os limiares técnicos e estratégicos a partir dos quais agentes ofensivos superarão sua atual falta de confiabilidade para executar ataques de ponta a ponta (da infiltração na rede à exfiltração de dados) sem intervenção humana, avaliando como a *Agentic AI* altera o balanço econômico e tático entre atacantes de poucos recursos e defensores;
    3. **Aplicação da Teoria Principal-Agente (*Principal-Agency Theory*) a Redes de Cibercrime Agêntico:** Utilizar a teoria econômica e sociológica de *principal-agent* (Eisenhardt, 1989; Kiser, 1999) para modelar como líderes criminosos (*principals*) delegam autoridade a agentes autônomos de IA (*agents* desprovidos de motivos pessoais, mas sujeitos a erros de programação, alucinações e perda de controle), gerenciando custos de agência, alinhamento de objetivos ilícitos e evasão de detecção.
- **Justificativa:** Formula uma agenda de pesquisa altamente original que articula limiares de autonomia ofensiva, corrida armamentista em *RaaB* e *Principal-Agency Theory* aplicada à delegação para agentes autônomos (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 0.5 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P14 |
| **Autores** | Nir Kshetri |
| **Ano** | 2025 |
| **Título** | *Transforming cybersecurity with agentic AI to combat emerging cyber threats* |
| **Periódico / Fonte** | *Telecommunications Policy* (Elsevier), Vol. 49, Art. 102976, pp. 1–12 |
| **DOI** | `10.1016/j.telpol.2025.102976` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Artigo de Análise Estratégica, Políticas e Gestão de Riscos com Estudos de Caso Industriais (68 referências) |
| **Domínio Principal** | *Agentic AI* em Cibersegurança e Operações de SOC: Automação de Triagem e Resposta a Incidentes, Gestão de Riscos (*NIST RMF*), Cibercrime e Governança |
| **Tecnologias / Frameworks Analisados** | **CrowdStrike Falcon Agent / Charlotte AI Detection Triage** (*Llama Nemotron + Nvidia NIM*), **ReliaQuest GreyMatter**, **Twine "Alex"**, **Darktrace / ENDPOINT** (*Enterprise Immune System*), **Microsoft Security Copilot** (11 agentes especializados: *Defender, Purview DSI, Entra, Intune* + 5 parceiros), **Agentic RAG**, **Code Property Graph (CPG)** para *AppSec*, *Ollama / llama.cpp / ChromaDB*, **NIST Risk Management Framework (SP 800-37r2)**, *Privacy-Enhancing Technologies (PETs)* |
| **Escopo de Aplicação** | Automação de *Security Operations Centers (SOCs)* (triagem de alertas, contenção de ameaças, *threat hunting*, *IAM* e redução de *MTTR*), correção autônoma de vulnerabilidades no *SDLC* e governança de segurança corporativa |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Distinção entre *AI Agents* (específicos de tarefa, reativos, baseados em regras) e *Agentic AI / super-agents* (autonomia elevada, raciocínio adaptativo, planejamento iterativo, aprendizado contínuo, Seção 2, pp. 2–3); 5 módulos (*Interfaces, Memory, Profile, Planning, Action*, p. 2); transição em SOCs frente a *breakout time* de `2m07s` e déficit de `4M` profissionais (pp. 1–2). |
| **RQ2** (Arquiteturas e Orquestração) | `P` | `0.5` | Análise de 5 plataformas comerciais de *Agentic SOC* (Seção 3.1–3.6, Tabela 1, pp. 3–4: *ReliaQuest GreyMatter, CrowdStrike Charlotte AI + Nvidia NIM, Twine Alex, Darktrace/ENDPOINT, Microsoft Security Copilot* com 11 agentes); **Code Property Graph (CPG)** para correção *non-breaking* no SDLC (p. 3); **Agentic RAG** com subagentes e rastreabilidade (p. 6); e arquitetura híbrida *agent + agentless* (p. 9). Sem diagramas de engenharia de baixo nível. |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Métricas operacionais de SOC (Tabela 1, pp. 3–4): **CrowdStrike Charlotte AI** (`>98%` acurácia em triagem, `>40h/semana` economizadas); **ReliaQuest GreyMatter** (alertas `20x` mais rápidos, `+30%` acurácia, `98%` alertas automatizados, contenção `< 5 min` em `>1.000` empresas); **Darktrace** (`-90%` tempo de triagem); e **Microsoft Security Copilot** (**`-30%` no MTTR**, analistas juniores `26%` mais rápidos e `35%` mais precisos). Dados secundários de mercado/fornecedores. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | **Risk Management Framework (Tabela 2, pp. 5–7):** *Shadow AI*, *Rare Enemy Syndrome*, **Prompt Probing**, vulnerabilidades em **Agentic RAG** (CVEs em *Ollama*, *llama.cpp* e *ChromaDB*, p. 6), vulnerabilidade objetiva vs. subjetiva, envenenamento de dados por `US$ 60` (`0,01%` do *LAION-400M*), alta de `45%` em fraude de identidade sintética (p. 7), falha de `75%` dos projetos internos (Forrester, p. 8) e governança via *AI gateways*, *onboarding/offboarding* em RH/IAM, privilégio mínimo, isolamento de brechas multiagentes, *PETs* e *GDPR/CCPA/HIPAA* (pp. 8–9). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Agenda futura na Seção 6.2 (pp. 9–10): adoção de agentes autônomos por organizações de *Ransomware-as-a-Business (RaaB)*, limiares técnicos/estratégicos para ataques 100% autônomos (*infiltration-to-exfiltration*), mudança na assimetria atacante-defensor e aplicação da **Teoria Principal-Agente (*Principal-Agency Theory*)** a redes cibercriminosas agênticas. |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Alta Aderência (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | Define explicitamente na Seção 1 (p. 2) o escopo analítico e as duas questões de pesquisa centrais do estudo (*RQ1: How can agentic AI transform cybersecurity practices in addressing emerging threats?* e *RQ2: What are the cybersecurity risks associated with agentic AI?*). |
| **QA2 — Busca e transparência metodológica** | `P` | `0.5` | Estrutura a análise sobre referenciais teóricos explícitos — o **NIST Risk Management Framework (SP 800-37r2)** (*Threat + Vulnerability + Impact*, Tabela 2, p. 5), a teoria de **Vulnerabilidade Objetiva e Subjetiva** (Busetta & Milito, 2009), a **Rare Enemy Syndrome** (Dawkins, 1982) e a **Principal-Agency Theory** (Eisenhardt, 1989) —, mas não documenta protocolo sistemático de busca ou seleção bibliográfica. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza cinco casos industriais de referência em SOCs na Tabela 1 (p. 3) e estrutura a matriz de risco na Tabela 2 (p. 5), porém baseia grande parte das evidências empíricas em literatura cinzenta, relatórios de consultorias (*Gartner, Forrester, BCG*) e comunicados de imprensa de fabricantes (*Business Wire, VentureBeat, SecurityWeek*), sem triangulação experimental independente. |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | Responde diretamente às duas questões de pesquisa na Seção 6 (p. 7) e oferece recomendações de governança maduras e equilibradas (Seção 6.1, pp. 7–9), embora aceite os indicadores promocionais de fornecedores na Seção 3 sem discutir os vieses de relato inerentes a *white papers* comerciais. |
| **Total (`SCORE_QA`)** | **Banda: Média** | **2.5 / 4.0** | **Qualidade Metodológica Moderada-Alta (62,5%)** |

---

## Parecer Final do Revisor

O artigo **P14** (Kshetri, 2025), publicado na *Telecommunications Policy* e integrante do **Corpus Fundacional** do Trabalho I, possui altíssima relevância temática para o núcleo da nossa RSL sobre *Agentic AI Copilot para Resposta a Incidentes* (`SCORE_RQ = 4.0 / 5.0`; `SCORE_QA = 2.5 / 4.0`, banda **Média**). É o estudo do corpus fundacional que mais diretamente analisa a implantação de **Agentic AI em Security Operations Centers (SOCs)**, compilando métricas operacionais de cinco plataformas líderes (**CrowdStrike Charlotte AI**, **ReliaQuest GreyMatter**, **Twine Alex**, **Darktrace/ENDPOINT** e os **11 agentes do Microsoft Security Copilot**, com reduções reportadas de **`30%` no MTTR**, **`90%` no tempo de triagem** e contenção em **`< 5 minutos`**, Tabela 1, p. 3). Além disso, oferece contribuições fundamentais para a **RQ4** ao adaptar o **NIST Risk Management Framework** à IA agêntica (expondo riscos de *Shadow AI*, *Prompt Probing* e CVEs em pilhas de *Agentic RAG* como *Ollama, llama.cpp* e *ChromaDB*) e propor controles de governança essenciais (como *onboarding/offboarding* de agentes em RH/IAM, restrição de autonomia baseada em risco e separação de papéis em sistemas multiagentes).
