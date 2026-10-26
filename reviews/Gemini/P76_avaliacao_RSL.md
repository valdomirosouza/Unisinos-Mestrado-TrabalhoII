# Avaliação RSL - Estudo P76

**Artigo:** Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence  
**Autores:** Ismail, Rahmat Kurnia, Zilmas Arjuna Brata, Ghitha Afina Nelistiani, Shinwook Heo, Hyeongon Kim, Howon Kim  
**Periódico:** *Information* (MDPI), 2025, 16(5), 365  
**DOI:** [10.3390/info16050365](https://doi.org/10.3390/info16050365)  
**RSL:** "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura" (Ciclo 2)  
**Metodologia Base:** Kitchenham (2009) / Critérios DARE (QA1–QA4)

---

## 1. Especificação do Prompt e Protocolo de Avaliação

```markdown
# PAPEL
Aja como pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por um professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, seguindo rigorosamente as diretrizes de Kitchenham (2009) no paper/artigo "Systematic literature reviews in software engineering – A systematic literature review". Sua avaliação de qualidade deve espelhar a lógica dos critérios DARE (QA1–QA4) descritos naquele trabalho.

# CONTEXTO DA RSL
Esta avaliação integra o artigo "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura", agora no ciclo 2 de atualização. O corpus prévio cobre P01–P40 (33 estudos incluídos). Você avaliará UM novo estudo candidato do ciclo 2 por vez, atribuindo o ID sequencial informado (a partir de P41), de modo que os resultados possam ser anexados diretamente às Tabelas 3, 5 e 7 da RSL existente.

# INSUMOS
- ID: P76
- Artigo: Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence
- Arquivo: P76_Toward_Robust_Security_Orchestration_and_Automated_Response_in_Security_Operations_Centers_with_a_Hyper-Automation_Approach_Using_Agentic_AI.pdf
- qualis: A2 (derivado do percentil Scopus 79.0%, regra CAPES 2025-2028)
- sjr_quartile: Q2
- ressalvas_triagem: aprovado na triagem; núcleo agêntico × SOC/SOAR; único candidato com MTTR citado (vs. literatura)

# REGRAS INVIOLÁVEIS (ANTIFABRICAÇÃO)
1. Avalie EXCLUSIVAMENTE o conteúdo presente no PDF anexado. Não use conhecimento externo nem suposições sobre o que o artigo "provavelmente" contém.
2. NÃO invente métricas, números de página, citações, DOI, quartil SJR, estrato Qualis ou contagem de citações.
3. Dados NÃO verificáveis no PDF (quartil SJR, estrato Qualis CAPES, número de citações) devem ser marcados como "[VERIFICAR]". Indique a fonte onde verificar (SJR: Scimago Journal Rank; Qualis: Plataforma Sucupira / Qualis CAPES; Citações: base indexadora).
4. Toda classificação (T/P/N e Y/P/N) deve ser ancorada em evidência concreta do texto (seção, figura, tabela ou página). Sem evidência localizável, a classificação é N.

# ETAPAS DO PROTOCOLO
- ETAPA 0 — Extração Bibliométrica (Tabela 3 da RSL)
- ETAPA 1 — Triagem de Elegibilidade (PRISMA / critérios RSL)
- ETAPA 2 — Extração e Classificação das RQs (RQ1 a RQ5; Tabela 5 da RSL)
- ETAPA 3 — Avaliação de Qualidade QA (QA1 a QA4; Tabela 7 da RSL)
- Parecer final do revisor fundamentado e com recomendações.
```

---

## 2. Etapa 0 — Extração Bibliométrica

* **ID do Estudo:** P76
* **Título do Artigo:** Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence
* **Autores:** Ismail, Rahmat Kurnia, Zilmas Arjuna Brata, Ghitha Afina Nelistiani, Shinwook Heo, Hyeongon Kim, Howon Kim
* **Afiliações Principais:** School of Computer Science and Engineering, Pusan National University & SmartM2M Co., Ltd. (República da Coreia)
* **Periódico:** *Information* (MDPI)
* **Ano:** 2025 (Publicado online em 29 de abril de 2025)
* **Volume / Edição / Artigo:** Vol. 16, Fasc. 5, Artigo 365
* **Tipo de Estudo:** Estudo Experimental / Prova de Conceito Arquitetural com Validação Piloto
* **DOI:** [10.3390/info16050365](https://doi.org/10.3390/info16050365)
* **Citações:** [VERIFICAR] (Base Scopus, Google Scholar ou Web of Science)
* **SJR (Quartil):** [VERIFICAR] (Classificação Scimago Journal Rank; insumo indica Q2)
* **Qualis CAPES:** [VERIFICAR] (Classificação Plataforma Sucupira; percentil Scopus 79.0% mapeado para A2 na regra 2025–2028)

---

## 3. Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério de Inclusão / Exclusão | Verificação no Texto do Artigo | Status |
| :--- | :--- | :---: |
| **Ano $\ge$ 2020** | Publicado em 29 de abril de 2025 (Page 1) | **Atendido** |
| **Publicação $\ne$ NULL** | Periódico indexado *Information* (MDPI, ISSN 2078-2489) | **Atendido** |
| **Citações $\ge$ 1** | Artigo publicado em 2025; citações em bases indexadoras | **[VERIFICAR]** |
| **SJR Q1–Q2** | Insumo indica Q2; confirmação formal no portal Scimago | **[VERIFICAR]** |
| **Qualis A1–A2** | Insumo indica A2 (percentil 79.0%); confirmação no Qualis/Sucupira | **[VERIFICAR]** |

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (aprovado condicionalmente na triagem com base nos insumos bibliométricos; apto para extração completa de conteúdo).

---

## 4. Etapa 2 — Avaliação e Classificação das Questões de Pesquisa (RQs)

### RQ1 — Context Definitions
* **Veredito:** Respondida Plenamente (**T = 1.0**)
* **Subdimensões:**
  * **a) Definição de Autonomia:** Define a IA agêntica como sistemas que operam de forma autônoma na análise, decisão e execução de respostas a incidentes com mínima supervisão humana direta, promovendo uma transição de fluxos reativos e estáticos para mitigação proativa (Seções 1, 2.3 e 3.2).
  * **b) Características Principais:** Apresenta raciocínio multi-etapas (*multi-step reasoning* com Chain-of-Thought), decomposição hierárquica de tarefas complexas, memória vetorial e coordenação com ferramentas externas (Seções 2.5.2, 3.2.2; Figuras 2 e 5).
  * **c) Modelo de Tomada de Decisão:** Ciclo fundamentado em percepção do ambiente (*Sense*), planejamento (*Plan*), roteamento inteligente entre LLMs especializados (*Router*), execução de comandos e validação com parada controlada por intervenção humana (Seções 3.1, 3.2.1, 3.4.4; Figuras 2, 4 e 6).
