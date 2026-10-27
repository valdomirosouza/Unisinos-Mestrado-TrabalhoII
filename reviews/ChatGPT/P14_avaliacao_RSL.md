# Avaliação do Artigo P14 — Corpus Fundacional

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P14  
**Artigo:** *Transforming cybersecurity with agentic AI to combat emerging cyber threats*  
**Autor:** Nir Kshetri  
**Fonte de evidência:** PDF anexado, 12 páginas  
**Natureza da análise:** Avaliação retroativa de aderência e qualidade. A inclusão herdada do Trabalho I não é rediscutida.

## Etapa 0 — Extração bibliométrica

### Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P14 | Telecommunications Policy, vol. 49, artigo 102976 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Artigo de discussão/análise conceitual, com síntese narrativa e exemplos secundários de fornecedores | 10.1016/j.telpol.2025.102976 |

**Evidência bibliográfica:** cabeçalho, título, autoria, informações editoriais e DOI, página 1. O trabalho formula duas questões próprias na Seção 1 (p. 2) e apresenta discussão conceitual, síntese de fontes e casos comerciais relatados, sem descrever protocolo de revisão sistemática ou experimento original. A designação do tipo de estudo é **classificação analítica do revisor**, não autodeclaração metodológica do autor.

**Nota de rastreabilidade:** o roteiro informa SJR Q1 e Qualis A1 como previamente verificados em `papers.csv` (27/07/2026). Como os valores não são verificáveis no PDF e a regra exige avaliação restrita ao documento, a tabela preserva **[VERIFICAR]**, sem contradizer ou substituir a checagem externa anteriormente relatada.

## Etapa 1 — Triagem de elegibilidade

| Critério | Constatação | Evidência / situação |
|---|---|---|
| Ano ≥ 2020 | Atendido | 2025, página 1 |
| Publicação identificável | Atendido | *Telecommunications Policy*, vol. 49, 102976, página 1 |
| Citações ≥ 1 | Pendente | [VERIFICAR] em base indexadora. As referências citadas **pelo** artigo não são sua contagem de citações **recebidas**. |
| SJR Q1–Q2 | Pendente no PDF | [VERIFICAR] no Scimago Journal Rank; roteiro informa verificação externa Q1. |
| Qualis A1–A2 | Pendente no PDF | [VERIFICAR] na Plataforma Sucupira / Qualis CAPES; roteiro informa verificação externa A1. |

**Resultado da triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações recebidas, SJR e Qualis). Não há motivo documental de inelegibilidade por ano ou veículo. O estudo permanece no corpus fundacional já incluído, e a extração é realizada conforme a regra do roteiro.

## Etapa 2 — Extração e classificação das RQs

**Escala:** T = Respondida Plenamente (1,0); P = Parcialmente Respondida (0,5); N = Não tem conteúdo suficiente (0,0).

### Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P14 | Kshetri (2025) | RQ1 — Context Definitions | Respondida Plenamente | T (1,0) | §2, pp. 2–3; §3.4, p. 4; §6.1, p. 8 | Diferencia agentes restritos e agentic AI, detalha autonomia adaptativa e planejamento iterativo, memória, interfaces e módulos de planejamento/ação, acesso a ferramentas por APIs e aprovação humana baseada em risco. Descreve percepção, decisão e execução em ambientes dinâmicos. |
| P14 | Kshetri (2025) | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | §2, p. 2; §3.2–3.6, pp. 4–5; §4, pp. 5–6; §6.1, pp. 8–9 | Apresenta arquitetura lógica de módulos (interfaces, memória, perfil, planejamento, ação), integrações, exemplos multiagentes, RAG, trilhas de auditoria, monitoramento e guardrails. Não fornece projeto técnico reproduzível, topologia, configuração, contratos de ferramentas ou detalhes de orquestração em produção. |
| P14 | Kshetri (2025) | RQ3 — Evidence Benefits | Parcialmente Respondida | P (0,5) | §3, p. 3, Tabela 1; §3.2–3.5, p. 4 | Reporta vantagens qualitativas e métricas quantitativas de fornecedores: Microsoft Security Copilot com redução de 30% no MTTR; ReliaQuest com triagem de alertas 20 vezes mais rápida e contenção inferior a 5 minutos; Darktrace com redução de 90% no tempo de triagem. Contudo, são informações atribuídas a fontes secundárias, sem desenho experimental próprio, comparabilidade padronizada ou demonstração independente. |
| P14 | Kshetri (2025) | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | §4 e Tabela 2, pp. 5–7; §5, p. 7; §6 e §6.1, pp. 7–9 | Examina superfície de ataque, prompt injection, envenenamento de dados, risco em sistemas multiagentes, vazamento de informações, perda de supervisão e consequências regulatórias. Propõe mecanismos como RMF, menor privilégio, separação de zonas, auditoria, monitoramento, guardrails, limitação da autonomia e supervisão humana. |
| P14 | Kshetri (2025) | RQ5 — Research Gaps | Parcialmente Respondida | P (0,5) | §6.2, pp. 9–10; §6.1, pp. 8–9 | A Seção 6.2 identifica pesquisas futuras sobre maturidade de agentes ofensivos, assimetria entre atacantes e defensores, limiares de autonomia e teoria principal-agente. A discussão de governança é relevante, mas falta agenda explícita de benchmarks de resposta a incidentes, observabilidade, validação de sistemas ou avaliação da carga cognitiva humana. |
| **P14** | | **SCORE_RQ** | | **3,5/5,0** | | **Boa aderência temática, com limitações de profundidade técnica e robustez empírica.** |

