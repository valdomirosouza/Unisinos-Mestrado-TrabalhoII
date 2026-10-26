# Avaliação Sistemática da Literatura (RSL) — Ciclo 2

## Registro de Avaliação: Estudo P83

---

### 1. Insumos e Diretrizes do Estudo

* **ID do Estudo:** P83
* **Título do Artigo:** Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot
* **Autores:** Ismail, Rahmat Kurnia, Farid Widyatama, Ilham Mirwansyah Wibawa, Zilmas Arjuna Brata, Ukasyah, Ghitha Afina Nelistiani, Howon Kim
* **Periódico:** *Sensors* (MDPI), Vol. 25, N. 3, Art. 870, 2025
* **DOI:** `10.3390/s25030870`
* **Insumos de Triagem:** 
  * Qualis presumido: A1 (derivado do percentil Scopus 91.0%, regra CAPES 2025–2028)
  * SJR Quartil presumido: Q1
  * Ressalvas de triagem: Aprovado na triagem; foco no núcleo de Copilot RAG em SOC; avaliação comparativa restrita (2 modelos LLM vs. ground truth).
* **Referencial Metodológico:** Diretrizes de Kitchenham (2009) para RSL em Engenharia de Software e critérios DARE (QA1–QA4).

---

### 2. Triagem de Elegibilidade (Critérios PRISMA)

| Critério | Verificação no Texto | Situação |
| :--- | :--- | :--- |
| **Ano $\ge$ 2020** | Publicado online em 31 de janeiro de 2025 | Cumprido |
| **Publicação $\neq$ NULL** | *Sensors* (MDPI) | Cumprido |
| **Citações $\ge$ 1** | Artigo de publicação recente (janeiro/2025) | `[VERIFICAR]` (Google Scholar / Scopus) |
| **SJR Q1–Q2** | Apontado como Q1 no insumo | `[VERIFICAR]` (SCImago Journal Rank) |
| **Qualis A1–A2** | Apontado como A1 no insumo | `[VERIFICAR]` (Plataforma Sucupira / CAPES) |

* **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações, confirmação de SJR e Qualis em bases indexadoras). Prossegue-se à extração completa.

---

### 3. Extração e Análise Detalhada das Questões de Pesquisa (RQs)

#### RQ1 — Context Definitions
* **Foco:** Capacidades, níveis de autonomia (planejamento, memória, ferramentas, supervisão humana) e modelo de tomada de decisão.
* **Evidência no Estudo:**
  * *(a) Autonomia:* O sistema SERC (*Security Event Response Copilot*) atua primariamente como copilot/assistente cognitivo para analistas humanos no SOC. O modelo mantém supervisão estrita do operador humano (*Human-in-the-Loop*), gerando planos e ações de mitigação sem execução de remediação ativa ou autônoma direta nos endpoints (Seção 1, p. 2; Seção 4.1, pp. 16–17).
  * *(b) Características Centrais:* Extração e estruturação em tempo real de alertas do SIEM, enriquecimento de contexto com fontes padronizadas de inteligência contra ameaças e interface conversacional contextual para esclarecimentos técnicos. Não formaliza memória episódica entre sessões distintas ou planejamento hierárquico deliberativo.
  * *(c) Tomada de Decisão:* Modelo centrado no analista humano, alimentado por um painel customizado integrado ao dashboard do Wazuh com recomendações estruturadas passo a passo.
* **Veredito:** **Parcialmente Respondida (P = 0.5)** — Aborda amplamente o paradigma de copilot e suporte à decisão, porém não conceitua formalmente níveis de autonomia agêntica nem arquiteturas com agentes autônomos de múltiplos passos.

---

#### RQ2 — Engineering Architecture
* **Foco:** Arquitetura de software, frameworks, orquestração, bases de conhecimento, guardrails e observabilidade.
* **Evidência no Estudo:**
  * *(a) Tipo de Arquitetura:* Pipeline RAG especializado em SOC com extração em duas fases: parsing/estruturação de logs não homogêneos via *prompting* *one-shot*, roteamento condicional por identificador MITRE, indexação vetorial tripartite e síntese por LLM gerador (Seções 3.1–3.4, pp. 11–16).
  * *(b) Ferramentas e Frameworks:* SIEM Wazuh, banco vetorial Qdrant, modelo de embeddings `BAAI/bge-large-en-v1.5` (otimizado via Matryoshka Representation Learning), emulador Atomic Red Team, gerador/extrator LLM Mistral Pixtral-Large-Instruct e OpenAI GPT-4o.
  * *(c) Capacidades Avançadas:* Separação explícita da base vetorial em 3 coleções temáticas (Incident Response Playbooks gerais, NIST CSF 2.0 e MITRE ATT&CK), serviço de middleware com verificação periódica e sincronização contínua de novas TTPs via API do MITRE, e normalização de logs JSON para texto denso otimizado para recuperação por similaridade de cosseno.
