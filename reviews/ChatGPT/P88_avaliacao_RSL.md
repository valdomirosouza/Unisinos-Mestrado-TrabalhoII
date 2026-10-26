# Avaliação do Artigo P88

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura — ciclo 2  
**Título:** A Decentralised Self-Healing Approach for Network Topology Maintenance  
**Autores:** Arles Rodríguez, Jonatan Gómez e Ada Diaconescu  
**Fonte primária:** PDF anexado, 36 páginas. Todas as evidências técnicas abaixo provêm exclusivamente desse PDF.

## Tabela A — Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P88 | *Autonomous Agents and Multi-Agent Systems*, 35:6 | 2021 | [VERIFICAR] | [VERIFICAR] (Q2 informado na triagem) | [VERIFICAR] (A2 informado na triagem) | Proposta de sistema multiagente descentralizado com avaliação quantitativa por simulação comparativa | https://doi.org/10.1007/s10458-020-09486-3 |

**Base documental:** cabeçalho e resumo, p. 1; métodos, §§3–4, pp. 6–18; resultados, §5, pp. 18–33. Publicação online em 27/11/2020; identificação bibliográfica do periódico como **2021**, volume 35, artigo 6 (p. 1). Não confundir a data online de 2020 com o ano do volume usado na tabela.

## Etapa 1 — Triagem de elegibilidade

| Critério | Evidência / julgamento |
|---|---|
| Ano ≥ 2020 | **Atendido**: 2021 no cabeçalho, p. 1. |
| Veículo identificável | **Atendido**: periódico identificado, p. 1. |
| Citações ≥ 1 | **[VERIFICAR]**: nenhuma contagem atual verificável no PDF. |
| SJR Q1–Q2 | **[VERIFICAR]**: Q2 é informação fornecida no protocolo de triagem, não demonstrada pelo PDF. |
| Qualis A1–A2 | **[VERIFICAR]**: A2 é informação fornecida no protocolo, não demonstrada pelo PDF. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, quartil SJR, estrato Qualis)**. A extração prossegue porque o protocolo autoriza avaliar artigos com elegibilidade pendente. A pré-triagem informa *agêntico não-LLM, multi-agent systems/self-healing, simulação*; a leitura do PDF confirma essas características, sem estabelecer aplicação de LLMs.

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P88 | A Decentralised Self-Healing Approach for Network Topology Maintenance | RQ1 — Context Definitions | Parcialmente Respondida | **P (0,5)** | §§3.2–3.4, pp. 6–9; §§4.3–4.4, pp. 16–18, algoritmos 5–7 | **a)** Autonomia operacional descentralizada é demonstrada por agentes e nós que coletam informações, detectam falhas e restauram topologia sem controlador global. **b)** Memória topológica, troca de mensagens, movimentação e regras locais são explícitas. **c)** Modelo de decisão baseado em regras e comparação do estado observado com memória anterior (incluindo desempate por menor ID), não raciocínio/plano dinâmico de LLM. Não detalha supervisão humana, planejamento cognitivo ou uso de ferramentas típico de copilotos. |
| P88 | A Decentralised Self-Healing Approach for Network Topology Maintenance | RQ2 — Engineering Architecture | Parcialmente Respondida | **P (0,5)** | §§3.2–3.5, pp. 6–12; §§4.2–4.4, pp. 13–18, algoritmos 1–7; nota de código-fonte, p. 7 | **a)** Arquitetura MAS descentralizada com nós-agentes estáticos e agentes móveis. **b)** Detalha Trickle, Random with Marks, memória distribuída e detecção por mensagens/heartbeat; disponibiliza referência ao código da simulação. **c)** Autorrecuperação e redução de mensagens redundantes são mecanismos avançados pertinentes, mas não se descrevem guardrails para LLMs, orquestração de ferramentas externas ou observabilidade de agentes em produção. A execução é simulada numa máquina, não validação em produção. |
| P88 | A Decentralised Self-Healing Approach for Network Topology Maintenance | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | §5.1, pp. 18–20; §5.2, p. 20, tabela 5; §5.4, pp. 22–24, figuras 4–6; §5.5, pp. 24–33, figuras 7 e tabelas 7–9; §6, pp. 33–34 | **a)** Reporta recuperação de topologia e trade-offs entre abordagens. **b)** Mede similaridade de grafos (%), largura de banda (bytes), memória (bytes), quantidade de mensagens e rodadas; repete experimentos 30 vezes. Ex.: no caso AS, mobile agents com k=3 e início precoce das falhas apresentam similaridade mediana de 99,95%, elevada a 100% após ajuste para k=5 (§5.4, pp. 23–24). **c)** Evidência quantitativa experimental, porém inteiramente de simulação. Não mede MTTD, MTTR, carga cognitiva, qualidade da decisão humana ou indicadores de um SOC/IR. |
| P88 | A Decentralised Self-Healing Approach for Network Topology Maintenance | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | §3.3.4, p. 8; §3.4, p. 9; §4.4, p. 18; §5.4, pp. 23–24; §6, pp. 33–34 | **a)** Explicita limitações por falhas simultâneas, conhecimento topológico insuficiente, topologias vulneráveis, necessidade de restauração mais rápida que falhas e peculiaridades da sincronização em simulação; discute replicação única e futura necessidade de lidar com paralelismo. **b)** Não aborda riscos éticos, privacidade, responsabilidade, segurança de IA ou governança organizacional. **c)** Apresenta mecanismos técnicos de consistência e coordenação, não estruturas de governança. |
| P88 | A Decentralised Self-Healing Approach for Network Topology Maintenance | RQ5 — Research Gaps | Parcialmente Respondida | **P (0,5)** | §3.2, p. 6; §4.4, p. 18; §6, pp. 33–34 | Aponta agenda explícita: limitar o alcance em hops dos dados propagados e determinar a vizinhança mínima necessária; estudar escalabilidade com redes de várias ordens de grandeza; aplicar a redes de contêineres e refinar coordenação/eleição. Lacunas relevantes à confiabilidade de automação distribuída, mas não discute benchmarking de LLMs, threat models de agentes generativos, alinhamento, governança ou avaliação de copilotos de IR. |
| **P88** | **TOTAL** | **SCORE_RQ** | **2,5 / 5,0** | **P + P + P + P + P** | **§§3–6** | **Contribuição parcial e indireta para a RSL, com ênfase em mecanismos agênticos não-LLM e resiliência de redes.** |

