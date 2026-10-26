# Avaliação do artigo P79

**Título:** AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation  
**Autores:** Siddhant Srinivas, Brandon Kirk, Julissa Zendejas, Michael Espino, Matthew Boskovich, Abdul Bari, Khalil Dajani e Nabeel Alzahrani  
**Fonte:** *Journal of Cybersecurity and Privacy*, 2025, 5, artigo 95  
**DOI:** https://doi.org/10.3390/jcp5040095  
**Protocolo:** prompt-P79.md, avaliação com base exclusivamente no PDF.

## Etapa 0 — Tabela A: Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P79 | Journal of Cybersecurity and Privacy | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado no prompt, não comprovável pelo PDF) | [VERIFICAR] (A2 informado no prompt, não comprovável pelo PDF) | Revisão sistemática da literatura / survey | 10.3390/jcp5040095 |

**Fontes para verificação externa:** citações em base indexadora (Scopus, Web of Science ou Google Scholar); quartil em *SCImago Journal Rank*; estrato Qualis na Plataforma Sucupira/Qualis CAPES. Valores Q1 e A2 constam nos insumos do protocolo, mas não são tratados como comprovados pelo próprio artigo.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência |
|---|---|---|
| Ano ≥ 2020 | Atende | Publicado em 5 de novembro de 2025 (p. 1). |
| Veículo identificável | Atende | *Journal of Cybersecurity and Privacy*, volume 5, artigo 95 (p. 1). |
| Citações ≥ 1 | [VERIFICAR] | Contagem não consta do PDF. |
| SJR Q1–Q2 | [VERIFICAR] | Q1 foi informado no prompt; requer comprovação independente. |
| Qualis A1–A2 | [VERIFICAR] | A2 foi informado no prompt; requer comprovação independente. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações, quartil SJR e Qualis). A extração prossegue conforme o protocolo, que autoriza avaliação de candidatos pendentes.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P79 | AI-Augmented SOC | RQ1 | Respondida Plenamente | T (1,0) | Seção 1, pp. 1–2; §3.1, p. 5; §4 e Figura 3, p. 12; §4.1, p. 13 | Define autonomia dos níveis 0–4, discute agentes com ferramentas, memória e planejamento e distingue HITL, HoTL e HoOTL, incluindo aprovação humana de ações críticas e delegação de decisões. As características são sintetizadas, não validadas experimentalmente. |
| P79 | AI-Augmented SOC | RQ2 | Parcialmente Respondida | P (0,5) | Tabela 1, p. 4; Figura 2, p. 12; §5.1, p. 15; §5.3, p. 16 | Aborda arquiteturas híbridas e multiagentes, integração com SOAR/EDR/XDR, LangChain, AutoGen e MCP/A2A/ACP, além de RAG e explicabilidade. Não especifica de forma integrada mecanismos implementáveis de memória, guardrails, observabilidade e operação em produção. |
| P79 | AI-Augmented SOC | RQ3 | Respondida Plenamente | T (1,0) | §§3.1–3.8, pp. 5–10; Tabela 2, p. 11; §7, p. 19 | Sintetiza benefícios qualitativos e quantitativos de estudos primários e discute o nível de evidência e seus limites. Exemplos: CyberAlly reduz falsos positivos de 70% para 35% e tempo de resposta de 8 h para 90 min (§3.2, p. 6); TrioXpert apresenta diagnóstico médio em 15 s (§3.5, p. 8). Os resultados não constituem validação experimental própria do survey. |
| P79 | AI-Augmented SOC | RQ4 | Respondida Plenamente | T (1,0) | §4–4.1, pp. 12–13; Tabela 4, pp. 14–15; §§5.1–5.5, pp. 15–17 | Identifica alucinações, prompt injection, envenenamento de memória/dados, privacidade, escalabilidade e dificuldades de interoperabilidade; discute accountability, confiança calibrada, supervisão humana, proveniência, XAI, RAG e mecanismos de governança proporcionais à autonomia. São recomendações conceituais e práticas relatadas, não controles verificados em uma implementação própria. |
| P79 | AI-Augmented SOC | RQ5 | Respondida Plenamente | T (1,0) | §4.2, p. 13; §§5.2–5.5, pp. 16–17; §6, p. 18; §7, p. 19; §8, p. 20 | Explicita lacunas na validação do modelo de maturidade, benchmarks comparáveis, robustez adversarial, generalização, validação em SOC real, interação humano-IA, confiança, auditoria, explicabilidade e privacidade. |
| **P79** | | **SCORE_RQ** | | **4,5 / 5,0** | | **Cobertura de 90% dos pontos possíveis; quatro RQs plenas e uma parcial.** |

### Justificativas complementares das classificações

**RQ1 (a/b/c):** (a) classificação explícita de operações manuais, assistidas, semiautônomas, condicionalmente autônomas e plenamente autônomas no §4, p. 12; (b) uso de ferramentas, memória e planejamento no §3.1, p. 5; (c) diferentes responsabilidades decisórias de analistas e sistemas de IA, incluindo aprovação e governança, no §4 e Figura 3, p. 12.

**RQ2 (a/b/c):** (a) arquiteturas híbridas, fluxo ponta a ponta e coordenação multiagente na Figura 2, p. 12; (b) ferramentas e protocolos de integração no §5.1, p. 15; (c) RAG, XAI, autorreflexão e uso de memória aparecem em passagens específicas, mas sem detalhamento integrado sobre observabilidade e guardrails em produção. Assim, a cobertura é parcial.

