# Avaliação RSL — Estudo P35

**Artigo:** _Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps_ — H. Zou, Y. Zhao, X. Chen, L. Wang, J. Yu, L. Yuan (State Grid Jiangsu Electric Power + Wuhan University of Technology, China)
**Arquivo:** P35-A2-TSP_CMC_77908.pdf (24 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                                            | Ano  | Cit.                                                            | SJR                               | Qualis                                          | Tipo                                                                                              | DOI                      |
| --- | -------------------------------------------------------------------------- | ---- | --------------------------------------------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------ |
| P35 | Computers, Materials & Continua (CMC), Tech Science Press (Vol. 88, No. 1) | 2026 | [VERIFICAR] (base indexadora — provável baixa, pub. 08/05/2026) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Artigo de pesquisa empírico (framework LLM multi-agente; 5 datasets, baselines, ablação, t-tests) | 10.32604/cmc.2026.077908 |

_Evidências: cabeçalho p.1 (DOI; recebido 19/12/2025, aceito 13/03/2026, publicado 08/05/2026); "Comput Mater Contin. 2026;88(1):40"; CC-BY. Templates de prompt no Apêndice A. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                          | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)            | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | ------------------------------- | ---------------------------- | ----------------------- | ------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P35 | Graph-Augmented Multi-Agent RCA | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §1, §4 (p.2-12)                   | Autonomia caracterizada — equipe de agentes especializados simula workflow de SRE; processo de decisão sequencial Diagnose-Propagate-Decide (a); características — planejamento/orquestração (Coordinator Agent c/ contexto global compartilhado + backtracking), memória (contexto compartilhado, biblioteca), uso de ferramentas (fault gradient, AFG, CoT) (b); modelo decisório explícito — Navigator (busca), Diagnoser (CoT), Verifier (validação adversarial), Coordinator (controle) (c). |
| P35 | "                               | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §4 (p.7-12), Apêndice A           | Arquitetura multi-agente em 2 fases (AFG + raciocínio colaborativo) (a); stack — LLM (GPT-4 Turbo), Anomaly Fusion Graph, alinhamento híbrido log-trace, GPT como "semantic arbitrator", templates de prompt (b); **guardrails fortes** — Verifier Agent c/ Adversarial Validation Protocol (counterfactual + symptom consistency + causal sufficiency), backtracking dinâmico baseado em stack p/ podar ramos incorretos (c).                                                                    |
| P35 | "                               | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §5, Tabs. 2-7 (p.13-18)           | Quantitativo robusto: F1 médio 88,4% (+4,6% sobre DeepTraLog, +17% sobre Direct-LLM), **significância estatística** (paired t-test p<0,01, mean±std de 5 runs); qualidade de associação log-trace 97,5% F1; **ablação** (Tab. 5), robustez da verificação (Tab. 4), **análise de runtime/custo** (~21,4s, 9,7K tokens, ~$0,15/falha) e **análise de casos de falha** (Tab. 7) (b); benefícios qualitativos — caminhos diagnósticos verificáveis (a); evidência — **5 datasets** diversos (c).     |
| P35 | "                               | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §1 (desafios), §5.2.6 (p.2-3, 18) | Desafios técnicos fortes e bem analisados — alucinação/"causal confusion" de LLMs, alinhamento multimodal, propagação ambígua, semântica de log insuficiente, degradação do backtracking em topologias densas (a). Mecanismo de robustez (validação adversarial) como guardrail (c parcial). Porém **sem discussão ética/governança/accountability** (b ausente).                                                                                                                                 |
| P35 | "                               | RQ5 Research Gaps            | Parcialmente Respondida | **P**         | §5.2.6, §6 (p.18)                 | Limitações bem caracterizadas (propagação ambígua, jargão fora do treino, janelas <10ms, custo do backtracking), porém a conclusão **não enuncia direções futuras explícitas** — as lacunas estão implícitas na análise de falhas.                                                                                                                                                                                                                                                                |
|     |                                 | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P35 | Artigo de pesquisa empírico (LLM multi-agente, AIOps) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (RCA manual trabalhoso; limitações de métodos single-modal e de LLMs diretos — alucinação/déficit de raciocínio estrutural) e solução agêntica (Graph-Augmented Multi-Agent) explícitos (§1).
- **QA2 = Y** — arquitetura, protocolo de raciocínio, fórmulas, hiperparâmetros (profundidade de busca = 10), 5 datasets, 2 baselines e **templates de prompt completos (Apêndice A)**. Ressalva menor: dados indisponíveis por restrições de privacidade e sem repositório de código — mas o método e os prompts são reprodutíveis.
- **QA3 = Y** — validação empírica **forte**: 5 datasets, baselines, ablação por componente, robustez da verificação, runtime/custo, análise de falhas e **teste de significância estatística** (mean±std, paired t-test p<0,01).
- **QA4 = Y** — conclusões coerentes com os resultados; **seção dedicada de limitações/análise de falhas** (§5.2.6) com taxas de falha por dataset e modos de erro.

## Parecer final do revisor

**Síntese.** Estudo empírico **fortemente agêntico e bem avaliado**: framework **LLM multi-agente** (Diagnoser/Navigator/Verifier/Coordinator) sobre um **Anomaly Fusion Graph**, para RCA robusta em AIOps/microsserviços. Destaques: combate explícito à alucinação via **Adversarial Validation Protocol** (Verifier) + backtracking dinâmico (Coordinator), com evidência sólida (5 datasets, ablação, **significância estatística**, custo/runtime e análise de falhas). Aderência alta a **RQ1-RQ3**; **RQ4 parcial** (desafios técnicos fortes, ética/governança ausente); **RQ5 parcial** (limitações ricas, mas sem direções futuras explícitas).

**Recomendação: INCLUIR.** SCORE_RQ 4,0/5,0 e QA 4,0/4,0 (Banda Alta). Estudo agêntico de alta qualidade metodológica (entre os mais rigorosos do lote — t-tests, ablação, custo, falhas), excelente par com P23/P27/P32 no eixo "RCA agêntico". Domínio: RCA em microsserviços (diagnóstico) — núcleo da etapa de diagnóstico do IR, não específico de segurança.

> ℹ️ **Para a síntese:** 3º estudo de equipe ligada à **State Grid** (cf. P31 SGCC, P32 SGCC/Beihang) — registrar a procedência institucional ao avaliar diversidade/independência dos estudos.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar. ⚠️ Publicado em 08/05/2026 — contagem possivelmente 0; atenção ao critério "Citações ≥ 1".
- **SJR (quartil)** → Scimago, _Computers, Materials & Continua_ (insumo: Q2).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2026 ✓; veículo CMC/Tech Science Press ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
