# Avaliação RSL — Estudo P34

**Artigo:** _Analysing the role of LLMs in cybersecurity incident management_ — G. Jones, D. Kasimatis, N. Pitropakis, R. Macfarlane, W. J. Buchanan (Edinburgh Napier University, UK + The American College of Greece)
**Arquivo:** P34-A2-s10207-025-01144-7.pdf (14 páginas)

> ⚠️ **Alerta de escopo:** estudo **primário empírico**, **diretamente no domínio de Resposta a Incidentes** (NIST 800-61, cenários reais), e explicitamente enquadrado como **"copilot/assistant"** — alinhado ao título da RSL. **Porém é não-agêntico**: avalia a qualidade de respostas de LLMs (prompt→resposta de turno único via API), sem autonomia/planejamento/uso de ferramentas/multi-agente. Posiciona-se no extremo **baixa-autonomia / copilot** do espectro.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                                        | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                                        | DOI                        |
| --- | ---------------------------------------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------- |
| P34 | International Journal of Information Security (Springer) (Vol. 24:228) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Artigo de pesquisa empírico (avaliação de LLMs; 1200 invocações, NIST 800-61, LLM-as-judge) | 10.1007/s10207-025-01144-7 |

_Evidências: cabeçalho p.1 ("Regular Contribution"; DOI; recebido 27/06/2025, aceito 19/10/2025, publicado 30/10/2025); "International Journal of Information Security (2025) 24:228"; © The Author(s) 2025. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)          | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | --------------------- | ---------------------------- | ----------------------- | ------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P34 | LLMs in IR management | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §4.1 (p.4), §6.1.1 (p.11)       | Núcleo **não-agêntico** (LLM como copilot de turno único; "agentes" só na revisão de trabalhos relacionados — Autobnb [26]). Cobre apenas a subdimensão de **supervisão humana / níveis de autonomia**: human-in-the-loop, autonomia em estágios (shadow → advisory → limited automation) e impacto na decisão. Ausentes planejamento, memória e uso de ferramentas como propriedades agênticas.                                                                                                                             |
| P34 | "                     | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §4.1-4.2 (p.4-6), §6.1.1 (p.11) | Arquitetura mínima (wrapper de prompt + OpenAI API) e harness de avaliação (b); **guardrails recomendados** (scores de confiança, abstenção, audit logs, aprovação do analista, least-privilege, red teaming) (c) — porém como **recomendações**, não como arquitetura agêntica implementada (sem orquestração/memória/observabilidade de agente).                                                                                                                                                                           |
| P34 | "                     | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §5, Tab. 1 (Apêndice) (p.8-12)  | Quantitativo extenso por **estágio do IR**: clarity, relevance, logical coherence, domain terminology, BERTScore, conciseness, coherence (Tab. 1); 1200 invocações (4 modelos × 10 cenários × 3 níveis × 10 repetições) (b); benefícios qualitativos — adequação por estágio (GPT-4o/3.5 p/ contenção/recuperação; o1/GPT-4 p/ análise/preparação) (a); evidência empírica real, mapeada ao NIST 800-61 (c). **Ressalva:** métricas são proxies de **qualidade textual via LLM-as-judge**, não desfechos operacionais de IR. |
| P34 | "                     | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §6.1, §6.1.1 (p.11)             | Cobertura **forte**: ética extensa (erosão de expertise humana, falsa confiança, cadeia de accountability, uso ofensivo de LLMs) + regulação (EU AI Act, GDPR) (a/b); **mecanismos de governança concretos** — human-in-the-loop, aprovação do analista, dual control, scores de confiança, provenance, deployment em estágios, audit logs, segregação de funções, red teaming, minimização de dados (c).                                                                                                                    |
| P34 | "                     | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §7 (p.12)                       | Direções explícitas: outros modelos generativos (locais), RAG + consulta iterativa, formatos de entrada com input humano, métricas quantitativas (mean response time), usabilidade via cenários/runbooks sob medida.                                                                                                                                                                                                                                                                                                         |
|     |                       | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P34 | Artigo de pesquisa empírico (avaliação de LLMs em IR) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (efetividade de LLMs em IR) e contribuições explícitos; foco em incident response bem delimitado (§1-§2).
- **QA2 = Y** — metodologia muito detalhada e replicável: modelos versionados (gpt-3.5-turbo, gpt-4-0125-preview, gpt-4o, o1-preview), 10 cenários, 3 níveis de contexto, 10 repetições (1200 invocações), mapeamento NIST 800-61, configurações default (reprodutíveis), exemplos de prompt e tabela completa de métricas (Apêndice).
- **QA3 = Y** — validação empírica substancial (1200 invocações, 4 modelos, 3 condições, cenários reais, métricas quanti+quali). **Ressalvas reconhecidas:** avaliação via **LLM-as-judge** (juiz/rubrica únicos) e ausência de validação de **correção operacional** por especialista humano.
- **QA4 = Y** — conclusões coerentes com os resultados (adequação modelo×estágio); limitações discutidas (limite de tokens, juiz único, scores podem não capturar correção operacional) + discussão ética/risco robusta.

## Parecer final do revisor

**Síntese.** Estudo empírico **diretamente sobre Resposta a Incidentes** (gestão de incidentes mapeada ao NIST 800-61, cenários reais), avaliando 4 LLMs como **copilots** de IR sob 3 níveis de contexto (1200 invocações). É, em termos de **domínio**, o estudo mais "IR-puro" do lote, e o enquadramento **copilot** casa com o título da RSL. Cobertura forte de **RQ3** (avaliação quantitativa por estágio), **RQ4** (ética/governança — entre as melhores) e **RQ5**. Entretanto, é **não-agêntico** (avaliação de respostas de LLM de turno único, sem autonomia/planejamento/ferramentas/multi-agente) → **RQ1 e RQ2 parciais**.

**Recomendação: INCLUIR COM RESSALVAS.** SCORE_RQ 4,0/5,0 e QA 4,0/4,0 (Banda Alta). Justifica-se pela **alta relevância ao domínio de IR + tema copilot + qualidade metodológica e ética**, mas com a ressalva central de que ocupa o extremo **baixa-autonomia/copilot** do espectro agêntico (útil, inclusive, como ponto de calibração do eixo de níveis de autonomia — cf. taxonomia de P33). Evidência é de **qualidade textual (LLM-as-judge)**, não de desfecho operacional de IR.

> ⚠️ **Decisão de protocolo:** se o protocolo exigir **sistemas agênticos** (autonomia/planejamento/uso de ferramentas), P34 entraria, no máximo, como estudo de **LLM-copilot de baixa autonomia** — distinto de P22/P25/P27/P28 (agênticos). Contraste com P30 (não-agêntico **e** fora de IR → excluído): P34 é não-agêntico **mas dentro de IR**, o que sustenta a inclusão com ressalva.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _International Journal of Information Security_ (insumo: Q2).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2025 ✓; veículo Springer IJIS ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
