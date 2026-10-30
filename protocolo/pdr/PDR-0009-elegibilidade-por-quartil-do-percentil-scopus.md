# PDR-0009 — Elegibilidade por quartil do percentil Scopus (Q1–Q3); Qualis/SJR informativos

- **Status:** ratificado
- **Data:** 2026-10-30
- **Condutor:** Valdomiro de Oliveira Souza Jr.
- **Artigos da constituição afetados:** Art. I (critérios I3/I4)

## Contexto

A revisão será publicada internacionalmente (artigo IEEE Access). O estrato
**Qualis/CAPES é uma classificação nacional brasileira sem validade
internacional**, e o quartil SJR era sua operacionalização auxiliar (I4).
Decisão do condutor em 2026-10-30: "Como é uma publicação internacional o
Estrato Qualis/CAPES não tem validade e vamos seguir a partir de agora
apenas com o critério de Scopus (Percentil) = Q1, Q2 ou Q3 como elegíveis",
com alcance **retroativo com ressalva** (opção escolhida pelo condutor após
análise de impacto sobre o corpus de 65 incluídos).

## Decisão

1. Os critérios I3 (Qualis A1–A2) e I4 (SJR Q1–Q2) são substituídos por um
   único critério de qualidade de veículo: o **percentil CiteScore (Scopus)**
   do periódico — ou da série de proceedings, pela regra do
   [PDR-0006](PDR-0006-estrato-de-conference-papers-pelo-percentil-da-serie.md),
   que permanece vigente — mapeado em quartis: **Q1 (≥ 75%), Q2 (50–74%) e
   Q3 (25–49%) são ELEGÍVEIS; Q4 (< 25%) e veículos sem CiteScore no Scopus
   são INELEGÍVEIS.**
2. **Aplicação retroativa com ressalva:** os incluídos dos ciclos 0–3 abaixo
   da régua — **P91 (não indexado), P101 (Q4, 11%) e P102 (não indexado)** —
   **permanecem no corpus com ressalva obrigatória reformulada**
   ("abaixo da régua Q1–Q3 — PDR-0009"), no precedente das emendas
   PDR-0002/PDR-0007. Nenhum estudo sai do corpus (65 mantido).
3. **Ressalvas de estrato Qualis anteriores perdem efeito** para estudos em
   Q1–Q3 (ex.: P62/P69 "A3" = Q2; P100 "B2 série" = Q3; P123 "A3" = Q2) —
   as ressalvas de **mérito** (evidência sintética, fundacional-condicional
   R1, agência limitada etc.) não mudam.
4. Qualis e SJR Quartile tornam-se **colunas informativas** do
   `Papers_Index.csv`, sem papel de elegibilidade.

## Consequências

- Distribuição do corpus (65) na régua nova: **53 Q1 · 8 Q2 · 1 Q3 · 1 Q4 ·
  2 não indexados** — a elegibilidade internacional valida o corpus quase
  inteiro.
- **Cluster MTTD/MTTR nominal:** P100 (Q3) e P123 (Q2) passam a elegíveis
  sem ressalva de veículo; P101 e P102 mantêm a ressalva reformulada. O
  artigo deixa de qualificar o cluster como "entirely at sub-threshold
  venues".
- Decisões históricas dos ciclos 1–3 (funis, pareceres, κ) **não são
  reabertas** (Art. VI): este PDR re-lê as ressalvas, não os vereditos.
- Artigo (draft v2): §III-D, PRISMA, §IV, ameaças e conclusão reescritos na
  régua internacional; statuses de P91/P101/P102 no índice anotados.
- O P90 e os 16 inelegíveis por série sem CiteScore permanecem inelegíveis
  (regra equivalente na régua nova).

## Aplicação

- [x] Índice de PDRs atualizado
- [x] Statuses de P91/P101/P102 no `Papers_Index.csv` (+MD)
- [x] Nota datada no DASHBOARD; adendo na síntese consolidada (+PDF)
- [x] Artigo reescrito na régua internacional (abstract, método, resultados,
      ameaças, conclusão)
- [ ] Texto normativo dos prompts (`templates/prompt-avaliacao.md`) — a
      atualizar no próximo ciclo que renderizar prompts (MINOR + changelog)
