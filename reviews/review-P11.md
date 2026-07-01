# Avaliação RSL — Estudo P11

**Artigo:** _Co-Evolving Multi-Agent Transfer Reinforcement Learning via Scenario Independent Representation_ — A. Siddiqua, S. Liu, A. S. Nipu, A. Harris, Y. Liu (Missouri State University / University of Wisconsin-Platteville / Hunan University)
**Arquivo:** P11-A1 - Co-Evolving_Multi-Agent_Transfer_Reinforcement_Learning_via_Scenario_Independent_Representation.pdf (13 páginas)

> ⚠️ **Recomendação: EXCLUIR — não-aderência ao escopo.** Deep MARL (StarCraft SMAC, framework Co-MACTRL); sem Agentic AI (LLM) e sem Resposta a Incidentes. Alta qualidade metodológica (QA 4.0/4), mas SCORE_RQ 0.0/5. Caso análogo a P7.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                               | DOI                         |
| --- | ----------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------------------- | --------------------------- |
| P11 | _IEEE Access_ (Vol. 12) | 2024 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa (Deep MARL / transfer learning) | 10.1109/ACCESS.2024.3430037 |

_Evidências: cabeçalho p.1 (DOI 10.1109/ACCESS.2024.3430037; recebido 19/05/2024, aceito 11/07/2024, publicado 17/07/2024; "VOLUME 12, 2024"; licença CC-BY-NC-ND; apoio NSF Award 2302060). Framework Co-MACTRL (co-evolução + curriculum transfer learning) validado em StarCraft SMAC/MP-SMAC (§III–IV). Varredura textual confirmou ausência de "agentic", "LLM", "incident"; "transformer" refere-se a arquitetura de rede e "cyber" apenas a referências/biografia. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                     | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.) | Parecer do revisor                                                                                                                                                                                                                                           |
| --- | -------------------------- | ---------------------------- | --------------------------- | ------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P11 | Co-Evolving MA Transfer RL | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §I–II (p.1–4)          | "Agentes" são políticas de **Deep MARL** em StarCraft (MAS no sentido de aprendizado por reforço multiagente). **Ausentes** Agentic AI (LLM), autonomia agêntica, planejamento/uso de ferramentas/supervisão humana no sentido da RSL.                       |
| P11 | "                          | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §III (p.5–8)           | Contribuição é uma **arquitetura de rede DRL + framework de transfer/curriculum learning** (CTSCE, representação scenario-independent), **não** arquitetura de agentic AI (sem orquestração, ferramentas/frameworks agênticos, guardrails, observabilidade). |
| P11 | "                          | RQ3 Evidence Benefits        | Não tem conteúdo suficiente | **N**         | §IV (p.8–11)           | Benefícios reportados são **taxas de vitória em StarCraft** (win rate, generalização entre cenários) — não benefícios de agentic AI nem de Resposta a Incidentes. Fora do escopo da RQ.                                                                      |
| P11 | "                          | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | (todo o artigo)        | Não discute riscos/ética/segurança/governança de agentic AI; apenas limitações técnicas de MARL/transfer learning.                                                                                                                                           |
| P11 | "                          | RQ5 Research Gaps            | Não tem conteúdo suficiente | **N**         | §V (p.11–12)           | Trabalho futuro trata de escalar Co-MACTRL/co-evolução em MARL — **não** lacunas de agentic AI (benchmarking/threat models/governança/observabilidade/alinhamento).                                                                                          |
|     |                            | **SCORE_RQ**                 |                             | **0.0 / 5.0** |                        | N + N + N + N + N                                                                                                                                                                                                                                            |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                      | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | --------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P11 | Artigo experimental (Deep MARL / transfer learning) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (transfer learning para MARL em MAS de larga escala) e solução (Co-MACTRL: co-evolução + curriculum transfer) explícitos (§I). _Ressalva: não é o problema/solução agêntico(a) da RSL._
- **QA2 = Y** — altamente replicável: paradigma CTSCE, ambiente SMAC/MP-SMAC, sequência de currículo (3m→8m→2s3z→3s5z), ablação de resolução de estado (19×19–55×55; 37×37 ótimo), 7 sementes aleatórias, 8M passos, matriz de avaliação (32 episódios/mapa).
- **QA3 = Y** — validação empírica robusta por **simulação com métricas** (win rates, cenários homogêneos/heterogêneos, baselines) — acima de toy example.
- **QA4 = Y** — conclusões coerentes com os resultados (superioridade/robustez/generalização do Co-MACTRL); trabalho futuro discutido.

## Parecer final do revisor

**Síntese.** P11 é um artigo **intrinsecamente de alta qualidade** (QA 4.0/4, banda Alta): estudo empírico rigoroso de **Deep Multi-Agent Reinforcement Learning** com transfer/curriculum learning (framework Co-MACTRL), validado no StarCraft Multi-Agent Challenge (SMAC/MP-SMAC) com experimentos controlados, múltiplas sementes e métricas de win rate. Contudo, sua **aderência ao escopo da RSL é nula** (SCORE_RQ 0.0/5): não há **Agentic AI baseada em LLM**, autonomia agêntica, uso de ferramentas/orquestração, nem **Resposta a Incidentes**. É um caso análogo a **P7**: "multi-agent systems" no sentido de MARL/gaming, não no sentido agêntico moderno. A única menção a "transformer" refere-se à arquitetura de rede para representação de estado; "cyber" aparece apenas em referências/biografia.

**Recomendação: EXCLUIR — por não-aderência ao escopo.** Justificativa: apesar de passar (provisoriamente) na elegibilidade formal e de excelente qualidade metodológica, o estudo **não contribui para nenhuma RQ** da RSL sobre "Agentic AI Copilot para Resposta a Incidentes". A banda Alta de QA reflete o mérito intrínseco, não a relevância — critério decisivo. Recomenda-se excluir e revisar os critérios de busca que o capturaram (provável casamento por "multi-agent"/"reinforcement learning").

**Pendências de verificação externa:** (registradas por completude; não alteram a exclusão por escopo)

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
