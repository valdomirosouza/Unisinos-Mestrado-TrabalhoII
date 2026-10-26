# Avaliação Sistemática de Estudo Primário — RSL (Kitchenham et al., 2009 / DARE)

## Identificação do Estudo
- **ID do Artigo:** P35
- **Arquivo PDF Avaliado:** [P35-A2-TSP_CMC_77908.pdf](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/P35-A2-TSP_CMC_77908.pdf)
- **Prompt de Referência:** [prompt-P35.md](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/prompt-P35.md)
- **Título:** *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps*
- **Autores:** Haodong Zou; Yichen Zhao; Xin Chen; Ling Wang; Jinghang Yu (State Grid Jiangsu Electric Power Co., Ltd., Nanjing, China); Long Yuan (Wuhan University of Technology, Wuhan, China)
- **Periódico / Fonte:** *Computers, Materials & Continua* (Tech Science Press), Vol. 88, No. 1, Art. 40, pp. 1–24, 2026
- **DOI:** `10.32604/cmc.2026.077908`

---

## Etapa 0 — Extração Bibliométrica e Escopo

- **Metadados verificados no PDF:** Artigo publicado em *Computers, Materials & Continua* (Tech Science Press), Vol. 88, No. 1, Art. 40, pp. 1–24, 2026 (Recebido em 19 de dezembro de 2025; Aceito em 13 de março de 2026; Publicado em 08 de maio de 2026, p. 1).
- **Métricas externas (`[VERIFICAR]`):**
  - **Citações:** `[VERIFICAR]` (não consta no PDF; verificar no *Scopus* ou *Google Scholar*).
  - **SJR / Quartil:** Informado como `Q2` no input do protocolo (`[VERIFICAR]` no *Scimago Journal Rank* para *Computers, Materials and Continua*, ISSN 1546-2218 / 1546-2226).
  - **Qualis CAPES:** Informado como `A2` no input do protocolo (`[VERIFICAR]` na *Plataforma Sucupira / Qualis Periódicos* na área de Ciência da Computação).
- **Adequação ao Escopo Temático da RSL:** **Altamente aderente (Core Match)**. O estudo propõe e avalia empiricamente uma arquitetura multiagente baseada em LLMs (*GPT-4 Turbo*) aumentada por grafo multimodal (*Anomaly Fusion Graph* — AFG) para Análise de Causa Raiz (*Root Cause Analysis* — RCA) em operações de TI e sistemas distribuídos de microsserviços em nuvem (AIOps).

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério PRISMA | Status | Evidência no Texto / Justificativa |
| :--- | :---: | :--- |
| **1. Publicação entre 2020 e 2026** | **Atende** | Publicado em 2026 (*Computers, Materials & Continua*, Vol. 88, No. 1, p. 1). |
| **2. Qualis A1–A2** | **`[VERIFICAR]`** | Informado no metadado do protocolo como `A2` (requer verificação externa na Plataforma Sucupira). |
| **3. Escopo: IA Agêntica em redes, segurança ou operações de TI** | **Atende** | Foco central em IA Agêntica aplicada a AIOps e RCA em sistemas de microsserviços (Seções 1–5, pp. 1–18). |
| **4. Texto completo disponível e acessível** | **Atende** | Texto integral completo de 24 páginas analisado via PDF, incluindo Apêndice A com templates de prompts (pp. 19–23). |
| **5. Sem critérios de exclusão (não é apenas ML clássico, IoT puro, resumo ou duplicata)** | **Atende** | Artigo completo de pesquisa original (*Research Article*) com arquitetura multiagente baseada em LLM e validação experimental extensa em 5 datasets. |

**Status da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (aprovado integralmente nos critérios de conteúdo, recorte temporal e completude; pendente apenas da confirmação externa de Qualis/SJR).

---

## Tabela A — Extração Bibliométrica (Tabela 3 do Protocolo)

| ID | Autores | Título | Ano | Fonte | Qualis | SJR | Citações | Escopo_Resumo |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **P35** | Zou, H.; Zhao, Y.; Chen, X.; Wang, L.; Yu, J.; Yuan, L. | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | 2026 | *Computers, Materials & Continua* (Vol. 88, No. 1, Art. 40, pp. 1–24) | A2 `[VERIFICAR]` | Q2 `[VERIFICAR]` | `[VERIFICAR]` | Propõe um framework multiagente baseado em LLM (*GPT-4 Turbo*) sobre um Grafo de Fusão de Anomalias (*AFG* multimodal unindo logs e traces OpenTelemetry) para Análise de Causa Raiz (RCA) em microsserviços (AIOps), utilizando quatro agentes especializados (*Diagnoser*, *Navigator*, *Verifier* e *Coordinator*) com protocolo de validação adversarial e *backtracking* dinâmico em pilha. |

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5 do Protocolo)

