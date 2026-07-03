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

O [`prompt.md`](prompt.md) instrui o assistente a operar como especialista em RSL sob Kitchenham et al. (2009) e retornar **15–25 candidatos** que estendam o corpus, obedecendo aos critérios de inclusão:

- **String de busca:** `("Agentic AI" OR "Multi-Agent System*") AND ("Incident Response" OR "Incident Management" OR "Incident Resolution" OR "AIOps" OR "LLM4AIOps" OR "Root Cause Analysis" OR "MTTR" OR "MTTD" OR "HITL" OR "HOTL")`
- **Fontes:** IEEE Xplore, Elsevier ScienceDirect, ACM DL (+ MDPI/Springer/Nature indexados que passem nos critérios).
- **Critérios de inclusão (todos):** ano ∈ [2020, 2026] · Qualis ∈ {A1, A2} · SJR ∈ {Q1, Q2} · citações ≥ 1 (com `RECENCY_EXCEPTION` para publicações < 12 meses) · revisado por pares.
- **Deduplicação:** nenhum dos 19 estudos do corpus (P1–P19); `author_overlap` marcado quando há autores em comum.
- **Tópicos-alvo (T1–T8):** execução autônoma segura/reversível (T1), telemetria complexa com LLMs (T2), integridade de memória (T3), governança/risco adversarial (T4), raciocínio causal (T5), eficiência/SLMs/edge (T6), frameworks e arquiteturas multiagente/HITL-HOTL (T7), evidência quantitativa de MTTR/MTTD (T8).
- **Anti-fabricação:** nunca inventar DOI/autor/venue/métrica; o que não puder ser confirmado é marcado `UNVERIFIED`; bloco `CAVEATS` obrigatório ao final.

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
