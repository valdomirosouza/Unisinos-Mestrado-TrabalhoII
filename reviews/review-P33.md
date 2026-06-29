# Avaliação RSL — Estudo P33

**Artigo:** _A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense_ — I. Adabara, B. Olaniyi Sadiq, A. Nuhu Shuaibu, Y. Ibarahim Danjuma, V. Maninti (Kampala International University, Uganda)
**Arquivo:** P33-A2-...f1000res169337.pdf (30 páginas)

> ⚠️ **Alerta de tipo de estudo:** **Revisão narrativa (narrative review)** — estudo **secundário** (F1000Research; "peer review: 2 approved"). Determinante para QA3 e recomendação. **Porém é o estudo secundário de melhor ajuste temático**: revisão **de** Agentic AI **em cibersegurança**, com Resposta a Incidentes explicitamente no escopo.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.             | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                         | DOI                             |
| --- | --------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------- |
| P33 | F1000Research (Vol. 14:843) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | **Revisão narrativa** — estudo secundário (peer review aberto: 2 aprovações) | 10.12688/f1000research.169337.1 |

_Evidências: cabeçalho p.1 (rótulo "REVIEW"; DOI; primeira publicação 01/09/2025; "F1000Research 2025, 14:843"; CC-BY). Strings Booleanas em material suplementar. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                             | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                    | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --- | ---------------------------------- | ---------------------------- | ----------------------- | ------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P33 | Review Agentic AI in Cybersecurity | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §1.1, §4 RQ1, Tab. 2 (p.3, 13-14)         | **Cobertura mais forte de RQ1 entre os secundários**: definição explícita de Agentic AI (autônomo, adaptável, goal-directed) e **taxonomia de níveis de autonomia** (Tab. 2: Reactive/Low, Proactive Goal-Seeking/Medium, Learning-Based/High, Human-in-the-Loop/Medium, Federated/Medium), incluindo "Threat triage assistants in SOCs" (a); arquiteturas cognitivas perception/reasoning/action, RL, híbrido humano-agente (b); decisão proativa/goal-directed (c). |
| P33 | "                                  | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §4 RQ1, §5.10 (p.13, 21)                  | Padrões de design (camadas modulares), arquiteturas híbridas (DRL+LLM+regras), estruturas de governança (centralizada/descentralizada/DAGN) e framework integrado Design-Governance-Resilience cobertos, porém de forma **conceitual/survey**; sem arquitetura de produção concreta com orquestração/guardrails/observabilidade específicos.                                                                                                                          |
| P33 | "                                  | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §3-§4 (p.10-15)                           | Benefícios qualitativos (melhora em detecção de anomalias e eficiência de IR) e tendências bibliométricas/exemplos de indústria (Mastercard, Airbus) (a); **sem síntese quantitativa própria de métricas** e sem evidência primária (b/c ausentes — estudo secundário).                                                                                                                                                                                               |
| P33 | "                                  | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §4 RQ2/RQ4, §5 (p.14-20), Tab. 3          | **Cobertura mais forte de RQ4 entre todos os estudos**: governança ética é pilar central — NIST AI RMF, ISO/IEC, **dual-use**, interoperabilidade de governança, accountability, transparência, mitigação de viés, DAGN, zero-trust (a/b/c todos explícitos); + desafios técnicos (ataques adversariais, model poisoning, pós-quântico).                                                                                                                              |
| P33 | "                                  | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §5.7-5.8 (p.20), tabela de lacunas (p.19) | Roadmap em horizontes curto/médio/longo prazo (XAI+defesa adversarial; federated+quantum-safe; neurosymbolic+quantum MARL), technology watchlist e tabela "lacuna/pergunta futura"; + duas seções de limitações (§2.7, §5.8).                                                                                                                                                                                                                                         |
|     |                                    | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P33 | Revisão narrativa (estudo secundário) | **Y** (1.0) | **P** (0.5) | **N** (0.0) | **Y** (1.0) | **2.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — objetivos claros: 4 RQs explícitas, 3 pilares temáticos (cognitive autonomy, ethical governance, quantum-resilient defense), problem context bem delimitado (§1-§2).
- **QA2 = P** — protocolo documentado e transparente (4 bases: IEEE/Scopus/WoS/ACM; strings Booleanas no suplemento; processo de 5 estágios; critérios de inclusão/exclusão; §2.7 limitações metodológicas), **porém é narrativa** (não sistemática): **sem contagens de estudos incluídos (sem fluxo PRISMA)**, síntese por interpretação humana + mapeamento assistido por IA (subjetividade reconhecida) → reprodutibilidade parcial.
- **QA3 = N** — **sem validação empírica primária** (revisão narrativa). Pela rubrica ("teórico = N").
- **QA4 = Y** — conclusões coerentes com a síntese e **duas seções explícitas de limitações** (metodológicas e da revisão) — reporte exemplarmente honesto.

## Parecer final do revisor

**Síntese.** Revisão narrativa abrangente e **diretamente no escopo da RSL**: Agentic AI **em cibersegurança**, cobrindo cognição/autonomia, governança ética e defesa quântica-resiliente, com IR explicitamente no escopo. É a **melhor referência secundária** do lote para fundamentar **RQ1** (traz uma **taxonomia de níveis de autonomia** — Tab. 2 — incluindo "copilot/human-in-the-loop em SOC", alinhada ao título da RSL) e **RQ4** (governança/ética é seu pilar central — a cobertura mais forte de todos os estudos), além de um **roadmap** de pesquisa (RQ5). Entretanto, é **estudo secundário (narrativa)**, sem evidência empírica própria (QA3 = N) → Banda Média.

**Recomendação: INCLUIR COM RESSALVAS — como referência fundacional/conceitual.** SCORE_RQ 4,0/5,0, QA 2,5/4,0 (**Banda Média**). Diferentemente de P26/P29 (secundários **não-agênticos** → excluir), P33 é um secundário **agêntico E de cibersegurança** — fit superior até a P24 (que era survey de Agentic AI, porém em Industry 4.0). Excelente para ancorar definições de autonomia (RQ1), o arcabouço de governança/ética (RQ4) e direções futuras (RQ5) na fundamentação da RSL.

> ⚠️ **Decisão de protocolo:** se o protocolo restringir a síntese primária a **estudos primários empíricos**, P33 deve entrar como **referência de fundamentação/related-review** (não no corpus primário) — mas é a **referência secundária prioritária** para o enquadramento conceitual da RSL. Nota: F1000Research usa peer review aberto pós-publicação (2 aprovações) — registrar para a avaliação de qualidade do veículo.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _F1000Research_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2025 ✓; veículo F1000Research ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**. _Observação:_ eventual EXCLUSÃO do corpus primário seria por **tipo de estudo (secundário)**, não por relevância — que aqui é alta.
