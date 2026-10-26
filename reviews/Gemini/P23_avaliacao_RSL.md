# Avaliação Sistemática de Literatura — Estudo P23

**Artigo avaliado:** *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems*  
**Autores:** Xiao Zhang; Qi Wang; Mingyi Li; Yuan Yuan; Mengbai Xiao; Fuzhen Zhuang; Dongxiao Yu  
**Arquivo fonte:** `P23-A1-TAMOFine-Grained_Root_Cause_Analysis_via_Tool-Assisted_LLM_Agent_With_Multi-Modality_Observation_Data_in_Cloud-Native_Systems.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — 2025 (novembro/dezembro de 2025, p. 1 / p. 4221).
- **Publicação ≠ NULL (veículo identificável):** Sim — *IEEE Transactions on Services Computing*, Volume 18, Número 6, pp. 4221–4233.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science, IEEE Xplore ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *IEEE Transactions on Services Computing*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P23 | IEEE Transactions on Services Computing (Vol. 18, No. 6, pp. 4221–4233) | 2025 | `[VERIFICAR]` (base indexadora: Scopus / IEEE Xplore / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Artigo de pesquisa empírica / Proposta de framework agêntico assistido por ferramentas multimodais com avaliação em benchmarks | `10.1109/TSC.2025.3629066` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P23 | TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems | RQ1 | Parcialmente Respondida | P (0.5) | Seção I (pp. 4221–4222); Seção III e III-D (pp. 4223, 4226); Figuras 2 e 3 (pp. 4224, 4227) | **(a) Autonomy definition:** O agente especialista ($\mathcal{A}$) atua como copiloto analítico (*human-in-the-loop*) que sintetiza inferências de ferramentas de percepção para fornecer relatórios de diagnóstico e planos de reparo a engenheiros SRE, sem execução autônoma no cluster. **(b) Core characteristics:** Uso de ferramentas especializadas de *deep learning* ($\mathcal{T}_1, \mathcal{T}_2, \mathcal{T}_3$) para percepção multimodal e raciocínio contextual via *prompt* estruturado; não implementa memória agêntica episódica ou planejamento iterativo multi-rodadas. **(c) Decision-making model:** Pipeline sequencial *feed-forward* em que as saídas quantitativas de localização e classificação de falhas são injetadas em um *template* de *prompt* do GPT-4 (Figura 3) para geração de análise de impacto, prioridade e medidas de reparo. |
| P23 | TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems | RQ2 | Respondida Plenamente | T (1.0) | Seção III-A a III-D (pp. 4223–4226); Figura 2 (p. 4224); Seção IV-B4 (p. 4228); Tabela IV (p. 4230) | **(a) Architecture type:** Arquitetura híbrida desacoplada composta por três ferramentas neurais de percepção ($\mathcal{T}_1$: alinhamento multimodal por difusão colaborativa de duplo ramo; $\mathcal{T}_2$: localização de causa raiz via FFT com filtro passa-alta + *self-attention* em frequência + GAT; $\mathcal{T}_3$: classificação de tipos de falha via Transformer + GAT + MLP) e um Agente Especialista RCA ($\mathcal{A}$). **(b) Tools/frameworks:** *PyTorch 2.4.0*, *CUDA 12.1*, parser de logs *Drain* + TF-IDF, *Patch-based Transformer*, *Graph Attention Network* (GAT) e *GPT-4*. **(c) Advanced capabilities:** Alinhamento temporal generativo de logs, métricas e traces (evitando estourar a janela de contexto do LLM) e construção dinâmica de grafo causal de propagação de falhas multi-nível (*Pod*, *Service*, *Node*). |
| P23 | TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems | RQ3 | Respondida Plenamente | T (1.0) | Seção I (p. 4222); Seção IV-B a IV-G (pp. 4227–4231); Tabelas II, III e IV (pp. 4229–4230); Figuras 4 a 7 (pp. 4230–4231) | **(a) Qualitative benefits:** Supera omissões e diagnósticos incorretos de LLMs alimentados diretamente com dados brutos, produzindo recomendações de remediação precisas e granulares por camada (ex.: ajuste de HPA/reinício de pod para sobrecarga de CPU em `CheckoutPod0` e inspeção de plugin CNI Calico/Cilium para perda de pacotes em `Currency Service`, Figura 7). **(b) Quantitative benefits / metrics:** Nos benchmarks *AIOps Challenge / HipsterShop* (Dataset A: 10 serviços, 40 pods, 6 nós, 15 tipos de falha) e *SocialNetwork* (Dataset B: 21 microsserviços), supera o estado da arte com ganho médio de 4,8% em `Acc@1` (localização) e 10,8% em `MiPr` (classificação). Em $A_n$, atinge `Acc@1` = 84,37%, `Acc@5` = 97,77%, `MiPr` = 0,8718 e `MiF1` = 0,8831; tempo de inferência das ferramentas de 0,17 s/amostra (10,96M parâmetros). **(c) Evidence level:** Avaliação experimental abrangente em 2 datasets públicos contra 9 *baselines*, acrescida de ablação e estudo de caso real. |
| P23 | TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems | RQ4 | Parcialmente Respondida | P (0.5) | Seção I (p. 4222); Seção IV-B4 (p. 4228); Seção IV-F e IV-G (pp. 4230–4231) | **(a) Technical challenges:** Analisa três limitações críticas de LLMs aplicados diretamente à observabilidade: desalinhamento semântico entre modalidades heterogêneas, restrição da janela de contexto frente a séries temporais massivas e incapacidade de modelar grafos de dependência dinâmicos; reporta ainda alta sensibilidade ao hiperparâmetro $\beta$ e necessidade de limpeza/pré-treinamento em dados normais. **(b) Ethical/governance challenges:** Não aborda questões éticas, privacidade ou responsabilidade legal. **(c) Governance mechanisms:** Opera exclusivamente em modo consultivo/assistivo para engenheiros SRE (Figura 2 e Seção III-D), sem mecanismos de governança de atuação autônoma. |
| P23 | TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems | RQ5 | Não tem conteúdo suficiente | N (0.0) | Seção V (p. 4231) | O artigo não apresenta seção ou discussão de limitações residuais do próprio método TAMO nem aponta direções de trabalhos futuros (*future work*) ou lacunas abertas na Conclusão. |
| **P23** | **TOTAL (SCORE_RQ)** | — | **3.0 / 5.0** | **2T, 2P, 1N** | — | Excelente profundidade técnica e experimental em arquitetura multimodal (RQ2) e métricas de RCA (RQ3), porém sem discussão de trabalhos futuros (RQ5) e com agente LLM restrito ao estágio final de síntese textual. |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P23 | Artigo de pesquisa empírica / Framework assistido por ferramentas com avaliação em benchmarks públicos | Y (1.0) | Y (1.0) | Y (1.0) | P (0.5) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** A Seção I (pp. 4221–4222) e a Figura 1 (p. 4223) caracterizam com clareza os três gargalos de LLMs em RCA de sistemas nativos em nuvem (entrada multimodal desalinhada, limite de janela de contexto e dependências dinâmicas) e definem o objetivo de resolvê-los por meio do framework TAMO.
- **QA2 — Metodologia Replicável (Y = 1.0):** Todas as etapas matemáticas das ferramentas $\mathcal{T}_1, \mathcal{T}_2, \mathcal{T}_3$ são formalizadas (Equações 1 a 26), o *template* de *prompt* do agente especialista $\mathcal{A}$ (*GPT-4*) é exibido na Figura 3 (p. 4227), os dois datasets utilizados são públicos (com URLs fornecidas nas notas de rodapé da p. 4227) e os hiperparâmetros, número de parâmetros (Tabela IV) e estratégia de treinamento modular em estágios são integralmente descritos (Seção IV-B4, p. 4228).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** A validação empírica utiliza dois benchmarks públicos de microsserviços (*HipsterShop / AIOps Challenge* e *SocialNetwork*), compara o método contra múltiplos *baselines* do estado da arte (*HolisticRCA*, *Eadro*, *TimesNet*, *SegRNN*, *DejaVu*, *LightGBM*, *Transformer*, *PatchTST*, *AutoFormer*), inclui estudo de ablação (Tabela III), análise de tempo de treinamento/inferência (Figura 5) e estudo de caso comparativo (Figuras 6 e 7).
- **QA4 — Conclusões Coerentes (P = 0.5):** Embora as conclusões sobre acurácia de localização e classificação derivem diretamente das evidências empíricas, o artigo não discute limitações próprias ou ameaças à validade na Seção V (p. 4231), e a avaliação da saída textual do agente LLM (*GPT-4*) restringe-se a um único estudo de caso qualitativo (Figura 7), sem métricas quantitativas sobre a qualidade das recomendações de remediação geradas pelo LLM.

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P23 propõe o framework TAMO para análise de causa raiz (RCA) fina e recomendação de reparo em sistemas de microsserviços *cloud-native* (Kubernetes), desacoplando o processamento de dados brutos multimodais (logs, métricas e traces) do LLM (*GPT-4*) por meio de três ferramentas neurais especializadas (difusão condicional colaborativa, atenção no domínio da frequência via FFT+GAT e classificador de falhas). Trata-se de uma contribuição altamente relevante sobre como superar o limite de janela de contexto e a cegueira temporal de agentes LLM em resposta a incidentes (`SCORE_RQ = 3.0/5.0`, `SCORE_QA = 3.5/4.0`, Banda Alta).
- **Recomendação:** **INCLUIR** — O artigo possui alta qualidade metodológica e experimental (`SCORE_QA = 3.5/4.0`) e resolve um problema arquitetural crítico para copilotos de resposta a incidentes (a compressão e alinhamento de telemetria multimodal em informações estruturadas consumíveis pelo agente LLM).
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science, IEEE Xplore ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *IEEE Transactions on Services Computing* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
