# Avaliação do Artigo P63

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura (Ciclo 2)  
**ID:** P63  
**Artigo:** Borsci et al. — *The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents*  
**Fonte exclusiva:** PDF fornecido, *Personal and Ubiquitous Computing*, 26:95–119 (2022).  
**Critério:** Aplicação do protocolo `prompt-P63.md`; não houve consulta externa.

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P63 | *Personal and Ubiquitous Computing* | 2022 | [VERIFICAR] | [VERIFICAR] (Q2 informado no protocolo, não confirmado no PDF) | [VERIFICAR] (A1 informado no protocolo, não confirmado no PDF) | Estudo metodológico de desenvolvimento e avaliação piloto de escala psicométrica, com revisão sistemática, survey, grupos focais e teste empírico | https://doi.org/10.1007/s00779-021-01582-9 |

**Evidência:** Cabeçalho e resumo, p. 95 (PDF p. 1); quatro estudos descritos na Introdução, p. 97 (PDF p. 3); Estudo 4, pp. 107–109 (PDF pp. 13–15). **Ano adotado:** 2022, ano do volume publicado; o PDF indica publicação online em 21/07/2021.

**Pendências:** consultar uma base indexadora para verificar ≥1 citação; Scimago Journal Rank para Q1/Q2 no período pertinente; Plataforma Sucupira / Qualis CAPES para A1/A2. Os valores Q2 e A1 são dados do *prompt*, não do PDF, e não foram tratados como verificados.

## Etapa 1 — Triagem de elegibilidade

| Critério | Avaliação | Evidência |
|---|---|---|
| Ano ≥ 2020 | Atende | 2022 no cabeçalho do periódico, p. 95; publicação online em 2021. |
| Publicação identificável | Atende | *Personal and Ubiquitous Computing*, vol. 26, pp. 95–119, p. 95. |
| Citações ≥ 1 | [VERIFICAR] | Contagem de citações não presente no PDF. |
| SJR Q1–Q2 | [VERIFICAR] | Q2 informado no protocolo, mas não verificável no PDF. |
| Qualis A1–A2 | [VERIFICAR] | A1 informado no protocolo, mas não verificável no PDF. |

**Resultado da triagem: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis).** A análise é mantida porque o protocolo autoriza continuar estudos com elegibilidade pendente. A aprovação preliminar na triagem, relatada no prompt, não demonstra aderência temática plena.

## Etapa 2 — Classificação das questões de pesquisa

### Tabela B — Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P63 | *The Chatbot Usability Scale* | RQ1 — Context Definitions | Não tem conteúdo suficiente | N (0,0) | Introdução, pp. 95–97; §4.3, p. 107 | Define chatbots e agentes conversacionais e discute percepção do usuário, mas não operacionaliza autonomia, planejamento, memória, uso de ferramentas ou um modelo de decisão de Agentic AI. A menção genérica a autonomia não cobre as subdimensões. |
| P63 | *The Chatbot Usability Scale* | RQ2 — Engineering Architecture | Não tem conteúdo suficiente | N (0,0) | §§2–5, pp. 98–109; Apêndices 6 e 8, pp. 114 e 116 | BOT-Check e BUS-15 são instrumentos de avaliação de interação, não arquiteturas de agentes. Não apresenta orquestração, memória arquitetural, ferramentas, frameworks de execução, guardrails ou observabilidade de sistemas agênticos em produção. |
| P63 | *The Chatbot Usability Scale* | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | §5.1–5.2, pp. 107–108; Fig. 2, p. 100; Tabelas 6 e 7, pp. 105–106 | Oferece evidência quantitativa e avaliação de satisfação e usabilidade: 96 participantes no piloto, 385 questionários utilizados, α global BUS-15 = 0,87 e correlações com UMUX-LITE. Mede percepção de tempo de resposta e qualidade da interação, mas não reporta redução de MTTD/MTTR, carga operacional ou desempenho em incident response. |
| P63 | *The Chatbot Usability Scale* | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | Tabela 1, pp. 98–99; Tabela 4, p. 103; §5.2.2, p. 108; §6, p. 109; Apêndice 8, p. 116 | Inclui percepção de privacidade e segurança, confiança, resiliência diante de falhas de comunicação e limitações de representatividade. Não desenvolve mecanismos concretos de accountability, governança ou controle de risco de agentes autônomos em sistemas críticos. |
| P63 | *The Chatbot Usability Scale* | RQ5 — Research Gaps | Parcialmente Respondida | P (0,5) | §5.3 e §6, p. 109 | Identifica necessidade de validar BUS-15 com mais chatbots, participantes diversos, inclusão de pessoas com deficiência e construção de benchmarks comparáveis. Lacunas relevantes à avaliação humano-IA, sem tratar especificamente de threat models, observabilidade e alinhamento agêntico. |
| **P63** | | **SCORE_RQ TOTAL** | | **1,5 / 5,0** | | **Aderência temática indireta, concentrada na avaliação de usabilidade e experiência com agentes conversacionais.** |

**Interpretação:** O escore baixo reflete a especificidade das RQs para Agentic AI e resposta a incidentes, não falta de rigor científico do estudo. A mensuração da satisfação de usuários de chatbots não constitui evidência de eficácia de copilotos de resposta a incidentes.

## Etapa 3 — Avaliação de qualidade metodológica

