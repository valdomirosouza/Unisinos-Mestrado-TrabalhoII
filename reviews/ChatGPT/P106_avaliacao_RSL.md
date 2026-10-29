# Parecer de avaliação integral — P106

**Estudo:** Sheth, A. et al. (2025). *Agentic AI for Autonomous Cyber Threat Hunting and Adaptive Defense in Dynamic Security Environments*. 2025 IEEE International Conference on Electro Information Technology (eIT). DOI: `10.1109/EIT64391.2025.11103697`.

**Decisão:** **Excluir (E2 — agência nominal, sem demonstração suficiente de intervenção agêntica).**

**Ressalva obrigatória de estrato:** série IEEE EIT, **B1**, percentil CiteScore/Scopus de **42%**, conforme informação de triagem fornecida e regras PDR-0006/PDR-0007. A classificação está fora de A1–A2. A ressalva permanece aplicável a qualquer uso secundário do estudo.

> **Limite documental:** o prompt menciona o PICOC “abaixo”, mas não explicita seus cinco componentes, e o arquivo `templates/review.md` não foi fornecido. Assim, a Tabela A apresenta um mapeamento analítico dos elementos PICOC a partir das RQs e do artigo, **sem pretender reconstruir os critérios normativos ausentes**. Da mesma forma, QA1–QA4 recebem definições operacionais transparentes neste parecer, pois seus enunciados não estão no prompt. A decisão E2 considera a sinalização explícita da triagem e as evidências do texto, sem presumir o conteúdo de precedentes não anexados.

## Tabela A — Identificação, bibliometria e PICOC

| Campo | Extração / julgamento | Evidência |
|---|---|---|
| Código | P106 | Prompt de avaliação |
| Título | Agentic AI for Autonomous Cyber Threat Hunting and Adaptive Defense in Dynamic Security Environments | p. 1 |
| Autoria | Adit Sheth; Advait Patel; Charit Upadhyay; Hariharan Ragothaman; Balkrishna Patil; Saai Krishnan Udayakumar | p. 1 |
| Ano e veículo | 2025; IEEE International Conference on Electro Information Technology (eIT) | p. 1 |
| DOI | 10.1109/EIT64391.2025.11103697 | p. 1 |
| Tipo de estudo | Artigo de conferência; proposta aplicada com avaliação quantitativa relatada | seções II–III, pp. 2–4 |
| Citações | OpenAlex **7**; Crossref **8**; Scopus **7**, consultas verificadas em 27/10/2026 segundo triagem; **não somar bases** | Prompt |
| Estrato | B1; percentil 42% da série IEEE EIT; SJR N/D | Prompt; PDR-0006/PDR-0007 |
| P — Population/Problem (mapeamento analítico) | Operações de segurança, caça a ameaças, detecção e mitigação de ataques em redes e ambientes organizacionais dinâmicos; não é um estudo diretamente centrado em SRE ou na carga cognitiva de técnicos de incident response | introdução p. 1; métodos p. 2 |
| I — Intervention (mapeamento analítico) | Classificadores CNN/RNN, Deep Reinforcement Learning e automação de monitoramento/detecção/resposta denominados “Agentic AI”; **não demonstra componentes e controle de uma arquitetura agêntica** | seção II, pp. 2–3 |
| C — Comparison (mapeamento analítico) | **Sim, comparação quantitativa relatada** com abordagem tradicional baseada em regras: resultados lado a lado para precisão, recall, F1, MTTD e MTTR. Baseline concreto é mencionado, mas sua implementação, configuração e paridade experimental não são suficientemente descritas | seção III, pp. 3–4, Tabela 1 |
| O — Outcomes (mapeamento analítico) | Accuracy 98,2%; precision 96,5%; recall 97,8%; F1 97,1%; MTTD 2,3 s; MTTR 5,1 s; FPR 1,8%; FNR 2,2%. **Carga cognitiva não medida** | seção III, pp. 3–4 |
| C — Context (mapeamento analítico) | SOC/cibersegurança, tráfego de rede e logs, dados CICIDS/DARPA e cenários de ataque simulados descritos; sem demonstração de implantação produtiva verificável | seções II–IV, pp. 2–4 |
| Triagem principal | **E2: agência nominal**, pois métodos automatizados não equivalem por si só a um agente com objetivos, planejamento, memória, ferramentas ou ciclo de decisão explicitado | seção II, pp. 2–3 |

## Tabela B — RQ1–RQ5

Escala determinada no prompt: **T = 1,0; P = 0,5; N = 0,0.** A classificação considera contribuição **à pergunta da RSL**, e não apenas presença de palavras-chave.

