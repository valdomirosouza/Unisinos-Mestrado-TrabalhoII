# Avaliação do Estudo P35

## Identificação do estudo

**ID:** P35  
**Artigo:** *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps*  
**Autores:** Haodong Zou, Yichen Zhao, Xin Chen, Ling Wang, Jinghang Yu e Long Yuan  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas pelo artigo, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A2.

---

## Etapa 0 - Extração bibliométrica

### Tabela A - Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P35 | *Comput Mater Contin.*, v. 88, n. 1 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com framework LLM multiagente, fusão multimodal, cinco datasets, comparação com baselines, ablação, análise de robustez, custo e falhas | 10.32604/cmc.2026.077908 |

**Evidência bibliométrica:** a primeira página apresenta o veículo abreviado como *Comput Mater Contin.*, o volume 88, número 1, o ano de 2026 e o DOI. O artigo foi recebido em 19 de dezembro de 2025, aceito em 13 de março de 2026 e publicado em 8 de maio de 2026.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 - Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano >= 2020 | O artigo foi publicado em 8 de maio de 2026, p. 1. | Atendido |
| Publicação identificável | O PDF apresenta veículo, volume, número, ano e DOI, p. 1. | Atendido |
| Citações >= 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1-Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1-A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos três itens bibliométricos externos.

---

## Etapa 2 - Extração e classificação das RQs

### Tabela B - Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | RQ1 - Context Definitions | Parcialmente Respondida | P | Introdução, pp. 1-3; Seção 4, pp. 5-13; Figura 4, p. 11; Algoritmo 3, pp. 12-13. | O artigo caracteriza os agentes como entidades autônomas que percebem o Anomaly Fusion Graph, raciocinam e refinam iterativamente o diagnóstico em um ciclo Perceive-Reason-Act. As capacidades centrais incluem especialização de papéis, Chain-of-Thought, memória compartilhada, contexto acumulado, verificação adversarial, raciocínio contrafactual e backtracking. O modelo decisório é formalizado como um Sequential Decision-Making Process e um protocolo Investigate-and-Walk. Entretanto, não apresenta níveis formais de autonomia, supervisão humana, aprovação de decisões ou limites operacionais definidos por humanos. |
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | RQ2 - Engineering Architecture | Respondida Plenamente | T | Seção 4, pp. 5-13; Figuras 2 e 4, pp. 6 e 11; Algoritmos 1-3, pp. 8-13; Seção 5.1, pp. 14-15; Apêndice A, pp. 20-23. | A arquitetura combina duas camadas: construção do Anomaly Fusion Graph e raciocínio colaborativo multiagente. Quatro agentes especializados são orquestrados pelo Coordinator: Diagnoser, Navigator, Verifier e Coordinator. O ambiente utiliza métricas, logs, traces, Drain3, OpenTelemetry, Python 3.9 e OpenAI GPT-4 API. As capacidades avançadas incluem memória global compartilhada, Hypothesis Stack, resumo contextual, LLM arbitration, heurística por fault gradient, limites de profundidade, thresholds de confiança, validação por consenso, raciocínio contrafactual, detecção de inconsistências e backtracking dinâmico. |
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | RQ3 - Evidence Benefits | Respondida Plenamente | T | Seção 5, pp. 13-18; Tabelas 1-7; Figuras 5 e resultados experimentais. | O estudo apresenta benefícios qualitativos em redução da correlação manual, interpretação da propagação de falhas, transparência do diagnóstico e mitigação de alucinações. Em cinco datasets, o framework alcança F1 médio de 88,4%, superando DeepTraLog em 4,6 pontos percentuais e Direct LLM Diagnosis em 17 pontos. A associação log-trace alcança F1 médio de 97,5%. A validação por consenso melhora o F1 de 83,7% sem verificação para 89,1%. São medidos precisão, recall, F1, média, desvio-padrão, significância estatística, tempo, tokens, custo e frequência de arbitragem. O tempo médio total é 21,4 segundos por falha e o custo estimado é US$ 0,15 por falha. A evidência é experimental e diversificada, mas não mede MTTD, MTTR, carga cognitiva ou impacto em operações humanas reais. |
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | RQ4 - Challenges & Ethics | Parcialmente Respondida | P | Introdução, pp. 2-3; Seções 4.2 e 5.2.3-5.2.6, pp. 10-18; Tabelas 4, 6 e 7. | O artigo discute riscos técnicos relevantes: alucinações, causal confusion, ruído multimodal, limites de contexto, propagação ambígua, logs semanticamente pobres, topologias densas, aumento de latência, consumo de tokens e falhas com jargão específico. Os mecanismos de mitigação incluem grafo estruturado, thresholds, profundidade máxima, validação por consenso, Golden Signals, causal sufficiency, raciocínio contrafactual, críticas estruturadas e backtracking. Contudo, não aborda suficientemente accountability, privacidade, controle de acesso, segregação de privilégios, supervisão humana, auditoria institucional ou responsabilidade por diagnósticos incorretos em sistemas críticos. |
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | RQ5 - Research Gaps | Parcialmente Respondida | P | Seção 5.2.5-5.2.6, pp. 17-18; Tabelas 6-7; Conclusão, pp. 18-19. | O estudo identifica limitações concretas: propagação ambígua corresponde a 59% das falhas; logs insuficientes representam 28%; topologias com fan-out superior a 10 aproximam o backtracking de uma busca exaustiva; em 12% dos casos complexos do AIOps, mais de cinco iterações aumentam a latência em aproximadamente 40%; jargão de domínio e janelas inferiores a 10 ms prejudicam a arbitragem. Entretanto, a conclusão não apresenta uma agenda explícita de trabalhos futuros sobre benchmarking, governança, supervisão humana, implantação em produção ou redução de custo e latência. |
| P35 |  | **SCORE_RQ** | **3,5 / 5,0** | **P + T + T + P + P** |  | O estudo apresenta elevada aderência à arquitetura agêntica, observabilidade multimodal, RCA e avaliação experimental. As principais lacunas estão na definição de níveis de autonomia, na governança responsável, na ausência de avaliação com operadores humanos e na falta de uma agenda futura explicitamente formulada. |

