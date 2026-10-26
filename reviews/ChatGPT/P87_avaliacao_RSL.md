# Avaliação do artigo P87

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura — Ciclo 2  
**ID:** P87  
**Título:** *An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense*  
**Autores:** Chia-Hong Chou, Arjun Sudheer e Younghee Park  
**Fonte da avaliação:** exclusivamente o PDF fornecido, conforme `prompt-P87.md`.  
**Critérios de avaliação:** rubrica de RQs e QA1–QA4 estabelecida no prompt, inspirada na lógica DARE/Kitchenham.

## Etapa 0 — Tabela A: Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P87 | *Journal of Sensor and Actuator Networks* | 2026 | [VERIFICAR] | [VERIFICAR] (Q2 informado no prompt) | [VERIFICAR] (A1 informado no prompt) | Pesquisa aplicada experimental; proposição e avaliação de arquitetura multiagente de IDS e relatórios de incidentes | https://doi.org/10.3390/jsan15020032 |

**Evidência bibliográfica:** primeira página: título, autores, identificação do periódico (*J. Sens. Actuator Netw.* 2026, 15, 32), publicação em 7 de abril de 2026 e DOI. Natureza experimental: seções 3 (*Methodology*) e 4 (*Results*).

> **Nota de rastreabilidade:** Q2 e A1 são metadados fornecidos no prompt de triagem, não comprovados pelo PDF. Por exigência de verificação independente, os campos permanecem `[VERIFICAR]`. Também não há no PDF contagem bibliométrica de citações recebidas pelo artigo.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / pendência |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicado em 2026; p. 1. |
| Veículo de publicação identificável | Atendido | *Journal of Sensor and Actuator Networks*; p. 1. |
| Citações ≥ 1 | [VERIFICAR] | Contagem de citações recebidas pelo artigo não consta no PDF; verificar em base indexadora, como Scopus. Por ser uma publicação de 2026, não presumir que já possui citação. |
| SJR Q1–Q2 | [VERIFICAR] | Q2 informado no prompt; verificar no *SCImago Journal Rank*, para periódico e ano aplicáveis. |
| Qualis A1–A2 | [VERIFICAR] | A1 informado no prompt como derivação de percentil; confirmar na Plataforma Sucupira / Qualis CAPES e no enquadramento aplicável à área e período. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis)**. A avaliação de conteúdo prossegue porque a rubrica permite extrair candidatos pendentes. Aprovação anterior na triagem temática não substitui a confirmação bibliométrica.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P87 | Chou et al. (2026) | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | §3.1, pp. 6–8; §3.6, pp. 10–11; §4.5, pp. 28–29 | **a) Autonomia:** há execução condicional e agente ReAct com chamadas de ferramentas; autonomia operacional delimitada a busca e redação, não à efetivação de mitigação. **b) Características:** estado compartilhado, busca externa e memória interna em Chroma DB são explícitos. **c) Decisão:** decisão por classificador/ensemble e síntese pelo LLM, com recomendação de revisão humana, mas sem modelo sistemático de níveis de autonomia ou de colaboração decisória humano–agente. |
| P87 | Chou et al. (2026) | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | §3.1, pp. 6–8, Fig. 1; §3.5, p. 9, Fig. 2; §3.6, pp. 10–11, Tabela 2; §3.7.2, pp. 11–14; §4.6, pp. 29–30 | **a) Arquitetura:** pipeline gráfico de três fases, com early exit, ensemble e agente ReAct. **b) Ferramentas:** LangGraph, Groq/Llama-3.1-8b-instant, Tavily, arXiv, Chroma DB, SHAP, RAGAs. **c) Capacidades:** ferramentas, busca, memória, citações e restrições de prompt. Entretanto, observabilidade operacional, controles de autorização, governança de ferramentas, resiliência e implantação produtiva não são suficientemente detalhados. |
| P87 | Chou et al. (2026) | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | §4.1, pp. 14–16; §4.2, pp. 17–22; §4.3, p. 23, Tabela 7; §4.4, p. 28; §4.6, pp. 29–30 | **a) Benefícios qualitativos:** relatórios explicáveis e sugestões de mitigação para apoiar analistas são apresentados como capacidades, não como ganhos humanos demonstrados. **b) Métricas:** pré-detecção com acurácia de 99,49%; ensemble com cerca de 99,8%; groundedness 1,0000; faithfulness 0,6391; 2,9–11,6 s por amostra maliciosa. **c) Evidência:** experimento quantitativo em dados de benchmark e avaliação automatizada de 176 relatórios; não há experimento com analistas, medidas de MTTD/MTTR/carga cognitiva, nem ablation do LLM/RAG. Assim, o impacto operacional da copilotagem permanece não comprovado. |
| P87 | Chou et al. (2026) | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | §3.7.2, pp. 11–14; §4.5, pp. 28–29; §4.6, pp. 29–30 | **a) Desafios técnicos:** latência, alucinações/atribuição indevida de evidências, generalização a zero-day, explicabilidade parcial do MLP, dependência de APIs e privacidade. **b) Governança/ética:** riscos de impacto operacional e exposição de dados são reconhecidos, sem análise formal de accountability, conformidade ou responsabilidade. **c) Mitigações:** evidências recuperadas, prompt restritivo, métricas de groundedness/faithfulness e recomendação explícita de *human-in-the-loop*; faltam mecanismos robustos demonstrados de auditoria, aprovação de ações e controle de acesso. |
| P87 | Chou et al. (2026) | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | §4.6, pp. 29–30; §4.5, pp. 28–29 | A seção de limitações explicita agenda verificável: ablation isolada de SHAP e de RAG; benchmark com baseline sem recuperação; detecção de ataques não vistos por *leave-one-class-out*; alternativas de explicabilidade para MLP; caching, destilação e chamadas assíncronas contra latência; implantação local sensível à privacidade; refinamento de recuperação e faithfulness. |
| **P87** | **Total** | **SCORE_RQ** | **3,0 / 5,0** | **P + P + P + P + T** | **§§3–4.6** | **Cobertura especialmente forte em implementação técnica e lacunas futuras, porém parcial quanto ao impacto humano e à governança de produção.** |

