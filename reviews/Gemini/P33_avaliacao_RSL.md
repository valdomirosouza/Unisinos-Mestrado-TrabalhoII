# Avaliação Sistemática de Estudo Secundário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P33
- **Título:** *A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense*
- **Autores:** Ibrahim Adabara; Bashir Olaniyi Sadiq; Aliyu Nuhu Shuaibu; Yale Ibarahim Danjuma; Venkateswarlu Maninti
- **Periódico/Conferência:** *F1000Research*, Vol. 14, Artigo 843, pp. 1–30 (Publicado em 1 de setembro de 2025; *version 1; peer review: 2 approved*)
- **DOI:** `10.12688/f1000research.169337.1`
- **Arquivo avaliado:** `P33-A2-64b5f019-bc3d-42da-870b-8f7434e7057c_f1000res169337.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Estudo secundário — Revisão Narrativa da Literatura (*Narrative Review*), sintetizando literatura acadêmica, industrial e de políticas públicas publicada entre 2005 e 2025 (135 referências bibliográficas e repositório suplementar no *Figshare* `10.6084/m9.figshare.29966266.v1`).
- **Foco técnico:** Síntese multidisciplinar de *Agentic Artificial Intelligence* (AAI) aplicada à cibersegurança ao longo de três pilares temáticos: (1) Autonomia Cognitiva (padrões de projeto, níveis de autonomia e colaboração humano-agente); (2) Governança Ética (alinhamento com *NIST AI RMF*, *EU AI Act*, *ISO/IEC 42001:2023* e mitigação de riscos de uso duplo); e (3) Defesa Resiliente à Computação Quântica (criptografia pós-quântica PQC, QKD e aprendizado federado *quantum-safe*).

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Totalmente atendido. O artigo foca diretamente em *Agentic AI* para operações de defesa cibernética, detecção de ameaças, triagem em SOCs (*human-in-the-loop*) e resposta autônoma a incidentes.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado em setembro de 2025 na plataforma *F1000Research* com 2 pareceres de revisão por pares aprovados em outubro de 2025 inclusos nas pp. 26–29 do PDF).
  - *IC3 (Rigor técnico/metodológico):* Atendido com ressalvas inerentes ao formato de revisão narrativa (possui questões de pesquisa explícitas, critérios de inclusão/exclusão, fluxo de 5 etapas e dados suplementares abertos, mas sem diagrama PRISMA quantitativo).
- **Critérios de Exclusão (EC):** Não incide em critério de exclusão.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P33 | F1000Research | 2025 | [VERIFICAR] | Q1 [VERIFICAR] | A2 [VERIFICAR] | Revisão Narrativa da Literatura (Secundário) | `10.12688/f1000research.169337.1` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF referentes ao próprio artigo e devem ser verificados nas fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P33 | A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense | **RQ1** (Contexto e Definições) | Respondida Plenamente | **T** (1.0) | Seções 1.1, 1.3 e 1.8 (pp. 3, 7); Seção 3.1 (pp. 9–10); Seção 3.5, Figura 6 (pp. 12–13); Seção 4, Tabela 2 (pp. 13–14) | **(a) Definição de autonomia:** Define formalmente *Agentic AI* e *Cognitive Autonomy* (p. 7) e classifica sistemas em níveis de autonomia (*Low*, *Medium*, *Medium-High*, *High*) segundo as taxonomias de Händler [75] e Cihon et al. [76] (p. 12), detalhando 6 arquétipos na Tabela 2 (p. 14): *Reactive*, *Proactive Goal-Seeking*, *Learning-Based*, *Human-in-the-Loop* (assistentes de triagem em SOCs que escalonam a humanos sob incerteza), *Federated Agent Networks* e *Reflexive Cognitive Loops*. **(b) Características centrais:** Memória persistente, autorreflexão, consciência de contexto, colaboração multiagente e governança embarcada (pp. 7, 9–10). **(c) Modelo decisório:** Aborda integração híbrida neuro-simbólica (DRL + LLMs + regras), o ciclo decisório explicável **TriQPAN** (*Trigger, Query, Process, Action, Notify* [84], p. 14), padrões de *human-agent teaming* (delegação e pareamento associativo [85]) e a matriz *Perception–Reasoning–Action–Adaptation–Oversight* (Figura 10, p. 21). |
| P33 | A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seção 3.5 (p. 12); Seção 4, Tabelas 2–5 (pp. 13–17); Seção 5.4 (p. 19); Seção 5.10, Figura 10 (p. 21) | **(a) Tipo de arquitetura:** Mapeia arquiteturas modulares em camadas de percepção/raciocínio/ação (*boxology* para atores híbridos [81–83]), planos de controle escaláveis (*Control Plane as a Tool* [103]), redes multiagentes federadas e arquiteturas descentralizadas em *blockchain* (pp. 12–14, 17). **(b) Ferramentas/frameworks:** Destaca protocolos de comunicação e contexto agêntico como o **Google Agent2Agent (A2A)** e o **Model Context Protocol (MCP)** [100, 114] (pp. 17, 19), o framework de risco **MAESTRO** para A2A [114] (p. 19), redes **DAGN** com *Tokenized Power Control* [78], **LOKA Protocol** [79] (p. 12) e algoritmos pós-quânticos (*Kyber*, *McEliece*, PQC baseado em reticulados, pp. 16–17). **(c) Capacidades avançadas:** Integração com *digital twins* para testes preemptivos (p. 21), aprendizado federado *quantum-safe*, distribuição quântica de chaves (QKD, Tabela 4, p. 16) e *honeypots* autorreguláveis com *loops* reflexivos (Tabela 2). |
| P33 | A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense | **RQ3** (Benefícios e Evidências) | Parcialmente Respondida | **P** (0.5) | Seções 3.2 e 3.3 (pp. 10–11); Seção 4, estudos de caso (pp. 14, 17) | **(a) Benefícios qualitativos:** Evolução da defesa estática reativa para mitigação proativa e contínua, operação autônoma de agentes de defesa (*AICAs* [3]) quando a comunicação com operadores humanos está degradada (p. 3), otimização da carga cognitiva em SOCs (p. 14) e resiliência pós-quântica. **(b) Benefícios quantitativos:** Por ser uma revisão narrativa conceitual, apresenta escassas métricas operacionais, limitando-se a indicadores bibliométricos (>1.200 artigos e >30.000 citações em 2023 [68], pp. 11–12) e dois breves relatos de caso: um sistema híbrido DRL+LLM que superou defesas estáticas contra *red-team* simulado [80] (p. 14) e um piloto *multi-cloud* com *Kyber*/*McEliece* PQC e gestão de chaves por IA que atingiu latência de criptografia `< 4 ms` e vulnerabilidade zero ao algoritmo de Shor [97] (p. 17). **(c) Nível de evidência:** Revisão narrativa secundária sem meta-análise quantitativa. |
| P33 | A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense | **RQ4** (Desafios e Ética) | Respondida Plenamente | **T** (1.0) | Seção 1.4, Figuras 1–2 (pp. 3–5); Seção 4 RQ2 e RQ4, Tabelas 3 e 5, Figura 8 (pp. 14–17); Seção 5.5 (p. 19) | **(a) Desafios técnicos:** Analisa ataques de *adversarial AI* (envenenamento de dados, evasão, *deepfakes*, inversão/extração de modelos), manipulação gradual de aprendizado *online*/*few-shot*, ameaça quântica (*"harvest now, decrypt later"* via algoritmo de Shor contra credenciais geridas por agentes, p. 4) e barreiras de integração com legados e custos (Tabela 5, p. 17). **(b) Desafios éticos/governança:** Examina profundamente o dilema de uso duplo (*dual-use*, Figura 2, pp. 4–5 — agentes defensivos ou de *self-healing* convertidos em armas ofensivas/infiltração), falta de atribuição, opacidade "caixa-preta", defasagem regulatória (*regulatory lag*) e assimetria geopolítica. **(c) Mecanismos de governança:** Compara 6 frameworks globais na Tabela 3 e Figura 8 (p. 15) — **NIST AI RMF**, **EU AI Act**, **ISO/IEC 42001:2023**, **IEEE 7000 Series**, **OECD AI Principles** e **UNESCO AI Ethics** —, além de salvaguardas como **DAGN**, **LOKA Protocol**, **MAESTRO** e *human override* (pp. 12, 19, 21). |
| P33 | A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção 1.5 (pp. 5–6); Seção 5.3, Tabela 6 (pp. 18–19); Seção 5.7 (p. 20) | Sistematiza 6 lacunas e questões futuras na Tabela 6 (p. 19): (1) formalização e *benchmarking* de autonomia cognitiva em agentes de cibersegurança; (2) ferramentas práticas de governança contra uso duplo (*dual-use*); (3) aprendizado federado *quantum-safe*; (4) estratégias de design para calibração de confiança humano-agente em agentes semiautônomos; (5) arquiteturas agênticas auditáveis e juridicamente interpretáveis; e (6) transferência de lições de aviação e saúde. Na Seção 5.7 (p. 20), propõe um *roadmap* em 3 horizontes: curto prazo (1–3 anos: XAI e robustez adversarial), médio prazo (3–7 anos: aprendizado federado com PQC e *blockchain*) e longo prazo (7+ anos: IA neuro-simbólica e *Quantum Multi-Agent Reinforcement Learning* — QMARL). |
| **P33** | **SCORE_RQ Total** | — | **4.5 / 5.0** | — | — | Atende plenamente RQ1 (1.0), RQ2 (1.0), RQ4 (1.0) e RQ5 (1.0), e parcialmente RQ3 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P33 | Revisão Narrativa da Literatura (Estudo Secundário) | Y (1.0) | P (0.5) | P (0.5) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Clareza e relevância dos objetivos / critérios de inclusão (Y = 1.0):** Define com precisão o objetivo da revisão, delimita claramente o escopo conceitual (Seções 1.6–1.8, pp. 6–7), formula quatro questões de pesquisa explícitas (RQ1–RQ4, p. 6) e estabelece critérios de inclusão e exclusão na Seção 2.4 (p. 8).
- **QA2 — Adequação da estratégia de busca e desenho metodológico (P = 0.5):** Informa as bases de busca (*IEEE Xplore*, *Scopus*, *Web of Science*, *ACM Digital Library* e literatura cinzenta), o período (2005–2025), o fluxo em 5 etapas (*Identify, Screen, Select, Classify, Synthesize*, Figura 3, p. 9) e disponibiliza *dataset* suplementar no *Figshare* (`10.6084/m9.figshare.29966266.v1`, p. 22). Contudo, por adotar um desenho de revisão narrativa iterativa (auxiliada por ferramentas de IA generativa para agrupamento temático, p. 8), não reporta o número exato de estudos recuperados, filtrados ou incluídos no texto principal, nem aplica avaliação formal de qualidade metodológica individual aos estudos primários (limitação apontada também nos relatórios de revisão por pares aberta nas pp. 27 e 29).
- **QA3 — Qualidade da avaliação / síntese dos estudos e evidências (P = 0.5):** Integra 135 referências em taxonomias e quadros analíticos bem estruturados (Tabelas 1–6 e Figuras 1–10), destacando-se na síntese conceitual de padrões de arquitetura (Tabela 2), frameworks regulatórios (Tabela 3) e estratégias pós-quânticas (Tabela 4). Todavia, a síntese de evidências empíricas no texto é superficial (a Tabela 1 na p. 10 lista apenas 5 estudos exemplares sem métricas quantitativas comparativas).
- **QA4 — Consistência entre evidências coletadas e conclusões (Y = 1.0):** As conclusões e o roteiro de pesquisa futura respondem coerentemente às quatro RQs propostas, e os autores discutem com transparência as limitações metodológicas do estudo em duas seções dedicadas (Seção 2.7 na p. 9 e Seção 5.8 na p. 20), reconhecendo riscos de viés de seleção/publicação, subjetividade da síntese narrativa e rápida obsolescência.

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
Esta revisão narrativa publicada na *F1000Research* sintetiza 135 fontes (2005–2025) sobre *Agentic AI* em cibersegurança estruturada em três pilares: Autonomia Cognitiva, Governança Ética e Defesa Resiliente à Computação Quântica. O artigo oferece contribuições conceituais de alto valor para a RSL, incluindo a classificação de seis padrões de projeto por nível de autonomia (Tabela 2, como *Human-in-the-Loop* para triagem em SOCs e *Reflexive Cognitive Loops*), o padrão de ciclo explicável *TriQPAN*, protocolos de interoperabilidade agêntica (*Google A2A*, *MCP*, *MAESTRO*, *DAGN*, *LOKA Protocol*) e o mapeamento comparativo de seis normas globais de governança (*NIST AI RMF*, *EU AI Act*, *ISO/IEC 42001:2023*, *IEEE 7000*, *OECD*, *UNESCO*).

### Recomendação
**INCLUIR COM RESSALVAS** — O estudo apresenta altíssima aderência temática às questões de pesquisa da RSL (`SCORE_RQ = 4.5/5.0`, especialmente para RQ1, RQ2, RQ4 e RQ5) e qualidade global Alta (`SCORE_QA = 3.0/4.0`). Recomenda-se sua inclusão como referência secundária de fundamentação teórica, arquitetural e de governança ética/regulatória, com a ressalva de tratar-se de uma revisão narrativa sem extração quantitativa detalhada de experimentos de resposta a incidentes.

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *F1000Research* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