* **Evidência:** Seção 1 (p. 2); Seção 2.3 (p. 6); Seções 3.1–3.2 (p. 10–16); Figuras 2 e 4 (p. 9, 17).

---

### RQ2 — Engineering Architecture
* **Veredito:** Respondida Plenamente (**T = 1.0**)
* **Subdimensões:**
  * **a) Tipo de Arquitetura:** Sistema multi-agente orquestrado por grafos de transição de estados determinísticos e modulares (Seções 3.2.2 e 3.4; Algoritmo 2).
  * **b) Ferramentas e Frameworks:** Emprego de arquitetura multi-modelo integrando `meta-llama/Llama-3.3-70B-Instruct` (para políticas e abstração) e `deepseek-ai/DeepSeek-R1-Distill-Llama-70B` (para raciocínio analítico e geração de código de resposta). Integração com Wazuh SIEM, base vetorial (Vector DB), cliente WebSocket persistente implementado em Go (Gorilla WebSocket) para shell remoto e utilitários de sistema (`iptables`, `Fail2Ban`, `AIDE`, `auditd`) (Seções 3.2.2, 3.4, 4.1; Algoritmo 1).
  * **c) Capacidades Avançadas:** Memória contextual persistente via embeddings e motor de similaridade de incidentes (*incident similarity engine*), síntese dinâmica de scripts executáveis sem depender de playbooks rígidos pré-compilados, e fallback estruturado para nós de erro e validação humana (Seções 3.3, 3.4.2–3.4.4; Algoritmo 2).
