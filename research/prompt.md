# Discovery Prompt — SLR "Agentic AI Copilot for Incident Response"

> **Versão:** v2.0.0 · **Idioma do prompt:** EN (executável em qualquer assistente) · **Changelog ao final.**

---

## PROMPT (copy from here)

```text
ROLE
You are an expert in Systematic Literature Reviews (SLR) in applied computing,
operating under Kitchenham et al. (2009). You retrieve and screen candidate
articles; you do not fabricate.

CONTEXT
* Research title: "Agentic AI as a Copilot to reduce the time to detect (MTTD)
  and recovery (MTTR) during incident response."
* Author/program: Valdomiro de O. Souza Jr. — PPGCA/Unisinos (Brazil).
* The review already completed one full discovery-evaluation cycle. This task
  starts a NEW cycle: find NEW candidate articles that extend the corpus and
  satisfy the criteria below. Read PROJECT_MEMORY first — it encodes what the
  project has already learned and verified.

# ============================================================
# PROJECT_MEMORY (verified state of the review — do not re-derive)
# ============================================================

## PM-1. Corpus and PRISMA flow (as of 2026-07-27)
* Current corpus: 39 papers, IDs P01–P40 (P36 removed as duplicate of P31).
  P01–P19 = foundational corpus (Trabalho I); P20–P40 = cycle-1 candidates.
* PRISMA flow of cycle 1: ~51 records identified (3 AI-assisted searches) →
  21 candidates after dedup/verification → 20 screened (−1 internal duplicate)
  → 18 full-text assessed (−2 ineligible, Qualis A3) → 14 included
  (−4 excluded) → final corpus 33 (19 foundational + 14 new).
* PRISMA inclusion criteria (ALL must hold):
  I1 year ∈ [2020, 2026]
  I2 identifiable peer-reviewed venue (journal/conference; DOI + ISSN)
  I3 Qualis ∈ {A1, A2} (CAPES 2025-2028)
  I4 SJR quartile ∈ {Q1, Q2}
  I5 citations >= 1 (RECENCY_EXCEPTION if published < 12 months)
  I6 thematic adherence: AGENTIC approach × IR/AIOps/SOC DOMAIN
* PRISMA exclusion criteria (any one excludes):
  E1 Qualis A3 or lower           (cycle 1: P39, P40)
  E2 non-agentic approach         (cycle 1: P26, P29, P30)
  E3 out of incident-response/IT-operations domain (cycle 1: P38 agriculture)
  E4 duplicate (internal or of corpus; check preprint DOI variants)
  E5 not peer-reviewed (unflagged preprint)

## PM-2. PICOC of the review (scope instrument; prompt v1.1.0 rule)
* Population:   complex software systems and IT-operations environments
                (cloud-native/microservices, ICT/networks, SOC/cybersecurity,
                SRE/NOC teams).
* Intervention: Agentic AI as copilot or autonomous agent — LLM-based
                multi-agent systems with orchestration/tools (dominant
                pattern), single LLM agents, SLM agents, copilots.
* Comparison:   RULE (v1.1.0): counts as DECLARED only with an EMPIRICAL
                baseline; conceptual/paradigmatic contrast = "N/A (conceptual
                contrast)". Prefer candidates with empirical baselines.
* Outcomes:     MTTD/MTTR, alert fatigue, cognitive load, RCA accuracy,
                remediation time. KEY VERIFIED GAP: none of the 39 corpus
                papers measures MTTD/MTTR nominally (primaries report proxies:
                response latency, diagnosis time). Studies with NAMED
                operational metrics are therefore TOP-PRIORITY finds.
* Context:      incident-response lifecycle, AIOps, observability, HITL/HOTL;
                corpus evidence is mostly offline/benchmark/simulation —
                production deployments are rare and highly valuable.

## PM-3. Validated search string (PICOC-derived; calibrated on the corpus)
Block A (Intervention) AND Block B (Context/Population). Validated recall:
13/14 included studies on both Scopus and OpenAlex; misses only
excluded/ineligible studies. Outcomes terms must NOT be a mandatory block
(making them mandatory retrieves 1/38 of the corpus).
  A: "agentic AI" OR "AI agent*" OR "LLM agent*" OR "language model agent*"
     OR "multi-agent" OR multiagent OR "autonomous agent*" OR copilot*
     OR "large language model*" OR "small language model*"
     OR "intelligent agent*"
  B: "incident response" OR "incident management" OR AIOps OR "IT operations"
     OR "site reliability" OR SRE OR "security operations" OR SOC
     OR cybersecurity OR "cyber security" OR "cyber threat*" OR "root cause"
     OR "anomaly detection" OR observability OR microservice* OR "cloud-native"
     OR "network management" OR "network operations" OR DevOps OR remediation
     OR "threat detection" OR resilience OR vulnerabilit*
Scopus syntax caveat (verified): use TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B)
per block — the nested form TITLE-ABS-KEY((A) AND (B)) silently false-zeroes
when combined with other fields (e.g., DOI()).

## PM-4. Verification APIs and sources (used by the project; cite-able)
* OpenAlex API  (api.openalex.org, keyless): DOI resolution, citation counts
  (cited_by_count), reference lists (referenced_works), search validation.
* Crossref API  (api.crossref.org, keyless): citation counts
  (is-referenced-by-count), reference DOIs; used by the project's DOIS.py.
* Scopus Search API (api.elsevier.com, institutional key): search-string
  execution, citation counts (citedby-count). Caveats verified: REF() matches
  reference TITLES, not DOIs; some venues are not indexed (e.g.,
  F1000Research → P01 invisible in Scopus).
* QUALIS lookup: https://qualis.pages.dev/ (CAPES 2025-2028 strata).
* SCImago JCR:  https://www.scimagojr.com/ (SJR quartiles).
* Full-text access: Portal de Periódicos CAPES (CAFe login / Unisinos).
* Known pitfall (P09 case): citations/references may point to a PREPRINT DOI
  instead of the version of record — always return the CANONICAL
  journal/conference DOI and note known preprint variants.

# ============================================================
# TASK
# ============================================================

INPUTS
* PROJECT_MEMORY above (authoritative).
* Corpus dedup list: the 39 DOIs in papers.csv (P01–P40) — if provided as an
  attachment, use it; otherwise ask for it before returning results.

SEARCH_STRING
Apply PM-3 (Block A AND Block B) consistently across all databases, adapting
syntax per database as noted. Do not add Outcomes terms as mandatory.

SOURCES (allowlist)
* IEEE Xplore, Elsevier ScienceDirect, ACM Digital Library, Scopus.
* Also admissible: MDPI, Springer Nature, Wiley, and other indexed venues —
  ONLY if they pass the PRISMA inclusion criteria (PM-1).

DEDUPLICATION
* Do NOT return any of the 39 corpus papers (P01–P40), including preprint/
  alternate-DOI versions of them (PM-4 pitfall).
* Related newer work by the same authors IS allowed; set `author_overlap` to
  the corpus P-id when authors overlap.
* Same-institution/same-group clusters (e.g., cycle 1 had three State Grid
  papers): set `group_provenance` so independence can be assessed.

TARGET_TOPICS (rank candidates by relevance) — refined by cycle-1 findings:
* T1 Safe/verifiable/reversible (rollback) autonomous execution
* T2 Complex telemetry / traces with LLMs
* T3 Memory integrity & contradictory-knowledge resolution
* T4 Governance, accountability, adversarial risk — SYSTEMATIC GAP in cycle 1
     (RQ4 fully answered by only 4/18); candidates strong here are valuable
* T5 Causal reasoning vs. statistical correlation
* T6 Resource efficiency / SLMs / edge
* T7 Frameworks & architectures (orchestration, multi-agent, HITL/HOTL)
* T8 Quantitative MTTD/MTTR or copilot-efficacy evidence — TOP PRIORITY:
     no corpus paper measures MTTD/MTTR nominally (PM-2); studies with named
     operational metrics and empirical baselines (PICOC v1.1.0) fill the
     review's central gap
* T9 Production deployments / field studies of agentic IR (rare in corpus)

TASK
Return 15–25 candidate articles satisfying the PRISMA inclusion criteria
(PM-1) and DEDUPLICATION, sorted by (relevance DESC, year DESC).

OUTPUT_SCHEMA (one row per candidate; Markdown table OR JSON array; keep
fields and order exact)
id | citation_full | doi | publisher | venue | year | sjr_quartile | qualis |
citations | peer_reviewed | flag | topics | picoc_fit | author_overlap |
group_provenance | relevance_note
Field rules:
* `doi` = canonical version-of-record DOI (never a preprint DOI; if only a
  preprint exists, flag=PREPRINT).
* `flag` ∈ {OK, PREPRINT, CONFERENCE, RECENCY_EXCEPTION, UNVERIFIED}
* `topics` = subset of {T1..T9}
* `picoc_fit` = one line mapping the candidate to P/I/C/O/C; state whether
  Comparison has an EMPIRICAL baseline (v1.1.0 rule) and whether Outcomes
  include NAMED operational metrics (MTTD/MTTR or proxies).
* `relevance_note` <= 2 sentences: specific contribution + which RQ/gap it
  serves.

RULES (verification & anti-fabrication)
* NEVER invent a DOI, author, venue, or metric. If a value cannot be
  confirmed from a real source, write `UNVERIFIED` and set `flag=UNVERIFIED`.
* Qualis/SJR values must be traceable to the QUALIS lookup / SCImago (PM-4);
  citations should be checkable in OpenAlex/Crossref/Scopus — note that the
  project will re-verify all three via API, so report the source you used.
* Prefer original publisher/index pages over aggregators.
* Group the final table by TARGET_TOPIC; keep the schema identical.
* After the table, output a `## CAVEATS` block listing: unverifiable metrics,
  preprint/conference items, inferred (not confirmed) Qualis values, and any
  known preprint-DOI ambiguity.

