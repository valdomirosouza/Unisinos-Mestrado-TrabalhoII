# Avaliação do artigo P85

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura (ciclo 2)  
**ID:** P85  
**Título:** Thermographic and cognitive assessment of fatigue in vessel traffic service operators: a socio-technical approach  
**Autores:** F. Crestelo Moreno; J. Roca González; J. Suardíaz Muro; R. López-Alonso  
**Fonte exclusiva:** PDF disponibilizado do artigo, *Cognition, Technology & Work* (2025), 27:417–448.  
**DOI:** https://doi.org/10.1007/s10111-025-00804-x

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P85 | Cognition, Technology & Work | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado no prompt, não comprovado no PDF) | [VERIFICAR] (A1 informado no prompt, não comprovado no PDF) | Estudo empírico observacional em campo, multimodal, com abordagem sociotécnica | 10.1007/s10111-025-00804-x |

**Evidência:** cabeçalho e resumo, p. 417; seções 4–5, pp. 422–434. O PDF apresenta 23 operadores de dois centros espanhóis, monitoramento termográfico, questionários e análises estatísticas. O quartil SJR e o estrato Qualis são metadados **informados pelo prompt**, não confirmáveis no PDF.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / pendência |
|---|---|---|
| Ano ≥ 2020 | Atendido | 2025, p. 417 |
| Veículo de publicação identificável | Atendido | *Cognition, Technology & Work*, volume 27, pp. 417–448, p. 417 |
| Citações ≥ 1 | [VERIFICAR] | A contagem de citações não consta no PDF; consultar uma base indexadora |
| SJR Q1–Q2 | [VERIFICAR] | Q1 fornecido no prompt, sem validação documental; consultar SCImago Journal Rank |
| Qualis A1–A2 | [VERIFICAR] | A1 fornecido no prompt, sem validação documental; consultar Plataforma Sucupira / Qualis CAPES |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações, quartil SJR e Qualis). A triagem temática foi indicada como aprovada no prompt, mas isso não equivale a evidência de pesquisa sobre Agentic AI. Conforme a instrução, a extração segue em caráter condicional.

## Etapa 2 — Classificação das questões de pesquisa

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P85 | Thermographic and cognitive assessment of fatigue in vessel traffic service operators: a socio-technical approach | RQ1 — Context Definitions | Não tem conteúdo suficiente | N (0,0) | §§ 1, 4.3, pp. 417–426 | Não define autonomia agêntica, planejamento, memória, uso de ferramentas por agentes ou modelo de decisão humano-agente. A tomada de decisão humana em centro de controle não constitui, por si, Agentic AI. |
| P85 | Mesmo artigo | RQ2 — Engineering Architecture | Não tem conteúdo suficiente | N (0,0) | §§ 3.1, 4.3.1–4.3.2, pp. 420–426 | FLIR E60, FLIR ThermaCAM Researcher e YOLO5Face compõem um processo de captura e análise termográfica, não uma arquitetura de agentes com orquestração, memória, ferramentas autônomas, guardrails ou observabilidade de sistemas agênticos. |
| P85 | Mesmo artigo | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | Resumo, p. 417; §§ 5.1–5.4, pp. 427–431; § 6, pp. 434–435 | Oferece evidência empírica e métricas de carga cognitiva/fadiga em operação crítica: 23 operadores, associação inversa da temperatura nasal com a carga mental (r = −0,78; p < 0,01), incremento de 15% no Borg RPE no turno noturno e resultados da escala IWS. Não mede redução de MTTD, MTTR, tempo de resposta a incidentes, precisão de decisão auxiliada por IA ou benefício de copiloto. |
| P85 | Mesmo artigo | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | §§ 2.1, 4.3.2, pp. 419–426; § 6, p. 435 | Discute robustez de medições fisiológicas (temperatura, umidade, emissividade, variabilidade individual, oclusões, faces múltiplas) e representatividade do conjunto de treinamento; relata aprovação ética (§ 4.4, p. 427). Não estabelece governança, accountability ou mecanismos de segurança para agentes autônomos. |
| P85 | Mesmo artigo | RQ5 — Research Gaps | Parcialmente Respondida | P (0,5) | §§ 6–7, pp. 435 | Propõe replicação em outros centros, ampliação e diversificação de amostras, refinamento da detecção termográfica, integração a sistemas de gestão de segurança e avaliação de custo-benefício/efeitos de longo prazo. São lacunas transferíveis à avaliação de fatores humanos, não lacunas específicas de Agentic AI. |
| **P85** | **SCORE_RQ total** | **RQ1–RQ5** | **1,5 / 5,0** | **N + N + P + P + P** | **Síntese das evidências acima** | **Aderência indireta; concentração em carga cognitiva e fadiga humana.** |

**Interpretação:** pontuações parciais nas RQ3–RQ5 indicam apenas que há subdimensões genericamente aproveitáveis para o escopo da RSL. Não comprovam eficácia ou segurança de agentes de IA.

## Etapa 3 — Avaliação de qualidade metodológica

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---:|---|
| P85 | Estudo empírico observacional em campo, com análise termográfica e instrumentos psicométricos | P (0,5) | P (0,5) | Y (1,0) | P (0,5) | **2,5 / 4,0** | **Média** |

**QA1 — Objetivos claros: P (0,5).** O objetivo de identificar fadiga e carga cognitiva mediante termografia e autorrelatos é explícito (resumo, p. 417; § 1, pp. 417–418). Entretanto, a rubrica específica da RSL exige problema e solução **agêntica**: nenhum agente ou copiloto é proposto. A avaliação de clareza do estudo isoladamente poderia ser mais favorável; a pontuação reflete a rubrica pedida.

