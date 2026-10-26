# Avaliação Sistemática de Literatura — Estudo P24

**Artigo avaliado:** *AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0*  
**Autores:** Francesco Piccialli; Diletta Chiaro; Sundas Sarwar; Donato Cerciello; Pian Qi; Valeria Mele  
**Arquivo fonte:** `P24-A1-1-s2.0-S0957417425020238-main.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — 2025 (recebido em dez. 2024, aceito em maio de 2025, disponível online em 2 de junho de 2025, p. 1).
- **Publicação ≠ NULL (veículo identificável):** Sim — *Expert Systems With Applications*, Volume 291, Artigo 128404, pp. 1–18.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science, ScienceDirect ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *Expert Systems With Applications*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P24 | Expert Systems With Applications (Vol. 291, Art. 128404, pp. 1–18) | 2025 | `[VERIFICAR]` (base indexadora: Scopus / WoS / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Revisão Sistemática da Literatura / *Survey* (*Review* seguindo PRISMA com 66 artigos) | `10.1016/j.eswa.2025.128404` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P24 | AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0 | RQ1 | Respondida Plenamente | T (1.0) | Seção 3, 3.1, 3.2 e 3.3 (pp. 3–7); Figuras 2, 3 e 4 (pp. 4, 5, 7); Tabelas 2 e 3 (pp. 6–7); Seção 6.2 e 6.3 (pp. 14–15) | **(a) Autonomy definition:** Diferencia sistemas não-autônomos (baseados em regras fixas e supervisão humana em ambientes controlados) de sistemas autônomos (orientados a metas e adaptativos em ambientes abertos), projetando a evolução da automação (Indústria 4.0) para colaboração humano-cêntrica (Indústria 5.0) e auto-regulação descentralizada (Indústria 6.0). **(b) Core characteristics:** Organiza a arquitetura interna em módulos de *Perception* (fusão multimodal VLM/LLM), *Cognition* (memória, base de conhecimento e tomada de decisão) e *Action* (execução e expansão dinâmica do espaço de ações com ferramentas), aliados a *data flywheel* e aprendizado *zero-shot/few-shot/fine-tuning*. **(c) Decision-making model:** Compara cinco paradigmas (Simbólico, Políticas em Grafos/KG, *Behaviour Trees*, Probabilístico/Bayesiano/MDP e LLMs Transformer, além de DRL/MARL) quanto a interpretabilidade, escalabilidade e adaptabilidade (Tabela 2), integrando supervisão *human-in-the-loop* e *interruptibility* (Figura 4). |
| P24 | AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0 | RQ2 | Parcialmente Respondida | P (0.5) | Seção 3.1 a 3.3 (pp. 4–7); Seção 4 e 5 (pp. 7–8); Figuras 2, 3, 4 e 5 (pp. 4, 5, 7, 8) | **(a) Architecture type:** Apresenta diagramas arquiteturais conceituais de alto nível, incluindo o ciclo de vida do agente (Figura 4) e uma arquitetura de manutenção preditiva na Indústria 4.0 que integra consultas NLP/SQL, *Code Executor* (Python/C), modelos preditivos de ML e GenAI/RAG (Figura 5). **(b) Tools/frameworks:** Menciona de forma panorâmica *Docker*, *Kubernetes*, *SDN/NFV*, protocolos (*gRPC*, *MQTT*, *QUIC*), modelos (*GPT-3/4*, *Llama*, *Gemini*, *DeepSeek*) e frameworks (*JADE*, *crewAI*). **(c) Advanced capabilities:** Aborda conceitualmente migração com *service discovery* e desligamento controlado (*interruptibility*, Tabela 3), mas não aprofunda mecanismos de engenharia em produção para resposta a incidentes. |
| P24 | AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0 | RQ3 | Parcialmente Respondida | P (0.5) | Seção 2 (p. 3); Seção 5 e Subseções 5.1 a 5.9 (pp. 8–14); Tabela 4 (p. 10); Figura 6 (p. 9) | **(a) Qualitative benefits:** Sintetiza benefícios qualitativos em 9 setores (Transporte, Energia, Saúde, Redes, Defesa, Jogos, Governança, Marketing e E-Learning), destacando detecção precoce de falhas, estimativa de vida útil remanescente (RUL) em manutenção preditiva e otimização de QoS em redes 5G/6G. **(b) Quantitative benefits / metrics:** Por ser uma revisão secundária ampla, reporta apenas métricas pontuais da literatura revisada (ex.: 94%–99% de acurácia no roteamento de consultas urbanas reduzindo decisões de dias para horas, p. 9; 25% de redução de energia e +7% de qualidade em tratamento de efluentes via MARL, p. 9), sem métricas específicas de resposta a incidentes de TI/cibersegurança. **(c) Evidence level:** Revisão sistemática secundária (PRISMA) cobrindo 66 artigos (2014–2025). |
| P24 | AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0 | RQ4 | Respondida Plenamente | T (1.0) | Seção 3 e 3.3 (pp. 4, 6–7); Tabela 3 e Figura 4 (p. 7); Seção 5.7 (pp. 12–13); Seção 6.1 e 6.2 (pp. 14–15) | **(a) Technical challenges:** Aponta fragmentação e ruído em dados industriais, sobrecarga de comunicação e convergência em *Edge AI/Federated Learning*, baixa transferência de simulações para o mundo real, falhas de coordenação multiagente, conduta adversarial e *input spoofing*. **(b) Ethical/governance challenges:** Analisa profundamente *automation bias*, distância psicológica que reduz a responsabilização moral, ausência de *moral grounding* em agentes puramente estatísticos, riscos de manipulação/engano (*deception*) por LLMs e tensões de privacidade/direito ao esquecimento. **(c) Governance mechanisms:** Detalha supervisão *human-in-the-loop*, *interruptibility* (parada segura com *fallback*), *activity logging* e visibilidade, simulação preditiva de consequências, avaliação sociotécnica em três níveis (design, organização e auditoria externa) e "transparência extrema". |
| P24 | AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0 | RQ5 | Respondida Plenamente | T (1.0) | Seção 5.4 (p. 11); Seção 6.1, 6.2 e 6.3 (pp. 14–15) | Delineia lacunas abertas e um *blueprint* para Indústria 5.0/6.0: (1) protocolos de negociação e consenso descentralizado para enxames multiagentes na borda; (2) inferência de intenções humanas latentes e raciocínio empático multimodal para prevenção proativa de acidentes (ex.: detectar tentativa humana de burlar trava de segurança); (3) ecossistemas industriais *self-healing* descentralizados baseados em *edge intelligence*, *blockchain* e aprendizado federado; (4) integração neuro-simbólica e MARL explicável; e (5) criação de *benchmarks* padronizados de confiabilidade e robustez em redes 5G/6G. |
| **P24** | **TOTAL (SCORE_RQ)** | — | **4.0 / 5.0** | **3T, 2P** | — | Forte contribuição conceitual em taxonomia de autonomia/ciclo de vida (RQ1), governança/ética/interrompibilidade (RQ4) e visão de futuro *self-healing* (RQ5); cobertura tangencial em arquitetura prática e métricas de IR (RQ2, RQ3). |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P24 | Revisão Sistemática da Literatura / *Survey* (PRISMA) | P (0.5) | Y (1.0) | P (0.5) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (P = 0.5):** O artigo define claramente suas cinco questões de pesquisa (Seção 1.1, p. 2) voltadas a mapear o panorama de *AgentAI* na Indústria 4.0. Entretanto, em relação ao escopo específico de *Resposta a Incidentes em TI/Cibersegurança*, o objetivo do artigo é genérico e multissetorial (abrangendo jogos, ensino de dança, marketing, saúde e energia), tocando apenas perifericamente em manutenção preditiva industrial e gerência de redes.
- **QA2 — Metodologia Replicável (Y = 1.0):** A coleta de literatura segue as diretrizes PRISMA (Seção 2, Figura 1, p. 3), especificando as quatro bases consultadas (*Scopus*, *Web of Science*, *IEEE Xplore*, *ScienceDirect*), a *query* booleana exata (`TITLE-ABS-KEY: ("AgentAI" OR "AgenticAI" OR "Agentic AI")`), os quantitativos em cada fase de filtragem ($255 \to 144 \to 66$ estudos incluídos) e um repositório público no GitHub (`https://github.com/MODAL-UNINA/AgenAI-literature-search`) contendo as planilhas de triagem.
- **QA3 — Base de Evidências Sólidas (P = 0.5):** Embora revise 66 artigos, o corpus selecionado mistura estudos recentes de LLMs com trabalhos antigos (2014–2021) de agentes clássicos (algoritmos genéticos, lógica *fuzzy*, *Markov models* em jogos de tabuleiro), e a síntese apresentada é essencialmente narrativa e descritiva, carecendo de comparação quantitativa sistemática de desempenho entre os estudos primários.
- **QA4 — Conclusões Coerentes (Y = 1.0):** As discussões e conclusões (Seções 6 e 7, pp. 14–15) são bem fundamentadas na literatura revisada, oferecendo uma análise crítica consistente sobre desafios éticos, governança, *interruptibility* e a transição para sistemas *self-healing* nas Indústrias 5.0 e 6.0.

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P24 é uma revisão sistemática (PRISMA) de amplo espectro sobre agentes autônomos (*AgentAI*) na Indústria 4.0, 5.0 e 6.0. Embora não seja focado especificamente em resposta a incidentes de cibersegurança ou operações de TI (AIOps), oferece insumos conceituais valiosos para a RSL no que tange à taxonomia de paradigmas agênticos e ciclo de vida (RQ1), governança ética, responsabilidade, *human-in-the-loop* e mecanismos de parada segura/*interruptibility* (RQ4), além de projetar infraestruturas industriais autocurativas (*self-healing*) descentralizadas (RQ5), atingindo `SCORE_RQ = 4.0/5.0` e `SCORE_QA = 3.0/4.0` (Banda Alta).
- **Recomendação:** **INCLUIR COM RESSALVAS** — Recomenda-se a inclusão como referência secundária/conceitual de suporte para fundamentar as seções de fundamentação teórica (ciclo de vida agêntico, módulos percepção-cognição-ação), governança ética (*interruptibility*, *accountability*, *automation bias*) e direções futuras (Indústria 5.0/6.0), registrando a ressalva de que se trata de um *survey* secundário multissetorial sem experimentos primários em resposta a incidentes de TI.
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science, ScienceDirect ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *Expert Systems With Applications* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
