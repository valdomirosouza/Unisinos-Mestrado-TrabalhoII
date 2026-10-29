# Parecer — P93: From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures

> Avaliador: Gemini · Data: 2026-10-29 · Prompt: prompt-P93.md
> (template v1.1.0)

## Tabela A — Identificação e PICOC

| Campo | Valor |
| :--- | :--- |
| **Veículo / ano / DOI** | *Journal of Information & Knowledge Management* (World Scientific), Vol. 25, No. 9, Art. 2650039 (27 pp.) · 2026 · DOI: `10.1142/s0219649226500395` |
| **Qualis · SJR (insumo)** | Qualis **A3** (derivado do percentil Scopus `65%` — regra CAPES 2025–2028; PDR-0007) · SJR **N/D** · Citações: OpenAlex `0` · Crossref `0` · Scopus `0` |
| **Tipo / paradigma** | Artigo Primário de Avaliação Operacional Comparativa e Modelagem de Equações Estruturais (**PLS-SEM**) sobre Simulação de 90 Dias (Framework **3E**: *Efficiency, Effectiveness, Experience* + Arquitetura *Agentic SOC*) |
| **P · I · C · O · C** | **P (Population):** Operações de *Security Operations Centres (SOCs)* corporativos de médio/grande porte (analistas Tier 1 e Tier 2) monitorando fluxos contínuos de alertas de SIEM, EDR, rede e nuvem (`N = 5.571` observações em janela simulada de 90 dias).<br>**I (Intervention):** Arquitetura **Agentic SOC (AI-Enhanced SOC)** estruturada em camadas (*Data, Perception, Action & Orchestration, Agentic Reasoning, Human Oversight*) com remediação autônoma pontuada por confiança em 4 níveis (*Network, Endpoint, Identity, System Integrity / Self-Healing*) e supervisão humana em *Strategic Checkpoints* (*Bounded Autonomy*), avaliada pelo framework multidimensional **3E (*Efficiency, Effectiveness, Experience*)**.<br>**C (Comparison):** Comparação empírica simulada contra **Traditional SOC** (SIEM baseado em regras estáticas e triagem/investigação manual centrada no analista sobre as mesmas distribuições de alertas durante 90 dias).<br>**O (Outcome):** Melhorias reportadas nas 3 dimensões (com divergência interna de escala entre Tabelas 3 e 9): na Tabela 3 (p. 14), **MTTD** cai de `6–12 h` para `30–90 min` (`75%`), **MTTR** de `12–24 h` para `2–6 h` (`80%`), **FPR** de `35–45%` para `10–15%` (`65%`) e carga de `500+` para `120–150` alertas/dia (`70%`); na Tabela 9 (p. 20), **MTTD** cai de `18,2 min` para `10,2 min` (`44%`), **MTTR** de `32,5 min` para `17,2 min` (`47%`), carga de `35` para `20` alertas/turno (`43%`), *Cognitive Fatigue* de `7,2/10` para `5,0/10` (`31%`) e *Trust-in-AI* sobe de `5,5/10` para `6,8/10` (`24%`). Em ataque *zero-day* simulado (Tabela 10, p. 21), o tempo de contenção cai de `42 min` para `9 min` (`-76%`). Matriz de confusão ($N = 5.571$, p. 22): `Precision = 0.873`, `Recall = 0.929`, `F1 = 0.900`, `Accuracy = 0.951`. Modelo **PLS-SEM** (Tabela 8, p. 20) valida `H1–H4` ($\beta = 0.64, 0.57, 0.33, 0.71$).<br>**C (Context):** Simulação controlada de 90 dias consecutivos com telemetria sintética parametrizada a partir de *benchmarks* da indústria (sem participação direta de sujeitos humanos). |

---

## Tabela B — Cobertura das RQs

