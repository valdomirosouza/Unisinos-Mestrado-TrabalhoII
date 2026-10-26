# Avaliação Sistemática de Literatura — Estudo P22

**Artigo avaliado:** *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control*  
**Autores:** Vasilis Avgerinos; Kostas Ramantas; Luis Alonso; Christos Verikoukis  
**Arquivo fonte:** `P22-A1-ARM_Autonomous_Remediation_and_Management_With_LLM_Agents_for_Intent-Driven_Control.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — publicado online em dezembro de 2025 / fascículo de maio de 2026 (p. 1 / p. 18305).
- **Publicação ≠ NULL (veículo identificável):** Sim — *IEEE Internet of Things Journal*, Volume 13, Número 9, pp. 18305–18315.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science, IEEE Xplore ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *IEEE Internet of Things Journal*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P22 | IEEE Internet of Things Journal (Vol. 13, No. 9, pp. 18305–18315) | 2026 (pub. dez. 2025) | `[VERIFICAR]` (base indexadora: Scopus / IEEE Xplore / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Artigo de pesquisa empírica / Framework em malha fechada com avaliação experimental via *Chaos Engineering* | `10.1109/JIOT.2025.3648858` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P22 | ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control | RQ1 | Respondida Plenamente | T (1.0) | Seção I (pp. 18305–18306); Seção III-D (p. 18307); Seção IV-A a IV-C (pp. 18307–18309) | **(a) Autonomy definition:** Define o agente como um operador autônomo em malha fechada (*closed-loop control*) com autoridade para diagnosticar causas-raiz (RCA) e executar ações corretivas em sistemas Cloud–Edge/IoT orientados a intenção. **(b) Core characteristics:** Planejamento explícito (`create_action_plan`), invocação de ferramentas via *Model Context Protocol* (MCP), reflexão *inline* a cada rodada, memória contextual cumulativa transiente (com *temporal caching* e filtro de chamadas recentes) e geração de relatório pós-execução (`generate_operational_summary`). **(c) Decision-making model:** Ciclo iterativo tipo *ReAct* governado por três restrições estruturais obrigatórias, raciocínio guiado por evidências (*evidence-first*), viés de resolução (*action bias*) e tabelas heurísticas de mapeamento sintoma-ação (Tabela II, p. 18309). |
| P22 | ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control | RQ2 | Respondida Plenamente | T (1.0) | Seção III-A a III-D (p. 18307); Seção IV-A a IV-C, Figura 1 e Tabela I (pp. 18307–18309); Seção V-A (p. 18309) | **(a) Architecture type:** Arquitetura *single-agent* em malha fechada (escolhida frente a *multi-agent* para maior auditabilidade), integrando monitoramento contínuo, gerador de objetos de intenção $\mathcal{I}(t)$, loop agêntico e servidor MCP. **(b) Tools/frameworks:** Cluster *Kubernetes K3s* sobre VMs QEMU, *Prometheus* e *Grafana*, servidor MCP expondo 4 classes de ferramentas (*Planning*, *Kubernetes Management* via `kubectl_apply/scale/delete/drain/patch`, *Monitoring* via Prometheus e *Utility* `sleep_seconds`), avaliado com *GPT-5* e *GPT-5-mini*. **(c) Advanced capabilities:** Observabilidade de topologia e séries temporais (latência P95 e taxa de sucesso), validação pós-intervenção após janela de estabilização, abstração segura de ferramentas via MCP e suporte a *workflows* de aprovação humana por ferramenta. |
| P22 | ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control | RQ3 | Respondida Plenamente | T (1.0) | Resumo (p. 18305); Seção V-A a V-E (pp. 18309–18311); Seção VI-A a VI-D, Tabelas IV e V, Figuras 3 e 4 (pp. 18311–18313); Apêndice (pp. 18313–18314) | **(a) Qualitative benefits:** Remediação autônoma fim a fim altamente explicável e auditável (planos e sumários estruturados), com adaptação sensível ao contexto (ex.: reinício de *pod* em nós de borda restritos vs. escalonamento HPA e ajuste de `nodeAffinity` na nuvem). **(b) Quantitative benefits / metrics:** Em 60 experimentos de *Chaos Engineering* (`chaosd`) sobre 3 aplicações *MuBench* (3, 8 e 12 microsserviços), o agente GPT-5 obteve ~80% de sucesso na restauração de SLAs (80,0% *IoT Gateway*, 90,0% *Smart Manufacturing*, 80,0% *Smart City*) e 80,0%–87,5% de acurácia de identificação por aplicação (no *Abstract*, cita-se 52,9% de identificação e 70,7% de mitigação geral), recuperando 80,4% da degradação de latência ($R_{\text{lat}}$) sob estresse de CPU em 13,0–18,6 rodadas médias (5,2 a 11,8 min), superando amplamente o *GPT-5-mini* (40,0%–66,7% de identificação). **(c) Evidence level:** Avaliação experimental sistemática em 4 fases em *testbed* Cloud–Edge virtualizado reproduzível com injeção controlada de falhas. |
| P22 | ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control | RQ4 | Parcialmente Respondida | P (0.5) | Seção IV-B e IV-C (pp. 18308–18309); Seção VI-A a VI-C (pp. 18311–18313); Seção VII (p. 18313) | **(a) Technical challenges:** Tempo de resolução elevado em topologias complexas (até 11,8–13,6 min), forte degradação de raciocínio causal em modelos menores (*GPT-5-mini* cai a 0% de identificação em falhas de memória/pod único e adota tentativa-e-erro), alto custo de coleta de contexto (ferramentas de observabilidade dominam as chamadas, Figura 3) e limitações da métrica binária de sucesso em falhas sutis. **(b) Ethical/governance challenges:** Discute o alto risco de ações destrutivas errôneas em produção (ex.: reiniciar serviços críticos saudáveis) e a exigência de *accountability* pós-hoc, sem abordar ética sociojurídica ampla. **(c) Governance mechanisms:** Camada MCP que impede acesso *shell* irrestrito, exigência de plano explícito com análise de riscos, vedação de intervenção especulativa sem evidência prévia e suporte a aprovação humana configurável por ferramenta. |
| P22 | ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control | RQ5 | Respondida Plenamente | T (1.0) | Seção VI-B (p. 18312); Seção VII (p. 18313) | Identifica direções claras de pesquisa futura: (1) paradigmas de compressão inteligente de contexto e filtragem dinâmica de telemetria para escalar a arquiteturas empresariais; (2) arquiteturas agênticas mais profundas combinando consultas de baixo nível com algoritmos de detecção de anomalias em ML; (3) *fine-tuning* de modelos menores para equilibrar custo/tamanho e acurácia causal; (4) formalização e avaliação de salvaguardas de segurança (*safety safeguards*) para ações de alto impacto; e (5) validação em *testbeds* IoT de produção em larga escala. |
| **P22** | **TOTAL (SCORE_RQ)** | — | **4.5 / 5.0** | **4T, 1P** | — | Estudo altamente alinhado a todas as RQs da RSL, cobrindo tanto RCA quanto mitigação ativa via MCP em Kubernetes. |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P22 | Artigo de pesquisa empírica / Framework em malha fechada com avaliação experimental via *Chaos Engineering* | Y (1.0) | Y (1.0) | Y (1.0) | Y (1.0) | **4.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** A Seção I e a Seção II-C (pp. 18305–18307) estabelecem de maneira cristalina a lacuna da literatura (foco exclusivo em diagnóstico/RCA passivo sem atuação corretiva) e o objetivo do framework ARM de realizar diagnóstico de causa raiz e mitigação autônoma em malha fechada para violações de SLA em ambientes Cloud–Edge/IoT.
- **QA2 — Metodologia Replicável (Y = 1.0):** Detalha rigorosamente a formulação matemática do monitoramento e critérios de recuperação ($\epsilon_{l,95}=0.15$, $\epsilon_{q,\text{success}}=0.01$, $R_{\text{lat}}$), as ferramentas expostas pelo servidor MCP (Tabela I), as regras e heurísticas do *system prompt* (Tabela II), a infraestrutura experimental (7 VMs QEMU com K3s, Prometheus, Grafana, emulador *MuBench* e injetor `chaosd`), o protocolo de 4 fases e um exemplo completo de execução no Apêndice (pp. 18313–18314).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Executa uma campanha experimental sistemática de 60 cenários de injeção de falhas (estresse de CPU/memória em nível de *pod* e nó, além de disrupção de *pods*) através de 3 aplicações distribuídas (3, 8 e 12 microsserviços), comparando dois modelos (*GPT-5* e *GPT-5-mini*) sob métricas objetivas de acurácia diagnóstica, sucesso de remediação, recuperação de latência, número de rodadas, tempo de resolução e distribuição de uso de ferramentas (Tabelas IV e V, Figuras 3 e 4).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões refletem fielmente os resultados obtidos e discutem com rigor crítico as limitações encontradas (como o *wall-clock time* elevado em topologias maiores, o viés da métrica binária em anomalias sutis para o modelo menor e a dependência de modelos de fronteira para raciocínio causal complexo).

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P22 é diretamente central para o tema de *Agentic AI Copilot para Resposta a Incidentes*, apresentando o framework ARM (*Autonomous Remediation and Management*), que integra agentes LLM ao *Model Context Protocol* (MCP), *Prometheus* e *Kubernetes* para detectar violações de SLA, diagnosticar a causa raiz (RCA) e executar autonomamente ações de mitigação (escalonamento HPA, reinício de *pods*, *cordon/drain* de nós e ajuste de afinidade). O trabalho preenche com excelência as dimensões de autonomia (RQ1), arquitetura de engenharia com MCP (RQ2), métricas empíricas de resposta a incidentes (RQ3) e lacunas de pesquisa (RQ5), obtendo `SCORE_RQ = 4.5/5.0` e `SCORE_QA = 4.0/4.0` (Banda Alta).
- **Recomendação:** **INCLUIR** — Estudo exemplar e diretamente aderente ao núcleo da RSL, fornecendo evidências quantitativas rigorosas e arquitetura detalhada (incluindo uso de servidor MCP e *guardrails* de planejamento/verificação) para resposta autônoma a incidentes em infraestruturas de microsserviços Cloud–Edge.
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science, IEEE Xplore ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *IEEE Internet of Things Journal* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
