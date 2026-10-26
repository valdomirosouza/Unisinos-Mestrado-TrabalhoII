# Avaliação RSL — Estudo P19 (fundacional, retroativa)

**Artigo:** _Agent System Mining: Vision, Benefits, and Challenges_ — A. Tour, A. Polyvyanyy, A. Kalenkova (School of Computing and Information Systems, The University of Melbourne)
**Arquivo:** P19-A1-Agent_System_Mining_Vision_Benefits_and_Challenges.pdf (15 páginas)
**Natureza da avaliação:** RETROATIVA — estudo do corpus fundacional (Trabalho I); a inclusão NÃO é rediscutida; mede-se aderência às RQs e qualidade DARE para padronização com os ciclos 1 e 2.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.      | Ano  | Cit.                                               | SJR             | Qualis          | Tipo                                                                                                    | DOI                         |
| --- | -------------------- | ---- | -------------------------------------------------- | --------------- | --------------- | ------------------------------------------------------------------------------------------------------- | --------------------------- |
| P19 | IEEE Access (Vol. 9) | 2021 | OA 32 / CR 32 / Scopus 36 (papers.csv, 2026-07-27) | Q1 (verificado) | A1 (verificado) | Vision paper (proposta conceitual) c/ exemplo motivacional simulado e revisão de literatura estruturada | 10.1109/ACCESS.2021.3095464 |

_Evidências: cabeçalho p.1 (DOI, recebido 16/06/2021, publicado 08/07/2021); rodapé "VOLUME 9, 2021" (pp. 99480–99494); licença CC-BY 4.0; afiliação University of Melbourne (p.1). Citações, SJR e Qualis verificados externamente nas três fontes (papers.csv, 2026-07-27)._

### Etapa 1 — Triagem de elegibilidade

**FUNDACIONAL — inclusão herdada do Trabalho I (não rediscutida); bibliometria verificada.**

