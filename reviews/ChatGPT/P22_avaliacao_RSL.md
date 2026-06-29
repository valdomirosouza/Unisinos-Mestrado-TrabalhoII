# Avaliação do Estudo P22

## Identificação do estudo

**ID:** P22  
**Artigo:** *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control*  
**Autores:** Vasilis Avgerinos, Kostas Ramantas, Luis Alonso e Christos Verikoukis  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Embora o arquivo de instruções informe SJR Q1 e Qualis A1, esses campos permanecem como **[VERIFICAR]**, em conformidade com as regras antifabricação.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P22 | IEEE Internet of Things Journal, v. 13, n. 9 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico experimental com protótipo e injeção controlada de falhas | 10.1109/JIOT.2025.3648858 |

**Observação sobre o ano:** o artigo foi publicado antecipadamente em 26 de dezembro de 2025, mas integra a edição de 1º de maio de 2026 do periódico. Para a Tabela 3, foi adotado o ano bibliográfico da edição, **2026**.

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
| Ano ≥ 2020 | Edição de 1º de maio de 2026; publicação antecipada em 26 de dezembro de 2025, p. 1 do PDF. | Atendido |
| Publicação identificável | IEEE Internet of Things Journal, v. 13, n. 9, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à verificação externa dos três critérios bibliométricos pendentes.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | RQ1 — Context Definitions | Respondida Plenamente | T | Introdução, pp. 1–2; Seção III.D, p. 3; Seção IV.A–C, pp. 3–5; Figura 1, p. 4. | O artigo caracteriza autonomia como a capacidade de detectar violações de SLA, investigar causas e executar ações corretivas sem intervenção humana obrigatória. As características centrais incluem planejamento, contexto acumulado com decisões anteriores, uso de ferramentas, reflexão após cada chamada, replanejamento e validação pós-ação. O modelo decisório é um ciclo fechado inspirado em ReAct, com planejamento, seleção de ferramentas, execução, integração de evidências e término condicionado à recuperação ou a um limite de rodadas. Fluxos de aprovação humana podem ser configurados por ferramenta, embora não haja uma taxonomia formal de níveis de autonomia. |
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seção III.C–D, p. 3; Seção IV.A–C, pp. 3–5; Figura 1 e Tabela I, p. 4; Seção V.A, p. 5. | A arquitetura de produção é descrita como um agente único em ciclo fechado, integrado a monitoramento Prometheus, Kubernetes/k3s, Grafana e um servidor MCP. A camada de ferramentas inclui planejamento, coleta de métricas e topologia, aplicação de comandos Kubernetes e espera para estabilização. Entre os mecanismos avançados estão cache temporal, filtragem de chamadas repetidas, saídas tipadas, tratamento de erros, critérios de conclusão, replanejamento obrigatório, validação posterior, restrições no prompt e aprovação humana configurável para ações críticas. |
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Resumo, p. 1; Seção V, pp. 5–7; Seção VI, pp. 7–9; Tabelas IV e V, pp. 7–8; Figuras 3 e 4, pp. 8–9. | O artigo apresenta benefícios qualitativos e quantitativos diretamente relacionados ao ciclo de incidentes: identificação de falhas, RCA, seleção de mitigação, execução e validação. O resumo reporta 52,9% de acurácia de identificação e 70,7% de mitigação bem-sucedida. Na análise por aplicação, o agente GPT-5 obtém acurácia entre 80,0% e 87,5% e sucesso de remediação entre 80,0% e 90,0%. Também são medidos rodadas de decisão, tempo de resolução, recuperação de latência, uso de ferramentas e retorno de métricas à linha de base. A evidência decorre de 60 cenários controlados de falha em três aplicações IoT. Não há, porém, mensuração de carga cognitiva humana. |
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seção IV.B–C, pp. 4–5; Seção VI.A–D, pp. 7–9; Seção VII, p. 9. | O estudo cobre riscos técnicos relevantes: ações incorretas, necessidade de evidências antes da intervenção, custo de contexto, latência de remediação, sensibilidade do modelo menor, limitações físicas de recursos e riscos de ações disruptivas. Os mecanismos de governança incluem acesso encapsulado por MCP, conformidade por política, aprovação humana configurável, rastreabilidade de planos e resumos, critérios de conclusão e validação pós-ação. Entretanto, questões éticas mais amplas, responsabilização organizacional, privacidade, segurança do MCP, segregação de privilégios, auditoria independente e gestão formal de responsabilidade não são aprofundadas. |
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção II.C, p. 3; Seção VI.B, p. 8; Seção VII, p. 9. | O artigo identifica como lacuna a predominância de trabalhos focados apenas em diagnóstico, sem mitigação autônoma. Também aponta limitações de escalabilidade, segurança, tamanho de contexto, desempenho de modelos menores, variedade de ferramentas e realismo do ambiente experimental. As direções futuras incluem compressão de contexto, arquiteturas mais profundas, integração com técnicas de detecção baseadas em ML, ajuste fino de modelos menores, formalização de salvaguardas e avaliação em testbeds IoT maiores e mais heterogêneos. |
| P22 |  | **SCORE_RQ** | **4,5 / 5,0** | **T + T + T + P + T** |  | O estudo apresenta aderência muito alta ao escopo da RSL, pois cobre o ciclo de detecção, RCA, mitigação e validação de incidentes com arquitetura agêntica operacional e evidência quantitativa. A principal lacuna está na governança responsável e na ausência de métricas sobre carga cognitiva e interação humana. |