**QA2 — Metodologia replicável: P (0,5).** Há descrição de participantes (n = 23), turnos, equipamento FLIR E60, emissividade 0,98, YOLO5Face adaptado a imagens térmicas, dataset TFW, filtros de média móvel de cinco minutos, questionários e testes estatísticos (§§ 3–4, pp. 420–427). Contudo, há informações que exigem esclarecimento: a § 2.1.2 menciona distância mínima de dois metros (p. 420), enquanto §§ 4.3.2 e 4.4 informam posicionamento de 90 cm (pp. 425–426); a câmera é especificada a 60 Hz na § 3.1 (p. 420), mas o processamento menciona 7,5 fps (§ 4.3.2, p. 425), sem reconciliação explícita; a Tabela 4 soma 242 horas (112 + 70 + 60), enquanto o resumo apresenta 200 horas e a § 4.2 diz “over 200 hours” (pp. 417, 424). Tais pontos não invalidam automaticamente os achados, mas reduzem a clareza de reprodução independente.

**QA3 — Base de evidências sólidas: Y (1,0).** Trata-se de coleta no ambiente operacional de dois Maritime Rescue Coordination Centers, com 23 participantes, avaliações pré/pós-turno e monitoramento termográfico, além de regressão, testes t, ANOVA, correlações e tamanhos de efeito (§§ 4–5, pp. 422–434). Exemplo: associação entre temperatura nasal e carga de trabalho r = −0,78, p < 0,01 (§ 5.2, p. 428). É validação empírica do **monitoramento de fadiga**, não de uma solução agêntica.

**QA4 — Conclusões coerentes: P (0,5).** A § 6 reconhece limitações de variáveis ambientais, variabilidade fisiológica e diversidade demográfica do dataset; § 7 recomenda replicação e estudos adicionais (p. 435). A coerência geral é aceitável, mas a redação sobre indicador “confiável em tempo real” e integração operacional deve ser interpretada como **potencial evidenciado em campo** e não validação de impacto causal, sensibilidade/especificidade de detecção de fadiga ou desempenho de uma intervenção automatizada. A abordagem é observacional e não testa um copiloto.

### Notas de cautela na interpretação

- As associações relatadas não demonstram causalidade, nem medem o efeito de IA sobre o desempenho de operadores.
- O YOLO5Face foi utilizado para localizar pontos faciais e extrair temperatura de gravações **em pós-análise** (§§ 4.3.1–4.3.2, pp. 424–425). O fato de o monitoramento ser contínuo não implica inferência autônoma em produção ou intervenção automática em tempo real.
- A acurácia média de 97% mencionada na § 4.3.1 refere-se a resultados anteriores do modelo no dataset TFW, e não a uma acurácia de classificação de fadiga aferida neste estudo (pp. 424–425).
- A comparação de temperaturas de 200 pontos anotados manualmente com 8.000 pontos detectados automaticamente resultou em desvio informado inferior a 0,1 °C (§ 4.3.1, p. 425); isso é verificação de medição/localização, não métrica de reconhecimento de fadiga.
- A Tabela 6 registra variação média de Borg RPE pré/pós de +1,1 no turno da manhã, +0,7 à tarde e +1,5 à noite (p. 429). A diferença entre turnos não deve ser confundida com avaliação de um sistema agêntico.

## Parecer final do revisor

**Síntese.** O P85 apresenta evidência empírica pertinente para caracterizar fadiga e carga cognitiva em operadores humanos que atuam em ambientes críticos e contínuos. Sua principal contribuição potencial à RSL é fundamentar a necessidade de suporte à decisão sensível à carga mental, embora a pesquisa seja conduzida em domínio marítimo, não em TI ou resposta a incidentes cibernéticos. O estudo não implementa nem avalia Agentic AI e, portanto, não responde diretamente às RQ1 e RQ2. A relevância para RQ3, RQ4 e RQ5 é contextual e deve permanecer explicitamente distinta da evidência sobre copilotos agênticos.

**Recomendação: INCLUIR COM RESSALVAS**, **exclusivamente** como evidência complementar do cluster *carga cognitiva/fadiga em operação crítica 24/7*, condicionada à confirmação externa da elegibilidade bibliométrica e à existência, no protocolo da RSL, de uma categoria para estudos de fatores humanos sem implementação de Agentic AI. Não utilizar P85 para atribuir benefícios quantitativos, arquitetura, autonomia ou segurança a copilotos de resposta a incidentes. Se os critérios formais de inclusão exigirem necessariamente um sistema de IA agêntica ou um cenário de incident response de TI, a decisão aplicável ao corpus principal será **EXCLUIR**, mantendo o artigo apenas como referência contextual.

**Pendências de verificação externa:** (1) ao menos uma citação, em base indexadora; (2) SJR Q1 no SCImago Journal Rank; (3) Qualis A1 na Plataforma Sucupira / Qualis CAPES e sua aplicabilidade ao período/área definidos na RSL. Os valores Q1 e A1 foram fornecidos como metadados pelo prompt, mas não foram verificados fora do PDF por respeito à regra de fonte exclusiva.

**Resultados consolidados:** SCORE_RQ **1,5/5,0**; SCORE_QA **2,5/4,0 (Média)**; **elegibilidade bibliométrica pendente**; recomendação **INCLUIR COM RESSALVAS (uso contextual)**.
