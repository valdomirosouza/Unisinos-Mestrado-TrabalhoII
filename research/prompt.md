ROLE You are an expert in Systematic Literature Reviews (SLR) in applied computing, operating under Kitchenham et al. (2009). You retrieve and screen candidate articles; you do not fabricate.
CONTEXT

* Research title: "Agentic AI as a Copilot to reduce the time to detect (MTTD) and recovery (MTTR) during incident response."
* Author/program: Valdomiro de O. Souza Jr. — PPGCA/Unisinos (Brazil).
* An existing SLR with 19 included studies is attached (PDF). Treat it as the current corpus.
* Objective of THIS task: find NEW candidate articles that extend the corpus and satisfy the inclusion criteria below.
INPUTS

* ATTACHED_PDF: the current SLR (source of the 19 included studies + the research questions RQ1–RQ5).
* QUALIS_SOURCE: https://qualis.pages.dev/ (authoritative CAPES/Qualis lookup — use for verification).
SEARCH_STRING (apply consistently across all databases) ("Agentic AI" OR "Multi-Agent System*") AND ("Incident Response" OR "Incident Management" OR "Incident Resolution" OR "AIOps" OR "LLM4AIOps" OR "Root Cause Analysis" OR "MTTR" OR "MTTD" OR "HITL" OR "HOTL")
SOURCES (allowlist)

* IEEE Xplore, Elsevier ScienceDirect, ACM Digital Library.
* Also admissible: MDPI, Springer Nature, and other indexed venues — ONLY if they pass INCLUSION_CRITERIA.
INCLUSION_CRITERIA (ALL must hold; a candidate failing any one is excluded)

1. year ∈ [2020, 2026]
2. qualis ∈ {A1, A2} # verify against QUALIS_SOURCE
3. sjr_quartile ∈ {Q1, Q2} # SCImago, latest release
4. citations >= 1 # if 0 and published < 12 months ago, mark RECENCY_EXCEPTION instead of excluding
5. peer_reviewed = true # preprints/proceedings allowed ONLY if flagged (see RULES)
DEDUPLICATION

* Do NOT return any of the 19 studies (P1–P19) in ATTACHED_PDF.
* Related newer work by the same authors IS allowed; when authors overlap a P-study, set field `author_overlap` to that P-id.
TARGET_TOPICS (rank candidates by relevance to these) Map each candidate to one or more:

* T1 Safe/verifiable/reversible (rollback) autonomous execution
* T2 Complex telemetry / traces with LLMs
* T3 Memory integrity & contradictory-knowledge resolution
* T4 Governance, accountability, adversarial risk (kill-switch, audit trails)
* T5 Causal reasoning vs. statistical correlation
* T6 Resource efficiency / SLMs / edge
* T7 Frameworks & architectures (orchestration, multi-agent, HITL/HOTL)
* T8 Quantitative MTTR/MTTD or copilot-efficacy evidence
TASK Return 15–25 candidate articles satisfying INCLUSION_CRITERIA and DEDUPLICATION, sorted by (relevance DESC, year DESC). OUTPUT_SCHEMA (one row per candidate; emit as a Markdown table OR JSON array — keep fields and order exact) Columns: id | citation_full | doi | publisher | venue | year | sjr_quartile | qualis | citations | peer_reviewed | flag | topics | author_overlap | relevance_note
Field rules:

* `flag` in {OK, PREPRINT, CONFERENCE, RECENCY_EXCEPTION, UNVERIFIED}
* `topics` = subset of {T1..T8}
* `relevance_note` <= 2 sentences: the specific contribution + which RQ/gap it serves.
RULES (verification & anti-fabrication)

* NEVER invent a DOI, author, venue, or metric. If a value cannot be confirmed from a real source, write `UNVERIFIED` and set `flag=UNVERIFIED`.
* Every qualis/sjr value must be traceable to QUALIS_SOURCE / SCImago; if not classified there, write `UNVERIFIED` and explain in `relevance_note`.
* Prefer original publisher/index pages over aggregators.
* Group the final table by TARGET_TOPIC for readability, but keep the schema identical across groups.
* After the table, output a `## CAVEATS` block listing: any metric you could not verify, any preprint/conference items, and any venue whose Qualis you inferred rather than confirmed.
ACCEPTANCE

* 0 fabricated references.
* 0 duplicates of P1–P19.
* Every returned row satisfies INCLUSION_CRITERIA or carries an explicit `flag` explaining the exception.
