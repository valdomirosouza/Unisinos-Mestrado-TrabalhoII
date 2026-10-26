# Avaliação Sistemática de Literatura — Estudo P21

**Artigo avaliado:** *Small Language Model Agent for the Operations of Continuously Updating ICT Systems*  
**Autores:** Nobukazu Fukuda; Haruhisa Nozue; Haruo Oishi  
**Arquivo fonte:** `P21-A1-Small_Language_Model_Agent_for_the_Operations_of_Continuously_Updating_ICT_Systems.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — 2025 (p. 1 / p. 37522).
- **Publicação ≠ NULL (veículo identificável):** Sim — *IEEE Access*, Volume 13, pp. 37522–37533.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science, IEEE Xplore ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *IEEE Access*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P21 | IEEE Access (Vol. 13, pp. 37522–37533) | 2025 | `[VERIFICAR]` (base indexadora: Scopus / IEEE Xplore / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Artigo de pesquisa empírica / Proposta de framework com avaliação experimental em benchmarks (*Research Article*) | `10.1109/ACCESS.2025.3544637` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P21 | Small Language Model Agent for the Operations of Continuously Updating ICT Systems | RQ1 | Respondida Plenamente | T (1.0) | Seção I (pp. 37522–37523); Seção III (pp. 37524–37525); Seção IV-A e IV-B (pp. 37525–37527) | **(a) Autonomy definition:** Formaliza o agente autônomo interagindo em múltiplos passos com o sistema de TIC ($\tau_T = (o_1, \rho_1, a_1, \dots, a_{T-1}, o_T)$) para cumprir objetivos operacionais sob regime conservador de produção (sem permissão de *reset* após erro). **(b) Core characteristics:** Decomposição hierárquica em subtarefas (*Nested Thoughts* com tags `begin`/`end`), memória de trajetórias estruturada em blocos com *timestamps*, execução de scripts Python internos para verificação de estado e reconfiguração dinâmica de *prompts*. **(c) Decision-making model:** Política $\pi(\hat{a}_t | (x^1, \hat{a}^1), \dots, x_t)$ guiada por exemplares *few-shot* com seleção consciente de diversidade e bloqueio preventivo pós-processamento caso a ação divirja dos templates operacionais. |
| P21 | Small Language Model Agent for the Operations of Continuously Updating ICT Systems | RQ2 | Respondida Plenamente | T (1.0) | Figuras 1–4 (pp. 37523–37526); Seção IV-A e IV-B (pp. 37525–37527); Algoritmos 1–3 (pp. 37526–37527); Seção V-C e V-D (pp. 37528–37529) | **(a) Architecture type:** Agente autônomo baseado em *Small Language Model* (SLM) com decomposição hierárquica de trajetórias em blocos pai-filho e recuperação dinâmica de contexto. **(b) Tools/frameworks:** Implementação em Python sobre SLMs quantizados (*LLaMA2-7B*, *Gemma2-9B*, *Mistral-7B*) executados em GPU única (*NVIDIA GeForce 2080Ti 11GB*), *SentenceTransformer* (`all-mpnet-base-v2`), parser de logs por expressões regulares e execução local de scripts Python. **(c) Advanced capabilities:** Adaptação contínua a atualizações de manuais via priorização de *timestamps*, amostragem de exemplares com diversidade de parâmetros para mitigar *shortcut reasoning*, e *guardrail* de pós-processamento (`safety_threshold`, Algoritmo 1, Linha 9). |
| P21 | Small Language Model Agent for the Operations of Continuously Updating ICT Systems | RQ3 | Respondida Plenamente | T (1.0) | Seção V-A a V-D (pp. 37528–37531); Figuras 6 a 11 (pp. 37528–37529) | **(a) Qualitative benefits:** Viabiliza automação agêntica local preservando confidencialidade operacional (sem envio de dados a APIs externas) e baixo consumo de hardware (4,7 GB de VRAM no LLaMA2-7B), mantendo conformidade estrita com manuais atualizados. **(b) Quantitative benefits / metrics:** No benchmark *ALFWorld* (134 tarefas), atingiu 96,3% de taxa de sucesso com LLaMA2-7B, superando *ReAct* (85,8%) e *RAP* (94,8%) com GPT-4; a seleção com diversidade elevou o *two-shot* de 84,3% para 96,3%. No benchmark real de operações de rede *WideEnet* (85 cenários, ex. *path switching* em switches Ethernet), elevou o sucesso do LLaMA2 de 3,70% (*ReAct*) para 87,0% e alcançou 88,9% com Mistral-7B; após 3 atualizações de ambiente, elevou a taxa de sucesso de 29,4% para 78,8%, com *overhead* médio de 5,2 chamadas de LM por passo (2,1× o *ReAct*). **(c) Evidence level:** Avaliação experimental robusta em benchmark público (*ALFWorld*) e ambiente realista de operações de rede comercial (*WideEnet*). |
| P21 | Small Language Model Agent for the Operations of Continuously Updating ICT Systems | RQ4 | Parcialmente Respondida | P (0.5) | Seção I (p. 37523); Seção IV-B-IV (p. 37527); Seção V-D e Figura 12 (pp. 37530–37531); Seção VI (p. 37531) | **(a) Technical challenges:** Demonstra empiricamente o fenômeno de *shortcut reasoning* em SLMs, intolerância a alucinações em ambientes de produção sem possibilidade de *rollback/reset*, *overhead* de chamadas de inferência (2,1× *ReAct*), erros residuais de formatação de saída (Figura 12) e alto esforço manual para estruturar trajetórias estendidas. **(b) Ethical/governance challenges:** Aborda confidencialidade de procedimentos operacionais de redes e risco de perdas severas por *outages*, mas não aprofunda dilemas éticos ou *accountability* regulatória. **(c) Governance mechanisms:** Implementa trava de segurança pós-processamento baseada em similaridade de template ($s_e^r < \text{safety\_threshold}$) que aborta comandos fora da política operacional antes da execução no ambiente. |
| P21 | Small Language Model Agent for the Operations of Continuously Updating ICT Systems | RQ5 | Respondida Plenamente | T (1.0) | Seção V-D (p. 37531); Seção VI (p. 37531) | Aponta lacunas e direções futuras concretas: (1) extração automatizada de trajetórias estruturadas a partir de manuais operacionais multimodais não estruturados (contendo tabelas, fluxogramas e diagramas); (2) construção de ambientes simulados de baixo custo (ex.: *network digital twins*) para validação pré-produção de agentes; (3) integração de técnicas de *self-reflection* ou exemplares negativos para coibir erros de formatação de saída em SLMs; e (4) expansão para *root cause analysis*, *troubleshooting* e ambientes de nuvem, microsserviços e 5G/WAN. |
| **P21** | **TOTAL (SCORE_RQ)** | — | **4.5 / 5.0** | **4T, 1P** | — | Excelente cobertura em definição de autonomia, arquitetura de engenharia com SLMs, validação experimental quantitativa e mapeamento de lacunas de pesquisa. |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P21 | Artigo de pesquisa empírica / Proposta de framework com avaliação experimental em benchmarks | Y (1.0) | Y (1.0) | Y (1.0) | Y (1.0) | **4.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** A Seção I (pp. 37522–37523) define com precisão o problema operacional em sistemas de TIC (sobrecarga de operadores, atualizações frequentes de manuais/políticas pós-incidentes, proibição de alucinações em produção e restrições de confidencialidade/custo de LLMs proprietários via API) e propõe um framework específico para viabilizar agentes baseados em SLMs locais.
- **QA2 — Metodologia Replicável (Y = 1.0):** A metodologia é formalizada matematicamente na Seção III e detalhada na Seção IV com três algoritmos completos (Algoritmos 1, 2 e 3, pp. 37526–37527), equação de corte dinâmico ($\Delta_i > \mu + \sigma$), especificação exata dos modelos avaliados (*LLaMA2-7B*, *Gemma2-9B*, *Mistral-7B*, *SentenceTransformer* `all-mpnet-base-v2`), hardware (*NVIDIA GeForce 2080Ti 11GB*) e exemplo literal de *prompt* e resposta (Figura 12, p. 37530).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Avaliação experimental abrangente em dois benchmarks distintos: *ALFWorld* (134 configurações) e *WideEnet* (85 configurações de teste extraídas de manuais reais de operações de redes Ethernet comerciais), comparando contra três *baselines* (*Act*, *ReAct*, *RAP*) e avaliando adaptação a atualizações incrementais e custo computacional (Figuras 6 a 11, pp. 37528–37531).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões derivam diretamente dos resultados empíricos, e o artigo analisa de forma transparente um caso de falha do método (Figura 12, pp. 37530–37531), além de discutir limitações práticas de implantação em produção na Seção VI (p. 37531).

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P21 investiga diretamente a operação autônoma de sistemas de TIC (AIOps / gerência de redes) sujeitos a atualizações contínuas decorrentes de relatórios de vulnerabilidade e lições aprendidas de incidentes passados. Propõe uma arquitetura inovadora baseada em *Small Language Models* (SLMs) executados localmente (preservando confidencialidade e reduzindo custos), combinando decomposição hierárquica (*Nested Thoughts*), reconfiguração dinâmica de *prompts*, mitigação de *shortcut reasoning* e *guardrails* de verificação de templates antes da execução de comandos, atingindo `SCORE_RQ = 4.5/5.0` e nota máxima de qualidade `SCORE_QA = 4.0/4.0` (Banda Alta).
- **Recomendação:** **INCLUIR** — Artigo altamente relevante e metodologicamente rigoroso (`SCORE_QA = 4.0/4.0`), oferecendo contribuições centrais para a RSL sobre como viabilizar agentes locais seguros, econômicos e adaptáveis para execução de procedimentos operacionais e mitigação em infraestruturas críticas de TIC.
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science, IEEE Xplore ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *IEEE Access* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