| RQ | T/P/N | Evidência (seção/página) |
| :--- | :---: | :--- |
| **RQ1** | **T** (`1.0`) | **Seções 1, 2 e 3, Tabelas 1 e 2, Figuras 1, 2 e 7 (pp. 2–9, 16–17):** Conceitua a transição do SOC manual e do SOAR reativo baseado em scripts para o **Agentic SOC** sob a perspectiva socio-técnica e de *Information and Knowledge Management (IKM)*. Diferencia automação baseada em regras de autonomia agêntica (delegação de decisão e execução sob governança) e formaliza o modelo **Bounded Autonomy** com *Strategic Checkpoints* humanos concentrados em incidentes de alta severidade ou ambiguidade contextual. |
| **RQ2** | **P** (`0.5`) | **Seção 3, Figura 3, Tabelas 6 e 7 (pp. 10–11, 14–15, 18):** Propõe uma arquitetura conceitual em camadas (*Data Layer, Perception Layer, Action & Orchestration Layer, Agentic Reasoning Layer* [regras + classificadores probabilísticos] e *Human Oversight Layer* com *Feedback Loop*, Figura 3, p. 11) e uma hierarquia de remediação autônoma em 4 camadas lógicas (*Network Control / Boundary Defence, Endpoint Control / Local Containment, Identity Control / Access Management, System Integrity / Self-Healing*, Tabelas 6–7, pp. 15, 18; mencionando brevemente arquitetura *Oracle Management Cloud — OMC* na p. 18). Contudo, não especifica modelos de IA/LLM concretos, protocolos de agentes nem implementação de software. |
| **RQ3** | **P** (`0.5`) | **Seções 3 e 4, Tabelas 3 a 12, Figuras 4 a 10 (pp. 11–23):** Apresenta ampla bateria de indicadores quantitativos sobre 90 dias de simulação (`N = 5.571`), incluindo validação estatística via **PLS-SEM** (`H1: AL -> OE`, $\beta = 0.64, p < 0.001$; `H2: AL -> DE`, $\beta = 0.57, p < 0.01$; `H3: AL -> AX`, $\beta = 0.33, p < 0.05$; `H4: OE+DE+AX -> SP`, $\beta = 0.71, p < 0.001$, Tabela 8, p. 20), matriz de confusão (`Precision = 0.873`, `Recall = 0.929`, `F1 = 0.900`, `Acc = 0.951`, Figura 10, pp. 22–23), TPR por camada de remediação (`97,7%` a `99,5%` vs. `45,6%` na triagem manual, Tabelas 5 e 7, pp. 14, 18) e contenção de *zero-day* (`42 min` $\to$ `9 min`, `-76%`, Tabela 10, p. 21). Recebe `P = 0.5` devido ao uso exclusivo de dados sintéticos/proxies simulados e à **inconsistência interna severa de escala** entre a Tabela 3 (p. 14: MTTD `6–12 h` $\to$ `30–90 min`, MTTR `12–24 h` $\to$ `2–6 h`, carga `500+` $\to$ `120–150` alertas) e a Tabela 9 (p. 20: MTTD `18,2 min` $\to$ `10,2 min`, MTTR `32,5 min` $\to$ `17,2 min`, carga `35` $\to$ `20` alertas/turno). |
| **RQ4** | **T** (`1.0`) | **Seções 2, 4 e 5, Figura 7, Tabelas 7 e 9 (pp. 4–6, 16–20, 23–25):** Analisa detalhadamente os desafios humanos, organizacionais e de governança: realocação cognitiva do analista (de triagem repetitiva para auditoria de decisão e tratamento de exceções), defasagem na calibração de confiança humana (*Trust-in-AI score* cresce apenas `24%`, mais lentamente que os ganhos operacionais de `44–47%`, pp. 19–20), necessidade de **Bounded Autonomy** em incidentes de alto impacto no negócio, *accountability* ética e barreiras de adoção (telemetria fragmentada, desconfiança algorítmica e relutância organizacional em delegar autoridade, p. 25). |
| **RQ5** | **P** (`0.5`) | **Seções 5 e 6 (pp. 24–26):** Aponta a inadequação dos modelos clássicos de maturidade de SOC (que tratam automação como estática e ignoram a autonomia decisória e a reconfiguração de papéis humano-IA, p. 24) e recomenda três direções futuras (p. 26): integração de mecanismos de *Explainable AI (XAI)*, estudos longitudinais em implantações reais de produção e refinamento contínuo dos mecanismos de governança e controle humano. |

**SCORE_RQ:** `3.5` (`3.5 / 5.0`)

---

## Tabela C — Qualidade (DARE)