### Distinções importantes na leitura dos resultados

- Os **99,49%** referem-se à classificação binária de pré-detecção, enquanto os **99,80%** referem-se ao ensemble multiclasse; não se deve atribuir ambos à mesma tarefa (§4, pp. 14 e seguintes).
- A avaliação RAG compreende **176 casos válidos de 200 tentativas**, após exclusão de **24 erros** (§4.3, p. 23), o que limita a interpretação da cobertura dos resultados.
- **Groundedness = 1,0000** decorre da métrica operacionalizada por um juiz LLM, aceitando apoio parcial (escore ≥ 1) em nível de sentença; não equivale a uma auditoria independente de veracidade nem à demonstração de ausência absoluta de alucinações (§3.7.2, pp. 12–13; §4.3, p. 23).
- **Faithfulness = 0,6391** mede a fração de afirmações atômicas plenamente sustentadas (escore 2), distinta de groundedness (§3.7.2, pp. 12–13). O mesmo modelo Llama-3.1-8b-instant é indicado como juiz e gerador (§3.6 e §3.7.2), sem validação humana independente de qualidade relatada no experimento principal.
- A contribuição do RAG e do SHAP à qualidade final não foi isolada em estudos de ablação; os próprios autores destacam essa ausência (§4.6, pp. 29–30).

## Etapa 3 — Tabela C: Avaliação de Qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P87 | Pesquisa aplicada experimental; framework multiagente para IDS e geração de relatórios | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

**QA1 — Objetivos Claros: Y (1,0).** O artigo delimita o problema da falta de interpretabilidade e de relatórios acionáveis nos IDS e propõe solução multiagente baseada em classificação, SHAP e RAG. **Evidências:** resumo e §1, pp. 1–3; §3.1, p. 6.