* **Evidência:** Seção 3.2.2 (p. 17–22); Seção 3.4 (p. 22–24); Algoritmo 1 (p. 21); Algoritmo 2 (p. 23); Figuras 5 e 6 (p. 18, 19).

---

### RQ3 — Evidence Benefits
* **Veredito:** Respondida Plenamente (**T = 1.0**)
* **Subdimensões:**
  * **a) Benefícios Qualitativos:** Redução substancial da fadiga e carga cognitiva do analista de segurança por meio de enriquecimento contextual automático de logs; mitigação da rigidez de playbooks no-code/low-code e adaptação dinâmica à infraestrutura atacada (Seções 1, 2.2, 4.2 e 5).
  * **b) Benefícios Quantitativos e Métricas:** Coleta e documentação inédita de Mean Time to Remediate (MTTR) decomposto em três fases: análise ($\approx$ 1 min 30 s), atualização de comandos ($\approx$ 1 min) e compilação ($\approx$ 1 min 30 s), confrontados com dados reportados por Freitas et al. (2024) para o Microsoft Copilot for Security (Seção 4.6). Demonstra também a otimização de fluxo: redução de um playbook tradicional de 38 passos (Cortex XSOAR) para 10 passos consolidados executados pelo agente (Seção 4.3; Tabela 2).
  * **c) Nível de Evidência:** Validação empírica em testbed experimental virtualizado (Ubuntu 22.04 LTS sobre VirtualBox com Wazuh SIEM integrado), monitorando ataques reais de força bruta em autenticação SSH PAM e calculando o Risco Relativo residual a cada intervenção (Seções 4.1, 4.4, 4.6).
* **Evidência:** Seção 4.3 (p. 26–28); Seção 4.4 (p. 28–29); Seção 4.6 (p. 30); Tabela 2 (p. 27–28); Figura 9 (p. 29).

---

### RQ4 — Challenges & Ethics
* **Veredito:** Respondida Plenamente (**T = 1.0**)
* **Subdimensões:**
  * **a) Desafios Técnicos:** Risco de alucinação e geração de comandos incorretos; dependência de credenciais administrativas elevadas no endpoint alvo, evidenciada por falha real de execução documentada no log (`Error: sudo: a password is required`) ao tentar instalar pacotes ou rodar regras de firewall sem sessão interativa; dificuldades de integração em sistemas agentless ou tecnologias operacionais (OT) (Seções 4.5 e 5; Tabela 3; Figura 10).
  * **b) Desafios Éticos e de Governança:** Falta de transparência/explicabilidade no raciocínio profundo de modelos fundacionais; riscos de conformidade regulatória (PCI DSS, HIPAA, GDPR) na manipulação de logs sensíveis; risco de indisponibilidade ou efeitos colaterais de contenção não autorizada em produção (Seções 2.5.2, 3.1.2, 5 e 6).
  * **c) Mecanismos de Governança:** Implementação formal de nó *Human-in-the-Loop* (`human_interrupt_node`) como barreira de segurança prévia à execução de comandos; adoção de cálculo de Risco Relativo incremental via Quantitative Risk Assessment ($R = (L \times I) \times (1 - E)$) para balizar a relação custo-benefício de cada ação defensiva (Seções 3.1.2, 3.2.1, 3.4.4; Figuras 3 e 4).
* **Evidência:** Seção 3.1.2 (p. 14–15); Seção 4.5 (p. 29–30); Seção 5 (p. 30–31); Tabela 3 (p. 30); Figura 10 (p. 29).

