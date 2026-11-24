# replication/ — Pacote de replicação (passo 3 do plano de conformidade)

Infraestrutura para gerar o **pacote de replicação** da RSL a ser
depositado em repositório confiável (Zenodo) com DOI, atendendo o art.
9º-I-g da Portaria CNPq nº 2.664/2026 e a pendência C7.4 do parecer
PPGCA. Plano: [`docs/DOU/plano-melhorias-artigo-portarias-CNPq.md`](../docs/DOU/plano-melhorias-artigo-portarias-CNPq.md) (item A4).

## Arquivos

- [`manifest.txt`](manifest.txt) — whitelist do que entra no pacote (protocolo, templates, prompts, picoc, reviews, report, research, scripts e os CSVs bibliométricos da raiz). **Política:** nada de `docs/` (PDFs com copyright — substituídos pelos metadados/DOIs em `papers*.csv` e `referencias.csv`) e nenhuma credencial.
- [`package-README.md`](package-README.md) — README em inglês injetado na raiz do pacote (estrutura, instruções de reprodução do κ/PRISMA, nota de proveniência e licenças).
- [`../scripts/build-replication-package.py`](../scripts/build-replication-package.py) — builder: copia pelo manifesto, **veta** `docs/`/credenciais, **varre vazamento** do conteúdo de `.scopus_key` em todos os arquivos, gera `MANIFEST.csv` (caminho/bytes/sha256), compacta em `dist/agentic-ir-slr-replication-<versão>.zip` e imprime o SHA-256 do zip.

## Como gerar

```bash
python3 scripts/build-replication-package.py --version v1.0.0
```

Saída em `dist/` (ignorada pelo git). O SHA-256 impresso deve ser
registrado na descrição do depósito Zenodo.

## Fluxo do depósito (pendente — requer ação do condutor)

1. Gerar o zip com a versão definitiva (sugestão: `v1.0.0` na submissão do artigo).
2. Criar o depósito no Zenodo (comunidade: a definir; licença: código sob a `LICENSE` do repo, dados/documentos CC BY 4.0), anexar o zip e publicar o SHA-256.
3. Reservar/obter o **DOI** e preenchê-lo na seção _Data Availability_ do artigo (marcador `[DOI pendente]` em `artigo/main.tex`).
4. Registrar versão e DOI no MEMORY.md e no `CHANGELOG.md`.
