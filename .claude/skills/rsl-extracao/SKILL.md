---
name: rsl-extracao
description: Etapas 3 e 9 do ciclo RSL — extração PICOC de leitura integral (pré-triagem) e fichas estruturadas de extração dos estudos incluídos.
---

# /rsl-extracao

Execute a etapa 3 (PICOC) ou a etapa 9 (fichas) do `WORKFLOW.md`:

**Etapa 3 — PICOC pré-triagem:**

1. Renderize `templates/prompt-extracao-picoc.md` para os candidatos do ciclo.
2. Um agente de leitura por PDF (fan-out); fallback de extração de texto se não
   houver renderizador. Em caso de interrupção, confira em disco o que já foi
   escrito e relance só os faltantes.
3. Consolide em `picoc/picoc-results-cicloN.md` com apêndice de raciocínio.

**Etapa 9 — fichas dos incluídos:**

1. Para cada estudo incluído, gere a ficha estruturada (11 campos, com âncora
   de evidência seção/página por claim) em `report/PXX-extraction.csv` (+ a
   variante traduzida, se a instância usar).
2. Consolide em `report/consolidated-extraction-cicloN.csv`; indexe tudo no
   `report/README.md`.

_Comparison_ declarado só com comparação empírica executada (Art. I).
