# Busca de Candidatos — Descoberta de Artigos (Etapa 1 da RSL)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](../reviews/DASHBOARD.md) · [📄 Relatório de síntese](../reviews/relatorio-sintese.md) · [📚 Pareceres](../reviews/README.md)

Primeira etapa da **Revisão Sistemática da Literatura (RSL)** _"Agentic AI como copilot para reduzir MTTD e MTTR e a carga cognitiva na resposta a incidentes"_ (PPGCA · Unisinos): descoberta, normalização, deduplicação e triagem de novos estudos que possam ampliar o corpus fundacional P01–P19.

O prompt original foi executado em **Gemini**, **Claude** e **ChatGPT** para ampliar cobertura e reduzir dependência de uma única ferramenta. Os resultados brutos originaram os candidatos P20–P40, posteriormente submetidos a verificação bibliométrica, avaliação integral e síntese.

> ⚠️ **Os relatórios de descoberta são insumos exploratórios.** As saídas dos assistentes não constituem inclusão final. Metadados não confirmados permanecem `UNVERIFIED`, e a decisão final depende de verificação rastreável e leitura integral.

## 🔎 O que há aqui

| Arquivo                                                    | Assistente | Idioma | Candidatos* | Formato                                                                    |
| ---------------------------------------------------------- | ---------- | ------ | :---------: | -------------------------------------------------------------------------- |
| [`prompt.md`](prompt.md)                                   | —          | EN     |      —      | Prompt reprodutível de descoberta, triagem e atualização da RSL            |
| [`gemini-research-report.md`](gemini-research-report.md)   | Gemini     | EN     |     ~20     | Relatório narrativo extenso, candidatos agrupados por tópico               |
| [`claude-research-report.md`](claude-research-report.md)   | Claude     | EN     |     16      | TL;DR + tabela de candidatos agrupada por tópico-alvo                      |
| [`chatgpt-research-report.md`](chatgpt-research-report.md) | ChatGPT    | PT     |     15      | Tabelas por tema + bloco `CAVEATS`                                         |

\* Registros reportados por cada assistente antes de deduplicação e verificação externa.

## 🧭 Prompt de busca v3.0.0

O [`prompt.md`](prompt.md) foi revisado após a auditoria dos artefatos P01–P40. A v3 transforma a descoberta em uma execução reprodutível e separa claramente **registro recuperado**, **estudo deduplicado**, **candidato triado**, **texto completo avaliado** e **estudo incluído**.

Principais melhorias:

- **Memória PRISMA corrigida:** distingue os **39 textos completos do repositório** do conjunto de **33 estudos incluídos na síntese**. Registra o fluxo ≈51 → 21 → 20 → 18 → 14 e exige contagens reconciliáveis por etapa.
- **PICOC e lacunas P01–P40:** incorpora a regra de Comparison com baseline empírico, a distribuição final 26/11/2, a ausência de medição nominal de MTTD/MTTR, a ausência de medição direta de carga cognitiva e a escassez de estudos em produção.
- **Recall documentado corretamente:** a string validada recupera 13/14 incluídos; **P24 é a única perda entre os incluídos**. P26, P38 e P39 são perdas desejáveis por terem sido excluídos ou considerados inelegíveis.
- **Busca complementar obrigatória:** backward/forward snowballing é exigido porque P01 não está indexado no Scopus e P24 não é recuperado pela consulta principal.
- **APIs e proveniência:** OpenAlex, Crossref, Scopus, Semantic Scholar e OpenCitations/COCI, além de QUALIS, SCImago, Portal CAPES e páginas dos editores.
- **DOI e versões:** normalização, DOI canônico da versão de registro, preservação de preprint/versões alternativas e deduplicação por linhagem.
- **Conferências separadas:** papers de conferência ficam em `SUPPLEMENTARY_EVIDENCE`, evitando aplicar silenciosamente Qualis Periódicos a proceedings.
- **Saída auditável:** `RUN_METADATA`, `SEARCH_LOG`, contagens PRISMA da execução, candidatos em JSON, logs de exclusão e deduplicação e bloco de desvios/caveats.
- **Sem preenchimento de quota:** a execução retorna menos candidatos quando poucos atendem aos critérios. Não são admitidos itens fracos ou não verificáveis apenas para atingir um número.

## 🔁 Da descoberta à avaliação

```text
prompt.md
   │
   ├── busca em bases + snowballing
   │
   ├── registros brutos + proveniência
   │
   ├── normalização e deduplicação
   │
   ├── triagem título/resumo
   │
   └── verificação bibliométrica
             │
             ├── PRIMARY_ELIGIBLE_CANDIDATE
             ├── SUPPLEMENTARY_EVIDENCE
             ├── PENDING_VERIFICATION
             └── EXCLUDED
                       │
                       ▼
          leitura integral + prompts/ + docs/ + reviews/
                       │
                       ▼
                 decisão de inclusão
```

## 📁 Estrutura da subpasta

```text
research/
├── README.md                     ← este arquivo
├── prompt.md                     ← prompt de busca/triagem v3.0.0
├── gemini-research-report.md     ← saída histórica do Gemini
├── claude-research-report.md     ← saída histórica do Claude
└── chatgpt-research-report.md    ← saída histórica do ChatGPT
```

As saídas históricas foram produzidas com a v1.0.0 e são preservadas como evidência do ciclo original. A v3.0.0 governa os próximos ciclos de atualização.
