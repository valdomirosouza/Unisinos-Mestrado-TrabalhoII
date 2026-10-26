# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P12
- **Arquivo PDF avaliado:** `P12-A1-Enhancing autonomous system security and resilience with generative AI A comprehensive survey.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo apresenta um *survey* abrangente sobre o papel da **Inteligência Artificial Generativa (GenAI)** e dos **Large Language Models (LLMs)** no fortalecimento da **segurança cibernética, resiliência operacional, detecção de anomalias, gestão de falhas, auto-recuperação (*self-healing*) e coordenação de enxames multiagentes** em sistemas autônomos e ciberfísicos (*UAVs*, veículos autônomos, robótica de borda e redes *IoT*), dedicando seções específicas a testes de penetração automatizados, detecção de *malware*, Sistemas de Detecção de Intrusão em Rede (*NIDS*), Inteligência de Ameaças Cibernéticas (*CTI*) e arquiteturas **Zero-Trust (NIST SP 800-207)** (Seção IV.D, Tabela 5, pp. 14–17).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *IEEE Access*, Volume 12, pp. 109470–109493, agosto de 2024 (Recebido em 12 de julho de 2024; Aceito em 31 de julho de 2024; Data de publicação em 6 de agosto de 2024; Versão atual em 16 de agosto de 2024).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão publicado em periódico científico revisado por pares (*IEEE Access*, IEEE), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 24 páginas em inglês com 173 referências, 6 tabelas e 3 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Transição de Modelos Discriminativos para Modelos Generativos e Multimodais (Seção III, Figs. 2 e 3, Tabela 2, pp. 3, 5–7):** O artigo fundamenta a diferença estrutural entre modelos discriminativos tradicionais (limitados a fronteiras de decisão estáticas) e cinco famílias de modelos de *GenAI* — **Variational Autoencoders (VAEs)**, **Generative Adversarial Networks (GANs)**, **Generative Diffusion Models (GDMs)**, **Transformers / LLMs / VLMs / MLLMs** (*GPT-4, Gemini, Llama 2/3, Mistral, Falcon, Orca, Claude 3*) e **Normalizing Flow Models (NFMs)** —, mapeando na Tabela 2 (p. 7) como cada paradigma viabiliza estimativa de estado para detecção de ameaças, tomada de decisão autônoma e detecção de anomalias.
  - **Autonomia Proativa, *Self-Awareness* e *Human-Machine Teaming (HMT)* (Seção IV.A.1–3, pp. 7–9; Seção IV.B.2, p. 11; Seção IV.C.2, p. 13):**
    - Define *self-awareness* operacional como a capacidade do sistema autônomo de avaliar continuamente integridade de hardware, desempenho de aplicação, localização física e postura de segurança sob sensores ruidosos (p. 7);
    - Analisa a integração de LLMs no raciocínio proativo diante de *edge cases* (*DriveLLM* [57], *ChatGPT for robotics* [66] e transferência universal de políticas entre diferentes morfologias robóticas via *RT-X* [59] e *MetaMorph* [107], pp. 8–9, 13);
    - Destaca a evolução além do *human-in-the-loop* tradicional rumo ao paradigma **Human-Machine Teaming (HMT)** estruturado pelo loop autonômico **MAPE-KMT (*Monitor, Analyze, Plan, and Execute*)** aumentado por *GenAI* para gestão de segurança em ambientes imprevisíveis (Seção IV.C.2, p. 13).
  - **Limitação:** O artigo concentra-se na aplicação ampla de modelos generativos (*GANs, VAEs, GDMs, NFMs, LLMs*) em sistemas autônomos e robóticos, sem formalizar uma taxonomia conceitual específica que diferencie *AI Agents* de *Agentic AI*.
- **Justificativa:** Fundamenta bem a transição de modelos discriminativos para arquiteturas generativas, *MAPE-KMT* e *Human-Machine Teaming*, mas sem foco específico na definição formal do paradigma *Agentic AI* (`P = 0.5`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Taxonomia Arquitetural em Quatro Níveis Operacionais (Fig. 1, p. 3; Seção IV.A–D, Tabelas 3, 4 e 5, pp. 7–17):**
    1. **Entidades Individuais — Detecção de Anomalias, Manutenção Preditiva e *Self-Healing* (Seção IV.A, Tabela 3, pp. 7–10):** Documenta arquiteturas como **MSGAN** [55] (treinamento offline, inferência online e aprendizado incremental para anomalias em sensores), **RoBiGAN** [56] (GAN bidirecional com perda de Wasserstein para diagnóstico online de falhas), **GenDeX** [6] (VAE com memória evolutiva para séries temporais multivariadas), **GAN-FP** [51] (previsão de falhas), **BERTery** [68] (*spatio-temporal transformer* para prognóstico de falhas de bateria) e o framework de **auto-recuperação (*self-healing*)** de Khlaisamniang et al. [70], que emprega *GenAI* para detecção de anomalias, geração de código, depuração automática (*debugging*) e criação de relatórios de incidentes em sistemas computacionais (p. 10);
    2. **Frotas e Coordenação de Enxames Multiagentes (Seção IV.B, Tabela 4, pp. 10–12):** Analisa **multi-agent LLMs** operando em dispositivos de borda para **redes baseadas em intenção (*intent-based networking*)**, traduzindo metas de alto nível (como redução de consumo energético de rede) em tarefas executáveis, com auto-replicação de agentes e consenso (pesquisa do *TII* [79], p. 11); coordenação multiagente via **MAPPO-GAIL** (*Multi-Agent PPO + Generative Adversarial Imitation Learning* [72]), **AGOD / D2SAC** (*Deep Diffusion Soft Actor-Critic* [80]), **CLIPSwarm** [78] e **GRIN** (*Generative Relation and Intention Network* combinando *GNNs* e *Transformers* [83]); resiliência de comunicação semântica (*SemCom* [81, 88, 89]); e consenso tolerante a falhas bizantinas via *blockchain* (**DPOS + PBFT**) e geração automatizada de protocolos de consenso via *Reinforcement Learning* (Vaz et al. [93], p. 12);
    3. **Planejamento de Missão e Segurança com Grafos de Conhecimento (Seção IV.C, pp. 12–14):** Descreve arquiteturas de planejamento e comando como **REAL** [99] (adaptação e resiliência com LLMs a bordo), **COA-GPT** [100] (geração acelerada de *Courses of Action* com feedback de operador), **LLM-Brain** [103], **LMPC** (*Language Model Predictive Control* com *PaLM 2* [105, 106]) e os mecanismos de *guardrail* **Embodied Robotic Control Prompts (ERCPs)** e **Embodied Knowledge Graphs (EKGs)** (Qi et al. [109], p. 13), que ancoram ações de LLMs em grafos de conhecimento fatuais para garantir conformidade de segurança;
    4. **Arquiteturas de Cibersegurança e *Zero-Trust* (Seção IV.D, Tabela 5, pp. 14–17):** Mapeia **SECGPT** [137] (arquitetura de isolamento de execução para sistemas baseados em LLMs que regula interações entre aplicações), **SecurityBERT** [138] (detecção leve de ameaças em *IoT* com codificação *PPFLE* e tokenizador *BBPE*), *fuzzers* guiados por LLM (**CHATAFL** [113] para protocolos de rede sem especificação legível por máquina e **Fuzz4All** [114]), detectores de *malware* (*CyBERT, MALBERT, CySecBERT, DLAM, DeGPT, SLAM, I-MAD*), arquiteturas *NIDS* (*FlowGAN, GIDS* para barramento CAN veicular, *SGAN-IDS, AE-CGAN* e **ARCADE** — *Adversarially Regularized Convolutional Autoencoder* [120]), plataformas de *CTI* (*CyberTwitter* [132]) e integração com **Zero-Trust Architecture (NIST SP 800-207)** para tradução automática de políticas em linguagem natural para regras formais e geração de *honeypots* adaptativos (**Intell-dragonfly** [133], pp. 16–17).
- **Justificativa:** Oferece um mapeamento arquitetural riquíssimo cobrindo desde isolamento de execução para LLMs (*SECGPT*), *AI firewalls*, *NIDS* e *Zero-Trust* até coordenação multiagente em redes baseadas em intenção e *self-healing* (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Compilação de Métricas Quantitativas de Estudos Primários de Segurança e Resiliência (Seção IV.A–D, pp. 10–16):**
    - **Gestão de Falhas e Eficiência em Borda (Seção IV.A.5, p. 10):** O modelo **BERTery** [68] antecipa falhas iminentes de bateria com até **`24 horas` de antecedência**; a portabilidade de modelos *VAE + LSTM* de detecção e classificação de falhas para **FPGAs** (Sadhu et al. [62]) alcançou um **aumento de `40 vezes` (`fortyfold`) na velocidade de processamento** e uma **redução de `50%` no consumo de energia** em comparação a GPUs;
    - **Inteligência e Coordenação de Enxames Multiagentes (Seção IV.B.1–2, pp. 10–11):** Aumento de **`12%` na acurácia de detecção de UAVs** via modelos de difusão texto-imagem (p. 10); o algoritmo multiagente **MAPPO-GAIL** [72] obteve um **aumento de `73,3%` na eficiência de busca cooperativa** frente a métodos *DRL* tradicionais (p. 11); a arquitetura *blockchain* **DPOS + PBFT** [82] escalou eficientemente para **`500 nós`** com sobrecarga mínima mitigando *spoofing*, *DoS* e *tampering* (p. 11);
    - **Meta-Aprendizado e Adaptação (Seção IV.C.3, p. 13):** O framework **LMPC** com *PaLM 2* [105, 106] elevou a **eficácia de ensino em `26,9%`** para novas tarefas e melhorou a **adaptabilidade a novas configurações robóticas em `31,5%`**;
    - **Métricas de Cibersegurança — *IoT*, *Malware*, *NIDS* e *CTI* (Seção IV.D, pp. 14–16):** O **SecurityBERT** [138] atingiu **`98,2%` de acurácia** na detecção de ameaças cibernéticas em redes *IoT* (p. 14); o modelo **DLAM** (*Stacked BiLSTM + GPT-2* [126]) alcançou **`98%` de acurácia** em nível de documento e `86%` em nível de sentença na detecção de código malicioso em arquivos *Portable Executable (PE)* (p. 15); o tráfego malicioso sintético gerado por **WGAN** [147] derrubou a taxa de detecção de *IDS* tradicionais de **`97,3%` para `47,6%`**, expondo fragilidades críticas de *NIDS* convencionais (p. 16); e o sistema híbrido de extração de *keyphrases* para *CTI* de Bose et al. [131] alcançou **escores F1 pelo menos `25%` superiores** aos *transformers* SOTA tradicionais (p. 16).
  - **Limitação:** Sendo uma revisão da literatura, o estudo não executa experimentos primários próprios nem consolida uma tabela quantitativa única padronizando métricas de tempo médio de resposta a incidentes (*MTTR*).
- **Justificativa:** Reúne evidências quantitativas secundárias sólidas em detecção de ameaças (`98,2%` no *SecurityBERT*, `98%` no *DLAM*, `+25%` F1 em *CTI*), coordenação multiagente (`+73,3%` no *MAPPO-GAIL*) e aceleração em hardware (`40x` em FPGA), mas sem experimentação primária (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Ameaças Ofensivas e Uso Dual de Agentes e LLMs (Seção IV.D, p. 14):**
    - **Net-GPT [139]:** Chatbot ofensivo baseado em LLM capaz de executar ataques **Man-in-the-Middle (MiTM)** sequestrando e manipulando comunicações entre *UAVs* e Estações de Controle em Solo (*GCS*);
    - **BadGPT [140]:** Ataque de *backdoor* contra o ajuste fino por Aprendizado por Reforço (*RL fine-tuning*), comprometendo o modelo de recompensa (*reward model*) para manipular de forma oculta o comportamento gerado;
    - **Exploração Autônoma de Vulnerabilidades (Fang et al. [111], p. 14):** Demonstração de que agentes baseados em **GPT-4 podem explorar autonomamente vulnerabilidades *one-day* do mundo real** a partir de descrições de *CVEs*, além do risco de criação de *malware* polimórfico em *pentesting* assistido por LLM [110].
  - **Taxonomia de Ataques Adversariais a LLMs, VLMs e Sistemas Multiagentes (Seção V, p. 17):** Com base em Shayegani et al. [159] e Jin et al. [160], estrutura os ataques em três classes:
    1. *Unimodal Attacks:* Ataques de **Jailbreak** (baseados em gradiente, evolutivos e por demonstração) e **Prompt Injection**;
    2. *Multimodal Attacks:* *Input Manipulation*, *Cross-Modal Exploits* (desalinhamento deliberado entre texto e imagem em *VLMs*) e *Contextual Confusion*;
    3. *Complex System Attacks:* Ataques direcionados especificamente a configurações distribuídas como **aprendizado federado e sistemas multiagentes**, explorando vulnerabilidades de agregação e coordenação para comprometer o sistema inteiro;
    - Acrescenta riscos de **ataques de extração de dados de treinamento (*training data extraction*)** em modelos de linguagem e difusão (Nasr et al. [155]; Carlini et al. [158], p. 17), alucinações e **comportamento bajulador (*sycophantic behavior*)** em análise de incidentes (Sufi [130], p. 16) e degradação severa de *VLMs* sob mínimas perturbações (*AUTOHALLUSION* [108], p. 13).
  - **Gargalos de Custo, Computação em Borda e Privacidade (Seção V, pp. 17–18):** Aponta o alto custo operacional de APIs proprietárias (`~US$ 0,006` por 750 palavras no GPT-4 e `~US$ 0,18` por imagem no DALL-E 2 [151]), a persistência de falhas em *edge cases* mesmo após `>US$ 100 bilhões` investidos em veículos autônomos [150], as limitações de conhecimento fatual de modelos compactos (*Phi-3-mini* [161]) e riscos de vazamento de PII, propondo mascaramento generativo (*ADGAN* [153], *TrajGANs*), enclaves seguros, criptografia homomórfica e o padrão **IEEE Std 7001-2021 (*Transparency of Autonomous Systems*)** [169].
- **Justificativa:** Examina com profundidade tanto as superfícies de ataque específicas de LLMs/multiagentes (*Net-GPT MiTM*, *BadGPT reward poisoning*, exploração autônoma de *CVEs*, *cross-modal exploits* e extração de dados) quanto barreiras de custo, borda e governança (`T = 1.0`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Roteiro Estruturado em Cinco Eixos de Pesquisa Futura (Seção V.A.1–5, pp. 18–19):**
    1. **Security Enhancements (Seção V.A.1, p. 18):** Desenvolvimento de autenticação e autorização contínuas para frotas autônomas, distribuição quântica de chaves (*QKD*), computação segura multipartidária (*MPC*), implantação de **AI Firewalls** para monitorar e filtrar entradas/saídas de modelos, adoção de *benchmarks* padronizados de segurança cibernética para LLMs — **CYBERSECEVAL 2 / CyberMetric** [162], **SecQA** [163], **WMDP-Cyber** [164] (desaprendizado de uso malicioso), **CyberBench** [165] e **LLM4Vuln** [166] — e mecanismos de **autoavaliação defensiva (*self-evaluation defense*, Brown et al. [167])** operando nos modos *Input-Only*, *Output-Only* e *Input-Output* para bloquear sufixos adversariais diretos e ataques *copy-paste* sem necessidade de *fine-tuning* adicional;
    2. **Explainability and Transparency (Seção V.A.2, p. 18):** Métricas padronizadas de auditabilidade para decisões de controle de acesso e avaliação de confiança, operacionalizando a norma **IEEE 7001-2021** [169];
    3. **Dynamic Adaptation and Robustness to Adversarial Attacks (Seção V.A.3, p. 18):** Algoritmos capazes de reajustar políticas de segurança em tempo real frente a ameaças inéditas, combinando privacidade diferencial, *blockchain* para verificação de proveniência, criptografia pós-quântica e *human-guided RL*;
    4. **Scalability and Ethical AI Integration (Seção V.A.4, p. 18):** Otimização *edge-cloud* e criação de conselhos de ética em IA (*AI ethics boards*) e auditorias éticas regulares;
    5. **Enhanced Transparency Mechanisms (Seção V.A.5, pp. 18–19):** Construção de frameworks *"glass-box"* e rastreabilidade completa de dados de treinamento.
- **Justificativa:** Mapeia com precisão as lacunas de *benchmarking* de segurança (*CyberMetric, SecQA, WMDP-Cyber, CyberBench, LLM4Vuln*), defesas autônomas (*AI firewalls*, *self-evaluation* *Input/Output*), padronização (*IEEE 7001-2021*) e adaptação dinâmica (`T = 1.0`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 0.5 + 1.0 + 0.5 + 1.0 + 1.0 = 4.0 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P12 |
| **Autores** | Martin Andreoni; Willian Tessaro Lunardi; George Lawton; Shreekant Thakkar |
| **Ano** | 2024 |
| **Título** | *Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 12, pp. 109470–109493 |
| **DOI** | `10.1109/ACCESS.2024.3439363` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | *Survey* / Revisão Abrangente da Literatura (173 referências, 6 tabelas) |
| **Domínio Principal** | Segurança Cibernética, Resiliência Operacional, Detecção de Anomalias/Falhas e Coordenação de Enxames em Sistemas Autônomos com IA Generativa e LLMs |
| **Tecnologias / Frameworks Analisados** | *LLMs/VLMs/MLLMs* (*GPT-4, Claude 3, Llama 3, PaLM 2, Phi-3*), *GANs* (*MSGAN, RoBiGAN, WGAN, FlowGAN, SGAN-IDS, ADGAN*), *VAEs* (*GenDeX, ARCADE, AE-CGAN*), *GDMs*, *NFMs*, **SECGPT**, **SecurityBERT**, **CHATAFL**, **Fuzz4All**, *CyBERT/MALBERT/CySecBERT*, **MAPPO-GAIL**, **MAPE-KMT**, **ERCPs/EKGs**, **NIST SP 800-207 (Zero-Trust)**, *CyberMetric, SecQA, WMDP-Cyber, CyberBench, LLM4Vuln* |
| **Escopo de Aplicação** | Cibersegurança (*pentesting*, detecção de *malware*, *NIDS*, *CTI* e políticas *Zero-Trust*), detecção de anomalias, manutenção preditiva, gestão de falhas/*self-healing* e coordenação de enxames (*UAVs*, veículos autônomos, robótica e *IoT*) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `P` | `0.5` | Contraste entre modelos discriminativos e 5 paradigmas de *GenAI* (*VAEs, GANs, GDMs, Transformers/LLMs, NFMs*, Seção III, Figs. 2–3, Tabela 2, pp. 3–7); *self-awareness*, autonomia em *edge cases* (*DriveLLM, RT-X*) e transição para *Human-Machine Teaming (HMT)* com loop **MAPE-KMT** (Seção IV.A–C, pp. 7–13). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Arquiteturas em 4 domínios (Fig. 1, Tabelas 3–5, pp. 3, 7–17): detecção de anomalias e *self-healing* (*MSGAN, RoBiGAN, GenDeX, BERTery*, geração/depuração de código [70]); enxames multiagentes (*multi-agent LLMs* para *intent-based networking* [79], *MAPPO-GAIL*, *AGOD/D2SAC*, *DPOS+PBFT*); *guardrails* com grafos de conhecimento (*ERCPs/EKGs* [109]); e cibersegurança (**SECGPT**, **SecurityBERT**, **CHATAFL**, **Fuzz4All**, **ARCADE** e **Zero-Trust NIST SP 800-207**). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Síntese de métricas quantitativas da literatura primária: `40x` velocidade e `-50%` energia em FPGA (*VAE+LSTM* [62], p. 10); prognóstico de falha com `24h` de antecedência (*BERTery* [68]); `+73,3%` eficiência de busca cooperativa multiagente (*MAPPO-GAIL* [72], p. 11); `98,2%` acurácia no *SecurityBERT* [138] (p. 14); `98%` acurácia no *DLAM* [126] (p. 15); queda de `97,3% -> 47,6%` em IDS sob ataque WGAN [147] (p. 16); e `+25%` F1 em *CTI* [131] (p. 16). Sem experimentos primários próprios. |
| **RQ4** (Riscos, Segurança e Governança) | `T` | `1.0` | Ameaças ofensivas (*Net-GPT MiTM* em UAVs [139], *BadGPT* no modelo de recompensa RL [140], exploração autônoma de *CVEs* por GPT-4 [111], p. 14); taxonomia de ataques *Unimodal* (*Jailbreak, Prompt Injection*), *Multimodal* (*Cross-Modal*) e *Complex System Attacks* em **sistemas multiagentes e federados** [159, 160], extração de dados de treino [155, 158], custos de inferência e limites de borda (Seção V, pp. 17–18). |
| **RQ5** (Lacunas e Direções Futuras) | `T` | `1.0` | Cinco direções futuras (Seção V.A, pp. 18–19): **AI Firewalls**, *benchmarks* de segurança (**CYBERSECEVAL 2 / CyberMetric, SecQA, WMDP-Cyber, CyberBench, LLM4Vuln**), defesa autônoma por autoavaliação (*Input-Only, Output-Only, Input-Output* [167]), transparência padronizada (**IEEE Std 7001-2021** [169]), adaptação dinâmica e auditorias éticas. |
| **Total (`SCORE_RQ`)** | — | **4.0 / 5.0** | **Alta Aderência (80,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `P` | `0.5` | Delimita com clareza o escopo na Seção I–II (pp. 1–5), apresenta a árvore taxonômica na Figura 1 (p. 3) e posiciona o trabalho frente a 16 *surveys* anteriores na Tabela 1 (p. 4) segundo quatro eixos (*GenAI, LLM, Security, Autonomous Systems*), mas não define critérios formais de inclusão e exclusão. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | Revisão narrativa/abrangente sem seção de metodologia de busca: não reporta bases indexadoras consultadas, *strings* booleanas, janela de coleta nem fluxograma PRISMA. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza 173 referências com bom nível de detalhamento técnico em cinco tabelas analíticas (Tabelas 1–5) e extrai métricas quantitativas relevantes dos estudos primários, porém sem aplicar avaliação formal de qualidade metodológica aos artigos revisados. |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | As conclusões e a agenda de pesquisa (Seções V e VI, pp. 17–20) são totalmente consistentes com as evidências discutidas no texto e mantêm transparência ética exemplar (declarando explicitamente o uso de ferramentas de revisão linguística no *Acknowledgment*, p. 20). |
| **Total (`SCORE_QA`)** | **Banda: Média** | **2.0 / 4.0** | **Qualidade Metodológica Moderada (50,0%)** |

---

## Parecer Final do Revisor

O artigo **P12** (Andreoni et al., 2024), elaborado por pesquisadores do *Technology Innovation Institute (TII)* e publicado no *IEEE Access* como parte do **Corpus Fundacional** do Trabalho I, apresenta alta aderência às questões de pesquisa da RSL (`SCORE_RQ = 4.0 / 5.0`) e qualidade metodológica na banda **Média** (`SCORE_QA = 2.0 / 4.0`). Para a nossa RSL sobre *Agentic AI Copilot para Resposta a Incidentes*, **P12** oferece contribuições técnicas diretas para as seções de **Arquitetura (RQ2)**, **Riscos e Ameaças (RQ4)** e **Lacunas de Pesquisa (RQ5)**: mapeia arquiteturas de isolamento de execução para LLMs (**SECGPT**), detecção leve de ameaças (**SecurityBERT** com `98,2%` de acurácia), *fuzzing* autônomo de protocolos (**CHATAFL**, **Fuzz4All**), coordenação de enxames com **multi-agent LLMs para *intent-based networking*** e o loop **MAPE-KMT**, além de catalogar ataques ofensivos (**Net-GPT MiTM**, **BadGPT**, exploração autônoma de *CVEs* por GPT-4), *benchmarks* de avaliação de segurança (**CyberMetric, SecQA, WMDP-Cyber, CyberBench, LLM4Vuln**) e defesas baseadas em **AI Firewalls** e autoavaliação *Input/Output*.