- Ano ≥ 2020 → 2021 ✓ (p.1)
- Publicação ≠ NULL → IEEE Access ✓ (p.1)
- Citações ≥ 1 → OA 32 / CR 32 / Scopus 36 ✓ (verificado)
- SJR Q1–Q2 → Q1 ✓ (verificado)
- Qualis A1–A2 → A1 ✓ (verificado)

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo              | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                  | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --- | ------------------- | ---------------------------- | ----------------------- | ------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P19 | Agent System Mining | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §III.D (p.6, 99485), §I (p.2)           | Definição explícita de agente com quatro aspectos-chave — autonomy, situatedness, proactivity, sociality: "autonomous agents achieve their goals by following their internal execution flows fully independent from the external control"; proatividade = planejamento e iniciativa (a, b parciais). Porém sem modelo decisório do agente (c), sem memória, uso de ferramentas (tool use no sentido agêntico) ou supervisão humana — agentes são componentes de MAS clássicos (ABM), não Agentic AI baseada em LLM.                                 |
| P19 | "                   | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §IV.A-B, Figs. 6-7 (p.6-9), §II (p.2-3) | Arquitetura conceitual detalhada: ASM Framework em V-model com 5 fases (Motivate/Plan/Develop/Evaluate/Use) e 7 atividades (search, project, discover, enhance, integrate, diagnose, check); MAS decomposto em sub-modelos de agente, ambiente e interações (a). Ferramentas citadas apenas no exemplo — Disco, AnyLogic (b parcial). Diagnose/check = observabilidade e validação do comportamento de agentes via logs reais × simulados (c parcial). Sem orquestração LLM, memória, guardrails ou stack de produção — framework não implementado. |
| P19 | "                   | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §IV.C (p.9-10), §II Figs. 1-4 (p.3-6)   | Benefícios qualitativos explícitos em 6 categorias: evidence-based modeling, shorter model development cycles, better conformance, managing complex/flexible/context-aware processes (a). Nenhuma métrica quantitativa nem avaliação empírica — evidência limitada a exemplo motivacional simulado (order fulfillment em AnyLogic, log publicado em DOI 10.26188/14401400) demonstrando que MAS evita "spaghetti process models" (b ausente, c fraco). Nada específico de Incident Response.                                                        |
| P19 | "                   | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §IV.D (p.10-11)                         | Oito desafios técnicos bem desenvolvidos: seleção de metamodel MAS, definição de escopo, suporte a simulação/análise estática, validação de modelos MAS, seleção de dados de evento, agent type discovery, sub-model discovery, seleção de linguagem de modelagem (a forte). Dimensão ética/governança quase ausente — apenas menção a data privacy em contexto cross-organizacional (desafio 5, p.11) e accountability citada só em trabalho relacionado [44] (§V.C1, p.12); sem mecanismos de governança próprios (b/c ausentes).                 |
| P19 | "                   | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §V.C (p.12-13), §VI (p.13)              | Lacunas explícitas da revisão estruturada: "little research has been done to understand which frameworks and metamodels are suitable for inferring MAS models from business process data"; trabalhos existentes "do not allow, neither individually nor collectively, implementing the ASM framework". Agenda futura em 3 eixos: metamodels/formalisms para MAS descobertos de dados, algoritmos ASM de discovery/enhancement, e técnicas de avaliação de qualidade dos modelos minerados (avaliação/observabilidade).                              |
|     |                     | **SCORE_RQ**                 |                         | **3.0 / 5.0** |                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                                      | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P19 | Vision paper c/ exemplo motivacional simulado e revisão estruturada | **Y** (1.0) | **P** (0.5) | **P** (0.5) | **Y** (1.0) | **3.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema explícito: assunções simplificadoras do Process Mining geram "spaghetti process models" ilegíveis em processos complexos/auto-organizados (Abstract; §I, p.1-2; §II, Fig. 3, p.5); solução agent-based explícita: ASM = Process Mining + ABM para inferir modelos MAS de processos de negócio a partir de event data (§I, §IV).
- **QA2 = P** — framework descrito com precisão conceitual (fases, atividades, artefatos — Figs. 6-7) e exemplo com log publicado (DOI 10.26188/14401400) e ferramentas nomeadas (Disco, AnyLogic); a revisão de literatura do §V é replicável (queries Q1-Q3, bases Scopus/WoS, data 16/02/2021, contagens 2.094→149, lista publicada em DOI 10.26188/14708772). Porém ASM não é implementado: sem algoritmos, parâmetros ou cenário experimental replicável.
- **QA3 = P** — sem validação empírica do framework; evidência limitada ao exemplo motivacional simulado (toy example: order fulfillment com GIS data em AnyLogic, §II, Figs. 1-4), que demonstra o problema e a alternativa MAS mas não avalia algoritmos ASM (inexistentes). Conforme rubrica: toy example = P.
- **QA4 = Y** — conclusões coerentes com a natureza de vision paper: não reivindicam resultados além do proposto; limitações reconhecidas como desafios abertos (§IV.D) e a necessidade de validação futura do framework é admitida explicitamente ("Further analysis of ASM benefits... will validate ASM Framework", §VI, p.13).

## Parecer final do revisor

**STATUS: MANTIDO NO CORPUS (fundacional)**

**Síntese.** Vision paper que propõe **Agent System Mining (ASM)**: a combinação de Process Mining e Agent-Based Modeling para descobrir, aprimorar e validar modelos MAS de processos de negócio a partir de event logs reais e simulados. O papel do estudo na RSL é fundacional para a dimensão de **observabilidade de comportamento de agentes**: as atividades discover/enhance/integrate/diagnose/check formalizam como inferir e verificar o comportamento de agentes autônomos a partir de dados de eventos — base conceitual para observability e behavioral mining de sistemas agênticos (RQ2c/RQ5). A aderência é moderada: o conceito de agente é o de MAS/ABM clássico (pré-LLM), sem mecanismos de Agentic AI moderna (memória, tool use, guardrails, supervisão humana) e sem conexão com Incident Response; RQ1-RQ4 ficam parciais e apenas RQ5 é plena (lacunas e agenda futura explícitas). SCORE_RQ 3.0/5.0; QA 3.0/4.0 (Banda Alta) — qualidade elevada para a sua categoria (objetivos claros, revisão de literatura replicável, conclusões honestas), penalizada pela ausência de implementação e validação empírica, inerente a um vision paper.

**Pendências de verificação externa:** nenhuma (bibliometria verificada nas três fontes).
