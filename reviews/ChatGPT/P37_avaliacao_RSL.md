# Avaliação do Estudo P37

## Identificação do estudo

**ID:** P37  
**Artigo:** *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response*  
**Autores:** Olufunsho I. Falowo e Jacques Bou Abdo  
**Escopo da avaliação:** análise baseada exclusivamente no conteúdo do PDF fornecido e nas instruções do arquivo Markdown anexado.

> **Nota metodológica:** o número de citações recebidas pelo artigo, o quartil SJR e o estrato Qualis CAPES não são apresentados no PDF. Esses campos permanecem como **[VERIFICAR]**, embora o arquivo de instruções informe SJR Q2 e Qualis A2.

---

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P37 | *Algorithms*, v. 19, artigo 62 | 2026 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Estudo empírico quantitativo baseado em survey com 194 profissionais de cibersegurança dos Estados Unidos | 10.3390/a19010062 |

**Evidência bibliométrica:** a primeira página identifica o periódico *Algorithms*, o volume 19, o artigo 62, o ano de 2026 e o DOI. O manuscrito foi recebido em 2 de dezembro de 2025, revisado em 29 de dezembro de 2025, aceito em 7 de janeiro de 2026 e publicado em 11 de janeiro de 2026.

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
| Ano ≥ 2020 | Publicado em 11 de janeiro de 2026, p. 1. | Atendido |
| Publicação identificável | O PDF apresenta periódico, volume, número do artigo e DOI, p. 1. | Atendido |
| Citações ≥ 1 | A quantidade de citações recebidas pelo estudo não consta no PDF. | [VERIFICAR] |
| SJR Q1–Q2 | O quartil SJR não consta no PDF. | [VERIFICAR] |
| Qualis A1–A2 | O estrato Qualis CAPES não consta no PDF. | [VERIFICAR] |

Não foi identificado critério interno de inelegibilidade. A extração completa prossegue, condicionada à confirmação dos três itens bibliométricos externos.

---

