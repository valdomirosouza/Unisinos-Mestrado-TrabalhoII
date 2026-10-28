---
name: rsl-descoberta
description: Etapa 1 do ciclo RSL — descobrir candidatos executando a string de busca nas bases (OpenAlex, Scopus, Portal CAPES) e registrá-los no índice canônico com PDFs em docs/.
---

# /rsl-descoberta

Execute a etapa 1 do `WORKFLOW.md`:

1. Leia `protocolo/picoc.md` (string de busca) e `protocolo/constituicao.md`.
2. Execute a busca nas bases configuradas; deduplique contra o corpus existente
   (todos os ciclos) e entre assistentes/bases.
3. Para cada candidato novo: linha no `Papers_Index.csv` (ID sequencial PXX,
   DOI, veículo, ano; citações **por fonte** — Art. V) e PDF em `docs/`.
4. Registre volume bruto, deduplicação e recall de calibração no artefato de
   descoberta do ciclo (`research/` ou equivalente).
5. Rode `bash scripts/check-rsl.sh` e indexe os arquivos novos nos READMEs.

Nunca some citações de fontes diferentes. `NÃO INDEXADO` ≠ 0.
