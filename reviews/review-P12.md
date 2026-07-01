# Avaliação RSL — Estudo P12

**Artigo:** _Enhancing Autonomous System Security and Resilience with Generative AI: A Comprehensive Survey_ — M. Andreoni, W. T. Lunardi, G. Lawton, S. Thakkar (Technology Innovation Institute, Abu Dhabi, UAE)
**Arquivo:** P12-A1 - Enhancing autonomous system security and resilience with generative AI A comprehensive survey.pdf (27 páginas)

> ⚖️ **Recomendação: INCLUIR COM RESSALVAS (decisão de fronteira).** Domínio certo (cibersegurança/resposta a ameaças, LLMs, riscos adversariais), mas paradigma **Generative AI**, não **Agentic AI**; alvo são sistemas ciber-físicos. SCORE_RQ 1.5/5 (N+N+P+P+P); QA 1.5/4 (Média). Ver "Nota de decisão".

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                 | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                 | DOI                         |
| --- | ------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------- | --------------------------- |
| P12 | _IEEE Access_ (versão de autor) | 2024 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Survey / revisão narrativa (GenAI × segurança de sistemas autônomos) | 10.1109/ACCESS.2024.3439363 |

_Evidências: rodapé p.1 (DOI 10.1109/ACCESS.2024.3439363; "accepted for publication in IEEE Access... author's version which has not been fully edited"; licença CC-BY-NC-ND). O cabeçalho traz artefatos de template ("ACCESS.2017.DOI", "VOLUME 4, 2016") por ser versão de autor. Survey sobre GANs/VAEs/Transformers/LLMs para segurança/resiliência de UxV/AVs/robôs. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                        | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)  | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --- | --------------------------------------------- | ---------------------------- | --------------------------- | ------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P12 | Enhancing Autonomous System Security w/ GenAI | RQ1 Context Definitions      | Não tem conteúdo suficiente | **N**         | §III (p.4–7)            | Caracteriza **Generative AI** (GANs, VAEs, Transformers, LLMs) — **não Agentic AI**. Autonomia discutida é de sistemas ciber-físicos (UxV/robôs/AVs), não autonomia agêntica (planejamento/memória/uso de ferramentas/supervisão). Sem framework de capacidades agênticas.                                                                                                                                                                               |
| P12 | "                                             | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | §III–IV (p.4–12)        | Apresenta arquiteturas de **modelos generativos**, não arquitetura de engenharia de agentic AI (orquestração/memória/ferramentas/guardrails/observabilidade como componentes agênticos). Menções a SOAR/SOC e SECGPT são citações de terceiros, não contribuição arquitetural agêntica própria.                                                                                                                                                          |
| P12 | "                                             | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §IV.D, Tab. 5 (p.13–17) | **Domínio de cibersegurança/resposta a ameaças** com benefícios de LLMs/GenAI: intrusion detection (SecurityBERT 98,2% em IoT), malware detection, **threat intelligence a partir de relatórios de incidentes (CTI)**, pentesting (GPT-4 explorando CVEs autonomamente), threat simulation/honeypots, SOAR/SOC. Métricas pontuais. Porém **GenAI (não agentic)** e evidência secundária; alvo primário é sistema ciber-físico, não copiloto de IR de TI. |
| P12 | "                                             | RQ4 Challenges & Ethics      | Parcialmente Respondida     | **P**         | §V (p.15–19)            | Desafios técnicos (custo/compute, adaptação/acurácia, hallucination) e **segurança/adversarial de LLMs** — jailbreak, prompt injection, data extraction, dual-use (Net-GPT, BadGPT), sociotechnical safety, privacidade. Relevante a riscos/guardrails de IR, mas em enquadramento **GenAI/ciber-físico**, não agentic AI.                                                                                                                               |
| P12 | "                                             | RQ5 Research Gaps            | Parcialmente Respondida     | **P**         | §V, §VI (p.15–20)       | Direções futuras: online learning/atualização contínua, robustez adversarial, hardware (FPGA), privacidade (federated/homomorphic), zero-trust. Sobreposição com threat models/robustez/governança da RSL, mas **específicas de GenAI-em-segurança**, não lacunas de agentic AI.                                                                                                                                                                         |
|     |                                               | **SCORE_RQ**                 |                             | **1.5 / 5.0** |                         | N + N + P + P + P                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo             | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | -------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P12 | Survey / revisão narrativa | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (segurança/resiliência de sistemas autônomos) e contribuições (mapear GenAI para cibersegurança/decisão/arquiteturas resilientes) explícitos (§I).
- **QA2 = N** — revisão **narrativa sem protocolo sistemático** (sem bases, string de busca, critérios de inclusão/exclusão, contagens). Tab. 1 apenas compara trabalhos relacionados.
- **QA3 = N** — **sem validação empírica própria**; síntese secundária (métricas como 98,2% são de trabalhos citados).
- **QA4 = P** — conclusões coerentes e §V de desafios extensa; porém sem discussão das limitações metodológicas do próprio survey.

