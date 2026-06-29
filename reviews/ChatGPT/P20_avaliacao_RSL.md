# Avaliação do Estudo P20

## Identificação do estudo

**ID:** P20  
**Artigo:** *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code*  
**Autores:** Dheer Toprani e Vijay K. Madisetti  
**Veículo:** IEEE Access, Volume 13  
**Ano:** 2025  
**Escopo da avaliação:** conteúdo exclusivamente presente no PDF fornecido.

> **Nota metodológica:** os valores de SJR, Qualis e número de citações não são verificáveis no PDF. Embora o prompt informe SJR Q1 e Qualis A1, esses dados foram mantidos como **[VERIFICAR]**, conforme a regra antifabricação estabelecida.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P20 | IEEE Access, Volume 13 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com avaliação controlada de um protótipo multiagente | 10.1109/ACCESS.2025.3560911 |

**Fontes para verificação externa:**

- **Citações:** base indexadora, como Scopus, Web of Science, IEEE Xplore ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência | Resultado |
|---|---|---|
| Ano ≥ 2020 | O cabeçalho informa publicação em 15 de abril de 2025, p. 1. | Atendido |
| Publicação identificável | IEEE Access, Volume 13, 2025, p. 1. | Atendido |
| Citações ≥ 1 | O número de citações do artigo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Como não foi identificado critério interno de inelegibilidade, a extração completa prossegue, condicionada à verificação externa dos três itens pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | RQ1 — Context Definitions | Parcialmente Respondida | P | Seção III.A.3, p. 3 (69177); Figura 1, p. 3; Seção IV.A, p. 3. | O artigo caracteriza um fluxo com agentes especializados para recuperação, detecção e geração de relatório. Há um modelo decisório sequencial e uso explícito de conhecimento recuperado. Contudo, não apresenta uma definição formal de autonomia, níveis de autonomia, planejamento autônomo, memória persistente ou um modelo operacional de supervisão humana. |
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seções III.A.2–III.A.3, p. 3; Seções IV.A–IV.D, pp. 3–4 (69177–69178). | A arquitetura multiagente com RAG é descrita, assim como Claude Sonnet 3.5 V2, Amazon Bedrock Agents, Titan Text Embeddings V2 e uma base vetorial exemplificada por Amazon OpenSearch. A cobertura é incompleta para operação em produção, pois não há especificação de observabilidade do sistema, guardrails formais, gestão de memória dos agentes, controle de acesso ao fluxo ou mecanismos robustos de fallback. |
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | RQ3 — Evidence Benefits | Parcialmente Respondida | P | Seção V.A, pp. 4–5; Tabela 1, p. 5 (69179); Seções V.B–V.F, pp. 5–6; Tabela 2, p. 6 (69180). | O estudo apresenta benefícios qualitativos e quantitativos: 17 de 20 vulnerabilidades detectadas, precisão, recall e F1 globais de 85%, três falsos positivos, aproximadamente 5% de sobrerremediação e tempo médio total de 85,1 segundos por template. A evidência é empírica, porém limitada a dez templates, vinte vulnerabilidades conhecidas e anotação de referência realizada por um único engenheiro. Além disso, não mede MTTD, MTTR, carga cognitiva ou resultados de resposta a incidentes. |
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seções V.C–V.E, p. 5; Seção VI.A–VI.C, p. 6 (69180); Seção VII, p. 7 (69181). | O artigo discute falsos positivos, alucinações, sobrerremediação, dependência de uma base atualizada, latência e dificuldade com templates condicionais. Também propõe mitigação por fontes autoritativas, estimativa de incerteza, feedback de usuários e políticas organizacionais. Entretanto, não desenvolve aspectos éticos, accountability, responsabilidade por decisões, auditoria, privacidade, controle de privilégios ou supervisão humana mandatória. |
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção V.F, p. 6; Seção VI.B–VI.C, p. 6; Seção VII, p. 7 (69181). | As lacunas e direções futuras são explícitas: ampliar o conjunto de avaliação, usar rotulagem semiautomatizada, executar estudos de ablação, melhorar o parsing de condicionais, criar feedback de desenvolvedores, incorporar políticas internas, combinar análise estática e LLM e generalizar para Terraform e ambientes multicloud. |
| P20 |  | **SCORE_RQ** | **3,0 / 5,0** | **P + P + P + P + T** |  | O estudo contribui de forma relevante para arquitetura, avaliação empírica e agenda futura, mas sua aderência é parcial às dimensões de autonomia, produção responsável e resposta a incidentes. |

