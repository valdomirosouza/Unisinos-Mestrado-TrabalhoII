# Avaliação RSL — Estudo P14

**Artigo:** _Transforming Cybersecurity with Agentic AI to Combat Emerging Cyber Threats_ — Nir Kshetri (The University of North Carolina at Greensboro, Bryan School of Business, EUA — autor único)
**Arquivo:** P14-A1 - Transforming Cybersecurity with Agentic AI to Combat Emerging Cyber Threats.pdf (32 páginas)

> ⚠️ **Recomendação: INCLUIR COM RESSALVAS — condicional à verificação de elegibilidade.** Conteúdo mais aderente do corpus (Agentic AI × SOC × Resposta a Incidentes; SCORE_RQ 4.0/5), MAS é **preprint SSRN não revisado por pares** com base em alegações de fornecedores. QA 1.5/4. **Insumo (Qualis A1/SJR Q1) inconsistente com o artefato (preprint).**

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                  | Ano  | Cit.                          | SJR                                          | Qualis                                       | Tipo                                       | DOI                                        |
| --- | -------------------------------- | ---- | ----------------------------- | -------------------------------------------- | -------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| P14 | **Preprint SSRN** (não revisado) | 2025 | [VERIFICAR] (base indexadora) | **N/A no artefato** (insumo: Q1) [VERIFICAR] | **N/A no artefato** (insumo: A1) [VERIFICAR] | Preprint não revisado / análise conceitual | SSRN abstract=5159598 (sem DOI de revista) |

_Evidências: carimbo em todas as páginas — "This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5159598". Autor único (Nir Kshetri, UNC Greensboro). Ano inferido 2025 (fontes 2024–2025). Não há periódico/DOI/volume/indexação. Como preprint SSRN, SJR/Qualis não se aplicam ao artefato — conflito com o insumo (A1/Q1)._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                   | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)      | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --- | ---------------------------------------- | ---------------------------- | ----------------------- | ------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P14 | Transforming Cybersecurity w/ Agentic AI | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | §2 (p.5–6)                  | Define AI agents/agentic AI: autonomia (perceber/decidir/agir com mínima intervenção), **memória entre tarefas**, integração de múltiplos modelos, decidir quando acessar sistemas internos/externos; distingue de IA tradicional (a, b, c). Profundidade de nível executivo/consultoria, mas cobre as três subdimensões.                                                                                                                                                                     |
| P14 | "                                        | RQ2 Engineering Architecture | Parcialmente Respondida | **P**         | §3–4, §6 (p.7–11, 20–22)    | Toca componentes de arquitetura de forma **dispersa**: memória, integração multi-modelo, **camada de orquestração** (menção a "bug na orchestration layer"), acesso a ferramentas/sistemas, e **guardrails/observabilidade** (least-privilege, zonas confiáveis/não-confiáveis, audit trails, monitoramento, logging). Não há tratamento arquitetural sistemático.                                                                                                                            |
| P14 | "                                        | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §3, Tab. 1, §6 (p.7–11, 20) | **Melhor cobertura de benefícios em IR do corpus** — e **diretamente em Resposta a Incidentes/SOC**: automação de triagem/alertas, tier 1/2, detecção/resposta autônoma. Métricas: CrowdStrike Charlotte AI (98% acurácia triagem, −40h/sem), ReliaQuest (20× mais rápido, 98% alertas, contenção <5 min, 1000+ empresas), Darktrace (−90% tempo triagem), Gartner (+40% eficiência SOC até 2026). **⚠️ Métricas são alegações de fornecedores (vendor claims), não validação independente.** |
| P14 | "                                        | RQ4 Challenges & Ethics      | Respondida Plenamente   | **T**         | §4–6 (p.11–22)              | Desafios técnicos (superfície de ataque ampliada, manipulação adversarial, data poisoning, DoS por orquestração, perda de supervisão); **uso malicioso** (ataques autônomos, phishing/ransomware, fraude de identidade sintética); mecanismos de governança — **Risk Management Framework (NIST, Tab. 2)**, guardrails, least-privilege, threat modeling, audit trails, compliance (HIPAA/CCPA), onboarding/offboarding de agentes.                                                           |
| P14 | "                                        | RQ5 Research Gaps            | Parcialmente Respondida | **P**         | §6 (p.20–23)                | Implicações/lacunas: gap entre assistentes LLM e agentes plenamente autônomos, necessidade de frameworks de governança alinhados a padrões nacionais/globais, começar por casos de uso restritos, refinamento/confiabilidade, reavaliar frameworks de cibersegurança. Framing de implicação prática, não agenda de pesquisa estruturada.                                                                                                                                                      |
|     |                                          | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                             | T + P + T + T + P                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                             | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda     |
| --- | ------------------------------------------ | ----------- | ----------- | ----------- | ----------- | ------------- | --------- |
| P14 | Preprint não revisado / análise conceitual | **Y** (1.0) | **N** (0.0) | **N** (0.0) | **P** (0.5) | **1.5 / 4.0** | **Média** |

