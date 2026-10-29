# Parecer — P106: Agentic AI for Autonomous Cyber Threat Hunting and Adaptive Defense in Dynamic Security Environments

> Avaliador: Gemini · Data: 2026-10-29 · Prompt: prompt-P106.md (template v1.1.0)

## Tabela A — Identificação e PICOC

| Campo | Conteúdo |
|---|---|
| Veículo / ano / DOI | 2025 IEEE International Conference on Electro Information Technology (eIT, pp. 316–321) · 2025 · `10.1109/eit64391.2025.11103697` |
| Qualis · SJR (insumo) | `B1` (derivado do percentil Scopus `42%` da série IEEE EIT — PDR-0006) · SJR `N/D` (citações: OpenAlex `7` · Crossref `8` · Scopus `7`) |
| Tipo / paradigma | Estudo primário descritivo/experimental de baixa especificação técnica (declara nominalmente *Agentic AI*, porém descreve apenas de forma genérica o uso de *Machine Learning* [`CNN`, `RNN`] e *Deep Reinforcement Learning* [`DRL`] sobre *datasets* tabulares de detecção de intrusão, exibindo como único artefato técnico 14 linhas de pré-processamento `scikit-learn` em CSV) |
| **P** (Population) | Redes corporativas e Centros de Operações de Segurança (*SOCs*) sujeitos a ataques de força bruta, *SQL injection*, DDoS, *zero-day exploits* e ameaças persistentes avançadas (*APTs*) |
| **I** (Intervention) | Intervenção denominada nominalmente como *"Agentic AI"*, mas descrita na Seção II.B (p. 317) exclusivamente como combinação genérica de redes neurais convolucionais (`CNN` para padrões espaciais de tráfego), redes recorrentes (`RNN` para dados sequenciais) e aprendizado por reforço profundo (`DRL`), sem LLM, sem arquitetura de agentes, sem especificação de estados/ações/recompensas e sem diagrama arquitetural |
| **C** (Comparison) | **Comparação tabular reportada sem caracterização metodológica do *baseline* (Tabela 1, p. 319):** coluna `"Traditional Method"` (descrita no texto apenas como *"traditional rule-based systems"* ou *"traditional interventions"*, sem especificar qual ferramenta SIEM/IDS, conjunto de regras ou protocolo experimental originou os tempos reportados) |
| **O** (Outcomes) | Valores agregados reportados na Seção III.A–C e Tabela 1 (pp. 318–319) comparando `"AI Model Performance"` vs. `"Traditional Method"`: acurácia `98,2%` vs. `85,7%`; precisão `96,5%` vs. `78,3%`; *Recall* `97,8%` vs. `82,4%`; `F1 Score` `97,1%` vs. `80,2%`; `MTTD` `2,3 Seconds` vs. `15,7 Minutes` (`-99,8%`); `MTTR` `5,1 Seconds` vs. `22,4 Minutes` (`-99,6%`); taxa de falsos positivos (`FPR`) `1,8%` vs. `14,3%`; taxa de falsos negativos (`FNR`) `2,2%` vs. `17,6%`; e acurácia em *zero-day exploits* de `92,6%` vs. `34,8%` |
| **C** (Context) | Experimentos declarados sobre os conjuntos de dados `CICIDS` e `DARPA` (mencionando também nominalmente `Cuckoo Sandbox`, `Metasploit` e `MITRE CALDERA` na Seção II.A.i, p. 317, sem detalhar sua configuração ou execução) |

## Tabela B — Cobertura das RQs

