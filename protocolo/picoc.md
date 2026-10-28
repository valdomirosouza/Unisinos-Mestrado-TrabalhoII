# PICOC — Agentic AI as a Copilot to Reduce MTTD and MTTR During Incident Response

> Delimitação ratificada da revisão (prompt de extração vivo em
> [`../picoc/picoc-extraction-prompt.md`](../picoc/picoc-extraction-prompt.md), v1.3.0).

| Elemento         | Definição                                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Population**   | Sistemas de software complexos e os times que os operam (SRE, NOC, SOC); microsserviços; pipelines de IT operations.                                                                                       |
| **Intervention** | Agentic AI como copilot ou agente autônomo: agentes baseados em LLM, sistemas multiagente, LLM4AIOps, o loop perceive–reason–act–learn.                                                                    |
| **Comparison**   | Automação tradicional, AIOps não-agêntico ou baselines humanos — _declarado somente com baseline empírico executado_ ([PDR-0001](pdr/PDR-0001-comparison-somente-com-baseline-empirico.md), regra v1.1.0). |
| **Outcomes**     | MTTD, MTTR, observabilidade, acurácia de detecção, alert fatigue e carga cognitiva do operador (outcome complementar).                                                                                     |
| **Context**      | O ciclo de vida de incident response em IT operations e cibersegurança; supervisão HITL/HOTL; produção vs. simulação.                                                                                      |

## String de busca

Dois blocos obrigatórios — _Intervention_ (agentic AI, LLM agents, multi-agent
systems, AIOps copilots) AND _Context/Population_ (incident response, IT
operations, SRE/NOC/SOC, observability) — com _Outcomes_ deliberadamente
opcional (apenas 1 de 38 estudos de calibração nomeava MTTD/MTTR nos
metadados). Validada por execução real: OpenAlex ≈ 49.700 registros e Scopus
Search API 12.783 (2020+, EN), recall 13/14 do conjunto de calibração em ambas
as bases, com a mesma perda única (P24 — recuperado por snowballing, que é
obrigatório no protocolo).

**String canônica, calibração e trade-offs:**
[`../picoc/picoc-search-string.md`](../picoc/picoc-search-string.md) (fonte de
verdade — não duplicar aqui).
