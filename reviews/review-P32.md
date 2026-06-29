# Avaliação RSL — Estudo P32

**Artigo:** _GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems_ — W. Zhang, Z. Yang, F. Peng, L. Zhang, Y. Chen, R. Chen (State Grid Corporation of China + Beihang University)
**Arquivo:** P32-A2-electronics-15-00243-v2.pdf (19 páginas)

> ℹ️ **Nota:** mesmo grupo (SGCC + Beihang) e autores parcialmente sobrepostos a **P31/LEMAD** (W. Zhang, L. Zhang, F. Peng). Trabalhos distintos (P31 = detecção de anomalias; P32 = localização de causa + recuperação), mas registrar a sobreposição de equipe/dados para a análise de independência dos estudos.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                   | Ano  | Cit.                                                            | SJR                               | Qualis                                          | Tipo                                                                                       | DOI                         |
| --- | --------------------------------- | ---- | --------------------------------------------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------- |
| P32 | Electronics (MDPI) (Vol. 15, 243) | 2026 | [VERIFICAR] (base indexadora — provável baixa, pub. 05/01/2026) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Artigo de pesquisa empírico (GNN+LLM; 3 datasets, 6 baselines, ablação, injeção de falhas) | 10.3390/electronics15010243 |

_Evidências: cabeçalho p.1 (DOI; recebido 14/11/2025, aceito 29/12/2025, publicado 05/01/2026); "Electronics 2026, 15, 243"; MDPI, CC-BY. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                               | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)          | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --- | ------------------------------------ | ---------------------------- | ----------------------- | ------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P32 | GALR (GNN + LLM agent, RCA+recovery) | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §3.4-3.5 (p.10-11), Algoritmo 1 | Componente agêntico **parcial**: "LLM-based recovery agent" com retrieval (biblioteca de casos = memória), geração de plano estruturado (passos/verificação/rollback = planejamento) e verificação de consistência (a/b parciais). Porém o núcleo é **GNN/GAT (não-agêntico)**; autonomia é **delimitada** (geração separada da execução, escalonamento manual), sem loop de planejamento autônomo nem uso amplo de ferramentas (perfil próximo de P23/TAMO). |
| P32 | "                                    | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §3 (p.5-11), Algoritmo 1        | Arquitetura unificada GNN+LLM, pipeline janelado closed-loop (a); stack — GAT c/ edge attention temporal, grafo multimodal, LLM (tripla de anomalia + geração), RAG/biblioteca de casos, embeddings/cosseno, templates de comando (b); **guardrails fortes** — verificação de consistência vs playbooks, separação geração/execução, espaço de ações restrito, allowlists/validação de parâmetros, observabilidade multimodal (c).                            |
| P32 | "                                    | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §4.3-4.5, Tabs. 3-5 (p.14-16)   | Quantitativo: localização Top-k/MRR (GALR MRR médio 0,931 vs PDiagnose 0,902) sobre 6 baselines; recuperação RAG 79,2/75,8/70,1% vs zero-shot/few-shot (Tab. 4); **ablação** (Tab. 5) (b); benefícios qualitativos — desambiguação grafo+semântica, interpretabilidade (a); evidência — 3 datasets, injeção de falhas (c). Ressalvas: recuperação avaliada **offline** (validade de ação, não operacional) e só **2 execuções** sem teste de significância.   |
| P32 | "                                    | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §5 "Discussion", §6 (p.16-17)   | Desafios técnicos discutidos de forma **equilibrada** — escalabilidade/latência, dependência da qualidade de logs/monitoramento, distribution shift, alucinação no plano de recuperação (a); **mecanismos de segurança/governança fortes** — espaço de ações restrito, validação de parâmetros, allowlists, escalonamento manual, consistency check (c). Ética propriamente dita (viés, dual-use) ausente (b).                                                |
| P32 | "                                    | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §5-§6 (p.16-17)                 | Direções explícitas e reflexivas: escalabilidade/latência (anotação LLM seletiva/incremental + caching), guardrails de segurança mais estritos, verificação online controlada + benchmarks de efetividade de recuperação; reconhece limitações (2 runs, offline, cobertura de injeção de falhas).                                                                                                                                                             |
|     |                                      | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P32 | Artigo de pesquisa empírico (GNN+LLM, microsserviços) | **Y** (1.0) | **P** (0.5) | **Y** (1.0) | **Y** (1.0) | **3.5 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (diagnóstico e recuperação tratados separadamente; playbooks frágeis; saídas de LLM precisam de grounding/verificação) e solução (GALR GNN+LLM closed-loop) explícitos (§1, 3 lacunas).
- **QA2 = P** — Algoritmo 1, equações e detalhes de implementação/hiperparâmetros (§4.3) bem descritos, com 1 dataset público (SockShop) e 6 baselines; **porém** os 2 datasets SGCC são **disponíveis "sob solicitação"** (proprietários), não há repositório de código e os resultados são média de **apenas 2 execuções** → replicabilidade parcial.
- **QA3 = Y** — validação empírica multi-dataset (3), 6 baselines e ablação para a localização. **Ressalvas relevantes** (reportadas pelos autores): recuperação avaliada **offline** (validade ao nível de ação, sem execução real) e **sem teste de significância estatística** (2 runs).
- **QA4 = Y** — conclusões coerentes e **exemplarmente caveatadas** (lista explícita de 3 limitações); discussão de limitações ampla com direções de mitigação.

## Parecer final do revisor

**Síntese.** Estudo empírico que une **GNN (GAT) para localização de causa raiz** + **agente LLM com RAG para geração de planos de recuperação**, em sistemas de microsserviços, fechando o loop percepção→localização→recuperação. Aderência alta a **RQ2** (arquitetura + guardrails de segurança) e **RQ3** (localização bem avaliada); **RQ5** forte e reflexiva; **RQ1 e RQ4 parciais**. O componente **agêntico é parcial** — o "agente" é um gerador RAG de recuperação sobre um núcleo GNN (perfil próximo de P23/TAMO), com autonomia **delimitada** (geração separada da execução, escalonamento manual). Destaque positivo: **mecanismos de segurança/verificação** (consistency check vs playbooks, espaço de ações restrito, validação de parâmetros) — relevantes para a etapa de **remediação** do IR.

**Recomendação: INCLUIR.** SCORE_RQ 4,0/5,0 e QA 3,5/4,0 (Banda Alta), com **ressalvas de evidência** (recuperação avaliada apenas offline/ao nível de ação; 2 execuções sem significância estatística — reportadas honestamente pelos autores). Bom par de comparação com P23 (RCA + agente LLM) e P22/P31 (remediação/AIOps), e útil para o eixo de **safety/guardrails de recuperação**. Domínio: RCA + recuperação em microsserviços (diagnóstico + remediação) — adjacente a IR, não específico de segurança.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar. ⚠️ Publicado em 05/01/2026 — contagem possivelmente baixa/0; atenção ao critério "Citações ≥ 1".
- **SJR (quartil)** → Scimago, _Electronics_ (MDPI) (insumo: Q2).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2026 ✓; veículo MDPI Electronics ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
