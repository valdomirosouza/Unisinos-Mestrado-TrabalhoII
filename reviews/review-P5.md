# Avaliação RSL — Estudo P5

**Artigo:** _A Survey of AIOps in the Era of Large Language Models_ — L. Zhang, T. Jia, M. Jia, Y. Wu, A. Liu, Y. Yang, Z. Wu, X. Hu, P. S. Yu, Y. Li (Peking University / Tsinghua / HKUST-Guangzhou / UIC)
**Arquivo:** P5-A1 - A Survey of AIOps in the Era of Large Language Models.pdf (35 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                                        | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                  | DOI                              |
| --- | ---------------------------------------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------- | -------------------------------- |
| P5  | _J. ACM_ (declarado; metadados de template acmart); arXiv:2507.12472v1 | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Revisão sistemática (SLR) — LLM4AIOps | [VERIFICAR] (placeholder no PDF) |

_Evidências: p.1–2 (rodapé "J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2025"; marca arXiv:2507.12472v1 [cs.SE], 23 Jun 2025; DOI placeholder `XXXXXXX`). **Atenção: "Vol. 37/No. 4/Article 111" são defaults do template acmart e o DOI é placeholder — veículo final a confirmar.** Protocolo de SLR documentado (Sec. 2): 5 bases (Scopus, WoS, IEEE, ACM, arXiv), string de busca (Fig. 3), IC1–IC4/EC1–EC5, workflow PRISMA 761→614→163 (Fig. 4). Abstract cita 183 papers analisados; §2.3 indica 163 selecionados. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                               | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                 | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --- | ------------------------------------ | ---------------------------- | ----------------------- | ------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P5  | A Survey of AIOps in the Era of LLMs | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §4.3 (Fig. 9), §5.5 (p.14–21)          | Autonomia tratada via **espectro de níveis de automação** da remediação (Assisted Questioning → … → Automatic Execution) com OCE no loop (a); uso de ferramentas via TAG (b, parcial); **não conceitua agentic AI, planejamento/memória como capacidades do agente nem um modelo de decisão** (c ausente). O foco é LLM4AIOps, não caracterização de agentic AI.                                                                      |
| P5  | "                                    | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §5 (Fig. 10), §5.5, §7.4 (p.15–21, 26) | Taxonomia de arquiteturas/métodos (foundation/fine-tuning/embedding/prompt/knowledge-based) (a); vasto catálogo de ferramentas/frameworks — RCAgent, RCACopilot, AIOpsLab (agent-cloud interface), LLexus, ChatOps4Msa, agente GPT-4 com 150 tools, integração Ansible/K8s (b); capacidades avançadas — RAG (memória/conhecimento), Tool-Augmented Generation, observabilidade (métricas/logs/traces) (c). Guardrails pouco tratados. |
| P5  | "                                    | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §1.1, §4, §6 (RQ4) (p.2–3, 11–23)      | **Máxima relevância a IR.** Benefícios qualitativos (menor carga do OCE, resolução mais rápida, maior automação, generalidade cross-platform) (a); taxonomia abrangente de métricas de avaliação — precision/recall/F1, BLEU/ROUGE/BERTScore, Functional Correctness, Execution Success Rate, Acc@N (b); nível de evidência secundário mas ancorado em **163 estudos empíricos primários** (EC5 exigia experimentos) (c).             |
| P5  | "                                    | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §7 (p.24–26)                           | Desafios técnicos amplamente cobertos — custo/tempo-real, uso de traces, generalização/adaptação, integração de toolchain, alucinação/inconsistência (a). **Dimensão ético-governança e mecanismos de governança/accountability essencialmente ausentes** (b/c) — questões gerais de LLM declaradas fora de escopo; HITL (OCE) presente como medida prática.                                                                          |
| P5  | "                                    | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §6.2, §7 (p.23–26)                     | Lacunas e direções futuras explícitas: eficiência/custo, incorporação de traces, generalização em evolução de software, integração com toolchains legadas; benchmarks/datasets (LogEval, OpsEval, KubePlaybook, AIOpsLab).                                                                                                                                                                                                            |
|     |                                      | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                        | P + T + T + P + T                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                          | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | --------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P5  | Revisão sistemática da literatura (SLR) | **Y** (1.0) | **Y** (1.0) | **N** (0.0) | **P** (0.5) | **2.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (falhas de runtime em sistemas distribuídos; lacuna: ausência de SLR de LLM4AIOps de processo completo) e contribuição (primeira SLR full-process, 4 RQs) explícitos (Sec. 1).
- **QA2 = Y** — protocolo altamente replicável (§2): 5 bases, string de busca completa (Fig. 3), IC1–4/EC1–5, workflow PRISMA com contagens por base e por critério (Fig. 4), revisor primário + secundário + validação por co-autores, entrevistas com OCEs.
- **QA3 = N** — SLR/estudo secundário **sem validação empírica própria** (não executa experimentos); sintetiza 163 estudos empíricos (forte embasamento indireto) + entrevistas metodológicas, mas per rubrica isso configura síntese secundária = N.
- **QA4 = P** — conclusões coerentes com as 4 RQs e Seção 7 substantiva de desafios/futuros; porém **sem seção explícita de limitações/threats to validity do próprio survey**.

## Parecer final do revisor

**Síntese.** P5 é a fonte **mais aderente ao domínio central da RSL** (AIOps = detecção de falhas, análise de causa-raiz e remediação = Resposta a Incidentes). É uma SLR rigorosa (protocolo PRISMA, 5 bases, 163 estudos) com força em **RQ2** (arquiteturas/ferramentas/RAG/TAG e integração de toolchain em produção), **RQ3** (benefícios e taxonomia de métricas de avaliação, com relevância máxima a IR) e **RQ5** (lacunas/benchmarks). É mais fraca em **RQ1** (não conceitua a autonomia/capacidades do _agente_ — trata níveis de automação da remediação) e **RQ4** (praticamente sem ética/governança/accountability, declaradas fora de escopo). **Ressalva de escopo:** o objeto é LLM4AIOps em geral; o conteúdo agêntico (Tool-Augmented Generation, execução automática, AIOpsLab "AI agents for autonomous clouds") é um subconjunto — valioso, porém não é um estudo exclusivamente de agentic AI.

**Recomendação: INCLUIR.** Justificativa: relevância direta e alta ao escopo de IR da RSL, metodologia sólida (QA2=Y) e cobertura forte de RQ2/RQ3/RQ5 tornam-no referência-chave para o pipeline de resposta a incidentes e remediação agêntica (níveis de automação, TAG, benchmarks como AIOpsLab). Ressalvas: (i) usar o material agêntico (TAG/auto-execução) como núcleo; (ii) complementar RQ1 (definições de agentic AI) e RQ4 (ética/governança) com outros estudos; (iii) confirmar veículo final/DOI (metadados de template acmart + placeholder).

**Pendências de verificação externa:**

- **Veículo final / DOI** → confirmar periódico e DOI (PDF traz defaults acmart e placeholder; arXiv:2507.12472v1).
- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (veículo confirmado); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
