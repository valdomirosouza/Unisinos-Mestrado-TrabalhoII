# Avaliação do Estudo P21

## Identificação do estudo

**ID:** P21  
**Artigo:** *Small Language Model Agent for the Operations of Continuously Updating ICT Systems*  
**Autores:** Nobukazu Fukuda, Haruhisa Nozue e Haruo Oishi  
**Escopo da avaliação:** conteúdo exclusivamente presente no PDF fornecido.

> **Nota metodológica:** o número de citações, o quartil SJR e o estrato Qualis não são verificáveis no PDF. Embora o arquivo de instruções informe SJR Q1 e Qualis A1, esses dados permanecem como **[VERIFICAR]**, em conformidade com a regra antifabricação.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P21 | IEEE Access, Volume 13 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com avaliação por benchmarks sintético e operacional | 10.1109/ACCESS.2025.3544637 |

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
| Ano ≥ 2020 | O cabeçalho registra publicação em 24 de fevereiro de 2025, p. 1 do PDF. | Atendido |
| Publicação identificável | IEEE Access, Volume 13, p. 1 do PDF. | Atendido |
| Citações ≥ 1 | A contagem de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR do periódico não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. Assim, a extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | RQ1 — Context Definitions | Parcialmente Respondida | P | Introdução, pp. 1–3 do PDF; Seção III, pp. 3–4; Figuras 1 e 2, p. 2. | O artigo define o agente como uma entidade que recebe um objetivo do operador e interage autonomamente com o ambiente em ciclos de ação, observação e planejamento. Também formaliza a decisão como uma política condicionada pela trajetória atual e por trajetórias anteriores. Há planejamento hierárquico, recuperação de experiências e uso de scripts. Contudo, não estabelece níveis de autonomia nem descreve supervisão humana contínua, aprovação de ações ou mecanismos de intervenção durante a execução. |
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seção IV, pp. 4–6; Algoritmos 1–3, pp. 5–6; Figuras 3 e 4, pp. 4–5; Seção V.C, p. 7. | A arquitetura é descrita em detalhes: agente SLM conectado ao ambiente, memória de trajetórias decompostas em blocos, recuperação por similaridade, seleção de exemplares, reconfiguração dinâmica do prompt e execução de scripts. O estudo informa Python, expressões regulares para parsing, SentenceTransformer `all-mpnet-base-v2`, GPU NVIDIA GeForce 2080 Ti e os modelos LLaMA2, Gemma2 e Mistral. Como guardrail, ações sem similaridade suficiente com os exemplares são bloqueadas. Observabilidade operacional do agente não é desenvolvida, mas as três subdimensões da RQ possuem cobertura explícita. |
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | RQ3 — Evidence Benefits | Parcialmente Respondida | P | Seção V, pp. 7–10; Figuras 6–11, pp. 7–10. | O estudo reporta evidências quantitativas robustas de qualidade decisória. No ALFWorld, o método com LLaMA2 alcança 96,3% de sucesso, superando os resultados reportados de ReAct com GPT-4, 85,8%, e RAP com GPT-4, 94,8%. No WideEnet, o melhor resultado é 88,9% com Mistral, e o LLaMA2 melhora de 3,70% para 87,0%. Após três atualizações, trajetórias recentes elevam o sucesso de 29,4% para 78,8%. O custo é maior: em média, 2,1 vezes mais chamadas ao modelo do que ReAct. Entretanto, não são medidos MTTD, MTTR, tempo real de resposta a incidentes, redução efetiva da carga cognitiva ou resultados em incidentes reais. |
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Introdução, p. 2; Seção IV.B-IV, p. 6; Seção V.D, pp. 9–10; Seção VI, p. 10. | O artigo discute alucinações, operações incorretas em produção, raciocínio por atalho, falhas de formato, confidencialidade, custo computacional, dependência de trajetórias completas e dificuldade de adaptação a situações não cobertas. Os mecanismos de controle incluem políticas operacionais predefinidas, seleção de trajetórias recentes, bloqueio de comandos não compatíveis com exemplares e teste de verificação antes da produção. Contudo, não desenvolve accountability, responsabilidade por danos, auditoria, segregação de privilégios, explicabilidade para operadores ou governança institucional. |
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção V.D, p. 10; Seção VI, p. 10 do PDF. | As lacunas são explícitas: incapacidade de tratar situações ausentes das trajetórias, custo da anotação manual de pensamentos e tags, dificuldade de extrair procedimentos de documentos multimodais, necessidade de ambientes interativos de verificação com menor custo e necessidade de técnicas adicionais para evitar saídas malformadas. Como direções futuras, os autores propõem extração automática de trajetórias e construção mais econômica de ambientes de validação. |
| P21 |  | **SCORE_RQ** | **3,5 / 5,0** | **P + T + P + P + T** |  | O estudo oferece forte contribuição arquitetural, experimental e operacional. Sua aderência ao escopo da RSL é elevada, embora as evidências estejam concentradas em execução de procedimentos de rede e não em resposta a incidentes reais ou em métricas clássicas como MTTD, MTTR e carga cognitiva. |

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P21 | Estudo empírico experimental com benchmark público e ambiente operacional baseado em rede comercial | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é apresentado de forma explícita: operações de sistemas ICT exigem conhecimento especializado, acompanham atualizações frequentes e não toleram ações incorretas decorrentes de alucinações. O artigo também explicita as restrições de custo e confidencialidade dos LLMs proprietários. A solução proposta combina SLM, pensamentos aninhados, decomposição de trajetórias, recuperação de blocos e reconfiguração dinâmica de prompts. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: P (0,5).**  
A arquitetura, a formulação do problema, os Algoritmos 1–3, a estratégia de recuperação, os modelos, o hardware, o modelo de embeddings, os benchmarks e o número de exemplares são descritos. Entretanto, o valor de `safety_threshold`, parâmetros completos de inferência e quantização, sementes, código-fonte, artefatos do WideEnet e detalhes suficientes para reconstruir o ambiente confidencial não são fornecidos. A replicação conceitual é possível, mas uma reprodução fiel dos resultados não está assegurada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A validação utiliza dois ambientes. O ALFWorld contém 134 configurações em seis tipos de tarefa. O WideEnet utiliza sete tipos de procedimentos extraídos de manuais, 34 trajetórias como exemplares e 85 configurações de teste. Há comparação com Act, ReAct e RAP, avaliação com três SLMs, análise por tarefa, experimento de seleção de exemplares, adaptação a atualizações e medição de sobrecarga computacional. Evidências: Seção V e Figuras 6–11, pp. 7–10.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões refletem os resultados de taxa de sucesso, adaptação a atualizações e custo computacional. Os autores reconhecem limitações relevantes, incluindo a dependência da cobertura das trajetórias, o custo de prepará-las, a incapacidade de eliminar todas as saídas incorretas e a dificuldade de construir ambientes interativos para validação prévia. Evidência: Seções V.D e VI, pp. 9–10.

---

## Parecer final do revisor

O estudo apresenta elevada aderência ao tema de Agentic AI aplicado à operação de sistemas ICT. Sua contribuição central é uma arquitetura de agente baseada em SLM capaz de planejar e executar sequências de ações em ambientes que mudam continuamente, com memória por trajetórias, recuperação contextual e um mecanismo preventivo de bloqueio de comandos. A avaliação experimental é ampla e inclui um benchmark público e um cenário operacional de redes. A relação com resposta a incidentes é relevante, mas indireta, pois os experimentos se concentram em procedimentos operacionais e atualização de políticas, sem medir incidentes reais, MTTD, MTTR ou carga cognitiva.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada pela qualidade metodológica, pela arquitetura detalhada e pelas evidências quantitativas em operações de ICT, incluindo tarefas longas, ramificadas e sujeitas a atualização. As ressalvas decorrem da ausência de avaliação direta em resposta a incidentes, da falta de métricas humanas e operacionais centrais à RSL e da cobertura limitada de governança e accountability. A inclusão definitiva também depende da confirmação dos critérios bibliométricos externos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
