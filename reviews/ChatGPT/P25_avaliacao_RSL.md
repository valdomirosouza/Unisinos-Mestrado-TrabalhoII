# Avaliação do Estudo P25

## Identificação do estudo

**ID:** P25  
**Artigo:** *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments*  
**Autores:** Alka Agrawal, Mohd Nadeem, Ahmed Al Nuaim e Abdullah Al Nuaim  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Embora o arquivo de instruções informe SJR Q1 e Qualis A1, esses campos permanecem como **[VERIFICAR]**, em conformidade com as regras antifabricação.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P25 | *Scientific Reports*, v. 16, artigo 11673 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com protótipo multiagente, simulação em cyber range, validação quantitativa e teste de aceitação | 10.1038/s41598-026-45937-9 |

**Fontes para verificação externa:**

- **Citações:** base indexadora, como Scopus, Web of Science, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | O periódico identifica o artigo como *Scientific Reports* (2026), v. 16, artigo 11673, p. 1. O manuscrito foi recebido em 9 de janeiro de 2026 e aceito em 23 de março de 2026, p. 18. | Atendido |
| Publicação identificável | *Scientific Reports*, v. 16, artigo 11673, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução e revisão, pp. 1–5; “Research objectives and hypothesis”, p. 6; “Multi-agent system architecture”, pp. 11–12; Algoritmo 1, p. 10. | O artigo caracteriza autonomia como a capacidade de agentes atacantes e defensores aprenderem, decidirem e se adaptarem por interação com o ambiente. O atacante utiliza uma política de reinforcement learning formulada como MDP, enquanto os defensores detectam anomalias e selecionam respostas. Comunicação assíncrona permite coordenação e ações paralelas. Entretanto, não apresenta uma taxonomia de níveis de autonomia, memória agêntica explícita, planejamento baseado em LLM ou um modelo detalhado de supervisão humana. Além disso, a remediação é apoiada por uma biblioteca de ações predefinidas, e não integralmente aprendida pelo agente. |
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | RQ2 — Engineering Architecture | Respondida Plenamente | T | “Research methodology”, pp. 7–8; Figuras 5–9, pp. 7–11; Algoritmo 1, p. 10; “Model implementation”, pp. 12–14. | A arquitetura multiagente é descrita com agentes atacantes baseados em DQN e Policy Gradient, defensores com Random Forest e Autoencoder, ambiente CyDER 2.0, APIs de integração, módulos de resposta, monitoramento e comunicação FIPA/ACL. A implementação utiliza Python, TensorFlow/PyTorch, scikit-learn, Docker, ZeroMQ e mensagens JSON. Capacidades avançadas incluem execução assíncrona, coordenação distribuída, detecção supervisionada e não supervisionada, resposta automática, otimização de hiperparâmetros, early stopping e monitoramento em tempo real. |
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | RQ3 — Evidence Benefits | Respondida Plenamente | T | “Experimental setup and results”, pp. 14–17; Tabelas 8–14, pp. 15–18; “Results”, p. 17. | O estudo apresenta evidência diretamente relacionada a incident response. O MAS alcança F1 entre 87,9% e 94,5% em redes de 50 a 200 hosts, enquanto o MAS baseado em regras obtém 71,8% a 80,1%. A latência média entre detecção e início da resposta varia de 4,2 a 6,1 segundos, contra 6,5 a 9,5 segundos no baseline baseado em regras e 12,1 a 18,4 segundos no cyber range estático. A Tabela 14 resume F1 de 91%, latência de 5,3 segundos e suporte a mais de 25 agentes. Também são avaliados precisão, recall, complexidade dos ataques, consumo de CPU/memória, confiabilidade de mensagens, robustez e escalabilidade. A evidência vem de simulação controlada com dados CICIDS2017 e UNSW-NB15, não de incidentes em produção, e não mede carga cognitiva humana. |
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Revisão da literatura, pp. 3–5; metodologia, pp. 8 e 12–14; “Results”, p. 17; conclusão, p. 18. | O artigo cobre desafios técnicos como escassez e limitações de datasets, ajuste de hiperparâmetros, overfitting, escalabilidade, consumo de recursos, confiabilidade da comunicação, generalização e operação em dispositivos de borda restritos. Como mecanismos de controle, utiliza validação cruzada, testes hold-out, stress testing, early stopping, regras predefinidas de resposta, alertas aos administradores e aceitação por especialistas. Entretanto, não desenvolve ética, accountability, autorização das ações defensivas, auditoria independente, segregação de privilégios, privacidade, segurança da comunicação ZeroMQ ou governança para erros de remediação. |
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | RQ5 — Research Gaps | Respondida Plenamente | T | “Summary and identified research gaps”, pp. 4–5; “Problem formulation”, pp. 5–6; Tabela 15, p. 18; conclusão, p. 18. | O estudo identifica lacunas explícitas: ausência de agentes adaptativos em cyber ranges, pouca integração entre MAS e ambientes operacionais de simulação, dependência de dados sintéticos, validação limitada, baixa escalabilidade e pouca automação da resposta a incidentes. Como direções futuras, propõe compressão de modelos, inferência leve e arquiteturas híbridas edge-cloud para reduzir restrições computacionais e de armazenamento. |
| P25 |  | **SCORE_RQ** | **4,0 / 5,0** | **P + T + T + P + T** |  | O estudo tem aderência elevada ao ciclo de detecção e resposta a incidentes, com arquitetura multiagente, ações automáticas e métricas de latência. A cobertura é menos completa quanto a definições contemporâneas de Agentic AI, memória, supervisão humana e governança responsável. |

