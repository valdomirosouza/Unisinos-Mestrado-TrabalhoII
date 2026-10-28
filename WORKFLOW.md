# WORKFLOW — o ciclo canônico da RSL

Ordem validada no worked example (dois ciclos, 89 candidatos, 61 avaliações).
Cada etapa referencia a skill que a executa e os artefatos que produz.
Um "ciclo" é uma rodada completa sobre um lote de candidatos; a RSL pode ter
vários ciclos de atualização sobre um corpus fundacional (update review).

| #   | Etapa                                                | Skill               | Entrada                                                       | Saída                                                                        |
| --- | ---------------------------------------------------- | ------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 0   | **Protocolo** (uma vez)                              | —                   | `protocolo/` preenchido                                       | PICOC, RQs, critérios, string de busca                                       |
| 1   | **Descoberta** de candidatos                         | `/rsl-descoberta`   | string de busca + bases (OpenAlex, Scopus, Portal CAPES)      | linhas novas em `Papers_Index.csv` + PDFs em `docs/`                         |
| 2   | **Elegibilidade bibliométrica** (Etapa 1)            | `/rsl-triagem`      | `Papers_Index.csv`                                            | `papers-cicloN.csv` (DOI, veículo, Qualis, SJR, citações **por fonte**)      |
| 3   | **Extração PICOC** de leitura integral               | `/rsl-extracao`     | PDFs                                                          | `picoc/picoc-results-cicloN.md` (evidência para a triagem)                   |
| 4   | **Triagem PRISMA**                                   | `/rsl-triagem`      | etapas 2+3                                                    | `reviews/triagem-cicloN.md` — aprovados/excluídos com critério e evidência   |
| 5   | **Geração dos prompts** de avaliação                 | `/rsl-avaliacao`    | `templates/prompt-avaliacao.md` + `scripts/render-prompts.py` | `prompts/prompt-PXX.md` (um por aprovado, por avaliador)                     |
| 6   | **Avaliação integral** — 3 avaliadores independentes | `/rsl-avaliacao`    | prompts + PDFs                                                | `reviews/review-PXX.md` + pastas `ChatGPT/`, `Gemini/`                       |
| 7   | **Consolidação**                                     | `/rsl-consolidacao` | pareceres                                                     | `resultados-consolidados-cicloN.csv`, gráficos, PRISMA atualizado, dashboard |
| 8   | **Comparação entre avaliadores**                     | `/rsl-comparacao`   | 3 conjuntos de pareceres                                      | `comparacao-avaliadores.csv/.md` (κ por par, Fleiss, divergências → PDRs)    |
| 9   | **Fichas de extração + síntese**                     | `/rsl-consolidacao` | incluídos                                                     | `report/PXX-extraction.csv` + relatório de síntese (com adendos datados)     |

## Regras transversais

- **Decisão de protocolo no meio do ciclo?** Escreva um PDR
  (`protocolo/pdr/PDR-NNNN-*.md`) ANTES de aplicá-la, e aplique-a no texto
  normativo do prompt (constituição, Art. II do worked example — regra R2).
- **Divergência entre avaliadores?** Classifique: protocolar (vira PDR) ou de
  mérito (vira reavaliação). No worked example, 8/8 divergências eram protocolares.
- **Fim de cada etapa:** rode `bash scripts/check-rsl.sh` e registre a etapa no
  log de memória do projeto antes do commit.
