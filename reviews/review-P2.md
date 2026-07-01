# Avaliação RSL — Estudo P2

**Artigo:** _The role of agentic AI in shaping a smart future: A systematic review_ — S. Hosseini & H. Seilani (Shahid Bahonar University of Kerman / Bahmanyar University of Kerman, Irã)
**Arquivo:** P2-A1 - The role of agentic AI in shaping a smart future A systematic review.pdf (15 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.               | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                          | DOI                         |
| --- | ----------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------- | --------------------------- |
| P2  | _Array_ (Elsevier), 26:100399 | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Revisão (rotulada "systematic"; de fato narrativa/conceitual) | 10.1016/j.array.2025.100399 |

_Evidências: rodapé p.1 (DOI; recebido 29/12/2024, revisado 04/04/2025, aceito 15/04/2025, online 08/05/2025; "Array 26 (2025) 100399"; licença CC-BY). **Inconsistência de tipo: título diz "systematic review", mas o Abstract declara "This narrative review" (p.1) — sem seção de metodologia, protocolo PRISMA ou critérios de seleção; "No data was used" (p.14).** Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                            | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                  | Parecer do revisor                                                                                                                                                                                                                                                                                                                                              |
| --- | --------------------------------- | ---------------------------- | ----------------------- | ------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P2  | Role of Agentic AI (Smart Future) | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | Sec. 1.1, Fig. 1, Tab. 1 e 3 (p.2–6)    | Define autonomia e distingue de IA tradicional (a); características núcleo — autonomia, comportamento orientado a metas, interação, aprendizado, otimização de workflow, multiagente (b, Fig.1/Tab.1); modelo de decisão via RL/feedback e "fast/slow thinking", com comparação Agentic×Generative×Autonomous (c, Tab.3).                                       |
| P2  | "                                 | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | Sec. 4 (Tab. 4), Sec. 7 (p.7, 10–12)    | Arquitetura hierárquica master/orchestrator/micro-agentes (a); ampla cobertura de ferramentas — LangChain, CrewAI, AutoGen, AutoGPT, LangGraph, IBM Watson, SageMaker, TensorFlow, Llama (b); capacidades avançadas — statefulness/memória, streaming, monitoring loops do LangGraph (c).                                                                       |
| P2  | "                                 | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | Sec. 3–4, 6 (p.4–9)                     | Benefícios qualitativos (produtividade, custo, inovação) (a) e muitas métricas quantitativas (+40% produtividade, −60% tempo de resposta, +85% previsão, ROI 3–5x) (b), porém **todos os números são secundários** (McKinsey/relatórios de mercado), sem estudo empírico próprio ("No data was used"); evidência fraca (c) e sem foco em Resposta a Incidentes. |
| P2  | "                                 | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | Sec. 1.2, 3.1, 6.3, 8.5 (p.2, 5, 9, 12) | Desafios técnicos (custo computacional, caixa-preta, viés) (a) e éticos (privacidade, segurança, deslocamento de mão de obra) (b) explícitos, mas **mecanismos de governança genéricos** — "governança robusta", compliance GDPR/HIPAA/EU AI Act em nível de recomendação (c), sem accountability/threat models. Cobertura superficial → P.                     |
| P2  | "                                 | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | Sec. 5.4, 9.1–9.2 (p.8, 13–14)          | Direções futuras explícitas: Explainable Agentic AI, People-to-AI collaboration, Federated Agentic AI, integração com quantum/edge; limitações declaradas (§9.2: falta de estudos de caso setoriais, aspectos ético-sociais).                                                                                                                                   |
|     |                                   | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                         | T + T + P + P + T                                                                                                                                                                                                                                                                                                                                               |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                       | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ---------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P2  | Revisão narrativa/conceitual (rotulada "systematic") | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **Y** (1.0) | **2.0 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (compreensão fragmentada de aplicações/desafios do Agentic AI; lacuna de síntese) e contribuição (framework de estratégia GenAI) explícitos (Abstract; Sec. 1).
- **QA2 = N** — **rotulado "systematic review" mas sem qualquer protocolo**: ausência de PRISMA, strings de busca, bases, critérios de inclusão/exclusão ou contagens; o Abstract admite "narrative review". Não replicável.
- **QA3 = N** — **sem validação empírica própria** (experimento, estudo de caso autoral ou simulação); apenas estatísticas secundárias de relatórios de consultoria/mercado; "No data was used" (p.14). Síntese secundária = N.
- **QA4 = Y** — conclusões coerentes com o corpo e **limitações explicitamente discutidas** (§9.2). Ressalva: as afirmações de benefício repousam sobre dados secundários não verificados.

## Parecer final do revisor

**Síntese.** P2 é uma revisão de orientação organizacional/negócios que cobre bem **RQ1** (definições, atributos-núcleo de agentic AI) e **RQ2** (arquitetura hierárquica e um amplo panorama de ferramentas: LangChain, CrewAI, AutoGen, AutoGPT, LangGraph), além de direções futuras claras (**RQ5**). É mais fraca em **RQ3** — apresenta muitas métricas, porém todas secundárias (relatórios de mercado/McKinsey) e sem estudo próprio — e em **RQ4**, cuja governança é tratada em nível genérico de recomendação. O foco é adoção corporativa de GenAI, **não Resposta a Incidentes**, e não há qualquer metodologia de revisão sistemática apesar do título.

**Recomendação: INCLUIR COM RESSALVAS.** Justificativa: SCORE_RQ 4.0/5 e forte cobertura conceitual/de ferramentas (RQ1/RQ2) sustentam a inclusão como referência **definicional e de tooling**; contudo, as ressalvas são relevantes — (i) rótulo "systematic review" sem metodologia sistemática (QA2=N); (ii) ausência de evidência empírica primária (QA3=N); (iii) números de benefício são secundários e não devem ser citados como evidência; (iv) foco em negócios/GenAI, com aderência apenas indireta ao escopo de IR da RSL. Usar para embasar taxonomia de atributos e mapa de ferramentas, não para evidência quantitativa de benefícios.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_Array_, Elsevier); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
