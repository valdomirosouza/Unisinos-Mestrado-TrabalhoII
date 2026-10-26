# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P27
- **Título:** *Leveraging multi-agent framework for root cause analysis*
- **Autores:** Feng Fu; Hong Ding; Yong Qin; Jian Yu; Dechao Xu
- **Periódico/Conferência:** *Complex & Intelligent Systems* (Springer), Vol. 12, Artigo 4, pp. 1–13 (Publicado online em 6 de novembro de 2025; volume de 2026)
- **DOI:** `10.1007/s40747-025-02096-0`
- **Arquivo avaliado:** `P27-A1-s40747-025-02096-0.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental (*Original Article*), propondo o framework multiagente colaborativo **MA-RCA** (*Multi-Agent Root Cause Analysis*) e avaliando-o em plataformas *cloud-native* (benchmark *Nezha*) e infraestruturas distribuídas de medição de energia elétrica (*Power monitoring dataset*), com integração de protótipo em sistema industrial real.
- **Foco técnico:** Automação de Análise de Causa Raiz (RCA) por meio da decomposição do fluxo de diagnóstico em quatro agentes especializados (*RCA Agent*, *Retrieval Agent*, *Validation Agent* e *Report Agent*) para mitigar alucinações induzidas por troca de contexto (*context-switching*) e propagação de erros em raciocínio multi-etapa.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Totalmente atendido. Propõe uma arquitetura multiagente baseada em LLMs diretamente voltada ao diagnóstico de anomalias, validação de hipóteses com ferramentas em tempo de execução e geração de relatórios de mitigação para engenheiros de confiabilidade (*SREs*).
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado em periódico revisado por pares da Springer, online em novembro de 2025 / volume de 2026).
  - *IC3 (Rigor técnico/metodológico):* Atendido (algoritmos formalizados, avaliação experimental contra 5 *baselines*, estudo de ablação, análise de sensibilidade de LLMs e *top-k* casos, e demonstração em sistema real).
- **Critérios de Exclusão (EC):** Não incide em nenhum critério de exclusão.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (exclusivamente para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P27 | Complex & Intelligent Systems | 2026 (online 2025) | [VERIFICAR] | Q1 [VERIFICAR] | A1 [VERIFICAR] | Artigo Experimental / Empírico (Primário) | `10.1007/s40747-025-02096-0` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A1`) não constam no corpo do PDF e devem ser verificados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Google Scholar / Scopus*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P27 | Leveraging multi-agent framework for root cause analysis | **RQ1** (Contexto e Definições) | Respondida Plenamente | **T** (1.0) | Seção *Introduction* (pp. 1–2); Seção *Method* (pp. 3–7); Seção *System illustration*, Figuras 3–4 (pp. 11–12) | **(a) Autonomia:** Opera como sistema multiagente autônomo de RCA integrado como *plug-in* de auxílio cognitivo (*Diagnosis Agent*, p. 11) acionado por linguagem natural por SREs, com protocolo em malha fechada que solicita reentrada ao usuário se faltarem parâmetros obrigatórios (Figura 2, pp. 4–5). **(b) Características centrais:** Decomposição por domínio em 4 agentes especializados, memória histórica híbrida (vetorial + grafo de conhecimento IEC + índice reverso) e uso de ferramentas de validação em tempo real. **(c) Modelo decisório:** Combina *pattern matching* determinístico, inversão causal (*Algorithm 1*, p. 5), validação de hipóteses guiada por ferramentas (*Algorithm 2*, p. 6) e pontuação de similaridade semântica (BERT) para síntese probabilística de causas-raiz (pp. 3–7). |
| P27 | Leveraging multi-agent framework for root cause analysis | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seção *Method*, Figuras 1–2, Algoritmos 1–2 (pp. 3–7); Seção *Evaluation*, Tabela 5 (p. 10) | **(a) Tipo de arquitetura:** Framework multiagente colaborativo e modular (*MA-RCA*, Figura 1, p. 4) orquestrado pelo *RCA Agent* coordenando *Retrieval Agent*, *Validation Agent* e *Report Agent*. **(b) Ferramentas/frameworks:** Avalia múltiplos LLMs base (`QwenMax`, `DeepSeek`, `LLAMA3.3-70B`, `Qwen-QwQ`, Tabela 5, p. 10), *embeddings* BERT, *cross-encoder reranking* com decaimento temporal, grafos de conhecimento (IEC 62053) e *Tool Box* com *Log Tools*, *Database Tools*, *Trace Tools* e *KPI Tools* via APIs para *Prometheus*, *Modbus/TCP* e PMUs a 10 Hz (pp. 4–7). **(c) Capacidades avançadas:** *Input parsing* estruturado (4 campos obrigatórios), *Root Cause Inversion* (índice invertido causa$\to$sintoma em milissegundos), deduplicação de verificações por *Locality-Sensitive Hashing* (LSH), escalonamento prioritário e *pool* de cache distribuído com *Time-to-Live* (TTL de 30s a 1h, p. 6). |
| P27 | Leveraging multi-agent framework for root cause analysis | **RQ3** (Benefícios e Evidências) | Respondida Plenamente | **T** (1.0) | Seção *Evaluation*, Tabelas 1–6 (pp. 7–11); Seção *System illustration*, Figuras 3–4 (pp. 11–12) | **(a) Benefícios qualitativos:** Supressão de alucinações por troca de contexto, expansão do espaço de hipóteses com indicadores latentes e geração automatizada de relatórios PDF auditáveis (normas IEC/NERC, p. 7). **(b) Benefícios quantitativos:** No dataset *cloud-native* **Nezha** (101 falhas em *OnlineBoutique* e *TrainTicket*, Tabela 1), obtém `Acc = 0.958`, `Pre = 0.960`, `Rec = 0.944` e `F1 = 0.952`, superando *CoT* (`F1 = 0.412`), *RAG* (`F1 = 0.704`), *RCACOPILOT* (`F1 = 0.748`), *RCAgent* (`F1 = 0.725`) e *mABC* (`F1 = 0.726`) (Tabela 3, p. 9). No dataset **Power monitoring** (211 falhas de TIC e elétricas, Tabela 2), atinge `Acc = 0.843` e `F1 = 0.828` (vs. `0.651` do *RCACOPILOT* e `0.613` do *mABC*). Ablações (Tabela 4, p. 10) mostram queda abrupta sem multiagentes (`F1 = 0.716`/`0.680`), sem *Retrieval Agent* (`F1 = 0.295`/`0.144`) e sem *Validation Agent* (`F1 = 0.681`/`0.543`). **(c) Nível de evidência:** Experimentos controlados em 2 domínios + implantação de protótipo em sistema real de medição de energia elétrica (pp. 11–12). |
| P27 | Leveraging multi-agent framework for root cause analysis | **RQ4** (Desafios e Ética) | Parcialmente Respondida | **P** (0.5) | Seção *Method* (pp. 4–7); Seção *Evaluation*, Tabela 6 (pp. 10–11); Seção *Conclusions* (p. 12) | **(a) Desafios técnicos:** Analisa alucinações por troca de contexto, propagação de erros entre etapas, degradação de desempenho por excesso de casos recuperados que introduzem ruído na janela de contexto ($N=10 \to \text{F1 } 0.820$; $N=20 \to \text{F1 } 0.800$, Tabela 6, pp. 10–11), dependência da completude do repositório histórico e latência adicional de coleta/validação (p. 12). **(b) Desafios éticos/governança:** Cita exigências de trilhas de auditoria e conformidade regulatória (IEC/NERC, p. 7), sem aprofundar questões éticas ou de *accountability*. **(c) Mecanismos de governança:** Validação obrigatória de esquema de entrada (Figura 2), verificação lógica via grafo de conhecimento físico (IEC 62053) para eliminar pseudo-associações fisicamente impossíveis (p. 6) e cadeia de evidências auditável em PDF (p. 7). |
| P27 | Leveraging multi-agent framework for root cause analysis | **RQ5** (Lacunas de Pesquisa) | Parcialmente Respondida | **P** (0.5) | Seção *Conclusions* (p. 12) | Aponta duas direções futuras concretas para sistemas multiagentes de RCA (p. 12): (1) mecanismos de recuperação adaptativa que determinem dinamicamente a quantidade ótima e a relevância de casos históricos conforme o contexto da anomalia, superando estratégias *top-k* estáticas; e (2) estratégias de execução especulativa (*speculative execution*) e pré-busca (*pre-fetching*) para a equipe de agentes, iniciando coletas de dados potenciais em paralelo para reduzir a latência do *pipeline* diagnóstico em cenários críticos em tempo. |
| **P27** | **SCORE_RQ Total** | — | **4.0 / 5.0** | — | — | Atende plenamente RQ1 (1.0), RQ2 (1.0) e RQ3 (1.0), e parcialmente RQ4 (0.5) e RQ5 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P27 | Artigo Experimental / Empírico (Primário) | Y (1.0) | P (0.5) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** Define com precisão os três desafios centrais da automação de RCA (mapeamento complexo entre anomalias e dados de *runtime*, lacuna semântica entre *logs* não estruturados e métricas estruturadas, e explosão combinatória de relações causais) e formula claramente a arquitetura multiagente MA-RCA para mitigar alucinações por troca de contexto (pp. 1–3).
- **QA2 — Metodologia Replicável (P = 0.5):** Apresenta algoritmos explícitos para o *Retrieval Agent* (Algoritmo 1, p. 5) e *Validation Agent* (Algoritmo 2, p. 6), o *prompt* de extração de entidades (Figura 2, p. 5), estatísticas detalhadas dos *datasets* (Tabelas 1 e 2) e divisão estratificada 50%/50%. Contudo, o *dataset* industrial *Power monitoring* é restrito por confidencialidade (p. 12), a adaptação dos *datasets* envolve geração sintética de fluxos de telemetria sobre dados pré-processados cujos hiperparâmetros não são integralmente detalhados (pp. 7–8), e não são reportadas métricas quantitativas de tempo/latência de execução.
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Conduz avaliação empírica abrangente em dois domínios distintos (*cloud-native* com 101 incidentes no *Nezha* e *cyber-physical* com 211 incidentes em *Power monitoring*), comparando contra 5 *baselines* representativas (*CoT*, *RAG*, *RCACOPILOT*, *RCAgent* e *mABC*, Tabela 3), além de estudo de ablação de 4 variantes (Tabela 4), avaliação de 4 LLMs base (Tabela 5), análise de sensibilidade ao número de casos históricos recuperados (Tabela 6) e demonstração prática de integração em sistema industrial real (Figuras 3–4, pp. 11–12).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões derivam diretamente dos resultados experimentais e de ablação, e os autores discutem explicitamente as limitações do método (forte dependência da qualidade do repositório histórico e sobrecarga de latência introduzida pelas etapas de coleta e validação, p. 12).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
O artigo apresenta o **MA-RCA**, uma arquitetura multiagente colaborativa para Análise de Causa Raiz (RCA) que decompõe o fluxo diagnóstico em quatro agentes especializados (*RCA*, *Retrieval*, *Validation* e *Report Agent*), combinando inversão causal assistida por grafos de conhecimento com validação dinâmica de hipóteses via ferramentas (*Prometheus*, *Modbus/TCP*, cache distribuído com TTL e agrupamento LSH). Os experimentos nos conjuntos *Nezha* (*cloud-native*, `F1 = 0.952`) e *Power monitoring* (*cyber-physical*, `F1 = 0.828`) demonstram ganhos expressivos sobre *RCACOPILOT*, *RCAgent* e *mABC*, comprovando que a especialização de domínio e a verificação ativa suprimem alucinações e propagação de erros. Trata-se de um estudo de alta aderência às RQs da RSL (`SCORE_RQ = 4.0/5.0`) e elevado rigor empírico (`SCORE_QA = 3.5/4.0`).

### Recomendação
**INCLUIR** — Estudo primário altamente relevante para a RSL (`SCORE_RQ = 4.0/5.0`, `SCORE_QA = 3.5/4.0`, Banda Alta), oferecendo contribuições arquiteturais concretas para engenharia de *Agentic AI Copilots* em resposta a incidentes (como deduplicação de chamadas de ferramentas via LSH, cache de telemetria com TTL diferenciado, inversão causa-sintoma e validação física/causal contra alucinações).

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Google Scholar* ou *Scopus* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *Complex & Intelligent Systems* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A1` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
