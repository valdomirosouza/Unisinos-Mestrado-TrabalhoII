# Avaliação Sistemática de Literatura — Estudo P25

**Artigo avaliado:** *Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments*  
**Autores:** Alka Agrawal; Mohd Nadeem; Ahmed Al Nuaim; Abdullah Al Nuaim  
**Arquivo fonte:** `P25-A1-s41598-026-45937-9.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — 2026 (recebido em 9 jan. 2026, aceito em 23 mar. 2026, publicado online em 7 abr. 2026, pp. 1, 18).
- **Publicação ≠ NULL (veículo identificável):** Sim — *Scientific Reports* (*Nature Portfolio*), Volume 16, Artigo 11673, pp. 1–20.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *Scientific Reports*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação / Interdisciplinar).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P25 | Scientific Reports (Vol. 16, Art. 11673, pp. 1–20) | 2026 | `[VERIFICAR]` (base indexadora: Scopus / WoS / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Artigo de pesquisa empírica / Proposta de framework multiagente (RL + ML) com avaliação experimental em *Cyber Range* | `10.1038/s41598-026-45937-9` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P25 | Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments | RQ1 | Respondida Plenamente | T (1.0) | Seções *Introduction* e *Model development* (pp. 1–2, 8–13); Algoritmo 1 (p. 10); Tabelas 14 e 15 (p. 18) | **(a) Autonomy definition:** Define autonomia adaptativa em um Sistema Multiagente (MAS) ofensivo/defensivo integrado a um *cyber range*, opondo agentes com autoaprendizado a simulações estáticas/baseadas em regras fixas. **(b) Core characteristics:** Agentes Atacantes modelados via Processo de Decisão de Markov $M=(S,A,P,R,\gamma)$ com memória de *replay buffer* (100k tuplas) e espaço de ações táticas (*Scan, Exploit, Privilege Escalation, Evade*); Agentes Defensores com percepção de fluxo de rede, comunicação assíncrona via padrões FIPA ACL / JSON e execução de contenção. **(c) Decision-making model:** Política *Deep Q-Network* (DQN) / *Policy Gradient* ($\epsilon$-greedy) nos atacantes e *ensemble* híbrido (*Random Forest* supervisionado + *Autoencoder* não-supervisionado) acoplado a regras de resposta baseadas no *NIST SP 800-61* nos defensores, com escalonamento de alertas e logs forenses a operadores humanos. *(Nota: não utiliza LLMs, empregando RL/ML clássico)*. |
| P25 | Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments | RQ2 | Respondida Plenamente | T (1.0) | Figuras 3, 5, 7, 8 e 9 (pp. 4, 7–9, 11); Seções *Model development* e *Model implementation* (pp. 8–14); Tabelas 4, 6 e 7 (pp. 12, 14) | **(a) Architecture type:** Arquitetura multiagente distribuída e conteinerizada (*Attacker Agents* e *Defender Agents*) acoplada via hooks de API ao simulador de *cyber range* em nuvem *CyDER 2.0*. **(b) Tools/frameworks:** *Python*, *TensorFlow*, *PyTorch*, *scikit-learn*, mensageria assíncrona *ZeroMQ* (JSON / FIPA ACL), contêineres *Docker*, simulador *CyDER 2.0* e pré-processamento com *SMOTE* sobre os datasets *CICIDS2017* e *UNSW-NB15*. **(c) Advanced capabilities:** Coordenação distribuída entre múltiplos defensores (compartilhamento de alertas com 99,8% de confiabilidade e latência de ação de $85 \pm 15\text{ ms}$) e ações automatizadas de contenção em tempo real (bloqueio de IP em firewall/IPS, quarentena de host comprometido, encerramento de sessão e geração de logs forenses). |
| P25 | Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments | RQ3 | Respondida Plenamente | T (1.0) | Tabelas 2, 3 e 5 a 14 (pp. 6, 13–18); Seções *Experimental setup and results* e *Results* (pp. 14–18) | **(a) Qualitative benefits:** Simulação realista de ataques multi-estágio (reconhecimento, exploração, escalonamento de privilégios, movimento lateral e exfiltração) e mitigação rápida automatizada validada por 25 especialistas em cibersegurança. **(b) Quantitative benefits / metrics:** Validação do *ensemble* defensor atingiu 93% de acurácia e 91,9% de F1-score (Tabela 6). Em 3 topologias de rede — Pequena (50 hosts), Média (120 hosts) e Grande (200 hosts) — o MAS proposto obteve F1 de 94,5%, 89,9% e 87,9% (vs. 80,1%, 75,5% e 71,8% do MAS baseado em regras e 67,8%, 59,2% e 56,1% do estático, Tabela 9; ganho médio de 25% em F1). A latência média de resposta a incidentes foi de 4,2 s (50 hosts), 5,6 s (120 hosts) e 6,1 s (200 hosts), reduzindo o tempo em 35% frente aos *baselines* (6,5–9,5 s e 12,1–18,4 s, Tabela 10). Consumo por agente: $30\pm 4\%$ CPU e $130\pm 12\text{ MB}$ RAM (defensor, Tabela 12). **(c) Evidence level:** Experimentos em simulador *CyDER 2.0* com dados de *CICIDS2017* e *UNSW-NB15* + validação estatística ($t$-test, ANOVA, $p<0,05$) e avaliação por 25 especialistas. |
| P25 | Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments | RQ4 | Parcialmente Respondida | P (0.5) | Seção *Literature review* (pp. 3–4); Seção *Experimental results* e *Results* (pp. 15–17); Seção *Conclusion* (p. 18) | **(a) Technical challenges:** Queda de acurácia de detecção (F1 de 94,5% para 87,9%) e aumento de latência (4,2 s para 6,1 s) conforme a escala da rede cresce para 200 hosts com ataques simultâneos; complexidade de ajuste de hiperparâmetros em RL; desbalanceamento de classes em datasets de intrusão; e restrições de CPU/memória para execução em dispositivos de borda (*edge*). **(b) Ethical/governance challenges:** Não aborda dilemas éticos ou regulatórios de IA, destacando apenas que *cyber ranges* oferecem ambiente seguro e controlado (*risk-free*) para testes ofensivos/defensivos. **(c) Governance mechanisms:** Ações defensivas estritamente vinculadas a regras baseadas no padrão *NIST SP 800-61* e geração de logs forenses e alertas para supervisão humana em estágios críticos como exfiltração de dados (p. 17). |
| P25 | Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments | RQ5 | Parcialmente Respondida | P (0.5) | Seção *Conclusion* (p. 18) | Aponta de forma concisa na conclusão a limitação de implantar o MAS em dispositivos de borda com recursos restritos, propondo como direções futuras: (1) técnicas de compressão de modelos; (2) modelos de inferência leves (*lightweight inference models*); e (3) arquiteturas híbridas *edge-cloud* para operação distribuída. |
| **P25** | **TOTAL (SCORE_RQ)** | — | **4.0 / 5.0** | **3T, 2P** | — | Forte aderência em coordenação multiagente para resposta automatizada a incidentes e métricas de tempo de resposta/F1, embora baseado em RL/ML tradicional (sem LLMs). |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P25 | Artigo de pesquisa empírica / Simulação multiagente em *Cyber Range* | Y (1.0) | P (0.5) | Y (1.0) | Y (1.0) | **3.5 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** O problema (incapacidade de *cyber ranges* estáticos de emular ameaças persistentes avançadas — APTs — com movimento lateral e resposta adaptativa) e as três hipóteses de pesquisa ($H_1$: acurácia de detecção, $H_2$: tempo de resposta a incidentes, $H_3$: escalabilidade, p. 6) são explicitamente declarados e validados previamente por *survey* com 25 especialistas (Tabelas 2 e 3, p. 6).
- **QA2 — Metodologia Replicável (P = 0.5):** O artigo explicita hiperparâmetros do DQN (3 camadas: 128, 64, 32 neurônios; $\text{lr}=0,001$; $\gamma=0,95$; $\epsilon$-greedy de 0,8 a 0,1 em 5.000 episódios), do *Random Forest* (100 árvores, profundidade 20) e do *Autoencoder* (p. 13), além do Algoritmo 1 (p. 10). Contudo, não disponibiliza código-fonte, não detalha tecnicamente como registros tabulares estáticos do *CICIDS2017*/*UNSW-NB15* são reencenados interativamente pelo agente RL no *CyDER 2.0*, e apresenta graves erros de indexação bibliográfica ao longo do texto (ex.: citações numéricas no texto e nas Tabelas 1 e 14 não correspondem aos respectivos artigos na lista de referências das pp. 19–20, incluindo referências desconexas sobre identificação de peptídeos e galáxias nos itens [1], [12] e [29]).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Fornece bateria empírica abrangente com pré-processamento documentado (Tabela 4), progressão de treinamento (Tabela 5), validação de componentes (Tabelas 6 e 7) e comparação em três escalas de rede (50, 120 e 200 hosts) contra dois *baselines* (*Rule-based MAS* e *Static Cyber-Range*) avaliando precisão, recall, F1-score, latência de resposta em segundos, complexidade de ataque e uso de CPU/RAM (Tabelas 9 a 12).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões confirmam as hipóteses testadas com base nas evidências reportadas e apontam de forma coerente as limitações de sobrecarga computacional para ambientes de borda (p. 18).

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P25 apresenta um framework de Sistema Multiagente (MAS) integrado ao simulador de *cyber range* *CyDER 2.0* para simulação adaptativa de ataques cibernéticos e resposta automatizada a incidentes (bloqueio de IP, quarentena de host, encerramento de sessão e geração de logs forenses segundo o *NIST SP 800-61*). Embora implemente seus agentes com Aprendizado por Reforço (*DQN*) e *ensemble* de *Machine Learning* (*Random Forest* + *Autoencoder*) em conjunto com comunicação *ZeroMQ/FIPA ACL* — sem utilizar modelos de linguagem (LLMs) —, o artigo entrega métricas de referência altamente relevantes para resposta a incidentes (redução de 35% na latência de resposta, operando entre 4,2 s e 6,1 s, e ganho de 25% em F1-score), obtendo `SCORE_RQ = 4.0/5.0` e `SCORE_QA = 3.5/4.0` (Banda Alta).
- **Recomendação:** **INCLUIR COM RESSALVAS** — O estudo aporta evidências quantitativas valiosas sobre coordenação multiagente e latência de contenção automatizada alinhada ao *NIST SP 800-61*; as ressalvas devem-se ao fato de a arquitetura agêntica basear-se em RL/ML clássico e regras (e não em LLMs/GenAI) e às inconsistências na numeração das referências bibliográficas do artigo publicado.
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *Scientific Reports* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