---

### RQ5 — Research Gaps
* **Veredito:** Respondida Plenamente (**T = 1.0**)
* **Subdimensões Identificadas:**
  * Necessidade de padronização de benchmarks públicos e conjuntos de dados abertos para medição rigorosa e reproduzível de MTTR entre plataformas de SOAR agêntico e comerciais de mercado (Seção 4.6).
  * Ampliação da base de validação para além de ataques de brute force em SSH, abrangendo vetores complexos como phishing, movimentação lateral, escalada de privilégios e ransomware (Seção 6).
  * Fortalecimento de técnicas de explicabilidade do raciocínio interno do LLM para elevar a confiança dos analistas de SOC antes da aprovação em esteiras HITL (Seções 5 e 6).
  * Desenvolvimento de estratégias seguras de integração e observabilidade para dispositivos que não suportam a instalação de agentes nativos baseados em WebSocket (dispositivos legados e ambientes de OT) (Seção 5).
* **Evidência:** Seção 4.6 (p. 30); Seção 5 (p. 30–31); Seção 6 (p. 31).

---

## 5. Etapa 3 — Avaliação de Qualidade Metodológica (Critérios DARE / Kitchenham)

* **QA1 — Objetivos Claros:** **1.0 (Y)**  
  O trabalho formula com clareza a problemática da sobrecarga de incidentes e a rigidez dos playbooks estáticos em ambientes no-code/low-code de SOCs, estabelecendo com precisão o objetivo de desenvolver uma arquitetura agêntica de hiper-automação orientada pelo framework IVAM (Investigate, Validate, Active Monitoring).
* **QA2 — Metodologia Replicável:** **1.0 (Y)**  
  A metodologia é documentada detalhadamente, apresentando a infraestrutura utilizada, os LLMs envolvidos (`Llama-3.3-70B-Instruct` e `DeepSeek-R1-Distill-Llama-70B`), a lógica de enriquecimento com MITRE ATT&CK e NIST CSF, o pseudocódigo formal do executor via WebSocket (Algoritmo 1) e o grafo de controle agêntico com nós de decisão (Algoritmo 2).
* **QA3 — Base de Evidências Sólidas:** **0.5 (P)**  
  Embora o estudo forneça validação empírica funcional integrada a um SIEM real (Wazuh) e meça métricas de MTTR e contagem de passos, o experimento pilota limitou-se a um único cenário de ataque controlado (brute force contra SSH Linux) em ambiente virtualizado local (VirtualBox), sem validação concorrente sob carga real de produção ou ataques multifacetados.
* **QA4 — Conclusões Coerentes:** **1.0 (Y)**  
  As conclusões e a discussão são integralmente fundamentadas nos dados observados. Os autores relatam com honestidade científica as limitações do protótipo, incluindo as falhas de execução decorrentes de requisitos de senha do `sudo` e a assimetria metodológica na comparação de MTTR com estudos de plataformas proprietárias.

---

## 6. Tabelas Consolidadas da RSL

### Tabela A — Extração Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P76** | Information (MDPI) | 2025 | [VERIFICAR] | [VERIFICAR] (Q2)* | [VERIFICAR] (A2)* | Estudo Experimental / Prova de Conceito | [10.3390/info16050365](https://doi.org/10.3390/info16050365) |

*\*Status herdado dos insumos de triagem do ciclo 2.*

---

