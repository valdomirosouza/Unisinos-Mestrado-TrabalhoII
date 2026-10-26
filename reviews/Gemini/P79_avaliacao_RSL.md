# INSTRUÇÕES DO PROMPT (CRITÉRIOS E DIRETRIZES DA RSL)

## PAPEL
Aja como pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por um professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, seguindo rigorosamente as diretrizes de Kitchenham (2009) no paper/artigo "Systematic literature reviews in software engineering – A systematic literature review". Sua avaliação de qualidade deve espelhar a lógica dos critérios DARE (QA1–QA4) descritos naquele trabalho.

## CONTEXTO DA RSL
Esta avaliação integra o artigo "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura", agora no ciclo 2 de atualização. O corpus prévio cobre P01–P40 (33 estudos incluídos). Você avaliará UM novo estudo candidato do ciclo 2 por vez, atribuindo o ID sequencial informado (a partir de P41), de modo que os resultados possam ser anexados diretamente às Tabelas 3, 5 e 7 da RSL existente.

## INSUMOS
- ID: P79
- Artigo: AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation
- Arquivo: P79_AI_Augmented_SOC_A_Survey_of_LLMs_and_Agents_for_Security_Automation.pdf
- qualis: A2 (derivado do percentil Scopus 85.0%, regra CAPES 2025-2028)
- sjr_quartile: Q1
- ressalvas_triagem: aprovado na triagem; candidato a fundacional (survey de LLMs/agentes em SOC, análogo a P33)

## REGRAS INVIOLÁVEIS (ANTIFABRICAÇÃO)
1. Avalie EXCLUSIVAMENTE o conteúdo presente no PDF anexado. Não use conhecimento externo nem suposições sobre o que o artigo "provavelmente" contém.
2. NÃO invente métricas, números de página, citações, DOI, quartil SJR, estrato Qualis ou contagem de citações.
3. Dados NÃO verificáveis no PDF (quartil SJR, estrato Qualis CAPES, número de citações) devem ser marcados como "[VERIFICAR]". Indique a fonte onde verificar (SJR: Scimago Journal Rank; Qualis: Plataforma Sucupira / Qualis CAPES; Citações: base indexadora).
4. Toda classificação (T/P/N e Y/P/N) deve ser ancorada em evidência concreta do texto (seção, figura, tabela ou página). Sem evidência localizável, a classificação é N.

## ETAPA 0 — EXTRAÇÃO BIBLIOMÉTRICA (alimenta a Tabela 3)
Extraia do PDF, quando presente: Periódico/Conferência, Ano, Tipo de estudo, DOI/URL. Marque como "[VERIFICAR]": Citações, SJR (quartil), Qualis (estrato).

## ETAPA 1 — TRIAGEM DE ELEGIBILIDADE (PRISMA / critérios da RSL)
Verifique os critérios de inclusão:
- Ano ≥ 2020
- Publicação ≠ NULL (veículo identificável)
- Citações ≥ 1 [pode exigir VERIFICAR]
- SJR Q1–Q2 [pode exigir VERIFICAR]
- Qualis A1–A2 [pode exigir VERIFICAR]
Resultado: "ELEGÍVEL", "INELEGÍVEL (motivo)" ou "ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (itens)". Só prossiga à extração completa se ELEGÍVEL ou PENDENTE; se INELEGÍVEL, registre o motivo e encerre.

## ETAPA 2 — EXTRAÇÃO E CLASSIFICAÇÃO DAS RQs (alimenta a Tabela 5)
Para cada RQ, avalie as subdimensões (a/b/c) e atribua UM veredito:
- "Respondida Plenamente" = T = 1.0 → todas as subdimensões cobertas com conteúdo explícito.
- "Parcialmente Respondida" = P = 0.5 → ao menos uma subdimensão coberta, ou cobertura genérica/superficial.
- "Não tem conteúdo suficiente" = N = 0.0 → subdimensões ausentes ou apenas tangenciais.
SCORE_RQ = soma (máx. 5.0).

- **RQ1 — Context Definitions:** Quais capacidades e níveis de autonomia (planejamento, memória, uso de ferramentas e supervisão humana) caracterizam Agentic AI e como afetam a tomada de decisão em ambientes complexos?
  - a) Autonomy definition
  - b) Core characteristics
  - c) Decision-making model
