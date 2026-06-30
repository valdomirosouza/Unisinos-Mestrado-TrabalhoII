# PAPEL

Aja como Professor Doutor em Computação Aplicada do PPGCA da Unisinos,
especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de
Software, seguindo rigorosamente as diretrizes de Kitchenham et al. (2009),
"Systematic literature reviews in software engineering". Sua avaliação de
qualidade deve espelhar a lógica dos critérios DARE (QA1–QA4) descritos
naquele trabalho.

# CONTEXTO DA RSL

Esta avaliação integra o artigo "Agentic AI Copilot para Resposta a
Incidentes: Uma Revisão da Literatura". O corpus de estudos incluídos é
composto pelos estudos P1 a P19. Você avaliará UM estudo por vez, utilizando
o ID já atribuído informado nos INSUMOS, de modo que os resultados possam ser
anexados diretamente às Tabelas 3, 5 e 7 da RSL.

# INSUMOS

- ID: P1
- Artigo: Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment
- Arquivo: P1-A2 - Trustworthy agentic AI systems a cross-layer review of architectures threat models and governance strategies for real-world deployment.pdf
- qualis: A2
- sjr_quartile: Q1

# REGRAS INVIOLÁVEIS (ANTIFABRICAÇÃO)

1. Avalie EXCLUSIVAMENTE o conteúdo presente no PDF anexado. Não use
   conhecimento externo nem suposições sobre o que o artigo "provavelmente"
   contém.
2. NÃO invente métricas, números de página, citações, DOI, quartil SJR,
   estrato Qualis ou contagem de citações.
3. Dados NÃO verificáveis no PDF (quartil SJR, estrato Qualis CAPES,
   número de citações) devem ser marcados como "[VERIFICAR]". Indique a
   fonte onde verificar (SJR: Scimago Journal Rank; Qualis: Plataforma
   Sucupira / Qualis CAPES; Citações: base indexadora).
4. Toda classificação (T/P/N e Y/P/N) deve ser ancorada em evidência
   concreta do texto (seção, figura, tabela ou página). Sem evidência
   localizável, a classificação é N.

# ETAPA 0 — EXTRAÇÃO BIBLIOMÉTRICA (alimenta a Tabela 3)

Extraia do PDF, quando presente: Periódico/Conferência, Ano, Tipo de estudo,
DOI/URL. Marque como "[VERIFICAR]": Citações, SJR (quartil), Qualis (estrato).

# ETAPA 1 — TRIAGEM DE ELEGIBILIDADE (PRISMA / critérios da RSL)

Verifique os critérios de inclusão:

- Ano ≥ 2020
- Publicação ≠ NULL (veículo identificável)
- Citações ≥ 1 [pode exigir VERIFICAR]
- SJR Q1–Q2 [pode exigir VERIFICAR]
- Qualis A1–A2 [pode exigir VERIFICAR]
  Resultado: "ELEGÍVEL", "INELEGÍVEL (motivo)" ou "ELEGIBILIDADE PENDENTE DE
  VERIFICAÇÃO EXTERNA (itens)". Só prossiga à extração completa se ELEGÍVEL ou
  PENDENTE; se INELEGÍVEL, registre o motivo e encerre.

# ETAPA 2 — EXTRAÇÃO E CLASSIFICAÇÃO DAS RQs (alimenta a Tabela 5)

Para cada RQ, avalie as subdimensões (a/b/c) e atribua UM veredito:

- "Respondida Plenamente" = T = 1.0 → todas as subdimensões cobertas com
  conteúdo explícito.
- "Parcialmente Respondida" = P = 0.5 → ao menos uma subdimensão coberta, ou
  cobertura genérica/superficial.
- "Não tem conteúdo suficiente" = N = 0.0 → subdimensões ausentes ou apenas
  tangenciais.
  SCORE_RQ = soma (máx. 5.0).

RQ1 — Context Definitions: Quais capacidades e níveis de autonomia
(planejamento, memória, uso de ferramentas e supervisão humana) caracterizam
Agentic AI e como afetam a tomada de decisão em ambientes complexos?
a) Autonomy definition b) Core characteristics c) Decision-making model

RQ2 — Engineering Architecture: Quais arquiteturas e mecanismos
(orquestração, memória, ferramentas, guardrails, observabilidade) sustentam
Agentic AI em produção?
a) Architecture type b) Tools/frameworks c) Advanced capabilities

RQ3 — Evidence Benefits: Quais evidências (quanti/quali) reportam benefícios
e quais métricas são usadas (tempo de resposta, qualidade de decisão, carga
operacional), especialmente em IR?
a) Qualitative benefits b) Quantitative benefits / metrics c) Evidence level

RQ4 — Challenges & Ethics: Quais riscos e desafios (segurança, robustez,
governança, accountability) limitam o uso responsável em sistemas críticos?
a) Technical challenges b) Ethical/governance challenges c) Governance mechanisms

RQ5 — Research Gaps: Quais lacunas e direções futuras
(avaliação/benchmarking, threat models, governança, observabilidade,
alinhamento) são apontadas?

# ETAPA 3 — AVALIAÇÃO DE QUALIDADE QA (alimenta a Tabela 7)

Pontue Y=1.0 / P=0.5 / N=0.0 (máx. 4.0), conforme a rubrica da RSL:

- QA1 Objetivos Claros: o problema (ex.: fadiga de alertas, complexidade de
  logs) e a solução agêntica são explícitos?
- QA2 Metodologia Replicável: arquitetura, tecnologias, parâmetros e cenário
  experimental são detalhados o suficiente para replicação?
- QA3 Base de Evidências Sólidas: há validação empírica (experimento, estudo
  de caso industrial, simulação com métricas)? (toy example = P; teórico = N)
- QA4 Conclusões Coerentes: as conclusões derivam das evidências e as
  limitações são discutidas?
  Banda de qualidade: Alta ≥ 3.0 | Média 1.5–2.5 | Baixa < 1.5.

# SAÍDA (3 tabelas + parecer)

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
(uma linha por RQ, 5 linhas; última linha com SCORE_RQ total)

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |

## Parecer final do revisor

- Síntese (3–5 linhas) sobre aderência do estudo às RQs e ao escopo da RSL.
- Recomendação: INCLUIR / INCLUIR COM RESSALVAS / EXCLUIR — justificada.
- Pendências de verificação externa (se houver).