### Tabela B — Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do Revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **P76** | Toward Robust Security Orchestration... | **RQ1** | Respondida Plenamente | **T** | Sec. 1 (p. 2); Sec. 2.3 (p. 6); Sec. 3.2 (p. 15-16); Fig. 2 (p. 9) | Define autonomia agêntica, raciocínio decomposto em múltiplas etapas, memória compartilhada e tomada de decisão contextualizada. |
| **P76** | Toward Robust Security Orchestration... | **RQ2** | Respondida Plenamente | **T** | Sec. 3.2.2 (p. 17-22); Sec. 3.4 (p. 22-24); Algo. 1-2 (p. 21, 23) | Apresenta arquitetura multi-agente e grafos de estado com Llama 3.3, DeepSeek-R1, Vector DB, SIEM Wazuh e cliente WebSocket em Go. |
| **P76** | Toward Robust Security Orchestration... | **RQ3** | Respondida Plenamente | **T** | Sec. 4.3 (p. 26-28); Sec. 4.6 (p. 30); Tab. 2 (p. 27-28); Fig. 9 (p. 29) | Mensura o MTTR empírico por fases (análise, execução, compilação), quantifica redução de passos de playbook (38 $\to$ 10) e avalia alívio cognitivo. |
| **P76** | Toward Robust Security Orchestration... | **RQ4** | Respondida Plenamente | **T** | Sec. 3.1.2 (p. 14-15); Sec. 4.5 (p. 29-30); Sec. 5 (p. 30-31); Tab. 3 (p. 30) | Analisa riscos de alucinação, parada obrigatória em nó Human-in-the-Loop, framework QRA para trade-off de mitigação e falhas de elevação sudo. |
| **P76** | Toward Robust Security Orchestration... | **RQ5** | Respondida Plenamente | **T** | Sec. 4.6 (p. 30); Sec. 5 (p. 30-31); Sec. 6 (p. 31) | Aponta expressamente lacunas em datasets/benchmarks abertos para MTTR, testes com ataques diversos (ransomware/phishing) e limitações em redes OT. |
| **P76** | **SCORE_RQ** | — | — | **5.0 / 5.0** | — | **Cobertura integral de todas as cinco questões de pesquisa da RSL.** |

---

### Tabela C — Avaliação de Qualidade Metodológica (Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda de Qualidade |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P76** | Estudo Experimental / Prova de Conceito | 1.0 (Y) | 1.0 (Y) | 0.5 (P) | 1.0 (Y) | **3.5 / 4.0** | **Alta** ($\ge$ 3.0) |

---

## 7. Parecer Final do Revisor

### Síntese Crítica e Aderência ao Escopo
O artigo candidato **P76** demonstra aderência primária e de altíssima relevância ao escopo da revisão sistemática sobre copilotos e agentes autônomos em resposta a incidentes. O trabalho se diferencia da maior parte da literatura recente por não se limitar a prompts conceituais ou análises teóricas de LLMs; ele implementa e formaliza a engenharia de software de um sistema agêntico completo em SOCs, detalhando o grafo de estados (Algoritmo 2), o protocolo bidirecional de execução remota em shell (Algoritmo 1) e o roteamento entre modelos especializados (`Llama-3.3-70B-Instruct` e `DeepSeek-R1-Distill-Llama-70B`). Destaca-se também como o único estudo do ciclo com levantamento empírico explícito de **MTTR** decomposto em etapas de análise e execução, estabelecendo comparação com benchmarks da literatura.

### Recomendação
* **Veredito:** **INCLUIR** no corpus principal da RSL.
* **Justificativa:** O estudo atingiu pontuação máxima nas questões de pesquisa (**SCORE_RQ = 5.0 / 5.0**) e classificação de qualidade **Alta** (**SCORE_QA = 3.5 / 4.0**). Fornece contribuições robustas para as discussões arquiteturais (RQ2), evidências de tempo e redução de esforço (RQ3), e mecanismos práticos de governança com validação humana e mitigação de risco relativo (RQ4).

### Pendências de Verificação Externa
1. **Contagem de Citações:** Verificar o volume de citações acumuladas nas bases indexadoras formais (Scopus / Google Scholar / Web of Science) na data final de congelamento do Ciclo 2.
2. **Confirmação de Quartil SJR:** Validar no Scimago Journal Rank a classificação do periódico *Information* (indicado como Q2).
3. **Confirmação de Estrato Qualis:** Confirmar na Plataforma Sucupira o estrato Qualis CAPES da conferência/periódico (estimado em A2 pelo percentil Scopus de 79.0%).