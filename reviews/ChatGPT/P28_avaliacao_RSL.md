# Avaliação do Estudo P28

## Identificação do estudo

**ID:** P28  
**Artigo:** *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models*  
**Autores:** Yasser Hmimou, Mohamed Tabaa, Azeddine Khiat e Zineb Hidila  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e na estrutura indicada no arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas, o quartil SJR e o estrato Qualis CAPES não constam no PDF. Esses campos permanecem como **[VERIFICAR]**, ainda que o material de apoio informe Q1 e A1.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P28 | *IEEE Access*, v. 13 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico com sistema LLM multiagente, datasets públicos e sintéticos, avaliação por especialistas e comparação com sistemas relacionados | 10.1109/ACCESS.2025.3602681 |

**Fontes para verificação externa:**

- **Citações:** IEEE Xplore, Scopus, Web of Science ou Google Scholar.
- **SJR:** Scimago Journal Rank.
- **Qualis:** Plataforma Sucupira / Qualis CAPES.

---

## Etapa 1 — Triagem de elegibilidade

### Resultado

**ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA: número de citações, quartil SJR e estrato Qualis.**

| Critério | Evidência no PDF | Resultado |
|---|---|---|
| Ano ≥ 2020 | Publicado em 25 de agosto de 2025, *IEEE Access*, volume 13, p. 1 do PDF. | Atendido |
| Publicação identificável | Periódico, volume e DOI são apresentados na primeira página. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos critérios bibliométricos externos.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | RQ1 — Context Definitions | Respondida Plenamente | T | Seções II–III, pp. 2–8; Figura 1, p. 4; Seção VI, pp. 15–16. | O artigo caracteriza uma autonomia deliberadamente limitada. Os agentes processam tarefas de forma independente em seus domínios, mas os LLMs não atuam como decisores autônomos: funcionam como unidades semânticas dentro de workflows determinísticos, com supervisão humana considerada indispensável. As características centrais incluem orquestração pelo Task Dispatcher, memória leve por agente, uso de ferramentas, RAG, processamento assíncrono, pontuação de risco e correlação entre contextos. O modelo decisório combina classificação estruturada, scores de risco, correlação sintática e temporal e síntese final de recomendações. |
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | RQ2 — Engineering Architecture | Respondida Plenamente | T | Seções III–IV, pp. 4–10; Figuras 1–7; Tabela 2, p. 9. | A arquitetura possui quatro camadas: interação com o usuário, Task Dispatcher, três agentes especializados e sistema central de recomendação cross-context. Os agentes tratam e-mail, logs e faixas de IP. A implementação utiliza LLaMA 3.3-70B via Groq, FAISS, RAG, ELK Stack, Suricata, Nmap, NVD API, RegEx, DNS e módulos Python. Os mecanismos avançados incluem validação de entrada, separação de responsabilidades, memória contextual, execução assíncrona, logging, rastreabilidade, outputs padronizados, explicabilidade, substituição de LLMs e fallback para ambientes restritos. |
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Seção V, pp. 10–15; Tabelas 5–7; Figuras 9–12. | O estudo reporta benefícios diretamente associados a SOC e resposta a incidentes: acurácia global de detecção de 93,6%, F1 de 0,94, acurácia de correlação de 87%, redução de falsos positivos de 41,3% e redução média do tempo de triagem de 38,5%. Os agentes individuais atingem acurácia entre 91,8% e 94,1%. As explicações foram consideradas tecnicamente válidas e úteis em mais de 90% dos casos, e a confiança média dos analistas foi 4,6 em 5. A evidência inclui SpamAssassin, CIC-IDS2017, aproximadamente 2.000 e-mails sintéticos, ambiente controlado de varredura de IP, 60 avaliações e comparação com 12 sistemas relacionados. Não há, contudo, medição direta de MTTD, MTTR ou carga cognitiva por instrumento validado. |
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P | Seção VI, pp. 15–16; Seções II–IV, pp. 3–9. | O artigo discute desafios técnicos e operacionais: dependência de ferramentas e APIs externas, latência, pontos únicos de falha, custo computacional, imprevisibilidade causada por prompts ou atualizações dos modelos, consistência da explicabilidade e limitação de datasets legados e sintéticos. Os mecanismos de governança incluem supervisão humana, rastreabilidade, auditabilidade, workflows determinísticos, validação de entrada, substituibilidade de modelos, fallback e proposta de implantação federada para privacidade. Entretanto, não há análise aprofundada sobre viés, accountability por erros, dual use, responsabilidade organizacional ou impactos éticos da automação em segurança. |
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção VI, pp. 15–16. | As lacunas e direções futuras são explícitas: suporte a entradas multimodais, como anexos, links e payloads visuais; processamento contínuo de streams de logs; implantação federada para ambientes distribuídos e com restrições de privacidade; adoção de LLMs mais leves; execução em edge e baixa largura de banda; aumento da resiliência; redução da latência e manutenção da rastreabilidade entre atualizações. |
| P28 |  | **SCORE_RQ** | **4,5 / 5,0** | **T + T + T + P + T** |  | O estudo possui aderência muito elevada ao tema da RSL. Sua principal contribuição é um copiloto multiagente, human-centric e orientado a workflows, diretamente aplicado à detecção, correlação e triagem de ameaças. A principal lacuna está na discussão ética e de accountability. |

