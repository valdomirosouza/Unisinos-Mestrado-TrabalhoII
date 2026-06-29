# Avaliação RSL — Estudo P24

**Artigo:** _AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0_ — F. Piccialli, D. Chiaro, S. Sarwar, D. Cerciello, P. Qi, V. Mele (University of Naples Federico II)
**Arquivo:** P24-A1-1-s2.0-S0957417425020238-main.pdf (18 páginas)

> ⚠️ **Alerta de tipo de estudo:** trata-se de um **SURVEY / REVIEW** (estudo secundário), explicitamente rotulado "Review" no cabeçalho da Elsevier. Isso é determinante para a avaliação de QA (ver QA3) e para a recomendação.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                             | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                          | DOI                        |
| --- | ------------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------- | -------------------------- |
| P24 | Expert Systems With Applications (Vol. 291) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | **Survey / Revisão sistemática (PRISMA)** — estudo secundário | 10.1016/j.eswa.2025.128404 |

_Evidências: cabeçalho p.1 (rótulo "Review"; DOI; recebido 13/12/2024, aceito 29/05/2025, online 02/06/2025); "Expert Systems With Applications 291 (2025) 128404"; CC-BY. Metodologia PRISMA com repositório público no GitHub (p.3). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                        | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)          | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                             |
| --- | ----------------------------- | ---------------------------- | ----------------------- | ------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P24 | AgentAI Survey (Industry 4.0) | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §3, §3.1-3.2 (p.3-5), Figs. 2-3 | Cobertura definicional **mais completa até aqui**: espectro não-autônomo↔totalmente autônomo (a); módulos perception/cognition/action, memória, aprendizado (zero/few-shot, fine-tuning), uso de ferramentas/expansão dinâmica do espaço de ações (b); modelos de decisão RL/MARL/LLM e supervisão humana (c).                                                                 |
| P24 | "                             | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §3.1-3.2 (p.4-5), Fig.2         | Tipos de arquitetura e workflow conceitual (user→agent→DB/vectorDB→LLM→ação→data flywheel) e frameworks (RL/DRL/MARL, LLMs/VLMs, ferramentas modulares) cobertos, porém de forma **genérica/survey**; sem orquestração de produção, guardrails ou observabilidade concretos (núcleo da RQ2).                                                                                   |
| P24 | "                             | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | §5 (taxonomia), §6.1 (p.6-14)   | Benefícios qualitativos amplos (escalabilidade, robustez, flexibilidade, eficiência) sintetizados por domínio (a); **sem métricas quantitativas próprias** (estudo secundário) e **sem evidência específica de IR** (b/c ausentes).                                                                                                                                            |
| P24 | "                             | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §6.1-6.2 (p.13-15)              | Cobertura **mais forte até aqui**: desafios técnicos (adaptabilidade em tempo real, contexto, generalização, silos de dados) (a); ética/governança extensa — viés, justiça, accountability, transparência, oversight humano (b); mecanismos de governança — frameworks embarcados na arquitetura, explicabilidade, mitigação de viés, privacidade/"right to be forgotten" (c). |
| P24 | "                             | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §6.1-6.3 (p.13-15)              | Direções futuras abrangentes: evolução Industry 5.0/6.0, autonomia responsável, coordenação multiagente, inferência de intenção, autogestão descentralizada, alinhamento ético.                                                                                                                                                                                                |
|     |                               | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                 |                                                                                                                                                                                                                                                                                                                                                                                |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P24 | Survey / Revisão sistemática (PRISMA) | **Y** (1.0) | **Y** (1.0) | **N** (0.0) | **P** (0.5) | **2.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — objetivos claros: RQs explícitas (§1.1), lacuna identificada (ausência de análise cross-domain coesa) e contribuições listadas (§1.2).
- **QA2 = Y** — metodologia replicável **para um estudo secundário**: protocolo PRISMA, 4 bases, string de busca explícita, estágios de triagem (255→144→66) e **repositório público no GitHub** com todos os artigos.
- **QA3 = N** — **sem validação empírica primária**: é uma síntese da literatura, sem experimento/estudo de caso/simulação com métricas próprias. Pela rubrica ("teórico = N"), estudo secundário não fornece base de evidências empíricas próprias.
- **QA4 = P** — conclusões coerentes com a síntese e discussão extensa de desafios do AgentAI, **porém sem discussão das limitações do próprio survey** (busca restrita ao termo "AgentAI/AgenticAI" — que tende a perder estudos agênticos de IR que não usam esse rótulo; exclusão de reviews; N final = 66).

## Parecer final do revisor

**Síntese.** Survey amplo e bem conduzido (PRISMA, reprodutível) sobre **AgentAI em Industry 4.0** (e 5.0/6.0) através de nove setores. É a referência **mais forte até aqui para RQ1** (definições de autonomia/componentes) e **RQ4/RQ5** (desafios, ética/governança e direções futuras). Entretanto, é um **estudo secundário (survey)**, sem validação empírica própria (QA3 = N), e seu **domínio não é Resposta a Incidentes** — os nove setores cobertos não incluem IR/cibersegurança operacional (segurança aparece apenas tangencialmente em "Networking"/"Defence"). A relevância para a RSL é, portanto, **contextual/fundacional**, não de evidência primária.

**Recomendação: INCLUIR COM RESSALVAS — como referência fundacional.** SCORE_RQ 4,0/5,0, mas QA 2,5/4,0 (**Banda Média**) por ser estudo secundário. Útil para ancorar definições de Agentic AI, taxonomia de autonomia (RQ1) e o panorama de desafios/ética (RQ4) na fundamentação teórica da RSL.

> ⚠️ **Decisão de protocolo (cabe ao condutor da RSL):** se o protocolo restringir os estudos primários (P-IDs) a **estudos primários empíricos no domínio de Resposta a Incidentes**, este artigo deve ser **EXCLUÍDO da síntese primária** (e eventualmente citado apenas na fundamentação), por ser (i) survey/secundário, (ii) fora do escopo de IR, (iii) sem evidência empírica própria. Diferentemente de P20-P23, ele não descreve um sistema agêntico avaliado para IR.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _Expert Systems With Applications_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios verificáveis no PDF atendidos (Ano 2025 ✓; veículo Elsevier ESWA ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
