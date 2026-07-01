# Avaliação RSL — Estudo P4

**Artigo:** _LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead_ — J. He, C. Treude, D. Lo (Singapore Management University)
**Arquivo:** P4-A2 - LLM-Based Multi-Agent Systems for Software Engineering Literature Review Vision and the Road Ahead.pdf (30 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                                         | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                      | DOI                                                |
| --- | ----------------------------------------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| P4  | Manuscrito ACM (veículo não nomeado no PDF); arXiv:2404.04834v4 [cs.SE] | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Revisão sistemática (estudos primários) + estudos de caso | [VERIFICAR] (placeholder `10.1145/nnnnnnn` no PDF) |

_Evidências: p.1 (© 2025 Association for Computing Machinery; ACM Reference Format; rodapé "Vol. 1, No. 1, Article. Publication date: July 2025"; marca arXiv:2404.04834v4 [cs.SE], 18 Jul 2025). **O veículo final (periódico/conferência) não é nomeado no PDF e o DOI é placeholder** — trata-se de manuscrito/preprint aceito ACM. Revisão sistemática de 71 estudos primários (DBLP + snowballing, Sec. 3) + 2 estudos de caso (Sec. 4). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                               | RQ                           | Veredito              | Símbolo       | Evidência (seção/pág.)             | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | ------------------------------------ | ---------------------------- | --------------------- | ------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P4  | LLM-Based Multi-Agent Systems for SE | RQ1 Context Definitions      | Respondida Plenamente | **T**         | Sec. 2.1–2.3 (p.3–4)               | Definição formal de autonomia (atributos §2.1; tupla ⟨L,O,M,P,A,R⟩ §2.2) (a); características núcleo — autonomia, percepção, goal-driven, social, aprendizado, memória, Rethink (b); modelo de decisão explícito (loop reflexivo + estilos CPDE/DPDE) (c).                                                                                                                                                                        |
| P4  | "                                    | RQ2 Engineering Architecture | Respondida Plenamente | **T**         | Sec. 2.3, Sec. 3 (p.4–8)           | Plataforma de orquestração (modelos de coordenação cooperativo/competitivo/hierárquico; comunicação centralizada/descentralizada; grafo G(V,E)) (a); vasto catálogo de frameworks — ChatDev, MetaGPT, AgileCoder, AutoGen, LangChain, DSPy, MapCoder, CodexGraph (b); capacidades avançadas — memória, RAG, retrieval agents, knowledge graphs, MCTS, blackboard, adaptação dinâmica (c). **Núcleo de arquitetura/orquestração.** |
| P4  | "                                    | RQ3 Evidence Benefits        | Respondida Plenamente | **T**         | Sec. 1, Sec. 3, Sec. 4 (p.2, 5–12) | Benefícios qualitativos (autonomia, robustez/tolerância a falhas, escalabilidade) (a); **métricas próprias** dos 2 estudos de caso — Snake 76s/$0,019 (2 tentativas), Tetris 70s/$0,020 (sucesso na 10ª, incompleto) (b); nível de evidência primário (execuções reais) + secundário (71 estudos) (c). **Ressalva: benefícios são de Engenharia de Software (tempo/custo de geração de código), não de IR.**                      |
| P4  | "                                    | RQ4 Challenges & Ethics      | Respondida Plenamente | **T**         | Sec. 5.2.6, Sec. 5.2 (p.19–22)     | Desafios técnicos — escalabilidade, gargalos de comunicação, limites de memória, alucinação, condições de término (a); ético-governança — privacidade, silos de dados, compliance GDPR/CCPA (b); mecanismos — RBAC/ABAC, differential privacy, SMPC, federated learning, homomorphic encryption, blockchain, privacy-by-design, HITL (c). Foco em privacidade/segurança; accountability/viés menos explorados.                    |
| P4  | "                                    | RQ5 Research Gaps            | Respondida Plenamente | **T**         | Sec. 5 (Fig. 4), Sec. 7 (p.12–22)  | Agenda de pesquisa estruturada em 2 fases + 8 research questions: role-playing, linguagem de prompting (AOP/MAOP), colaboração humano-agente, **benchmarking multiagente** (§5.2.2), escalabilidade, princípios industriais, adaptação dinâmica, privacidade/segurança.                                                                                                                                                           |
|     |                                      | **SCORE_RQ**                 |                       | **5.0 / 5.0** |                                    | T + T + T + T + T                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P4  | Revisão sistemática + estudos de caso | **Y** (1.0) | **Y** (1.0) | **P** (0.5) | **Y** (1.0) | **3.5 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (complexidade de SE; lacuna no mapeamento de LMA) e abordagem (revisão sistemática + case studies + agenda) explícitos (Sec. 1, contribuições).
- **QA2 = Y** — método altamente replicável: base DBLP, conjuntos exatos de keywords com truncagem, keywords por fase do SDLC, 8 critérios de exclusão, triagem em 3 fases + snowballing, data da busca (14/11/2024), parâmetros dos case studies (ChatDev, GPT-3.5-turbo, temperatura 0.2, prompts completos).
- **QA3 = P** — há validação empírica com métricas (2 estudos de caso: tempo, custo, taxa de sucesso), porém limitada a **2 jogos clássicos com 1 framework** (nível de _toy example_); o restante é síntese secundária de 71 estudos.
- **QA4 = Y** — conclusões coerentes com revisão + case studies; **threat to validity explícito** (§6.2) e limitações dos case studies reconhecidas (§4).

## Parecer final do revisor

**Síntese.** P4 é uma revisão sistemática rigorosa (estudos primários via DBLP + snowballing, 8 critérios de exclusão, threats to validity) acompanhada de dois estudos de caso empíricos com métricas próprias. Alcança **SCORE_RQ máximo (5.0/5)**, com força excepcional em **RQ1** (definição formal ⟨L,O,M,P,A,R⟩) e **RQ2** (plataforma de orquestração, modelos de coordenação/comunicação, vasto catálogo de frameworks) — sendo uma das melhores fontes do corpus para fundamentos de arquitetura/orquestração agêntica — e uma agenda de pesquisa detalhada (**RQ5**). **Ressalva central de escopo:** o domínio é Engenharia de Software (SDLC), não Resposta a Incidentes; a evidência de benefícios (RQ3) é sobre geração de código (tempo/custo), sem métricas de IR.

**Recomendação: INCLUIR.** Justificativa: qualidade metodológica alta (QA 3.5/4) e cobertura plena das RQs (5.0/5) tornam o estudo uma **referência arquitetural/taxonômica** de primeira linha para agentic AI/multiagente. Ressalvas: (i) usar como fundamento de definição/arquitetura/orquestração, **não** como evidência de benefício em IR (domínio SE); (ii) a validação empírica é de escala reduzida (2 jogos); (iii) confirmar o veículo final e o DOI (o PDF é preprint v4 com DOI placeholder).

**Pendências de verificação externa:**

- **Veículo final / DOI** → confirmar publicação (PDF traz placeholder `10.1145/nnnnnnn`; arXiv:2404.04834v4).
- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (veículo-alvo); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A2.