## Etapa 2 — Extração e classificação das RQs

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | RQ1 — Context Definitions | Parcialmente Respondida | P | Seção 2.2, pp. 2–3; Tabela 1, pp. 4–5; Seções 4.1.2–4.1.5, pp. 11–13; Seção 5.3, p. 25. | O artigo define Agentic AI como sistemas autônomos ou semiautônomos capazes de perceber o ambiente, raciocinar sobre objetivos complexos e executar ações independentes, como atualizar regras de firewall ou isolar nós comprometidos, sem comandos humanos passo a passo. Também distingue essa abordagem da automação linear baseada em scripts e investiga níveis de confiança em decisões sem supervisão. Entretanto, não apresenta um modelo decisório técnico, planejamento, memória, reflexão ou seleção de ferramentas. A cobertura se concentra na percepção dos profissionais sobre autonomia e human-in-the-loop. |
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | RQ2 — Engineering Architecture | Parcialmente Respondida | P | Seção 2.6, p. 4; Tabelas 1 e 2, pp. 4–9; Seção 5.4.1, pp. 25–26; Seções 6.4–6.5, pp. 29–30. | O estudo discute SOAR, NIST, SANS, playbooks, modularidade, escalabilidade, interoperabilidade, auditabilidade e modelos de risco específicos para IA. Os respondentes demonstram preferência por frameworks simples, modulares, adaptativos e compatíveis com supervisão humana. Contudo, o artigo não implementa nem especifica uma arquitetura agêntica de produção, ferramentas concretas, memória, orquestração, observabilidade do agente, guardrails técnicos ou mecanismos de fallback. A contribuição é de requisitos e prontidão organizacional, não de engenharia de uma solução. |
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | RQ3 — Evidence Benefits | Respondida Plenamente | T | Resumo, p. 1; Tabela 3, p. 11; Figuras 2–10, pp. 12–16; Seções 5.1–5.5, pp. 22–26. | O estudo apresenta benefícios qualitativos e quantitativos diretamente relacionados a incident response. Entre 194 respondentes, 84% afirmaram integrar Agentic AI ao processo de resposta, 92% perceberam redução significativa de MTTD/MTTR e 74% relataram retraining das equipes. Em contraste, 70% consideram que as ferramentas atuais não acompanham ameaças orientadas por IA. São apresentados percentuais, intervalos de confiança e coeficientes de consistência interna de 0,82 e aproximadamente 0,78. A evidência é empírica e proveniente de profissionais, mas mede percepções autorrelatadas, não valores observados de MTTD, MTTR, carga cognitiva ou desempenho operacional. |
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | RQ4 — Challenges & Ethics | Respondida Plenamente | T | Seções 2.4–2.5, pp. 3–4; Tabela 3, p. 11; Figuras 4–6, pp. 13–14; Tabela 4, pp. 16–17; Seções 5.3–5.6, pp. 25–27; Seções 6.2–6.5, pp. 28–30. | O artigo cobre riscos técnicos, éticos e organizacionais: falsos positivos e negativos, imprevisibilidade, ataques adversariais, opacidade, baixa confiança, falta de accountability, inadequação regulatória e dificuldade de mapear indicadores como model drift e data poisoning. Apenas 13% confiam em decisões de IA sem intervenção humana, 63% rejeitam triagem e contenção sem supervisão, e 83% não consideram que os benefícios superem os riscos. Os mecanismos recomendados incluem human-in-the-loop, rastreabilidade, auditabilidade, regras de segurança, taxonomia de autonomia, threat modeling específico para IA, frameworks modulares e orientação ética explícita. |
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | RQ5 — Research Gaps | Respondida Plenamente | T | Seção 2.6, p. 4; Tabela 4, pp. 16–17; Seções 5.5–5.6, pp. 26–27; Seções 6–6.5, pp. 27–30. | O artigo identifica lacunas em integração de SOAR, taxonomias de autonomia, ameaça e risco específicos para IA, interoperabilidade, governança, exercícios de mesa, mapeamento de model drift e atualização de NIST e SANS. Entre os respondentes, 79% não possuem processo separado de AI threat modeling e 96% apoiam uma revisão ampla dos frameworks. As direções futuras incluem entrevistas, estudos de caso, pesquisa longitudinal, validação externa, pilotos, ajustes iterativos, escalas mais granulares e desenvolvimento de um framework modular e orientado a IA. |
| P37 |  | **SCORE_RQ** | **4,0 / 5,0** | **P + P + T + T + T** |  | O estudo apresenta aderência muito elevada aos benefícios percebidos, confiança, governança e lacunas de Agentic AI em incident response. Sua contribuição é limitada nas dimensões de arquitetura e tomada de decisão técnica, pois não implementa nem avalia um agente ou copiloto operacional. |

### Observação sobre a natureza da evidência

Os resultados representam **percepções de profissionais**, não medições instrumentadas dos ambientes das organizações. A afirmação de que 92% observaram redução de MTTD/MTTR indica forte percepção de benefício, mas o estudo não coleta tempos anteriores e posteriores, valores absolutos, telemetria operacional ou dados de incidentes que permitam estimar a magnitude da redução.

### Observação sobre adoção e confiança

O artigo identifica uma tensão relevante. Embora 84% dos participantes relatem integração de Agentic AI e 92% percebam ganhos em MTTD/MTTR, somente 13% confiam em decisões sem intervenção humana e 37% apoiam triagem e contenção sem supervisão. Esses resultados favorecem modelos de copiloto ou autonomia delimitada, nos quais a automação amplia a capacidade do analista sem eliminar a responsabilidade humana.

### Observação sobre generalização

O cálculo inicial de tamanho amostral presume amostragem aleatória em uma população nacional de gestores de TI. Contudo, a coleta efetiva utilizou grupos do LinkedIn, fóruns de ISC2, redes da ISACA e outras comunidades profissionais. O próprio artigo classifica essa estratégia como amostragem proposital ou por conveniência e recomenda cautela ao interpretar a margem de erro de 4,97% e a generalização dos resultados.

