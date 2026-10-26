# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P13
- **Arquivo PDF avaliado:** `P13-A1-Retail Resilience Engine An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo propõe, implementa e avalia experimentalmente o **Retail Resilience Engine (RRE)**, um framework de **Agentic AI** que integra **Test-Driven Development (TDD)** a um modelo *Transformer/GPT* treinado sobre logs operacionais, logs de sistema anonimizados, registros de inventário e *feedback* de clientes para automatizar a validação de testes, a mitigação proativa de falhas e a tomada de decisão resiliente em engenharia de sistemas comerciais (Seções I–IV, pp. 1–15).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *IEEE Access*, Volume 13, pp. 50226–50243, março de 2025 (Recebido em 27 de fevereiro de 2025; Aceito em 15 de março de 2025; Data de publicação em 18 de março de 2025; Versão atual em 26 de março de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de pesquisa original completo publicado em periódico científico revisado por pares (*IEEE Access*, IEEE), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Estudo primário completo de 18 páginas em inglês com 56 referências, 11 tabelas e 8 figuras.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Transição da Validação Manual e Baseada em Regras Estáticas para *Agentic AI* Integrada a *TDD* (Seção I.B–D, pp. 1–2; Seção II.C–G, Tabelas 1 e 2, pp. 3–4):** O artigo identifica que abordagens tradicionais de manutenção e evolução de sistemas dependem de regras estáticas ou intervenção manual de múltiplos especialistas humanos (cujo desenvolvimento manual de casos de teste correlacionando múltiplos subsistemas é lento e propenso a erros), enquanto soluções convencionais de IA operam de forma isolada da engenharia de software. Para superar essa dicotomia, propõe substituir o processo decisório humano multinível por uma tomada de decisão centralizada e contínua conduzida por **Agentic AI** acoplada ao ciclo *write-test-then-develop* do **Test-Driven Development (TDD)** (Seção III.E.5, p. 9; Seção IV.C, p. 11).
  - **Revisão Sistemática Embarcada para Identificação de Lacunas (Seção II.1–2, Tabelas 1 e 2, pp. 2–4):** Conduz uma revisão preliminar baseada em Kitchenham e PRISMA (`212` artigos recuperados em *IEEE Xplore, SpringerLink, ScienceDirect, Google Scholar* $\to$ `48` artigos incluídos entre 2018 e 2024), formalizando três lacunas na Tabela 1 (p. 4): (1) integração limitada entre TDD e IA; (2) ausência de um framework de *Agentic AI* para resiliência de sistemas; e (3) falta de estudo de viabilidade sobre a substituição de especialistas humanos em TDD por LLMs.
  - **Limitação:** O artigo utiliza o termo *Agentic AI* para descrever um modelo *Transformer* único acoplado a uma camada de controle e API de execução de testes, sem formalizar níveis de autonomia agêntica, planejamento multi-etapas (*ReAct/CoT*) ou coordenação multiagente.
- **Justificativa:** Fundamenta bem a motivação de engenharia de software para unir *TDD* e *Agentic AI* visando resiliência operacional e redução de intervenção humana, mas com conceituação teórica simplificada de agência (`P = 0.5`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Arquitetura Modular em Quatro Camadas do *Retail Resilience Engine — RRE* (Seção III.A–C, Fig. 1, pp. 4–5):**
    1. **Data Source Layer:** Ingestão híbrida de seis fontes de dados estruturados e não estruturados (`100.000` documentos no total, Tabela 3, p. 6): livros de varejo e TDD [29–38], `5.000` avaliações textuais anonimizadas de clientes, `10.000` registros transacionais de inventário, `50.000` documentos de **logs operacionais (*Operational Logs*)** e `35.000` documentos de repositórios analíticos e **logs de sistema anonimizados (*Anonymized System Logs*)**;
    2. **Pre-processing Layer:** Pipeline em quatro estágios com interface de API dedicada (*Data Pre-processing API Interface*, Fig. 1): extração matemática (Eq. 1, p. 6), limpeza em duas fases (inspeção manual de anomalias + filtragem algébrica de ruído/stopwords e imputação dinâmica contextual, Eq. 2, p. 7), tokenização em subpalavras (Eq. 3, p. 7) e divisão estratificada `80%-10%-10%` (Eq. 4, p. 7);
    3. **Feature Management Layer:** Composta por *Permanent Feature Storage*, *Temporary Feature Storage*, módulo de *Feature Comparison and Retainment* e *Updated Features* (Fig. 1, p. 5), permitindo incorporar dinamicamente novos parâmetros operacionais sem retreinar o modelo do zero (p. 7);
    4. **Software Layers:** Integram *User Interface*, *Application Layer*, *Business Logic Layer*, *Data Flow API*, **AI Agent API** (que executa testes automatizados em tempo real a partir de casos de teste gerados dinamicamente), **Application Control Unit** (verificação contínua de respostas frente ao comportamento esperado) e **Learning Control Unit** (Seção III.B–C, p. 5).
  - **Estrutura Interna do Modelo *Transformer* de 16 Camadas (Seção III.E, Tabela 4, Eqs. 5–15, pp. 7–9):** Especifica na Tabela 4 (p. 8) a arquitetura neural completa do motor: Camada 1 (*Input Embedding* `50.000 x 512`), Camada 2 (*Positional Encoding* senoidal de dimensão `512`, Eqs. 6–7), Camadas 3 a 14 (`12` blocos *Transformer Encoder* contendo *Multi-Head Attention* de `8 cabeças` `512 x 512`, *Layer Normalization* Eq. 12, *Feed-Forward Network* ReLU `512 -> 2048 -> 512` Eq. 11, *Dropout* com taxa $p = 0.1$ e conexões residuais Eq. 13), Camada 15 (*Output Embedding* `512 x 50.000`) e Camada 16 (*Softmax Layer* de dimensão `50.000`, Eqs. 14–15).
  - **Mecanismo de *Guardrail* por Filtragem Semântica de *Prompts* (Seção III.G, Tabela 5, Eq. 19, Algoritmo 1, p. 10):** Implementa o **Relevancy Verification Algorithm** (Algoritmo 1, p. 10), que calcula a similaridade de cosseno $R(p) = \frac{\mathbf{v}_p \cdot \mathbf{v}_k}{\|\mathbf{v}_p\|\|\mathbf{v}_k\|}$ entre o vetor do *prompt* de entrada e um dicionário de `22` palavras-chave operacionais (Tabela 5, incluindo *System Downtime*, *Risk Mitigation* e *Operational Efficiency*), bloqueando entradas irrelevantes antes do processamento pelo *Transformer*.
- **Justificativa:** Apresenta especificação arquitetural, matemática e algorítmica completa (Fig. 1, Tabelas 3–5, Eqs. 1–19 e Algoritmo 1), detalhando desde a ingestão de logs de sistema e gerenciamento dinâmico de atributos até a execução contínua de testes via *AI Agent API* e filtragem de *prompts* (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Ambiente de Treinamento e Evolução de Perplexidade (Seção III.F, Figs. 2 e 3, Eqs. 16–18, pp. 9–11):** Treinado em um cluster de **4 GPUs NVIDIA A100** (`lr = 0.001`, *batch size* `32`, `150 épocas`, otimizador *Adam* e validação cruzada de 5 pastas, p. 9, 15), reduzindo a perplexidade de validação de `~20` para `< 15` (Fig. 3, p. 11).
  - **Alinhamento de Impacto Decisório com Especialistas Humanos — *RDIA* (Seção IV.C, Tabela 6, Fig. 4, Eq. 21, pp. 11–12):** Comparou as decisões do RRE contra **3 especialistas humanos** (com `> 10 anos` de experiência) em 10 consultas críticas (`Q1` a `Q10`, avaliadas na escala $-5 \le r \le 5$), obtendo **coeficiente de correlação de Pearson $\rho = 0,96$ (`96%` de alinhamento)** (p. 12) e **índice de similaridade de `97,5%`** (Resumo, p. 1; Conclusão, p. 16), validado estatisticamente por teste $t$ pareado com **$p\text{-valor} = 0,021 < 0,05$** (Seção IV.H, Eq. 22, pp. 13–14).
  - **Qualidade dos Planos de Implementação TDD (Seção IV.D, Tabela 7, Fig. 5, p. 12):** Em avaliação cega por três avaliadores independentes (escala de 1 a 5 por avaliador, máximo de 15 pontos), o plano gerado pelo **RRE obteve `13 / 15` pontos** (`4 + 5 + 4`), empatando com o *Expert 3* (`13 / 15`), superando amplamente o *Expert 2* (`8 / 15`) e ficando a apenas 1 ponto do *Expert 1* (`14 / 15`).
  - **Análise de Escalabilidade e Eficiência Computacional em Tempo Real (Seção IV.E, Tabelas 8 e 9, Fig. 6, pp. 12–14):**
    - **Escalabilidade linear (Tabela 8, p. 12):** *Small* (`100` consultas: `12 s`, Acurácia `0,92`, Precisão `0,91`, Recall `0,93`), *Medium* (`500` consultas: `56 s`, Acurácia `0,91`, Precisão `0,90`, Recall `0,92`) e *Large* (`1.000` consultas: `120 s`, Acurácia `0,90`, Precisão `0,89`, Recall `0,91`);
    - **Eficiência operacional em GPU NVIDIA A100 (Tabela 9, p. 14):** Tempo médio de inferência de **`52 ms` por consulta**, consumo de memória VRAM de **`4,2 GB`**, taxa de processamento em lote de **`19,3 consultas/segundo`** e **latência ponta a ponta em nuvem de `86 ms`**.
  - **Robustez Multicategoria e Desempenho do Filtro de *Prompts* (Seção IV.F–G, Tabelas 10 e 11, Figs. 7 e 8, pp. 13–15):**
    - Na Tabela 10 (p. 15), o RRE manteve acurácia e F1-score entre **`0,89` e `0,93`** ao longo de 10 domínios operacionais, destacando-se **Risk Mitigation** (Acurácia `0,92`, Precisão `0,91`, Recall `0,93`, F1 `0,92`) e **Customer Feedback / Supplier Performance** (Acurácia `0,93`, F1 `0,93`);
    - Na Tabela 11 (p. 15), ao longo de 5 experimentos (`150` a `250` *prompts*), o mecanismo de filtragem bloqueou em média `196,4` de `200` *prompts* irrelevantes, atingindo **acurácia média de filtragem de `98,20%`** (`98,22%` na p. 10).
- **Justificativa:** Reporta um conjunto amplo e detalhado de métricas quantitativas primárias (precisão, recall, F1, latência em milissegundos, uso de memória em GB, correlação com especialistas humanos e teste de significância estatística) (`T = 1.0`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Análise Crítica de Limitações Técnicas, Éticas e Operacionais (Seção V.A–I, pp. 15–16):**
    - **Desafios Éticos, PII e Conformidade Regulatória (Seção V.A, p. 15):** O treinamento sobre logs operacionais e registros de clientes envolve *Personally Identifiable Information (PII)*, exigindo conformidade estrita com **GDPR** e **CCPA**;
    - **Opacidade *Black-Box* e Explicabilidade (Seção V.C, p. 15):** A natureza caixa-preta do modelo *Transformer* dificulta a auditoria humana da razão subjacente às recomendações de teste e decisão;
    - **Riscos Operacionais de *Agentic AI* em Ambientes Dinâmicos (Seção V.I, p. 16):** Destaca três riscos críticos: (1) **latência decisória (*decision latency*)** durante picos extremos de demanda ou interrupções abruptas da cadeia de suprimentos; (2) **vulnerabilidade a cenários inéditos (*unprecedented conditions / distributional shift*)** não representados nos dados históricos; e (3) **degradação por dados de entrada incompletos, enviesados ou inconsistentes**, gerando recomendações subótimas;
    - **Mecanismo de Contenção de Entradas Irrelevantes (Seção III.G e IV.G, pp. 10, 13–15):** O filtro de similaridade de cosseno (Algoritmo 1) atua como *guardrail* de entrada impedindo que `98,20%` dos *prompts* fora de escopo consumam recursos ou desestabilizem o motor.
  - **Limitação:** Não analisa ataques adversariais maliciosos específicos contra agentes (como *prompt injection* adversarial, *jailbreak* ou envenenamento intencional de logs).
- **Justificativa:** Discute de forma estruturada os riscos de privacidade (*GDPR/CCPA*), opacidade *black-box*, latência decisória e *distributional shift* na Seção V (pp. 15–16), além de implementar filtragem de *prompts*, mas sem modelagem de ameaças cibernéticas adversariais (`P = 0.5`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Agenda de Evolução do Framework *RRE* (Seção V.A–I, pp. 15–16):** Propõe oito direções concretas de pesquisa futura: (1) incorporação de **aprendizado federado (*federated learning*)** e **privacidade diferencial (*differential privacy*)** para proteção de PII sob *GDPR/CCPA*; (2) integração de técnicas de **Explainable AI (XAI)** para transparência decisória; (3) **compressão de modelo (quantização, poda/*pruning* e processamento paralelo)** para reduzir a latência abaixo de `52 ms` (Tabela 9, p. 14); (4) **otimização bayesiana (*Bayesian optimization*)** de hiperparâmetros em substituição a ajustes heurísticos; (5) **arquiteturas híbridas nuvem-borda (*cloud-edge*) e integração com *IoT*** para decisão descentralizada; (6) **detecção multimodal de anomalias baseada em saliência visual (*saliency-based anomaly detection*)**; e (7) uso de **aprendizado por reforço (*reinforcement learning*)** para autoaprendizado contínuo de testes sem intervenção humana.
- **Justificativa:** Apresenta direções futuras claras e alinhadas às limitações identificadas no próprio sistema (Seção V, pp. 15–16), embora circunscritas à evolução do próprio framework de varejo (`P = 0.5`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 0.5 + 1.0 + 1.0 + 0.5 + 0.5 = 3.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P13 |
| **Autores** | Lalit Narayan Mishra; Biswaranjan Senapati |
| **Ano** | 2025 |
| **Título** | *Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 13, pp. 50226–50243 |
| **DOI** | `10.1109/ACCESS.2025.3552592` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Estudo Primário Experimental com RSL Preliminar Embarcada (56 referências, 11 tabelas) |
| **Domínio Principal** | Engenharia de Software Resiliente e Automação de Testes orientados por *Agentic AI* e *Test-Driven Development (TDD)* |
| **Tecnologias / Frameworks Analisados** | **Retail Resilience Engine (RRE)**, Modelo *Transformer/GPT* customizado de 16 camadas (`8-head attention`, `512` dim), *Test-Driven Development (TDD)*, *AI Agent API*, *Application Control Unit*, Algoritmo de Filtragem de *Prompts* por Similaridade de Cosseno (Algoritmo 1), GPUs *NVIDIA A100* |
| **Escopo de Aplicação** | Confiabilidade e resiliência de sistemas comerciais de varejo: geração e execução automatizada de testes TDD, análise de logs operacionais e de sistema (`85.000` logs), mitigação de riscos, previsão de demanda e gestão de inventário |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `P` | `0.5` | Integração conceitual entre *Agentic AI* e *Test-Driven Development (TDD)* para substituir validação manual multinível por decisão automatizada orientada a testes (Seções I–II, Tabelas 1–2, pp. 1–4). Conceituação de agência restrita a um *Transformer* único com API de controle. |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Arquitetura modular de 4 camadas do **RRE** (*Data Source, Pre-processing, Feature Management, Software Layers*, Fig. 1, pp. 4–5); *Transformer* de 16 camadas detalhado na Tabela 4 (p. 8) e Eqs. 1–18; armazenamento dinâmico de atributos sem retreinamento total; e *guardrail* de entrada via **Algoritmo 1 (*Relevancy Verification Algorithm*)** com 22 palavras-chave (Tabela 5, p. 10). |
| **RQ3** (Evidências Empíricas e Métricas) | `T` | `1.0` | Avaliação empírica em `100.000` documentos e `4x NVIDIA A100` (Tabelas 6–11, Figs. 2–8, pp. 10–15): correlação de Pearson **$\rho = 0,96$** e **índice de similaridade de `97,5%`** com especialistas humanos ($p = 0,021$); nota **`13/15`** em qualidade de planos TDD; inferência em **`52 ms`**, **`4,2 GB` VRAM**, **`19,3 queries/s`** e latência em nuvem de **`86 ms`**; acurácia de **`0,89–0,93`** em 10 domínios (`0,92` em *Risk Mitigation*); e **`98,20%`** de acurácia na filtragem de *prompts* irrelevantes. |
| **RQ4** (Riscos, Segurança e Governança) | `P` | `0.5` | Discussão de 9 limitações na Seção V (pp. 15–16): privacidade de PII e conformidade com **GDPR/CCPA**, opacidade *black-box*, latência decisória em eventos de alta frequência, *distributional shift* perante condições de mercado inéditas e sensibilidade a dados ruidosos/enviesados, além do filtro de *prompts* (Algoritmo 1). |
| **RQ5** (Lacunas e Direções Futuras) | `P` | `0.5` | Roteiro futuro (Seção V.A–I, pp. 15–16): *federated learning* e *differential privacy*, *XAI*, compressão de modelo (*quantization/pruning*), otimização bayesiana, arquiteturas híbridas *cloud-edge/IoT*, detecção visual de anomalias por saliência e *Reinforcement Learning* para autoaprendizado em TDD. |
| **Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Boa Aderência (70,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | Delimita claramente os objetivos de pesquisa (Seção I.C, Tabela 2, pp. 2, 4) e inclui uma RSL preliminar explícita (Seção II.1–2, pp. 2–3) com 4 questões de pesquisa, 4 bases consultadas (*IEEE Xplore, SpringerLink, ScienceDirect, Google Scholar*), critérios formais de inclusão/exclusão (2018–2024) e filtragem PRISMA (`212` recuperados $\to$ `48` incluídos). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | Apresenta alta transparência arquitetural e experimental: detalha as 6 fontes e volumes exatos do *dataset* de `100.000` documentos (Tabela 3, p. 6), as 16 camadas e dimensões da rede *Transformer* (Tabela 4, p. 8), as 22 equações matemáticas, o pseudocódigo do filtro (Algoritmo 1, p. 10) e uma seção dedicada de **Reproducibility Measures** (Seção IV.I, p. 15) especificando hardware (`4x A100`), hiperparâmetros (`lr = 0.001, batch = 32, epochs = 150`), validação cruzada 5-fold e repositório disponibilizado mediante solicitação. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `Y` | `1.0` | Conduz seis baterias de experimentos quantitativos e comparativos contra três especialistas humanos sêniores (`> 10 anos`), reportando tabelas completas de alinhamento decisório (Tabela 6), qualidade de plano (Tabela 7), escalabilidade (Tabela 8), eficiência de hardware/latência (Tabela 9), robustez em 10 domínios (Tabela 10), acurácia de filtragem (Tabela 11) e teste $t$ pareado (Eq. 22). |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | Embora as conclusões decorram dos resultados experimentais e a Seção V discuta 9 limitações, o artigo apresenta deslizes metodológicos e editoriais pontuais que exigem cautela: (i) na Seção IV.H (pp. 13–14), a rejeição da hipótese nula $H_0$ no teste $t$ pareado ($p = 0,021 < 0,05$) — que estatisticamente indica diferença significativa entre médias — é interpretada textualmente como confirmação de alinhamento; (ii) há referências bibliográficas desconexas citadas para sustentar pontos do experimento (ex.: ref. [52] sobre diagnóstico de câncer de pulmão citada para escalabilidade na Tabela 8, p. 12); e (iii) a Seção IV.I (p. 15) menciona alinhamento com padrões do *"Springer Empirical Software Engineering journal"* em um artigo publicado no *IEEE Access*. |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **3.5 / 4.0** | **Qualidade Metodológica Alta (87,5%)** |

---

## Parecer Final do Revisor

O artigo **P13** (Mishra & Senapati, 2025), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, alcança qualidade metodológica na banda **Alta** (`SCORE_QA = 3.5 / 4.0`) e boa aderência às questões da RSL (`SCORE_RQ = 3.5 / 5.0`). Seu principal valor para a nossa revisão reside na demonstração empírica de como acoplar **Test-Driven Development (TDD)** e verificação contínua de comportamento (*Application Control Unit* + *AI Agent API*) a um motor baseado em *Transformer* treinado sobre **`85.000` logs operacionais e de sistema** (Tabela 3, p. 6). O estudo contribui diretamente para a **RQ2** e a **RQ3** com métricas de produção concretas — **latência de inferência de `52 ms`** (`86 ms` ponta a ponta em nuvem), **consumo de `4,2 GB` de VRAM**, **alinhamento de `96%` ($\rho = 0,96$) / similaridade de `97,5%`** com especialistas humanos e um **filtro de *prompts* por similaridade de cosseno (Algoritmo 1)** que bloqueia **`98,20%`** das entradas irrelevantes antes da inferência.
