# Avaliação do Estudo P27

## Identificação do estudo

**ID:** P27  
**Artigo:** *Leveraging Multi-Agent Framework for Root Cause Analysis*  
**Autores:** Feng Fu, Hong Ding, Yong Qin, Jian Yu e Dechao Xu  
**Framework avaliado:** MA-RCA (*Multi-Agent Root Cause Analysis*)  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF e na estrutura de avaliação fornecida no arquivo Markdown.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, ainda que o material de apoio informe Q1 e A1.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P27 | *Complex & Intelligent Systems*, v. 12, artigo 4 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com framework LLM multiagente, dois datasets, comparação com baselines, ablação e ilustração de implantação industrial | 10.1007/s40747-025-02096-0 |

**Observação sobre o ano:** o artigo foi publicado online em 6 de novembro de 2025, mas integra o volume bibliográfico de **2026**. Para a Tabela 3, foi adotado o ano da edição do periódico.

**Fontes para verificação externa:**

- **Citações:** Scopus, Web of Science, Dimensions ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | *Complex & Intelligent Systems* (2026), v. 12, artigo 4; publicação online em 6 de novembro de 2025, p. 1. | Atendido |
| Publicação identificável | Periódico, volume, artigo e DOI são apresentados na primeira página. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | RQ1 — Context Definitions | Respondida Plenamente | T | Introdução, pp. 1–3; “RCA Agent” e “Agent scheduling”, pp. 3–5; Figuras 1–2. | O artigo caracteriza um sistema com alto grau de autonomia operacional no diagnóstico: o RCA Agent interpreta a solicitação, coordena agentes especializados, constrói hipóteses e consolida evidências. As características centrais incluem decomposição de tarefas, memória externa por casos históricos, RAG, uso de ferramentas, validação dinâmica e interação com o SRE. O modelo decisório combina correspondência determinística de padrões, associação probabilística, recuperação semântica, verificação de hipóteses e síntese causal. Não há uma escala formal de níveis de autonomia, mas as três subdimensões são explicitamente cobertas. |
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seção “Method”, pp. 3–7; Figura 1; Algoritmos 1 e 2, pp. 5–6; “System illustration”, pp. 11–12. | MA-RCA adota arquitetura colaborativa com quatro agentes: RCA Agent, Retrieval Agent, Validation Agent e Report Agent. O ambiente inclui repositório histórico, espaço vetorial híbrido, grafo de conhecimento e caixa de ferramentas para logs, bancos de dados, traces e KPIs. Entre as capacidades avançadas estão orquestração dinâmica, recuperação híbrida, reranking, cache com TTL, deduplicação de consultas, priorização de ferramentas, checagem de completude da entrada, grounding e validação *tool-in-the-loop*. Esses mecanismos atuam como guardrails técnicos contra alucinação e propagação de erros. |
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seção “Evaluation”, pp. 7–11; Tabelas 3–6; “System illustration”, pp. 11–12. | O estudo apresenta benefícios qualitativos e quantitativos. No Nezha, MA-RCA alcança acurácia de 0,958 e F1 de 0,952; no conjunto de monitoramento de energia, acurácia de 0,843 e F1 de 0,828. O método supera CoT, RAG, RCACOPILOT, RCAgent e mABC. A ablação demonstra queda substancial sem o Retrieval Agent, o Validation Agent ou a arquitetura multiagente. Há ainda avaliação de diferentes LLMs e da quantidade de casos recuperados. A evidência combina benchmark cloud-native, dados do domínio de energia e integração como plug-in de diagnóstico. Contudo, não mede MTTD, MTTR, carga cognitiva ou redução de trabalho humano com um protocolo específico. |
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Introdução, pp. 1–3; “Validation Agent”, pp. 6–7; Conclusão, p. 12. | O artigo discute riscos técnicos importantes: alucinação, propagação de erros, troca excessiva de contexto, ruído na recuperação, dependência do repositório histórico e latência adicional de coleta e validação. Como mecanismos de mitigação, utiliza grounding, testes dinâmicos, checagem de entrada, filtragem por regras de domínio, evidências auditáveis e relatórios estruturados. Entretanto, não aprofunda accountability, privacidade, controle de acesso, responsabilização por diagnósticos incorretos, auditoria independente, aprovação humana ou governança institucional. |
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | RQ5 — Research Gaps | Respondida Plenamente | T | Conclusão, p. 12; Tabelas 4 e 6, pp. 10–11. | As limitações e direções futuras são explícitas. O desempenho depende da qualidade, atualidade e cobertura dos casos históricos, enquanto a coleta e a validação introduzem latência. Os autores propõem recuperação adaptativa, com determinação dinâmica do número e da relevância dos casos, além de execução especulativa e *prefetching* para paralelizar a coleta de evidências e reduzir o tempo do pipeline. |
| P27 |  | **SCORE_RQ** | **4,5 / 5,0** | **T + T + T + P + T** |  | O estudo apresenta elevada aderência às dimensões de autonomia, arquitetura, evidência e agenda futura. A principal lacuna está na governança responsável. O escopo também se concentra em diagnóstico e recomendação, sem execução autônoma das ações de remediação. |

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P27 | Estudo empírico experimental com framework LLM multiagente | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é apresentado de modo explícito: a análise manual não escala diante do crescimento da telemetria, enquanto agentes LLM de propósito geral sofrem com alucinação, troca de contexto e propagação de erros em raciocínios multietapas. A solução proposta é um framework multiagente com especialização, recuperação de conhecimento, validação por ferramentas e geração de relatórios. Evidências: Resumo e Introdução, pp. 1–3.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo detalha arquitetura, responsabilidades dos agentes, algoritmos de recuperação e validação, datasets, divisão estratificada 50/50, cinco baselines, métricas, ablações e estudos de sensibilidade. Também informa exemplos de tecnologias e mecanismos, como BERT, LSH, Prometheus, Modbus/TCP, cache TTL e diferentes LLMs. Porém, não apresenta código-fonte, prompts completos de todos os agentes, parâmetros de geração, configurações integrais dos modelos, ambiente de execução ou detalhes suficientes para reconstruir o dataset industrial. O conjunto Power Monitoring contém informação sensível e é disponibilizado apenas mediante solicitação. Assim, a replicação conceitual é possível, mas a reprodução fiel não está assegurada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A avaliação utiliza dois contextos distintos: Nezha, com OnlineBoutique e TrainTicket, e um conjunto proveniente de infraestrutura real de medição de energia. O estudo compara MA-RCA com cinco baselines, mede acurácia, precisão, recall e F1, executa ablação de quatro componentes, compara quatro LLMs e avalia diferentes quantidades de casos recuperados. As Figuras 3 e 4 também mostram a integração do “Diagnosis Agent” como plug-in em um sistema operacional de medição de energia. Evidências: pp. 7–12.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões derivam dos resultados comparativos e das ablações, que sustentam a contribuição da especialização dos agentes, do grounding histórico e da validação dinâmica. O artigo também reconhece limitações concretas relativas à qualidade do repositório e à latência adicional, relacionando-as diretamente às direções futuras propostas. Evidência: Conclusão, p. 12.

---

## Parecer final do revisor

O estudo apresenta forte aderência ao tema de Agentic AI como copiloto para diagnóstico de incidentes. MA-RCA combina orquestração multiagente, memória externa, RAG, ferramentas operacionais e validação de hipóteses para reduzir alucinações. A avaliação empírica é consistente e inclui comparação com baselines, ablação e aplicação em dois domínios. Entretanto, o framework permanece concentrado em RCA e recomendação, sem demonstrar execução autônoma de remediações ou benefícios humanos medidos diretamente.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada porque o estudo constitui evidência central para arquitetura e eficácia de agentes LLM especializados em RCA. As ressalvas decorrem da reprodutibilidade parcial, da ausência de métricas de MTTD, MTTR e carga cognitiva, da cobertura insuficiente de governança e do fato de a saída apoiar o SRE, mas não fechar autonomamente o ciclo de remediação. A permanência no corpus final também depende da confirmação dos critérios bibliométricos externos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
