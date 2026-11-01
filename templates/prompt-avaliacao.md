# Prompt de avaliação integral — {{PAPER_ID}}

<!-- TEMPLATE CANÔNICO. Nunca envie este arquivo a um avaliador: gere as cópias
     por estudo/avaliador com scripts/render-prompts.py. Marcadores: {{...}}.
     Versão: 1.3.0 — mudanças de texto normativo = PDR + MINOR + changelog. -->

## PAPEL

Aja como {{PERSONA}}, conduzindo uma RSL seguindo as diretrizes de Kitchenham (2009) no paper
"Systematic literature reviews in software engineering – A systematic
literature review".

## TEXTO NORMATIVO (vincula o veredito — Constituição Art. II)

1. Julgue a elegibilidade temática exclusivamente contra o PICOC abaixo.
2. _Comparison_ declarado **somente** com comparação empírica executada contra
   baseline concreto.
3. Emendas vigentes (texto de cada PDR ratificado, via `--emendas`):
   {{EMENDAS_NORMATIVAS}}
4. Pontue RQ1–RQ5 (T/P/N = 1.0/0.5/0.0) e QA1–QA4 (Y/P/N = 1.0/0.5/0.0);
   bandas Alta ≥ 3.0 · Média 1.5–2.5 · Baixa < 1.5.

## INSUMOS

- **Estudo:** {{PAPER_ID}} — {{TITULO}} ({{ANO}}, {{VEICULO}}, DOI {{DOI}})
- **Bibliometria (por fonte, nunca somar):** OpenAlex {{CIT_OA}} · Crossref
  {{CIT_CR}} · Scopus {{CIT_SC}} · Qualis {{QUALIS}} · SJR {{SJR}}
- **Ressalvas da triagem:** {{RESSALVAS_TRIAGEM}}
- **PDF:** {{ARQUIVO_PDF}}

## QUESTÕES DE PESQUISA

{{RQS}}

## TAREFA

1. Leia o PDF na íntegra.
2. Preencha: Tabela A (identificação e PICOC do estudo), Tabela B (RQ1–RQ5 com
   evidência âncora seção/página), Tabela C (QA1–QA4 com justificativa).
3. Emita o parecer no formato de `templates/review.md`, terminando com a
   recomendação: `Incluir` | `Incluir c/ ressalvas (motivo)` | `Excluir
(critério ou PDR)`.

---

**Rodapé obrigatório da resposta (comprovação de versão):** encerre o
arquivo MD da resposta com a linha abaixo, preenchida no momento da
execução:

`Executado por: <nome e versão exatos do modelo> | Execução: <AAAA-MM-DD HH:MM (fuso)>`

<!-- Changelog
1.3.0 (2026-11-01) — rodapé obrigatório da resposta: a saída MD deve terminar
com a linha "Executado por: <modelo e versão> | Execução: <data/hora>", para
comprovação futura das versões (decisão do condutor, 2026-11-01; aplicada
retroativamente a todos os prompts renderizados em prompts/). Não normativo.
Nota: a 1.2.0 existe apenas no repo Template-RSL (renomeação dos marcadores de
estrato, PERCENTIL_SCOPUS/SJR_QUARTIL) e será adotada nesta instância junto com
o texto normativo do PDR-0009, no próximo ciclo que renderizar prompts.
1.1.0 (2026-10-28) — marcadores instrucionais ({{PERSONA — ex.: …}},
{{EMENDAS_NORMATIVAS — ex.: …}}, {{RQ1..RQ5 — …}}) trocados por marcadores
limpos {{PERSONA}}, {{EMENDAS_NORMATIVAS}} e {{RQS}}, resolvíveis pelo
render-prompts.py ou reportados como "preencher na instância" (PERSONA e RQS
são preenchidos pela instância pós-render). Não normativo.
1.0.0 (2026-10-27) — template inicial extraído do worked example. -->
