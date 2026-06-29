# Avaliação RSL — Estudo P38

**Artigo:** _Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation_ — I. Radeva, I. Popchev, L. Doukovska, M. Dimitrova (Bulgarian Academy of Sciences + Trakia University, Bulgária)
**Arquivo:** P38-A2-electronics-14-04883-v2.pdf (35 páginas)

> ⚠️ **Alerta de domínio (decisivo):** estudo **agêntico de alta qualidade**, porém **inteiramente fora do escopo de Resposta a Incidentes** — o domínio é **perguntas-e-respostas factuais de AGRICULTURA** (FAO Climate-Smart Agriculture Sourcebook). Verificação por busca: **0 menções** a incident response/cibersegurança/SOC/threat detection; 12 menções a agricultura/clima/FAO.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                    | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                                             | DOI                         |
| --- | ---------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------- |
| P38 | Electronics (MDPI) (Vol. 14, 4883) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Artigo de pesquisa empírico (avaliação comparativa multi-agente vs RAG; **domínio agricultura**) | 10.3390/electronics14244883 |

_Evidências: cabeçalho p.1 (DOI; recebido 15/11/2025, publicado 11/12/2025); "Electronics 2025, 14, 4883"; MDPI, CC-BY. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                               | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)      | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                   |
| --- | ------------------------------------ | ---------------------------- | ----------------------- | ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P38 | Multi-Agent vs RAG (Q&A agricultura) | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §1 (p.1-2)                  | Define **estratégias de coordenação multi-agente** (colaborativa/peer-to-peer, sequencial/pipeline, competitiva/seleção, hierárquica/manager-worker) e mecanismos de decisão (consenso vs seleção) (b/c parciais). Porém **sem taxonomia de níveis de autonomia, memória, uso de ferramentas (além de RAG) ou supervisão humana** (a ausente).                       |
| P38 | "                                    | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §1.2, §3 (p.3-...)          | Eixo central do estudo: **4 arquiteturas de coordenação** + RAG single-agent (a); stack — Mistral 7B, Llama 3.1 8B, Granite 3.2 8B, RAG, shared context retrieval, Two-Phase Consensus (b); capacidades/análise de orquestração — custo de coordenação, retrieval compartilhado vs independente, síntese por consenso (c). (Sem guardrails/observabilidade.)         |
| P38 | "                                    | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §4-§5, Figs. 4-6 (p.~13-26) | Evidência **quantitativa rigorosa** (CPS/T-CPS, 9 métricas, 3100 avaliações, effect sizes, p<0,001) (b/c fortes), **porém o resultado é NEGATIVO** (todas as 28 configs multi-agente **degradam** −4,4% a −35,3% vs RAG single-agent) e **fora de IR** (Q&A de agricultura). Não há benefícios de IR (resposta/decisão/carga operacional) — apenas qualidade de Q&A. |
| P38 | "                                    | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §5.1-5.4 (p.24-26)          | Desafios técnicos fortes e bem analisados — **custo de coordenação** (fator dominante), fragmentação de retrieval, perda de informação no consenso, "stable mediocrity", dependência de tamanho de modelo, propagação de erro (a). Porém **sem ética/governança/accountability** (b, c ausentes).                                                                    |
| P38 | "                                    | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §5.3, §6 (p.26-27)          | Direções explícitas: modelos maiores, equipes de agentes heterogêneas, prompting por papel, mecanismos de consenso avançados (weighted voting, argumentação estruturada, agregação aprendida), outros domínios; seção de limitações detalhada.                                                                                                                       |
|     |                                      | **SCORE_RQ**                 |                         | **3.5 / 5.0** |                             |                                                                                                                                                                                                                                                                                                                                                                      |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                               | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------------------ | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P38 | Artigo de pesquisa empírico (comparação multi-agente vs RAG) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — 4 objetivos de pesquisa + 3 perguntas de deployment explícitos; problema (a coordenação multi-agente compensa o overhead vs RAG?) claro (§1.1).
- **QA2 = Y** — metodologia muito detalhada e replicável: 3 modelos versionados, 4 estratégias, 31 configurações, 4 fases, **base pública (FAO)**, métricas CPS/T-CPS (9 sub-métricas) definidas, hardware especificado, métodos estatísticos (effect sizes, p-values).
- **QA3 = Y** — validação empírica **forte**: 3100 avaliações, 31 configs, análise estatística (effect sizes, p<0,001), decomposição por fases (isola overhead vs fragmentação de retrieval).
- **QA4 = Y** — conclusões coerentes com os resultados; **seção de limitações ampla** (§5.3: domínio único, tier de modelo, agentes homogêneos, prompts gerados por IA, hardware) + comparação com a literatura.

## Parecer final do revisor

**Síntese.** Estudo empírico **agêntico, metodologicamente excelente** (QA 4,0; estatística rigorosa), cujo resultado central é **cautelar**: para modelos open-source 7-8B em **Q&A factual**, **a coordenação multi-agente degrada o desempenho** vs RAG single-agent (custo de coordenação dominante; seleção > consenso). Entretanto, o **domínio é agricultura** — **sem qualquer conteúdo de Resposta a Incidentes/cibersegurança**. É, portanto, **agêntico mas fora do escopo da RSL** (o espelho de P34, que é IR mas não-agêntico).

**Recomendação: EXCLUIR da síntese primária — por domínio (fora de IR/cibersegurança)**, **apesar da alta qualidade**. SCORE_RQ 3,5/5,0 e QA 4,0/4,0. Recomendo fortemente **retê-lo como referência metodológica/comparativa na discussão** da RSL: o achado "multi-agente vs RAG single-agent / custo de coordenação / seleção > consenso" é **diretamente útil para decisões de arquitetura de um copilot de IR** (quando usar multi-agente vs single-agent RAG, especialmente em deployment com restrição de recursos) — informa RQ2/RQ4 de forma transferível.

> ⚠️ **Decisão de protocolo:** se o protocolo restringir o corpus a estudos **no domínio de IR/cibersegurança**, P38 deve ser **excluído** (como caso primário) e, no máximo, citado como evidência metodológica externa. Diferente de P24 (survey **de definições** agênticas, retido como fundacional), P38 é um achado empírico **específico de outro domínio** (agricultura), com menor transferibilidade conceitual — daí a exclusão do corpus.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _Electronics_ (MDPI) (insumo: Q2).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios de elegibilidade verificáveis no PDF atendidos (Ano 2025 ✓; veículo MDPI Electronics ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**. _Observação:_ a EXCLUSÃO recomendada é por **relevância de domínio**, não por inelegibilidade formal nem por qualidade (que é Alta).
