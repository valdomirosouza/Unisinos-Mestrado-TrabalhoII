# Avaliação RSL — Estudo P19

**Artigo:** _Agent System Mining: Vision, Benefits, and Challenges_ — A. Tour, A. Polyvyanyy, A. Kalenkova (The University of Melbourne)
**Arquivo:** P19-A1 - Agent_System_Mining_Vision_Benefits_and_Challenges.pdf (15 páginas)

> ⚠️ **Recomendação: EXCLUIR — não-aderência ao escopo.** "Agent System Mining" = Process Mining + Agent-Based Modeling em BPM (2021); "agente" no sentido de ABM/MAS, **não** Agentic AI (LLM). Sem IR. Captura falsa-positiva por "agent" (como P7/P11). SCORE_RQ 0.0/5; QA 1.5/4.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.        | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                              | DOI                         |
| --- | ---------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------- | --------------------------- |
| P19 | _IEEE Access_ (Vol. 9) | 2021 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de visão/conceitual (Process Mining + ABM) | 10.1109/ACCESS.2021.3095464 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2021.3095464; recebido 16/06/2021, publicado 08/07/2021; "VOLUME 9, 2021"; licença CC-BY). Propõe Agent System Mining (ASM) e ASM Framework, combinando Process Mining e Agent-Based Modeling em Business Process Management, ilustrado por exemplo "order fulfillment". Varredura confirmou ausência de "agentic", "LLM", "incident", "cyber". Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                    | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.) | Parecer do revisor                                                                                                                                                                                                     |
| --- | ------------------------- | ---------------------------- | --------------------------- | ------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P19 | Agent System Mining (ASM) | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §I, §III (p.1–7)       | "Agente" no sentido de **Agent-Based Modeling / MAS em BPM** (agentes autônomos induzindo processos de negócio, sistemas sociotécnicos). **Não** é Agentic AI (LLM); sem autonomia/planejamento/ferramentas agênticas. |
| P19 | "                         | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §IV (p.7–13)           | O "framework" ASM combina **Process Mining + ABM** para inferir modelos de MAS de logs de eventos — **não** arquitetura de engenharia de agentic AI (sem orquestração/memória/ferramentas/guardrails de agentes LLM).  |
| P19 | "                         | RQ3 Evidence Benefits        | Não tem conteúdo suficiente | **N**         | §I, §IV (p.1, 7–13)    | Benefícios reportados são de **ASM/process mining** (modelos de processo mais realistas e compreensíveis) — não benefícios de Agentic AI nem de Resposta a Incidentes. Domínio é BPM/mineração de processos.           |
| P19 | "                         | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | §IV (p.7–13)           | Desafios são de **implementação do ASM Framework** (mineração de processos + ABM), não desafios/ética/governança de agentic AI.                                                                                        |
| P19 | "                         | RQ5 Research Gaps            | Não tem conteúdo suficiente | **N**         | §VI (p.14)             | Direções futuras tratam de ASM/BPM — **não** lacunas de agentic AI (benchmarking/threat models/observabilidade/alinhamento agêntico).                                                                                  |
|     |                           | **SCORE_RQ**                 |                             | **0.0 / 5.0** |                        | N + N + N + N + N                                                                                                                                                                                                      |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                    | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P19 | Artigo de visão/conceitual (Process Mining + ABM) | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (complexidade dos "spaghetti models" do Process Mining; MAS para gerenciá-la) e solução (ASM + ASM Framework) explícitos (§I).
- **QA2 = N** — **artigo de visão sem metodologia replicável** (proposta conceitual ilustrada por exemplo "order fulfillment"; não é revisão sistemática nem estudo experimental reproduzível).
- **QA3 = N** — **sem validação empírica** (exemplo ilustrativo, não experimento/estudo de caso/simulação com métricas). §IV.4 discute validação de modelo MAS apenas conceitualmente.
- **QA4 = P** — conclusões coerentes com a visão e discussão de benefícios/desafios; porém sem grounding empírico nem limitações do próprio estudo.

## Parecer final do revisor

**Síntese.** P19 é um **artigo de visão/conceitual de 2021** que propõe **Agent System Mining (ASM)** — a combinação de **Process Mining + Agent-Based Modeling** no contexto de **Business Process Management** — para inferir modelos de sistemas multiagentes de processos de negócio a partir de logs de eventos. O termo "Agent/Multi-Agent" é usado no sentido de **modelagem baseada em agentes/MAS em BPM**, **não** de Agentic AI (LLM). Não há LLMs, autonomia agêntica, uso de ferramentas/orquestração, nem qualquer relação com **Resposta a Incidentes** (varredura confirmou ausência de "agentic", "LLM", "incident", "cyber"). Nenhuma das cinco RQs é atendida (SCORE_RQ 0,0/5). É um caso **análogo a P7/P11** — captura falsa-positiva pelo termo "agent"/"multi-agent" — porém, ao contrário deles (MARL empírico forte, QA 4,0), P19 é um **paper de visão sem validação empírica** (QA 1,5, Média).

**Recomendação: EXCLUIR — por não-aderência ao escopo.** Justificativa: apesar de passar (provisoriamente) na elegibilidade formal, o estudo **não contribui para nenhuma RQ** da RSL sobre Agentic AI para IR — é Process Mining + ABM em BPM, paradigma e domínio alheios. Recomenda-se excluir e revisar os critérios de busca que o capturaram (provável casamento por "agent system"/"multi-agent").

**Pendências de verificação externa:** (registradas por completude; não alteram a exclusão por escopo)

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