| RQ | Escopo | Nota | Justificativa (seção / página do PDF) |
|---|---|---|---|
| RQ1 | Arquiteturas / padrões agênticos | **N** (`0.0`) | O artigo **não apresenta nenhuma arquitetura agêntica**. Não há diagrama de componentes, protocolo de comunicação entre agentes, modelo cognitivo (BDI, ReAct, LLM) ou sequer a formulação do processo de decisão de Markov (MDP: espaço de estados, ações e função de recompensa) para o suposto `DRL`. A menção a `CNN`, `RNN` e `DRL` restringe-se a três frases genéricas na Seção II.B (p. 317), e o único trecho técnico do artigo inteiro é um *snippet* elementar de 14 linhas em Python (`pandas.read_csv`, `StandardScaler` e `train_test_split` sobre `CICIDS_dataset.csv`, Seção II.C.i, p. 318). |
| RQ2 | Ganhos vs. *workflow* tradicional | **P** (`0.5`) | A Tabela 1 (p. 319) e a Seção III.A–B (p. 318) contrastam numericamente `"AI Model Performance"` com `"Traditional Method"` (`MTTD` de `2,3s` vs. `15,7 min`; `MTTR` de `5,1s` vs. `22,4 min`; acurácia de `98,2%` vs. `85,7%`). Recebe nota parcial mínima (`P`) porque o *baseline* `"Traditional Method"` não possui qualquer definição técnica, configuração experimental ou referência empírica rastreável. |
| RQ3 | Ciclo de vida coberto | **P** (`0.5`) | O texto afirma cobrir monitoramento em tempo real, detecção de ameaças (*threat hunting*) e resposta automatizada (Seção II.B, p. 317), porém não descreve nenhum mecanismo, *playbook* ou integração de sistema capaz de executar contenção ou remediação a partir da classificação tabular do `CICIDS_dataset.csv`. |
| RQ4 | Métricas (MTTD, MTTR, F1 etc.) | **P** (`0.5`) | Reporta na Tabela 1 (p. 319) acurácia (`98,2%`), precisão (`96,5%`), *recall* (`97,8%`), `F1-Score` (`97,1%`), `MTTR` (`5,1s`), `MTTD` (`2,3s`), `FPR` (`1,8%`) e `FNR` (`2,2%`). Recebe `P` porque não há desagregação por modelo (`CNN` vs. `RNN` vs. `DRL`) nem por *dataset* (`CICIDS` vs. `DARPA`), e não há explicação metodológica de como tempos operacionais de resposta (`MTTR = 5,1s`) foram extraídos de *datasets* estáticos de tráfego de rede. |
| RQ5 | Governança, *guardrails*, riscos | **N** (`0.0`) | O artigo não implementa nem especifica qualquer mecanismo de governança, *guardrails*, validação *human-in-the-loop* ou controle de risco operacional. Limita-se a comentários genéricos de trabalhos futuros na Seção V.C (p. 320) sugerindo que pesquisas futuras deveriam investigar *Explainable AI (XAI)*, treinamento adversarial e ética. |

**SCORE_RQ:** `1.5 / 5.0`

## Tabela C — Qualidade (DARE)

| Critério | Descrição | Nota | Justificativa |
|---|---|---|---|
| QA1 | Critérios de inclusão / escopo | **P** (`0.5`) | A Seção II.A.i (p. 317) lista nominalmente `CICIDS`, `DARPA`, `Cuckoo Sandbox`, `Metasploit` e `MITRE CALDERA`, mas não especifica qual versão do `CICIDS` (2017 ou 2018) ou do `DARPA` foi utilizada, quantos registros compuseram a amostra nem quais cenários de ataque foram efetivamente executados. |
| QA2 | Busca / desenho experimental | **N** (`0.0`) | Completamente irreprodutível. Embora a Seção II.C (*Sufficient Detail for Reproduction*, pp. 317–318) afirme disponibilizar documentação e *scripts* no GitHub (*"provided on GitHub, containing information on Model Training Code, Deployment Scripts and Data Preprocessing Scripts"*), **nenhum link ou identificador de repositório GitHub é fornecido no artigo**. O único código exibido (p. 318) realiza apenas `dropna()`, `StandardScaler()` e `train_test_split()` sobre um arquivo CSV, sem qualquer definição de arquitetura neural, hiperparâmetros, ambiente de reforço ou método de medição de `MTTD`/`MTTR`. |
| QA3 | Validação dos primários / resultados | **N** (`0.0`) | Os resultados numéricos da Tabela 1 (p. 319) carecem de validade interna demonstrável: o artigo não explica qual modelo gerou os `98,2%` de acurácia nem como um classificador supervisionado treinado via `train_test_split` em dados tabulares estáticos (`CICIDS_dataset.csv`) poderia produzir medições empíricas de `MTTR = 5,1 segundos` contra `22,4 minutos` de um método tradicional não identificado. |
| QA4 | Síntese / descrição dos estudos | **P** (`0.5`) | O texto apresenta a Tabela 1 (p. 319) e discute genericamente falsos positivos e ataques adversariais na Seção IV.B (p. 319), mas é altamente repetitivo, puramente discursivo e omite qualquer detalhamento técnico dos modelos ou dos experimentos. |

**SCORE_QA:** `1.0 / 4.0` · **Banda:** `Baixa`

---

## Detalhamento Analítico (Etapa 0 e Etapa 1)

