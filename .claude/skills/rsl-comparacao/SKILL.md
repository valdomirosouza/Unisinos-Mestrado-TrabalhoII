---
name: rsl-comparacao
description: Etapa 8 do ciclo RSL — comparar os três avaliadores (κ de Cohen por par, Fleiss, prevalência), classificar divergências e propor PDRs para as protocolares.
---

# /rsl-comparacao

Execute a etapa 8 do `WORKFLOW.md`:

1. Monte `reviews/comparacao-avaliadores.csv` (header:
   `templates/comparacao-avaliadores.csv`) com escores e recomendação dos três
   avaliadores por estudo.
2. Compute: `python3 scripts/compute-kappa.py --csv reviews/comparacao-avaliadores.csv`
   - Regra de colapso: "incluir"/"mantido" (case-insensitive) = Incluir.
   - Reporte **acordo percentual E κ** (o paradoxo da prevalência deflaciona o
     κ quando quase tudo é Incluir) e rotule a banda honestamente
     (Landis & Koch: 0.41–0.60 _moderate_, 0.61–0.80 _substantial_).
3. Classifique cada divergência: **protocolar** (os escores concordam, a regra
   de consequência difere) → proponha um PDR; **de mérito** (leitura do
   conteúdo difere) → reavaliação cega do estudo.
4. Documente em `reviews/comparacao-avaliadores.md` (famílias de divergência,
   quem diverge, regra em aberto) e atualize o índice canônico.

Escores `NA` (estudo não avaliado por um dos três) ficam fora das médias de
diferença — o script já trata.
