# Avaliação RSL — Estudo P27

**Artigo:** _Leveraging multi-agent framework for root cause analysis_ (MA-RCA) — F. Fu, H. Ding, Y. Qin, J. Yu, D. Xu (NARI-TECH Nanjing Control Systems Ltd, China)
**Arquivo:** P27-A1-s40747-025-02096-0.pdf (13 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                       | Ano       | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                                                         | DOI                        |
| --- | ----------------------------------------------------- | --------- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------- |
| P27 | Complex & Intelligent Systems (Springer) (Vol. 12, 4) | 2025/2026 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa empírico (framework LLM multi-agente; 2 datasets, baselines, ablação, sistema implantado) | 10.1007/s40747-025-02096-0 |

_Evidências: cabeçalho p.1 (DOI; recebido 20/06/2025, aceito 05/09/2025, online 06/11/2025); "Complex & Intelligent Systems (2026) 12:4"; © The Author(s) 2025 (open access). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                    | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                         | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --- | ------------------------- | ---------------------------- | ----------------------- | ------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P27 | MA-RCA (multi-agente RCA) | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | "RCA Agent", "Agent scheduling" (p.3-5), Fig.1 | Autonomia explícita — RCA Agent como orquestrador com "dynamic decision engine"; agentes selecionam ferramentas e coordenam workflow; supervisão humana via interface NL do SRE + requery por campos faltantes (a); características — orquestração/planejamento, memória (repositório de casos históricos), uso de ferramentas (tool repository, Validation Agent), retrieval/RAG (b); modelo decisório — pattern matching determinístico + mineração de associação probabilística, síntese de hipóteses (c). |
| P27 | "                         | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | "Method" (p.3-7), Fig.1, Algoritmo 1           | Arquitetura multi-agente colaborativa — 4 agentes especializados (RCA/Retrieval/Validation/Report) + repositórios (a); stack — agentes LLM, RAG (vector DB, cosseno, indexação hierárquica/LSH), tool repository, testes dinâmicos (b); capacidades avançadas/guardrails — Retrieval Agent (grounding), Validation Agent (verificação tool-in-the-loop contra alucinação), checagem de completude de entrada (c).                                                                                             |
| P27 | "                         | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | "Evaluation", Tabs. 3-6 (p.7-11)               | Quantitativo robusto: Nezha F1 0,952 (Acc 0,958), Power F1 0,828 (Acc 0,843), superando 5 baselines (CoT 0,412; RAG 0,704; RCACOPILOT 0,748; RCAgent 0,725; mABC 0,726) (b); ablação por componente (Tab. 4) e sensibilidade ao nº de casos (Tab. 6); benefícios qualitativos — supressão de alucinação, grounding (a); evidência forte — 2 datasets reais + sistema implantado como plug-in "Diagnosis Agent" (c).                                                                                           |
| P27 | "                         | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | "Introduction", "Conclusions" (p.1-2, 12)      | Desafios técnicos/robustez fortes — alucinação, propagação de erro, context-switching, dependência da qualidade do repositório de casos, latência adicional (a); mecanismos de mitigação (Validation Agent, checagem de entrada) como guardrails (c parcial). Porém **sem discussão ética/governança/accountability** (b ausente).                                                                                                                                                                            |
| P27 | "                         | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | "Conclusions" (p.12)                           | Limitações + direções explícitas: retrieval adaptativo (top-k dinâmico por contexto), execução especulativa/prefetching para reduzir latência da equipe de agentes.                                                                                                                                                                                                                                                                                                                                           |
|     |                           | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                 | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ---------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P27 | Artigo de pesquisa empírico (LLM multi-agente) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (desafios de RCA; alucinação de LLM; propagação de erro em arquiteturas single-agent) e solução agêntica (MA-RCA multi-agente) explícitos (Introduction).
- **QA2 = Y** — arquitetura e workflow detalhados, Algoritmo 1 (Retrieval Agent), datasets (Nezha público + Power metering), 5 baselines, métricas, pré-processamento (partição estratificada 50/50), estudo de sensibilidade. _Ressalvas:_ o **LLM base não é claramente especificado**, o dataset Power é proprietário/parcialmente sintético e não há link de código.
- **QA3 = Y** — validação empírica robusta: 2 datasets de mundo real, 5 baselines fortes, ablação por componente, sensibilidade de hiperparâmetro e **demonstração de sistema implantado** (plug-in em infraestrutura de medição de energia).
- **QA4 = Y** — conclusões decorrem dos resultados; limitações explicitamente discutidas (dependência do repositório histórico, latência) com direções de mitigação.

## Parecer final do revisor

**Síntese.** Estudo **fortemente agêntico** e bem avaliado: framework **LLM multi-agente (MA-RCA)** com orquestrador (RCA Agent), Retrieval Agent (RAG/grounding), Validation Agent (verificação tool-in-the-loop contra alucinação) e Report Agent, aplicado a RCA em sistemas cloud-native (Nezha) e infraestrutura de medição de energia. Aderência alta a **RQ1-RQ3 e RQ5**; **RQ4 parcial** (robustez/guardrails fortes, mas sem ética/governança). Diferencial: combate explícito à alucinação via grounding + validação por ferramentas, com **ablação** demonstrando a indispensabilidade de cada agente e um **sistema implantado**.

**Recomendação: INCLUIR.** SCORE_RQ 4,5/5,0 e QA 4,0/4,0 (Banda Alta). Estudo central e bem alinhado ao escopo agêntico da RSL (LLM multi-agente com orquestração/memória/ferramentas/validação). Observação de escopo: o domínio é **RCA/diagnóstico** (cloud-native + cyber-físico de energia), núcleo da etapa de diagnóstico do IR, embora não seja resposta a incidentes de segurança em sentido estrito — bom par de comparação com P23 (RCA com agente LLM de síntese) e P22 (remediação autônoma).

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar (artigo recente, nov/2025 — possível baixa contagem).
- **SJR (quartil)** → Scimago, _Complex & Intelligent Systems_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios verificáveis no PDF atendidos (Ano 2025/2026 ✓; veículo Complex & Intelligent Systems ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