### 1. Elegibilidade e Decisão sobre o Critério `E2` (Etapa 0)
- **Análise da Flag Central da Triagem (Agência Nominal vs. Critério `E2`):** A triagem sinalizou que o parecer de texto completo deveria decidir sobre a aplicação do critério de exclusão **`E2`** (*ausência de perspectiva de IA agêntica / sistemas autônomos de agentes*), confrontando P106 com os precedentes de inclusão com ressalvas (`P73`, `P88`, `P91`) e com os precedentes de exclusão pós-avaliação (`P26`, `P29`, `P30`).
- **Distinção Técnica em Relação a `P73`, `P88` e `P91`:** Nos estudos não-LLM retidos com ressalvas (`P73`, `P88` e `P91`), os autores efetivamente especificaram uma arquitetura operacional de agentes autônomos ou *loops* de decisão/contenção (por exemplo, em P91, uma arquitetura de 4 estágios com modelos especificados, limiares de anomalia, ações concretas de contenção por tipo de incidente e tabela de piloto de 30 dias). Em **P106**, ao contrário, o termo *"Agentic AI"* é utilizado **exclusivamente como *buzzword* nominal no título e na prosa discursiva**:
  1. Não existe arquitetura de agentes, diagrama de sistema, agente de software, LLM, orquestrador ou sequer especificação formal de um agente de *Reinforcement Learning* (sem estados, ações ou função de recompensa);
  2. O único elemento técnico concreto em todas as 6 páginas do artigo é um bloco de 14 linhas de código Python elementar (`pandas.read_csv('CICIDS_dataset.csv')`, `StandardScaler`, `train_test_split`, p. 318);
  3. O repositório GitHub prometido na Seção II.C (p. 317) não existe no texto (nenhuma URL foi incluída);
  4. Os valores de `MTTD = 2,3s` e `MTTR = 5,1s` (Tabela 1, p. 319) não possuem lastro metodológico no procedimento experimental descrito, resultando em **`SCORE_QA = 1.0 / 4.0` (Banda `Baixa`, `< 1.5`)**.
- **Enquadramento Normativo (`E2` cumulado com Banda `Baixa` de Qualidade, e registro de `PDR-0006`/`PDR-0007`):** Diante da agência puramente nominal sem arquitetura de agentes (`E2`) e da insuficiência metodológica severa (`SCORE_QA = 1.0`, Banda `Baixa`), a recomendação técnica rigorosa é a **exclusão pelo critério `E2`** (em consonância com os precedentes `P26`, `P29` e `P30`). Caso o revisor humano decida pela retenção condicional na fase de consolidação, registra-se desde já que a série *IEEE International Conference on Electro Information Technology (eIT)* possui percentil Scopus de `42%` (**Qualis B1** pelo `PDR-0006`), exigindo obrigatoriamente a **`RESSALVA DE ESTRATO OBRIGATÓRIA`** (`PDR-0007`).

---

## Síntese do avaliador

O estudo **P106** (Sheth et al., *IEEE eIT*, 2025) emprega o termo *"Agentic AI"* no título e ao longo do texto de forma **puramente nominal**, sem propor ou descrever qualquer arquitetura de agentes, protocolo de decisão autônoma, LLM ou formulação de *Reinforcement Learning*. O único conteúdo técnico explícito do artigo resume-se a 14 linhas de código *boilerplate* do `scikit-learn` (`StandardScaler` e `train_test_split` sobre `CICIDS_dataset.csv`, p. 318), acompanhadas da promessa de um repositório GitHub cuja URL foi omitida (p. 317) e de uma tabela única (Tabela 1, p. 319) que reporta `MTTD = 2,3s` e `MTTR = 5,1s` sem explicar como métricas temporais de resposta e recuperação foram obtidas a partir de *datasets* estáticos de classificação de tráfego e contra um *baseline* tradicional não caracterizado. O artigo obtém `SCORE_RQ = 1.5 / 5.0` e `SCORE_QA = 1.0 / 4.0` (**Banda Baixa**), recomendando-se sua **exclusão pelo critério E2** (agência nominal sem arquitetura de agentes, alinhado aos precedentes `P26/P29/P30`), registrando-se subsidiariamente a `RESSALVA DE ESTRATO OBRIGATÓRIA` (`Qualis B1`, `PDR-0006`/`PDR-0007`).

## Recomendação

**Excluir (critério E2 — IA agêntica puramente nominal restrita a menção genérica de CNN/RNN/DRL e snippet elementar de train_test_split em CSV sem arquitetura de agentes, cumulado com qualidade metodológica Baixa [SCORE_QA = 1.0 < 1.5], análogo aos precedentes P26/P29/P30; subsidiariamente, em caso de retenção pelo revisor humano, aplica-se RESSALVA DE ESTRATO OBRIGATÓRIA — série IEEE EIT Qualis B1, percentil 42%, PDR-0006/PDR-0007).**
