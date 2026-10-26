# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P31
- **Título:** *LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services*
- **Autores:** Xin Ji; Le Zhang; Wenya Zhang; Fang Peng; Yifan Mao; Xingchuang Liao; Kui Zhang
- **Periódico/Conferência:** *Electronics* (MDPI), Vol. 14, Artigo 3008, pp. 1–19 (Publicado em 28 de julho de 2025)
- **DOI:** `10.3390/electronics14153008`
- **Arquivo avaliado:** `P31-A2-electronics-14-03008.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental em escala industrial (*Article*), propondo o sistema multiagente hierárquico **LEMAD** (*LLM-Empowered Multi-Agent System for Anomaly Detection*) e avaliando-o sobre dados reais de produção da *State Grid Corporation of China* (SGCC) cobrindo 1.289 serviços e 28,88 milhões de invocações em quatro plataformas de *middleware*.
- **Foco técnico:** Integração hierárquica de Sistemas Multiagentes (MAS) distribuídos via *Apache Kafka* e Grandes Modelos de Linguagem (`BERT`, `gpt-4o-mini`, `LLaMA`, `DeepSeek-v3`) para coleta multimodal (*logs* e métricas), correlação em *streaming* (*PyFlink*), detecção de anomalias compostas, localização de causa raiz e geração de recomendações explicáveis de O&M em infraestruturas *cloud-native* de redes elétricas.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Totalmente atendido. Apresenta uma arquitetura multiagente potencializada por LLMs operando em ciclo fechado *"sense–analyze–diagnose–respond"* para detecção de anomalias, diagnóstico de causa raiz e recomendações operacionais em produção.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *Electronics*, Vol. 14, julho de 2025).
  - *IC3 (Rigor técnico/metodológico):* Atendido (arquitetura de produção detalhada em *Kubernetes*/*Kafka*/*Flink*, avaliação em 4 plataformas industriais contra 7 *baselines*, medição de latência de inferência e estudo de ablação).
- **Critérios de Exclusão (EC):** Não incide em nenhum critério de exclusão.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P31 | Electronics | 2025 | [VERIFICAR] | Q2 [VERIFICAR] | A2 [VERIFICAR] | Artigo Experimental / Industrial (Primário) | `10.3390/electronics14153008` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q2`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF e devem ser verificados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P31 | LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services | **RQ1** (Contexto e Definições) | Respondida Plenamente | **T** (1.0) | Seção 1 (p. 2); Seção 3, Figuras 1–4, Algoritmo 1 (pp. 4–9); Seção 4.4 (p. 12) | **(a) Definição de autonomia:** Implementa um ciclo operacional fechado *"sense–analyze–diagnose–respond"* (Seção 3.1, p. 5) com agentes distribuídos que executam monitoramento contínuo, correlação multimodal, geração de alertas diretos/postergados, agregação de causa raiz, recomendações acionáveis para operadores de O&M e suporte a autocura (*Automated Self-Healing*, Figura 1, p. 5). **(b) Características centrais:** Hierarquia de 4 agentes especializados comunicando-se assincronamente via *Kafka*, consciência de contexto (topologia de serviços, cadeias de chamadas, períodos de pico e *deployments* recentes, Figura 4, p. 9) e integração de LLMs. **(c) Modelo decisório:** Combina *parsing* semântico na borda (`BERT`), correlação em *streaming* (`PyFlink` com DTW e limiares adaptativos), detecção híbrida (*LSTM-Transformer*, *Isolation Forest*, *Z-score*), alocação de tarefas por leilão (*auction-based task allocation*) e inferência causal/explicável via `gpt-4o-mini` (pp. 7–9, 12). |
| P31 | LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seção 3, Figuras 1–4, Algoritmo 1 (pp. 4–10); Seção 4.4 (p. 12) | **(a) Tipo de arquitetura:** Sistema multiagente hierárquico *cloud-native* conteinerizado em *Kubernetes* com 4 agentes: *Performance Data Collection Agent* e *Log Processing Agent* (camada inferior), *Real-Time Analysis Agent* (camada de *streaming*) e *Anomaly Detection Agent* (camada coordenadora/decisória). **(b) Ferramentas/frameworks:** Mensageria *Apache Kafka v3.2*; coleta de *logs* em Python 3.12.9 com *Fluentd*, *Filebeat*, compressão `gzip`/`lz4` e HuggingFace `transformers` (`BERT`); coleta de métricas em Go com *OpenTelemetry SDK*, `psutil` e *Prometheus*; processamento em *stream* via *Apache Flink* / *PyFlink* (*exactly-once*); decisão com *LSTM-Transformer*, *Isolation Forest*, *Z-score* e `gpt-4o-mini` (além de menção a `LLaMA`, `GPT-4o` e `DeepSeek-v3`); armazenamento *hot–cold* em *Elasticsearch* e *MinIO* (p. 12). **(c) Capacidades avançadas:** Escalonamento dinâmico de carga por leilão (*auction-based task allocation*), *checkpointing* com *offsets*, *prompts* JSON estruturados com injeção de topologia e histórico de *deployments* (Figuras 2–4). |
| P31 | LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services | **RQ3** (Benefícios e Evidências) | Respondida Plenamente | **T** (1.0) | Seções 4 e 5, Tabelas 1–4, Figuras 5–6 (pp. 10–16) | **(a) Benefícios qualitativos:** Detecção de anomalias compostas e falhas em cascata inter-serviços, fusão semântica entre *logs* e métricas e geração de relatórios explicáveis de RCA e recomendações de manutenção (pp. 8–9, 16). **(b) Benefícios quantitativos:** Avaliado em *cluster* `H800` por 72h sobre dados de produção da **State Grid Corporation of China (SGCC)** (1.289 serviços, 28,88 milhões de invocações, 1.674 anomalias em 8 tipos de falha balanceadas com 10.000 normais, Tabelas 1–2, p. 10). Supera 7 *baselines* (*PCA*, *LogCluster*, *IM*, *LogBERT*, *DeepLog*, *LogGPT*, *LogAnomaly*, Tabela 3, p. 13) nas 4 plataformas: *Customer Service* (`P = 92.16%`, `R = 85.63%`, `F1 = 88.78%`), *Grid Resource* (`F1 = 86.34%`), *Financial Mgmt* (`F1 = 84.58%`) e *Project Mgmt* (`F1 = 87.48%`). Mede a latência média de inferência (`L = 3156 ms` no LEMAD vs. `1782 ms` no *LogGPT* e `856 ms` no *LogBERT*). Na ablação (Tabela 4, p. 15), o F1 evolui de `75.26%` (*BERT only*) para `80.44%` (`+agents`), `80.45%` (`+LLM`) e `84.58%` (sistema completo). **(c) Nível de evidência:** Implantação e validação experimental em escala industrial na SGCC. |
| P31 | LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services | **RQ4** (Desafios e Ética) | Parcialmente Respondida | **P** (0.5) | Seção 3.3 (p. 7); Seção 4.4 (p. 12); Seção 5.1, Tabela 3 (pp. 13–14); Seção 6 (p. 16) | **(a) Desafios técnicos:** Analisa criticamente o *trade-off* entre acurácia/explicabilidade e latência de inferência: o *overhead* de escalonamento multiagente e inferência LLM eleva a latência para `3156 ms` (Tabela 3), inviabilizando o uso em sistemas de controle em tempo real que exigem respostas abaixo de 3 segundos (*sub-3-s responses*, Seção 6, p. 16). Aborda também o desbalanceamento severo de falhas em produção (taxa de erro entre 0,23% e 1,57%, Tabela 1). **(b) Desafios éticos/governança:** Cita a restrição a decisões opacas em infraestruturas críticas reguladas de energia (p. 2), sem discutir ética ou *accountability* jurídica. **(c) Mecanismos de governança:** Tolerância a falhas com *checkpointing* e semântica *exactly-once* no *Flink*, retenção auditável *hot–cold* (*Elasticsearch*/*MinIO*) e relatórios JSON estruturados com evidências de suporte e *confidence score* (Figuras 3–4, pp. 8–9, 12). |
| P31 | LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção 5.1 (p. 14); Seção 6 (*Discussion*, p. 16) | Delimita quatro direções futuras claras (pp. 14, 16): (1) aplicação de técnicas de compressão de modelos (como destilação de conhecimento — *knowledge distillation*), inferência aproximada e implantação na borda (*edge deployment*) para mitigar a latência de `3156 ms` sem perda de acurácia; (2) incorporação de aprendizado *online* (*online learning*) para adaptação contínua à evolução dinâmica dos serviços; (3) validação cruzada do framework em outros domínios críticos como finanças e transporte; e (4) aprimoramento da interação humano-IA (*human–AI interaction*) via interfaces conversacionais em linguagem natural e *visual analytics*. |
| **P31** | **SCORE_RQ Total** | — | **4.5 / 5.0** | — | — | Atende plenamente RQ1 (1.0), RQ2 (1.0), RQ3 (1.0) e RQ5 (1.0), e parcialmente RQ4 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P31 | Artigo Experimental / Industrial (Primário) | Y (1.0) | P (0.5) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** Explicita com clareza o desafio de monitorar mais de 10.000 instâncias de microsserviços que geram terabytes diários de *logs* e métricas na plataforma em nuvem da *State Grid Corporation of China* (p. 2) e propõe o sistema multiagente hierárquico LEMAD para unir a precisão numérica de métricas, a semântica de *logs* via LLMs e a escalabilidade distribuída de MAS (Seções 1–3, pp. 1–5).
- **QA2 — Metodologia Replicável (P = 0.5):** Descreve minuciosamente a infraestrutura de engenharia e *deploy* (*Kubernetes*, *Apache Kafka v3.2*, *Fluentd*, *Filebeat*, *OpenTelemetry SDK*, *PyFlink*, *Prometheus*, *Elasticsearch*, *MinIO*, cluster GPU `H800`, `BERT` e `gpt-4o-mini`, Seção 4.4, p. 12), o algoritmo de ponta a ponta (Algoritmo 1) e os *prompts* JSON de cada agente (Figuras 2–4). Recebe pontuação parcial porque o *dataset* de produção da SGCC e o código não são públicos (p. 16) e certos mecanismos internos (como a formulação matemática do algoritmo de leilão para balanceamento de carga citado na p. 12 e os pesos de fusão entre *LSTM-Transformer*, *Isolation Forest* e *Z-score*) não são detalhados algebricamente.
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Forte validação empírica sobre 28,88 milhões de invocações reais de 1.289 serviços distribuídos em 4 plataformas de negócios da SGCC (Tabelas 1 e 2), comparando o LEMAD contra 7 métodos *baseline* (*PCA*, *LogCluster*, *IM*, *LogBERT*, *DeepLog*, *LogGPT* e *LogAnomaly*, Tabela 3), incluindo medição direta de latência de inferência em milissegundos e estudo de ablação avaliando isoladamente e em conjunto o efeito dos agentes e do módulo LLM (Tabela 4, p. 15). *(Nota editorial menor: o Abstract menciona "five baseline methods", mas o experimento na Seção 4.2 e Tabela 3 avalia sete baselines).*
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões estão rigorosamente alinhadas aos resultados empíricos e destacam-se pela discussão honesta da limitação de latência (`3156 ms`, Seções 5.1 e 6, pp. 14, 16), reconhecendo explicitamente que a solução não atende sistemas de controle em tempo real estrito (< 3s), sendo voltada a diagnóstico e RCA em escala de minutos.

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
O artigo apresenta o **LEMAD**, uma arquitetura multiagente hierárquica *cloud-native* (*Kubernetes* + *Apache Kafka* + *PyFlink*) integrada a modelos de linguagem (`BERT` na borda para *parsing* de *logs* e `gpt-4o-mini` na camada decisória para RCA e explicação) implantada na infraestrutura da *State Grid Corporation of China* (1.289 serviços, 28,88 milhões de invocações). O sistema supera sete *baselines* (incluindo *LogGPT* e *LogBERT*) nas quatro plataformas avaliadas (alcançando até `88.78%` de F1-score e `92.16%` de precisão), além de documentar quantitativamente o *trade-off* de latência (`3156 ms`) inerente à coordenação multiagente com LLMs. Apresenta excelente aderência às questões da RSL (`SCORE_RQ = 4.5/5.0`) e alta qualidade metodológica (`SCORE_QA = 3.5/4.0`).

### Recomendação
**INCLUIR** — Estudo primário de alto valor prático e industrial para a RSL (`SCORE_RQ = 4.5/5.0`, `SCORE_QA = 3.5/4.0`, Banda Alta), fornecendo uma arquitetura de referência completa para *Agentic AI* em produção (*Kubernetes*, *Kafka*, *OpenTelemetry*, *PyFlink*, *Prometheus*, *Elasticsearch*/*MinIO*) e evidências quantitativas reais sobre o balanço entre ganho de F1-score (+10% a +12%) e custo de latência (`3156 ms`).

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q2` para *Electronics* (MDPI) no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
