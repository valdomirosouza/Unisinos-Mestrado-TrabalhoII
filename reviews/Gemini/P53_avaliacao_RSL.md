# Avaliação de Estudo Candidato — RSL Ciclo 2

## 1. Contexto e Diretrizes Metodológicas (Prompt de Entrada)

### Papel
Pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, seguindo rigorosamente as diretrizes de Kitchenham (2009) no paper/artigo *"Systematic literature reviews in software engineering – A systematic literature review"*. A avaliação de qualidade espelha a lógica dos critérios DARE (QA1–QA4).

### Contexto da RSL
Esta avaliação integra o artigo **"Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura"**, no ciclo 2 de atualização. O corpus prévio cobre P01–P40 (33 estudos incluídos). Avalia-se um candidato por vez para integração direta às Tabelas 3, 5 e 7 da RSL existente.

### Insumos Fornecidos
- **ID:** P53
- **Artigo:** Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks
- **Arquivo:** `P53_Anomaly_Detection_and_Root_Cause_Analysis_in_Cloud-Native_Environments_Using_Large_Language_Models_and_Bayesian_Networks.pdf`
- **Qualis:** A1 (derivado do percentil Scopus 91.0%, regra CAPES 2025-2028)
- **SJR Quartile:** Q1
- **Ressalvas de Triagem:** Aprovado na triagem; *Comparison N/A* (contraste conceitual) na extração PICOC.

### Regras Invioláveis (Antifabricação)
1. Avaliar exclusivamente o conteúdo presente no PDF anexado, sem usar suposições ou conhecimento externo não verificável no texto.
2. Não inventar métricas, números de página, citações, DOI, quartil SJR, estrato Qualis ou contagem de citações.
3. Dados não verificáveis no PDF (quartil SJR, estrato Qualis CAPES, número de citações) devem ser marcados como `[VERIFICAR]`.
4. Toda classificação (T/P/N e Y/P/N) deve ser ancorada em evidência concreta do texto (seção, figura, tabela ou página).

---

## 2. Etapa 1 — Triagem de Elegibilidade (PRISMA / Critérios da RSL)

- **Ano $\ge$ 2020:** 2025 (Recebido: 12/fev/2025, Aceito: 17/abr/2025, Publicado: 29/abr/2025) $\rightarrow$ **Aprovado** (p. 77550).
- **Publicação $\neq$ NULL:** Periódico IEEE Access (Volume 13, 2025) $\rightarrow$ **Aprovado** (p. 77550).
- **Citações $\ge$ 1:** Não verificável diretamente no corpo do PDF $\rightarrow$ **[VERIFICAR em base indexadora]**.
- **SJR Q1–Q2:** Insumo reporta Q1 $\rightarrow$ **[VERIFICAR no Scimago Journal Rank]**.
- **Qualis A1–A2:** Insumo reporta A1 $\rightarrow$ **[VERIFICAR na Plataforma Sucupira/CAPES]**.

**Veredito da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (procedendo à extração técnica completa).

---

## 3. Tabela A — Extração Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo de Estudo | DOI / URL |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P53** | IEEE Access | 2025 | [VERIFICAR: Scopus/Scholar] | [VERIFICAR: Scimago Q1] | [VERIFICAR: Sucupira A1] | Artigo de Periódico (Estudo Experimental em PaaS) | [10.1109/ACCESS.2025.3565220](https://doi.org/10.1109/ACCESS.2025.3565220) |

---

## 4. Tabela B — Classificação das Questões de Pesquisa (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (Seção/Pág.) | Parecer do Revisor |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **P53** | Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks | **RQ1** | Parcialmente Respondida | **P** | Abstract (p. 77550), Sec. I (p. 77551), Sec. IV-A (p. 77556–77557) | Aborda o suporte à decisão operacional em ambientes complexos por meio de inferência probabilística e interface conversacional para operadores. Contudo, não formaliza níveis explícitos de autonomia agêntica (ex.: L1-L5), planejamento autônomo multi-etapa ou modelos rigorosos de governança HITL/HOTL. |
| **P53** | Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks | **RQ2** | Respondida Plenamente | **T** | Sec. III, IV, IV-A, IV-B, Figs. 1, 3, 5, 11 (p. 77554–77561) | Detalha extensivamente a arquitetura dos sistemas MAIA e Baynet: ingestão com Grafana Loki e AWS S3, orquestração no EKS com Istio, mensageria via AWS SQS, fine-tuning do Llama-3 8B, Sentence Transformers (MPNet) para thresholding de cosseno ($0.8$) e inferência em Redes Bayesianas dinâmicas com pgmpy integradas ao Grafana Tempo. |
| **P53** | Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks | **RQ3** | Respondida Plenamente | **T** | Sec. VI, Figs. 16, 17, 18, 19 (p. 77561–77563) | Apresenta evidência quantitativa robusta em 12 cenários de falha injetados: matriz completa com Acurácia, Precisão, Recall, F1-Score, Falsos Positivos e Falsos Negativos. Demonstra a probabilidade de causalidade por nó gráfico (ex.: *frontend* 90.0%, *shipping* 78.0%) e o efeito em cadeia em nós dependentes (*orders* 12.16%). |
| **P53** | Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks | **RQ4** | Parcialmente Respondida | **P** | Sec. II-A (p. 77552–77554), Sec. IV-A (p. 77556–77557), Sec. VII (p. 77563) | Discute com profundidade riscos operacionais e técnicos: trade-off entre precisão e recall, fadiga de alertas por falsos positivos, risco de sobreajuste (*overfitting* no teste de cache), custo computacional de LLMs e a cegueira de LLMs para valores numéricos estritos. Entretanto, carece de análise de implicações éticas e conformidade regulatória estrita. |
| **P53** | Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks | **RQ5** | Respondida Plenamente | **T** | Sec. VII (p. 77563) | Delineia direções futuras detalhadas: mapeamento sistemático do grafo de dependência de falhas com Chaos Mesh, hibridização do pipeline com redes neurais recorrentes (LSTM) para métricas numéricas estruturadas e substituição do cabeçote de linguagem por um cabeçote classificador supervisionado dedicado. |
| **P53** | **SCORE_RQ** | — | — | — | — | **4.0 / 5.0** |

