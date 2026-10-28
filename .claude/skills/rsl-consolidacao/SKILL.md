---
name: rsl-consolidacao
description: Etapas 7 e 9 do ciclo RSL — consolidar pareceres em CSV canônico, gráficos, PRISMA e dashboard; atualizar a síntese narrativa com adendos datados.
---

# /rsl-consolidacao

Execute a etapa 7 (e o fecho da 9) do `WORKFLOW.md`:

1. Consolide os pareceres do ciclo em
   `reviews/resultados-consolidados-cicloN.csv`
   (header: `templates/resultados-consolidados.csv`). O CSV é a fonte de
   verdade — todo número da síntese deriva dele (Art. VII).
2. Gere os gráficos do ciclo e o resumo no dashboard. Atenção à armadilha do
   worked example: **média ≠ mediana** — rotule cada estatística corretamente.
3. Atualize o `Papers_Index.csv` (status + escores dos 3 avaliadores) e derive
   o MD: `python3 scripts/derive-index.py --csv Papers_Index.csv --out Papers_Index.md`.
4. Síntese narrativa: ciclos anteriores não são reescritos — acrescente
   **adendos datados** (Art. VI) e regenere o PDF da síntese, se houver.
5. Rode `bash scripts/check-rsl.sh` (o C5 confere parecer-a-parecer contra o
   CSV) antes do commit.
