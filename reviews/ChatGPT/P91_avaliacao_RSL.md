# Parecer de avaliação integral — P91

**Estudo:** P91  
**Título:** *Autonomous Agentic AI Architectures for Optimizing Security Operations Centers (SOC) KPIs: Methodology, Impact on Detection, Response, and Recovery*  
**Autores:** Miroslav Stefanov; Kristyan Stefanov; Laxima Niure Kandel; Sean Crouse; Boyan Jekov  
**Fonte:** *Land Forces Academy Review* (*Revista Academiei Forţelor Terestre*), v. XXX, n. 3(119), 2025, pp. 479–493  
**DOI:** 10.2478/raft-2025-0046  
**Tipo:** artigo de periódico; estudo aplicado com implementação e demonstração experimental de arquitetura baseada em agentes  
**Extensão examinada:** PDF integral, 15 páginas (pp. 479–493)  
**Protocolo fornecido:** `prompt-P91.md`  

> **Limitação documental do protocolo:** o prompt menciona um “PICOC abaixo” e o formato `templates/review.md`, mas não contém a tabela formal do PICOC, a definição dos critérios QA1–QA4 nem o arquivo de template. Assim, a Tabela A apresenta o enquadramento **provisório** compatível com as RQs explicitadas, e a Tabela C usa critérios operacionais **declarados aqui**, não supostamente oficiais. A decisão é fundamentada no foco da pesquisa e nas regras expressas do prompt, sujeita a revisão caso o PICOC formal contenha exclusões adicionais.

## Síntese executiva

O artigo propõe uma arquitetura de **dez agentes especializados** para automatizar cálculo, previsão e acionamento de rotinas relacionadas a KPIs de Security Operations Centers (SOC), apoiada por cinco modelos: dois classificadores XGBoost, dois regressores LightGBM e um modelo BERT para sentimento. O estudo processa 214 arquivos CSV, com 25.182.806 registros iniciais e 8.628.160 observações após limpeza (Seção 3.1, p. 481). A evidência é relevante para **agentes orientados a regras e aprendizado de máquina, não para agentes baseados em LLMs**. O uso de BERT para classificação de sentimento não estabelece orquestração por LLM.

O trabalho oferece evidência de implementação funcional, resultados preditivos e execução de regras/playbooks em cenários de teste. **Não apresenta comparação empírica contra baseline operacional concreto** nem demonstra redução observada do tempo real de detecção, resposta ou recuperação antes/depois da adoção. Portanto, métricas reportadas de inferência, valores dos KPIs e acionamento de alertas não devem ser interpretados como efeitos causais de melhoria em SOC de produção.

## Tabela A — Identificação e enquadramento PICOC

| Campo | Extração / avaliação | Evidência |
|---|---|---|
| ID | P91 | Protocolo |
| Ano / idioma | 2025 / inglês | p. 479 |
| Veículo | *Land Forces Academy Review*, periódico | pp. 479, 493 |
| População (P) | Operações de segurança/SOC, equipes de resposta a incidentes e processos de detecção, resposta, recuperação e acompanhamento | Seções 1–2, pp. 480–481 |
| Intervenção (I) | Dez agentes especializados baseados em regras e ML; classificadores XGBoost, regressores LightGBM e classificador de sentimento BERT; disparo de playbooks, notificações e atribuições | Seções 3.2–3.3, pp. 482–484 |
| Comparação (C) | **N/A: não há baseline empírico concreto**. A comparação de desempenho entre os modelos FPR/FNR e entre predições e valores reais não constitui comparação da intervenção agêntica contra um SOC sem intervenção ou outro método baseline | Seções 4.1–4.4, pp. 484–491 |
| Resultados (O) | Accuracy, F1, AUC, MAE, MSE, R²; TTD, TTR, MTTR, FPR, FNR, IRR, SIHR, OE, CSR, SIER; disparo de alertas e playbooks | Seções 4.1–4.4, pp. 484–491 |
| Contexto (C) | SOC e segurança cibernética, com dados públicos e outras fontes de logs; avaliação de componentes em ambiente experimental/simulações, sem demonstração robusta de operação continuada em produção | Seções 3.1, 3.3, 4.4, pp. 481–491 |
| Natureza agêntica | **Agêntico não-LLM**: autonomia funcional delimitada, agentes especializados coordenados, regras e inferência ML; planejamento deliberativo, memória deliberativa e supervisão humana formal não demonstrados | Seção 3.3, pp. 483–484 |
| Relevância para MTTD/MTTR | **Direta para indicadores e arquitetura**; indireta para comprovação de reduções efetivas; TTD e MTTR são medidos/preditos sem avaliação causal de melhoria | Seções 2, 4.4, pp. 480–491 |
| Carga cognitiva | A redução de alert fatigue e workload é motivação/benefício esperado, **não uma variável medida** em estudo com operadores | pp. 480, 483, 491 |
| OpenAlex | **5 citações** (dado informado no prompt, verificação indicada: 27/10/2026) | Insumos do protocolo |
| Crossref | **5 citações** (outra fonte, não somar com OpenAlex) | Insumos do protocolo |
| Scopus | **Não indexado**, segundo triagem fornecida | Insumos do protocolo |
| Qualis / CiteScore | **Não indexado / sem percentil Scopus informado**, segundo triagem | Insumos do protocolo |
| SJR | N/D, segundo triagem | Insumos do protocolo |
| Regra bibliométrica | **PDR-0007: RESSALVA DE ESTRATO OBRIGATÓRIA** para periódico sem indexação de estrato; PDR-0006 refere-se especificamente a conference papers e não é exclusão aplicável a este artigo de periódico | Protocolo |
| Elegibilidade temática | **Potencialmente elegível**, alinhado a arquitetura agêntica e resposta a incidentes, com ressalva de ausência do PICOC formal no material recebido | Avaliação fundamentada nas RQs |