**QA2 — Metodologia Replicável: P (0,5).** São fornecidos dataset, pipeline, pré-processamento, divisão treino/teste, validação cruzada, ferramentas, configuração do LLM, critérios do juiz e arquiteturas dos modelos; Figuras 1–2, Tabelas 2–3 e Apêndice A ampliam a rastreabilidade. A replicação integral da etapa de recuperação e geração, porém, depende de conteúdos externos mutáveis, da base interna e de decisões de orquestração não integralmente especificadas; faltam comparações ablativas. **Evidências:** §§3.1–3.7, pp. 6–14; Apêndice A; §4.6, pp. 29–30.

**QA3 — Base de Evidências Sólidas: Y (1,0).** Há validação empírica quantitativa do classificador binário, do ensemble, da latência e da geração RAG, inclusive métricas e gráficos. Isso satisfaz o critério da rubrica para evidências experimentais, **sem** demonstrar causalmente benefício do RAG, redução da carga cognitiva ou eficácia com equipes de resposta. **Evidências:** §4.1–§4.4, pp. 14–28; Tabela 7 do artigo, p. 23.

**QA4 — Conclusões Coerentes: Y (1,0).** Os autores relacionam suas conclusões aos resultados experimentais e explicitam limitações importantes, incluindo latência, privacidade, generalização a ameaças inéditas e ausência de ablations de RAG/SHAP. O argumento de benefício aos analistas deve, contudo, ser entendido como potencial de apoio, não como impacto operacional empiricamente comprovado. **Evidências:** §§4.5–4.6, pp. 28–30; §5, p. 30 e seguintes.

## Parecer final do revisor

**Síntese:** O estudo P87 é diretamente relevante à RSL ao combinar orquestração agêntica, detecção de incidentes de rede, explicabilidade SHAP e geração de relatórios fundamentados em contexto recuperado. A arquitetura é descrita com detalhe e submetida a experimentos quantitativos. Sua contribuição principal está na integração técnica entre detecção e elaboração de relatórios orientados a analistas. A ausência de estudos ablativos e de avaliação humana impede concluir que o agente reduza efetivamente MTTD, MTTR ou carga cognitiva no SOC/SRE. Os riscos de implantação real, autonomia e governança são reconhecidos, mas apenas parcialmente resolvidos.

**Recomendação: INCLUIR COM RESSALVAS**, **condicionada à confirmação dos critérios bibliométricos de elegibilidade**. O artigo oferece evidência útil sobre **arquitetura de copilotagem agêntica para análise e documentação de incidentes de segurança de rede**, não sobre resposta autônoma com execução de remediações ou ganhos operacionais humanos medidos. A pontuação de qualidade metodológica é **3,5/4,0 (Alta)** e a cobertura das RQs é **3,0/5,0**.

**Ressalvas essenciais para a síntese da RSL:** (1) não confundir a acurácia dos classificadores com qualidade ou benefício causado pelo agente; (2) ausência de ablation de LLM/RAG e SHAP; (3) não extrapolar groundedness perfeita para ausência garantida de alucinações; (4) ausência de mensuração empírica de tempo de resposta humano, MTTD, MTTR ou carga operacional; (5) avaliação em um único dataset conhecido, sem demonstração de capacidade zero-day ou de implantação real; (6) necessidade de supervisão humana dos relatórios.

**Pendências de verificação externa:**

1. **Citações recebidas ≥ 1:** confirmar em base indexadora, como Scopus; não consta no PDF.
2. **SJR Q1–Q2:** confirmar no *SCImago Journal Rank* o quartil do periódico para a edição/ano pertinente; Q2 foi apenas informado no prompt.
3. **Qualis A1–A2:** confirmar na Plataforma Sucupira / Qualis CAPES o enquadramento válido na área e no período; A1 derivado de percentil não é tratado como fato documental verificado.

**Decisão de inclusão no corpus:** **provisória**, até o fechamento das pendências; se algum critério obrigatório não for satisfeito, rever a elegibilidade antes da inclusão definitiva.