## Parecer final do revisor

**Síntese.** P12 é um **caso limítrofe**. É a **primeira do corpus a habitar o domínio certo — cibersegurança e resposta a ameaças** — cobrindo LLMs em pentesting, intrusion/malware detection, threat intelligence a partir de **relatórios de incidentes (CTI)**, SOAR/SOC, e riscos adversariais de LLMs (jailbreak, prompt injection, data extraction). Isso a distingue nitidamente de P7/P8/P11 (SCORE_RQ 0). **Porém**, o enquadramento é **Generative AI** (GANs/VAEs/Transformers/LLMs), **não Agentic AI** (o construto central da RSL): não define autonomia/capacidades agênticas (RQ1=N) nem apresenta arquitetura de engenharia agêntica (RQ2=N). Além disso, o alvo primário são **sistemas ciber-físicos autônomos** (drones/veículos/robôs), não copilotos de IR de TI. Daí SCORE_RQ 1.5/5 (três P's no domínio de segurança). Qualidade metodológica Média (QA 1.5): narrativa sem protocolo (QA2=N), sem evidência própria (QA3=N).

**Recomendação: INCLUIR COM RESSALVAS** _(decisão de fronteira — ver nota)_. Justificativa: fornece **material de fundamentação genuíno** para as dimensões de **benefícios em cibersegurança/IR (RQ3)**, **riscos adversariais/segurança de LLMs (RQ4)** e **lacunas de robustez/threat models (RQ5)** — úteis à RSL sobre Agentic AI Copilot para IR, especialmente o inventário de aplicações de LLM em segurança (Tab. 5) e a taxonomia de ataques adversariais a LLMs. **Ressalvas fortes:** (i) é **Generative AI, não Agentic AI** — não usar para RQ1/RQ2 (definições/arquitetura agêntica), que ficam N; (ii) alvo é sistema ciber-físico, não IR de TI/SOC — aderência a IR é **adjacente**, não central; (iii) metodologia narrativa não-reprodutível (QA2=N) e sem evidência própria (QA3=N); (iv) **versão de autor aceita** (não final editada) — reverificar dados na versão publicada.

**Nota de decisão (para o orientando).** Se a RSL aplicar critério **estrito de inclusão "somente Agentic AI"**, P12 deve ser **EXCLUÍDA por escopo** (RQ1/RQ2=N; é GenAI). Se admitir **referências adjacentes de cibersegurança/segurança de LLMs** como fundamentação, **INCLUIR COM RESSALVAS** (como aqui). Recomendo decidir esse critério no protocolo da RSL para tratar P12 de forma consistente.

**Pendências de verificação externa:**

- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
- **SJR (quartil)** → Scimago Journal Rank (_IEEE Access_); insumo informa Q1.
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES; insumo informa A1.
- **Dados bibliográficos finais** → confirmar volume/páginas na **versão publicada** (o PDF é versão de autor com placeholders de template).
