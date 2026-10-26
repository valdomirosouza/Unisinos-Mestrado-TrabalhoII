# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P28
- **Título:** *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models*
- **Autores:** Yasser Hmimou; Mohamed Tabaa; Azeddine Khiat; Zineb Hidila
- **Periódico/Conferência:** *IEEE Access*, Vol. 13, pp. 150199–150215 (Publicado em 25 de agosto de 2025; versão atual em 2 de setembro de 2025)
- **DOI:** `10.1109/ACCESS.2025.3602681`
- **Arquivo avaliado:** `P28-A1-A_Multi-Agent_System_for_Cybersecurity_Threat_Detection_and_Correlation_Using_Large_Language_Models.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental (*Research Article*), propondo e avaliando uma arquitetura multiagente modular integrada a LLMs (`LLaMA 3.3-70B` via API Groq) para detecção, correlação multi-domínio e explicação de ameaças cibernéticas.
- **Foco técnico:** Orquestração de agentes especializados em três superfícies de ataque — verificação de e-mails (*phishing*), análise de *logs* de servidores/rede e varredura de faixas de IP/vulnerabilidades (CVEs) — coordenados por um *Task Dispatcher Agent* e unificados por um *Contextual Recommendation System* para triagem explicável (*XAI*) e resposta a incidentes em SOCs.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Totalmente atendido. O sistema multiagente atua diretamente como um copiloto/sistema de suporte à decisão para analistas de segurança na detecção, correlação multi-vetor, explicação passo a passo (*Chain-of-Thought*) e recomendação de remediação de incidentes cibernéticos.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *IEEE Access*, Vol. 13, 2025).
  - *IC3 (Rigor técnico/metodológico):* Atendido (arquitetura detalhada em 4 camadas, integração de ferramentas reais de segurança, avaliação quantitativa por agente e em *pipeline* completo, mais validação cega com 3 analistas humanos em 60 cenários).
- **Critérios de Exclusão (EC):** Não incide em nenhum critério de exclusão.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (apenas para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P28 | IEEE Access | 2025 | [VERIFICAR] | Q1 [VERIFICAR] | A1 [VERIFICAR] | Artigo Experimental / Empírico (Primário) | `10.1109/ACCESS.2025.3602681` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A1`) não constam no texto do PDF e devem ser auditados nas fontes oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *IEEE Xplore / Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P28 | A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models | **RQ1** (Contexto e Definições) | Respondida Plenamente | **T** (1.0) | Seção II (pp. 150200–150202); Seção III (pp. 150202–150206); Seção IV-D (pp. 150208–150209); Seção VI (p. 150213) | **(a) Definição de autonomia:** Posiciona explicitamente o sistema como uma arquitetura multiagente *workflow-driven* de suporte à decisão (*human-in-the-loop*), na qual os LLMs atuam como processadores semânticos modulares dentro de *pipelines* determinísticos, sem autonomia cognitiva irrestrita, preservando a supervisão humana em operações críticas de SOC (pp. 150200, 150202, 150208, 150213). **(b) Características centrais:** Especialização por domínio (e-mail, *logs*, rede/IP), módulos de memória local e de contexto para correlação temporal entre sessões, uso de ferramentas clássicas de segurança e raciocínio explicável via RAG e *Chain-of-Thought* (CoT). **(c) Modelo decisório:** Filtragem simbólica/determinística seguida de enriquecimento semântico via LLM e fusão inter-domínios (sintática por RegEx e temporal por *timestamps*) no *Contextual Recommendation System* (Figura 6, p. 150206). |
| P28 | A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seção III, Figuras 1–6 (pp. 150202–150206); Seção IV, Figuras 7–8, Tabela 2 (pp. 150206–150209) | **(a) Tipo de arquitetura:** Sistema multiagente modular em 4 camadas (Figura 1, p. 150202): interface de usuário, *Task Dispatcher Agent* (validação, classificação e fila assíncrona, Figura 2), 3 agentes especialistas (*Email Verification Agent* na Figura 3, *Log Analyzer Agent* na Figura 4 e *IP Range Analyzer Agent* na Figura 5) e *Contextual Recommendation System* centralizado (Figura 6). **(b) Ferramentas/frameworks:** `LLaMA 3.3-70B Versatile` via *Groq API*; *FAISS* (busca vetorial), *RegEx*, `tldextract`, `dns.resolver`, `TextBlob` e *NLTK*; *ELK Stack* (*Elasticsearch, Logstash, Kibana*) e *Suricata* (IDS); módulo Python `ipaddress`, *Nmap* e API do *NVD* (CVEs/CVSS) (Tabela 2, p. 150207). **(c) Capacidades avançadas:** RAG integrado a bases de *phishing* e NVD (Figura 7), *Chain-of-Thought* estruturado, memória de histórico de sessões e arquivamento centralizado (*Central Logging and Archiving*, Figura 8, p. 150209) de todos os *prompts* e saídas para auditoria e *red teaming*. |
| P28 | A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models | **RQ3** (Benefícios e Evidências) | Respondida Plenamente | **T** (1.0) | Seção V, Tabelas 4–7, Figuras 9–12 (pp. 150209–150213) | **(a) Benefícios qualitativos:** Geração de narrativas explicáveis (*XAI*) rastreáveis até linhas exatas de *logs*, redução da carga cognitiva e recomendações de mitigação adaptadas ao perfil operacional (engenheiro de segurança ou gestor de risco, p. 150205). **(b) Benefícios quantitativos:** No nível de agente (Tabela 5, Figura 9, p. 150211): *Log Analyzer* (`Acc = 91.8%`, `FPR = 8.7%`, `Explanation Success = 89.5%`), *IP Range Analyzer* (`Acc = 92.7%`, `FPR = 5.4%`, `Explanation Success = 93.2%`) e *Email Verification* (`Acc = 94.1%`, `FPR = 6.2%`, `Explanation Success = 91.4%`). No *pipeline* integrado em 60 tarefas multi-domínio avaliadas por 3 analistas humanos cegos ao *ground truth* (Tabela 6, Figuras 10–12, pp. 150211–150213): `System-Wide Accuracy = 93.6%` (`F1 = 0.94`), `Threat Correlation Precision = 87.0%`, redução de falsos positivos de `41.3%` (vs. SIEM de referência), redução média no tempo de triagem do analista de `38.5%` e escore médio de confiança humana de `4.6 / 5.0`. **(c) Nível de evidência:** Experimentos controlados com *datasets* públicos (*SpamAssassin*, *CIC-IDS 2017*), dados sintéticos/emulados e avaliação cega com analistas humanos. |
| P28 | A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models | **RQ4** (Desafios e Ética) | Respondida Plenamente | **T** (1.0) | Seção II (p. 150202); Seção IV-D (pp. 150208–150209); Seção VI (p. 150213) | **(a) Desafios técnicos:** Dependência de ferramentas e APIs externas (*Nmap*, *Groq*) que podem introduzir gargalos de latência em ambientes de alto *throughput* e atuar como pontos únicos de falha (*single points of failure*); custo computacional e risco de inconsistência das explicações entre mudanças de *prompts* ou atualizações do LLM; e defasagem de *datasets* legados frente a ameaças emergentes (Seção VI, p. 150213). **(b) Desafios éticos/governança:** Alerta contra a automação opaca (*opaque automation*) e a delegação de decisão autônoma livre a LLMs em operações críticas de segurança que exigem conformidade, rastreabilidade e supervisão humana inegociáveis, além de restrições locais de privacidade (p. 150213). **(c) Mecanismos de governança:** Confinamento dos LLMs a *workflows* determinísticos pré-roteirizados sem autonomia decisória livre, validação estrita no *Task Dispatcher*, registro integral de *prompts*/saídas para trilha de auditoria (Figura 8) e arquitetura modular com *fallback* para modelos locais (p. 150213). |
| P28 | A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção VI (*Conclusion and Future Work*, p. 150213) | Aponta quatro direções futuras explícitas (p. 150213): (1) integração de entradas multimodais (anexos, links embutidos e *payloads* visuais) para detecção de *phishing* e engenharia social avançada; (2) aprimoramento da responsividade em tempo real adaptando o agente de *logs* para fluxos contínuos de dados (*continuous data streams*) e execução assíncrona resiliente; (3) exploração de modelos de implantação federada (*federated deployment*) para infraestruturas distribuídas com restrições locais de privacidade; e (4) adoção de variantes mais leves de LLMs para implantação em borda (*edge systems*) ou ambientes de baixa largura de banda mantendo clareza semântica e rastreabilidade. |
| **P28** | **SCORE_RQ Total** | — | **5.0 / 5.0** | — | — | Atende plenamente todas as cinco questões de pesquisa da RSL (RQ1 a RQ5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P28 | Artigo Experimental / Empírico (Primário) | Y (1.0) | P (0.5) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** O problema da fragmentação em silos das ferramentas tradicionais de segurança (IDS baseados em regras e antivírus baseados em assinaturas), a incapacidade de correlacionar ataques multi-estágio/APTs e a necessidade de explicabilidade para reduzir o tempo de triagem são claramente articulados, assim como a proposta da arquitetura multiagente baseada em *workflows* e LLMs (Seções I e III, pp. 150199–150202).
- **QA2 — Metodologia Replicável (P = 0.5):** Descreve detalhadamente a arquitetura de 4 camadas e os fluxos de cada agente (Figuras 1–8), o conjunto de ferramentas (Tabela 2), os *datasets* empregados (Seção IV-C) e as definições matemáticas das métricas (Tabela 4). Entretanto, não disponibiliza os *templates* literais dos *prompts*, não especifica qual plataforma SIEM serviu de *baseline* para as comparações de redução de falsos positivos (41,3%) e tempo de triagem (38,5%), mantém privado o *dataset* de 2.000 e-mails sintéticos e os *scripts* de geração das 60 tarefas (disponíveis apenas mediante solicitação, p. 150208) e apresenta pequenos descuidos editoriais (repetição literal de um parágrafo inteiro nas pp. 150204 e 150208, e erro de digitação na Tabela 3, p. 150209, onde o *CIC-IDS 2017* aparece associado a `Email` / `Email Verification Agent`).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Conduz validação experimental estruturada em duas fases: (i) avaliação individual dos três agentes especializados utilizando *SpamAssassin* (~6.000 mensagens), *CIC-IDS 2017*, ~2.000 e-mails de *phishing* gerados por LLM e ambiente virtualizado escaneado com *Nmap*/NVD (Tabela 5, Figura 9); e (ii) avaliação integrada do *pipeline* completo sobre 60 tarefas multi-domínio julgadas por três analistas humanos cegos ao *ground truth*, medindo acurácia global (93,6%), precisão de correlação (87,0%), redução de falsos positivos (41,3%), redução do tempo de triagem (38,5%) e confiança do analista (4,6/5,0) (Tabela 6, Figuras 10–12).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões são diretamente sustentadas pelas evidências quantitativas e qualitativas coletadas, e a Seção VI (p. 150213) analisa de forma crítica e transparente as limitações do estudo e ameaças à validade (dependência de APIs externas como pontos únicos de falha e latência, custo e estabilidade das explicações geradas por LLMs e uso de *datasets* legados).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
Este artigo apresenta uma arquitetura multiagente modular para detecção, correlação e explicação de ameaças cibernéticas que combina três agentes de domínio (*Email Verification*, *Log Analyzer* e *IP Range Analyzer*), um despachante assíncrono (*Task Dispatcher*) e um correlacionador central (*Contextual Recommendation System*) impulsionados pelo `LLaMA 3.3-70B` (via Groq API), RAG (*FAISS*/NVD) e *Chain-of-Thought*. Um diferencial conceitual importante para a RSL é a defesa explícita de agentes governados por *workflows* determinísticos (em vez de autonomia cognitiva livre) para garantir auditabilidade, controle e supervisão humana em SOCs. Os experimentos demonstram 93,6% de acurácia global, 87,0% de precisão de correlação inter-agentes, 41,3% de redução em falsos positivos e 38,5% de redução no tempo de triagem de analistas humanos (`SCORE_RQ = 5.0/5.0`, `SCORE_QA = 3.5/4.0`).

### Recomendação
**INCLUIR** — Estudo primário de altíssima aderência ao escopo da RSL (`SCORE_RQ = 5.0/5.0` e `SCORE_QA = 3.5/4.0`, Banda Alta), fornecendo evidências quantitativas e humanas diretas sobre o impacto de um *Agentic AI Copilot* multi-domínio na redução de falsos positivos, tempo de triagem e aumento da confiança de analistas em resposta a incidentes de cibersegurança.

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *IEEE Xplore*, *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *IEEE Access* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A1` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
