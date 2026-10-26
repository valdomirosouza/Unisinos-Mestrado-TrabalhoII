# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P30
- **Título:** *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports*
- **Autores:** Hongwei Li; Yongjun Wang
- **Periódico/Conferência:** *Big Data and Cognitive Computing* (MDPI), Vol. 10, Artigo 60, pp. 1–17 (Publicado em 13 de fevereiro de 2026)
- **DOI:** `10.3390/bdcc10020060`
- **Arquivo avaliado:** `P30-A2-BDCC-10-00060-v2.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental (*Article* — estudo exploratório e de viabilidade), propondo um *pipeline* estático baseado em texto para classificação de causa raiz, localização de módulo e geração de sugestões de reparo para defeitos de software em motores de inferência de LLMs (*vLLM* e *TensorRT-LLM*) a partir de relatórios de *issues* do GitHub.
- **Foco técnico:** Engenharia de software voltada à confiabilidade e depuração *offline* de motores de inferência de LLMs (*LLM inference engines*), combinando aprendizado de máquina estatístico clássico (vetorização TF-IDF + Regressão Logística Multinomial e similaridade de cosseno) com geração condicional de texto por LLM (`ChatGPT-5.2` e `Qwen3-235B-A22B`) no último estágio.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Atendido apenas tangencialmente. Embora aborde Análise de Causa Raiz (RCA) e sugestão de reparo com auxílio de LLM, **não** implementa uma arquitetura de *Agentic AI* (não há agentes autônomos, planejamento dinâmico, memória agêntica ou uso de ferramentas pelo LLM) e o objeto de análise é a triagem estática *offline* de *bug reports* do GitHub de motores de inferência (*vLLM*, *TensorRT-LLM*), e não resposta a incidentes operacionais em tempo de execução.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *Big Data and Cognitive Computing*, 2026).
  - *IC3 (Rigor técnico/metodológico):* Atendido (algoritmos formalizados, *dataset* público anotado com 276 *issues*, validação cruzada, teste *cross-engine* e avaliação humana com Fleiss' $\kappa$).
- **Critérios de Exclusão (EC):** Limiar de exclusão por escopo arquitetural (ausência de *Agentic AI* — o LLM atua exclusivamente como gerador condicional de texto ao final de um classificador TF-IDF + Regressão Logística, conforme declarado na Seção 3.4, pp. 8–9).
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para métricas bibliométricas externas; prossegue-se à avaliação completa das RQs e QA conforme protocolo para subsidiar a decisão final do revisor).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P30 | Big Data and Cognitive Computing | 2026 | [VERIFICAR] | Q1 [VERIFICAR] | A2 [VERIFICAR] | Artigo Experimental / Empírico (Primário) | `10.3390/bdcc10020060` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF e devem ser verificados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P30 | Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports | **RQ1** (Contexto e Definições) | Não tem conteúdo suficiente | **N** (0.0) | Seção 3 (pp. 4–5); Seção 3.4 (pp. 8–9) | O estudo **não** aborda *Agentic AI*, autonomia agêntica, planejamento, memória ou uso autônomo de ferramentas. Os próprios autores ressaltam na Seção 3.4 (pp. 8–9): *"Finally, we emphasize that the LLM is used solely as a conditional text generator in the final stage of the pipeline. All diagnostic reasoning, such as root cause classification and module localization, is performed independently by deterministic or statistical components"*. |
| P30 | Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports | **RQ2** (Arquitetura de Engenharia) | Parcialmente Respondida | **P** (0.5) | Seções 3 e 4, Figura 1, Tabela 1, Algoritmos 1–4 (pp. 4–10) | Descreve um *pipeline* estático modular em 3 estágios sem execução de código (*Static-first and execution-free*, Figura 1, p. 4): (1) classificação supervisionada de causa raiz em 4 classes (`model_execution`, `runtime_state`, `resource_concurrency`, `io_semantic`, Tabela 1) usando TF-IDF + Regressão Logística Multinomial (`scikit-learn`, Algoritmo 2); (2) localização de módulo via similaridade de cosseno sobre perfis TF-IDF de *issues* históricas (Algoritmo 3); e (3) geração de sugestão de reparo via API (`ChatGPT-5.2` e `Qwen3-235B-A22B`) ancorada em padrões de reparo (*root cause–repair patterns*) e *template* de *prompt* estruturado (Algoritmo 4, p. 8). Contudo, não possui arquitetura agêntica, orquestração de agentes ou observabilidade em produção. |
| P30 | Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports | **RQ3** (Benefícios e Evidências) | Parcialmente Respondida | **P** (0.5) | Seção 5, Tabelas 2–6, Figuras 2–3 (pp. 10–15) | Avalia o método em 176 *issues* fechadas do **vLLM** e 100 do **TensorRT-LLM** (Seção 5.1, Tabela 2, p. 11): (i) na classificação de causa raiz (5-*fold* CV no *vLLM*, Tabela 3), TF-IDF + Regressão Logística obtém `Accuracy = 0.688` e `Macro-F1 = 0.421` (vs. `0.500` / `0.266` do Linear SVM e `0.500` / `0.265` do Random Forest); (ii) na localização de módulo (Tabela 4, Figura 3), atinge `Top-1 = 0.705` e `Top-2 = 0.841` em dezenas de milissegundos (~0,8 s para 140 *issues*); (iii) na generalização *cross-engine* (*vLLM* $\to$ *TensorRT-LLM*, Tabela 5), obtém `Accuracy = 0.640` e `Macro-F1 = 0.405`; e (iv) na avaliação humana cega de 50 *issues* por 5 pesquisadores (escala Likert 1–5, Fleiss' $\kappa \in [0.44, 0.61]$, Tabela 6), `ChatGPT-5.2` atinge `Correctness = 3.7`, `Usefulness = 3.6`, `Clarity = 4.3` e `Qwen3-235B-A22B` obtém `3.5`, `3.4`, `4.1`. As evidências referem-se à depuração estática de *bugs* de software no GitHub, não à resposta a incidentes operacionais por agentes. |
| P30 | Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports | **RQ4** (Desafios e Ética) | Parcialmente Respondida | **P** (0.5) | Seção 3.4 (p. 8); Seção 5.2, Figura 2 (pp. 11–12); Seção 5.5 (p. 15); Seção 6 (p. 15) | Identifica desafios técnicos relevantes: (1) efeito cascata (*cascading effect*) onde erros nas etapas estatísticas anteriores (causa raiz/módulo) induzem sugestões de reparo genéricas ou irrelevantes no LLM (p. 15); (2) dependência da qualidade e completude textual dos relatos de *bugs* dos usuários; (3) desbalanceamento severo de classes reais (a categoria `runtime_state`, com apenas 3,4% / 6 casos no *vLLM*, teve zero acertos na matriz de confusão da Figura 2, p. 12); e (4) granularidade grosseira restrita a módulos. Como *guardrail* técnico contra alucinações, restringe o *prompt* do LLM com os resultados intermediários e padrões de reparo abstratos (p. 8). Não discute ética ou governança agêntica. |
| P30 | Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports | **RQ5** (Lacunas de Pesquisa) | Parcialmente Respondida | **P** (0.5) | Seções 5.5, 6 e 7 (pp. 15–16) | Aponta direções futuras específicas para depuração de motores de inferência de LLMs (pp. 15–16): (1) incorporação de artefatos estruturados e semiestruturados adicionais (*commits*, *code diffs*, *stack traces* e grafos de dependência); (2) refinamento da localização do nível de módulo para função ou bloco de código, integrando com técnicas de reparo automático de programas (*Automated Program Repair* — APR) e geração de testes; e (3) ampliação do *dataset* para mais motores de inferência e expansão da amostra de avaliadores humanos. |
| **P30** | **SCORE_RQ Total** | — | **2.0 / 5.0** | — | — | Não atende RQ1 (0.0) e atende apenas parcialmente RQ2 (0.5), RQ3 (0.5), RQ4 (0.5) e RQ5 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P30 | Artigo Experimental / Empírico (Primário) | P (0.5) | Y (1.0) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (P = 0.5):** O problema da complexidade de depuração de motores de inferência de LLMs (*vLLM*, *TensorRT-LLM*) sem execução dinâmica é claramente exposto (Seções 1 e 2, pp. 1–4). Contudo, sob a rubrica da RSL (que exige explicitação do problema operacional e da **solução agêntica**), recebe pontuação parcial porque a solução proposta **não é agêntica**, consistindo em um classificador estatístico clássico (TF-IDF + Regressão Logística) seguido de geração de texto condicional em passo único.
- **QA2 — Metodologia Replicável (Y = 1.0):** Alto grau de reprodutibilidade: apresenta os quatro algoritmos do *pipeline* (Algoritmos 1–4), o *template* exato do *prompt* (Seção 3.4, p. 8), detalhes de pré-processamento e bibliotecas (`Python 3.10`, `scikit-learn`), especificações de hardware (Ubuntu 22.04, Xeon Gold 6430, 256 GB RAM, p. 11) e disponibiliza publicamente o código-fonte e o *dataset* anotado no GitHub (`https://github.com/moxi828/BDCC/tree/main`, p. 16).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Validação experimental bem conduzida sobre 276 *issues* reais (176 do *vLLM* e 100 do *TensorRT-LLM*), incluindo validação cruzada estratificada de 5 *folds*, matriz de confusão, avaliação de escalabilidade temporal, experimento de transferência *cross-engine* sem retreinamento e avaliação humana cega com 5 especialistas e coeficiente $\kappa$ de Fleiss sobre 50 casos utilizando dois LLMs distintos (`ChatGPT-5.2` e `Qwen3-235B-A22B`).
- **QA4 — Conclusões Coerentes (Y = 1.0):** Os autores interpretam seus resultados com rigor e parcimônia científica, reconhecendo explicitamente na Seção 7 (p. 16) que o desempenho de classificação (`Macro-F1 = 0.421`) é modesto devido à escala reduzida e ao forte desbalanceamento dos dados, enquadrando o estudo honestamente como exploratório e de viabilidade.

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
O artigo investiga um problema relevante de infraestrutura de IA — os defeitos de software em motores de inferência de LLMs (*vLLM* e *TensorRT-LLM*, como erros de concorrência/OOM CUDA, estado de *KV cache* e *kernels* de atenção) —, propondo um *pipeline* estático que classifica a causa raiz e localiza o módulo afetado via TF-IDF + Regressão Logística e utiliza um LLM (`ChatGPT-5.2` / `Qwen3-235B-A22B`) apenas no estágio final para redigir sugestões de reparo baseadas em padrões. Apesar da boa qualidade metodológica do experimento (`SCORE_QA = 3.5/4.0`), o trabalho não apresenta uma arquitetura de *Agentic AI* e foca em triagem estática de *bug reports* de desenvolvimento no GitHub, resultando em baixa aderência às questões de pesquisa da RSL (`SCORE_RQ = 2.0/5.0`).

### Recomendação
**EXCLUIR** (ou mencionar apenas tangencialmente na fundamentação de confiabilidade de infraestrutura de *serving* de LLMs) — Embora metodologicamente bem executado (`SCORE_QA = 3.5/4.0`), o estudo obtém o menor escore de aderência às RQs até o momento (`SCORE_RQ = 2.0/5.0`, com `RQ1 = N`) porque **não projeta nem avalia um agente ou sistema multiagente**, declarando explicitamente que todo o raciocínio diagnóstico (RCA e localização) é feito por modelos lineares TF-IDF e que o LLM atua exclusivamente como gerador condicional de texto em passo único sobre relatórios de *bugs* de código. Caso os autores da RSL desejem mantê-lo apenas como referência complementar sobre falhas internas da infraestrutura de inferência que hospeda LLMs (`resource_concurrency`, `runtime_state`, `model_execution`), sua inclusão deve ser estritamente circunscrita a esse ponto.

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Google Scholar* ou *Scopus* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *Big Data and Cognitive Computing* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