- **RQ2 — Engineering Architecture:** Quais arquiteturas e mecanismos (orquestração, memória, ferramentas, guardrails, observabilidade) sustentam Agentic AI em produção?
  - a) Architecture type
  - b) Tools/frameworks
  - c) Advanced capabilities
- **RQ3 — Evidence Benefits:** Quais evidências (quanti/quali) reportam benefícios e quais métricas são usadas (tempo de resposta, qualidade de decisão, carga operacional), especialmente em IR?
  - a) Qualitative benefits
  - b) Quantitative benefits / metrics
  - c) Evidence level
- **RQ4 — Challenges & Ethics:** Quais riscos e desafios (segurança, robustez, governança, accountability) limitam o uso responsável em sistemas críticos?
  - a) Technical challenges
  - b) Ethical/governance challenges
  - c) Governance mechanisms
- **RQ5 — Research Gaps:** Quais lacunas e direções futuras (avaliação/benchmarking, threat models, governança, observabilidade, alinhamento) são apontadas?

## ETAPA 3 — AVALIAÇÃO DE QUALIDADE QA (alimenta a Tabela 7)
Pontue Y=1.0 / P=0.5 / N=0.0 (máx. 4.0), conforme a rubrica da RSL:
- **QA1 Objetivos Claros:** o problema (ex.: fadiga de alertas, complexidade de logs) e a solução agêntica são explícitos?
- **QA2 Metodologia Replicável:** arquitetura, tecnologias, parâmetros e cenário experimental são detalhados o suficiente para replicação?
- **QA3 Base de Evidências Sólidas:** há validação empírica (experimento, estudo de caso industrial, simulação com métricas)? (toy example = P; teórico = N)
- **QA4 Conclusões Coerentes:** as conclusões derivam das evidências e as limitações são discutidas?
Banda de qualidade: Alta ≥ 3.0 | Média 1.5–2.5 | Baixa < 1.5.

---

# RESULTADO DA AVALIAÇÃO E PARECER DO ARTIGO (P79)

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P79 | Journal of Cybersecurity and Privacy (MDPI) | 2025 | [VERIFICAR] (Google Scholar / Scopus) | [VERIFICAR] Q1 (Scimago Journal Rank; informado nos insumos) | [VERIFICAR] A2 (Plataforma Sucupira / CAPES 2025–2028; informado nos insumos) | Systematic Review / Survey | 10.3390/jcp5040095 |

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA / Critérios da RSL)

- **Ano ≥ 2020:** Sim (2025).
- **Publicação ≠ NULL:** Sim (*Journal of Cybersecurity and Privacy*, MDPI).
- **Citações ≥ 1:** [VERIFICAR] (Publicado em novembro de 2025; contagem pendente em bases indexadoras).
- **SJR Q1–Q2:** [VERIFICAR] (Q1 indicado nos insumos; confirmar no Scimago Journal Rank).
- **Qualis A1–A2:** [VERIFICAR] (A2 indicado nos insumos derivado do percentil Scopus 85.0%; confirmar no Qualis Sucupira).

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações, confirmação formal de SJR e Qualis). Procede-se à extração completa por cumprir integralmente os critérios no escopo do documento.

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P79 | AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation | RQ1 | Respondida Plenamente | T (1.0) | Seção 3 (pp. 3–11), Seção 4 (pp. 12–14, Figura 3, Tabela 3) | Cobre plenamente: (a) define 5 níveis de autonomia (Nível 0 Manual a Nível 4 Totalmente Autônomo com modelos HITL, HoTL e HoOTL); (b) aborda características essenciais como planejamento, decomposição de tarefas multi-step, uso de ferramentas e memória; (c) detalha modelos de tomada de decisão autônoma e colaborativa em triagem, CTI e resposta a incidentes. |
| P79 | AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation | RQ2 | Respondida Plenamente | T (1.0) | Seção 3 (pp. 3–11, Tabela 1), Figura 2 (p. 12), Seção 5.1 (p. 16) | Cobre plenamente: (a) mapeia arquiteturas multiagente, coordenação global e híbridas; (b) cataloga ferramentas e protocolos de produção (LangChain, AutoGen, SOAR, SIEM/EDR, MCP, A2A, ACP, APIs); (c) explora capacidades avançadas como RAG, Chain-of-Thought (CoT), self-reflection e knowledge graphs. |
| P79 | AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation | RQ3 | Respondida Plenamente | T (1.0) | Seção 3 (pp. 3–11), Tabela 1 (p. 4), Tabela 2 (p. 11), Seção 4.2 (p. 13) | Cobre plenamente: (a) benefícios qualitativos (mitigação de fadiga de alertas, redução de sobrecarga cognitiva, consistência analítica); (b) ricas métricas quantitativas (MTTD/MTTR reduzido de 8h para 90 min, contenção < 5 min, redução de falsos positivos de 70% para 35%, F1-score, BERTScore, acurácia); (c) nível de evidência secundário (RSL com síntese de 105 estudos empíricos e industriais). |
| P79 | AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation | RQ4 | Respondida Plenamente | T (1.0) | Seção 5 (pp. 14–17, Tabela 4) | Cobre plenamente: (a) desafios técnicos (alucinações, latência, overhead de comunicação inter-agente, black box); (b) éticos e de governança (vazamento de dados, responsabilidade por erros, conformidade regulatória, erosão de confiança/complacência); (c) mecanismos de governança e defesas (Human-on-the-Loop, estruturação "Role, Goal, Constraints", auto-verificação, isolamento seguro). |
| P79 | AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation | RQ5 | Respondida Plenamente | T (1.0) | Seção 4.2 (p. 13), Seção 6 (pp. 17–18), Seção 7 (pp. 19–20) | Cobre plenamente: detalha lacunas e rotas futuras em benchmarking de segurança/adversarial (ex.: ASB), necessidade de ambientes de teste operacionais e dinâmicos, calibragem de confiança humano-IA, observabilidade/XAI avançada e validação empírica do modelo de maturidade com métricas operacionais. |
| **Total** | | | **SCORE_RQ** | **5.0 / 5.0** | | |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P79 | Systematic Review / Survey | 1.0 (Y) | 1.0 (Y) | 0.5 (P) | 1.0 (Y) | **3.5 / 4.0** | Alta |

