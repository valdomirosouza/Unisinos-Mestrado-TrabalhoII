# Parecer de avaliação integral — P100

## Identificação e escopo

**Estudo:** Pratinav, Akshay; Kataria, Archana. *AIDR-Cloud: An Agentic AI–Driven Incident Response Framework for Cloud Failures*. IEEE SoutheastCon, 2026, pp. 163–168. DOI: 10.1109/SOUTHEASTCON63549.2026.11476571.

**Fonte analisada:** PDF integral de seis páginas. **Referência da triagem:** `prompt-P100.md`.

**Nota de conformidade:** O prompt não fornece a formulação completa do PICOC, os enunciados formais de QA1–QA4 nem o arquivo `templates/review.md`. Assim, o mapeamento PICOC e a rubrica QA abaixo são explicitamente *operacionais/provisórios* e não substituem uma classificação segundo esses instrumentos originais. As RQs, os PDRs, as bandas e a bibliometria foram transcritos dos insumos fornecidos, sem verificação bibliométrica externa nesta etapa.

## Tabela A — Identificação e PICOC

| Campo | Extração / julgamento fundamentado |
|---|---|
| ID | P100 |
| Título | AIDR-Cloud: An Agentic AI–Driven Incident Response Framework for Cloud Failures |
| Autores | Akshay Pratinav; Archana Kataria |
| Ano / veículo | 2026; IEEE SoutheastCon; conference paper; pp. 163–168 |
| DOI | 10.1109/SOUTHEASTCON63549.2026.11476571 |
| Tipo | Proposta arquitetural com relato de implementação, experimento de injeção de falhas e observação em produção |
| Population (mapeamento operacional) | Sistemas distribuídos cloud-native, Kubernetes multirregional, Kafka, serviços e dados gerenciados; equipes de SRE e operadores de incidentes (seções I, IV–V, pp. 163, 165–167) |
| Intervention (mapeamento operacional) | AIDR-Cloud: percepção de métricas/logs/traces, grafo de conhecimento Neo4j, agentes LLM Detector/Hypothesis/Validator/Planner/Critic e remediação via APIs com políticas (seção III, pp. 164–165) |
| Comparison (empírico, concreto) | SREs experientes com dashboards de observabilidade e runbooks, comparados a AIDR-Cloud em cenários de fault injection; também comparação observacional entre incidentes com e sem auxílio do sistema em produção (seções V.A e V.E, pp. 166–167) |
| Outcomes | MTTD, MTTR, latência de RCA, acurácia de causa/remediação, escalações, esforço manual, custo de tokens e qualidade de postmortems (seção V, pp. 166–167) |
| Context | Incidentes e falhas em operação de nuvem multirregional; resposta automatizada com supervisão humana e guardrails |
| Relevância temática | Alta, sujeita à confirmação contra o PICOC formal não anexado |
| Bibliometria informada | OpenAlex: 1; Crossref: 1; Scopus: 0 (consulta informada de 27/10/2026); nunca somar contagens de fontes distintas |
| Estrato informado | B2 pelo percentil CiteScore/Scopus de 37% da série IEEE SOUTHEASTCON (PDR-0006); SJR não disponível nos insumos |
| Ressalva mandatória | Sim, PDR-0007: B2 fora de A1–A2, em **todo uso** das evidências |

## Tabela B — RQs, pontuação e evidências âncora

| RQ | T/P/N | Nota | Evidência âncora e interpretação |
|---|---|---:|---|
| RQ1 — Contexto/definições e autonomia | T | 1,0 | Seções II–IV, pp. 164–165: planejamento multietapas, ferramentas, memória de trabalho, revisão crítica e três modos de atuação: shadow/assist, execução autônoma de baixo risco e aprovação humana para alto risco. Há operacionalização clara da autonomia no caso de uso, embora não uma taxonomia universal. |
| RQ2 — Engenharia/arquitetura | T | 1,0 | Seção III, pp. 164–165, Fig. 1, e seção IV, p. 165: percepção, cognição, ação, grafo Neo4j, orquestração serverless em Go, observabilidade, execução idempotente, canary, rollback e policy engine. |
| RQ3 — Benefícios e evidências | T | 1,0 | Seção V, pp. 166–167, Tabelas II–III, e conclusão, p. 168: comparação executada com baseline de SREs; MTTD p90 de 30 para 5 min (−83%) e MTTR p90 de 240 para 20 min (−91%) em incidentes reais; conclusão informa redução de ~63% no tempo médio de recuperação, RCA ~3× mais rápida, escalações −65%, acerto de remediação ~70%. **Números reportados sem detalhamento amostral suficiente, testes e ICs efetivamente tabulados**. |
| RQ4 — Desafios/ética e governança | T | 1,0 | Seções III–IV, p. 165, e discussão, pp. 167–168: limites de ações, canaries, rollback automático, aprovação humana, logging e auditoria; dependência da integridade da telemetria e das relações do grafo, falhas inéditas e custo. Segurança adversarial e accountability institucional recebem menos profundidade. |
| RQ5 — Lacunas e futuro | T | 1,0 | Seção VII, p. 168: aprendizado com histórico (RL/RAG), ampliação da taxonomia/grafo, mitigação proativa e compartilhamento interorganizacional de conhecimento. Discussão, p. 168, aponta limitações de cobertura, telemetria e custo. |
| **Total** |  | **5,0/5,0** | **Banda Alta** (≥ 3,0). |

**Cautela interpretativa sobre RQ3:** “T” indica que há evidência diretamente pertinente à questão, e não que as estimativas tenham sido reproduzidas, auditadas ou demonstradas com precisão estatística suficiente. A Tabela III se refere a quantis p90; não deve ser tratada como média de MTTD/MTTR. Os valores da conclusão não devem ser confundidos com aqueles quantis.