* **Veredito:** **Respondida Plenamente (T = 1.0)** — Excelente profundidade nos detalhes de engenharia, esquemas de prompt, banco vetorial, parâmetros de inferência (temperatura 0.1, top-k 50, top-p 0.9, max tokens 4096) e integração com SIEM.

---

#### RQ3 — Evidence Benefits
* **Foco:** Evidências quantitativas e qualitativas, métricas de tempo, assertividade e carga cognitiva em Incident Response.
* **Evidência no Estudo:**
  * *(a) Benefícios Qualitativos:* Redução da fadiga de alertas e da sobrecarga analítica de operadores SOC, aceleração do tempo de interpretação de eventos correlacionados e padronização das respostas segundo boas práticas regulatórias e táticas (Seções 1 e 2.8).
  * *(b) Benefícios Quantitativos e Métricas:* Validação empírica sobre 12 cenários de ataque simulados confrontados com o *ground truth* dos playbooks do SOCFortress.
    * *Cosine Similarity:* OpenAI obteve picos de até 75,81% (cenário 8), mas quedas acentuadas a 46,61% (cenário 6). Pixtral mostrou maior regularidade, alcançando até 71,69% (cenário 9).
    * *BERTScore (Precisão):* Pixtral manteve faixa de 84,5% a 87,0%; OpenAI variou entre 83,8% e 86,2%.
    * *BERTScore (Recall):* Pixtral obteve 85,6% a 87,5%; OpenAI registrou 84,8% a 87,0%.
    * *BERTScore (F1-score):* Pixtral oscilou entre 85,4% e 87,2%; OpenAI entre 84,9% e 86,5%.
    * *Limitação métrica:* Não reporta métricas de tempo operacional como MTTR (*Mean Time to Respond*) ou MTTD (*Mean Time to Detect*) em minutos/horas.
  * *(c) Nível de Evidência:* Experimento empírico em bancada de testes controlada com geração real de tráfego adversário contra agentes de monitoramento em endpoints de teste (Seção 4.2).
* **Veredito:** **Respondida Plenamente (T = 1.0)** — Avaliação empírica sólida com múltiplas métricas semânticas e contextuais padronizadas (BERTScore e similaridade de cosseno) sobre cenários representativos de incidentes cibernéticos.

---

#### RQ4 — Challenges & Ethics
* **Foco:** Riscos técnicos, robustez, privacidade de dados, accountability, governança e conformidade.
* **Evidência no Estudo:**
  * *(a) Desafios Técnicos:* Inconsistência e variabilidade de desempenho entre modelos fundacionais em ataques específicos (ex.: script interpreters e ransomware); risco de alucinação de mitigações inadequadas minimizado pelo desacoplamento da base RAG (Seções 2.8 e 5).
  * *(b) Desafios Éticos e Governança:* Ausência de debate sobre vazamento de informações sigilosas ou dados sensíveis (PII, credenciais em logs brutos) ao consumir endpoints de APIs comerciais como a da OpenAI.
  * *(c) Mecanismos de Governança:* O sistema mitiga riscos de ações errôneas preservando o operador humano como decisor final (*human-in-the-loop*), servindo estritamente como guia de consulta e recomendação.
* **Veredito:** **Parcialmente Respondida (P = 0.5)** — Trata com clareza a variabilidade de desempenho, latência e riscos de alucinações técnicas dos modelos, mas não aprofunda governança de dados, conformidade ou privacidade de logs.

---

#### RQ5 — Research Gaps
* **Foco:** Lacunas identificadas e direções futuras em IA para segurança cibernética.
* **Evidência no Estudo:**
  * Necessidade de fine-tuning com dados proprietários e de domínio para superar o platô de assertividade dos modelos genéricos (Seção 5, pp. 21–22).
  * Aplicação de treinamento adversarial e *active learning* guiado por feedback de analistas seniores de SOC para adaptação contínua a ameaças emergentes.
  * Evolução do Copilot consultivo para automação ponta a ponta mediante integração nativa com soluções de orquestração e resposta SOAR (*Security Orchestration, Automation, and Response*).
* **Veredito:** **Respondida Plenamente (T = 1.0)** — Apresenta direções de pesquisa claras, exequíveis e diretamente fundamentadas nos limites observados durante o experimento.

---

### 4. Avaliação de Qualidade (Critérios DARE / Kitchenham)