**Nota de interpretação:** o P88 não é classificado como estudo de *Agentic AI baseado em LLM*. Os julgamentos parciais identificam analogias de engenharia de agentes, sem atribuir ao artigo funcionalidades cognitivas ou resultados operacionais que não foram investigados.

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P88 | Proposição arquitetural multiagente; simulação experimental quantitativa comparativa | **Y (1,0)** | **Y (1,0)** | **Y (1,0)** | **Y (1,0)** | **4,0 / 4,0** | **Alta** |

**QA1 — Objetivos Claros (Y):** resumo, p. 1; §1, pp. 2–4; §3.1, p. 6. O problema de conservar/restabelecer a topologia após falhas é inequívoco; a solução combina coleta distribuída e restauração local via agentes. A clareza metodológica não implica foco em copiloto com LLM.

**QA2 — Metodologia Replicável (Y):** §§3–4, pp. 6–18, algoritmos 1–7; tabelas 1–4, pp. 12, 19–20; §5.1, pp. 18–20. Inclui modelos de agentes, regras de recuperação, tipos de rede, intervalos, parâmetros, indicadores e referência ao código-fonte (p. 7). A simulação usa rodadas sincronizadas, distinguindo-se de uma implantação real distribuída.

**QA3 — Base de Evidências Sólidas (Y):** §§5.1–5.5, pp. 18–33, especialmente tabela 5 e figuras 4–7. Experimentos quantitativos repetidos 30 vezes com seis topologias, inclusive um grafo de 512 nós, e comparação com Trickle, medindo similaridade e sobrecarga. **Escopo da força probatória:** validação simulada, não estudo de caso industrial ou avaliação em produção.

**QA4 — Conclusões Coerentes (Y):** §§5.4–5.5, pp. 22–33; §6, pp. 33–34; hipóteses de §3.4, p. 9. As conclusões de autorrecuperação condicionada e trade-offs de recursos se relacionam aos experimentos; são descritos limites de taxa de falha, dependência topológica e necessidade de futuras avaliações de escalabilidade e em redes de contêineres.

## Parecer final do revisor

**Síntese.** O P88 oferece evidência experimental consistente sobre autonomia distribuída, memória topológica local e reconfiguração automática frente a falhas, com comparação entre agentes móveis e Trickle. Ele contribui principalmente para **RQ1–RQ3** e oferece subsídios técnicos a RQ4 e RQ5. A contribuição é limitada ao nível arquitetural: não utiliza LLM, não caracteriza copilotos e não avalia integração humano-IA ou resposta operacional a incidentes. Sua qualidade metodológica é alta dentro do âmbito de simulação, o que não deve ser confundido com aderência integral ao objeto da RSL.

**Recomendação: INCLUIR COM RESSALVAS.** Manter como estudo complementar de fundamentos de *self-healing* em sistemas multiagentes, claramente identificado como **não-LLM / simulação**. Não utilizá-lo para comprovar ganhos de MTTD, MTTR, redução de carga cognitiva ou segurança de copilotos. Inclusão definitiva condicionada à confirmação dos critérios bibliométricos exigidos no protocolo.

**Pendências de verificação externa:**

1. **Citações [VERIFICAR]:** confirmar ao menos uma citação em base indexadora (por exemplo, Scopus ou Web of Science).
2. **SJR [VERIFICAR]:** confirmar quartil Q1/Q2 e período de referência no *SCImago Journal Rank*; Q2 foi informado no prompt, mas não pode ser comprovado pelo PDF.
3. **Qualis [VERIFICAR]:** confirmar enquadramento A1/A2 e método/quadriênio aplicável na Plataforma Sucupira / Qualis CAPES; A2 e percentil Scopus 76,0% foram fornecidos no prompt, mas não são certificáveis pelo PDF.

**Nota de rastreabilidade:** Tabelas 5–9 citadas nas evidências correspondem às tabelas internas do artigo; não devem ser confundidas com as Tabelas 3, 5 e 7 da RSL. Não foram consultadas fontes externas, em cumprimento ao protocolo.