### Justificativa por subdimensão

**RQ1.** (a) A autonomia é diferenciada da de agentes orientados a tarefas fixas, com objetivos de longo prazo e adaptação (§2, pp. 2–3). (b) São explicitados módulos de memória de curto e longo prazo, perfil, planejamento, ação, interfaces e integrações por API (§2, p. 2). (c) A decisão é descrita como sequência de percepção contextual, planejamento iterativo, ação adaptativa e, em certos cenários, aprovação do operador (§2, p. 2; §3.4, p. 4). O artigo não apresenta uma taxonomia formal de níveis de autonomia, mas cobre explicitamente as três subdimensões da rubrica.

**RQ2.** (a) Existe arquitetura **conceitual** modular (§2, p. 2); (b) são citados APIs, acesso a dados, RAG, LLMs e plataformas comerciais (§§2–4, pp. 2–6); (c) há capacidades de colaboração multiagente, rastreabilidade, monitoramento e controles (§4, p. 6; §6.1, pp. 8–9). A cobertura não chega a especificar como implementar, operar e reproduzir a arquitetura; por isso, **P**.

**RQ3.** (a) O trabalho cita redução de esforço dos analistas, agilidade, melhoria de detecção e automação (§3, pp. 3–4). (b) A Tabela 1 apresenta números de desempenho, inclusive 30% de redução de MTTR com Microsoft e 90% de redução de triagem com Darktrace (p. 3). (c) O nível de evidência é **secundário, predominantemente declaratório/comercial**: os indicadores são associados a produtos e relatórios citados, não a medições controladas do artigo. Não são demonstrados intervalos de confiança, metodologia de coleta, amostras comparáveis ou medição direta de carga cognitiva. Por isso, **P**, apesar da presença de números.

**RQ4.** (a) Vulnerabilidades técnicas e efeitos em cascata são examinados nas §§4–5 (pp. 5–7). (b) A discussão cobre segurança, privacidade, decisões sem rastreabilidade, responsabilidade, supervisão e enquadramento regulatório (§6.1, pp. 8–9). (c) O trabalho aponta RMF, governança por risco, permissões explícitas, menor privilégio, limitação de autonomia, auditoria, monitoramento, isolamento e intervenção humana (§4, p. 5; §6.1, pp. 8–9). **T**.

**RQ5.** Há seção formal dedicada a pesquisa futura (§6.2, pp. 9–10), centrada em adoção ofensiva de agentes, assimetrias, avanço da autonomia e teoria principal-agente. Entretanto, faltam lacunas operacionalizadas em métricas/benchmarks de IR, observabilidade do copilot e interação humano-agente. **P**.

## Etapa 3 — Avaliação de qualidade DARE

**Escala:** Y = 1,0; P = 0,5; N = 0,0. Bandas: Alta ≥3,0; Média = 1,5–2,5; Baixa <1,5.

### Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P14 | Análise conceitual/narrativa com exemplos e indicadores secundários de mercado | Y (1,0) | N (0,0) | N (0,0) | P (0,5) | **1,5/4,0** | **Média** |

### Fundamentação dos critérios de qualidade

