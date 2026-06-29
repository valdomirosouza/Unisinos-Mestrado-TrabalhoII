# Avaliação RSL — Estudo P29

**Artigo:** _AIOps for log anomaly detection in the era of LLMs: A systematic literature review_ — M. De la Cruz Cabello, T. Prince Sales, M. R. Machado (University of Twente, Holanda)
**Arquivo:** P29-A2-1-s2.0-S2667305325001346-main.pdf (18 páginas)

> ⚠️ **Alerta de tipo de estudo:** é uma **Revisão Sistemática da Literatura (SLR)** — estudo **secundário**. Determinante para QA3 e para a recomendação. **NÃO é centrado em Agentic AI** — o tema é **detecção de anomalias em logs com LLMs + RAG**; agentes/autonomia aparecem apenas tangencialmente (um trabalho citado, Loevenich et al., sobre agentes autônomos de defesa).

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                                    | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                              | DOI                        |
| --- | ------------------------------------------------------------------ | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------- | -------------------------- |
| P29 | Intelligent Systems with Applications (Elsevier) (Vol. 28, 200608) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | **SLR / Revisão sistemática** — estudo secundário | 10.1016/j.iswa.2025.200608 |

_Evidências: cabeçalho p.1 (rótulo "Review"; DOI; recebido 13/07/2025, aceito 09/11/2025, online 19/11/2025); "Intelligent Systems with Applications 28 (2025) 200608"; CC-BY. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                          | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)        | Parecer do revisor                                                                                                                                                                                                                                                                                                       |
| --- | ------------------------------- | ---------------------------- | --------------------------- | ------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P29 | SLR AIOps log anomaly (LLM+RAG) | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §4.4 (p.12)                   | A SLR **não define** autonomia, planejamento, memória, uso de ferramentas ou modelo decisório agêntico. "Agentes autônomos" surgem apenas em menção tangencial (Loevenich et al., MARL+LLM em rede NATO). Foco é LLM+RAG para detecção de anomalias, não Agentic AI.                                                     |
| P29 | "                               | RQ2 Engineering Architecture | Parcialmente Respondida     | **P**         | §4.2-4.4, Figs. 9-10 (p.8-14) | Sintetiza técnicas/ferramentas LLM+RAG (vector DBs, Drain parsing, fine-tuning, prompt engineering) e propõe um framework de 3 estágios (CRISP-ML) para detecção (b/c parciais). Porém **não é arquitetura agêntica** (sem orquestração de agentes, guardrails, observabilidade ou memória de agente).                   |
| P29 | "                               | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §4.1-4.2 (p.6-11)             | Sintetiza benefícios (LLM+RAG > tradicional em acurácia/interpretabilidade/adaptabilidade) e métricas do campo (F1, precisão, recall) (a/b parciais); **sem evidência empírica própria** (estudo secundário) e não específica de Agentic AI/IR (c ausente).                                                              |
| P29 | "                               | RQ4 Challenges & Ethics      | Parcialmente Respondida     | **P**         | §4.1-4.3 (p.6-12)             | Desafios técnicos fortes — data/domain drift, escassez de dados rotulados, restrições de tempo real, desbalanceamento de classes, parsing, eficiência computacional, alucinações (a); privacidade de logs e explicabilidade ("black-box") tangenciados (b/c parciais). Sem ética/governança/accountability aprofundadas. |
| P29 | "                               | RQ5 Research Gaps            | Respondida Plenamente       | **T**         | §4.4 (p.12-14)                | Lacunas e direções explícitas: pipelines de detecção em tempo real, datasets de log sob medida para RAG, aplicação ao domínio militar, framework CRISP-ML proposto; reflexão sobre a própria limitação (base única, viés de seleção).                                                                                    |
|     |                                 | **SCORE_RQ**                 |                             | **2.5 / 5.0** |                               |                                                                                                                                                                                                                                                                                                                          |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo            | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P29 | SLR / Revisão sistemática | **Y** (1.0) | **P** (0.5) | **N** (0.0) | **Y** (1.0) | **2.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — objetivos claros: 4 knowledge questions explícitas, foco em AIOps/LLM/RAG para detecção de anomalias em logs (§1, §2).
- **QA2 = P** — protocolo replicável (critérios em Tabela 1, **strings de busca explícitas**, snowballing, tabela de extração no Apêndice), **porém rigor limitado**: apenas **uma base primária (Scopus)** + arXiv, corpus pequeno (**33 artigos**), sem estágio formal de avaliação de qualidade dos estudos incluídos; viés de seleção reconhecido pelos próprios autores.
- **QA3 = N** — **sem validação empírica primária**: síntese da literatura. Pela rubrica ("teórico = N").
- **QA4 = Y** — conclusões coerentes com a síntese **e** discussão das próprias limitações (base única, viés de seleção, escassez de estudos no domínio militar).

## Parecer final do revisor

**Síntese.** SLR sobre **detecção de anomalias em logs com LLMs + RAG** no contexto de AIOps, com uma vertente de aplicação ao domínio militar/defesa. Para a RSL sobre **Agentic AI Copilot para Resposta a Incidentes**, o ajuste é **fraco em dois eixos**: (i) **estudo secundário** (SLR), sem evidência empírica própria (QA3 = N); e (ii) **não centrado em Agentic AI** — autonomia/agentes só tangenciais (**RQ1 = N**). Topicamente, porém, está **mais próximo de IR** do que P26 (RCA geral), pois detecção de anomalias/incidentes é a sub-tarefa de **detecção** do IR/AIOps.

**Recomendação: EXCLUIR da síntese primária** (estudo secundário + não-agêntico), **retendo como referência de fundamentação / revisão correlata** — útil para posicionar a contribuição da RSL no panorama de detecção de anomalias com LLM e como "related review". SCORE_RQ 2,5/5,0 e QA 2,5/4,0 (**Banda Média**). Perfil análogo a P26 (SLR/survey não-agêntico) e distinto de P24 (survey **de** Agentic AI, forte em RQ1).

> ⚠️ **Decisão de protocolo:** se o protocolo restringir o corpus a **estudos primários** e/ou **centrados em Agentic AI**, P29 deve ser **excluído**. Por ser uma SLR vizinha (AIOps/anomaly detection), é candidata natural a **referência de trabalhos relacionados** na fundamentação da RSL.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _Intelligent Systems with Applications_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2025 ✓; veículo Elsevier ISwA ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**. _Observação:_ a decisão de EXCLUIR é por **tipo de estudo/relevância**, não por inelegibilidade formal.