## Tabela C — Qualidade metodológica (rubrica operacional provisória)

Como os enunciados oficiais de QA1–QA4 não acompanham o prompt, esta tabela utiliza quatro dimensões convencionais **apenas para apoiar a leitura crítica**. Não a tratar como pontuação oficial da RSL sem confrontar os critérios originais.

| Item operacional | Y/P/N | Nota | Justificativa e âncora |
|---|---|---:|---|
| QA1 — Objetivo e contexto claramente definidos | Y | 1,0 | Problema, arquitetura e cenário cloud-native são explícitos; objetivos de resposta a incidentes e eficiência operacional, pp. 163–165. |
| QA2 — Desenho do método e baseline definidos | P | 0,5 | Há comparador humano concreto, injeção de falhas, condições comparáveis e plano de testes estatísticos; porém faltam número de rodadas, distribuição por cenário, características dos SREs e detalhes operacionais reproduzíveis, p. 166. |
| QA3 — Resultados verificáveis e sustentados por evidências suficientes | P | 0,5 | Tabelas II–III apresentam custos e p90 pré/pós; a seção V diz aplicar bootstrap, testes pareados e power analysis, mas não inclui n por grupo, valores p, intervalos de confiança, tamanhos de efeito numéricos ou tabelas detalhadas. A própria seção V.B indica que números precisos “can be reported”, p. 166; pp. 166–168. |
| QA4 — Limitações e ameaças à validade discutidas | P | 0,5 | Limitações práticas sobre falhas inéditas, dependências fora do grafo, telemetria incompleta e custo são reconhecidas, p. 168; não se apresenta seção estruturada de ameaças à validade, vieses de comparação pré/pós e generalização. |
| **Total provisório** |  | **2,5/4,0** | Interpretação apenas pela rubrica operacional desta revisão. |

## Síntese crítica

**Contribuição principal.** O artigo combina agente detector, gerador de hipóteses, validador, planejador e crítico/governança, com grafo de dependências, observabilidade e camada de ação sujeita a controles. O modelo human-in-the-loop é explicitamente graduado pelo risco, de modo que somente ações de baixo risco podem ser executadas autonomamente.

**Comparison efetivamente executado.** A seção V.A afirma múltiplas execuções independentes por tipo de falha em duas condições: SREs usando dashboards/runbooks e AIDR-Cloud como respondedor primário com supervisão humana. A seção V.E descreve comparação de incidentes reais com e sem participação dos agentes. Isto satisfaz o requisito normativo de comparação com baseline concreto, diferentemente da Tabela I, que é apenas uma comparação conceitual entre abordagens.

**Resultados que podem ser extraídos com segurança como alegações dos autores.** Na Tabela III: p90 de MTTD 30→5 minutos, p90 de MTTR 240→20 minutos; na Tabela II: custo médio estimado de LLM de US$0,079 ± US$0,024 por incidente, com 12.400 ± 3.200 tokens de entrada e 2.800 ± 890 de saída. A conclusão apresenta ~63% de redução em mean recovery time, RCA 3 vezes mais rápida, 65% menos escalações e 70% de remediações corretas. A seção V não publica detalhe suficiente para associar esses quatro valores conclusivos a seus denominadores, cenários e intervalos de incerteza.

**Principais limitações.** O texto informa que conduz análise de poder a priori, intervalos bootstrap e testes estatísticos, mas não disponibiliza valores numéricos centrais de inferência. A frase na seção V.B de que as contagens exatas de rodadas e intervalos “can be reported in tabular form” sugere relato incompleto. Na avaliação em produção, o emprego de cenários heterogêneos e comparação pré/pós demanda controle de fatores de confusão não suficientemente descrito. Não há medida psicométrica direta de carga cognitiva, embora ações manuais e escalações sejam usadas como proxies de esforço. A afirmação de zero ações inseguras não vem acompanhada de exposição total, critérios operacionais verificáveis ou estimativa de incerteza para eventos raros.

**Aplicabilidade à dissertação.** Estudo diretamente relevante para a arquitetura de copilotos de resposta a incidentes, para métricas MTTD/MTTR, para supervisão humana e para desenho de experimentos com fault injection. O uso de proxies operacionais não deve ser traduzido como comprovação de redução da carga cognitiva. Os resultados quantitativos devem ser citados como *reportados pelos autores e insuficientemente auditáveis*, com ressalva de estrato B2 em toda utilização da evidência.

## Parecer e recomendação final

**Elegibilidade temática:** favorável, com ressalva de que o PICOC formal não foi incluído nos insumos recebidos.  
**Comparison:** presente e empírico, com baseline concreto de SREs humanos.  
**RQs:** 5,0/5,0 — Alta.  
**QAs:** 2,5/4,0 — avaliação operacional provisória, não oficial.  
**Estrato:** B2 informado para a série IEEE SOUTHEASTCON, percentil 37%, conforme PDR-0006.  
**Exigência PDR-0007:** ressalva obrigatória de estrato em todos os usos de evidência.

**Recomendação: Incluir c/ ressalvas (estrato B2 obrigatório, PDR-0006/0007; relato estatístico incompleto e limites de reprodutibilidade).**

O estudo deve contribuir sobretudo como fonte de mecanismos arquiteturais e hipóteses empíricas pertinentes. As magnitudes de benefício, embora promissoras, não devem ser tratadas como estimativas definitivamente validadas. A decisão final permanece condicionada à confirmação do PICOC completo e dos critérios QA oficiais da RSL.
