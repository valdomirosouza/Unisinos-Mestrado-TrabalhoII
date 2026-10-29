# Parecer — P91: Autonomous Agentic AI Architectures for Optimizing Security Operations Centers (SOC) KPIs: Methodology, Impact on Detection, Response, and Recovery

> Avaliador: Gemini · Data: 2026-10-29 · Prompt: prompt-P91.md
> (template v1.1.0)

## Tabela A — Identificação e PICOC

| Campo | Valor |
| :--- | :--- |
| **Veículo / ano / DOI** | *Revista Academiei Forţelor Terestre (Land Forces Academy Review)*, Vol. XXX, No. 3(119), pp. 479–493 · 2025 · DOI: `10.2478/raft-2025-0046` |
| **Qualis · SJR (insumo)** | Qualis **NÃO INDEXADO** (journal sem CiteScore/percentil no Scopus — PDR-0007) · SJR **N/D** · Citações: OpenAlex `5` · Crossref `5` · Scopus `NÃO INDEXADO` |
| **Tipo / paradigma** | Artigo Primário Experimental (Pipeline de *Machine Learning* Supervisionado + 10 Agentes Baseados em Regras/Thresholds — **Agêntico não-LLM**) |
| **P · I · C · O · C** | **P (Population):** Operações de *Security Operations Centers (SOCs)* monitorando logs de SIEM, IDS, gestão de incidentes, tarefas e CRM (`214` arquivos CSV públicos, `25.182.806` registros brutos limpos para `8.628.160` observações e `343` colunas de CICIDS2017, CSE-CIC-IDS2018, CTU-13, SOF-ELK, Suricata e Wazuh Cloud Demo).<br>**I (Intervention):** Arquitetura de automação de 10 KPIs de SOC (agrupados em 4 categorias a partir de 16 indicadores) composta por **10 agentes especializados** (*TTD Monitoring, FNR Analysis, FPR Suppression, TTR Response, IRR Tracking, SIHR Validation, MTTR Recovery, OE Task, CSR Feedback, SIER Metrics*) apoiados por **5 modelos de ML** (`2` classificadores *XGBoost* para FNR/FPR, `2` regressores *LightGBM* para TTR/MTTR e `1` analisador *BERT fine-tuned* para CSR).<br>**C (Comparison):** **N/A** (Ausência de baseline comparativo empírico; os modelos são avaliados isoladamente em divisão treino/teste 80%/20% e os agentes são demonstrados sobre fatias do dataset sem comparação antes/depois contra um SOC manual ou baseline externo).<br>**O (Outcome):** Métricas preditivas offline (*FPR Classifier*: `Accuracy = 65%`, `F1 = 0.71`, `AUC = 0.74`; *FNR Classifier*: `Accuracy = 80%`, `F1 = 0.76`, `AUC = 0.78`; *TTR Regressor*: `MAE = 18%`, `MSE = 1000`, $R^2 = 0.85$; *MTTR Regressor*: `MAE = 20%`, `MSE = 1160`, $R^2 = 0.80$; *BERT CSR*: `Eval Loss = 1.02–1.06`) e execução automatizada de cálculo/alerta de KPIs (`TTD = 0.01 s`, supressão de alertas, disparo de playbooks para `499` casos de malware, `IRR = 85.6%`, `OE = 85.6%`, `CSR = 60%`, `SIER = 25%`).<br>**C (Context):** Ambiente laboratorial/offline utilizando consolidação de datasets públicos de cibersegurança e logs de demonstração. |

---

## Tabela B — Cobertura das RQs