| QA | Y/P/N | Justificativa |
| :--- | :---: | :--- |
| **QA1 Objetivos claros** | **Y** (`1.0`) | Define com clareza 4 questões de pesquisa (`RQ1–RQ4`, Seção 1, pp. 3–4) mapeadas às dimensões do framework **3E** (*Efficiency, Effectiveness, Experience* e *Cross-cutting*, Tabela 1, p. 7) e 4 hipóteses estruturais (`H1–H4`, Seção 4, pp. 19–20). |
| **QA2 Metodologia replicável** | **P** (`0.5`) | Apresenta as fórmulas matemáticas das métricas (MTTD, MTTR, FPR, ER, $\text{AI}_{\text{Impact}}$, p. 12) e os critérios de ajuste do PLS-SEM (`CFI, RMSEA, SRMR, CR > 0.70, AVE > 0.50` sobre `N = 5.571`, p. 11), porém não disponibiliza o dataset sintético, o código de simulação nem a especificação algorítmica exata dos agentes e dos proxies da dimensão *Experience*. |
| **QA3 Base de evidência sólida** | **P** (`0.5`) | Embora execute comparação controlada e modelagem PLS-SEM, a evidência apresenta três fragilidades importantes: (1) os dados são inteiramente sintéticos e a dimensão humana (*Experience*, incluindo fadiga cognitiva e *Trust-in-AI*) foi gerada por *proxies* de sistema simulados, sem pesquisa com analistas reais (Seção 3, pp. 6, 10); (2) há uma **contradição numérica interna não explicada** entre os valores de MTTD, MTTR, FPR e carga de trabalho da Tabela 3 (p. 14, em horas e centenas de alertas) e os da Tabela 9 (p. 20, em minutos e dezenas de alertas); e (3) há erros de revisão técnica no artigo, como a equação do F1-Score na p. 22 impressa como $\frac{1240}{1240+95}$ (idêntica à do Recall, embora o resultado `0.900` esteja correto) e a duplicação do bloco *Action & Orchestration Layer* na Figura 3 (p. 11). |
| **QA4 Conclusões coerentes** | **P** (`0.5`) | A síntese socio-técnica sobre *Bounded Autonomy*, *Strategic Checkpoints* e a transformação do papel do analista (Seções 5 e 6, pp. 23–26) é conceitualmente sólida e bem articulada, mas as afirmações quantitativas exigem cautela devido às inconsistências de escala entre as tabelas de resultados e à natureza simulada dos indicadores de experiência humana. |

**SCORE_QA:** `2.5` (`2.5 / 4.0`) · **Banda:** Média

---

## Detalhamento Analítico (Etapa 0 e Etapa 1)

### Elegibilidade e Alinhamento ao Protocolo (PDR-0006 / PDR-0007)
- **Aderência Temática (PICOC):** O estudo avalia diretamente o impacto operacional e organizacional de arquiteturas de **Agentic SOC** frente ao SOC manual tradicional, mensurando MTTD, MTTR, taxa de falsos positivos, sucesso de remediação por camada e redistribuição de carga cognitiva do analista.
- **Avaliação de Comparison:** O estudo executa comparação quantitativa estruturada (*Traditional SOC vs. AI-Enhanced Agentic SOC*) sobre 90 dias de telemetria simulada (`N = 5.571` eventos) e um cenário de ataque *zero-day* (Tabela 10), atendendo à exigência de baseline comparativo, embora sob dados sintéticos.
- **Avaliação de Estrato (PDR-0007):** Publicado no *Journal of Information & Knowledge Management* (World Scientific), que possui percentil Scopus de `65%`, correspondendo ao estrato **Qualis A3** pela regra CAPES 2025–2028. Conforme o **PDR-0007**, por situar-se fora de A1–A2, o artigo recebe **RESSALVA DE ESTRATO OBRIGATÓRIA**.

---

## Síntese do avaliador

O estudo **P93 (Wahed & Aljawarneh, 2026)** contribui para a RSL com o framework multidimensional **3E (*Efficiency, Effectiveness, Experience*)** e com a fundamentação socio-técnica do modelo de **Bounded Autonomy** em operações de SOC, demonstrando via **PLS-SEM** ($N = 5.571$) que a delegação de triagem e contenção rotineira a agentes autônomos desloca o analista humano para *Strategic Checkpoints* de supervisão, auditoria e decisão ética em incidentes críticos. Merece destaque a análise estratificada de remediação em quatro camadas (*Identity, Data, Endpoint, Self-Healing*, Tabelas 5–7), que evidencia o contraste entre o gargalo da triagem manual (`FPR = 54,4%`) e a precisão das ações autônomas (`TPR` entre `97,7%` e `99,5%`), bem como a redução de `76%` no tempo de resposta a um incidente *zero-day* (`42 min` $\to$ `9 min`). Entretanto, o uso da evidência requer dupla cautela: (i) **RESSALVA DE ESTRATO OBRIGATÓRIA** por tratar-se de periódico **Qualis A3** (**PDR-0007**); e (ii) ressalva metodológica quanto à natureza puramente sintética da telemetria e dos *proxies* de experiência humana (sem analistas reais) e à inconsistência interna de escala entre as Tabelas 3 (p. 14) e 9 (p. 20) nos valores absolutos de MTTD, MTTR e carga de alertas.

## Recomendação

`Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA — Qualis A3, PDR-0007; simulação com telemetria sintética e proxies de experiência sem sujeitos humanos; inconsistência interna de escala entre as Tabelas 3 e 9 para MTTD/MTTR/carga de trabalho)`
