# Busca de Candidatos — Descoberta de Artigos (Etapa 1 da RSL)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](../reviews/DASHBOARD.md) · [📄 Relatório de síntese](../reviews/relatorio-sintese.md) · [📚 Pareceres](../reviews/README.md)

Primeira etapa da **Revisão Sistemática da Literatura (RSL)** _"Agentic AI como copilot para reduzir MTTD e MTTR na resposta a incidentes"_ (PPGCA · Unisinos): a **descoberta de novos artigos candidatos** para ampliar o corpus existente (P1–P19). O mesmo prompt de busca foi executado em três assistentes de IA — **Gemini**, **Claude** e **ChatGPT** — para comparar cobertura e reduzir viés de uma única ferramenta. Os candidatos resultantes desta etapa alimentam a triagem e a avaliação detalhada dos estudos **P20–P40** (ver [`reviews/`](../reviews/)).

> ⚠️ **Insumos exploratórios, não verificados.** Estes relatórios são a **saída bruta** dos assistentes. Seguindo a lógica anti-fabricação de Kitchenham et al. (2009), a maioria dos campos **Qualis**, **SJR (quartil)** e **citações** permanece `UNVERIFIED` — os assistentes não conseguiram confirmá-los de forma rastreável em Scimago / Qualis (qualis.pages.dev) durante a sessão. Preprints e artigos de conferência estão sinalizados (`PREPRINT` / `CONFERENCE`) e **não** foram aceitos sem verificação posterior.

## 🔎 O que há aqui

| Arquivo                                                    | Assistente | Idioma | Candidatos\* | Formato                                                                    |
| ---------------------------------------------------------- | ---------- | ------ | :----------: | -------------------------------------------------------------------------- |
| [`prompt.md`](prompt.md)                                   | —          | EN     |      —       | Prompt de busca/triagem executado (papel, critérios, tópicos-alvo, schema) |
| [`gemini-research-report.md`](gemini-research-report.md)   | Gemini     | EN     |     ~20      | Relatório narrativo extenso, candidatos agrupados por tópico T1–T8         |
| [`claude-research-report.md`](claude-research-report.md)   | Claude     | EN     |      16      | TL;DR + tabela de candidatos agrupada por tópico-alvo                      |
| [`chatgpt-research-report.md`](chatgpt-research-report.md) | ChatGPT    | PT     |      15      | Tabelas por tema + bloco `CAVEATS`                                         |

\* Número de linhas-candidato (`Cxx`) reportadas por cada assistente, antes de deduplicação e verificação externa.

## 🧭 Prompt de busca (resumo)

O [`prompt.md`](prompt.md) (**v2.0.0** — revisado após o ciclo 1; os relatórios desta pasta são saídas da **v1.0.0**) instrui o assistente a operar como especialista em RSL sob Kitchenham et al. (2009) e retornar **15–25 candidatos** que estendam o corpus. A v2 embute uma **`PROJECT_MEMORY`** com o estado verificado da revisão:

- **PRISMA (PM-1):** fluxo do ciclo 1 (≈51 → 21 → 20 → 18 → 14; corpus final 33) e critérios I1–I6 / E1–E5 com os casos concretos de exclusão.
- **PICOC (PM-2):** elementos da revisão com a regra v1.1.0 de Comparison (só baseline empírico) e o achado central — nenhum dos 39 estudos mede MTTD/MTTR nominalmente → estudos com métricas operacionais nomeadas são prioridade máxima.
- **String validada (PM-3):** blocos Intervention × Context derivados do PICOC, calibrados no corpus (recall 13/14 em Scopus e OpenAlex), com o caveat de sintaxe do Scopus (`TITLE-ABS-KEY` por bloco).
- **APIs e fontes (PM-4):** OpenAlex, Crossref, Scopus (com quirks documentados: `REF()` por título; F1000Research não indexada), QUALIS (qualis.pages.dev), SCImago e Portal CAPES/CAFe; armadilha do DOI de preprint (caso P09) — exigir DOI da versão de registro.
- **Deduplicação:** nenhum dos **39** estudos P01–P40 (incl. variantes de DOI de preprint); `author_overlap` e novo `group_provenance` (independência de grupos).
- **Tópicos-alvo (T1–T9):** T8 (evidência quantitativa de MTTD/MTTR) promovido a **prioridade máxima** e novo T9 (implantações em produção); T4 anotado com a lacuna sistemática de RQ4. Cota mínima: ≥1/3 dos candidatos em T8/T9.
- **Anti-fabricação:** nunca inventar DOI/autor/venue/métrica; `UNVERIFIED` + bloco `CAVEATS` obrigatórios; novo campo `picoc_fit` ancora cada candidato nos elementos PICOC.

## 🔁 Da descoberta à avaliação

```
prompt.md ──► Gemini / Claude / ChatGPT ──► *-research-report.md   (esta pasta: candidatos brutos)
                                                     │
                                                     ▼
                             triagem + verificação externa (Qualis/SJR/citações)
                                                     │
                                                     ▼
                         corpus P20–P40 ──► prompts/ + docs/ + reviews/   (avaliação detalhada)
```

Os candidatos convergentes e verificáveis desta etapa deram origem aos estudos **P20–P40** avaliados em [`reviews/`](../reviews/). Consulte o [Dashboard](../reviews/DASHBOARD.md) e o [relatório de síntese](../reviews/relatorio-sintese.md) para o resultado da avaliação.

## 📁 Estrutura da subpasta

```
research/
├── README.md                     ← este arquivo
├── prompt.md                     ← prompt de busca/triagem (EN)
├── gemini-research-report.md     ← resultado do Gemini  (relatório narrativo, ~20 candidatos)
├── claude-research-report.md     ← resultado do Claude   (tabela, 16 candidatos)
└── chatgpt-research-report.md    ← resultado do ChatGPT  (tabelas + CAVEATS, 15 candidatos)
```