| RQ | T/P/N | Evidência (seção/página) |
| :--- | :---: | :--- |
| **RQ1** | **P** (`0.5`) | **Seções 1, 2 e 3.3 (pp. 480–481, 483–484):** Estrutura uma taxonomia operacional de **10 KPIs** derivados de **16 indicadores** em 4 categorias do ciclo de vida do SOC: *Detection and Filtering* (`TTD, FNR, FPR`), *Response and Resolution* (`TTR, IRR, SIHR`), *Recovery and Operational Efficiency* (`MTTR, OE`) e *Satisfaction and Risk Management* (`CSR, SIER`). Define papéis funcionais para 10 agentes, porém o nível de autonomia restringe-se à avaliação de limiares estáticos (*thresholds*) e invocação de métodos `.predict()` de modelos supervisionados offline, sem planejamento autônomo dinâmico, memória episódica ou raciocínio baseado em LLM. |
| **RQ2** | **P** (`0.5`) | **Seções 3.1, 3.2 e 3.3, Tabela 1 (pp. 481–484):** Descreve o pipeline de pré-processamento (`214` CSVs, `5.270,09 MB` $\to$ `8.628.160` linhas), a suíte de **5 modelos de ML** (*XGBoost* para `clf_fnr.model` e `clf_fpr.model`, *LightGBM* para `reg_ttr.txt` e `reg_mttr.txt` com retreinamento mensal, e *BERT fine-tuned* por 20 épocas para sentimento de clientes) e os **10 agentes especializados** operando sobre DataFrames (`alerts_df`, `incidents_df`, `tasks_df`) e arquivo de configuração `detection_rules.json`. Faltam mecanismos formais de orquestração multiagente, protocolo de comunicação inter-agentes, memória compartilhada e guardrails de segurança. |
| **RQ3** | **P** (`0.5`) | **Seções 4.1 a 4.4, Tabelas 2 e 3, Figuras 1–13 (pp. 484–491):** Reporta desempenho dos classificadores XGBoost (*FPR*: `Acc = 65%`, `F1 = 0.71`, `AUC = 0.74`; *FNR*: `Acc = 80%`, `F1 = 0.76`, `AUC = 0.78`, Tabela 2, p. 484), dos regressores LightGBM (*TTR*: `MAE = 18%`, `MSE = 1000`, $R^2 = 0.85$; *MTTR*: `MAE = 20%`, `MSE = 1160`, $R^2 = 0.80$, Tabela 3, p. 486), convergência do BERT (`Eval Loss` `1.02–1.06`, Figura 3, p. 487) e logs de console da execução dos agentes (`TTD = 0.01 s`, supressão de 3 alertas, acionamento de playbook em 499 incidentes de malware, `TTR` de `655–4192 min`, `IRR = 85.6%`, `49` checklists incompletos, `MTTR = 1884.21 h`, `OE = 85.6%`, `CSR = 60%`, `SIER = 25%`). Contudo, não há baseline comparativo (*Comparison N/A*) que comprove redução real de TTD/MTTR frente a um processo não-agêntico. |
| **RQ4** | **P** (`0.5`) | **Seção 5 (pp. 491–492):** Discute brevemente limitações práticas de implantação: necessidade de recursos iniciais substanciais, alta expertise técnica, manutenção contínua via retreinamento periódico e o risco de **automação excessiva** causar desatenção humana a ameaças inéditas fora do escopo de treinamento dos agentes. Não analisa ameaças adversariais nem *accountability* formal. |
| **RQ5** | **P** (`0.5`) | **Seção 5 (p. 492):** Identifica três direções futuras: (i) integração de técnicas de *continual learning* para adaptação a ameaças emergentes; (ii) aplicação de *Explainable AI (XAI)* (citando Arrieta et al., 2020) para ampliar a transparência e a confiança nas decisões automatizadas; e (iii) validação empírica em ambientes operacionais de SOC reais. |

**SCORE_RQ:** `2.5` (`2.5 / 5.0`)

---

## Tabela C — Qualidade (DARE)

| QA | Y/P/N | Justificativa |
| :--- | :---: | :--- |
| **QA1 Objetivos claros** | **Y** (`1.0`) | O objetivo de automatizar a gestão preditiva e o monitoramento de 10 KPIs de SOC (baseados em 16 indicadores distribuídos em 4 categorias operacionais) é claramente definido e estruturado nas Seções 1 e 2 (pp. 480–481). |
| **QA2 Metodologia replicável** | **P** (`0.5`) | Identifica os conjuntos de dados públicos utilizados (CICIDS2017, CSE-CIC-IDS2018, CTU-13, Wazuh Demo, SOF-ELK, Suricata) e os 5 algoritmos (Seção 3, Tabela 1, pp. 481–484), mas não divulga o código-fonte, os hiperparâmetros dos modelos XGBoost/LightGBM/BERT nem o mapeamento exato de fusão dos 214 arquivos CSV em 343 colunas. |
| **QA3 Base de evidência sólida** | **P** (`0.5`) | Apresenta métricas clássicas de validação de ML (Tabelas 2 e 3, Figuras 1–3), mas carece de comparação contra baseline (*Comparison N/A*) e exibe inconsistências internas de lógica: na Seção 3.3 (p. 483), afirma que o *FPR Suppression Agent* filtra alertas com `severity < 3`, porém o log da Figura 5 (Seção 4.4.1, p. 488) mostra o agente removendo como *"low-risk"* alertas de `severity 3 (Medium)` e `severity 4 (High severity attack)`. Além disso, os logs das Figuras 6–12 refletem recortes pequenos e estáticos (`11` incidentes para TTR, `1000` tarefas para OE, `2000` eventos para SIER). |
| **QA4 Conclusões coerentes** | **P** (`0.5`) | Embora reconheça limitações de manutenção e riscos de automação excessiva (Seção 5, pp. 491–492), o texto extrapola as evidências ao declarar no Resumo (p. 479) e na Conclusão (p. 491) que os resultados demonstram redução de tempos de detecção/resposta e de falsos alarmes sem ter executado um experimento comparativo antes/depois. |