| RQ | Nota | Evidência âncora (seção/página) | Avaliação crítica |
|---|---:|---|---|
| **RQ1 — Definições e níveis de autonomia** | **N (0,0)** | Seção I.C, “Hypothesis”, p. 2: ação e decisão autônomas com intervenção manual mínima; seção II.B, p. 2 | Há alegação de autonomia, mas **não** definição operacional de agência, planejamento, memória, uso de ferramentas, limites decisórios ou supervisão humana. A afirmação genérica não responde à questão tal como formulada. |
| **RQ2 — Arquitetura e engenharia** | **P (0,5)** | Seção II.A–B, p. 2: CICIDS, DARPA, TensorFlow, PyTorch, CNN/RNN/DRL, logs, UEBA e automação de caça a ameaças | Apresenta blocos de uma pipeline de ML e monitoramento; faltam arquitetura de agentes, orquestração, armazenamento de estado/memória, guardrails, observabilidade do agente e especificações de operação em produção. Contribuição apenas periférica. |
| **RQ3 — Evidências e benefícios** | **T (1,0)** | Seção III.A–D, pp. 3–4; Tabela 1, p. 4 | Reporta comparação quantitativa com baseline baseado em regras, inclusive MTTD e MTTR, precisão, recall, F1 e erros. **O registro das métricas atende à RQ, mas sua credibilidade é limitada** pela caracterização insuficiente do baseline e do protocolo. Não mede esforço/carga cognitiva. |
| **RQ4 — Desafios, ética e governança** | **P (0,5)** | Seção IV.B, p. 4; seção V.C, p. 5 | Discute falsos positivos, fadiga de alertas, novos ataques, adversarial training, explicabilidade e accountability, mas sem avaliação sistemática de segurança, políticas, riscos de ações autônomas e responsabilidade operacional. |
| **RQ5 — Lacunas e agenda futura** | **P (0,5)** | Seção V.C, p. 5 | Propõe XAI, robustez/adversarial training e governança ética; não propõe de modo substancial benchmarks de agentes, observabilidade de decisões, protocolos de validação ou interação humano–agente. |
| **Total** | **2,5 / 5,0** | | **Aderência MÉDIA** (faixa 1,5–2,5), mas **não supera o critério excludente E2**. |

## Tabela C — QA1–QA4

**Nota metodológica:** o prompt especifica identificadores e pontuação, mas não os textos de QA1–QA4. Para evitar atribuição falsa ao protocolo original, os rótulos abaixo são **operacionalizações provisórias deste parecer**; a equivalência com o instrumento oficial depende da disponibilização da rubrica.

| QA operacionalizada | Nota | Evidência e justificativa |
|---|---:|---|
| **QA1 — Objetivos e escopo claros** | **Y (1,0)** | Introdução e hipótese, pp. 1–2: objetivo identificável de detecção/mitigação proativa por ML/DRL. A precisão de “Agentic AI”, contudo, é insuficiente. |
| **QA2 — Método e reprodutibilidade adequados** | **P (0,5)** | Métodos, pp. 2–3: conjuntos de dados, bibliotecas, pipeline geral e trecho de código. Faltam detalhes de modelos, hiperparâmetros, política/recompensa DRL, partições, seeds, volumes de dados e configuração experimental. Alega documentação GitHub, mas o trecho lido **não identifica uma URL verificável**. |
| **QA3 — Avaliação, baseline e medidas confiáveis** | **P (0,5)** | Seção III, pp. 3–4: medidas e baseline são relatados, mas faltam configuração de regras, definição das amostras e cargas, dispersão/incerteza, repetições e forma de aferição de tempos. A comparação é reportada, não suficientemente auditável. |
| **QA4 — Conclusões sustentadas e limitações reconhecidas** | **P (0,5)** | Discussão e conclusão, pp. 4–5: reconhece falsos positivos, robustez e XAI; extrapola a evidência ao afirmar capacidade de adaptação e benefício operacional sem demonstração detalhada de agentes em produção ou teste longitudinal. |
| **Total** | **2,5 / 4,0** | Qualidade **parcial**, com incerteza relevante sobre validade interna e reprodutibilidade. |

## Exame crítico dos resultados quantitativos

A **Tabela 1** (p. 4) informa:

| Métrica | IA proposta | Baseline baseado em regras |
|---|---:|---:|
| Accuracy | 98,2% | 85,7% |
| Precision | 96,5% | 78,3% |
| Recall | 97,8% | 82,4% |
| F1 | 97,1% | 80,2% |
| MTTD | 2,3 s | 15,7 min |
| MTTR | 5,1 s | 22,4 min |
| Taxa de falsos positivos | 1,8% | 14,3% |
| Taxa de falsos negativos | 2,2% | 17,6% |

