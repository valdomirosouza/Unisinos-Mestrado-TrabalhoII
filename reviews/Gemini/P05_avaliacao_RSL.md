# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P05
- **Arquivo PDF avaliado:** `P05-A1-A Survey of AIOps in the Era of Large Language Models.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo realiza a primeira revisão sistemática abrangente sobre **AIOps na era dos Large Language Models (LLM4AIOps)**, cobrindo todo o ciclo operacional de gerenciamento de falhas em sistemas distribuídos de larga escala: pré-processamento de dados e novas fontes semânticas (relatórios de incidentes, código-fonte, *QA*), percepção de falhas (*failure prevention, failure prediction, anomaly detection*), análise de causa raiz (*failure localization, failure category classification, root cause report generation*) e remediação assistida/autônoma em cinco níveis progressivos de automação (*Assisted Questioning* até *Automatic Execution*), incluindo agentes baseados em LLMs e *Tool-Augmented Generation (TAG)*.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em setembro de 2025 no periódico *ACM Computing Surveys (CSUR)*, Volume 58, Número 2, Artigo 44 (Recebido em 23 de junho de 2024; Revisado em 22 de abril de 2025; Aceito em 19 de junho de 2025; Publicado em setembro de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão sistemática publicado no principal periódico de *surveys* da ciência da computação (*ACM Computing Surveys*), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 35 páginas em inglês com protocolo sistemático rigoroso e cobertura direta do domínio de operações de TI e resposta a incidentes.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Limitações estruturais do AIOps tradicional (ML/DL) vs. Paradigma *LLM4AIOps* (Seção 1.1, pp. 2–3):** Identifica cinco gargalos do AIOps clássico baseado em ML/DL: (1) necessidade de engenharia complexa de atributos (*feature extraction*); (2) falta de generalidade entre plataformas (*lack of cross-platform generality*); (3) falta de flexibilidade entre tarefas (*lack of cross-task flexibility*); (4) adaptabilidade limitada a mudanças de software; e (5) níveis restritos de automação (estagnados em triagem ou recomendação estática). Demonstra como os LLMs superam esses limites via compreensão nativa de dados não estruturados, raciocínio lógico *cross-platform*, execução multitarefa em linguagem natural, adaptação contínua via *RAG* e geração/execução autônoma de scripts e ferramentas.
  - **Transformação das Fontes de Dados e do Fluxo de *Root Cause Analysis* (Seção 3.2, Fig. 6, pp. 9–11; Seção 4.2, Fig. 8, pp. 12–13):** Mostra que o AIOps evoluiu do uso exclusivo de dados gerados por máquina (*metrics, logs, traces*) para a fusão com dados gerados por humanos (*Software Information/Architecture/Config*, *Source Code*, *Question & Answer* e *Incident Reports* submetidos a *On-Call Engineers — OCEs*).
  - **Escala evolutiva de 5 níveis de automação na Remediação de Incidentes (Seção 4.3, Fig. 9, pp. 14–15):** Com base na literatura (especialmente estudos da Microsoft) e em entrevistas com *On-Call Engineers (OCEs)* de empresas parceiras, formaliza a transição gradual de assistência humana para autonomia total em cinco estágios: (1) *Assisted Questioning* $\to$ (2) *Mitigation Solution Generation* $\to$ (3) *Command Recommendation* $\to$ (4) *Script Generation* $\to$ (5) *Automatic Execution* (execução ponta a ponta sem intervenção manual).
- **Justificativa:** Fundamenta de forma exemplar a transição tecnológica do AIOps clássico para o *LLM4AIOps* e estabelece uma taxonomia de cinco níveis de automação na resolução de incidentes validada com engenheiros de plantão (*OCEs*).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia de Cinco Famílias Metodológicas e Arquiteturais (Seção 5, Fig. 10, pp. 15–21):** Classifica as arquiteturas de *LLM4AIOps* em:
    1. **Foundation Models (Seção 5.1, pp. 16–17):** *Encoder-only* (*LoFI*, *ART*), *Decoder-only* (*Lag-Llama*, *TimesFM*, *ShellGPT*, *Timer*) e *Encoder-decoder* (*TimeGPT*, *SimMTM*, *PreLog*, *KAD-Disformer*);
    2. **Fine-tuning Approaches (Seção 5.2, pp. 17–18):** *Full Fine-Tuning* (*PromptCast*, *UniTime*, *AnomalyLLM*, *RAG4ITOps*) e *Parameter-Efficient Fine-Tuning — PEFT* (*OWL* com *mixture-of-adapters* em LLaMA2-13B, *LLM4TS*, *LogLM*, *LLMParser*);
    3. **Embedding-based Approaches (Seção 5.3, p. 18):** *Pre-trained Embedding* e *Prompt Embedding* (*Time-LLM* com *Prompt-as-Prefix*, *TEST*, *TEMPO*);
    4. **Prompt-based Approaches (Seção 5.4, pp. 18–20):** *In-Context Learning — ICL* com cache adaptativo (*LILAC*, *DivLog*, *LogBatcher*, *RCACopilot*, *Xpert*, *LasRCA*), *Chain-of-Thought — CoT* (*LSTPrompt*, *LogGPT*, *RealTCD*, *LM-PACE*) e *Task Instruction Prompting* (*Sigllm*, *TabLLM*);
    5. **Knowledge-based & Agentic Approaches (Seção 5.5, pp. 20–21):** Divide-se em **Retrieval-Augmented Generation (RAG)** (*MonitorAssistant*, *RAGLog*, *LogRAG*, *LLMDB*, *DB-GPT*, *LogExpert*, *Oasis*) e **Tool-Augmented Generation (TAG) / Sistemas Agênticos**, destacando agentes que invocam ferramentas de diagnóstico e execução em nuvem: **RCAgent** [133], **RCACopilot** [16], agente GPT-4 com 150 ferramentas Linux de Cao et al. [9], **NetLM** [129], **LLexus** [64] (integração de ferramentas semânticas e scripts baseados em *Troubleshooting Guides — TSGs*), **AIOpsLab** [14, 117] (interface agente-nuvem com injeção de falhas via *chaos engineering*), **mABC** [168] (colaboração multiagente inspirada em *blockchain* para RCA em microsserviços) e **AgentFM** [159] (multiagentes orientados a papéis para bancos de dados distribuídos).
- **Justificativa:** Oferece um mapeamento arquitetural completo do ecossistema *LLM4AIOps*, cobrindo desde modelos fundacionais de séries temporais/logs até sistemas agênticos com *RAG*, *TAG* e coordenação multiagente.

### RQ3 — Evidências Empíricas e Métricas Operacionais (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Sistematização das Metodologias de Avaliação, Métricas e *Benchmarks* de AIOps (Seção 6, Fig. 11, pp. 21–24):** O artigo dedica uma questão de pesquisa inteira (RQ4 do survey) à avaliação empírica de sistemas *LLM4AIOps*, estruturando quatro famílias de métricas (Fig. 11, p. 21):
    1. **Classification Task Metrics (Seção 6.1.1, pp. 21–22):** *Precision, Recall, F1-score, Accuracy, AUC-ROC*, `Acc@k` (acurácia top-$N$ na localização de causa raiz), *Grouping Accuracy (GA)* para *log parsing*, e métricas de erro regressivo (*MAE, MSE, RMSE, MAPE*);
    2. **Generation Task Metrics (Seção 6.1.2, p. 22):** Métricas léxicas (*BLEU, ROUGE, METEOR*) e semânticas (*BERTScore, BLEURT, NUBIA*) para avaliação de relatórios de causa raiz e planos de mitigação;
    3. **Execution Task Metrics (Seção 6.1.3, p. 22):** Métricas específicas para remediação automatizada e geração de scripts (ex.: playbooks *Ansible*): *Functional Correctness (FC)*, *Average Correctness (AC)*, *Execution Success Rate* e *Correct Refactorings*;
    4. **Manual Evaluation (Seção 6.1.4, pp. 22–23):** Rubricas de avaliação qualitativa por especialistas (*Precise, Imprecise, Hallucination, Reasoning Error, Retrieval Error*) e avaliação de preferência humana em estudos de caso.
  - **Catalogação de Novos *Datasets* e *Benchmarks* Agênticos (Seção 6.2, pp. 23–24):** Analisa *benchmarks* criados especificamente para LLMs em AIOps: **LogEval** (`4.000` entradas de logs e `15` prompts por tarefa), **OpsEval** (`7.184` questões de múltipla escolha e `1.736` pares *QA* bilíngues com *leaderboard* contínuo), **OWL-bench** (9 subdomínios de O&M), **KubePlaybook** (`130` prompts em linguagem natural para geração de playbooks *Ansible* de auto-remediação em Kubernetes) e **AIOpsLab** (framework holístico da Microsoft que injeta falhas em tempo real via *chaos engineering* para avaliar agentes autônomos na localização e resolução de incidentes).
- **Justificativa:** Sistematiza de forma exaustiva as métricas quantitativas de classificação, geração, execução de scripts de auto-remediação (*FC, AC, Execution Success Rate*) e os *benchmarks* experimentais do domínio (`T = 1.0`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Análise de gargalos operacionais, latência em tempo real e modos de falha (Seção 6.1.4, p. 23; Seção 7.1–7.3, pp. 24–25):**
    - Categoriza explicitamente os modos de erro de LLMs em diagnóstico de incidentes: *Hallucination* (informação fabricada não ancorada nos dados de entrada), *Reasoning Error* (inferência lógica inválida) e *Retrieval Error* (uso incorreto ou incompleto do contexto recuperado via RAG, p. 23);
    - Demonstra a **inviabilidade de tempo e custo de inferência** em tarefas contínuas de percepção de falhas: exemplifica que, se uma janela de detecção de anomalias é acionada a cada `10 segundos`, o modelo precisa inferir em menos de `1 segundo` para alertar os *OCEs* a tempo — requisito que os LLMs atuais não atendem de forma custo-efetiva (Seção 7.1, p. 24);
    - Aponta o risco de verificação insuficiente na **Execução Automática** de scripts de remediação em produção (Seção 4.3, p. 15) e a falta de validação empírica da generalização de LLMs frente à evolução contínua do software (Seção 7.3, p. 25).
  - **Limitação:** Os próprios autores delimitam na Seção 1 (p. 2) e na Seção 7 (p. 24) que segurança de rede (*network security*) e vulnerabilidades gerais de NLP fogem ao escopo central do artigo, não aprofundando ataques adversariais como *prompt injection* ou *privilege escalation* em agentes de *AIOps*.
- **Justificativa:** Analisa com rigor técnico as limitações de latência em tempo real (`< 1s` por janela de `10s`), custo computacional, alucinações/erros de recuperação em RCA e riscos de auto-execução, mas sem abordar superfícies de ataque cibernético ou governança regulatória (`P = 0.5`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Quatro Direções Estratégicas para Pesquisa Futura em *LLM4AIOps* (Seção 7.1–7.4, pp. 24–26):**
    1. **Eficiência temporal e custo-efetividade via arquiteturas híbridas (Seção 7.1, pp. 24–25):** Combinação orgânica de modelos pequenos de baixo custo (*small-scale models*), LLMs e engenheiros de plantão (*OCEs*);
    2. **Uso aprofundado de fontes de dados subexploradas e fechamento do ciclo de automação (Seção 7.2, p. 25):** Integração efetiva de dados de **traces** distribuídos (grafos de chamadas complexos e aninhados hoje negligenciados pelos estudos com LLMs), uso de *prompt embedding* para logs brutos e conexão direta entre *failure perception* (dados de máquina) $\to$ geração automática de *incident reports* $\to$ *root cause analysis* (eliminando a dependência de abertura manual de chamados);
    3. **Generalização e adaptabilidade durante a evolução de software (Seção 7.3, pp. 25–26):** Testes sistemáticos de resiliência sob mudanças de versão/arquitetura com *incremental fine-tuning* e *continuous learning*;
    4. **Integração modular com *toolchains* de AIOps e automação existentes (Seção 7.4, p. 26):** Divisão de trabalho na qual detectores leves processam métricas/logs de alta frequência, LLMs realizam correlação contextual, explicação de causa raiz e geração/refinamento de scripts, e motores consolidados como **Ansible** e **Kubernetes operators** executam a orquestração determinística com menor risco operacional.
- **Justificativa:** Apresenta um roteiro técnico preciso e diretamente aplicável à engenharia de sistemas autônomos de detecção, diagnóstico e remediação de incidentes (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 1.0 + 1.0 + 0.5 + 1.0 = 4.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P05 |
| **Autores** | Lingzhe Zhang; Tong Jia; Mengxi Jia; Yifan Wu; Aiwei Liu; Yong Yang; Zhonghai Wu; Xuming Hu; Philip Yu; Ying Li |
| **Ano** | 2025 |
| **Título** | *A Survey of AIOps in the Era of Large Language Models* |
| **Periódico / Fonte** | *ACM Computing Surveys (CSUR)*, Vol. 58, No. 2, Art. 44, pp. 44:1–44:35 |
| **DOI** | `10.1145/3746635` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão Sistemática da Literatura (*Systematic Survey* de 163/183 artigos primários entre 2020 e 2024, complementada por entrevistas com *On-Call Engineers*) |
| **Domínio Principal** | *Artificial Intelligence for IT Operations (AIOps)* baseado em LLMs (*LLM4AIOps*): Detecção de Anomalias, Análise de Causa Raiz (*RCA*) e Auto-Remediação de Incidentes |
| **Tecnologias / Frameworks Analisados** | *RCAgent*, *RCACopilot*, *Xpert*, *LM-PACE*, *AIOpsLab*, *LLexus*, *mABC*, *AgentFM*, *OWL*, *LogLM*, *LILAC*, *DivLog*, *Time-LLM*, *TimeGPT*, *Lag-Llama*, *TimesFM*, *ShellGPT*, *RAG4ITOps*, *DB-GPT*, *KubePlaybook*, *OpsEval*, *LogEval*, *Ansible*, *Kubernetes* |
| **Escopo de Aplicação** | Confiabilidade operacional e gerenciamento de falhas em tempo de execução em sistemas distribuídos e de nuvem de larga escala (*Log Parsing*, *Failure Perception*, *Root Cause Analysis*, *Assisted & Automatic Remediation*) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Contraste entre AIOps tradicional (ML/DL) e *LLM4AIOps* (Seção 1.1, pp. 2–3); fusão de dados de máquina (*metrics, logs, traces*) com dados humanos (*incident reports, source code, QA*, Seção 3, Fig. 6); taxonomia de 5 níveis de automação na remediação (*Assisted Questioning* $\to$ *Automatic Execution*, Seção 4.3, Fig. 9, pp. 14–15). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Taxonomia em 5 grupos metodológicos (Seção 5, Fig. 10, pp. 15–21): *Foundation Models*, *Fine-tuning (Full/PEFT)*, *Embedding-based*, *Prompt-based (ICL/CoT)* e *Knowledge-based (RAG e Tool-Augmented Generation — TAG)*, incluindo agentes como *RCAgent*, *RCACopilot*, *LLexus*, *AIOpsLab*, *mABC* e *AgentFM*. |
| **RQ3** (Evidências Empíricas e Métricas) | `T` | `1.0` | Sistematização completa das métricas de avaliação de *LLM4AIOps* (Seção 6.1, Fig. 11, pp. 21–23): classificação (`Acc@k`, *GA*, *F1*), geração (*BLEU, ROUGE, BERTScore, BLEURT, NUBIA*), execução de scripts (*Functional Correctness, Average Correctness, Execution Success Rate*) e avaliação manual; análise dos *benchmarks* *LogEval*, *OpsEval*, *OWL-bench*, *KubePlaybook* e *AIOpsLab* (Seção 6.2, pp. 23–24). |
| **RQ4** (Riscos, Segurança e Governança) | `P` | `0.5` | Gargalos de latência em tempo real (inferência `< 1s` para janelas de `10s`, Seção 7.1, p. 24) e custo computacional; taxonomia de falhas em RCA (*Hallucination, Reasoning Error, Retrieval Error*, p. 23); riscos de execução automática de scripts sem validação (p. 15). Não aborda ataques adversariais cibernéticos. |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Roteiro futuro detalhado (Seção 7.1–7.4, pp. 24–26): arquiteturas híbridas (*small models* + LLMs + *OCEs*), integração de *traces* distribuídos, fechamento do loop automático *failure perception* $\to$ *incident report* $\to$ *RCA*, adaptabilidade à evolução de software e integração com *Ansible*/*Kubernetes operators*. |
| **Total (`SCORE_RQ`)** | — | **4.5 / 5.0** | **Aderência Excepcional (90,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | A Seção 2.2 (pp. 5–6) define formalmente 4 critérios de inclusão (`IC1–IC4`) e 5 critérios de exclusão objetivos (`EC1`: modelos com menos de `1 bilhão` de parâmetros, excluindo modelos pequenos tipo BERT; `EC2`: fora de sistemas de software; `EC3`: fora do escopo de AIOps; `EC4`: retratados ou sem texto completo; `EC5`: artigos puramente conceituais sem resultados experimentais). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | A Seção 2.1–2.3 e as Figuras 3 e 4 (pp. 5–7) documentam a *string* booleana exata, as 5 bases consultadas (*Scopus*, *Web of Science*, *IEEE Xplore*, *ACM Digital Library* e *arXiv*) entre janeiro de 2020 e dezembro de 2024, o processo de revisão por pares entre coautores e o fluxograma de seleção com contagens por base (`761` identificados $\to$ `614` sem duplicatas $\to$ `395` para leitura integral $\to$ `163` novos estudos selecionados, compondo as `183` referências analisadas). *(Nota: há uma pequena divergência aritmética no diagrama da Fig. 4 entre $614 - 333 = 281$ vs. `395` e $395 - 232 = 163$, mas todas as etapas e motivos de exclusão são explicitamente reportados).* |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `Y` | `1.0` | Elimina estudos sem validação experimental via `EC5` (p. 6), sintetiza comparativamente as revisões anteriores na Tabela 1 (p. 4), valida a taxonomia de auto-remediação por meio de entrevistas com *On-Call Engineers (OCEs)* de empresas parceiras (Seção 4.3, p. 14) e analisa criticamente a maturidade dos métodos, métricas e *benchmarks* nas Seções 3 a 6. |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões e direções futuras (Seções 7 e 8, pp. 24–27) são rigorosamente fundamentadas nos achados empíricos e nas lacunas observadas na literatura (como a ausência de estudos com *traces* e a ruptura do fluxo automático quando o RCA depende de relatórios humanos). |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **4.0 / 4.0** | **Qualidade Metodológica Máxima (100,0%)** |

---

## Parecer Final do Revisor

O artigo **P05** (Zhang et al., 2025), publicado na *ACM Computing Surveys* e integrante do **Corpus Fundacional** do Trabalho I, alcança pontuação máxima de qualidade metodológica (`SCORE_QA = 4.0 / 4.0`, banda **Alta**) e altíssima aderência às questões de pesquisa da RSL (`SCORE_RQ = 4.5 / 5.0`). Trata-se de um dos pilares mais importantes de toda a revisão para o domínio de operações de TI e resposta a incidentes: (i) estrutura a evolução completa de *Failure Perception*, *Root Cause Analysis* e *Assisted Remediation*; (ii) propõe e valida junto a engenheiros de plantão (*OCEs*) a escala de 5 níveis de automação na remediação de incidentes (de *Assisted Questioning* até *Automatic Execution*); (iii) cataloga as métricas específicas para avaliar geração e execução autônoma de scripts de correção (*Functional Correctness*, *Average Correctness*, *Execution Success Rate*) e os principais *benchmarks* agênticos (*AIOpsLab*, *OpsEval*, *LogEval*, *KubePlaybook*); e (iv) demonstra com precisão o gargalo de latência em tempo real (`< 1s`) que exige arquiteturas híbridas combinando detectores leves, agentes LLM e orquestradores determinísticos (*Ansible*/*Kubernetes*).
