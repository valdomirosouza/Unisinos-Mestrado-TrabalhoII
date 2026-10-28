# PDR-0006 — Estrato de conference papers pelo percentil Scopus da série

- **Status:** ratificado
- **Data:** 2026-10-28
- **Condutor:** Valdomiro de Oliveira Souza Jr.
- **Artigos da constituição afetados:** Art. I (critérios I3/I4)

## Contexto

O ciclo 3 trouxe os primeiros **conference papers** da revisão (26 de 37
candidatos; ciclos 1–2 foram 100% journals). Os critérios I3 (Qualis A1–A2) e
I4 (SJR Q1–Q2) são estratos de periódico e não definem tratamento para
proceedings — caso-limite sem regra, levado ao condutor antes da Etapa 1
(Constituição; skill `/rsl-triagem`).

## Decisão

O estrato de um conference paper é derivado do **percentil CiteScore (Scopus)
da série de proceedings** em que foi publicado (ex.: LNCS, CCIS, LNNS,
Procedia CS, séries de conferências IEEE com ISSN), pela mesma régua
percentil→Qualis calibrada em `papers.csv`. **Evento cuja série não possui
CiteScore no Scopus é INELEGÍVEL** na Etapa 1. A verificação inclui busca por
ISSN e por título da série (`serial/title` API), registrada em
`research/ciclo3-data/c3-conf-series.json`.

## Consequências (ciclo 3)

- Séries aferidas: LNCS 44% (B1), CCIS 28% (B2), LNNS 22% (B3), Procedia CS
  53% (A4), SOUTHEASTCON 37% (B2), EIT 42% (B1), GLOBECOM 54% (A4), ISDFS 11%
  (B4) — todas sub-A2, seguindo com ressalva de estrato sob o
  [PDR-0007](PDR-0007-renovacao-da-emenda-de-estratos-para-o-ciclo-3.md).
- 16 candidatos INELEGÍVEIS por série sem CiteScore (P90, P96, P98, P99,
  P103, P104, P105, P107, P111, P115, P116, P117, P118, P120, P124, P125).
- **Nota do condutor registrada:** P90 — o candidato mais citado da descoberta
  (OA 7 · CR 7 · SC 6) — sai por esta regra; o snowballing obrigatório do
  protocolo permanece como rota de recaptura, e nova decisão pode revisitar o
  caso.