_Âncoras:_

- **QA1 = Y** — problema (agentic AI transformando cibersegurança + riscos) e RQs explícitos (RQ1/RQ2), estrutura clara (§1).
- **QA2 = N** — **sem metodologia sistemática** (sem bases, string, critérios); síntese narrativa de fontes de indústria/consultoria. Autor único, ensaio.
- **QA3 = N** — **sem validação empírica própria**; base de evidências são **alegações de fornecedores e relatórios de consultoria** (BCG, Gartner, Malwarebytes, ReliaQuest/CrowdStrike/Darktrace) — secundárias/promocionais, não validadas. Agrava-se por **não ser peer-reviewed**.
- **QA4 = P** — conclusões coerentes com o material apresentado (responde RQ1/RQ2); porém **sem discussão das limitações do próprio estudo** e sem revisão por pares.

## Parecer final do revisor

**Síntese.** P14 é, **em conteúdo, o estudo mais aderente do corpus ao tema exato da RSL** — _Agentic AI Copilot para Resposta a Incidentes_: trata explicitamente de **agentic AI em SOCs, triagem de alertas, incident response tier 1/2, detecção e resposta autônoma de ameaças**, com exemplos comerciais reais (CrowdStrike, ReliaQuest, Darktrace, Twine), um **Risk Management Framework** (NIST) e discussão de governança/uso malicioso. Daí o SCORE_RQ 4.0/5, o mais alto entre os estudos de domínio de IR. **Contudo, a qualidade evidencial e a elegibilidade são frágeis:** trata-se de um **preprint SSRN explicitamente não revisado por pares**, cuja base são **relatórios de consultoria e alegações de fornecedores** (as métricas de 98%/20×/<5 min são _vendor claims_, não validação independente). QA 1.5 (Média): sem metodologia (QA2=N), sem evidência própria (QA3=N).

**⚠️ Conflito insumo × artefato:** o insumo declara **Qualis A1 / SJR Q1**, incompatível com um **preprint SSRN** (que não possui periódico/SJR/Qualis). Isto precisa ser resolvido antes da decisão final.

**Recomendação: INCLUIR COM RESSALVAS — condicional à verificação de elegibilidade.** Duas trilhas:

1. **Se existir versão publicada e revisada por pares** deste trabalho (Nir Kshetri publica em _IEEE IT Professional/Computer_ etc.) em veículo **A1–A2 / Q1–Q2** → **substituir o PDF pela versão publicada** e **INCLUIR** (relevância excepcional para RQ1/RQ3/RQ4).
2. **Se somente o preprint SSRN existir** → sob critério estrito da RSL (peer-review + SJR/Qualis), **EXCLUIR por elegibilidade** (não revisado por pares; A1/Q1 do insumo não se sustentam).

**Ressalvas inegociáveis (em qualquer trilha):** (i) **jamais citar as métricas (98%/20×/<5 min/−90%) como evidência validada** — são alegações de fornecedores em preprint não revisado; usar apenas como _ilustração de mercado/afirmações da indústria_; (ii) tratar definições/benefícios como **fundamentação de nível executivo**, corroborando-os com fontes acadêmicas revisadas; (iii) sinalizar a natureza não-peer-reviewed em qualquer citação.

**Pendências de verificação externa (prioritárias):**

- **Status de publicação** → localizar versão peer-reviewed/indexada (periódico, DOI). **Decisivo para elegibilidade.**
- **Qualis/SJR reais** → só se aplicam se houver periódico; reconciliar com o insumo (A1/Q1 atualmente **sem suporte no artefato**).
- **Citações ≥ 1** → base indexadora (Scopus/WoS/Google Scholar).
