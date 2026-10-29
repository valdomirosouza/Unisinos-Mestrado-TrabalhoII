# Parecer — P97: Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Conceptual Framework

> Avaliador: Gemini · Data: 2026-10-29 · Prompt: prompt-P97.md
> (template v1.1.0)

## Tabela A — Identificação e PICOC

| Campo | Valor |
| :--- | :--- |
| **Veículo / ano / DOI** | *Network* (MDPI), Vol. 6, No. 4, Art. 84 (33 pp.) · 2026 · DOI: `10.3390/network6040084` |
| **Qualis · SJR (insumo)** | Qualis **A2** (derivado do percentil Scopus `79%`) · SJR **N/D** · Citações: OpenAlex `0` · Crossref `0` · Scopus `NÃO INDEXADO` (artigo recém-publicado) |
| **Tipo / paradigma** | Estudo Misto: Revisão Sistemática da Literatura (PRISMA, `33` estudos) + Framework Arquitetural Conceitual (**Agentic AI-Driven SOCaaS** em 6 Camadas) + 4 Experimentos de Simulação baseados em Componentes |
| **P · I · C · O · C** | **P (Population):** Operações de segurança em nuvem pública, híbrida e multi-cloud gerenciadas no modelo **SOC-as-a-Service (SOCaaS)** multitenant (e corpus de `33` estudos revisados: `23` legados + `10` da atualização Scopus a partir de `2.181` registros).<br>**I (Intervention):** Framework **Agentic AI-Driven SOCaaS** estruturado em **9 princípios de design**, **4 fronteiras de confiança** (*evidence, knowledge, decision, execution*), **6 camadas operacionais** (`L1 SENSE` [ingestão], `L2 TRIAGE` [correlação/enriquecimento], `L3 GROUND` [RAG sobre playbooks/MITRE ATT&CK/políticas], `L4 REASON` [orquestração agêntica], `L5 GOVERN` [aprovação humana e políticas], `L6 ACT` [execução e auditoria forense]) e um **Cross-Cutting Agent Security and Trust-Enforcement Plane**.<br>**C (Comparison):** Na validação por simulação (`seed = 42`), compara: (Exp. 1) política *Argmax* vs. *Conservative Gate* ($p \ge 0.90$) sobre `20.000` eventos; (Exp. 2) mapeamento de playbooks *Ungrounded* (apenas títulos) vs. *Grounded Retrieval* (TF-IDF) em `60` queries; e (Exp. 3) **Agentic + Governance ($\theta = 0.50$)** vs. **Manual SOC** e vs. **Narrow-AI Assisted SOC** em simulação de eventos discretos (`2.000` incidentes, `6` analistas, taxas de chegada de `6` a `26` incidentes/hora).<br>**O (Outcome):** **Exp. 1 (Triagem Random Forest):** `Macro F1 = 0.907`, `Accuracy = 0.945`; sob *Conservative Gate* ($p \ge 0.90$), suprime **59,5%** do volume de alertas reduzindo *threat leakage* de `12,22%` para **4,81%**. **Exp. 2 (Retrieval TF-IDF):** eleva acurácia Top-1 de **0,317 para 0,850** (`2,7x`) e Top-3 de **0,583 para 0,933**. **Exp. 3 (Orquestração):** reduz **MTTT** de `20,1 min` (Manual) e `7,1 min` (Narrow-AI) para **2,1 min**, e **MTTR** de `59,5 min` (Manual) e `23,4 min` (Narrow-AI) para **8,8 min** (**redução de 6,8x**), reduzindo toques de analista de `3,50` para `0,32` (`67,9%` auto-executados e apenas `1,29%` de ações de alto impacto sem aprovação humana). **Exp. 4 (Auditoria Monte Carlo, 1.000 runs):** **95,5%** de cadeias forenses completas (`5,95/6` passos) com *overhead* médio de **1,79%** (`54,3 s` baixo risco vs. `327,7 s` alto risco com aprovação).<br>**C (Context):** Síntese de literatura sobre SOCaaS em nuvem combinada a ambiente de simulação estocástica/ML em Python (`scikit-learn`, `NumPy`, simulador de eventos discretos) sob premissas sintéticas explícitas (*internal feasibility rather than production efficacy*). |

---

## Tabela B — Cobertura das RQs