### Síntese por subdimensão

- **RQ1:** cobre características centrais e fluxo decisório, mas não define autonomia nem supervisão humana.
- **RQ2:** cobre arquitetura, ferramentas e RAG, mas não descreve integralmente guardrails, memória e observabilidade operacional.
- **RQ3:** apresenta evidência qualitativa e quantitativa, porém em um experimento pequeno e fora do contexto direto de resposta a incidentes.
- **RQ4:** cobre desafios técnicos e algumas mitigações, mas não oferece tratamento suficiente de ética, governança e accountability.
- **RQ5:** apresenta lacunas e direções futuras claras, variadas e diretamente relacionadas às limitações observadas.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P20 | Estudo empírico experimental com avaliação controlada de protótipo | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é apresentado como a limitação de ferramentas estáticas e baseadas em regras diante de vulnerabilidades contextuais e interdependentes. O objetivo de detectar configurações inseguras e produzir remediações acionáveis por meio de LLM, RAG e agentes especializados é explícito na Introdução, pp. 1–2, e na Seção III, pp. 2–3.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo descreve a arquitetura, os agentes, os modelos empregados, a base de conhecimento, o parsing de CloudFormation e a estrutura geral do prompt nas Seções III e IV, pp. 2–4. Entretanto, não fornece o prompt integral, parâmetros de inferência, configuração de recuperação, valor de *top-k*, critérios de seleção dos templates, artefatos experimentais ou código-fonte. Essas ausências impedem uma replicação fiel.

**QA3 — Base de evidências sólidas: Y (1,0).**  
Há avaliação empírica com dez templates CloudFormation, vinte vulnerabilidades conhecidas, comparação entre detecções e *ground truth*, métricas de precisão, recall, F1, falsos positivos e desempenho temporal. As Tabelas 1 e 2, pp. 5–6, apresentam resultados por template. A validade externa é limitada pelo pequeno corpus e pela anotação realizada por um único especialista, mas existe experimento quantitativo estruturado.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões retomam os resultados de detecção, contextualização e integração em CI/CD e reconhecem limitações relacionadas à atualização da base, configurações especializadas, custos de execução e remediações excessivamente conservadoras. As Seções VI–VIII, pp. 6–7, mantêm coerência com as evidências apresentadas.

---

## Parecer final do revisor

O estudo apresenta uma arquitetura multiagente concreta para detecção e remediação de vulnerabilidades em Infrastructure-as-Code, combinando LLM, RAG, base de conhecimento e integração com CI/CD. Sua principal contribuição para a RSL está na descrição arquitetural e na avaliação empírica com métricas de detecção e desempenho. A aderência ao tema de Agentic AI é relevante, mas parcial: o artigo não formaliza níveis de autonomia, supervisão humana, memória, accountability ou observabilidade dos agentes. Também atua de forma preventiva sobre IaC, sem avaliar diretamente resposta a incidentes, MTTD, MTTR ou carga cognitiva.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada porque o artigo fornece evidência empírica, arquitetura multiagente e mecanismos de remediação automatizada relevantes para segurança e automação operacional. As ressalvas decorrem da distância em relação ao contexto direto de resposta a incidentes, da limitada discussão de governança e autonomia e da escala reduzida da avaliação. A inclusão definitiva deve ser condicionada à confirmação dos critérios bibliométricos externos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
