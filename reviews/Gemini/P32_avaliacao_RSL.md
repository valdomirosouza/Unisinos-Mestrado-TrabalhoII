# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P32
- **Título:** *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems*
- **Autores:** Wenya Zhang; Zhi Yang; Fang Peng; Le Zhang; Yiting Chen; Ruibo Chen
- **Periódico/Conferência:** *Electronics* (MDPI), Vol. 15, Artigo 243, pp. 1–19 (Publicado em 5 de janeiro de 2026)
- **DOI:** `10.3390/electronics15010243`
- **Arquivo avaliado:** `P32-A2-electronics-15-00243-v2.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental (*Article*), propondo o framework **GALR** (*Graph-Based Root Cause Localization and LLM-Assisted Recovery*) e avaliando-o em três conjuntos de dados de sistemas de microsserviços (*Customer Service*, *Power Grid Resource* e *SockShop*).
- **Foco técnico:** Arquitetura em malha fechada para localização de causa raiz e planejamento de recuperação (*self-healing*) em microsserviços, acoplando Redes Neurais em Grafos com Atenção (*Graph Attention Networks* — GAT) enriquecidas por *priors* semânticos de probabilidade/incerteza extraídos de *logs* via LLM (`DeepSeek V3`) a um agente de recuperação aumentado por recuperação de casos (*Retrieval-Augmented Recovery Agent* com `BGE-M3`) e verificação de consistência contra *playbooks* padrão.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Totalmente atendido. O estudo aborda diretamente a localização de causa raiz multimodal (*logs*, métricas e *traces*) e um agente baseado em LLM+RAG para geração verificável de planos de recuperação de incidentes em microsserviços.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *Electronics*, Vol. 15, janeiro de 2026).
  - *IC3 (Rigor técnico/metodológico):* Atendido (formulação matemática completa nas Equações 1–13, Algoritmo 1, avaliação em 3 *datasets* contra 6 *baselines* de RCA e 2 *baselines* de geração de planos, além de estudo de ablação).
- **Critérios de Exclusão (EC):** Não incide em nenhum critério de exclusão.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P32 | Electronics | 2026 | [VERIFICAR] | Q2 [VERIFICAR] | A2 [VERIFICAR] | Artigo Experimental / Empírico (Primário) | `10.3390/electronics15010243` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q2`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF e devem ser verificados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P32 | GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems | **RQ1** (Contexto e Definições) | Respondida Plenamente | **T** (1.0) | Seção 1 (pp. 1–2); Seção 3, Figura 1, Algoritmo 1 (pp. 5–11); Seção 5 (p. 16) | **(a) Definição de autonomia:** Propõe um fluxo de *self-healing* da percepção de anomalias à geração de planos de recuperação com mínima intervenção humana, mas estabelece uma fronteira clara de segurança (Seção 5, p. 16): separa a geração da execução, restringe ações a *templates* predefinidos e exige escalonamento para confirmação manual humana ou *canary release* caso restrições de segurança sejam violadas. **(b) Características centrais:** Integra inferência semântica de estados com incerteza explícita via LLM ($s_i = [p_{\text{anom}}, p_{\text{norm}}, p_{\text{uncert}}]$, Equação 8), memória episódica de 500 casos históricos de recuperação ($\mathcal{C}$, p. 13) e verificação de consistência contra *playbooks* de especialistas. **(c) Modelo decisório:** Acoplamento neuro-simbólico/híbrido entre propagação em grafo de chamadas via GAT (com decaimento temporal $\omega_{ij}$ e viés semântico $\Delta_{ij}$ derivado do LLM, Equações 4–11) e planejamento de recuperação via RAG + verificação de sobreposição de ações (Equações 12–13, pp. 8–11). |
| P32 | GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seção 3, Figura 1, Tabela 1, Equações 1–13, Algoritmo 1 (pp. 5–11); Seção 4.3 (p. 13) | **(a) Tipo de arquitetura:** Pipeline unificado em 4 módulos (*GALR*, Figura 1, p. 6): fusão multimodal de métricas/*logs*/*traces*, enriquecimento semântico de nós via LLM, localização de causa raiz baseada em GAT e agente de planejamento de recuperação baseado em RAG. **(b) Ferramentas/frameworks:** Ambiente *Kubernetes* (*SockShop*), *Chaos-Mesh* (injeção de falhas), *Locust* (geração de carga), *Prometheus* (métricas), *Fluent Bit* (*DaemonSet* de *logs*); rede `GATConv` (2 camadas, 4 cabeças, otimizador `AdamW`, `BCEWithLogitsLoss` ponderada); LLM `DeepSeek V3` e modelo de *embeddings* `BGE-M3` sobre biblioteca $\mathcal{C}$ de 500 casos curados (Seção 4.3, p. 13). **(c) Capacidades avançadas:** Vetor de probabilidade suave com incerteza ($p_{\text{uncert}}$), injeção de regras de negócio no *prompt* (p. 9), viés de atenção semântico aprendível ($\Delta_{ij} = \lambda \cdot p_i^{\text{anom}} \cdot p_j^{\text{anom}}$, Equação 10) e verificação de consistência de planos contra *playbooks* padrão (Equação 13, p. 10). |
| P32 | GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems | **RQ3** (Benefícios e Evidências) | Respondida Plenamente | **T** (1.0) | Seção 4, Tabelas 2–5, Figura 2 (pp. 11–16) | **(a) Benefícios qualitativos:** Alinhamento entre semântica profunda de *logs* e raciocínio estrutural de dependências em grafos, gerando planos de recuperação estruturados (ações, métricas de verificação, *rollback* e resultados esperados, p. 10). **(b) Benefícios quantitativos:** Avaliado em 3 *datasets* com 6 tipos de falhas e cadeias de 5–20 *hops* (Tabela 2, p. 12): *Customer Service* (23.183 *traces*, 67 serviços), *Power Grid Resource* (19.872 *traces*, 89 serviços) e *SockShop* (8.981 *traces*, 15 serviços). Na localização de causa raiz (Tabela 3, p. 14), supera 6 *baselines* (*MicroRank*, *GCN*, *GraphSAGE*, *MicroEGRCL*, *DiagFusion*, *PDiagnose*) em todos os cenários, atingindo `MRR` médio de `0.931` (`Customer Service`: `Top-1 = 0.842`, `MRR = 0.923`; `Power Grid`: `Top-1 = 0.883`, `MRR = 0.916`; `SockShop`: `Top-1 = 0.931`, `MRR = 0.953`). Na geração de planos de recuperação (Tabela 4, p. 15), `LLM + RAG (GALR)` atinge `79.2%` (*SockShop*), `75.8%` (*Power Grid*) e `70.1%` (*Customer Service*), superando `Few-shot` (`68.9%`, `61.5%`, `54.3%`) e `Zero-shot` (`62.5%`, `55.1%`, `48.9%`). Ablações (Tabela 5) confirmam a contribuição da atenção nas arestas. **(c) Nível de evidência:** Experimentos controlados em 3 *datasets* de microsserviços com injeção de falhas e estudo de ablação. |
| P32 | GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems | **RQ4** (Desafios e Ética) | Respondida Plenamente | **T** (1.0) | Seção 3.4 (p. 10); Seção 4.3 (p. 13); Seção 5 (p. 16); Seção 6 (p. 17) | **(a) Desafios técnicos:** Analisa quatro limitações (Seção 5, p. 16): (1) gargalo de escalabilidade e latência em grafos extensos devido à agregação de vizinhança e consultas de anotação/recuperação ao LLM; (2) sensibilidade à qualidade do alinhamento multimodal e estabilidade de *templates* de *logs* entre plataformas; (3) risco de estratégias incompletas ou alucinadas sob *distribution shifts* (falhas inéditas ou *logs* ruidosos); e (4) limitações da injeção de falha única e avaliação *offline*. **(b) Desafios éticos/governança:** Destaca a criticidade de segurança (*safety-critical*) da execução automatizada de ações de recuperação em sistemas de produção (p. 16). **(c) Mecanismos de governança:** Separação entre geração e execução, espaço de ação atômico restrito (*restart*, *rollback*, *migration*, *scaling*) mapeado em *templates* de comando, escore de consistência contra *playbooks* padrão (Equação 13), restrições de parâmetros (*allowlists*, limites numéricos, operações proibidas) e escalonamento para confirmação humana/validação em *canary release* (pp. 10, 13, 16). |
| P32 | GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção 5 (p. 16); Seção 6 (*Conclusions*, p. 17) | Aponta três direções futuras prioritárias (p. 17): (1) aprimoramento da escalabilidade e latência mediante anotação LLM seletiva e incremental combinada com políticas de *caching* e atualização (*refresh policies*); (2) introdução de *guardrails* de segurança mais estritos para execução de recuperação, incluindo espaços de ação restritos e validação formal em nível de parâmetros; e (3) estabelecimento de verificação *online* controlada em ambientes vivos, juntamente com protocolos de avaliação e *benchmarks* mais fiéis (cobrindo efeitos em cascata/retardados e testes de significância estatística). |
| **P32** | **SCORE_RQ Total** | — | **5.0 / 5.0** | — | — | Atende plenamente todas as cinco questões de pesquisa da RSL (RQ1 a RQ5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P32 | Artigo Experimental / Empírico (Primário) | Y (1.0) | P (0.5) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** Articula com precisão as três lacunas que limitam o *self-healing* prático em microsserviços (separação entre localização e recuperação, redução de *logs* a *templates* rasos desconectados do raciocínio em grafos e dependência de *playbooks* estáticos manuais) e apresenta de forma clara a arquitetura unificada GALR (Seções 1–3, pp. 1–6).
- **QA2 — Metodologia Replicável (P = 0.5):** Apresenta formulação matemática rigorosa (Equações 1–13), tabela de notações (Tabela 1), pseudocódigo do *pipeline* (Algoritmo 1), estatísticas dos 3 *datasets* (Tabela 2) e configuração detalhada do ambiente experimental (*Kubernetes*, *Chaos-Mesh*, *Locust*, *Prometheus*, *Fluent Bit*, `GATConv`, `AdamW`, `DeepSeek V3`, `BGE-M3`, biblioteca $\mathcal{C}$ de 500 casos, Seção 4.3, p. 13). Recebe pontuação parcial porque os dados e códigos estão disponíveis apenas mediante solicitação (p. 17), a avaliação dos planos de recuperação restringe-se à sobreposição *offline* de tipos de ação sem validar parâmetros específicos de execução (p. 13) e os resultados reportados são médias de apenas duas execuções sem teste de significância estatística (pp. 16–17).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Conduz avaliação experimental abrangente sobre três conjuntos de dados de microsserviços (*Customer Service* com 23.183 *traces*, *Power Grid Resource* com 19.872 *traces* e *SockShop* com 8.981 *traces*), comparando a localização de causa raiz (`Top-1`, `Top-3`, `Top-10` e `MRR`) contra 6 *baselines* representativas (*MicroRank*, *GCN*, *GraphSAGE*, *MicroEGRCL*, *DiagFusion* e *PDiagnose*, Tabela 3), a geração de estratégias de recuperação contra *Zero-shot* e *Few-shot* (Tabela 4) e realizando estudo de ablação do módulo de atenção (Tabela 5).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões derivam diretamente das evidências empíricas e os autores demonstram elevado rigor científico nas Seções 5 e 6 (pp. 16–17) ao explicitar todas as ressalvas metodológicas do trabalho (cenário *single-node/single-fault*, validação *offline* de ações de recuperação sem execução ao vivo e ausência de testes de significância estatística sobre as duas rodadas).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
O artigo propõe o **GALR**, um framework unificado para localização de causa raiz e recuperação assistida por LLM em sistemas de microsserviços que injeta *priors* semânticos de anomalia e incerteza ($s_i = [p_{\text{anom}}, p_{\text{norm}}, p_{\text{uncert}}]$ extraídos via `DeepSeek V3`) diretamente no mecanismo de atenção de uma *Graph Attention Network* (GAT) com decaimento temporal, acoplando-a a um agente RAG (`BGE-M3` sobre 500 casos históricos) que gera planos de recuperação verificados contra *playbooks* de especialistas. Nos três *datasets* avaliados (*Customer Service*, *Power Grid Resource* e *SockShop*), o GALR atinge `MRR` médio de `0.931` (superando 6 *baselines* de grafos/RCA) e eleva a acurácia de estratégias de recuperação para `70.1%–79.2%`. Além disso, oferece uma excelente discussão de *guardrails* para *self-healing* seguro (separação geração-execução, *allowlists* de parâmetros, espaço de ação restrito e *canary release*), atingindo pontuação máxima nas RQs (`SCORE_RQ = 5.0/5.0`) e qualidade Alta (`SCORE_QA = 3.5/4.0`).

### Recomendação
**INCLUIR** — Estudo primário altamente aderente a todas as questões de pesquisa da RSL (`SCORE_RQ = 5.0/5.0`, `SCORE_QA = 3.5/4.0`, Banda Alta), destacando-se pela integração elegante entre GNNs e LLMs na localização multimodal de falhas e pela proposta de mecanismos concretos de governança e verificação de consistência para geração segura de *playbooks* de recuperação.

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q2` para *Electronics* (MDPI) no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