ACCEPTANCE
* 0 fabricated references.
* 0 duplicates of P01–P40 (including alternate-DOI versions).
* Every returned row satisfies the PRISMA inclusion criteria or carries an
  explicit `flag` explaining the exception.
* At least 1/3 of returned candidates address T8 or T9 (the review's central
  gap), unless genuinely unavailable — state so in CAVEATS if that is the case.
```

---

## Changelog

- **v2.0.0** (2026-07-27) — Revisão pós-ciclo 1, incorporando as lições de P01–P40:
  - **`PROJECT_MEMORY`** embutida no prompt: fluxo e critérios **PRISMA** (I1–I6/E1–E5 com os casos do ciclo 1), **PICOC** com a regra v1.1.0 de Comparison (baseline empírico) e o achado central verificado (nenhum estudo mede MTTD/MTTR nominalmente), **string de busca validada** (recall 13/14 em Scopus e OpenAlex; Outcomes nunca como bloco obrigatório) e **APIs/fontes de verificação** (OpenAlex, Crossref, Scopus + quirks documentados; QUALIS, SCImago, Portal CAPES/CAFe).
  - String de busca substituída pela versão derivada do PICOC e calibrada no corpus (a v1 perdia "AI agent*", "LLM agent*", copilot* etc.).
  - Deduplicação ampliada de P1–P19 para **P01–P40**, incluindo **variantes de DOI de preprint** (caso P09).
  - Schema: novos campos **`picoc_fit`** (ancoragem por elemento + baseline empírico + métricas nomeadas) e **`group_provenance`** (independência de grupos, lição State Grid); `doi` obrigatoriamente da **versão de registro**.
  - Tópicos: **T8 promovido a prioridade máxima** (lacuna central da RSL) e novo **T9** (implantações em produção, raras no corpus); T4 anotado com a lacuna sistemática de RQ4 (4/18).
  - Aceitação reforçada: cota mínima de candidatos T8/T9.
- **v1.0.0** — Versão original executada no ciclo 1 (Gemini/Claude/ChatGPT), com string inicial estreita, dedup P1–P19 e critérios de inclusão sem memória de projeto.
