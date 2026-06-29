# Avaliação RSL — Estudo P30

**Artigo:** _Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports_ — H. Li, Y. Wang (National University of Defense Technology, China)
**Arquivo:** P30-A2-BDCC-10-00060-v2.pdf (17 páginas)

> ⚠️ **Alerta de escopo:** estudo **primário empírico**, porém **NÃO-agêntico** — é um pipeline ML/NLP (classificação TF-IDF + localização por similaridade + geração de sugestão por LLM com padrões). Não há autonomia, planejamento, loop de agente nem uso de ferramentas no sentido agêntico. Domínio = **triagem/depuração de bugs de motores de inferência LLM** (vLLM, TensorRT-LLM), não Resposta a Incidentes operacional. Determinante para a recomendação.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                       | Ano  | Cit.                                                        | SJR                               | Qualis                                          | Tipo                                                                                    | DOI                  |
| --- | ----------------------------------------------------- | ---- | ----------------------------------------------------------- | --------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------- |
| P30 | Big Data and Cognitive Computing (MDPI) (Vol. 10, 60) | 2026 | [VERIFICAR] (base indexadora — provável 0, pub. 13/02/2026) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Artigo de pesquisa empírico (estudo de viabilidade/exploratório); pipeline ML/NLP + LLM | 10.3390/bdcc10020060 |

_Evidências: cabeçalho p.1 (DOI; recebido 12/01/2026, aceito 12/02/2026, publicado 13/02/2026); "Big Data Cogn. Comput. 2026, 10, 60"; MDPI, CC-BY. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                      | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)        | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | ------------------------------------------- | ---------------------------- | --------------------------- | ------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P30 | Static RCA + Repair (LLM inference engines) | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §3, §4 (p.4-10)               | **Sem conteúdo agêntico**: nenhuma definição de autonomia, planejamento, memória, uso de ferramentas ou modelo decisório de agente. O LLM atua como gerador passivo de sugestões, restrito por padrões — não há agente.                                                                                                                                                                                                                                        |
| P30 | "                                           | RQ2 Engineering Architecture | Parcialmente Respondida     | **P**         | §3-§4 (p.4-10)                | Arquitetura **modular de 3 estágios** (classificação → localização de módulo → geração de reparo) e stack explícito (TF-IDF, Logistic Regression, LSA, similaridade textual, ChatGPT-5.2, Qwen3-235B) (a/b). Padrões root-cause→repair como priors estruturados (c). Porém **não é arquitetura agêntica** (sem orquestração de agentes, guardrails, observabilidade ou memória).                                                                               |
| P30 | "                                           | RQ3 Evidence Benefits        | Respondida Plenamente       | **T**         | §5.2-5.5, Tabs. 3-6 (p.11-15) | Quantitativo: RCA accuracy 68,8% / Macro-F1 0,421; localização Top-1 70,5% / Top-2 84,1%; generalização cross-engine (TensorRT-LLM); avaliação humana Likert (correctness 3,7/3,5; usefulness 3,6/3,4; clarity 4,3/4,1) + Fleiss' κ (b); benefícios qualitativos (leve, sem execução, model-agnostic, modular) (a); evidência empírica — dataset real, 5-fold CV, baselines, human eval (c). Ressalva: desempenho **modesto** e auto-declarado "exploratório". |
| P30 | "                                           | RQ4 Challenges & Ethics      | Parcialmente Respondida     | **P**         | §6 "Discussion" (p.15-16)     | Desafios técnicos/limitações bem discutidos — dependência da completude textual, localização grosseira (nível de módulo), escala/desbalanceamento de dados, efeito cascata de erros (a). Porém **sem discussão ética/governança/accountability** (b, c ausentes).                                                                                                                                                                                              |
| P30 | "                                           | RQ5 Research Gaps            | Respondida Plenamente       | **T**         | §6 (p.16), §7 (p.16)          | Lacunas e direções explícitas: incorporar artefatos estruturados (commits, diffs, stack traces), granularidade fina (função/bloco de código), expansão de dataset/engines.                                                                                                                                                                                                                                                                                     |
|     |                                             | **SCORE_RQ**                 |                             | **3.0 / 5.0** |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                      | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | --------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P30 | Artigo de pesquisa empírico (estudo de viabilidade) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (bugs de motores de inferência difíceis de diagnosticar; depuração baseada em execução impraticável; lacuna de dataset) e solução (RCA estática issue-based + sugestão de reparo) explícitos, com 3 desafios e RQs.
- **QA2 = Y** — metodologia detalhada: dataset (176 vLLM + 100 TensorRT-LLM, anotado), TF-IDF+LogReg/LSA, similaridade textual, 5-fold CV, hardware (Xeon Gold 6430), LLMs usados, protocolo de avaliação humana (50 issues, 5 avaliadores, Likert, Fleiss' κ); **dataset e código a serem liberados**. Replicável.
- **QA3 = Y** — validação empírica genuína: dataset real, baselines (Linear SVM, Random Forest, Most-Frequent, Random Guess), validação cruzada, estudo cross-engine e avaliação humana com confiabilidade inter-avaliadores. (O desempenho modesto é matéria de resultado, não da existência de base empírica.)
- **QA4 = Y** — conclusões coerentes e **honestamente modestas** (auto-declarado "feasibility/exploratory"); limitações explicitamente discutidas (dependência textual, localização grosseira, escala de dados, cascata de erros).

## Parecer final do revisor

**Síntese.** Estudo primário **metodologicamente sólido e honesto** (QA Alta) que propõe um pipeline estático, baseado em relatórios de issues, para **RCA + sugestão de reparo de bugs de motores de inferência LLM** (vLLM, TensorRT-LLM), usando classificação TF-IDF, localização por similaridade e um LLM (constrangido por padrões) na geração de sugestões. Contudo, o ajuste ao escopo da RSL é **fraco em dois eixos**: (i) **não é Agentic AI** — não há agente, autonomia, planejamento ou uso de ferramentas (**RQ1 = N**); o LLM é um gerador passivo; e (ii) o **domínio é depuração de software** de infraestrutura de serving, não **Resposta a Incidentes** operacional. A conexão com IR é apenas temática (RCA/diagnóstico), não de paradigma agêntico nem de domínio.

**Recomendação: EXCLUIR da síntese primária** (por **escopo**: não-agêntico + fora do domínio de IR), **apesar da qualidade metodológica Alta**. SCORE_RQ 3,0/5,0 e QA 4,0/4,0. No limite, poderia ser **retido como referência contextual** de RCA/reparo assistido por LLM (não-agêntico), caso o protocolo admita.

> ⚠️ **Decisão de protocolo (cabe ao condutor da RSL):** se o protocolo exigir **estudos centrados em Agentic AI** (autonomia/planejamento/uso de ferramentas), P30 deve ser **excluído** — diferentemente de P20-P22 (agênticos) ou mesmo P23 (agente-LLM de síntese), aqui não há componente agêntico algum. Trata-se de "LLM-assistido", não "LLM-agêntico".

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar. ⚠️ Publicado em 13/02/2026 — **contagem provavelmente 0**; pode **reprovar** o critério "Citações ≥ 1" se aplicado estritamente (possível **INELEGÍVEL** por esse critério).
- **SJR (quartil)** → Scimago, _Big Data and Cognitive Computing_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2026 ✓; veículo MDPI BDCC ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA** — com **atenção especial à contagem de citações** dada a publicação muito recente.