**SCORE_QA:** `2.5` (`2.5 / 4.0`) · **Banda:** Média

---

## Detalhamento Analítico (Etapa 0 e Etapa 1)

### Elegibilidade e Alinhamento ao Protocolo (PDR-0006 / PDR-0007)
- **Aderência Temática (PICOC):** O estudo investiga a automação de operações de SOC (detecção, resposta, recuperação e gestão de risco/satisfação) por meio de uma arquitetura nominalmente denominada *Agentic AI* combinada a modelos preditivos de *Machine Learning* (XGBoost, LightGBM e BERT).
- **Natureza da Agência:** Conforme sinalizado na triagem (precedente `P88`), trata-se de **arquitetura agêntica não-LLM**: os 10 agentes são módulos de software especializados que monitoram colunas específicas de tabelas de eventos/incidentes, invocam inferências supervisionadas (`.predict()`) e disparam regras condicionais (`if/else` sobre limiares estáticos, como `TTD > 3 min`, `TTR > 300 min`, `IRR < 90%`, `OE < 30%`, `CSR < 90%`, `SIER > 5%`).
- **Avaliação de Estrato (PDR-0007):** Publicado na *Revista Academiei Forţelor Terestre (Land Forces Academy Review)*, periódico **NÃO INDEXADO** no Scopus (sem CiteScore/percentil). Nos termos do **PDR-0007**, o estudo é elegível exclusivamente sob **RESSALVA DE ESTRATO OBRIGATÓRIA**.

---

## Síntese do avaliador

O estudo **P91 (Stefanov et al., 2025)** propõe uma metodologia estruturada para automação do monitoramento e predição de **10 KPIs operacionais de SOC** (`TTD, FNR, FPR, TTR, IRR, SIHR, MTTR, OE, CSR, SIER`) integrando cinco modelos de aprendizado de máquina (*XGBoost*, *LightGBM* e *BERT*) a dez agentes funcionais baseados em regras sobre um corpus consolidado de `8,6 milhões` de registros de datasets públicos. A principal contribuição do artigo reside na sistematização taxonômica dos 16 indicadores de desempenho cobrindo todo o ciclo de vida de resposta a incidentes e no acoplamento entre regressão de tempos operacionais (`TTR` com $R^2 = 0.85$ e `MTTR` com $R^2 = 0.80$) e gatilhos automatizados de *playbooks* e reatribuição de tarefas. Todavia, o trabalho apresenta limitações metodológicas importantes: (i) os "agentes" são scripts determinísticos acoplados a predições supervisionadas offline (agência não-LLM, análoga a P88); (ii) não há comparação empírica contra um baseline concreto (*Comparison N/A*); e (iii) há contradições internas nos testes de execução (como a supressão automática de um ataque de alta severidade `severity = 4` na Figura 5 contrariando a regra de filtragem `severity < 3` definida na Seção 3.3). Em conformidade com o **PDR-0007**, sua inclusão no corpus deve ser acompanhada de **ressalva obrigatória de estrato** (periódico não indexado no Scopus) e de escopo metodológico.

## Recomendação

`Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA — journal NÃO INDEXADO no Scopus, PDR-0007; arquitetura agêntica não-LLM baseada em regras e ML supervisionado [precedente P88]; ausência de baseline comparativo empírico [Comparison N/A])`
