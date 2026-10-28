---
name: rsl-triagem
description: Etapas 2 e 4 do ciclo RSL — elegibilidade bibliométrica (critérios I1–I5) e triagem PRISMA com evidência da extração PICOC (I6/E2/E3), gerando o artefato de triagem do ciclo.
---

# /rsl-triagem

Execute as etapas 2 e 4 do `WORKFLOW.md`:

1. **Elegibilidade (etapa 2):** para cada candidato do ciclo, verifique I1–I5
   em `protocolo/criterios.md` com dados do `Papers_Index.csv`. Gere
   `papers-cicloN.csv`. Estratos fora de I3/I4 só avançam se um PDR autorizar
   (com ressalva obrigatória).
2. **Triagem PRISMA (etapa 4 — exige a extração PICOC pronta):** aplique
   I6/E2/E3 citando a evidência de leitura integral e precedentes de ciclos
   anteriores. Preencha `templates/triagem.md` como
   `reviews/triagem-cicloN.md`.
3. Atualize o diagrama PRISMA (`reviews/PRISMA.md`) como **seção nova do
   ciclo** — nunca reescreva o diagrama de ciclos anteriores (Art. VI).
4. Rode `bash scripts/check-rsl.sh` antes do commit.

Toda exclusão cita critério + evidência. Caso-limite sem regra clara → pare e
proponha um PDR antes de decidir.