---

## 5. Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 (Objetivos) | QA2 (Reprodutibilidade) | QA3 (Evidência) | QA4 (Conclusões) | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P53** | Estudo Experimental (PaaS / Cloud-Native) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

### Justificativas dos Critérios DARE:
- **QA1 (Objetivos Claros = Y):** Os autores definem de forma transparente o desafio de diagnosticar falhas em topologias distribuídas de alta volatilidade, formulando a solução por meio do desacoplamento entre detecção de anomalias textuais não estruturadas (LLM) e localização causal estruturada (Bayes Network).
- **QA2 (Metodologia Replicável = Y):** A infraestrutura é descrita de ponta a ponta: stack *sock-shop* de 12 microsserviços poliglota, cluster AWS EKS, automação de CI/CD via CircleCI, gerador de carga Locust, injeção de caos via Chaos Mesh, modelo Llama-3 8B treinado em janelas deslizantes de 10 logs normais e limiar de corte de similaridade de cosseno fixado em $0.8$.
- **QA3 (Base de Evidências Sólidas = Y):** Validação conduzida com pipeline automatizado sob baterias de teste de 30 minutos por cenário (10 min estável, 10 min injeção de anomalia, 10 min recuperação), cobrindo falhas de pod, lentidão de rede, aborto HTTP, restrição de CPU/memória e IO de banco em Mongo e MySQL, acompanhado de contagem exata de VP, FP e FN.
- **QA4 (Conclusões Coerentes = Y):** As conclusões refletem estritamente as limitações dos dados coletados, discutindo a vulnerabilidade da abordagem em anomalias de IO (Mongo IO fail com Recall de $0.7077$) e a tendência da LLM em desconsiderar grandezas escalares críticas (latências, portas e IPs).

---

## 6. Parecer Final do Revisor

### Síntese
O artigo investiga a automação do ciclo de resposta a incidentes operacionais em ambientes nativos em nuvem (*cloud-native*), mitigando diretamente o tempo de diagnóstico (MTTD e MTTR) e a sobrecarga cognitiva do operador SRE. A arquitetura proposta articula o uso de Large Language Models para capturar anomalias em fluxos de logs sem esquema (*schema-free*) com o uso de Redes Bayesianas dinâmicas alimentadas por telemetria de rede e traces do Istio/Tempo para computar a probabilidade de causa-raiz. O trabalho possui forte relevância prática e alinhamento central com as dimensões de observabilidade e arquiteturas de suporte a incidentes analisadas na RSL.

### Recomendação
**INCLUIR COM RESSALVAS.**
- *Justificativa:* O estudo atinge alta pontuação metodológica (**SCORE_QA: 4.0/4.0**) e ampla cobertura de questões técnicas (**SCORE_RQ: 4.0/5.0**). A ressalva decorre da classificação conceitual na extração PICOC (*Comparison N/A*, pois o artigo estabelece contraste conceitual com baselines da literatura sem submetê-las ao mesmo ambiente empírico de testes de caos) e do fato de o componente agêntico/conversacional atuar prioritariamente como copiloto consultivo e inferencial, sem disparar ações corretivas autônomas de remediação ativa em malha fechada.

### Pendências de Verificação Externa
1. **Citações:** Checar a contagem de citações consolidadas nas bases indexadoras (Scopus e Google Scholar).
2. **Qualis CAPES:** Confirmar o estrato oficial atribuído ao periódico *IEEE Access* no quadriênio vigente na Plataforma Sucupira (insumo estima A1 com base em percentil de citação).
3. **SJR Quartile:** Validar o enquadramento em Q1 junto ao portal oficial do Scimago Journal & Country Rank.