### Justificativas da Avaliação de Qualidade (DARE / Kitchenham):
- **QA1 (Objetivos Claros = 1.0 / Y):** O problema operacional nos SOCs (fadiga de alertas, sobrecarga em triagem e complexidade de dados não estruturados) e as soluções agênticas/LLM em 8 funções operacionais são claramente estabelecidos e contextualizados.
- **QA2 (Metodologia Replicável = 1.0 / Y):** Segue rigorosamente o protocolo PRISMA 2020 com fluxograma detalhado (Figura 1), estratégias de busca explícitas (2022–2025, IEEE Xplore, ACM DL, arXiv, simpósios de ponta como NDSS, USENIX Security, ACM CCS, IEEE S&P) e pré-registro formal no Open Science Framework (OSF DOI: 10.17605/OSF.IO/9QC7V).
- **QA3 (Base de Evidências Sólidas = 0.5 / P):** Por ser uma revisão sistemática e survey da literatura, sintetiza 105 artigos primários com validações empíricas, mas não conduz experimentos práticos primários próprios (pontuação parcial P segundo os critérios DARE aplicados a estudos secundários).
- **QA4 (Conclusões Coerentes = 1.0 / Y):** Conclusões fortemente alinhadas aos achados e dados extraídos, apresentando uma discussão aprofundada das ameaças à validade (Seção 7: viés de seleção, validade ecológica, heterogeneidade métrica e rápida obsolescência dos modelos).

---

## Parecer Final do Revisor

- **Síntese de Aderência:** O estudo apresenta total alinhamento e máxima relevância para a RSL. Abrange com profundidade arquitetural e analítica a inserção de LLMs e sistemas multiagente nas 8 atividades centrais de SOC, com foco especial em Resposta a Incidentes, Triagem de Alertas e Sumarização de Logs. O Capability Maturity Model proposto fornece uma base conceitual e taxonômica sólida para categorizar graus de autonomia e níveis de supervisão (HITL, HoTL, HoOTL).
- **Recomendação:** **INCLUIR** (Artigo de alta qualidade metodológica, pontuação máxima em cobertura de RQs (5.0/5.0), qualidade DARE Alta (3.5/4.0), posicionando-se como candidato a estudo fundacional para o ciclo 2 da RSL, em linha com P33).
- **Pendências de Verificação Externa:** Confirmar contagem atual de citações em bases indexadoras (Google Scholar / Scopus) e verificar a homologação definitiva das métricas de periódicos (SJR Q1 e Qualis A2) nos sistemas de avaliação vigentes.