# Avaliação RSL — Estudo P16

**Artigo:** _A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey_ — J. Diaz-de-Arcaya, A. I. Torre-Bastida, G. Zárate, R. Miñón (Tecnalia, BRTA), A. Almeida (Universidade de Deusto), Espanha
**Arquivo:** P16-A1 - A Joint Study of the Challenges Opportunities and Roadmap of MLOps and AIOps - A Systematic Survey.pdf (30 páginas)

> ⚖️ **Recomendação: INCLUIR COM RESSALVAS (referência de contexto, não estudo agêntico).** SLR exemplar (ACM Computing Surveys, QA 3.5/4 Alta), mas objeto é **MLOps/AIOps (2023, pré-agêntica)**, não Agentic AI. Domínio adjacente (AIOps = detecção/RCA/remediação de incidentes). SCORE_RQ 1.0/5.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                   | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                  | DOI             |
| --- | --------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------- | --------------- |
| P16 | _ACM Computing Surveys_, 56(4):84 | 2023 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Revisão sistemática (SLR, 93 estudos) | 10.1145/3625289 |

_Evidências: cabeçalho p.1 (DOI 10.1145/3625289; "ACM Comput. Surv. 56, 4, Article 84 (October 2023), 30 pages"). SLR PRISMA-style: 44.903 registros → 93 estudos (§2–3). Termo "agentic" ausente; LLMs citados apenas como oportunidade emergente. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo              | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)        | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                               |
| --- | ------------------- | ---------------------------- | --------------------------- | ------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P16 | MLOps & AIOps (SLR) | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §1.1, Tab. 1 (p.2–3)          | Define **MLOps** (ML Operations) e **AIOps** (AI for IT Operations) — metodologias derivadas de DevOps. **Não** define Agentic AI (agentes autônomos baseados em LLM); autonomia tratada é de pipelines de ops/self-healing, não agêntica.                                                                                                                                       |
| P16 | "                   | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §4.4 (p.15–21)                | Frameworks/arquiteturas são **plataformas de MLOps/AIOps** (CI/CD, orquestração de pipelines, observabilidade, monitoramento), **não** arquitetura de agentic AI. Há adjacência conceitual (observabilidade/orquestração de IA em produção), mas o objeto não é agêntico.                                                                                                        |
| P16 | "                   | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §4.3, §4.5 (p.14–15, 21–23)   | **Conteúdo forte do domínio de IR**: AIOps para **detecção/predição de incidentes, root cause analysis, remediation**, análise de logs para resolução de incidentes no menor tempo, self-healing (a). Porém são benefícios de **AIOps/IA clássica, não de Agentic AI**, majoritariamente **sem LLMs** — servem como **baseline operacional** de IR, não como evidência agêntica. |
| P16 | "                   | RQ4 Challenges & Ethics      | Não tem conteúdo suficiente | **N**         | §4.1 (p.11–14)                | Desafios são de **operacionalização de MLOps/AIOps** (dados, colaboração, deployment, monitoramento), não desafios/ética/governança de **Agentic AI**. Menção pontual à ética de LLMs (Harrer, 2023) é tangencial.                                                                                                                                                               |
| P16 | "                   | RQ5 Research Gaps            | Parcialmente Respondida     | **P**         | §4.2–4.3, §6 (p.13–15, 23–24) | **Lacuna motivadora relevante**: "automação ainda é deficiente" em AIOps (foco em detecção/RCA, pouca remediação automatizada); e "o recente avanço dos LLMs se espalhará para AIOps" — **ponte direta** para a motivação da RSL (copiloto agêntico preenchendo a lacuna de automação de IR). Mas são gaps de MLOps/AIOps, não de agentic AI.                                    |
|     |                     | **SCORE_RQ**                 |                             | **1.0 / 5.0** |                               | N + N + P + N + P                                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo            | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P16 | Revisão sistemática (SLR) | **Y** (1.0) | **Y** (1.0) | **P** (0.5) | **Y** (1.0) | **3.5 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — objetivos claros (§1.2) e **5 RQs explícitas**.
- **QA2 = Y** — **protocolo sistemático exemplar**: recuperação de artigos (§2.1), termos de busca (§2.2), critérios de seleção (§2.3), métricas de qualidade (§2.4), funil PRISMA (44.903→93, tabela por estágio identificação/triagem). Totalmente replicável.
- **QA3 = P** — base de evidências sistemática (93 estudos com extração rigorosa); **sem validação empírica própria** (é revisão). Consistente com SLRs rigorosas (cf. P15).
- **QA4 = Y** — conclusões coerentes **e com seção explícita de "Risk of Bias" (§3.2)** — tratamento formal de ameaças à validade, acima da maioria dos reviews do corpus.

## Parecer final do revisor

**Síntese.** P16 é uma **SLR exemplar** (ACM Computing Surveys, protocolo PRISMA, 93 estudos, avaliação de risco de viés) — **QA 3,5/4 (Alta)**, uma das mais altas do corpus em qualidade metodológica. **Contudo, seu objeto é MLOps/AIOps**, não Agentic AI: publicada em **2023 (pré-onda agêntica)**, trata metodologias operacionais derivadas de DevOps e IA/ML clássica para operações de TI; LLMs aparecem apenas como **oportunidade emergente**, e o termo "agentic" está ausente. Daí SCORE_RQ 1,0/5 — RQ1/RQ2/RQ4 = N (não é agentic AI). **Onde P16 é valiosa é no domínio operacional da RSL:** AIOps cobre **detecção/predição de incidentes, root cause analysis e remediação** (RQ3=P) e articula a **lacuna motivadora** — "automação de AIOps ainda deficiente" + "LLMs se espalharão para AIOps" (RQ5=P) — que é exatamente o problema que um copiloto agêntico de IR endereça.

**Recomendação: INCLUIR COM RESSALVAS — como referência de fundamentação/contexto (não como estudo agêntico).** Justificativa: é um **âncora de background e de trabalhos relacionados de altíssima qualidade** para caracterizar o **cenário operacional de AIOps/IR** e a **lacuna de automação** que a RSL busca preencher, além de ser ponte histórica para LLM4AIOps. **Ressalvas:** (i) **NÃO é Agentic AI** — usar apenas para RQ3/RQ5 (domínio de IR/AIOps e motivação), **não** para RQ1/RQ2/RQ4 (que ficam N); (ii) **2023, pré-agêntica** — LLMs só como tendência; (iii) **complementar com P5 (LLM4AIOps) e estudos agênticos** para o paradigma. **Complementaridade no corpus:** P16 (AIOps clássico, baseline) → P5 (LLM4AIOps, ponte) → P14/P15 (agentic AI em IR/SOC).

**Nota de decisão (para o orientando).** Sob critério **estrito "somente Agentic AI"**, P16 seria **EXCLUÍDA por escopo** (não é agêntica). Recomendo **incluí-la como referência de contexto/fundamentação de AIOps** (não como fonte de evidência agêntica), dada a qualidade (CSUR/A1) e a aderência direta ao **domínio de IR** — decisão a fixar no protocolo, coerente com o tratamento dado a P12.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (provável alta contagem — CSUR).
- **SJR (quartil)** → Scimago Journal Rank (_ACM Computing Surveys_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