* **QA1 (Objetivos Claros): Y (1.0)** — Problema de pesquisa (fadiga de alertas e ineficiência na triagem manual em SOCs de código aberto) e solução proposta (SERC com arquitetura RAG e integração no Wazuh) plenamente delimitados.
* **QA2 (Metodologia Replicável): Y (1.0)** — Descrição rica dos componentes de software, esquemas de prompt, bibliotecas de chunking (NLTK), modelo de embedding, parâmetros de inferência e fontes de dados de referência (NIST CSF 2.0, MITRE ATT&CK e playbooks SOCFortress).
* **QA3 (Base de Evidências Sólidas): Y (1.0)** — Validação empírica sobre 12 cenários de ataque emulados com Atomic Red Team, medidos objetivamente via BERTScore e similaridade de cosseno contra ground truth estruturado.
* **QA4 (Conclusões Coerentes): P (0.5)** — Conclusões sustentadas pelos dados empíricos, mas as limitações discutidas restringem-se ao comportamento dos dois LLMs, deixando de discutir limitações operacionais da bancada (custos computacionais de inferência, vazão de eventos por segundo e latência em ambientes de produção com alto volume de dados).

---

### 5. Tabelas da RSL

#### Tabela A — Extração Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo de Estudo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P83** | *Sensors* (MDPI) | 2025 | `[VERIFICAR]` | `[VERIFICAR]` Q1 | `[VERIFICAR]` A1 | Experimental / Simulação de Bancada | `10.3390/s25030870` |

---

#### Tabela B — Classificação das Questões de Pesquisa (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência no Texto | Parecer do Revisor |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| P83 | Ismail et al. | RQ1 | Parcialmente Respondida | P (0.5) | Seção 1 (p. 2); Seção 4.1 (pp. 16–17) | Enfoca o modelo copilot assistivo (HITL); não formaliza taxonomia de autonomia agêntica plena. |
| P83 | Ismail et al. | RQ2 | Respondida Plenamente | T (1.0) | Seção 3.1–3.4 (pp. 11–16) | Arquitetura RAG com base vetorial tripartite (Qdrant), extração one-shot de logs e integração SIEM Wazuh. |
| P83 | Ismail et al. | RQ3 | Respondida Plenamente | T (1.0) | Seção 4.2–4.3 (pp. 18–21) | Evidência empírica com 12 cenários Atomic Red Team avaliados via BERTScore (P, R, F1) e Cosine Similarity. |
| P83 | Ismail et al. | RQ4 | Parcialmente Respondida | P (0.5) | Seção 2.8 (pp. 10–11); Seção 5 (pp. 21–22) | Analisa variabilidade e alucinações técnicas dos modelos, mas não discute privacidade e governança de dados. |
| P83 | Ismail et al. | RQ5 | Respondida Plenamente | T (1.0) | Seção 5 (pp. 21–22) | Identifica a transição de Copilot para automação via SOAR, active learning e fine-tuning com dados de domínio. |
| **P83** | **SCORE_RQ** | — | — | **4.0 / 5.0** | — | **Alta aderência ao corpus da RSL, cobrindo o estado da arte de Copilots em SOC/SIEM.** |

---

#### Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 (Objetivos) | QA2 (Replicabilidade) | QA3 (Evidências) | QA4 (Conclusões) | SCORE_QA | Banda de Qualidade |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P83** | Experimental (Simulação com Emulador Red Team) | 1.0 (Y) | 1.0 (Y) | 1.0 (Y) | 0.5 (P) | **3.5 / 4.0** | **Alta ($\ge$ 3.0)** |

---

### 6. Parecer Final do Revisor

* **Síntese de Aderência:** O artigo propõe o SERC (*Security Event Response Copilot*), uma solução prática e arquiteturalmente rica que estende o SIEM de código aberto Wazuh com recursos de RAG orientados por três coleções de conhecimento estruturado (MITRE ATT&CK, NIST CSF 2.0 e Guias de IR). A metodologia empírica avalia dois modelos fundacionais (Pixtral-Large-Instruct e OpenAI GPT-4o) em 12 cenários concretos de ataque executados com Atomic Red Team, gerando dados comparativos de precisão, revocação e similaridade semântica. O estudo contribui expressivamente para o entendimento de como arquiteturas RAG sustentam copilots em ambientes de monitoramento de segurança operacional.
* **Recomendação Final:** **INCLUIR**
  * *Justificativa:* Qualidade metodológica comprovadamente alta (SCORE_QA = 3.5), excelente pontuação de alinhamento com as RQs (SCORE_RQ = 4.0/5.0) e relevância prática incontestável para o corpus da RSL na intersecção entre SIEM aberto, RAG e resposta guiada a incidentes.
* **Pendências de Verificação Externa:**
  * `[VERIFICAR]` Contagem consolidada de citações nas bases indexadoras (Scopus, Google Scholar, Web of Science).
  * `[VERIFICAR]` Confirmação do quartil SJR na base Scimago Journal Rank para a publicação em *Sensors*.
  * `[VERIFICAR]` Confirmação do estrato Qualis CAPES aplicável ao veículo na Plataforma Sucupira.