**QA1 — Objetivos claros: Y (1,0).** O resumo (p. 1) e a introdução (§1, p. 2) explicitam o problema da evolução das ameaças digitais, a proposta de aplicação da agentic AI em SOCs e resposta a incidentes, e os riscos de sua integração. O autor formula expressamente duas perguntas sobre transformação da cibersegurança e riscos associados (§1, p. 2).

**QA2 — Metodologia replicável: N (0,0).** O artigo apresenta módulos de agentes e exemplos de produtos, mas não informa método de seleção de fontes, procedimento de revisão replicável, configuração de modelos, arquitetura implementada, datasets, parâmetros, protocolo experimental ou scripts (§§2–3, pp. 2–4). Não há cenário de avaliação próprio que possa ser reproduzido apenas com as informações fornecidas.

**QA3 — Base de evidências sólidas: N (0,0).** A Tabela 1 (p. 3) e as subseções 3.2–3.6 (pp. 4–5) reproduzem resultados e alegações atribuídos a empresas ou publicações citadas. Embora úteis como evidência secundária e motivação, **não constituem validação empírica executada pelo autor**, nem há experimento, simulação mensurada ou estudo de caso industrial com protocolo e resultados próprios. Não confundir a existência de métricas reportadas com demonstração de robustez metodológica original.

**QA4 — Conclusões coerentes: P (0,5).** A discussão (§6, pp. 7–9) e a conclusão (§7, p. 10) retomam os ganhos e riscos abordados e recomendam governança e monitoramento. Também reconhecem custos, complexidade, problemas de segurança e limites da autonomia (§6.1, pp. 8–9). Porém, a conclusão de transformação operacional se apoia majoritariamente em referências e declarações de mercado, sem tratamento suficientemente explícito das limitações do método de síntese e da força causal das métricas. Por isso a coerência é **parcial**, não plena.

## Parecer final do revisor

### Síntese

O estudo apresenta aderência relevante ao escopo da RSL, especialmente para definições de agentic AI, aplicações em Security Operations Centers e governança de sistemas autônomos. Reúne indicadores reportados de produtividade, triagem e resposta a incidentes, incluindo redução de MTTR, mas sem validação empírica própria. As contribuições sobre arquitetura são principalmente conceituais; questões como replicabilidade, benchmarking e medição de carga cognitiva permanecem insuficientemente tratadas. A maior contribuição do artigo é contextual e analítica, e não demonstrativa.

### Recomendação

**INCLUIR COM RESSALVAS.** Manter o artigo P14 no corpus fundacional, conforme decisão herdada do Trabalho I, e utilizar seus resultados para fundamentação conceitual, mapeamento de riscos, mecanismos de governança e identificação preliminar de benefícios reportados por fornecedores. Não tratá-lo como prova experimental independente de redução de MTTR, de carga operacional ou de eficácia de uma arquitetura de copilot agêntico. **SCORE_RQ = 3,5/5,0; SCORE_QA = 1,5/4,0 (Média).**

### Pendências de verificação externa

1. **Citações recebidas ≥1:** [VERIFICAR] em base indexadora (Scopus, Web of Science ou Google Scholar), registrando data da consulta.
2. **SJR / quartil Q1:** [VERIFICAR] em Scimago Journal Rank, registrando ano e categoria; o prompt registra Q1 como previamente verificado, mas o PDF não o confirma.
3. **Qualis A1:** [VERIFICAR] na Plataforma Sucupira / Qualis CAPES, registrando área de avaliação e período; o prompt registra A1 como previamente verificado, mas o PDF não o confirma.

### Nota metodológica sobre o uso na RSL

As métricas de fornecedores citadas no artigo devem ser codificadas como **resultados secundários reportados**, e não como medidas primárias do estudo P14. Sua referência pode apoiar hipóteses sobre redução de tempos de resposta, mas não substituir estudos com avaliação controlada, definição de métricas, cenários reprodutíveis e comparação entre intervenção humana e copilot agêntico.

---

**Fonte única da avaliação:** KSHETRI, Nir. *Transforming cybersecurity with agentic AI to combat emerging cyber threats*. **Telecommunications Policy**, v. 49, artigo 102976, 2025. DOI: https://doi.org/10.1016/j.telpol.2025.102976. Informações extraídas do PDF anexo; sem consulta a fontes externas.
