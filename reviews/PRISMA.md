# Diagrama PRISMA — Seleção de Estudos da RSL

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](DASHBOARD.md) · [📚 Pareceres](README.md) · [🔎 Descoberta](../research/README.md) · [🧩 PICOC](../picoc/picoc-comparacao-avaliadores.md)

Fluxo de seleção da RSL **"Agentic AI Copilot para Resposta a Incidentes"** no formato **PRISMA 2020** (adaptado para atualização de revisão: o corpus fundacional P01–P19 do Trabalho I entra como _estudos da revisão anterior_). Contagens auditáveis nos artefatos do repositório ([`research/`](../research/), [`reviews/`](README.md), [`Artigos-TrabalhoII.csv`](../Artigos-TrabalhoII.csv)).

## Diagrama

```mermaid
flowchart TB
    subgraph PREV["CORPUS PRÉVIO (Trabalho I)"]
        A0["Estudos incluídos na RSL fundacional<br/><b>n = 19</b> (P01–P19)"]
    end

    subgraph IDENT["IDENTIFICAÇÃO (Etapa 1 — research/)"]
        A1["Registros identificados via busca assistida por IA<br/>Gemini ≈ 20 · Claude = 16 · ChatGPT = 15<br/><b>n ≈ 51</b> registros-candidatos"]
        A2["Registros após deduplicação<br/>(vs. corpus P01–P19 e entre assistentes)<br/>e verificação externa (DOI/veículo)<br/><b>n = 21</b> candidatos (P20–P40)"]
        A3["Duplicata interna removida<br/>P36 = P31/LEMAD<br/><b>n = 1</b>"]
        A1 --> A2
        A2 --> A3
    end

    subgraph SCREEN["TRIAGEM (elegibilidade bibliométrica)"]
        B1["Candidatos triados<br/><b>n = 20</b> (P20–P35, P37–P40)"]
        B2["Excluídos na triagem — INELEGÍVEIS<br/>Qualis A3 (critério: A1–A2)<br/><b>n = 2</b> (P39, P40)"]
        B1 --> B2
    end

    subgraph ELIG["ELEGIBILIDADE (Etapa 2 — avaliação integral)"]
        C1["Artigos avaliados na íntegra<br/>(prompt + PDF; Tabelas A/B/C; RQ1–RQ5; QA1–QA4)<br/><b>n = 18</b>"]
        C2["Excluídos após avaliação — <b>n = 4</b><br/>• P26 — survey RCA não-agêntico (relevância/tipo)<br/>• P29 — SLR não-agêntica (relevância/tipo)<br/>• P30 — não-agêntico, bug-triage (relevância/tipo)<br/>• P38 — fora de domínio (agricultura)"]
        C1 --> C2
    end

    subgraph INCL["INCLUSÃO"]
        D1["Novos estudos incluídos<br/><b>n = 14</b><br/>7 plenos · 5 com ressalvas · 2 fundacionais condicionais (P24, P33)"]
        D2["<b>Corpus final da RSL: n = 33</b><br/>19 fundacionais (P01–P19) + 14 novos (P20–P37)"]
        D1 --> D2
    end

    A3 --> B1
    B2 --> C1
    C2 --> D1
    A0 --> D2
```

## Critérios de elegibilidade

### Critérios de inclusão (todos obrigatórios)

| #   | Critério                                                                                  | Verificação                                                                  |
| --- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| I1  | Ano de publicação ∈ [2020, 2026]                                                          | [`papers.csv`](../papers.csv) (coluna Year)                                  |
| I2  | Veículo identificável e revisado por pares (journal/conference)                           | [`papers.csv`](../papers.csv) (Venue, ISSN, DOI)                             |
| I3  | Qualis ∈ {A1, A2} (2025-2028)                                                             | [`papers.csv`](../papers.csv) — verificação externa concluída                |
| I4  | SJR ∈ {Q1, Q2}                                                                            | [`papers.csv`](../papers.csv) — verificação externa concluída                |
| I5  | Citações ≥ 1, com `RECENCY_EXCEPTION` para publicações < 12 meses                         | [`papers.csv`](../papers.csv) (colunas de citações OpenAlex/Crossref/Scopus) |
| I6  | Aderência temática: abordagem **agêntica** × **domínio IR/AIOps/SOC** (eixo da avaliação) | Pareceres [`review-Pxx.md`](README.md) (RQ1–RQ5)                             |

### Critérios de exclusão (qualquer um)

| #   | Critério                                                 | Aplicado a                       |
| --- | -------------------------------------------------------- | -------------------------------- |
| E1  | Qualis A3 ou inferior (inelegível na triagem)            | P39, P40                         |
| E2  | Abordagem não-agêntica (survey/pipeline sem agência)     | P26, P29, P30                    |
| E3  | Fora do domínio de resposta a incidentes/operações de TI | P38                              |
| E4  | Duplicata (interna ou do corpus prévio)                  | P36 (= P31/LEMAD)                |
| E5  | Não revisado por pares (preprint sem aceite)             | aplicado na Etapa 1 (descoberta) |

### Notas metodológicas

- **Estudos secundários (P24, P33):** incluídos como **fundacionais condicionais** — permanecem no corpus para fundamentação (RQ1/RQ4/RQ5); se o protocolo restringir a estudos primários, migram para a fundamentação e o corpus primário novo fica com **12** estudos.
- **Identificação assistida por IA:** os ≈51 registros brutos são a saída dos três assistentes ([`research/`](../research/README.md)), com campos não confirmáveis marcados `UNVERIFIED` (antifabricação); a verificação externa de Qualis/SJR foi concluída posteriormente em [`papers.csv`](../papers.csv).
- **Validação cruzada da seleção:** a triagem/avaliação teve comparação entre avaliadores (Claude × ChatGPT: concordância 90%, κ = 0,74 — [`comparacao-avaliadores.md`](comparacao-avaliadores.md)); a extração PICOC teve três avaliadores ([`picoc/`](../picoc/picoc-comparacao-avaliadores.md)).

---

_Formato PRISMA 2020 adaptado para atualização de revisão. Contagens: ≈51 identificados → 21 candidatos → 20 triados (−1 duplicata) → 18 avaliados (−2 inelegíveis A3) → 14 incluídos (−4 excluídos) → corpus final 33 (19 + 14)._