### Observação sobre as métricas reportadas

O PDF apresenta diferentes agregações de desempenho. O resumo informa **52,9% de acurácia** e **70,7% de mitigação**, enquanto a Tabela V e a conclusão destacam resultados superiores do agente baseado em GPT-5 por aplicação. O estudo não explicita de forma suficiente, nos trechos apresentados, como essas agregações se relacionam. Por isso, os valores foram preservados conforme seus respectivos contextos, sem tentativa de reconciliação por inferência.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P22 | Estudo empírico experimental com protótipo, benchmark reproduzível e injeção de falhas | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitado como a inviabilidade crescente da gestão manual e a insuficiência de automações estáticas em ambientes cloud–edge e IoT. A solução também é clara: um agente LLM em ciclo fechado para identificar causas, executar mitigação e validar a recuperação de violações de SLA. Evidências: Resumo e Introdução, pp. 1–2.

**QA2 — Metodologia replicável: P (0,5).**  
O estudo descreve arquitetura, ferramentas, categorias de chamadas, topologia do cluster, recursos de hardware virtualizados, k3s, QEMU, Prometheus, Grafana, aplicações, tipos de falha, quantidade de experimentos, protocolo em quatro fases e critérios matemáticos de sucesso. Contudo, o prompt completo não é disponibilizado, pois o próprio artigo afirma que a lógica integral é extensa demais para apresentação. Também não são informados todos os parâmetros dos modelos, temperatura, versão exata de API, sementes, código-fonte ou artefatos completos do experimento. A replicação conceitual é viável, mas a reprodução fiel permanece limitada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
A avaliação inclui três aplicações com 3, 8 e 12 microserviços, sete nós distribuídos entre nuvem, borda e gestão, 60 cenários de falha, anomalias em pods e nós, comparação entre GPT-5 e GPT-5-mini e métricas de identificação, sucesso, latência recuperada, rodadas, tempo e uso de ferramentas. O protocolo de reset, baseline, injeção e recuperação reduz interferências e favorece repetibilidade. Evidências: Seção V e Seção VI, pp. 5–9.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões refletem os resultados de recuperação, acurácia, tempo de resolução e diferença entre modelos. O artigo reconhece limitações de tempo, escalabilidade, segurança, tamanho de contexto, modelos menores e distância de ambientes reais. Há uma ambiguidade na relação entre os números agregados do resumo e os resultados destacados na conclusão, mas as conclusões principais permanecem sustentadas pelas tabelas e análises experimentais. Evidência: Seção VII, p. 9.

---

## Parecer final do revisor

O estudo possui forte aderência ao tema de Agentic AI como copiloto ou executor no ciclo de resposta a incidentes. A arquitetura fecha o ciclo entre observabilidade, detecção de violação, RCA, planejamento, atuação e validação, utilizando ferramentas reais de Kubernetes e Prometheus. A evidência experimental é ampla para um protótipo e inclui métricas diretamente relacionadas à qualidade da decisão e ao tempo de recuperação. As principais limitações estão no uso de ambiente emulado, na ausência de avaliação com operadores humanos e na cobertura ainda parcial de governança e segurança de ações autônomas.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é fortemente recomendada porque o artigo contribui diretamente para RQ1, RQ2, RQ3 e RQ5 e apresenta um dos casos mais completos de remediação autônoma dentro do escopo da RSL. As ressalvas decorrem da validação exclusivamente experimental, da ausência de métricas de carga cognitiva, da discussão limitada de accountability e da necessidade de confirmar os critérios bibliométricos externos. Caso SJR, Qualis e número mínimo de citações sejam confirmados, o estudo deve permanecer no corpus final.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em base indexadora.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
