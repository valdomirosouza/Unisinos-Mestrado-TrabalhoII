# Avaliação crítica do estudo P53 — Ciclo 2 da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P53  
**Estudo:** Pedroso et al., *Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks*  
**Fonte da análise:** exclusivamente o artigo PDF fornecido.  
**Nota metodológica:** Os critérios QA1–QA4 e as RQs são os definidos no prompt-P53. Não se pressupõe que um detector de anomalias baseado em LLM seja, por si só, um agente autônomo.

## Etapa 0 — Tabela A: Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P53 | IEEE Access, vol. 13 | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado na triagem) | [VERIFICAR] (A1 informado na triagem) | Pesquisa aplicada com protótipo e avaliação experimental em ambiente cloud-native simulado | 10.1109/ACCESS.2025.3565220 |

**Evidência:** folha de rosto, p. 1 (identificação do periódico, ano e DOI); seções III–VI, pp. 5–13 (ambiente, arquitetura e avaliação). O estrato e o quartil fornecidos no prompt são dados da triagem, mas não são verificáveis no artigo e, portanto, não são aqui tratados como confirmados.

## Etapa 1 — Elegibilidade

| Critério | Evidência e situação |
|---|---|
| Ano ≥ 2020 | **Atendido:** publicação em 2025 (p. 1). |
| Publicação identificável | **Atendido:** IEEE Access, volume 13 (p. 1). |
| Citações ≥ 1 | **[VERIFICAR]:** contagem não documentada no artigo; consultar base indexadora. |
| SJR Q1–Q2 | **[VERIFICAR]:** Q1 consta da triagem, não do PDF; consultar SCImago Journal Rank, com o ano de referência pertinente. |
| Qualis A1–A2 | **[VERIFICAR]:** A1 consta da triagem, não do PDF; consultar Plataforma Sucupira/Qualis CAPES e enquadramento pertinente. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações, SJR e Qualis). Prossegue-se à extração completa, conforme a regra expressa no protocolo. A ressalva PICOC de *Comparison N/A* permanece registrada: há contraste conceitual com trabalhos anteriores, mas não um comparador experimental controlado que sustente afirmações de superioridade sobre baselines.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P53 | Pedroso et al. (2025) | RQ1 — Context Definitions | Não tem conteúdo suficiente | **N (0,0)** | Seções IV–V, pp. 5–11: pipeline de detecção e inferência; não há definição de Agentic AI ou níveis de autonomia. | **a) Autonomia:** não definida como propriedade agêntica. **b) Características:** há LLM e inferência, mas não descrição de planejamento, memória ou ciclo de ação de agente. **c) Decisão:** Baynet calcula probabilidades para apoio ao diagnóstico, sem explicitar modelo decisório autônomo nem supervisão humana estruturada. Trata-se de automação analítica, não evidência direta da caracterização de Agentic AI. |
| P53 | Pedroso et al. (2025) | RQ2 — Engineering Architecture | Parcialmente Respondida | **P (0,5)** | Seções IV–V, pp. 5–11; Figuras 3, 5 e 11; análise de traces e Baynet. | **a) Arquitetura:** MAIA integra detecção por LLM e análise probabilística de dependências. **b) Ferramentas:** AWS EKS, Kubernetes, Istio/Envoy, Loki, S3, Llama-3 8B, modelo de similaridade de sentenças, Tempo, pgmpy, SQS, Redis, Grafana, Locust e Chaos Mesh. **c) Capacidades:** observabilidade multimodal (logs e traces) e ajuste dinâmico de pesos/relações; não há descrição explícita de memória agêntica, guardrails, planejamento ou orquestração de agentes. |
| P53 | Pedroso et al. (2025) | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | Seção VI, pp. 11–13, Figuras 16–19; seção V, pp. 7–10. | **a) Benefícios qualitativos:** detecção de anomalias e visualização de prováveis pontos de falha e dependências. **b) Evidências quantitativas:** acurácia, precisão, recall, F1 e probabilidades de falha. No cenário Mongo IO Failure: recall 0,71, acurácia 0,78 e F1 0,83; exemplo Baynet: shipping 78% e orders 12,16% de probabilidade de falha. **c) Nível de evidência:** experimento com falhas injetadas em Sock Shop, sem validação de redução de MTTD, MTTR, carga cognitiva ou qualidade decisória de operadores. |
| P53 | Pedroso et al. (2025) | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | Seção II-A, pp. 3–5; seções V–VI, pp. 7–12; seção VII, pp. 13–14. | **a) Desafios técnicos:** falsos positivos, falsos negativos, sensibilidade ao limiar, possível overfitting e dificuldade com sinais numéricos nos logs. **b) Ética/governança:** o artigo menciona governança e controle de custos da plataforma experimental, sem discussão desenvolvida de accountability, privacidade, segurança de agentes ou responsabilidade por decisões. **c) Mecanismos:** teste controlado, pipeline e acompanhamento operacional; não se apresenta uma arquitetura de governança de Agentic AI ou política explícita de aprovação humana. |
| P53 | Pedroso et al. (2025) | RQ5 — Research Gaps | Parcialmente Respondida | **P (0,5)** | Seção VI, pp. 11–13; seção VII, pp. 13–14. | São propostas validação de resultados perfeitos para evitar overfitting, ampliação do mapeamento das relações entre erros, experimentos sistemáticos, aperfeiçoamento do treinamento e investigação de LSTM para valores numéricos. As lacunas são concretas para AIOps/RCA, mas não tratam diretamente de threat models, governança, alinhamento e avaliação de autonomia agêntica. |
| **P53** | **TOTAL** | **SCORE_RQ** | **Aderência parcial à RSL** | **2,0 / 5,0** | **RQ1=0; RQ2=0,5; RQ3=0,5; RQ4=0,5; RQ5=0,5** | **Contribuição de base técnica e empírica para um copilot; não comprovação de um sistema agentic completo.** |

