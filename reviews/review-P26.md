# Avaliação RSL — Estudo P26

**Artigo:** _Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications_ — Z. Li, J. Yu, Z. Huang, Y. Huang
**Arquivo:** P26-A1-Surveying_Root_Cause_Analysis_Techniques...pdf (18 páginas)

> ⚠️ **Alerta de tipo de estudo:** rotulado explicitamente **"(Survey Paper)"** na p.1 — estudo **secundário**. Segue as diretrizes de Kitchenham et al. (a mesma metodologia da própria RSL). Determinante para QA3 e para a recomendação. **Além disso, NÃO é um estudo centrado em Agentic AI** — o tema é RCA em geral (estatístico/grafo/DL/LLM); agentes aparecem apenas tangencialmente (§VII).

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                          | Ano       | Cit.                          | SJR                               | Qualis                                          | Tipo                                                             | DOI                      |
| --- | -------------------------------------------------------- | --------- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------- | ------------------------ |
| P26 | IEEE Transactions on Services Computing (Vol. 19, No. 1) | 2025/2026 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | **Survey / Revisão (diretrizes Kitchenham)** — estudo secundário | 10.1109/TSC.2025.3631913 |

_Evidências: cabeçalho p.1 ("(Survey Paper)"; DOI; recebido 28/04/2024, aceito 08/11/2025, publicado 13/11/2025, versão atual 05/02/2026); "IEEE Transactions on Services Computing, Vol. 19, No. 1, Jan/Fev 2026"; material suplementar disponível. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                     | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)                           | Parecer do revisor                                                                                                                                                                                                                                                                                      |
| --- | -------------------------- | ---------------------------- | --------------------------- | ------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P26 | Survey RCA (multi-service) | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §VII (p.8)                                       | O survey **não define** autonomia, planejamento, memória, uso de ferramentas nem modelo decisório agêntico. "Agente" aparece apenas como técnica pontual (agente LLM ReAct [65], OpenRCA [66]) — menção tangencial, sem conteúdo definicional sobre Agentic AI.                                         |
| P26 | "                          | RQ2 Engineering Architecture | Parcialmente Respondida     | **P**         | §VII (hybrid/LLM), §VIII-X, §XI (tools/datasets) | Há inventário de **técnicas/ferramentas/datasets** de RCA e métodos híbridos/LLM (b/c parciais), porém **não é arquitetura agêntica** (sem orquestração, guardrails, observabilidade, memória de agente). Taxonomia de métodos de RCA, não de Agentic AI.                                               |
| P26 | "                          | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §IX (métricas), §VII (p.8)                       | Sintetiza métricas de avaliação do campo (accuracy, precision, recall, Top-k) e alguns números reportados de terceiros (ex.: melhor agente LLM resolve só 11,3% no OpenRCA; 40K incidentes Microsoft) (a/b parciais); **sem evidência empírica própria** e não específica de Agentic AI/IR (c ausente). |
| P26 | "                          | RQ4 Challenges & Ethics      | Parcialmente Respondida     | **P**         | §XII "Open Issues" (p.15-16)                     | Desafios técnicos fortes — limitações algorítmicas, alucinações e contexto limitado de LLMs, escassez de datasets, generalização cross-domain, interpretabilidade (a). Porém **sem discussão ética/governança/accountability** (b, c ausentes).                                                         |
| P26 | "                          | RQ5 Research Gaps            | Respondida Plenamente       | **T**         | §XII "Future research", §XIII (p.16)             | Lacunas e direções explícitas: aprimorar RCA com LLM (contexto, alucinações, conhecimento de sistema), fusão multimodal, RCA explicável + tempo real, datasets multi-domínio; reflexão sobre a própria limitação (96 queries "keyword+venue" podem excluir trabalhos; ampliar p/ literatura cinza).     |
|     |                            | **SCORE_RQ**                 |                             | **2.5 / 5.0** |                                                  |                                                                                                                                                                                                                                                                                                         |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ----------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P26 | Survey / Revisão (Kitchenham) | **Y** (1.0) | **P** (0.5) | **N** (0.0) | **Y** (1.0) | **2.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — objetivos claros: revisar técnicas de RCA por cenário de aplicação e tipo de dado, datasets, ferramentas e métricas (§I, §II).
- **QA2 = P** — metodologia descrita (diretrizes Kitchenham, 5 bases, critérios de inclusão/exclusão, 96 queries "keyword+venue", material suplementar), **porém sem fluxo PRISMA com contagens explícitas de triagem/inclusão nem strings de busca completas** → replicabilidade parcial (inferior à de P24).
- **QA3 = N** — **sem validação empírica primária**: síntese da literatura. Pela rubrica ("teórico = N"), estudo secundário não fornece base de evidências própria.
- **QA4 = Y** — conclusões coerentes com a síntese **e** discute a limitação do próprio método de busca (possível exclusão de fontes; ampliar p/ literatura cinza).

## Parecer final do revisor

**Síntese.** Survey bem organizado de **técnicas de Root Cause Analysis** para aplicações multi-serviço, com taxonomia dupla (cenário × tipo de dado), inventário de datasets/ferramentas e discussão de métricas. Contudo, para uma RSL sobre **Agentic AI Copilot para Resposta a Incidentes**, há dois problemas combinados: (i) é **estudo secundário** (survey), sem evidência empírica própria (QA3 = N); e (ii) **não é centrado em Agentic AI** — autonomia/agentes aparecem apenas tangencialmente (§VII), resultando em **RQ1 = N**. Sua relevância é como **panorama do campo de RCA** (etapa de diagnóstico do IR), métricas e datasets — não como evidência sobre sistemas agênticos.

**Recomendação: EXCLUIR da síntese primária** (reter, no máximo, como **referência de fundamentação** sobre o panorama de RCA, datasets e métricas). SCORE_RQ 2,5/5,0 e QA 2,5/4,0 (**Banda Média**). Comparado a P24 (que ao menos era um survey **de** Agentic AI, forte em RQ1/RQ4/RQ5), P26 é um survey **de RCA** com conteúdo agêntico marginal — fit mais fraco com o escopo da RSL.

> ⚠️ **Decisão de protocolo (cabe ao condutor da RSL):** se o protocolo restringir o corpus a **estudos primários** e/ou **centrados em Agentic AI**, P26 deve ser **excluído** (dupla razão: secundário + não-agêntico). Se admitir referências contextuais de RCA, pode ser citado na fundamentação — inclusive por seguir Kitchenham, alinhado ao método da RSL.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → IEEE Xplore / Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _IEEE Transactions on Services Computing_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios de elegibilidade verificáveis no PDF atendidos (Ano 2025/2026 ✓; veículo IEEE TSC ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**. _Observação:_ a decisão de EXCLUIR aqui é por **relevância/tipo de estudo**, não por inelegibilidade formal.
