# Avaliação RSL — Estudo P22

**Artigo:** _ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control_ — V. Avgerinos, K. Ramantas, L. Alonso, C. Verikoukis
**Arquivo:** P22-A1-ARM_Autonomous_Remediation...pdf (11 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                  | Ano       | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                          | DOI                       |
| --- | ------------------------------------------------ | --------- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------- |
| P22 | IEEE Internet of Things Journal (Vol. 13, No. 9) | 2025/2026 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa c/ avaliação experimental (chaos engineering, cluster K3s) | 10.1109/JIOT.2025.3648858 |

_Evidências: cabeçalho p.1 (DOI; recebido 17/07/2025, aceito 11/12/2025, publicado 26/12/2025; data da edição 1 May 2026); rótulo "IEEE Internet of Things Journal, Vol. 13, No. 9". Citações/SJR/Qualis não constam no PDF. Obs.: carimbo de download do IEEE Xplore identifica "UNIVERSIDADE DO VALE DO RIO DOS SINOS"._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                       | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                 | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | ---------------------------- | ---------------------------- | ----------------------- | ------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P22 | ARM (Autonomous Remediation) | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §IV.A-C (p.3-5), §III.D, Fig.1         | Autonomia explícita — "autonomous operator with authority to execute corrective actions", modelo de execução "accountable", visão zero-touch + workflows de aprovação humana opcionais (a); planejamento (create_action_plan, planning-first), memória (contexto cumulativo in-context, transiente), uso de ferramentas (MCP/ReAct) (b); modelo decisório evidence-first com critérios de conclusão e intent object I(t) (c).                                                  |
| P22 | "                            | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §IV (p.3-5), §V.A (p.5), Tab. I, Fig.1 | Arquitetura closed-loop single-agent round-based, influência ReAct (a); stack explícito — MCP server, kubectl, Prometheus/Grafana, K3s, GPT-5/GPT-5-mini, emulador MuBench, chaosd (b); capacidades avançadas: tool abstraction layer c/ guardrails, aprovação humana por ferramenta, caching temporal, delays de estabilização, observabilidade via topologia/timeseries (c).                                                                                                 |
| P22 | "                            | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §VI, Tabs. IV-V, Figs. 3-4 (p.6-9)     | Quantitativo extenso: identificação 52,9% / mitigação 70,7% (abstract); GPT-5 ~80% restauração SLA e ~78% identificação; latency recovery Rlat 80,4%; rounds de decisão e wall-clock (5,2 vs 12,8 min); % de uso de ferramentas (b); benefícios qualitativos — explicabilidade, rastreabilidade, adaptação por camada (a); evidência forte — 60 cenários de falha, chaos engineering, 2 modelos comparados (c).                                                                |
| P22 | "                            | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §IV.C, §VI.C, §VII (p.4-9)             | Desafios técnicos fortes — wall-clock elevado, gap entre tamanhos de modelo, limites de contexto, exaustão de recursos, sensibilidade a falhas latentes (a). Mecanismos de governança concretos — aprovação humana, conformidade de política via MCP, viés-de-ação evidence-first, cautela quanto a ação errada em produção (c). Porém, dimensão **ética** propriamente dita (responsabilidade, viés, risco societal) ausente (b apenas tangencial via accountability/safety). |
| P22 | "                            | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §II.C, §VII (p.2-3, 9)                 | Identifica a lacuna central do campo (foco em diagnóstico vs. mitigação autônoma) e direções explícitas: context-compression, arquiteturas de agente mais profundas, fine-tuning de modelos menores, formalização de safety safeguards p/ ações de alto impacto, testbeds IoT heterogêneos maiores.                                                                                                                                                                            |
|     |                              | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                                   | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ---------------------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P22 | Artigo de pesquisa c/ avaliação experimental (chaos engineering) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (gestão manual insustentável; lacuna "diagnóstico-sem-mitigação" do estado da arte) e solução agêntica (RCA + mitigação autônoma closed-loop) explícitos (§I, §II.C).
- **QA2 = Y** — protocolo de 4 fases, cluster K3s de 7 nós com specs, emulador MuBench, chaosd, critério de sucesso formal com tolerâncias (ϵ_lat=0,15; ϵ_success=0,01), tool layer e filosofia do system prompt detalhados; Apêndice traz par plano/sumário real. Ressalva menor: prompt completo não publicado ("too extensive") e ausência de link de código.
- **QA3 = Y** — validação empírica com 60 cenários de falha, chaos engineering, comparação GPT-5 vs GPT-5-mini, múltiplas métricas (Tabs. IV-V) e traços de mitigação (Fig. 4). Ressalva: testbed único/emulado e sem baseline não-LLM.
- **QA4 = Y** — conclusões decorrem dos resultados (~80% restauração, ~78% identificação); limitações discutidas (wall-clock, gap de modelo, restrição de recursos) com direções de mitigação (§VII).

## Parecer final do revisor

**Síntese.** Estudo empírico forte que apresenta o **ARM**, framework closed-loop com agente LLM para **RCA + mitigação autônoma** de violações de SLA em ambientes Kubernetes IoT/edge. Aderência elevada a **RQ1-RQ3 e RQ5**; **RQ4 parcial** (desafios técnicos e mecanismos de governança/accountability fortes — aprovação humana, conformidade de política via MCP, cautela em produção —, mas sem tratamento ético propriamente dito). É, até aqui, o trabalho **mais aderente ao tema de Resposta a Incidentes**: fecha o ciclo detecção→diagnóstico→**remediação**, justamente a etapa que o próprio artigo aponta como lacuna do estado da arte.

**Recomendação: INCLUIR.** SCORE_RQ 4.5/5.0 e QA 4.0/4.0 (Banda Alta). Estudo central para a RSL — cobre arquitetura agêntica, evidências quantitativas robustas e o diferencial de **mitigação autônoma** (não apenas diagnóstico), com mecanismos de accountability e safety relevantes para sistemas críticos.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → IEEE Xplore / Scopus / Google Scholar (artigo recente, dez/2025 — possível baixa contagem).
- **SJR (quartil)** → Scimago, _IEEE Internet of Things Journal_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios verificáveis no PDF atendidos (Ano 2025/2026 ✓; veículo IEEE IoT Journal ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
