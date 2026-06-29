# Avaliação RSL — Estudo P20

**Artigo:** _LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code_ — D. Toprani & V. K. Madisetti
**Arquivo:** P20-A1-LLM_Agentic_Workflow...pdf (7 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.       | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                         | DOI                         |
| --- | --------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------------- | --------------------------- |
| P20 | IEEE Access (Vol. 13) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa c/ avaliação experimental | 10.1109/ACCESS.2025.3560911 |

_Evidências: cabeçalho p.1 (DOI, datas: recebido 06/02/2025, publicado 15/04/2025); rodapé "VOLUME 13, 2025" e licença CC-BY 4.0 (p.1). Periódico identificado como IEEE Access pelo prefixo DOI 10.1109/ACCESS e formato. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                     | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                     | Parecer do revisor                                                                                                                                                                                                                                                            |
| --- | -------------------------- | ---------------------------- | ----------------------- | ------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P20 | LLM Agentic Workflow (IaC) | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §III.A "Multi-Agent Orchestration" (p.2-3) | Descreve agentes especializados e uso de ferramentas (b), mas não define níveis de autonomia nem supervisão humana (a), nem um modelo formal de tomada de decisão (c).                                                                                                        |
| P20 | "                          | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §III, §IV.A-B (p.2-4), Fig.1               | Arquitetura multi-agente em pipeline (a); stack explícito — Claude Sonnet 3.5 V2 via Amazon Bedrock Agents, Titan Embeddings V2, OpenSearch, RAG (b); capacidades avançadas: RAG + base de conhecimento contínua + integração CI/CD (c). Guardrails/observabilidade ausentes. |
| P20 | "                          | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §V, Tabelas 1 e 2 (p.4-6)                  | Benefícios qualitativos (menos alucinações, melhor remediação) (a); métricas quantitativas — 85% detecção, ~15% FP, latência 80-100s (b); evidência empírica em 10 templates com ground-truth anotado por engenheiro certificado (c), embora N pequeno.                       |
| P20 | "                          | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §VI "Limitations" (p.6)                    | Desafios técnicos bem cobertos — dependência de KB atualizada, templates condicionais, FP, latência (a). Ausência de discussão ética/governança/accountability (b) e de mecanismos de governança (c).                                                                         |
| P20 | "                          | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | §VI.C, §VII "Future Work" (p.6-7)          | Lacunas e direções explícitas: feedback loop, "context modules", abordagem híbrida static+LLM, ablação sobre KB, generalização p/ Terraform/multi-cloud. Não aborda threat models/alinhamento.                                                                                |
|     |                            | **SCORE_RQ**                 |                         | **4.0 / 5.0** |                                            |                                                                                                                                                                                                                                                                               |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                         | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------------ | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P20 | Artigo de pesquisa / estudo empírico de pequena escala | **Y** (1.0) | **P** (0.5) | **P** (0.5) | **Y** (1.0) | **3.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (misconfigurations em IaC que ferramentas estáticas/rule-based não pegam) e solução agêntica explícitos (§I, §II, p.1-2).
- **QA2 = P** — arquitetura e tecnologias descritas (§IV), mas sem prompts completos, parâmetros do modelo, ou dataset público; corpus não compartilhado → replicação parcial.
- **QA3 = P** — validação empírica real com métricas (Tabelas 1-2), porém N=10 templates, anotação por **um** único engenheiro e sem comparação quantitativa head-to-head com CDK-Nag (apesar de citada como objetivo) → acima de toy example, abaixo de validação robusta.
- **QA4 = Y** — conclusões derivam das evidências e limitações são amplamente discutidas (§VI), incluindo mitigações.

## Parecer final do revisor

**Síntese.** O estudo apresenta um workflow agêntico (multi-agente + RAG + base de conhecimento contínua) para detecção e remediação de vulnerabilidades em IaC (AWS CloudFormation), com forte aderência à **RQ2** (arquitetura/orquestração/ferramentas) e à **RQ3** (benefícios e métricas quantitativas: 85% de detecção, ~15% de FP, latência 80-100s). É mais fraco na **RQ1** (não há definição de autonomia nem modelo decisório formal) e na **RQ4** (cobre desafios técnicos, mas omite dimensões éticas/governança). O domínio é **segurança preventiva de IaC**, não Resposta a Incidentes em sentido estrito — a relação com IR é indireta (prevenção pré-deploy), o que deve ser registrado ao mapear o escopo da RSL.

**Recomendação: INCLUIR COM RESSALVAS.** Estudo de qualidade Alta (QA 3.0) e SCORE_RQ 4.0, empírico e relevante para as RQs de arquitetura e evidências agênticas. Ressalvas: (i) escopo é detecção/remediação de vulnerabilidades, não IR operacional — usar com essa fronteira clara; (ii) evidência empírica de pequena escala (N=10, anotador único, sem baseline quantitativo); (iii) lacunas em autonomia/decisão e ética/governança.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → verificar em base indexadora (IEEE Xplore / Scopus / Google Scholar).
- **SJR (quartil)** → verificar no Scimago Journal Rank para _IEEE Access_ (insumo informa Q1).
- **Qualis (estrato)** → verificar na Plataforma Sucupira / Qualis CAPES (insumo informa A1).

Os três critérios de elegibilidade dependentes desses dados (Citações ≥ 1, SJR Q1-Q2, Qualis A1-A2) ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**; os critérios verificáveis no PDF (Ano ≥ 2020 ✓ 2025; veículo ≠ NULL ✓ IEEE Access) estão atendidos.