### Observação crítica sobre a autonomia da resposta

Embora o sistema seja apresentado como um framework autônomo, a seção de resultados informa que o componente de resposta utiliza uma biblioteca predefinida de ações inspirada em metodologias existentes. A inteligência adaptativa está mais claramente demonstrada na simulação ofensiva e na detecção de anomalias. A seleção ou execução da resposta combina resultados aprendidos com políticas baseadas em regras. Portanto, o estudo não deve ser interpretado como evidência de remediação inteiramente aprendida ou planejada de forma autônoma.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P25 | Estudo empírico experimental com protótipo, cyber range, datasets públicos e validação quantitativa | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O artigo explicita como problema a incapacidade de cyber ranges estáticos ou baseados em regras representarem ataques adaptativos, encadeados e próximos do comportamento de adversários reais. A solução é apresentada como um MAS com agentes atacantes baseados em reinforcement learning e defensores capazes de detectar anomalias e coordenar respostas automáticas. Três hipóteses avaliam acurácia, tempo de resposta e escalabilidade. Evidências: pp. 1–2 e 5–6.

**QA2 — Metodologia replicável: P (0,5).**  
A metodologia descreve datasets, pré-processamento, divisão 80/20, SMOTE, topologias com 50, 120 e 200 hosts, cenários de ataque, número de agentes, métricas, baselines, arquitetura DQN, camadas, taxa de aprendizado, desconto, estratégia ε-greedy, replay buffer, batch, sincronização da rede-alvo, parâmetros do Random Forest e critérios de early stopping. Entretanto, não informa versões exatas de todas as bibliotecas, configuração completa do Autoencoder, conteúdo integral da biblioteca de respostas, número de repetições por cenário, sementes aleatórias, código-fonte ou detalhes suficientes para reconstruir integralmente o ambiente CyDER 2.0 e reproduzir todos os testes estatísticos. A replicação conceitual é possível, mas a reprodução fiel permanece limitada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
Há experimentos em três tamanhos de rede e diferentes níveis de complexidade, usando dois datasets públicos. O artigo realiza comparação com baselines estático e baseado em regras, validação cruzada, hold-out, testes de estresse, múltiplos treinamentos, avaliação de aceitação por especialistas e testes estatísticos. As métricas abrangem precisão, recall, F1, latência, complexidade do ataque, uso de recursos, confiabilidade, disponibilidade e escalabilidade. Evidências: pp. 8 e 14–18.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões retomam os ganhos observados em detecção, velocidade de resposta, complexidade dos cenários e escalabilidade. O artigo reconhece que os testes de CPU e memória foram realizados em ambiente de classe servidor e que a execução em dispositivos de borda representa uma limitação computacional e de armazenamento. Também apresenta trabalhos futuros coerentes com essa limitação. Evidência: conclusão, p. 18.

---

## Parecer final do revisor

O estudo apresenta aderência elevada ao escopo de resposta a incidentes, pois integra detecção, coordenação multiagente, contenção automática e avaliação do tempo de resposta em cyber range. Sua principal força é a validação quantitativa em cenários controlados com datasets públicos, diferentes tamanhos de rede e comparação com abordagens estáticas. Contudo, não utiliza LLMs, opera exclusivamente em ambiente simulado e combina decisões aprendidas com políticas predefinidas de remediação. A governança e a supervisão de ações autônomas também recebem atenção limitada.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada pela relação direta com incident response, pelas métricas de latência e qualidade de detecção e pela arquitetura multiagente adaptativa. As ressalvas decorrem da distância em relação ao paradigma de copiloto baseado em LLM, da ausência de validação em produção, do componente de resposta parcialmente baseado em regras e da cobertura insuficiente de accountability, segurança das ações e interação humano-agente. O estudo deve ser tratado como evidência de automação multiagente adaptativa para treinamento e simulação de resposta a incidentes, não como comprovação de um copiloto agêntico completo em ambiente operacional real.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
