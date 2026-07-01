# Avaliação RSL — Estudo P3

**Artigo:** _A Research Landscape of Agentic AI and Large Language Models: Applications, Challenges and Future Directions_ — S. Brohi, Q.-u.-a. Mastoi, N. Z. Jhanjhi, T. R. Pillai (University of the West of England / Taylor's University / INTI International University)
**Arquivo:** P3-A2 - A Research Landscape of Agentic AI and Large Language Models Applications, Challenges and Future Directions.pdf (29 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.             | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                          | DOI               |
| --- | --------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------- | ----------------- |
| P3  | _Algorithms_ (MDPI), 18:499 | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Scoping review estruturado + análise temática (c/ demonstrações ilustrativas) | 10.3390/a18080499 |

_Evidências: cabeçalho p.1 (DOI; recebido 01/07/2025, aceito 06/08/2025, publicado 11/08/2025; "Algorithms 2025, 18, 499"; licença CC-BY). Tipo: scoping review de 4 fases documentadas (Sec. 2, Fig. 5), com contagens 327→71→84 fontes, dedup Zotero e análise VOSviewer; autodeclarado "not formally a systematic review" (p.5). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                  | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                        | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | --------------------------------------- | ---------------------------- | ----------------------- | ------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P3  | Research Landscape of Agentic AI & LLMs | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | Sec. 1 (Fig. 3), Sec. 3 (p.3–4, 9)            | Define autonomia (LLM como núcleo de raciocínio, agentes agem) (a); características núcleo — percepção, raciocínio, ação, aprendizado, colaboração em ciclo fechado (b); modelo de decisão via orchestrator + external services layer, exemplo de workflow (voo) (c).                                                                                                                                                             |
| P3  | "                                       | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | Sec. 1 (Fig. 3), Sec. 5 (Tab. 2) (p.3, 21–24) | Arquitetura apresentada só via **um workflow ilustrativo** (orchestrator/external services); ferramentas incidentais (AutoGPT, APIs, Pinecone/Elasticsearch, Salesforce); capacidades avançadas (memory-aware, cooperative, safe agents) tratadas como **desafios em aberto**, não mecanismos realizados → cobertura conceitual/superficial.                                                                                      |
| P3  | "                                       | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | Sec. 3.1–3.6 (p.9–12)                         | Benefícios qualitativos por domínio (educação, saúde, **cibersegurança/IR**, AV, e-commerce, atendimento) (a); métrica quantitativa escassa e secundária (Med-Flamingo "+20% acurácia") (b); evidência ilustrativa/secundária (c). **Forte relevância a IR** (§3.3: durante incidente, avaliar, priorizar riscos, conter/remediar — revogar credenciais, aplicar patches; SOC ReliaQuest/CrowdStrike), mas sem métricas próprias. |
| P3  | "                                       | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | Sec. 4–5, Tab. 1 e 2 (p.12–25)                | Desafios técnicos — segurança/privacidade, gestão de contexto, decisão opaca, coordenação multiagente, safety de longo prazo (a); ético-governança — viés, misinformation, alinhamento de valor, inclusividade, accountability (b); mecanismos — audit trails, decision logging, modelos de responsabilidade, sandboxing, HITL, EU AI Act/NIST (c). Núcleo do artigo.                                                             |
| P3  | "                                       | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | Sec. 4–5 (Tab. 1 e 2), Sec. 6 (p.12–25)       | Cada desafio mapeado a uma "Open Research Opportunity": trustworthy/aligned/explainable/collaborative/memory-aware/cooperative/safe/accountable agents — cobre alinhamento, benchmarking de safety, governança, observabilidade/auditoria, threat models. Roadmap explícito.                                                                                                                                                      |
|     |                                         | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                               | T + P + P + T + T                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                          | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P3  | Scoping review estruturado + demonstrações ilustrativas | **Y** (1.0) | **Y** (1.0) | **P** (0.5) | **Y** (1.0) | **3.5 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — lacuna explícita (ausência de análise integrada peer-reviewed de LLM+Agentic AI) e 4 contribuições declaradas (Sec. 1).
- **QA2 = Y** — método de scoping documentado e rastreável: bases, palavras-chave, recorte 2020–2025, contagens por fonte (327→71→84), dedup Zotero, VOSviewer, Fig. 5. Reprodutível em bom grau (ressalva: critérios de qualidade descritos qualitativamente).
- **QA3 = P** — inclui demonstrações empíricas próprias (GPT-4o/DeepSeek-R1, 3 prompts × 3 dias), mas os autores as declaram "not formal experiments / not rigorous or fully reproducible" → nível de _toy example_; benefícios apoiados em literatura secundária.
- **QA4 = Y** — conclusões coerentes com o corpo e **limitações explícitas** (§6: scoping, não systematic; sugere revisões formais futuras).

## Parecer final do revisor

**Síntese.** P3 é um _scoping review_ metodologicamente sólido (protocolo documentado, banda de qualidade Alta) que integra LLMs e Agentic AI num "research landscape" único. Cobre plenamente definições (**RQ1**), desafios técnicos/éticos e mecanismos de governança (**RQ4**) e lacunas/roadmap (**RQ5**), com mapeamento explícito desafio→oportunidade de pesquisa (Tabelas 1 e 2). É parcial em **RQ2** (arquitetura apenas ilustrada por um workflow, capacidades tratadas como desafios) e **RQ3** (benefícios qualitativos/secundários, sem métricas próprias). Destaque: **forte aderência a Resposta a Incidentes** — a seção de cibersegurança descreve explicitamente avaliação de situação, priorização de riscos e ações de contenção/remediação por agentes em SOC (ReliaQuest, CrowdStrike).

**Recomendação: INCLUIR.** Justificativa: alta qualidade metodológica (QA 3.5/4, banda Alta), SCORE_RQ 4.0/5 e relevância direta ao escopo de IR da RSL justificam inclusão plena. Ressalvas menores: a evidência de benefícios é qualitativa/secundária (não citar como métrica); as demonstrações com GPT-4o/DeepSeek são ilustrativas, não validação robusta. Excelente fonte para taxonomia de desafios/governança e roadmap de pesquisa.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_Algorithms_, MDPI); insumo informa Q2.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A2.