## Tabela B — Cobertura das questões de pesquisa

**Escala:** T = totalmente atendida (1,0); P = parcialmente atendida (0,5); N = não atendida (0,0).

| RQ | Nota | Evidência âncora (seção/página) | Fundamentação |
|---|---:|---|---|
| **RQ1 — Contexto / definições** | **P — 0,5** | §3.3, pp. 483–484; §5, pp. 491–492 | Descreve dez papéis autônomos e decisões por limiares, inferência e acionamento de workflows. Não caracteriza sistematicamente níveis de autonomia, planejamento, memória, supervisão humana ou decisões colaborativas humano-agente. |
| **RQ2 — Engenharia / arquitetura** | **T — 1,0** | §3.1–3.3, pp. 481–484; Tabela 1, p. 482 | Define fontes, esquema de dados, modelos, artefatos de configuração, especialização de agentes, integração funcional, emissão de alertas e execução/simulação de playbooks. A contribuição arquitetural é direta, apesar da ausência de detalhes de infraestrutura de produção, guardrails e governança. |
| **RQ3 — Evidência / benefícios** | **P — 0,5** | §4.1–4.4, pp. 484–491; Tabelas 2–3, pp. 484, 486 | Relata métricas de classificação e regressão, indicadores SOC calculados e triggers de automação. Não mede redução causal de MTTD/MTTR, qualidade de decisão humana nem carga cognitiva, e não realiza comparação com baseline. |
| **RQ4 — Desafios / ética** | **P — 0,5** | §5, pp. 491–492 | Discute custo de implantação, especialização exigida, retreinamento e risco de automação não detectar ameaças imprevistas. Não desenvolve modelo de ameaças à arquitetura, accountability, supervisão, segurança das ações ou governança de automação. |
| **RQ5 — Lacunas / futuro** | **P — 0,5** | §5, p. 492 | Indica aprendizado contínuo, XAI e validação em operações reais. Não apresenta agenda sistemática de benchmarking, avaliação de humanos, segurança e governança de agentes. |
| **Total** | **3,0 / 5,0** | | **Banda Alta**, pela régua do protocolo (≥ 3,0), com predomínio de cobertura parcial e força empírica limitada. |

### Âncoras quantitativas essenciais para RQ3

