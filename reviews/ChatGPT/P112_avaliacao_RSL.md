# Parecer acadêmico P112

**Estudo:** Bilal, M.; Crowcroft, J.; Wang, R.; Xu, X.; Dustdar, S. *Large Language Models for Agentic NetOps and AIOps: Architectures, Evaluation, and Safety* (2026).

**Veículo/DOI informados no protocolo:** Computer Science Review; 10.1016/j.cosrev.2026.101075. **Estrato informado:** Qualis A1 (percentil Scopus 98%). **Citações informadas na triagem (27/10/2026):** OpenAlex 0; Crossref 0; Scopus 0 (fontes independentes, não somáveis). A capa do PDF também indica arXiv:2605.12729v2, 15/06/2026; a correspondência com versão editorial é tomada como dado do protocolo, sem verificação bibliográfica independente.

## Tabela A — Identificação e PICOC

| Dimensão | Extração e decisão |
|---|---|
| Tipo de estudo | Revisão estruturada/survey, estudo secundário; corpus declarado de 181 registros: 159 artigos avaliados por pares, 9 preprints e 13 documentos técnicos/normativos. Seção I-C, pp. 4–5. |
| Population | Operações de rede, TI, sistemas em nuvem e serviços distribuídos; SRE e equipes que lidam com incidentes. Seções I e II, pp. 2 e 8–12. |
| Intervention | Sistemas agentic baseados em LLM, com recuperação de evidências, planejamento, uso de ferramentas, gradações de autonomia, verificação externa e controle de execução. Seções III–IV, pp. 13–20. |
| Comparison | Não identificado experimento próprio contra baseline concreto. Comparações entre classes de estudos e propostas são analíticas, não ensaios empíricos realizados pelos autores. |
| Outcomes | Taxonomia e arquitetura; critérios de segurança, auditabilidade e benchmarking; proxies recomendados de MTTD/MTTR, RCA@k, risco, latência e custos. Seção VII, pp. 29–35. Não são reduções próprias empiricamente demonstradas. |
| Context | NetOps, AIOps, SRE, troubleshooting, incident response, RCA, mitigação e self-healing limitado. Seções II e VI, pp. 8–12 e 25–28. |
| Elegibilidade temática | Elegível: aderência elevada ao PICOC, como evidência secundária/teórica. |

## Tabela B — RQ1–RQ5

| Questão | T/P/N | Pontos | Âncora e justificativa |
|---|---|---:|---|
| RQ1 | T | 1,0 | Seção I-B, pp. 3–4; seção IV-A/B e Tabela III, pp. 16–18. Define agentes por estado, ferramentas, planos e aprovação; quatro níveis: copilot, analyst, planner–executor e closed-loop. Formaliza o contrato Ck=(Tk,Rk,Gk,Uk,Bk). |
| RQ2 | T | 1,0 | Seção III, pp. 13–15; seção IV-C/D, pp. 18–19; Figuras 4 e 6. Arquitetura de ferramentas tipadas, recuperação com proveniência e atualização, limites de custos, *verification wall*, aprovações, canários e rollback. |
| RQ3 | P | 0,5 | Seção VII e Tabela VI, pp. 29–35, particularmente p. 32. Sistematiza avaliação com MTTD/MTTR proxies, RCA@k, latência, custo e violações; não executa experimento próprio com baseline e não demonstra magnitude de redução de carga cognitiva. |
| RQ4 | T | 1,0 | Seção VIII e Tabela VII, pp. 35–39. Discute prompt injection, evidence/telemetry poisoning, excesso de agência, privacidade, privilégio mínimo e auditoria. |
| RQ5 | T | 1,0 | Seção IX e Tabela VIII, pp. 39–42. Lacunas sobre avaliação realista/reprodutível, segurança composicional, causalidade com LLM, padronização, integração humana, drift e custos. |
| **Total** | | **4,5/5** | **Alta (≥3,0).** |

## Tabela C — QA1–QA4

**Nota metodológica:** O arquivo do prompt especifica a escala QA1–QA4, mas não define os enunciados dos quatro critérios. Para evitar atribuir definições inexistentes ao protocolo, os itens abaixo são *operacionalizações provisórias* que exigem confronto com a rubrica oficial.

| Critério operacional provisório | Y/P/N | Pontos | Justificativa |
|---|---|---:|---|
| QA1 — Clareza dos objetivos | Y | 1,0 | Objetivos e contribuições explicitados em I-B e I-E, pp. 3–7. |
| QA2 — Transparência e reprodutibilidade do método | P | 0,5 | I-C, pp. 4–5: fontes, período 2020–maio/2026, triagem em dois estágios, critérios, snowballing e 181 documentos; não apresenta todos os totais de busca e exclusão por etapa. |
| QA3 — Fundamentação da síntese | Y | 1,0 | Taxonomia operacional, quadro de sistemas, matrizes de métricas/ameaças e referências, seções IV e VII–IX. Pontua qualidade de síntese, não validação experimental própria. |
| QA4 — Reconhecimento de limitações | Y | 1,0 | Seção I-C, p. 5 e IX, pp. 39–42: pouca publicidade de sistemas industriais, evidência desigual, rápida mudança tecnológica e desafios de benchmark. |
| **Total provisório** | | **3,5/4** | **Alta, dependente da rubrica QA oficial.** |

## Síntese crítica e relevância para a dissertação

O principal aporte é a transição de uma visão de *agentes que respondem* para *agentes que operam sob contratos auditáveis*. A escada de autonomia, a separação **read–propose–execute**, os rastros de evidência e as barreiras de verificação permitem justificar uma arquitetura de copiloto SRE com ação mediada por políticas e supervisão humana. A Tabela III (p. 18) descreve obrigações específicas por nível de autonomia; a Figura 6 (p. 19) transforma a revisão humana em um pacote verificável de alterações, pré-condições, controles, canário, rollback e vínculos às evidências.

A Tabela VI (p. 32) é valiosa para definir instrumentos de medição: MTTD proxy é o tempo até o primeiro sinal correto de triagem ou consulta discriminante; MTTR proxy é o tempo até mitigação verificada em sandbox/replay ou plano aprovado em cenário supervisionado. Esses *proxies* não devem ser tratados automaticamente como MTTD/MTTR medidos em produção. Para a carga cognitiva, o texto discute fatores humanos e esforço operacional (IX-F, p. 41), mas não estabelece uma redução causal quantificada em estudo próprio.

A recomendação para uso é **base teórica/arquitetural e orientação do desenho de avaliação**, com posterior triangulação de cada alegação de eficácia com estudos primários controlados. O survey não deve ser contabilizado como experimento que comprova melhora de MTTD, MTTR ou sobrecarga cognitiva.

## Restrições e PDR

- **PDR-0006:** não incide como regra de exclusão para conference paper, pois o veículo informado é journal.
- **PDR-0007:** não exige ressalva de estrato quando se aceita a classificação A1 informada; não se fez aferição bibliométrica independente neste parecer.
- **Comparison:** não preenchido como comparação empírica, pois faltam intervenção e baseline concretos executados no estudo.
- **Tipo de evidência:** secundária; a eventual designação *fundacional-condicional* requer o registro e as condições da regra R1 no protocolo completo, não fornecido no prompt.

## Recomendação final

**Incluir c/ ressalvas (estudo secundário de caráter fundacional-condicional, adequado para fundamentação conceitual, arquitetural e metodológica; não utilizar como evidência empírica primária de redução de MTTD, MTTR ou carga cognitiva; enquadramento fundacional condicionado à regra R1 do protocolo).**