| Questão de Pesquisa (RQ) | Classificação | Pontuação | Evidências e Justificativa Detalhada (com páginas, seções, tabelas e figuras) |
| :--- | :---: | :---: | :--- |
| **RQ1 (Adaptação e autonomia de modelos fundacionais como agentes para gestão de redes/TI)** | **T** | **1.0** | **Abordagem completa e explícita.** O framework simula uma equipe humana de *Site Reliability Engineering* (SRE) operando sob um ciclo *Perceive-Reason-Act* (Seção 4, p. 5) e modela o diagnóstico como um *Sequential Decision-Making Process* (SDMP) sobre um "modelo de mundo" estruturado (*Anomaly Fusion Graph* — AFG) com protocolo *Investigate-and-Walk* / *Diagnose-Propagate-Decide* (Seção 4.2, Algoritmo 3, pp. 10–13). A arquitetura decompõe papéis em 4 agentes especializados (Figura 4, pp. 10–12): (1) *Diagnoser Agent* (avaliador de estado que aplica *Chain-of-Thought* para distinguir erros intrínsecos de sintomas extrínsecos propagados, Eq. 7); (2) *Navigator Agent* (política de transição / roteador probabilístico que calcula o "gradiente de falha" local com base em desvio de latência, taxa de propagação de erro e volatilidade de tráfego, Eq. 8); (3) *Verifier Agent* (validador consensual sob *Adversarial Validation Protocol*, Eq. 9); e (4) *Coordinator Agent* (memória e controle via *Shared Diagnostic Context* — SDC estilo *blackboard*, mantendo *Visited Set*, *Hypothesis Stack* LIFO para *backtracking* e *Contextual Summary*). |
| **RQ2 (Arquiteturas, padrões de design e integração com infraestrutura de TI)** | **T** | **1.0** | **Arquitetura detalhada e reproduzível.** Apresenta arquitetura em duas camadas (Figura 2, p. 5; Algoritmos 1–3, pp. 6–13) e todos os 7 templates de prompts no Apêndice A (pp. 19–23): (1) *AFG Construction* (Seção 4.1, Algoritmos 1–2, Eqs. 1–6): agrupamento grosseiro por proximidade espaço-temporal ($P_{st}$, Eq. 4) $\to$ associação fina híbrida log-span ($P_{assoc}$, Eq. 5) $\to$ *LLM Arbitration* apenas para casos ambíguos de alta concorrência ($\tau_{low} \le p_{max} < \tau_{high}$, Figura 3, p. 8) $\to$ *LLM Summarizer* para gerar relatórios estruturados de saúde de nó ($R_v$, Eq. 6); (2) *Multi-Agent Collaborative Reasoning* (Seção 4.2, Algoritmo 3). Implementado em Python 3.9 integrando `Drain3` (parsing de logs), `OpenTelemetry` (processamento de traces distribuídos) e `OpenAI GPT-4 API` (`GPT-4 Turbo`), executado em servidor com 2x Intel Xeon Gold 6248R, 512 GB RAM e 4x GPUs NVIDIA A100, com hiperparâmetros definidos por *grid search* ($\tau_{prox}=0.6$, $\tau_{conf}=0.85$, $\tau_{verify}=0.90$, profundidade máxima $D_{max}=10$, Seção 5.1, pp. 13–15). |
| **RQ3 (Cenários de avaliação, métricas de desempenho e eficácia)** | **T** | **1.0** | **Avaliação empírica multi-dataset rigorosa.** Avaliado em 5 benchmarks (Tabela 1, p. 14): *Train Ticket (TT)* (45 serviços, 73 falhas, >132K traces, 7,7M logs), *Online Boutique (OB)* (56 falhas), *MSDS* (OpenStack, 80+ falhas), *AIOps Challenge 2025* (400 falhas, coletadas via Prometheus, DeepFlow, Jaeger e Filebeat) e *OpenTelemetry Demo (OTel)* (45 falhas). **Principais resultados:** (1) *Localização de Causa Raiz* (Tabela 2, p. 15, média $\pm$ DP em 5 execuções): alcança média de `Precision = 87,5 ± 0,9%`, `Recall = 89,2 ± 1,0%` e `F1-Score = 88,4 ± 0,9%` (`TT: 88,2%`, `OB: 90,5%`, `MSDS: 86,4%`, `AIOps: 89,1%`, `OTel: 87,6%`), superando *DeepTraLog* (`Avg F1 = 83,8 ± 1,3%`, +4,6 pp, $p < 0,01$ no teste-$t$ pareado) e *Direct LLM Diagnosis* (`Avg F1 = 71,4 ± 2,1%`, +17,0 pp); (2) *Qualidade da Associação Log-Trace* (Tabela 3, p. 16): `F1 médio = 97,5%` (`Precision = 97,0%`, `Recall = 98,0%`) vs. *Temporal Window* (`68,9%`) e *Semantic-Temporal* (`79,1%`); (3) *Robustez da Verificação no AIOps* (Tabela 4, pp. 16–17): *Consensus-Based Verification* atinge `F1 = 89,1%` (`Precision = 88,1%`) vs. *Single-Pass* (`86,6%`) e *No Verification* (`83,7%`, `Precision = 79,5%`); (4) *Ablação no Train Ticket* (Tabela 5, p. 17): remoção do *Verifier Agent* reduz o F1 de `88,2%` para `82,9%` (`-8,5%` em Precision); sem *Dynamic Backtracking* cai para `79,2%` (`-13,6%` em Recall); sem *Heuristic Navigation* cai para `75,3%`; (5) *Latência e Custo* (Tabela 6, pp. 17–18): latência média total de `21,4 s` por falha (`3,3 s` construção do AFG + `18,1 s` raciocínio multiagente com 3–5 chamadas), consumo médio de `9,7K tokens` (`8,5K` OB a `12,3K` AIOps), arbitragem LLM acionada em apenas `16,1%` (`13,8%–20,3%`) dos pares log-trace e custo médio de `~$0,15` por falha diagnosticada. |
| **RQ4 (Desafios de segurança, confiabilidade, alucinação, guarda-corpos e limitações)** | **P** | **0.5** | **Análise técnica aprofundada de modos de falha e guarda-corpos contra alucinação, mas sem discussão de governança ética/regulatória.** Implementa mecanismos explícitos de mitigação de alucinação e propagação de erros: *Adversarial Validation Protocol* com ensemble em 3 perspectivas (*Consistency Check* contra Golden Signals, *Causal Sufficiency* e *Counterfactual Reasoning* / *Devil's Advocate*, Seção 4.2.3, p. 11), *backtracking* em pilha LIFO e limite de profundidade ($D_{max}=10$). Na Seção 5.2.6 e Tabela 7 (p. 18), quantifica e categoriza a taxa residual de falha (`8,2% a 11,3%` entre os datasets) em três modos: (1) *Ambiguous Propagation Chains* (`59%` das falhas, ex.: *timeouts* em cascata quase simultâneos); (2) *Insufficient Log Semantics* (`28%` das falhas, mensagens genéricas como `"Error occurred"`); e (3) *Backtracking Degradation in Dense Topologies* (quando o *fan-out* do nó $> 10$, o *backtracking* aproxima-se de busca exaustiva; em `12%` dos casos do AIOps excede 5 iterações e eleva a latência em `~40%`). Também reporta que a arbitragem LLM (`94,2%` de acurácia) falha diante de jargões de domínio não vistos ou janelas ultracurtas ($< 10\text{ ms}$). Não discute impactos éticos, privacidade ou conformidade regulatória. |
| **RQ5 (Tendências futuras e direções de pesquisa abertas)** | **N** | **0.0** | **Não abordado.** Nem a análise de falhas (Seção 5.2.6, p. 18) nem a conclusão (Seção 6, p. 18) formulam uma agenda de trabalhos futuros ou direções abertas de pesquisa (o texto diagnostica as limitações atuais, mas encerra sem propor extensões futuras). |
| **Pontuação Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Média de aderência às RQs: 70,0% (3 Ts, 1 P, 1 N).** |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 do Protocolo)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências do Artigo |
| :--- | :---: | :---: | :--- |
| **QA1 (Clareza e explicitação dos objetivos e questões da pesquisa)** | **Y** | **1.0** | A Seção 1 (*Introduction*, pp. 1–3) define claramente os três gargalos de RCA em microsserviços (desalinhamento entre logs e traces sob alta concorrência, sobrecarga de contexto em LLMs diretos e ausência de verificação auto-corretiva) e enumera explicitamente as contribuições do artigo (p. 3). |
| **QA2 (Descrição adequada do método, arquitetura e reprodutibilidade)** | **P** | **0.5** | Fornece formalização matemática completa (Eqs. 1–9), três algoritmos passo a passo (Algoritmos 1–3, pp. 6, 8, 12), hiperparâmetros de *grid search* (Seção 5.1.4, pp. 14–15) e todos os 7 templates de prompts no Apêndice A (pp. 19–23). Contudo, declara na seção *Availability of Data and Materials* (p. 19): *"Data are unavailable due to privacy or ethical restrictions"*, não disponibiliza repositório de código-fonte e não especifica qual modelo exato de *sentence embedding* ($\Phi$) foi utilizado na Eq. 5 (p. 7). |
| **QA3 (Suficiência da validação empírica, cenários e métricas)** | **Y** | **1.0** | Validação experimental robusta em 5 datasets (totalizando >654 casos de falha), comparada contra 8 *baselines* cobrindo métodos baseados em traces, logs, multimodais e LLMs diretos (Tabela 2, p. 15), com médias e desvios-padrão sobre 5 execuções, testes-$t$ pareados de significância estatística ($p < 0,01$), estudos de ablação (Tabela 5), análise de custo/latência/tokens (Tabela 6) e taxonomia quantitativa de falhas (Tabela 7). |
| **QA4 (Consistência entre resultados obtidos e conclusões reportadas)** | **Y** | **1.0** | As conclusões (Seção 6, p. 18) refletem com exatidão os ganhos empíricos reportados nas Tabelas 2–6 e são devidamente temperadas pela análise de casos de falha e limitações de topologias densas na Seção 5.2.6 (Tabela 7, p. 18). |
| **Pontuação Total (`SCORE_QA`)** | **Banda Alta** | **3.5 / 4.0** | **Qualidade metodológica Alta (`SCORE_QA = 3.5`, faixa $\ge 3.0$).** |

