# Avaliação de Estudo Candidato - Ciclo 2 (RSL Agentic AI Copilot para IR)

**Contexto:** Artigo "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura"  
**Orientação e Diretrizes:** Kitchenham (2009) / Critérios DARE (QA1–QA4)  
**Programa:** PPGCA - Unisinos  

---

## 1. Dados de Entrada do Estudo

- **ID:** P74
- **Artigo:** Transitioning from MLOps to LLMOps: Navigating the Unique Challenges of Large Language Models
- **Arquivo:** `P74_Transitioning_from_MLOps_to_LLMOps_Navigating_the_Unique_Challenges_of_Large_Language_Models.pdf`
- **Qualis Informado:** A2 (derivado do percentil Scopus 79.0%, regra CAPES 2025–2028)
- **SJR Quartile Informado:** Q2
- **Ressalvas de Triagem:** Aprovado na triagem; estudo secundário sobre LLMOps (tema prioritário da tese); contraste conceitual.

---

## 2. Etapa 1 — Triagem de Elegibilidade

- **Ano ($\ge 2020$):** 2025 (Publicado em 23/01/2025). *(Atende)*
- **Publicação $\neq$ NULL:** *Information* (MDPI). *(Atende)*
- **Citações ($\ge 1$):** `[VERIFICAR]` (artigo recente, publicado no início de 2025).
- **SJR (Q1–Q2):** Q2 (`[VERIFICAR no Scimago Journal Rank]`).
- **Qualis (A1–A2):** A2 (`[VERIFICAR na Plataforma Sucupira / Qualis CAPES]`).
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações na base indexadora, confirmação de SJR e Qualis). Procede-se à extração por se tratar de estudo secundário sobre LLMOps aprovado em triagem temática preliminar.

---

## 3. Tabela A — Bibliométrica (Alimenta a Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P74** | *Information* (MDPI) | 2025 | `[VERIFICAR]` (Google Scholar/Scopus) | Q2 `[VERIFICAR no Scimago]` | A2 `[VERIFICAR no Sucupira]` | Review / Survey | [10.3390/info16020087](https://doi.org/10.3390/info16020087) |

---

## 4. Tabela B — Classificação das RQs (Alimenta a Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **P74** | Transitioning from MLOps to LLMOps... | **RQ1** | Não tem conteúdo suficiente | **N** (0.0) | Sec. 1, 3.1–3.4 (p. 2–3, 10–13) | O artigo foca na transição operacional de MLOps para LLMOps, RAG e ciclo de vida de LLMs. Não aborda a taxonomia formal de Agentic AI, arquiteturas de planejamento deliberativo, memória episódica autônoma ou modelos de tomada de decisão agêntica sob supervisão humana. |
| **P74** | Transitioning from MLOps to LLMOps... | **RQ2** | Parcialmente Respondida | **P** (0.5) | Sec. 3.2, 3.6, Fig. 3, Tab. 2 (p. 10–12, 15–17) | Cobre amplamente arquiteturas de suporte a LLMs: RAG acoplado a bancos vetoriais, ferramentas de orquestração e cadeias (LangChain), stacks de nuvem (Vertex AI, AWS Inferentia) e frameworks de observabilidade de LLMs. Contudo, não contempla orquestração multiagente nem guardrails de execução agêntica em IR. |
| **P74** | Transitioning from MLOps to LLMOps... | **RQ3** | Não tem conteúdo suficiente | **N** (0.0) | Sec. 2.2, 3.5 (p. 5–7, 13–15) | Apresenta benefícios qualitativos de produtividade e cita superficialmente casos de uso em domínios como cibersegurança e saúde. Não apresenta evidências empíricas quantitativas, benchmarks ou métricas operacionais aplicadas a Resposta a Incidentes (ex.: MTTD, MTTR, alívio de fadiga de alertas). |
| **P74** | Transitioning from MLOps to LLMOps... | **RQ4** | Parcialmente Respondida | **P** (0.5) | Sec. 1 (p. 2), Sec. 3.4 (p. 13–14), Sec. 6 (p. 22–23) | Analisa vulnerabilidades e ameaças inerentes a LLMs em produção (adversarial attacks, jailbreaks, data poisoning, vazamento de dados via embeddings e viés algorítmico). Defende práticas de DevSecOps, guardrails de conformidade e auditoria ética, embora de forma genérica para modelos de fundação. |
| **P74** | Transitioning from MLOps to LLMOps... | **RQ5** | Parcialmente Respondida | **P** (0.5) | Sec. 6 (p. 22–23) | Aponta lacunas futuras relevantes em integração de LLMs a esteiras de CI/CD, dificuldades de padronização de testes cross-platform, necessidade de mecanismos Human-in-the-Loop (HITL) para mitigação contínua de vieses e desafios de avaliação em larga escala. |
| **P74** | **SCORE_RQ TOTAL** | | | **1.5 / 5.0** | | |

---

## 5. Tabela C — Avaliação de Qualidade QA (Alimenta a Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P74** | Review / Survey narrativa | 1.0 (Y) | 0.5 (P) | 0.0 (N) | 0.5 (P) | **2.0 / 4.0** | **Média** |

### Justificativas dos Critérios DARE:
- **QA1 (Objetivos Claros = 1.0 / Y):** O objetivo é bem delimitado: mapear as discrepâncias e necessidades arquiteturais/operacionais entre MLOps tradicional e LLMOps, contextualizando infraestrutura, dados e governança.
- **QA2 (Metodologia Replicável = 0.5 / P):** Apresenta taxonomia clara e tabelas comparativas detalhadas com versões de softwares e ferramentas (Tabelas 1–6). Contudo, não é uma RSL formal: inexiste protocolo de busca com string reprodutível ou critérios explícitos de exclusão de literatura.
- **QA3 (Base de Evidências Sólidas = 0.0 / N):** Estudo de natureza conceitual/secundária. Não apresenta experimento empírico original, simulação controlada com métricas operacionais ou estudo de caso industrial conduzido diretamente pelos autores.
- **QA4 (Conclusões Coerentes = 0.5 / P):** As conclusões refletem adequadamente a análise teórica e bibliográfica realizada, mas o estudo carece de discussão crítica aprofundada sobre as limitações do método de levantamento adotado.

---

## 6. Parecer Final do Revisor

- **Síntese:** Trata-se de uma revisão recente e abrangente sobre as diferenças conceituais e práticas entre DevOps, MLOps e LLMOps. O trabalho organiza de forma muito clara os componentes de ciclo de vida de modelos de linguagem (RAG, vector stores, fine-tuning, inferência e observabilidade). Embora não aborde especificamente sistemas agênticos ou rotinas táticas de Incident Response, fornece a fundamentação operacional de infraestrutura necessária para sustentar arquiteturas de LLMs em produção.
- **Recomendação:** **INCLUIR COM RESSALVAS**. O trabalho deve ser incorporado na fundamentação teórica e nas discussões de infraestrutura/arquitetura (RQ2) e governança/desafios (RQ4) como estudo secundário de referência para LLMOps, ressaltando-se que não aborda diretamente a automação agêntica em IR.
- **Pendências de Verificação Externa:**
  1. *Citações:* Verificar contagem atualizada no Scopus ou Google Scholar.
  2. *SJR:* Validar percentil e quartil Q2 na base Scimago Journal Rank.
  3. *Qualis CAPES:* Validar estrato A2 para o periódico *Information* (ISSN 2073-431X) na Plataforma Sucupira/CAPES.