# Avaliação RSL — Estudo P1

**Artigo:** _Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment_ — I. Adabara, B. O. Sadiq, A. N. Shuaibu, Y. I. Danjuma, V. Maninti (Kampala International University)
**Arquivo:** P1-A2 - Trustworthy agentic AI systems...pdf (54 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.       | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                         | DOI                             |
| --- | --------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ---------------------------- | ------------------------------- |
| P1  | F1000Research, 14:905 | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Revisão narrativa (_survey_) | 10.12688/f1000research.169927.1 |

_Evidências: cabeçalho p.1-2 (DOI, "First published: 11 Sep 2025, 14:905", licença CC-BY). **Status editorial: "version 1; peer review: awaiting peer review" (p.1) — ainda não revisado por pares.** Tipo autodeclarado como revisão narrativa, não SLR (Sec. 1, p.3; Sec. 2, p.4). Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                         | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                   | Parecer do revisor                                                                                                                                                                                                                                                              |
| --- | ------------------------------ | ---------------------------- | ----------------------- | ------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | Trustworthy agentic AI systems | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | Sec. 3.1–3.4 (p.7–10)                    | Define autonomia e distingue agentic AI de LLMs/agentes tradicionais (a); capacidades núcleo memória/raciocínio/planejamento/uso de ferramentas (b, §3.2); modelos de decisão via RL, teoria dos jogos, ToM, ACT-R/Soar (c, §3.4).                                              |
| P1  | "                              | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | Sec. 4 (Tab. 1), Sec. 8 (p.10–13, 31–37) | Tipologia arquitetural mono/multi-agente, federada, híbrida/blockchain com quadro comparativo (a); frameworks/ferramentas — UserCentrix, Magentic-One, S-AI, SHIELD, SAGA, ZTA (b); memória, guardrails, observabilidade/runtime monitoring (c).                                |
| P1  | "                              | RQ3 Evidence Benefits        | Parcialmente Respondida | **P**         | Sec. 7.1 (p.27–28)                       | Benefícios qualitativos em IR (ReliaQuest: maior velocidade de detecção, menor carga humana; Twine's Alex) (a). **Sem métricas quantitativas de benefício** — os números citados (24%, 99%) são taxas de ataque, não benefícios (b); evidência apenas secundária/narrativa (c). |
| P1  | "                              | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | Sec. 5, 6, 8, 9 (p.13–45)                | Taxonomia de ameaças em camadas (a, §5); frameworks de governança EU AI Act/NIST/OECD e lacunas de accountability/ética (b, §6); mecanismos de defesa SHIELD/ZTA/SAGA e desafios abertos (c, §8–9).                                                                             |
| P1  | "                              | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | Sec. 9.1–9.9 + Tab. 5 (p.38–45)          | Lacunas explícitas: alinhamento (§9.1), integridade de memória (§9.2), auditabilidade/observabilidade (§9.3), prontidão institucional (§9.7), benchmarking/validação (§9.8), síntese cross-domínio (§9.9/Tab.5).                                                                |
|     |                                | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                                          | T + T + P + T + T                                                                                                                                                                                                                                                               |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo               | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ---------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P1  | Revisão narrativa (_survey_) | **Y** (1.0) | **P** (0.5) | **N** (0.0) | **P** (0.5) | **2.0 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (lacunas de segurança/governança/confiabilidade em agentic AI) e proposta (revisão cross-layer + 4 contribuições) explícitos (Abstract; Sec. 1, p.3–4).
- **QA2 = P** — Sec. 2 descreve fontes (IEEE, ACM, Springer, ScienceDirect, arXiv + relatórios de política) e clusters de palavras-chave, mas **assumidamente não-sistemática**: sem protocolo PRISMA, sem strings/contagens reprodutíveis. Compreensível, não replicável.
- **QA3 = N** — **sem validação empírica própria** (nenhum experimento, estudo de caso industrial autoral ou simulação com métricas). Casos "reais" (Sec. 7) são anedotas secundárias. Rubrica: síntese teórica/secundária = N.
- **QA4 = P** — conclusões (Sec. 10) coerentes com o corpo, mas limitações do próprio estudo apenas implícitas (trade-off narrativa vs. SLR na Sec. 2); sem discussão crítica dedicada (viés de seleção, não reprodutibilidade, status _awaiting peer review_).

## Parecer final do revisor

**Síntese.** P1 é uma revisão narrativa ampla e bem estruturada que cobre com profundidade definições/autonomia (**RQ1**), arquiteturas e mecanismos de engenharia (**RQ2**), desafios e ética/governança (**RQ4**) e lacunas de pesquisa (**RQ5**), com forte aderência ao escopo _cross-layer_ da RSL (arquiteturas, ameaças, governança). A aderência é apenas parcial em **RQ3**: há benefícios qualitativos relevantes a Resposta a Incidentes (caso ReliaQuest: detecção autônoma, resposta a incidentes, priorização de risco), mas sem métricas quantitativas de benefício e apoiada só em evidência secundária. Qualidade metodológica média (QA=2.0): objetivos claros, porém método não replicável e sem validação empírica própria.

**Recomendação: INCLUIR COM RESSALVAS.** Justificativa: SCORE_RQ alto (4.5/5) e cobertura conceitual excelente para RQ1/RQ2/RQ4/RQ5 justificam a inclusão; as ressalvas decorrem de (i) status editorial _awaiting peer review_ — ainda não revisado por pares; (ii) ausência de evidência empírica primária (QA3=N), o que limita seu peso na RQ3 sobre benefícios/métricas em IR; (iii) natureza narrativa não-reprodutível. Recomenda-se usá-lo como fonte **conceitual/definicional e de taxonomia de ameaças**, não como evidência de benefício quantitativo.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (periódico _F1000Research_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A2.
- **Status de revisão por pares** → confirmar se saiu de _"awaiting peer review"_ (impacta rigor/veículo).