---

## Parecer Final do Revisor

### Síntese Crítica (3–5 linhas)
O artigo **P35** apresenta uma contribuição técnica e experimental de alto rigor para a área de AIOps ao combinar um Grafo de Fusão de Anomalias multimodal (*AFG*, unindo logs e traces OpenTelemetry com arbitragem seletiva por LLM) a um sistema multiagente inspirado em equipes SRE (*Diagnoser*, *Navigator*, *Verifier* e *Coordinator*). O protocolo de validação adversarial em três ângulos e o mecanismo de *backtracking* dinâmico em pilha LIFO demonstram eficácia empírica consistente em cinco benchmarks (`F1 médio = 88,4%`, superando *DeepTraLog* em +4,6 pp com $p < 0,01$), mantendo custo operacional viável (`21,4 s` e `~$0,15` por falha). A presença dos algoritmos completos, análise de ablação, perfilamento de custo/tokens e catálogo de prompts no Apêndice A torna o estudo uma referência central para responder às questões **RQ1, RQ2, RQ3 e RQ4** da RSL.

### Recomendação Final
- **Decisão:** **INCLUIR**
- **Justificativa:** Estudo primário diretamente alinhado ao escopo central de IA Agêntica para operações de TI (AIOps/RCA), com excelente pontuação de qualidade metodológica (`SCORE_QA = 3.5/4.0`, Banda Alta) e forte cobertura das questões de pesquisa (`SCORE_RQ = 3.5/5.0`).

### Pendências de Verificação Externa (`[VERIFICAR]`)
1. **Qualis CAPES:** Confirmar a classificação `A2` do periódico *Computers, Materials & Continua* (ISSN 1546-2218 / 1546-2226) na *Plataforma Sucupira (Qualis Periódicos)* na área de Ciência da Computação.
2. **SJR / Quartil:** Confirmar o quartil `Q2` e o índice SJR vigente no portal *Scimago Journal Rank*.
3. **Citações:** Levantar o número atual de citações do artigo (`DOI: 10.32604/cmc.2026.077908`) no *Scopus* ou *Google Scholar*.
