# Avaliação RSL: Agentic AI Copilot para Resposta a Incidentes (Ciclo 2)

---

## 1. Contexto e Diretrizes do Protocolo da Revisão

### Papel
Pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, seguindo rigorosamente as diretrizes de Kitchenham (2009) no paper *"Systematic literature reviews in software engineering – A systematic literature review"* e critérios DARE (QA1–QA4).

### Contexto da RSL
Avaliação integrante do artigo *"Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura"*, Ciclo 2 de atualização (corpus prévio cobrindo P01–P40, com 33 estudos incluídos).

### Insumos do Estudo Candidato
- **ID:** P87
- **Artigo:** An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense
- **Autores:** Chia-Hong Chou, Arjun Sudheer, Younghee Park
- **Arquivo analisado:** `P87_An_LLM-Based_Agentic_Network_Traffic_Incident-Report_Approach_Towards_Explainable-AI_Network_Defense.pdf`
- **Veículo:** *Journal of Sensor and Actuator Networks* (MDPI), Vol. 15, Issue 2, Artigo 32, 2026. DOI: 10.3390/jsan15020032
- **Qualis estimado:** A1 (derivado do percentil Scopus 97.0%, regra CAPES 2025–2028)
- **SJR estimado:** Q2
- **Ressalvas de triagem:** Aprovado na triagem; núcleo agêntico × IR de rede; componente LLM/RAG sem ablação isolada.

---

## 2. Etapa 1 — Triagem de Elegibilidade (Critérios PRISMA / Protocolo RSL)

- **Ano $\ge$ 2020:** 2026 (Publicado em 7 de abril de 2026) $\rightarrow$ **Atendido**
- **Publicação $\ne$ NULL:** Periódico internacional revisado por pares (*Journal of Sensor and Actuator Networks*, MDPI) $\rightarrow$ **Atendido**
- **Citações $\ge$ 1:** `[VERIFICAR]` (Artigo recentemente publicado; verificar contagem atualizada em base Scopus/Google Scholar)
- **SJR Q1–Q2:** Q2 `[VERIFICAR no Scimago Journal Rank]` $\rightarrow$ **Atendido condicionalmente**
- **Qualis A1–A2:** A1 `[VERIFICAR na Plataforma Sucupira/CAPES]` $\rightarrow$ **Atendido condicionalmente**

**Veredito da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (requer conferência cadastral de citações e indicadores indexados). Prossegue-se para a extração completa e classificação.

---

## 3. Tabela A — Extração Bibliométrica (Alimenta a Tabela 3 da RSL)

