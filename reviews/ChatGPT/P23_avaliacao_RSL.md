# Avaliação do Estudo P23

## Identificação do estudo

**ID:** P23  
**Artigo:** *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems*  
**Autores:** Xiao Zhang, Qi Wang, Mingyi Li, Yuan Yuan, Mengbai Xiao, Fuzhen Zhuang e Dongxiao Yu  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Embora o arquivo de instruções informe SJR Q1 e Qualis A1, esses campos permanecem como **[VERIFICAR]**, em conformidade com as regras antifabricação.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P23 | IEEE Transactions on Services Computing, v. 18, n. 6 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com framework, benchmarks públicos, ablação e estudo de caso | 10.1109/TSC.2025.3629066 |

**Fontes para verificação externa:**

- **Citações:** base indexadora, como Scopus, Web of Science, IEEE Xplore ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | Publicação em 5 de novembro de 2025 e versão corrente de 11 de dezembro de 2025, p. 1 do PDF. | Atendido |
| Publicação identificável | IEEE Transactions on Services Computing, v. 18, n. 6, novembro/dezembro de 2025, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução, pp. 1–2 do PDF; Seção III e Figura 2, pp. 3–4; Seção III.D, p. 6. | O artigo caracteriza o agente principalmente pelo uso de ferramentas especializadas e pela síntese contextual de resultados para diagnóstico e recomendação. O modelo decisório segue um pipeline explícito: alinhamento multimodal, localização da causa raiz, classificação do tipo de falha e geração de análise pelo agente GPT-4. Entretanto, não define níveis de autonomia, planejamento autônomo, memória, reflexão iterativa ou supervisão humana como componentes formais. A saída é destinada a auxiliar engenheiros, não a executar autonomamente a remediação. |
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seção III, pp. 3–6; Figura 2, p. 4; Figura 3, p. 7; Seção IV.B.4, p. 8. | A arquitetura é detalhada como um framework de um agente especialista e três ferramentas: T1 para alinhamento de logs, métricas e traces; T2 para localização da causa raiz com FFT, atenção, grafo causal e GAT; e T3 para classificação de falhas com Transformer e GAT. O artigo informa GPT-4, Drain, TF-IDF, modelos de difusão, Transformers, PyTorch 2.4.0, CUDA 12.1, Python 3.8 e GPU RTX 3090. As capacidades avançadas incluem fusão multimodal, raciocínio sobre dependências dinâmicas, análise em múltiplos níveis e prompt estruturado. Não há guardrails ou memória persistente, mas as três subdimensões da RQ são cobertas explicitamente. |
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seção IV, pp. 7–11; Tabelas II–IV, pp. 9–10; Figuras 4–7, pp. 10–11. | O estudo apresenta benefícios qualitativos e quantitativos diretamente associados ao diagnóstico de incidentes. TAMO reporta melhoria média de 4,8% em Acc@1 para localização da causa raiz e de 10,8% em microprecisão para classificação de falhas. No conjunto de nós, alcança Acc@1 de 84,37%, MiPr de 0,8718 e MiF1 de 0,8831. A inferência leva 0,17 segundo por amostra. O estudo de caso localiza Currency Service com 97,96% de confiança e CheckoutPod0 com 82,39%, além de produzir recomendações de reparo mais adequadas que o LLM alimentado com dados brutos. A evidência inclui dois datasets públicos, comparações com baselines, ablação e estudo de caso, embora não avalie MTTD, MTTR ou carga cognitiva humana. |
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Introdução, pp. 1–2; Seção II, p. 3; Seção IV.F, p. 10; Figura 7, p. 11. | Os desafios técnicos são claramente apresentados: desalinhamento multimodal, limite de contexto, dependências dinâmicas, heterogeneidade de entidades, sobrecarga computacional e sensibilidade a hiperparâmetros. A comparação da Figura 7 também mostra omissões, diagnósticos incorretos e recomendações inadequadas quando o LLM processa dados brutos. Contudo, o artigo não discute riscos éticos, accountability, auditoria, privacidade, segurança dos dados de observabilidade, aprovação humana, controle de acesso ou mecanismos formais de governança. |
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | RQ5 — Research Gaps | Parcialmente Respondida | P | Introdução, p. 2; Seção II, p. 3; Seção IV.F, p. 10; Conclusão, p. 11. | O artigo identifica lacunas dos métodos existentes: suporte restrito a modalidades, perda de padrões temporais, limitação de contexto, dependência de regras predefinidas, ausência de traces e dificuldade de modelar grafos dinâmicos. Também evidencia sensibilidade ao parâmetro de regularização e custo adicional de treinamento e inferência. Entretanto, a conclusão não apresenta uma agenda explícita de trabalhos futuros sobre benchmarking, threat models, governança, observabilidade ou alinhamento. |
| P23 |  | **SCORE_RQ** | **3,5 / 5,0** | **P + T + T + P + P** |  | O estudo apresenta elevada aderência às dimensões de arquitetura e evidência empírica para RCA em sistemas cloud-native. Sua contribuição é mais forte como framework de diagnóstico assistido por ferramentas do que como agente plenamente autônomo de resposta a incidentes, pois recomenda ações, mas não executa ou valida remediações. |

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P23 | Estudo empírico experimental com benchmarks, ablação e estudo de caso | Y (1,0) | P (0,5) | Y (1,0) | P (0,5) | **3,0 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitado por três limitações centrais dos métodos baseados em LLM: entrada multimodal, janela de contexto e dependências dinâmicas. A solução proposta também é clara: um agente especialista apoiado por três ferramentas para alinhar observações, localizar causas, classificar falhas e gerar recomendações contextualizadas. Evidências: Resumo e Introdução, pp. 1–2.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo descreve detalhadamente a arquitetura, as equações, os datasets, os baselines, as métricas, as versões de software, o hardware, o otimizador, a taxa de aprendizado, o número de épocas e outros hiperparâmetros. Também apresenta o template do prompt do agente. Entretanto, não informa o valor da semente aleatória, todos os detalhes de pré-processamento e particionamento, a configuração completa das redes e do processo de difusão, os parâmetros de geração do GPT-4 ou um repositório com a implementação integral. A reprodução conceitual é possível, mas a replicação fiel permanece limitada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A avaliação utiliza dois datasets públicos com métricas, logs e traces. O Dataset A inclui 10 serviços, 40 pods, seis nós e 15 tipos de falha; o Dataset B inclui 21 microserviços e três tipos de falha. O estudo compara TAMO com múltiplos baselines, emprega métricas de localização e classificação, realiza ablação, análise de hiperparâmetros, avaliação de eficiência e estudo de caso com dados de falha do HipsterShop. Evidências: Seção IV, pp. 7–11.