| RQ | T/P/N | Evidência (seção/página) |
| :--- | :---: | :--- |
| **RQ1** | **T** (`1.0`) | **Seções 1, 4.1 a 4.11 e 5.2, Figuras 2 e 3, Tabelas 1 a 3 (pp. 1–3, 7–17):** Sintetiza 33 estudos em 4 correntes e propõe uma taxonomia de maturidade em **3 níveis** (Figura 3, p. 13; Tabela 3, p. 14): **Level 1 — Narrow AI for Detection / Triage**, **Level 2 — Contextual Support and Workflow Assistance (LLM/RAG)** e **Level 3 — Semi-Autonomous and Agentic Orchestration**. Fundamenta o conceito de **Bounded Autonomy** (autonomia restrita por políticas determinísticas e supervisão humana para ações de alto impacto em nuvem). |
| **RQ2** | **T** (`1.0`) | **Seções 5.1 a 5.7, Figuras 4 e 5, Tabela 4 (pp. 16–22):** Especifica os **9 princípios de design** (Seção 5.3, pp. 17–18), as **4 fronteiras de confiança** (*evidence, knowledge, decision, execution boundaries*, Seção 5.1, p. 16), as **6 camadas arquiteturais** (`SENSE, TRIAGE, GROUND, REASON, GOVERN, ACT`, Figura 4, p. 18) e o **Cross-Cutting Agent Security and Trust-Enforcement Plane** (Seção 5.4.1, Tabela 4, pp. 18–19), além de fluxo operacional completo de resposta a escalonamento de privilégios em IAM/API multi-cloud (Figura 5, pp. 20–21). |
| **RQ3** | **P** (`0.5`) | **Seções 6.1 a 6.7, Tabelas 5 a 10, Figuras 6 a 10 (pp. 22–29):** Apresenta 4 experimentos reproduzíveis (`seed = 42`): (1) triagem com *Random Forest* (`Macro F1 = 0.907`, supressão de `59,5%` com `4,81%` de *threat leakage* sob gate $p \ge 0.90$, Tabelas 5–6); (2) *grounding* léxico TF-IDF sobre playbooks MITRE ATT&CK (`Top-1` de `0.317` $\to$ `0.850`, Tabela 7); (3) simulação de filas de `2.000` incidentes demonstrando redução de **MTTR em 6,8x** (`59,5 min` $\to$ `8,8 min`), estabilidade sob carga até `26 incidentes/h` e curva de sensibilidade do limiar de governança $\theta \in [0.30, 0.90]$ (Tabelas 8–9, Figuras 8–9); e (4) `1.000` rodadas Monte Carlo atingindo `95,5%` de completude de trilha de auditoria com `1,79%` de *overhead* (Tabela 10, Figura 10). Recebe `P = 0.5` porque os experimentos avaliam modelos substitutos (*Random Forest*, *TF-IDF* e filas estocásticas) sobre dados sintéticos, qualificados pelos próprios autores como *"internal feasibility rather than production efficacy"* (pp. 1, 22, 28). |
| **RQ4** | **T** (`1.0`) | **Seções 4.7, 4.8, 5.1, 5.4.1 e 6.4, Tabelas 4 e 9, Figura 9 (pp. 12, 16, 18–20, 26–27):** Mapeia 6 classes de ameaças adversariais e operacionais em agentes de SOCaaS (*Direct prompt injection, Indirect prompt injection, Retrieval poisoning, Tool misuse, Cross-tenant leakage, Audit manipulation*) aos respectivos controles arquiteturais (Tabela 4, p. 19) e quantifica a assimetria risco-velocidade da governança (Tabela 9 e Figura 9, pp. 26–27): elevar o limiar $\theta$ de `0.50` para `0.90` economiza apenas `2,2 min` de MTTR (`8,8` $\to$ `6,6 min`), mas faz a execução automática sem aprovação humana de ações de alto impacto saltar de `1,29%` para `74,15%`. |
| **RQ5** | **T** (`1.0`) | **Seções 6.6 e 7 (pp. 28–30):** Discute exaustivamente 6 limitações e 5 direções de pesquisa futuras: (1) ampliação da RSL para *Web of Science* e recuperação dos 55 artigos não acessados; (2) implementação de protótipos com agentes LLM reais em nuvem; (3) avaliação comparativa e adversarial empírica (testando *prompt injection*, *retrieval poisoning* e vazamento *cross-tenant* entre RAG léxico, denso e híbrido); (4) engenharia de políticas executáveis (*policy-as-code*) para limiares de aprovação e retenção forense; e (5) investigação de fatores humanos (fadiga, calibração de confiança e qualidade de decisões HITL sob pressão). |

**SCORE_RQ:** `4.5` (`4.5 / 5.0`)

---

## Tabela C — Qualidade (DARE)