### Observação sobre o nível de autonomia

O framework realiza de maneira autônoma a navegação pelo grafo, a avaliação dos nós, a formulação de hipóteses, a validação e o backtracking. A Figura 4 e o Algoritmo 3 demonstram um ciclo decisório estruturado entre agentes. Contudo, o PDF não define como operadores humanos acompanham, interrompem, aprovam ou contestam o diagnóstico. Assim, a autonomia é tecnicamente implementada, mas não é enquadrada por um modelo explícito de supervisão humana.

### Observação sobre o escopo de resposta a incidentes

O estudo cobre diretamente a etapa de diagnóstico e localização da causa raiz. Ele não gera nem executa ações de contenção, mitigação ou recuperação. Portanto, sua contribuição ao ciclo de incident response concentra-se na redução do espaço de investigação e na melhoria da qualidade diagnóstica, não na redução empiricamente comprovada de MTTR ou no fechamento autônomo do ciclo de remediação.

### Observação sobre custo e desempenho operacional

A fase multiagente consome, em média, 18,1 segundos, enquanto a construção do AFG consome 3,3 segundos, totalizando 21,4 segundos por falha. O consumo médio é de 9,7 mil tokens e o custo estimado é de US$ 0,15 por falha. No dataset AIOps, o tempo total chega a 26,6 segundos e o consumo a 12,3 mil tokens. Esses dados demonstram viabilidade experimental, mas também evidenciam um trade-off entre robustez, custo e velocidade.

---

## Etapa 3 - Avaliação de qualidade

### Tabela C - Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P35 | Estudo empírico experimental com framework LLM multiagente para RCA em AIOps | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 - Objetivos claros: Y (1,0).**  
O problema é explicitamente delimitado: a correlação manual de métricas, logs e traces é trabalhosa e sujeita a erros; métodos existentes apresentam alinhamento multimodal insuficiente; e LLMs isolados sofrem com alucinações e deficiência de raciocínio estrutural. A solução proposta combina um grafo multimodal com agentes especializados, validação adversarial e backtracking. Evidências: Resumo e Introdução, pp. 1-3.

**QA2 - Metodologia replicável: P (0,5).**  
O artigo descreve formalmente as modalidades, equações, algoritmos, arquitetura dos agentes, templates de prompts, hardware, Python 3.9, Drain3, OpenTelemetry, GPT-4 API, datasets, divisão 80/20, grid search, thresholds finais, profundidade máxima e métricas. Entretanto, o código-fonte não é disponibilizado no PDF, os dados são declarados indisponíveis por restrições de privacidade ou ética, e não são informados parâmetros completos da API, versão exata do modelo, temperatura, sementes ou configuração integral de detecção de anomalias. A replicação conceitual é viável, mas a reprodução fiel permanece limitada.

**QA3 - Base de evidências sólidas: Y (1,0).**  
A avaliação utiliza cinco datasets, diferentes escalas, dados multimodais, mais de 132 mil traces em um dos conjuntos, 400 falhas no AIOps Challenge e 45 cenários próprios no OpenTelemetry Demo. O estudo compara dois baselines, executa cinco repetições, apresenta média e desvio-padrão, aplica teste t pareado com p < 0,01, avalia alinhamento, robustez, ablação, tempo, custo e casos de falha. A evidência é ampla e diretamente relacionada a RCA.

**QA4 - Conclusões coerentes: Y (1,0).**  
A conclusão retoma a contribuição do AFG, dos agentes especializados, da validação adversarial e do backtracking, em consonância com os resultados. A Seção 5.2.6 discute falhas observadas, incluindo propagação ambígua, logs insuficientes, custo do backtracking e limitações da arbitragem. Embora não apresente trabalhos futuros explícitos, as conclusões permanecem sustentadas pelas evidências e as limitações são discutidas.

---

## Parecer final do revisor

O estudo apresenta forte aderência ao tema de Agentic AI aplicado a RCA em AIOps. Sua arquitetura multiagente possui memória compartilhada, papéis especializados, raciocínio iterativo, validação adversarial e backtracking, com avaliação quantitativa em cinco datasets. A contribuição concentra-se no diagnóstico, sem executar remediações ou avaliar operadores humanos.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada pela elevada aderência arquitetural e empírica às etapas de investigação e diagnóstico de incidentes. As ressalvas decorrem da ausência de contenção ou recuperação automática, da falta de métricas de MTTD, MTTR e carga cognitiva, da governança insuficiente, da indisponibilidade dos dados, do custo e latência do raciocínio multiagente e da ausência de uma agenda explícita de trabalhos futuros. O estudo deve ser utilizado como evidência de **RCA agêntica e robusta**, não como validação de um ciclo completo de resposta e recuperação.

### Pendências de verificação externa

1. **Número de citações >= 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1-Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1-A2:** verificar na Plataforma Sucupira / Qualis CAPES.
