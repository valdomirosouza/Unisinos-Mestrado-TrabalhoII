# Avaliação RSL — Estudo P21

**Artigo:** _Small Language Model Agent for the Operations of Continuously Updating ICT Systems_ — N. Fukuda, H. Nozue, H. Oishi (NTT Access Network Service Systems Laboratories)
**Arquivo:** P21-A1-Small_Language_Model_Agent...pdf (12 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.       | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                        | DOI                         |
| --- | --------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ----------------------------------------------------------- | --------------------------- |
| P21 | IEEE Access (Vol. 13) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa c/ avaliação experimental (2 benchmarks) | 10.1109/ACCESS.2025.3544637 |

_Evidências: cabeçalho p.1 (DOI, recebido 24/01/2025, publicado 24/02/2025); rodapé "VOLUME 13, 2025"; licença CC-BY-NC-ND 4.0; afiliação NTT (p.1). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                         | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                              |
| --- | --------------------- | ---------------------------- | ----------------------- | ------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P21 | SLM Agent for ICT Ops | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §III "Problem Settings" (p.3), §I, §IV (p.4-6) | Modelo decisório formal — política π(â\|τ) sobre trajetórias (c); capacidades de planejamento (nested thoughts/decomposição), memória (blocks + retrieval keys) e uso de ferramentas (scripts no agente, log parsing) (b); autonomia caracterizada em cenário "conservador" de produção com supervisão (operador define objetivo, gating de segurança) (a).                     |
| P21 | "                     | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §IV + Algoritmos 1-3 (p.4-6), §V.C (p.7)       | Arquitetura: SLM agent c/ nested thoughts + dynamic prompt reconfiguration (a); stack explícito — LLaMA2 7B/Gemma2 9B/Mistral 7B quantizados, SentenceTransformer all-mpnet-base-v2, log parser regex, GPU 2080Ti (b); capacidades avançadas: retrieval por template, seleção de exemplares diversa, guardrail de segurança em pós-processamento (c).                           |
| P21 | "                     | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §V.D, Figs. 6-11 (p.7-10)                      | Quantitativo robusto: ALFWorld — proposta+LLaMA2 96,3% > ReAct GPT-4 85,8% e RAP GPT-4 94,8%; WideEnet — Mistral 88,9%, LLaMA2 3,70%→87,0%; adaptação a updates 29,4%→78,8%; overhead 5,2× chamadas-LM/passo, 2,1× ReAct (b); benefícios qualitativos: baixo custo, confidencialidade, adaptação a atualizações (a); evidência forte — 2 benchmarks + baselines + ablações (c). |
| P21 | "                     | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §I (p.1-2), §VI (p.10)                         | Desafios técnicos fortes — alucinação intolerável em produção, shortcut reasoning, abrangência das trajetórias, custo de construção do ambiente, teste de verificação (a). Confidencialidade (evitar API proprietária) e gating de segurança como mecanismo (b/c parciais), mas sem discussão de ética/accountability/governança ampla.                                         |
| P21 | "                     | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §VI "Conclusion and Discussion" (p.10)         | Lacunas e direções explícitas: extração de trajetórias de documentos multimodais; construção de ambientes de verificação de baixo custo; extensão a microsserviços/cloud/5G/WAN; aplicação a provisionamento, RCA e troubleshooting; supressão de erros via reflexão (fora do escopo).                                                                                          |
|     |                       | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                                                |                                                                                                                                                                                                                                                                                                                                                                                 |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                              | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P21 | Artigo de pesquisa c/ avaliação experimental (2 benchmarks) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (operação autônoma de sistemas ICT; custo/confidencialidade de LLMs API; limites de raciocínio do SLM) e solução agêntica explícitos (§I, p.1-2).
- **QA2 = Y** — pseudocódigo completo (Algoritmos 1-3), formulação formal (§III), hiperparâmetros (cutoff µ+σ, 2 exemplares), modelos, embedding e hardware (§V.C). Ressalva menor: WideEnet é proprietário/confidencial e não há repositório de código — mas o método e o benchmark ALFWorld (público, exemplares especificados) são replicáveis.
- **QA3 = Y** — validação empírica extensa: 2 benchmarks (sintético ALFWorld + rede real WideEnet), baselines (Act/ReAct/RAP), e ablações (shortcut-aware vs unaware, adaptação a updates, overhead).
- **QA4 = Y** — conclusões decorrem dos resultados; limitações discutidas (abrangência das trajetórias estendidas, custo de construção do ambiente) com direções de mitigação (§VI).

## Parecer final do revisor

**Síntese.** Estudo empírico forte de um agente baseado em **Small Language Model** para operação autônoma de sistemas ICT em ambiente continuamente atualizado, com modelo decisório formal, planejamento/memória/uso de ferramentas e guardrails de segurança. Aderência elevada a **RQ1** (definições/decisão), **RQ2** (arquitetura/orquestração) e **RQ3** (evidências quantitativas robustas, incl. benchmark de operação de rede real). **RQ5** bem coberta; **RQ4** parcial (desafios técnicos e confidencialidade fortes, mas governança/ética ampla ausente). É o primeiro trabalho a focar SLM em operações de ICT — alta relevância metodológica para a RSL.

**Recomendação: INCLUIR.** SCORE_RQ 4.5/5.0 e QA 4.0/4.0 (Banda Alta). Estudo central para as RQs de definição, arquitetura e evidências de Agentic AI. Observação de escopo: o domínio é **operação de sistemas ICT/redes** (AIOps), adjacente a Resposta a Incidentes — o próprio artigo cita aplicabilidade a RCA, troubleshooting e recuperação, o que reforça a pertinência ao tema da RSL, ainda que não seja IR em sentido estrito.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → IEEE Xplore / Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, periódico _IEEE Access_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios de elegibilidade verificáveis no PDF atendidos (Ano 2025 ✓; veículo IEEE Access ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
