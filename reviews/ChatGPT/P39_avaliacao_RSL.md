# Avaliação do Estudo P39

## Identificação do estudo

**ID:** P39  
**Artigo:** *Agentic AI and the Cyber Arms Race*  
**Autores:** Sean Oesch, Jack Hutchins, Phillipe Austria e Amul Chaulagain  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas pelo artigo, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q1 e Qualis A3.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P39 | *Computer*, coluna Cybertrust, IEEE Computer Society | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Artigo conceitual e prospectivo, com discussão técnico-geopolítica e ilustração baseada em pesquisa anterior dos autores | 10.1109/MC.2025.3544116 |

**Evidência bibliométrica:** a primeira página do PDF informa publicação na revista *Computer*, da IEEE Computer Society, DOI 10.1109/MC.2025.3544116 e data da versão corrente em 28 de abril de 2025. O cabeçalho da edição indica maio de 2025.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, IEEE Xplore, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | A versão corrente é datada de 28 de abril de 2025 e integra a edição de maio de 2025, pp. 1 e 4 do PDF. | Atendido |
| Publicação identificável | O PDF identifica o veículo *Computer*, a coluna Cybertrust, a IEEE Computer Society e o DOI, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado no próprio PDF um critério bibliométrico que permita encerrar a avaliação como inelegível. A extração prossegue, condicionada à confirmação externa dos três itens.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P39 | *Agentic AI and the Cyber Arms Race* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução, p. 1; descrição do agente CARL e dos agentes especializados, p. 2; seção “Implications for the Balance of Power in Cyberwarfare”, pp. 2–3. | O artigo caracteriza Agentic AI por autonomia, adaptação, delegação de tarefas, interação com ferramentas e coordenação hierárquica. O exemplo conceitual do CARL descreve um agente central de reinforcement learning controlando agentes especializados em engenharia reversa, logs, redes e descoberta de vulnerabilidades. O processo decisório envolve delegação e coevolução por retreinamento. Entretanto, não há taxonomia de níveis de autonomia, memória explícita, planejamento detalhado, reflexão, supervisão humana ou critérios formais de decisão. |
| P39 | *Agentic AI and the Cyber Arms Race* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Descrição do CARL, dos agentes especializados, das bibliotecas e ferramentas, p. 2; menção ao CrewAI, XBOW, RunSybil e Dropzone AI, p. 2. | O texto apresenta uma arquitetura hierárquica conceitual, com um agente central coordenando agentes de domínio e permitindo que eles utilizem bibliotecas e ferramentas existentes. Também menciona plataformas de orquestração multiagente e agentes especializados para pentest e triagem de alertas. Contudo, não especifica componentes de produção, memória, observabilidade, protocolos, guardrails, fallback, controle de acesso, segurança da orquestração ou detalhes de implantação reproduzíveis. |
| P39 | *Agentic AI and the Cyber Arms Race* | RQ3 — Evidence Benefits | Parcialmente Respondida | P | Introdução, p. 1; exemplos de XBOW e Dropzone AI, p. 2; Figura 1 e respectiva legenda, p. 3. | O artigo descreve benefícios qualitativos como escalabilidade, automação de tarefas repetitivas, análise rápida de código malicioso, triagem de alertas, pentest automatizado e adaptação entre agentes ofensivos e defensivos. Como evidência quantitativa secundária, informa que o XBOW encontrou e explorou vulnerabilidades em 75% de benchmarks de segurança web. A Figura 1 ilustra a coevolução entre agentes red e blue ao longo de episódios de treinamento. Entretanto, não apresenta experimento próprio detalhado, métricas de incident response, MTTD, MTTR, carga cognitiva ou avaliação sistemática de qualidade decisória. |
| P39 | *Agentic AI and the Cyber Arms Race* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seção “Implications for the Balance of Power in Cyberwarfare”, pp. 2–3; seção “Implications for Geopolitics”, pp. 3–4. | O artigo discute riscos técnicos e sociopolíticos relevantes: ataques adversariais contra agentes, comprometimento de robustez, proliferação de capacidades ofensivas, redução da barreira de entrada, assimetria entre ataque e defesa, dificuldade de atribuição, opacidade, velocidade das operações e risco de escalada. Também destaca ausência de transparência, supervisão e accountability. Contudo, não apresenta mecanismos concretos de governança, padrões de auditoria, human-in-the-loop, limites de autoridade, protocolos de interrupção ou controles técnicos para sistemas críticos. |
| P39 | *Agentic AI and the Cyber Arms Race* | RQ5 — Research Gaps | Parcialmente Respondida | P | Discussão sobre adaptação ofensiva e defensiva, p. 2; discussão sobre adversarial AI e robustez, p. 2; conclusão geopolítica, p. 4. | O texto aponta implicitamente lacunas relacionadas à robustez contra adversarial AI, velocidade de adaptação defensiva, atribuição, supervisão, accountability e controle da proliferação. Afirma que garantir a robustez dos agentes será essencial. Entretanto, não apresenta uma agenda sistemática de pesquisa, benchmarks, threat models, protocolos de avaliação, direções de observabilidade ou estudos futuros claramente delimitados. |
| P39 |  | **SCORE_RQ** | **2,5 / 5,0** | **P + P + P + P + P** |  | O estudo contribui como análise conceitual sobre autonomia, coordenação multiagente, riscos e impactos estratégicos. Sua aderência ao escopo da RSL é parcial, pois não avalia um copiloto de resposta a incidentes, não apresenta arquitetura operacional detalhada e não mede benefícios em ambientes reais. |