| Indicador | Resultado reportado | Leitura metodologicamente permitida | Localização |
|---|---|---|---|
| FPR XGBoost | Accuracy 65%; F1 0,71; AUC 0,74 | Qualidade de um classificador, não redução observada da taxa operacional FPR | Tabela 2, p. 484 |
| FNR XGBoost | Accuracy 80%; F1 0,76; AUC 0,78 | Qualidade de classificador, não redução observada de incidentes não detectados | Tabela 2, p. 484 |
| TTR LightGBM | MAE 18%; MSE 1000; R² 0,85 | Desempenho preditivo; não comprova que o tempo real de resposta foi reduzido | Tabela 3, p. 486 |
| MTTR LightGBM | MAE 20%; MSE 1160; R² 0,80 | Desempenho preditivo; não comprova menor recuperação real | Tabela 3, p. 486 |
| TTD | 0,01 segundo, comparado a limiar de 3 minutos | Valor computado/apresentado pelo fluxo; **limiar não é baseline**; não representa por si só ganho causal de MTTD | §4.4.1, p. 488 |
| TTR | 11 incidentes entre 655 e 4192 minutos, acima do limiar de 300 minutos | Detecta violações e alertas; não comprova aceleração da resposta | §4.4.2, p. 489 |
| IRR | 85,6%, abaixo do limiar de 90% | Apuração e alerta | §4.4.2, p. 489 |
| Checklists SIHR | Texto refere 49 incidentes; a Figura 8 exibe “Found 100 incomplete checklists” | **Divergência interna a registrar**, requer esclarecimento sobre unidade/conjunto analisado | §4.4.2 e Fig. 8, p. 489 |
| MTTR previsto | 1884,2 horas | Predição em escala elevada e gatilho de atribuição; não evidência de redução | §4.4.3, p. 490 |
| OE | 856/1000 tarefas, 85,6% | Taxa de conclusão calculada; descrição aproxima conclusão de tarefas e pontualidade, conceitos que não são necessariamente equivalentes | §4.4.3, p. 490 |
| CSR | 60%, versus limiar de 90% | Monitoramento de satisfação | §4.4.4, p. 490 |
| SIER | 25%, versus limiar de 5% | Apuração de proporção de incidentes e aviso | §4.4.4, p. 491 |

**Nota crítica sobre dados e figuras:** o texto da §3.3 indica que o agente FPR remove automaticamente alertas de severidade inferior a 3 (p. 483); já a §4.4.1 informa supressão de alertas com severidade 3 e 4 (p. 488). É uma discrepância que dificulta reconstruir a regra operacional e avaliar riscos de supressão indevida. A Figura 8 (p. 489) também diverge da quantidade indicada no parágrafo. Essas inconsistências devem limitar o peso da evidência.

## Tabela C — Avaliação de qualidade (QA1–QA4)

**Atenção:** os nomes/definições oficiais de QA1–QA4 **não foram fornecidos**. Abaixo estão critérios substitutos, explicitados para permitir uma avaliação auditável. Não devem ser transcritos como QA oficiais sem conferência do protocolo completo.

| Critério operacional adotado | Julgamento | Justificativa | Evidência |
|---|---:|---|---|
| **QA1 — Objetivo e contexto explicitados** | **Y — 1,0** | Problema de alert fatigue, fragmentação e indicadores SOC, objetivo e abordagem são claros | Introdução e §2, pp. 480–481 |
| **QA2 — Métodos e intervenção suficientemente descritos** | **P — 0,5** | Apresenta origem/volume dos dados, modelos e papéis dos agentes, mas faltam detalhes suficientes de amostragem, separação temporal/antivazamento, hiperparâmetros, execução e reprodução independente | §§3.1–3.3, pp. 481–484 |
| **QA3 — Evidência empírica sólida e análise de validade** | **P — 0,5** | Tabelas e saídas quantitativas estão presentes; contudo, não há baseline, intervalos de confiança, testes estatísticos ou análise robusta de validade operacional. Algumas métricas não especificam unidades ou denominadores com clareza | §4, pp. 484–491 |
| **QA4 — Discussão crítica, limitações e transparência** | **P — 0,5** | Reconhece manutenção, risco de automação e necessidade de validação real, mas não discute suficientemente vieses, segurança de automações, inconsistências internas e generalização | §5, pp. 491–492 |
| **Total provisório** | **2,5 / 4,0** | **Banda Média**, conforme 1,5–2,5; depende de confirmação das definições oficiais de QA1–QA4 | |

## Análise crítica para a RSL

### Contribuições aproveitáveis

1. **Padrão arquitetural modular:** dez agentes por responsabilidade funcional (TTD, FNR, FPR, TTR, IRR, SIHR, MTTR, OE, CSR e SIER), com coordenação por informação compartilhada e mecanismos de acionamento. A contribuição é útil para examinar decomposição de responsabilidades em uma arquitetura agêntica (pp. 483–484).
2. **Acoplamento entre telemetria, predição e ação:** logs de SIEM/IDS, incident management, task tracking e CRM alimentam processamento, modelos, indicadores e notificações. É um caso concreto de automação orientada a sinais (pp. 481–484).
3. **Relação com incident response:** há monitoramento de detecção, resposta, recuperação, playbooks e atribuições; o estudo contextualiza métricas pertinentes a MTTD/MTTR, embora não prove sua redução causal (pp. 488–490).
4. **Limitações e agenda:** o trabalho reconhece custos, retreinamento, riscos de automação, necessidade de aprendizado contínuo, XAI e experimentação em operação real (p. 492).

