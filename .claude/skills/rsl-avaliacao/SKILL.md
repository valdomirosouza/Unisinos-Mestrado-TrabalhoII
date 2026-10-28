---
name: rsl-avaliacao
description: Etapas 5 e 6 do ciclo RSL — gerar os prompts de avaliação a partir do template canônico (render-prompts.py) e executar os pareceres dos três avaliadores independentes.
---

# /rsl-avaliacao

Execute as etapas 5 e 6 do `WORKFLOW.md`:

1. **Prompts (etapa 5):** gere com o render — nunca à mão:

   ```bash
   python3 scripts/render-prompts.py --index Papers_Index.csv \
     --ids PXX,PYY --emendas "<texto normativo dos PDRs vigentes>"
   ```

   As emendas entram no **texto normativo** (Art. II). Um marcador não
   resolvido = prompt incompleto; não envie.

2. **Pareceres (etapa 6):** execute cada prompt com o PDF para cada um dos
   três avaliadores, de forma independente (sem ver o parecer dos outros).
   Saída no formato `templates/review.md`:
   - avaliador 1 → `reviews/review-PXX.md`
   - avaliadores 2 e 3 → `reviews/<Avaliador>/PXX_avaliacao_RSL.md`

3. Pontue conforme Art. IV (SCORE_RQ máx. 5.0; SCORE_QA máx. 4.0 com bandas).
4. Indexe os pareceres no `reviews/README.md`; rode `bash scripts/check-rsl.sh`.

Pareceres publicados são imutáveis (Art. VI) — refação vira artefato novo.