---

## Etapa 3 — Avaliação de qualidade

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P37 | Estudo empírico quantitativo baseado em survey com profissionais de cibersegurança | Y (1,0) | P (0,5) | Y (1,0) | Y (1,0) | **3,5 / 4,0** | **Alta** |

### Justificativas da avaliação de qualidade

**QA1 — Objetivos claros: Y (1,0).**  
O problema é explicitamente delimitado: integração fragmentada de SOAR, baixa prontidão dos frameworks tradicionais para ameaças baseadas em IA, incerteza sobre autonomia e confiança e ausência de evidências provenientes de profissionais. O objetivo é investigar expectativas sobre automação e avaliar a prontidão de NIST e SANS para modernização. As duas questões de pesquisa são apresentadas na Seção 2.7, p. 4.

**QA2 — Metodologia replicável: P (0,5).**  
O artigo apresenta as vinte perguntas do survey, justificativa das variáveis binárias, cálculo do tamanho amostral, canais de recrutamento, plataforma Qualtrics, período de coleta, aprovação ética, fórmulas, intervalos de confiança e coeficientes de consistência. Entretanto, os itens psicométricos completos e os dados em nível de respondente não são disponibilizados no PDF; os dados dependem de solicitação aos autores. Também não há caracterização detalhada da experiência, função, setor ou maturidade das organizações participantes, e a distribuição por redes profissionais não possui um quadro amostral reproduzível. Assim, o desenho geral pode ser replicado, mas a reprodução integral da amostra e dos cálculos permanece limitada.

**QA3 — Base de evidências sólidas: Y (1,0).**  
O estudo coleta 194 respostas válidas de profissionais envolvidos em cibersegurança ou segurança da informação, superando a meta de 140 participantes. Apresenta resultados quantitativos para vinte itens, intervalos de confiança e análise de consistência interna. A evidência é apropriada ao objetivo de mapear percepções, confiança e prontidão organizacional. Como ressalva, não constitui validação técnica de um sistema agêntico nem comprova causalmente redução de MTTD/MTTR, pois os benefícios são autorrelatados e a amostra é de conveniência.

**QA4 — Conclusões coerentes: Y (1,0).**  
As conclusões derivam dos resultados e preservam a diferença entre modernizar e substituir os frameworks atuais. O artigo discute explicitamente limitações de respostas binárias, sampling bias, concentração geográfica nos Estados Unidos, autorrelato, construct validity bias e framing effects. Também propõe entrevistas, estudos de caso, pesquisas longitudinais, pilotos e validação externa como próximos passos.

---

## Parecer final do revisor

O estudo possui elevada aderência ao escopo de incident response e fornece evidência empírica relevante sobre adoção de Agentic AI, percepção de redução de MTTD/MTTR, confiança em autonomia e prontidão dos frameworks. Sua contribuição é especialmente forte para governança, human-in-the-loop e modernização de NIST, SANS e SOAR. Entretanto, não apresenta arquitetura, protótipo ou avaliação operacional de um agente ou copiloto.

### Recomendação

**INCLUIR COM RESSALVAS.**

A inclusão é recomendada porque o estudo oferece uma das evidências mais diretamente relacionadas às percepções de profissionais sobre Agentic AI em resposta a incidentes, incluindo MTTD/MTTR, autonomia, supervisão e governança. As ressalvas decorrem da natureza autorrelatada dos resultados, da amostragem por conveniência, da ausência de métricas operacionais objetivas, da falta de detalhamento dos contextos organizacionais e do fato de o estudo não implementar uma solução agêntica. Deve ser utilizado como evidência sociotécnica e organizacional, não como comprovação técnica da eficácia de agentes em produção.

### Pendências de verificação externa

1. **Número de citações ≥ 1:** verificar em Scopus, Web of Science, Dimensions ou Google Scholar.
2. **SJR Q1–Q2:** verificar no Scimago Journal Rank.
3. **Qualis A1–A2:** verificar na Plataforma Sucupira / Qualis CAPES.
