# Avaliação RSL — Estudo P37

**Artigo:** _Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response_ — O. I. Falowo, J. Bou Abdo (University of Cincinnati, USA)
**Arquivo:** P37-A2-algorithms-19-00062-v2.pdf (32 páginas)

> ⚠️ **Alerta de tipo de estudo:** **estudo empírico de levantamento (survey de percepção)** — primário, **diretamente sobre adoção de Agentic AI em IR**, porém **NÃO descreve/avalia um sistema agêntico**. Mede **percepções de 194 profissionais** (confiança, delegação de autonomia, prontidão de frameworks NIST/SANS/SOAR). Categoria distinta dos estudos técnicos de sistema — evidência do **lado da demanda/governança**.

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                 | Ano  | Cit.                                                            | SJR                               | Qualis                                          | Tipo                                                                                                 | DOI               |
| --- | ------------------------------- | ---- | --------------------------------------------------------------- | --------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------- |
| P37 | Algorithms (MDPI) (Vol. 19, 62) | 2026 | [VERIFICAR] (base indexadora — provável baixa, pub. 11/01/2026) | [VERIFICAR] (Scimago; insumo: Q2) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A2) | Estudo empírico de levantamento (survey de percepção; 194 respondentes, validação psicométrica, IRB) | 10.3390/a19010062 |

_Evidências: cabeçalho p.1 (DOI; recebido 02/12/2025, aceito 07/01/2026, publicado 11/01/2026); "Algorithms 2026, 19, 62"; MDPI, CC-BY. Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                                       | RQ                           | Veredito                    | Símbolo       | Evidência (seção/pág.)            | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --- | -------------------------------------------- | ---------------------------- | --------------------------- | ------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P37 | Survey: AI Trust & Framework Readiness in IR | RQ1 Context Definitions      | Parcialmente Respondida     | **P**         | §2.2, §4 (Q4-Q5) (p.2, 12-13)     | Define Agentic AI para os respondentes (sistemas autônomos/semi-autônomos de decisão) e mede **níveis de autonomia/confiança e supervisão humana** — confiança em decisão sem intervenção humana (13%), apoio a triagem autônoma (37%), preferência por co-gestão semi-autônoma (a/c parciais). Porém **não caracteriza tecnicamente** planejamento/memória/uso de ferramentas (b ausente) — é perspectiva de percepção, não de sistema. |
| P37 | "                                            | RQ2 Engineering Architecture | Não tem conteúdo suficiente | **N**         | —                                 | **Não descreve arquitetura agêntica alguma** — é um survey de percepções. Avalia prontidão de frameworks (NIST/SANS/SOAR) e demanda por estruturas modulares com auditabilidade, mas nenhum mecanismo de orquestração/memória/ferramentas/guardrails de um sistema.                                                                                                                                                                      |
| P37 | "                                            | RQ3 Evidence Benefits        | Parcialmente Respondida     | **P**         | §4 (Q3) (p.12)                    | Evidência **quantitativa de percepção** sobre benefícios (92% percebem redução de MTTD/MTTR; base empírica sólida de 194 com validação psicométrica) (a/b parciais), porém é **dado de percepção**, não desempenho medido de um sistema agêntico (c ausente).                                                                                                                                                                            |
| P37 | "                                            | RQ4 Challenges & Ethics      | Respondida Plenamente       | **T**         | §4-§5 (Q4-Q10), §5.6 (p.12-26)    | Cobertura **forte** (eixo central do estudo): confiança em decisão autônoma, oversight ético de decisões de AI-agent, lacuna de maturidade de threat modeling de IA, atraso regulatório (41%), accountability (a/b); demanda por **mecanismos de governança** — auditabilidade de decisão, modelos de risco específicos de IA, frameworks modulares, supervisão humana (c).                                                              |
| P37 | "                                            | RQ5 Research Gaps            | Respondida Plenamente       | **T**         | §4 (Q10: 96%), §5.6, §6 (p.22-27) | Lacunas e direções explícitas: modernização de frameworks de IR (consenso de 96%), nova taxonomia de ferramentas (79%), simulação/tabletop de próxima geração, modelos de risco de IA; roadmap de validação (pilotos, ajustes iterativos) como trabalho futuro.                                                                                                                                                                          |
|     |                                              | **SCORE_RQ**                 |                             | **3.0 / 5.0** |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P37 | Estudo empírico de levantamento (survey de percepção) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — 2 research questions explícitas e problema (modernização de IR frente a ameaças de IA) bem delimitado (§2.7).
- **QA2 = Y** — metodologia de survey **rigorosa e replicável**: cálculo de tamanho de amostra (fórmula p/ população finita), **aprovação IRB**, 194 respondentes, itens binários + de validação psicométrica, instrumento de pesquisa (Tabelas 1 e questões listadas), análise de MOE.
- **QA3 = Y** — validação empírica primária sólida (194 respondentes, validação **convergente/discriminante**, proporções com MOE). _Ressalva de escopo:_ a evidência é de **percepção**, não de desempenho de sistema agêntico — relevante para o uso na RSL, mas não rebaixa a solidez metodológica do levantamento.
- **QA4 = Y** — conclusões coerentes com os dados e **reflexão exemplar sobre vieses** (§6.1-6.3: viés de validade de construto, efeitos de enquadramento, formato binário, viés de amostragem).

## Parecer final do revisor

**Síntese.** Estudo empírico **primário e diretamente sobre Agentic AI em Resposta a Incidentes**, mas de natureza distinta dos demais: um **levantamento de percepções** de 194 profissionais (confiança em autonomia, adoção de agentic AI, prontidão de frameworks). Fornece **evidência do lado da demanda/governança** que os estudos técnicos não trazem: apenas 13% confiam em decisão de IA sem intervenção humana, 37% apoiam triagem autônoma, mas 96% querem modernização dos frameworks de IR para incluir dimensões de IA/agentes. Aderência forte a **RQ4** (confiança/governança/prontidão — eixo central) e **RQ5** (lacunas de framework); **RQ1 parcial** (autonomia/confiança sob ótica de percepção); **RQ2 = N** (sem sistema) e **RQ3 parcial** (percepção, não desempenho).

**Recomendação: INCLUIR COM RESSALVAS.** SCORE_RQ 3,0/5,0 e QA 4,0/4,0 (Banda Alta). Estudo metodologicamente **muito sólido** (IRB, validação psicométrica, reflexão de vieses) e de **alto valor para a discussão de adoção, confiança e governança** da RSL — complementa os estudos técnicos com a perspectiva do praticante/SOC. Ressalva central: **não é um sistema agêntico** (RQ2=N; evidência de percepção, não de eficácia operacional). Recomendo classificá-lo em categoria própria ("survey de percepção/adoção") no mapeamento, distinta dos estudos de sistema (P22/P25/P27/P28/P31/P32/P35).

> ⚠️ **Decisão de protocolo:** se o protocolo restringir a estudos que **proponham/avaliem sistemas agênticos**, P37 entraria como **evidência contextual de demanda/governança** (forte para fundamentação e discussão), não como caso técnico. Bom par com P33 (governança/ética) e P34 (copilot LLM) no eixo "humano/organizacional".

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar. ⚠️ Publicado em 11/01/2026 — contagem possivelmente baixa/0; atenção ao critério "Citações ≥ 1".
- **SJR (quartil)** → Scimago, _Algorithms_ (MDPI) (insumo: Q2).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A2).

Critérios verificáveis no PDF atendidos (Ano 2026 ✓; veículo MDPI Algorithms ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