**QA4 — Conclusões coerentes: P (0,5).**  
A conclusão é coerente com os resultados e reafirma o melhor desempenho nos dois datasets, o tratamento de dados multimodais e a adaptação a dependências dinâmicas. Contudo, o artigo não apresenta uma discussão explícita e sistemática de limitações, ameaças à validade ou direções futuras. Além disso, a qualidade das recomendações do agente é demonstrada principalmente por comparação qualitativa em um estudo de caso, sem uma métrica específica de correção ou utilidade das soluções propostas.

---

## Parecer final do revisor

O estudo apresenta forte aderência ao escopo da RSL ao tratar RCA automatizada em sistemas cloud-native com logs, métricas e traces. Sua maior contribuição está na arquitetura híbrida, que combina ferramentas especializadas e um LLM para produzir diagnóstico contextual e recomendações de reparo. A validação empírica é ampla para localização e classificação de falhas. Entretanto, o agente não executa remediações, não fecha o ciclo de recuperação e não aborda adequadamente autonomia, supervisão humana e governança.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada pela relevância direta para RCA em incidentes, pelo uso explícito de ferramentas e observabilidade multimodal e pela qualidade da avaliação experimental. As ressalvas decorrem do caráter predominantemente diagnóstico e consultivo do agente, da ausência de execução e validação de remediações, da limitada discussão de riscos e governança e da falta de uma agenda explícita de trabalhos futuros. A inclusão definitiva também depende da confirmação dos critérios bibliométricos externos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