### Tabela C — Avaliação de Qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P63 | Desenvolvimento e estudo piloto de instrumento psicométrico, precedido por revisão, survey e grupos focais | P (0,5) | P (0,5) | Y (1,0) | Y (1,0) | **3,0 / 4,0** | **Alta** |

**QA1 — Objetivos claros (P = 0,5).** A lacuna sobre instrumentos padronizados de satisfação com chatbots, os objetivos e as entregas BUS-15/BOT-Check são explícitos (Resumo, p. 95; Introdução, p. 97). Porém, a rubrica específica requer problema e solução *agênticos* explícitos, ausentes no estudo. Portanto, pontuação parcial segundo o protocolo da RSL, embora os objetivos próprios do artigo sejam claros.

**QA2 — Metodologia replicável (P = 0,5).** Há detalhamento dos quatro estudos, instrumentos e tarefas (Seções 2–5; Apêndices 1, 5, 7 e 8). No piloto são descritos 10 chatbots, 96 voluntários, 385 questionários analisados, escala Likert de cinco pontos, análise fatorial exploratória bayesiana com 50.000 iterações, pacotes `BayesFM` e `psych`, confiabilidade alfa e correlações de Pearson (§5.1, pp. 107–108). Isso oferece replicabilidade parcial do procedimento psicométrico; não existe arquitetura/sistema agêntico reproduzível e a reexecução exata depende da disponibilidade dos chatbots e dados usados, não integralmente assegurada pelo artigo.

**QA3 — Base de evidências sólidas (Y = 1,0).** A investigação empírica contém survey de seleção de atributos (29 respostas; §3, p. 100), grupos focais (16 voluntários; §4, p. 105) e piloto de interação com chatbots (96 voluntários e 385 questionários válidos; §5, pp. 107–108). O instrumento final BUS-15 obteve alfa global de 0,87, e sua relação com UMUX-LITE foi analisada (Tabelas 6 e 7). Trata-se de evidência empírica para o **construto de usabilidade**, não para desempenho de um copilot agêntico.

**QA4 — Conclusões coerentes (Y = 1,0).** A discussão distingue resultado exploratório de validação definitiva e reconhece explicitamente a necessidade de novos estudos, amostras mais diversas e inclusão de pessoas com deficiência (§5.3 e §6, p. 109). Os autores ressaltam que BUS-15 ainda não está validado como instrumento pronto para uso irrestrito em testes de usabilidade, enquanto BOT-Check tem aplicação diagnóstica mais imediata.

> **Nota de interpretação:** A banda **Alta** corresponde à qualidade do desenho e relato de evidências sobre usabilidade. Não significa alta relevância para a arquitetura ou eficácia de Agentic AI em incident response.

## Parecer final do revisor

### Síntese

O P63 desenvolve os instrumentos BOT-Check e BUS-15 para avaliar a qualidade da interação e a satisfação de usuários com chatbots de serviço. O estudo apresenta uma sequência empírica estruturada e explora propriedades psicométricas da escala, com consistência interna geral de 0,87. Sua contribuição para a RSL é **complementar**, principalmente na mensuração da experiência humano-IA, da clareza conversacional, da privacidade percebida e da resposta percebida. Não oferece arquitetura, autonomia, observabilidade ou evidências de benefícios operacionais para copilotos agênticos na resposta a incidentes.

### Recomendação: **INCLUIR COM RESSALVAS**

**Justificativa:** Manter como referência de suporte à dimensão *human-in-the-loop / human–AI interaction*, à concepção de instrumentos de avaliação de usabilidade e à futura construção de benchmarks de percepção do usuário. Não empregar como evidência direta de redução de MTTD/MTTR, melhora da tomada de decisão operacional, redução de carga cognitiva em SRE ou capacidade autônoma de resolução de incidentes. Caso o corpus final exija exclusivamente aplicações agênticas concretas em IR, o artigo deverá ser reclassificado como **referência contextual**, fora do conjunto principal de evidências.

### Pendências de verificação externa

1. **Citações:** confirmar pelo menos uma citação em base indexadora (por exemplo, Scopus, Web of Science ou Google Scholar).
2. **SJR:** conferir quartil do periódico no *Scimago Journal Rank* para o período da RSL.
3. **Qualis:** verificar estrato na *Plataforma Sucupira / Qualis CAPES* segundo a regra e período adotados na RSL.

**Decisão bibliométrica definitiva condicionada às três verificações.** Os qualificadores A1 e Q2 aparecem nos metadados do prompt, não são resultados auditáveis no PDF.

### Rastreabilidade adicional

- **BUS-15:** itens e cinco dimensões listados no Apêndice 8, p. 116: acessibilidade às funções do chatbot; qualidade das funções; qualidade da conversação e informação; privacidade e segurança percebidas; tempo de resposta.
- **BOT-Check:** checklist no Apêndice 6, p. 114.
- **Amostra e procedimento do piloto:** §5.1, pp. 107–108; resultados de confiabilidade e validação exploratória: §5.2, p. 108, Tabelas 6–7.
- **Limitações e pesquisas futuras:** §5.3 e §6, p. 109.

---

*Páginas indicadas correspondem à paginação impressa do periódico; quando explicitado, também se indica a página física do PDF. Classificações ancoradas exclusivamente no artigo anexo.*