1. **MTTD e MTTR:** a redução aproximada de **99,76%** no MTTD decorre de `2,3 / (15,7 × 60)`; a redução aproximada de **99,62%** no MTTR decorre de `5,1 / (22,4 × 60)`. São coerentes com os percentuais arredondados de **99,8%** e **99,6%** informados na seção III.B (p. 3). Não demonstram, por si, benefícios causados por agência de IA.
2. **Medição do ciclo de resposta:** o artigo não detalha claramente fronteiras temporais dos eventos, condição de encerramento da resposta, método de instrumentação, distribuição das observações ou incerteza das médias.
3. **Baseline:** o estudo traz **valores empíricos comparativos**, portanto é incorreto classificá-lo como “sem Comparison”; contudo não documenta adequadamente regras, ferramentas, tuning, hardware, bases e condições comparáveis.
4. **Possível vazamento de dados:** no trecho de código da seção II.C (p. 3), `StandardScaler().fit_transform(X)` antecede `train_test_split(...)`. Se essa ordem foi de fato utilizada na avaliação, o escalonamento incorpora informação estatística do conjunto de teste e compromete a independência da avaliação. O texto não permite garantir que o trecho represente todo o protocolo.
5. **Resultados zero-day:** a seção III.C (p. 3) afirma **92,6%** contra **34,8%** para ataques zero-day, mas não especifica claramente a composição de eventos inéditos, o procedimento de exclusão de famílias de ataque do treinamento nem as análises de generalização.
6. **Composição de métricas:** MTTD + MTTR, segundo as médias apresentadas, resulta em **7,4 s** para IA e **38,1 min** para baseline, como mencionado na seção III.D (p. 4). São **somas de médias**, não evidência independente de um ciclo end-to-end diretamente mensurado.
7. **Carga cognitiva/custos:** o artigo sugere menor trabalho humano e custo de SOC, mas não apresenta medida observacional de carga cognitiva, esforço dos analistas, custo financeiro ou satisfação operacional.

## Elegibilidade temática e distinção entre automação e agência

A contribuição descreve **modelos ML/CNN/RNN, DRL e implantação de “AI agents” para varredura e mitigação** (seção II.B, p. 2). O uso do termo *agent* e de aprendizado por reforço **não prova** a existência de um sistema de Agentic AI no sentido de autonomia orientada a objetivos com controle de ciclo de ação. Não são documentados de modo verificável: objetivos atribuídos a agentes, decomposição/planejamento de tarefas, política de invocação de ferramentas e seus resultados, memória/estado persistente, coordenação multiagente, guardrails e intervenção humana condicionada a risco.

Não se exige necessariamente **LLM** nem **multiagentes** para definir toda IA agêntica. O ponto decisivo é a **ausência de demonstração arquitetural e experimental suficiente de comportamento agêntico**. DRL poderia integrar um agente legítimo, mas o estudo não reporta o estado, espaço de ações, recompensa, estratégia aprendida ou ciclos de decisão de modo que a agência possa ser verificada.

Portanto, os tempos de detecção e mitigação têm utilidade **como referência contextual de automação de segurança**, não como evidência primária de um **copiloto agêntico** para resposta a incidentes. A evidência não demonstra a redução da carga cognitiva de técnicos nem governança de intervenção humano–agente.

## Validade, vieses e limites

- **Validade de constructo:** a designação “Agentic AI” não é alinhada a componentes operacionais de agência; autonomia equivale principalmente a classificação e mitigação automatizadas.
- **Validade interna:** baseline não suficientemente controlado ou especificado; ausência de intervalos de confiança/testes de significância; risco de vazamento na preparação dos dados mostrada.
- **Validade externa:** uso de datasets e cenários de ataque, sem evidência detalhada de implantação operacional e de desempenho em incidentes de produção.
- **Reprodutibilidade:** bibliotecas e datasets são nomeados, mas parâmetros, execução DRL, protocolo de teste e artefatos reproduzíveis não são fornecidos suficientemente no documento.
- **Risco de extrapolação:** benefícios de custo, redução de esforço humano, generalização para zero-day e autonomia em larga escala carecem de medições específicas.

## Síntese decisória

O artigo é **relevante para o domínio adjacente** de automação em SOC e traz métricas diretamente relacionadas a incident response. A comparação com mecanismos rule-based é **relatada e deve ser registrada** na extração. Ainda assim, o ponto fundamental não é o valor das métricas, mas a atribuição dessas métricas a uma arquitetura de agentes que **não é demonstrada**.

**Aplicação E2:** excluir da síntese primária sobre Agentic AI, por **agência nominal**. Pode ser citado, se permitido pelo protocolo, apenas como estudo contextual de ML/DRL em threat hunting, **nunca como comprovação de eficácia de um copiloto agêntico**.

**Ressalva de estrato obrigatória PDR-0006/PDR-0007:** conferência IEEE EIT, série classificada **B1**, percentil **42%** (dados fornecidos no prompt), fora do estrato A1–A2. **Todo uso residual da evidência requer explicitar essa ressalva.** A exclusão por E2 não depende do estrato.

## Recomendação final

**Excluir (E2 — agência nominal: o estudo apresenta CNN/RNN e Deep Reinforcement Learning com automação de detecção e resposta, mas não demonstra arquitetura, mecanismos ou comportamento suficientemente caracterizados de Agentic AI; ressalva de estrato obrigatória B1, PDR-0006/PDR-0007, em qualquer referência contextual).**