| QA | Y/P/N | Justificativa |
| :--- | :---: | :--- |
| **QA1 Objetivos claros** | **Y** (`1.0`) | Explicita 5 questões de pesquisa (`RQ1–RQ5`, Seção 2, p. 3), critérios de inclusão/exclusão em 5 eixos temáticos (Seção 3.3, pp. 4–5) e rubrica estruturada de avaliação de relevância (8 dimensões, escala `0–2`) e qualidade metodológica (5 critérios, escala `0–2`, limiar $\ge 7/10$, Seção 3.5, p. 6). |
| **QA2 Metodologia replicável** | **P** (`0.5`) | A Fase 2 da RSL (atualização Scopus com `2.181` registros, PRISMA na Figura 1, p. 5, e planilhas suplementares `Tables S1–S6`) e os 4 experimentos de simulação (código e dados abertos no GitHub `https://github.com/usamrf/agentic-socaas-validation` e Zenodo `10.5281/zenodo.22375531`, p. 32) possuem excelente reprodutibilidade. Contudo, a Fase 1 (*legacy corpus* de `23` estudos, contendo `6` preprints = `18,2%` do total) não preservou registros intermediários de busca/triagem, e `55 dos 65` estudos elegíveis na Fase 2 não puderam ser baixados em texto completo (Seções 3.4 e 7, pp. 4–5, 29). |
| **QA3 Base de evidência sólida** | **P** (`0.5`) | A síntese de 33 estudos é bem estruturada e os 4 experimentos são matematicamente consistentes, mas a validação empírica não instancia um LLM real nem testa o plano de segurança contra ataques adversariais reais, utilizando componentes substitutos (*Random Forest* para triagem, *TF-IDF* para retrieval e filas lognormais/exponenciais assumidas, Seção 6.6, p. 28). |
| **QA4 Conclusões coerentes** | **Y** (`1.0`) | Rigor e transparência exemplares na interpretação dos resultados: desde o Resumo (p. 1) até as Ameaças à Validade (Seção 6.6, p. 28) e Conclusões (Seção 8, p. 31), os autores delimitam que os resultados demonstram **viabilidade interna condicional às premissas sintéticas**, sem reivindicar eficácia em produção. |

**SCORE_QA:** `3.0` (`3.0 / 4.0`) · **Banda:** Alta

---

## Detalhamento Analítico (Etapa 0 e Etapa 1)

### Elegibilidade e Alinhamento ao Protocolo (PDR-0006 / PDR-0007)
- **Aderência Temática (PICOC):** O artigo aborda diretamente a arquitetura, governança e orquestração de **Agentic AI para Resposta a Incidentes em Nuvem** no modelo **SOC-as-a-Service (SOCaaS)**, integrando SIEM/SOAR, RAG (MITRE ATT&CK / playbooks), supervisão humana (*Bounded Autonomy*) e auditoria forense.
- **Avaliação de Comparison:** O Experimento 3 executa comparação quantitativa entre três modelos operacionais (*Manual SOC*, *Narrow-AI Assisted* e *Agentic + Governance*) sobre `2.000` incidentes simulados, embora baseado em simulação de eventos discretos parametrizada.
- **Avaliação de Estrato:** Publicado no periódico *Network* (MDPI), classificado como **Qualis A2** (percentil Scopus `79%`), sem necessidade de ressalva de estrato.

---

## Síntese do avaliador

O estudo **P97 (Alhumaidi et al., 2026)** combina uma revisão sistemática focada de **33 estudos** com a proposição de uma arquitetura de referência em **6 camadas (`SENSE, TRIAGE, GROUND, REASON, GOVERN, ACT`)** e um plano transversal de segurança e confiança para **Agentic AI-Driven SOC-as-a-Service (SOCaaS)** em ambientes de nuvem. Suas contribuições mais valiosas para a nossa RSL são: (1) a taxonomia de maturidade em três níveis (Narrow AI $\to$ Contextual LLM/RAG $\to$ Agentic Orchestration, Figura 3); (2) a formalização de quatro fronteiras de confiança (*evidence, knowledge, decision, execution*) e isolamento *multitenant* (Seção 5.1 e 5.3); e (3) a demonstração quantitativa da curva de sensibilidade do limiar de governança (Tabela 9 e Figura 9), que prova matematicamente por que a **autonomia limitada (*Bounded Autonomy*)** em torno de $\theta = 0.50$ captura quase todo o ganho de redução de MTTR (`6,8x`, de `59,5 min` para `8,8 min`) mantendo a exposição a ações de alto impacto não supervisionadas em apenas `1,29%`. A recomendação é de inclusão com ressalva metodológica, pois — como os próprios autores destacam com exemplar transparência — os quatro experimentos avaliam modelos substitutos (*Random Forest*, *TF-IDF* e filas Monte Carlo sintéticas) que comprovam viabilidade interna (*internal feasibility*) e não eficácia de um agente LLM em produção.

## Recomendação

`Incluir c/ ressalvas (estudo misto RSL + framework conceitual + simulação de componentes; validação empírica qualificada pelos próprios autores como viabilidade interna condicional a modelos substitutos [Random Forest, TF-IDF e filas estocásticas] e não eficácia em produção)`
