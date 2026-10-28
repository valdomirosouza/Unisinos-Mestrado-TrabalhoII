# Estrutura esperada da instância

Depois do `adopt.sh`, a revisão cresce nestas pastas (todas com README de
índice — o check C3 falha para arquivo não indexado):

```text
Papers_Index.csv        índice canônico de candidatos (fonte de verdade; Art. VII)
Papers_Index.md         derivado — scripts/derive-index.py (nunca editar à mão)
docs/                   PDFs dos candidatos (um por linha do índice)
research/               descoberta: execuções da string de busca por base/assistente
picoc/                  extrações PICOC consolidadas por ciclo
prompts/                prompts renderizados por estudo (saída do render-prompts.py)
reviews/                pareceres (review-PXX.md + pastas por avaliador),
                        triagem-cicloN.md, PRISMA.md, resultados-consolidados*.csv,
                        comparacao-avaliadores.*, dashboard e síntese
report/                 fichas de extração por estudo + consolidados
protocolo/              constituição, PICOC, critérios e PDRs (este template)
MEMORY.md               log de memória por sessão (Art. IX) — itens numerados,
                        prompt → ações → comandos → incidentes, commitados
```

Convenções herdadas do worked example:

- IDs sequenciais `P01, P02, …` atravessando ciclos; duplicatas mantêm o ID
  aposentado (nunca reutilize um ID).
- Artefato histórico ganha **nota de versão/errata**, nunca reescrita.
- Chaves de API em arquivos `.gitignore`-ados; o check C4 varre vazamentos.