### Justificativa adicional das RQs

O trabalho distingue-se pela combinação de previsão de logs, similaridade semântica e inferência bayesiana condicionada a informações de rastreamento distribuído. O modelo fine-tuned Llama-3 8B utiliza uma sequência de 10 logs prévios para prever a próxima mensagem e assinala anomalias quando a similaridade cosseno fica abaixo de 0,8 (seção V-A, pp. 7–9). Após a detecção, Baynet utiliza relações de serviços e traces para estimar probabilidades de falha (seção V-B, pp. 10–11). Isso é pertinente como *subsistema* de diagnóstico ou fonte de evidência para um copilot de resposta a incidentes, sem demonstrar capacidades agênticas fim a fim.

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P53 | Pesquisa aplicada, protótipo e experimentação com injeção de falhas | **P (0,5)** | **P (0,5)** | **Y (1,0)** | **P (0,5)** | **2,5 / 4,0** | **Média** |

**QA1 — Objetivos claros: P (0,5).** O problema de análise de logs, alertas e identificação de causa-raiz e a solução de detecção por LLM com inferência bayesiana são claramente apresentados (resumo e introdução, pp. 1–2; seção IV, pp. 5–6). A rubrica da RSL também requer explicitação da solução **agêntica**; o artigo não demonstra um agente com planejamento, ações e supervisão humana, justificando a pontuação parcial.

**QA2 — Metodologia replicável: P (0,5).** A arquitetura MAIA, o benchmark Sock Shop com 12 microsserviços, Locust, Chaos Mesh, fluxo de treinamento, Llama-3 8B, sequência de 10 logs, limiar 0,8 e arquitetura Baynet são descritos (seções IV–V, pp. 5–11; Tabela 3; Figuras 3–6 e 11). Apesar disso, o PDF não fornece detalhamento completo necessário à replicação exata do fine-tuning, versões/configurações e construção integral das probabilidades condicionais; há ainda dependência de uma amostra rotulada manualmente (~10%, p. 10), cujo procedimento de amostragem/rotulagem não é suficientemente aprofundado.

**QA3 — Base de evidências sólidas: Y (1,0).** Há experimento controlado em aplicação distribuída com 12 microsserviços, cargas produzidas por Locust, perturbações introduzidas via Chaos Mesh (Tabela 3, p. 8) e avaliação quantitativa dos classificadores por acurácia, precisão, recall e F1 (seção VI, pp. 11–12; Figuras 16–17), além de exemplos probabilísticos da rede bayesiana (Figuras 18–19, pp. 12–13). A pontuação indica **existência de validação empírica com métricas**, não validação industrial de um agente autônomo ou de métricas de resposta operacional.

**QA4 — Conclusões coerentes: P (0,5).** O artigo discute fragilidades de recall, suspeita de overfitting, trade-off de falsos positivos/negativos e próximos experimentos (seções VI–VII, pp. 11–14). Porém, a alegação ampla do resumo de identificação de todos os eventos de erro sem perdas conflita com o cenário Mongo IO Failure, cujo recall é 0,71, e com a identificação explícita de falsos negativos na seção VI. Os resultados sustentam potencial técnico, mas não alegações irrestritas de detecção perfeita ou melhoria medida de eficiência de resposta a incidentes.

## Parecer final do revisor

**Síntese.** O artigo P53 apresenta evidência experimental pertinente à detecção de anomalias e à análise probabilística de causas-raiz em aplicações cloud-native, integrando LLM, logs, traces e dependências de microsserviços. A contribuição mais forte à RSL está na arquitetura de observabilidade/diagnóstico e na avaliação de classificadores em cenários de falhas injetadas. Em contrapartida, não há definição ou avaliação de capacidades agênticas, nem medição de MTTD, MTTR, carga operacional ou tomada de decisão apoiada por agente. Há limitações de reprodutibilidade e inconsistência entre a narrativa do resumo e resultados de recall da seção VI.

**Recomendação: INCLUIR COM RESSALVAS**, **condicionada à confirmação dos critérios bibliométricos**. Classificar o P53 como estudo de **AIOps/RCA baseado em LLM e redes bayesianas, com relevância indireta à arquitetura de copilotos agênticos**, e não como evidência de autonomia de Agentic AI. Manter *Comparison: N/A* na extração PICOC com contraste conceitual, sem assumir comparação experimental controlada. Não usar o estudo como evidência de ganho de MTTD/MTTR.

**Pendências de verificação externa:**

1. **Citações ≥ 1:** verificar em base indexadora (Scopus, Web of Science ou outra adotada pela RSL) e registrar data de consulta.
2. **SJR Q1–Q2:** conferir no **SCImago Journal Rank**, com ano e categoria compatíveis com o protocolo; a indicação Q1 do prompt ainda não está corroborada pelo PDF.
3. **Qualis A1–A2:** conferir na **Plataforma Sucupira / Qualis CAPES**, de acordo com o enquadramento oficial aplicável; a indicação A1/percentil Scopus no prompt ainda não está corroborada pelo PDF.

**Resultado consolidado:** SCORE_RQ **2,0/5,0**; SCORE_QA **2,5/4,0**; banda **Média**; **elegibilidade pendente** e **inclusão recomendada com ressalvas**.