### Observação sobre o nível de autonomia

O trabalho emprega o termo “agente”, mas diferencia explicitamente seus componentes de agentes cognitivamente autônomos. Os LLMs não planejam livremente nem executam remediações. Eles processam, explicam e correlacionam evidências dentro de pipelines predefinidos. Portanto, o estudo representa **autonomia delimitada com supervisão humana**, adequada ao conceito de copiloto, e não autonomia closed-loop.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P28 | Estudo empírico com sistema LLM multiagente aplicado à cibersegurança | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é claramente delimitado: soluções isoladas e baseadas em regras apresentam dificuldade para detectar ataques contextuais, multivetoriais e distribuídos entre e-mail, logs e infraestrutura de rede. A solução proposta também é explícita: uma arquitetura modular com agentes especializados, LLMs integrados a ferramentas e um mecanismo central de correlação e recomendação. Evidências: Resumo e Introdução, pp. 1–2.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo descreve os agentes, workflows, ferramentas, LLM utilizado, datasets públicos, pré-processamento, camadas de integração, métricas e protocolo geral de avaliação. Entretanto, não disponibiliza os prompts integrais, o código-fonte, parâmetros de inferência, seeds, configurações completas do ambiente nem o dataset sintético de phishing. Também não detalha suficientemente como os casos de correlação foram construídos e rotulados. A replicação arquitetural é possível, mas a reprodução fiel dos resultados permanece limitada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
Há validação em diferentes domínios, com dados públicos e sintéticos, métricas por agente, avaliação sistêmica, comparação com um SIEM de referência, análise por especialistas e benchmarking com sistemas relacionados. São medidos acurácia, F1, correlação, falsos positivos, tempo de triagem, qualidade das explicações e confiança do analista. Como ressalvas, a avaliação humana é pequena, parte dos dados é sintética ou legada e não são apresentados testes estatísticos inferenciais.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões retomam os resultados de detecção, correlação, redução de falsos positivos, explicabilidade e apoio ao analista. O artigo também apresenta seção explícita de limitações e ameaças à validade, relacionando dependência de APIs, latência, custo, atualizações de modelo e datasets legados às estratégias de mitigação e aos trabalhos futuros.

---

## Parecer final do revisor

O estudo apresenta excelente aderência ao tema **Agentic AI Copilot para Resposta a Incidentes**. Sua arquitetura multiagente correlaciona sinais de e-mail, logs e rede e fornece explicações e recomendações ao analista. O desenho é human-centric, auditável e explicitamente não autônomo na decisão final. Além da avaliação técnica, o artigo mede tempo de triagem e confiança humana, dimensões especialmente relevantes para a RSL.

### Recomendação

**INCLUIR.**

O artigo deve integrar o corpus por sua elevada aderência conceitual e operacional, SCORE_RQ de 4,5 e qualidade metodológica alta. Ele representa um caso claro de copiloto multiagente para SOC e resposta a incidentes, com resultados quantitativos e avaliação humana. As limitações de replicabilidade, uso de datasets legados e sintéticos e ausência de testes estatísticos devem ser registradas, mas não anulam sua contribuição. A inclusão definitiva permanece condicionada à confirmação dos critérios bibliométricos externos.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em IEEE Xplore, Scopus, Web of Science ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
