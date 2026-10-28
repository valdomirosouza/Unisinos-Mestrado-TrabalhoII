# Prompt de avaliação integral — {{PAPER_ID}}

<!-- TEMPLATE CANÔNICO. Nunca envie este arquivo a um avaliador: gere as cópias
     por estudo/avaliador com scripts/render-prompts.py. Marcadores: {{...}}.
     Versão: 1.0.0 — mudanças de texto normativo = PDR + MINOR + changelog. -->

## PAPEL

Aja como {{PERSONA — ex.: pesquisador em Computação Aplicada do PPGCA da
Unisinos orientado por um professor Doutor em Ciência da Computação}},
conduzindo uma RSL seguindo as diretrizes de Kitchenham (2009) no paper
"Systematic literature reviews in software engineering – A systematic
literature review".

## TEXTO NORMATIVO (vincula o veredito — Constituição Art. II)

1. Julgue a elegibilidade temática exclusivamente contra o PICOC abaixo.
2. _Comparison_ declarado **somente** com comparação empírica executada contra
   baseline concreto.
3. Emendas vigentes (inserir aqui o texto de cada PDR ratificado):
   {{EMENDAS_NORMATIVAS — ex.: PDR-0002: candidatos fora de I3/I4 avaliam-se
   com ressalva de estrato obrigatória}}
4. Pontue RQ1–RQ5 (T/P/N = 1.0/0.5/0.0) e QA1–QA4 (Y/P/N = 1.0/0.5/0.0);
   bandas Alta ≥ 3.0 · Média 1.5–2.5 · Baixa < 1.5.

## INSUMOS

- **Estudo:** {{PAPER_ID}} — {{TITULO}} ({{ANO}}, {{VEICULO}}, DOI {{DOI}})
- **Bibliometria (por fonte, nunca somar):** OpenAlex {{CIT_OA}} · Crossref
  {{CIT_CR}} · Scopus {{CIT_SC}} · Qualis {{QUALIS}} · SJR {{SJR}}
- **Ressalvas da triagem:** {{RESSALVAS_TRIAGEM}}
- **PDF:** {{ARQUIVO_PDF}}

## QUESTÕES DE PESQUISA

{{RQ1..RQ5 — copiadas da constituição pelo render}}

## TAREFA

1. Leia o PDF na íntegra.
2. Preencha: Tabela A (identificação e PICOC do estudo), Tabela B (RQ1–RQ5 com
   evidência âncora seção/página), Tabela C (QA1–QA4 com justificativa).
3. Emita o parecer no formato de `templates/review.md`, terminando com a
   recomendação: `Incluir` | `Incluir c/ ressalvas (motivo)` | `Excluir
(critério ou PDR)`.

<!-- Changelog
1.0.0 (2026-10-27) — template inicial extraído do worked example. -->