| ID | Periódico / Conferência | Ano | Cit. | SJR | Qualis | Tipo de Estudo | DOI / URL |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P87** | *Journal of Sensor and Actuator Networks* (MDPI) | 2026 | [VERIFICAR]\* | Q2 [VERIFICAR]\*\* | A1 [VERIFICAR]\*\*\* | Estudo Experimental / Proposta Arquitetural e Empírica | [10.3390/jsan15020032](https://doi.org/10.3390/jsan15020032) |

\* *Verificar número de citações em base indexadora consolidada (Scopus / Web of Science / Google Scholar).*  
\*\* *Verificar quartil SJR no Scimago Journal Rank.*  
\*\*\* *Verificar estrato no Qualis CAPES 2025–2028 (Sucupira).*

---

## 4. Tabela B — Classificação das RQs (Alimenta a Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência no Texto | Parecer do Revisor |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **P87** | Chou et al. (2026) | **RQ1** (Context Definitions) | Respondida Plenamente | **T** (1.0) | Seção 1 (p. 2–3); Seção 3.1.3 (p. 8–9); Seção 3.6 (p. 11); Seção 4.5 (p. 29–30) | Define formalmente a autonomia assistiva orientada ao paradigma *Human-in-the-Loop* (HITL), atuando o agente como analista copiloto gerador de relatórios e mitigações acionáveis. Detalha capacidades essenciais (RAG dinâmico, raciocínio em múltiplos passos e ancoragem fática). Explicita o modelo de tomada de decisão baseado no framework ReAct (*Reasoning and Acting*) com *chain-of-thought* e chamada autônoma a ferramentas. |
| **P87** | Chou et al. (2026) | **RQ2** (Engineering Architecture) | Respondida Plenamente | **T** (1.0) | Seção 3.1 (p. 7–9, Fig. 1); Seção 3.6 (p. 11, Tab. 2); Apêndices A e B (p. 32–34) | Apresenta arquitetura multiagente baseada em grafo orquestrada com LangGraph e subgrafos especializados (pré-detecção rápida em borda, classificação em ensemble com soft voting, explicabilidade SHAP TreeExplainer e agente sumariador ReAct). Utiliza estado global compartilhado para retenção de memória/contexto; integra ferramentas Tavily (busca web em tempo real), ArXiv (artigos acadêmicos) e ChromaDB (vector store com `all-MiniLM-L6-v2`); implementa guardrails rígidos via prompt engineering (proibição explícita de alucinações, citação mandatória de fontes e temperatura 0.0). |
| **P87** | Chou et al. (2026) | **RQ3** (Evidence Benefits) | Respondida Plenamente | **T** (1.0) | Resumo (p. 2); Seção 4.1 a 4.4 (p. 15–28, Tabelas 5, 6 e 7) | Comprova qualitativamente a redução da sobrecarga cognitiva e da fadiga de alertas por meio de relatórios interpretáveis e acionáveis. Reporta amplo conjunto de métricas quantitativas: precisão do ensemble >99,8% em 11 classes de tráfego, F1-score por classe (recuperando a classe UDP Flood de 48% no MLP isolado para 95% no ensemble), latência fim a fim (2,9 a 11,6 s), consumo de tokens (média de 5.247 tokens/amostra maliciosa) e avaliação inédita de RAG com *LLM-as-Judge* atingindo Groundedness perfeito (1.0) e Faithfulness analítica (0.64). Evidência empírica sólida e replicável sobre o ACI IoT Network Dataset 2023. |
| **P87** | Chou et al. (2026) | **RQ4** (Challenges & Ethics) | Respondida Plenamente | **T** (1.0) | Seção 1 (p. 2–3); Seção 3.7.2 (p. 12–14); Seções 4.5 e 4.6 (p. 29–31) | Analisa exaustivamente desafios técnicos e riscos de governança: suscetibilidade a alucinações em domínios críticos, não-determinismo de modelos generativos, inferências cruzadas especulativas (sobre-síntese) e riscos de privacidade decorrentes do uso de APIs em nuvem pública (Groq, Tavily), inadequadas para redes *air-gapped*. Formaliza mecanismos de controle via verificação em nível atômico de alegações (*atomic claim decomposition*) com métricas de Faithfulness e Groundedness, preconizando supervisão humana mandatória antes da aplicação de contramedidas na rede. |
| **P87** | Chou et al. (2026) | **RQ5** (Research Gaps) | Respondida Plenamente | **T** (1.0) | Seções 4.5 e 4.6 (p. 29–31); Seção 5 (p. 31) | Mapeia lacunas cruciais de pesquisa: necessidade de estudos de ablação formais isolando as contribuições individuais do RAG e da injeção do SHAP; otimização da latência de ponta a ponta mediante caching de assinaturas, execução assíncrona de ferramentas e destilação de modelos locais; integração de explicabilidade nativa para arquiteturas neurais densas (como Integrated Gradients para MLP); avaliação em cenários *out-of-distribution* e ataques de dia zero (*zero-day* com protocolo *leave-one-class-out*); e adaptação para edge computing soberano e privado via quantização. |
| **TOTAL** | — | — | **SCORE_RQ** | **5.0 / 5.0** | — | **Cobertura Plena de todas as RQs da revisão.** |

---

## 5. Tabela C — Avaliação de Qualidade Metodológica QA (Critérios DARE / Tabela 7)

| ID | Tipo de Estudo | QA1 (Objetivos) | QA2 (Metodologia) | QA3 (Evidências) | QA4 (Conclusões) | SCORE_QA | Banda de Qualidade |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P87** | Estudo Experimental / Proposta Arquitetural | Y (1.0) | Y (1.0) | Y (1.0) | Y (1.0) | **4.0 / 4.0** | **Alta ($\ge 3.0$)** |

### Justificativas Detalhadas dos Critérios QA:
- **QA1 — Objetivos Claros (1.0):** Formulação clara da lacuna de pesquisa: a opacidade e a incapacidade de resposta acionável dos IDSs tradicionais frente a ataques complexos em ambientes IoT. A solução proposta articula de forma explícita a união de ensemble de aprendizado de máquina, atribuição de características por SHAP e um agente ReAct munido de RAG multiferramenta para geração de relatórios de incidentes.
- **QA2 — Metodologia Replicável (1.0):** Alto grau de detalhamento técnico e metodológico. Documenta diagrama de grafo, fluxo de dados, pipeline de pré-processamento estrito com prevenção de vazamento de dados (*data leakage*), hiperparâmetros completos das quatro redes/modelos (Tabelas A1–A4), parâmetros de busca no Optuna, formulação matemática das métricas, configurações completas do LLM (Llama-3.1-8b via Groq API), templates textuais dos prompts (Tabela 3) e *traces* integrais de execução para tráfego benigno e malicioso (Tabelas A5 e A6).
- **QA3 — Base de Evidências Sólidas (1.0):** Validação empírica de larga escala utilizando 1.170.570 instâncias de fluxo do ACI IoT Network Dataset 2023, divididas em 80% treino e 20% teste estratificado com validação cruzada em 10 *folds*. Avaliação quantitativa profunda contemplando acurácia, precisão, revocação, F1 macro e ponderado, tempos de inferência, custo de tokens e validação fática em 176 relatórios com RAGAs (*LLM-as-Judge*).
- **QA4 — Conclusões Coerentes (1.0):** Conclusões estritamente respaldadas pelos dados experimentais. Os autores analisam criticamente o equilíbrio entre Groundedness (1.0) e Faithfulness (0.64), justificam a necessidade do modelo assistivo com analista humano e dedicam seção exclusiva para delinear limitações estruturais (ausência de ablação do RAG, latência de ferramentas externas e dependência de serviços em nuvem).

---

## 6. Parecer Final do Revisor

### Síntese Crítica
O artigo **P87** apresenta alinhamento direto e aprofundado com o escopo da RSL sobre *Agentic AI Copilot para Resposta a Incidentes*. O trabalho não apenas propõe um pipeline multiagente funcional orquestrado em grafo (integrando pré-detecção leve em borda, ensemble de três classificadores, explicabilidade técnica via SHAP e agente ReAct com RAG multiferramenta), como também introduz um avanço metodológico indispensável para a governança de copilotos de segurança: a avaliação sistemática da fidelidade e fundamentação fática dos relatórios através de *LLM-as-Judge* e métricas RAGAs personalizadas (Groundedness e Faithfulness).

### Recomendação
**INCLUIR COM RESSALVAS**

**Justificativa:** O estudo atinge a pontuação máxima tanto no espectro de questões de pesquisa (**SCORE_RQ = 5.0 / 5.0**) quanto na avaliação de qualidade metodológica (**SCORE_QA = 4.0 / 4.0, Banda Alta**). A qualificação "Com Ressalvas" decorre estritamente da ausência de estudo de ablação isolado para demonstrar o ganho marginal específico da recuperação externa RAG frente ao conhecimento interno do LLM, além da necessidade protocolar de homologação dos índices bibliométricos externos.

### Pendências de Verificação Externa
1. **Contagem de Citações:** Verificar em bases indexadoras consolidadas (Scopus / Google Scholar) o atingimento do critério $\text{Citações} \ge 1$.
2. **SJR (Quartil):** Confirmar no Scimago Journal Rank a classificação do periódico no estrato Q1 ou Q2.
3. **Qualis CAPES:** Confirmar na Plataforma Sucupira o enquadramento do periódico no estrato A1 ou A2 para o quadriênio 2025–2028.