### Limites de inferência

- **Sem baseline real:** os limiares de tempo e qualidade usados nas rotinas não satisfazem o requisito de Comparison; comparar modelos distintos ou predito versus real não supre essa ausência.
- **Sem comprovação de ganho operacional:** frases de melhoria de KPIs na conclusão não são respaldadas por série pré/pós-intervenção ou controle comparável; não extrair percentuais de economia de tempo.
- **Sem mensuração cognitiva:** não há instrumento para medir NASA-TLX, atenção, fadiga, esforço mental ou carga de trabalho de analistas; alert fatigue é contexto/motivação.
- **Autonomia limitada:** o artigo descreve agentes especializados, regras, predição e triggers, mas não demonstra uso de LLM como raciocinador, planejamento agentivo complexo, memória deliberativa, negociação multiagente ou políticas de aprovação humana.
- **Operação em produção não validada:** dados incluem repositórios públicos, e a descrição refere simulação de playbooks e testes de lógica. Não generalizar diretamente a SOCs reais contínuos.
- **Segurança de decisão:** a discrepância entre critério de supressão por severidade e exemplos suprimidos é especialmente relevante para falso negativo e risco de interrupção indevida de alertas.
- **Qualidade do relato:** a contagem de checklists inconclusos diverge entre narrativa e figura; alguns indicadores precisam de unidade, origem e validação mais claras.

### Aplicação à dissertação / extração recomendada

**Classificar o estudo como:** evidência de **arquitetura e automação agêntica não-LLM em SOC**, com **validação experimental de componentes preditivos e gatilhos**, não como evidência comprovada de redução de MTTD, MTTR ou carga cognitiva. Pode apoiar a discussão sobre integração entre observabilidade, classificação de alertas, gestão de incidentes e mecanismos de acionamento, acompanhada da ressalva metodológica.

**Registro para síntese:** separar as métricas de acurácia preditiva dos resultados de operação. Não codificar o TTD de 0,01 s como redução de MTTD, nem o R² de 0,80 para MTTR como redução de tempo de recuperação. A recomendação de playbooks e as simulações demonstram resposta automatizada planejada/acionada, sem evidência de remediação eficaz em produção.

## Bibliometria e aplicação das emendas

Os números de citações **OpenAlex = 5** e **Crossref = 5** são os valores de triagem fornecidos no prompt e representam fontes diferentes, portanto **não somar**. A triagem, datada de 27/10/2026, informa periódico sem indexação Scopus/CiteScore/estrato e SJR indisponível. Esta avaliação não revalidou os metadados externamente.

A **PDR-0006** disciplina especificamente a classificação dos *conference papers* e não determina exclusão neste caso, pois o P91 é artigo de periódico. A **PDR-0007** exige **RESSALVA DE ESTRATO OBRIGATÓRIA**, que acompanha qualquer uso desta evidência. O enquadramento definitivo da elegibilidade depende também da tabela PICOC formal, não anexada.

## Parecer conclusivo

**Aderência temática:** relevante, particularmente RQ2 e parcialmente RQ1, RQ3, RQ4 e RQ5.  
**Cobertura RQ:** **3,0/5,0 — Alta** segundo as bandas fornecidas.  
**Qualidade QA (critérios operacionais provisórios):** **2,5/4,0 — Média**, sujeita à substituição pela rubrica QA oficial.  
**Comparison:** **N/A**, por ausência de comparação empírica contra baseline concreto.  
**Natureza da intervenção:** **agêntico não-LLM (regras + ML)**.  
**Força da inferência:** arquitetura experimental e predição, **não eficácia causal demonstrada**.  
**Estrato:** **RESSALVA DE ESTRATO OBRIGATÓRIA — periódico sem indexação de estrato conforme triagem, PDR-0007**.

**Recomendação final: Incluir c/ ressalvas (PDR-0007: RESSALVA DE ESTRATO OBRIGATÓRIA por periódico sem estrato indexado; ausência de baseline empírico, autonomia não-LLM, inconsistências de relato e ausência de demonstração causal de redução de MTTD/MTTR ou carga cognitiva; elegibilidade condicionada à conferência do PICOC formal).**