**RQ3 (a/b/c):** (a) redução de fadiga de alertas e carga de trabalho e melhoria do apoio a analistas nos §§3.2–3.6; (b) métricas de precisão, recall, F1, falsos positivos e tempos de resposta nas Tabelas 1–2 e §3; (c) o §7, p. 19, diferencia implicitamente a força das evidências ao reconhecer benchmarks, simulações, dados sintéticos e escassez de validações operacionais. Não se deve interpretar os indicadores como uma comparação experimental controlada entre todas as abordagens.

**RQ4 (a/b/c):** (a) dificuldades técnicas nos §§5.1–5.4; (b) riscos socio-técnicos, confiança e responsabilização no §5.5; (c) HITL/HoTL, controles de autonomia, proveniência e explicabilidade nos §§4–4.1. Há recomendações de governança, mas não demonstração de eficácia dos controles.

**RQ5:** lacunas explícitas e agenda futura nos §§6–8, incluindo benchmarks unificados, avaliação longitudinal, segurança, supervisão humana e ensaios em SOCs operacionais.

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P79 | Revisão sistemática / survey | Y (1,0) | P (0,5) | P (0,5) | Y (1,0) | **3,0 / 4,0** | **Alta** |

**QA1 — Y (1,0), objetivos claros.** Resumo e Introdução (pp. 1–2) explicitam problemas de fadiga de alertas, falsos positivos e atrasos na resposta, bem como o objetivo de sintetizar aplicações de LLMs e agentes em oito tarefas de SOC. A taxonomia e o modelo de maturidade constituem contribuições declaradas.

**QA2 — P (0,5), metodologia parcialmente replicável.** O §2 (pp. 2–3) descreve período da busca, fontes bibliográficas, critérios de seleção, triagem e revisão de 105 artigos, com Figura 1 PRISMA. Porém, não apresenta no corpo do PDF uma estratégia integral de busca reproduzível por fonte, e o fluxo não explicita a exclusão dos 25 registros entre os 130 textos completos e os 105 incluídos. Há ainda **contradição interna**: na p. 3 o texto afirma que a revisão não havia sido registrada, mas adiante na mesma página declara pré-registro no OSF com DOI. Esses pontos impedem nota máxima de replicabilidade.

**QA3 — P (0,5), base empírica indireta.** §§3.1–3.8 (pp. 5–10) e Tabela 2 (p. 11) sintetizam estudos com métricas, simulações e aplicações industriais. Contudo, o artigo não descreve um experimento próprio de avaliação da proposta de taxonomia ou do modelo de maturidade. O §4.2 (p. 13) reserva a validação do modelo para trabalho futuro. A heterogeneidade de benchmarks e a dependência de resultados secundários justificam classificação parcial, não ausência completa de evidências.

**QA4 — Y (1,0), conclusões coerentes.** §§7–8 (pp. 19–20) reconhecem viés de seleção, validade ecológica, métricas não homogêneas, obsolescência de baselines e insuficiência de validação de integração humano-IA. A conclusão está alinhada à síntese e ressalta a necessidade de estudos em SOCs reais, sem apresentar autonomia plena como já demonstrada em produção.

## Parecer final do revisor

O P79 possui elevada relevância conceitual para a RSL **Agentic AI Copilot para Resposta a Incidentes**. Consolida estudos sobre triagem, resposta, tratamento de tickets e inteligência de ameaças e organiza um espectro de autonomia humana e agêntica que pode apoiar a fundamentação teórica da pesquisa. Apresenta indicadores operacionais relevantes, mas derivados de estudos primários heterogêneos e não diretamente comparáveis. Sua contribuição é principalmente de síntese, classificação e identificação de lacunas, não de validação arquitetural ou de efetividade do próprio modelo de maturidade.

**Recomendação: INCLUIR COM RESSALVAS**, como estudo fundacional e secundário, condicionado à confirmação dos requisitos bibliométricos de elegibilidade. Não tratar resultados quantitativos citados como métricas obtidas pelos autores do P79 e não contá-lo como experimento primário independente.

### Ressalvas e pendências

1. **[VERIFICAR]** Contagem de citações (mínimo de 1), em base indexadora.
2. **[VERIFICAR]** Quartil SJR Q1–Q2, no SCImago Journal Rank; o Q1 fornecido no prompt não é evidência presente no PDF.
3. **[VERIFICAR]** Qualis A1–A2, na Plataforma Sucupira/Qualis CAPES; o A2 fornecido no prompt não é evidência presente no PDF.
4. **Rastreabilidade interna:** divergência quanto ao pré-registro da revisão na p. 3 e diferença não detalhada entre 130 artigos avaliados na íntegra e 105 incluídos na Figura 1.
5. **Validade da evidência:** ausência de avaliação experimental própria do modelo de maturidade, métricas entre estudos não comparáveis diretamente e limitada validação longitudinal de sistemas em SOC real (pp. 13, 19).

**Síntese para incorporação:** `P79 | SCORE_RQ=4,5 | QA1=Y | QA2=P | QA3=P | QA4=Y | SCORE_QA=3,0 | Banda=Alta | INCLUIR COM RESSALVAS | Elegibilidade bibliométrica pendente`.