### Observação sobre a natureza do estudo

O artigo possui caráter predominantemente prospectivo e argumentativo. Ele apresenta cenários plausíveis, exemplos de mercado e uma ilustração de coevolução baseada em pesquisa anterior dos autores. Não descreve um protocolo experimental completo conduzido especificamente para este artigo.

### Observação sobre o escopo de incident response

A relação com resposta a incidentes aparece em exemplos de triagem de alertas, análise de código malicioso, contenção e adaptação defensiva. Entretanto, o foco principal está na corrida armamentista cibernética, no equilíbrio entre ofensiva e defesa e nas implicações geopolíticas. O texto não investiga processos de SRE, SOC, MTTD, MTTR, RCA, recuperação ou carga cognitiva com método empírico.

### Observação sobre a Figura 1

A Figura 1, na página 3 do PDF, mostra a evolução alternada de agentes red e blue em múltiplas rodadas de treinamento. A legenda afirma que os agentes aprendem a adaptar-se às mudanças de capacidade do adversário. Embora relevante para demonstrar coevolução, o artigo não fornece parâmetros, configuração do ambiente, número de repetições, incerteza estatística ou comparação com baselines.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P39 | Artigo conceitual e prospectivo sobre Agentic AI, cyberwarfare e geopolítica | Y (1,0) | N (0,0) | P (0,5) | P (0,5) | **2,0 / 4,0** | **Média** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O artigo declara explicitamente que examina as implicações da evolução de Agentic AI para cyberwarfare e política global. Também delimita o problema da proliferação de capacidades ofensivas e defensivas anteriormente restritas a atores com muitos recursos. Evidência: título, resumo introdutório e primeira página.

**QA2 — Metodologia replicável: N (0,0).**  
Não há seção metodológica, desenho experimental, amostragem, parâmetros, arquitetura implementada, protocolo de avaliação ou procedimento de análise que permita replicar o estudo. A Figura 1 deriva de pesquisa anterior e é apresentada sem detalhes suficientes de configuração e execução.

**QA3 — Base de evidências sólidas: P (0,5).**  
O texto utiliza exemplos concretos de agentes comerciais e apresenta uma figura de coevolução gerada no ambiente Cyberwheel, associada à pesquisa anterior dos autores. Contudo, a evidência não é estruturada como experimento completo deste artigo, não contém avaliação estatística e não examina diretamente resposta a incidentes. Assim, há sustentação ilustrativa, mas não uma base empírica robusta.

**QA4 — Conclusões coerentes: P (0,5).**  
As conclusões são coerentes com a argumentação sobre proliferação, assimetria, opacidade e risco de escalada. Entretanto, não há seção formal de limitações, ameaças à validade ou delimitação metodológica. Parte das afirmações permanece prospectiva e depende de analogias históricas e inferências sobre cenários futuros.

---

## Parecer final do revisor

O estudo apresenta relevância conceitual para compreender autonomia, coordenação multiagente, coevolução ofensiva e defensiva, adversarial AI e accountability. Contudo, sua contribuição para a RSL é indireta e predominantemente estratégica. Não há avaliação de um copiloto, experimento de incident response, mensuração operacional ou arquitetura de produção detalhada.

### Recomendação

**EXCLUIR DO CORPUS PRINCIPAL.**

A exclusão é recomendada porque o artigo é uma análise prospectiva sobre cyberwarfare e geopolítica, sem metodologia replicável e sem validação direta de Agentic AI como copiloto para resposta a incidentes. Além disso, o material de entrada informa Qualis A3, abaixo do critério A1–A2 da RSL, mas esse dado deve ser confirmado externamente antes de ser utilizado como motivo bibliométrico definitivo. O artigo pode ser mantido como referência contextual para riscos de proliferação, adversarial AI, atribuição e governança.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, IEEE Xplore, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES. O arquivo de instruções informa A3, o que, se confirmado, torna o estudo inelegível pelo critério da RSL.
