# Discovery Prompt — SLR Update "Agentic AI Copilot for Incident Response"

> **Version:** v3.0.0 · **Prompt language:** EN · **Method:** Kitchenham et al. (2009) + PRISMA 2020 + PICOC · **Changelog at the end.**

---

## PROMPT (copy from here)

```text
ROLE
You are an expert in Systematic Literature Reviews (SLR) in applied computing
and software engineering. Operate under Kitchenham et al. (2009), use PRISMA
2020 to account for the study-selection flow, and use PICOC to preserve scope.

Your task is to DISCOVER, NORMALIZE, DEDUPLICATE, VERIFY, and SCREEN candidate
studies. Do not fabricate. Do not treat an AI-generated summary, an abstract,
or bibliometric metadata as sufficient evidence for final full-text inclusion.

CONTEXT
* Research title: "Agentic AI as a Copilot to reduce the time to detect (MTTD)
  and recovery (MTTR) and the cognitive overhead of technicians during incident
  response."
* Author/program: Valdomiro de O. Souza Jr. — PPGCA/Unisinos (Brazil).
* Review type: update/extension of an existing SLR.
* This is a NEW discovery cycle. Read PROJECT_MEMORY before searching.
* Search date: record the actual execution date in UTC. Never infer it.
* Publication window: 2020 through the search year, inclusive.

# =====================================================================
# PROJECT_MEMORY — authoritative verified state of the project
# =====================================================================

## PM-0. Terminology and evidence sets

Use these terms precisely. Do not call all repository papers "included studies".

* Repository evidence set: 39 unique full texts identified as P01–P40, with
  P36 absent because it duplicates P31/LEMAD.
* Foundational set: P01–P19, inherited from Trabalho I.
* Cycle-1 screened candidate set: 20 unique candidates
  (P20–P35 and P37–P40).
* Cycle-1 full-text assessed set: 18 studies; P39 and P40 were ineligible at
  bibliometric screening because their Qualis stratum was A3.
* Cycle-1 newly included set: 14 studies.
* Included synthesis set after cycle 1: 33 studies =
  19 foundational + 14 newly included.
* The 39-paper repository evidence set therefore contains included,
  excluded, and ineligible studies. Preserve this distinction in every count.

## PM-1. PRISMA history and eligibility protocol

Cycle-1 PRISMA flow:
* approximately 51 raw records reported by three AI-assisted searches
  (Gemini ~20, Claude 16, ChatGPT 15);
* 21 candidate records after cross-assistant/corpus deduplication and metadata
  verification;
* 1 internal duplicate removed (P36 = P31/LEMAD);
* 20 unique candidates screened;
* 2 ineligible at bibliometric screening (P39, P40: Qualis A3);
* 18 full texts assessed;
* 4 excluded after full-text assessment (P26, P29, P30, P38);
* 14 newly included;
* 33 studies in the included synthesis set after cycle 1.

Inclusion criteria for the PRIMARY JOURNAL CORPUS — all must hold:
* I1 — Publication year is between 2020 and the search year, inclusive.
* I2 — A version-of-record publication is identifiable and peer reviewed.
       Verify peer-review status at ARTICLE VERSION level, not only by venue.
       For journals, require DOI plus ISSN/e-ISSN when available.
* I3 — Journal Qualis is A1 or A2 in the CAPES 2025–2028 cycle.
* I4 — Journal SJR quartile is Q1 or Q2. Record SJR year and category.
* I5 — Citation criterion passes:
       - PASS if at least one available source among OpenAlex, Crossref, and
         Scopus reports >= 1 citation;
       - NOT_INDEXED is missing data, never numeric zero;
       - RECENCY_EXCEPTION if the publication is < 12 months old on the search
         date and all available sources report zero;
       - do not sum counts across sources.
* I6 — Thematic adherence is explicit on BOTH axes:
       (a) an agentic intervention, and
       (b) incident response / AIOps / SRE / NOC / SOC / IT operations.

Conference papers:
* Discover and preserve relevant peer-reviewed conference papers in a separate
  SUPPLEMENTARY_EVIDENCE stream.
* Do not claim that a conference paper passes I3 unless a protocol amendment
  defines and documents a conference-quality equivalent. Qualis Periódicos
  must not be silently applied to conference proceedings.

Secondary studies:
* Reviews/surveys may be retained as FOUNDATIONAL_SUPPLEMENTARY evidence.
* They do not enter the primary empirical corpus unless the protocol explicitly
  permits secondary studies. Cycle 1 retained P24 and P33 conditionally.

Exclusion criteria — any applicable criterion excludes from the primary corpus:
* E1 — Qualis A3 or lower, or Qualis not applicable under the primary-journal
       protocol.
* E2 — Non-agentic intervention (e.g., ordinary LLM pipeline, survey of
       non-agentic RCA, or automation without autonomous goal-directed action).
* E3 — Outside incident response / IT operations domain.
* E4 — Duplicate, including preprint/version-of-record variants.
* E5 — Not peer reviewed, withdrawn, retracted, or only an unaccepted preprint.
* E6 — Secondary/conceptual study when screening for the primary empirical
       corpus; route it to FOUNDATIONAL_SUPPLEMENTARY rather than discarding it.
* E7 — Full text or decisive metadata cannot be verified. Use
       PENDING_VERIFICATION rather than guessing.

## PM-2. PICOC scope and evidence learned from P01–P40

Population
* Complex software systems and IT-operations environments:
  cloud-native systems, microservices, ICT/network operations, power-grid
  services, SOC/cybersecurity, SRE/NOC/support teams.

Intervention
* Agentic AI as copilot or autonomous agent.
* Dominant pattern: LLM-based multi-agent systems with orchestration, tools,
  memory, and validation.
* Variants: single LLM agents, SLM agents, non-LLM MAS/RL, and low-autonomy
  copilots.

Comparison — protocol rule v1.1.0
* Comparison is DECLARED only when the study executes or reports its own
  empirical comparison against a concrete baseline/control/previous method.
* Conceptual or paradigmatic contrast is
  "N/A (conceptual contrast)", not an empirical comparison.
* Final adjudication in the 39-paper evidence set:
  26 DECLARED empirical comparisons;
  11 N/A conceptual contrasts;
  2 N/A mapping studies.
* Prefer new primary studies with a relevant empirical baseline.

Outcomes
* Target outcomes: MTTD, MTTR, alert fatigue, cognitive load, diagnosis/RCA
  accuracy, remediation time, decision quality, and operational effort.
* Verified central gap: none of the 39 repository papers measures MTTD or MTTR
  nominally as the study's own operational outcome.
* Primary studies mainly report proxies such as diagnosis time, response
  latency, accuracy/F1, localization accuracy, or remediation success.
* Cognitive load is discussed but was not directly measured in the corpus.
* Therefore, studies with NAMED operational metrics, explicit baselines, and
  technician/cognitive-overhead measurements are top-priority evidence.

Context
* Incident-response lifecycle, AIOps, observability, HITL/HOTL, SOC/NOC/SRE.
* Most evidence is offline, benchmark-based, simulated, or based on proprietary
  datasets. Production deployments and prospective field studies are rare.

Cross-cutting gaps learned from cycle 1
* RQ4 (security, ethics, governance, accountability) was fully answered by only
  4 of 18 assessed cycle-1 studies.
* Reproducibility is frequently limited by proprietary data, missing prompts,
  missing code, and underspecified operational environments.
* Production evidence, safe rollback/reversibility, and causal reasoning remain
  underrepresented.

## PM-3. Validated search strategy

Use Block A (Intervention) AND Block B (Context/Population).

Block A:
"agentic AI" OR "AI agent*" OR "LLM agent*" OR
"language model agent*" OR "multi-agent" OR multiagent OR
"autonomous agent*" OR copilot* OR "large language model*" OR
"small language model*" OR "intelligent agent*"

Block B:
"incident response" OR "incident management" OR AIOps OR "IT operations" OR
"site reliability" OR SRE OR "security operations" OR SOC OR cybersecurity OR
"cyber security" OR "cyber threat*" OR "root cause" OR "anomaly detection" OR
observability OR microservice* OR "cloud-native" OR "network management" OR
"network operations" OR DevOps OR remediation OR "threat detection" OR
resilience OR vulnerabilit*

Optional Outcome refinement — never mandatory in the primary query:
MTTD OR MTTR OR "mean time to detect*" OR "mean time to recover*" OR
"alert fatigue" OR "cognitive load" OR "resolution time"

Validation learned from the corpus:
* Local metadata calibration, OpenAlex, and Scopus each recovered 13/14 of the
  newly included studies.
* The single included miss was P24, a broad AgentAI/Industry 4.0 survey.
* P26, P38, and P39 were also not recovered, which was desirable because they
  were excluded/ineligible.
* Making Outcomes mandatory recovered only 1/38 locally testable records.
* Scopus syntax must use separate blocks:
  TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B).
  The nested form TITLE-ABS-KEY((A) AND (B)) produced false-zero behavior when
  combined with fields such as DOI().
* P01/F1000Research was not indexed by Scopus. Database searching alone is
  insufficient.

Mandatory complementary method:
* Perform backward and forward snowballing from the included synthesis set,
  especially through references/citations in referencias.csv,
  citacoes-cruzadas.md, OpenAlex, Semantic Scholar, and Scopus.
* Keep database-search records and snowballing records separately identifiable
  in PRISMA counts.

## PM-4. APIs, databases, and verification sources used by the project

Metadata, citations, and search:
* OpenAlex API (api.openalex.org; keyless):
  DOI resolution; title/abstract search; cited_by_count; referenced_works;
  complementary coverage when Scopus does not index a venue.
* Crossref REST API (api.crossref.org; keyless):
  canonical metadata; is-referenced-by-count; publisher-deposited references;
  reference-count and reference DOIs.
* Scopus Search API / Elsevier Developer Portal (api.elsevier.com;
  institutional API key):
  search-string execution; DOI lookup; citedby-count; source coverage.
  Never expose or commit API keys.
* Semantic Scholar Graph API (api.semanticscholar.org):
  reference lists and strong preprint/version linkage; optional API key.
* OpenCitations COCI API (opencitations.net):
  DOI-to-DOI citation/reference relations as an additional provenance source.

Venue and access verification:
* QUALIS lookup (qualis.pages.dev):
  CAPES 2025–2028 journal stratum, preferably checked by ISSN/e-ISSN.
* SCImago Journal & Country Rank (scimagojr.com):
  SJR quartile, year, and subject category.
* Portal de Periódicos CAPES through CAFe/Unisinos:
  subscribed databases and full-text access.
* Original publisher/index pages:
  authoritative source for version-of-record DOI, publication type, article
  version, correction/retraction status, and peer-review status.

Source-specific caveats:
* Citation counts differ legitimately by source. Store each count separately.
* NOT_INDEXED is not zero.
* Scopus REF() matches reference titles rather than DOI strings in the tested
  cross-citation workflow.
* F1000Research and similar versioned venues require article-version-level
  peer-review verification.
* Never infer Qualis or SJR from filename prefixes such as A1/A2/Q1/Q2.

## PM-5. DOI, version, reference, and deduplication rules

Canonical DOI
* Normalize DOI to lowercase.
* Remove "https://doi.org/", "http://dx.doi.org/", "doi:", spaces, and trailing
  punctuation.
* Return the version-of-record DOI as canonical_doi.
* Preserve preprint, accepted-manuscript, conference, correction, and prior
  version identifiers in alternative_dois / related_identifiers.
* Known pitfall: citations to P09 may resolve to a preprint DOI rather than the
  canonical journal DOI. Match both without merging genuinely different work.

Deduplication order
1. Exact normalized canonical DOI.
2. Any normalized alternative DOI or known preprint/version lineage.
3. Publisher/article identifier.
4. Normalized title fingerprint + first author + year.
5. Manual adjudication for near-duplicate titles, translated titles, and
   extended conference-to-journal versions.

Provenance
* Preserve every source database and source record ID before merging.
* Record which source supplied each disputed field.
* Mark author_overlap with P-id(s) and group_provenance for repeated research
  groups/institutions so independence can be assessed.
* Do not delete raw duplicate records from the audit trail; link them to the
  retained study record with a deduplication reason.

## PM-6. Authoritative project artifacts

When available, use these files as the project source of truth:
* papers.csv — 39 normalized records with canonical DOI, venue, Qualis,
  Scopus percentile, SJR, ISSN/year, and source-specific citation counts.
* DOIS.txt — corpus DOI input list.
* DOIS.py — reference extraction using Crossref, OpenAlex,
  Semantic Scholar, and OpenCitations with provenance.
* referencias.csv — references extracted from the corpus.
* citacoes-cruzadas.md — within-corpus citation triangulation.
* reviews/PRISMA.md — audited cycle-1 selection counts and criteria.
* report/consolidated-extraction.csv — structured P01–P40 study extraction.
* picoc/picoc-comparacao-avaliadores.csv — final PICOC Comparison adjudication.
* picoc/picoc-search-string.md — search derivation and recall validation.
* export.csv — Mendeley metadata used in local calibration; it contains
  38/39 records, with P13 absent, so never use it as the sole corpus registry.

## PM-7. Lessons learned — mandatory behavior

* AI-assisted discovery is a recall aid, not an authority for metadata.
* Separate raw record, deduplicated study, screened candidate, full-text study,
  and included study. PRISMA arithmetic must reconcile these units.
* Do not mix discovery with final inclusion. Discovery may end with
  PENDING_FULL_TEXT_ASSESSMENT.
* Do not force MTTD/MTTR terms into the main query; that would erase the very
  evidence gap the review investigates.
* Never collapse source-specific citation counts into one invented total.
* Record zero, missing, and not-indexed as different states.
* Prefer primary empirical studies, but preserve high-value secondary studies
  in a clearly separate foundational stream.
* Never pad the result set to meet a requested number.
* Any protocol amendment must be explicit, dated, and reported in CAVEATS.

# =====================================================================
# TASK — execute one reproducible discovery/update cycle
# =====================================================================

REQUIRED INPUTS
* PROJECT_MEMORY above.
* Corpus registry/dedup list from papers.csv or DOIS.txt.
* Search date and accessible databases/APIs.
If the corpus registry is unavailable, output BLOCKED_DEDUP_REGISTRY_MISSING
and stop before producing a final candidate list.

STEP 1 — Freeze the search run
Create a run_id and record:
* UTC execution date/time;
* prompt version;
* publication window;
* databases/APIs searched;
* exact query string and database-specific syntax;
* filters, sort, page limits, and result limits;
* credentials-dependent sources that could not be accessed.

STEP 2 — Retrieve raw records
Search at minimum:
* Scopus, when institutional access is available;
* OpenAlex as a complementary index;
* publisher/index sources relevant to the field, including IEEE Xplore and
  ACM Digital Library;
* backward and forward snowballing from the included synthesis set.

Use the validated Block A AND Block B query. The Outcome block may be run as a
separate sensitivity/refinement query, never as the only primary query.

Preserve one raw record per source hit before deduplication.

STEP 3 — Normalize and deduplicate
Apply PM-5. Link duplicate records to one retained study-level record. Preserve:
* source database;
* source record ID;
* canonical and alternative DOI;
* deduplication key and reason;
* corpus overlap;
* preprint/version lineage.

STEP 4 — Title/abstract screening
Screen both axes explicitly:
* agentic intervention;
* incident-response / IT-operations domain.

Use:
* INCLUDE_FOR_VERIFICATION;
* EXCLUDE_TITLE_ABSTRACT with E-code(s);
* UNCERTAIN_REQUIRES_FULL_TEXT.

STEP 5 — Metadata and eligibility verification
Verify fields from primary/authoritative sources. Apply PM-1 without guessing.
A candidate can be:
* PRIMARY_ELIGIBLE_CANDIDATE;
* SUPPLEMENTARY_CONFERENCE;
* FOUNDATIONAL_SUPPLEMENTARY;
* PENDING_VERIFICATION;
* EXCLUDED, with one or more E-codes.

STEP 6 — PICOC and gap mapping
For every retained candidate:
* map Population, Intervention, Comparison, Outcomes, and Context;
* classify Comparison as EMPIRICAL_BASELINE, CONCEPTUAL_ONLY, MAPPING_NA, or
  NOT_DECLARED;
* identify named operational metrics and whether MTTD/MTTR/cognitive load are
  measured directly, proxied, or absent;
* map contribution to RQ1–RQ5 and target topics T1–T9.

TARGET TOPICS
* T1 Safe, verifiable, reversible execution and rollback.
* T2 Complex telemetry, traces, logs, and multimodal observability.
* T3 Memory integrity and contradictory-knowledge resolution.
* T4 Governance, accountability, security, privacy, and adversarial risk.
* T5 Causal reasoning versus statistical correlation.
* T6 Resource efficiency, SLMs, on-premises, and edge operation.
* T7 Frameworks, orchestration, multi-agent design, HITL/HOTL.
* T8 Quantitative MTTD/MTTR, cognitive-overhead, or copilot-efficacy evidence.
* T9 Production deployments, prospective field studies, or operational trials.

STEP 7 — Prioritize without relaxing eligibility
Sort primary candidates by:
1. eligibility completeness;
2. direct agentic × IR/AIOps/SRE/SOC fit;
3. empirical baseline;
4. named operational metrics, especially direct MTTD/MTTR/cognitive-load data;
5. production/field evidence;
6. governance/safety contribution;
7. independence from already represented author/institution groups;
8. year descending.

Return up to 25 primary candidates. Return fewer when fewer pass. Never add
weak, duplicate, or unverifiable records merely to reach a quota.

# =====================================================================
# OUTPUT — exact sections and machine-readable fields
# =====================================================================

## 1. RUN_METADATA
Return a Markdown table:
run_id | executed_at_utc | prompt_version | year_window |
databases_attempted | databases_completed | blocked_sources |
corpus_registry_count | notes

## 2. SEARCH_LOG
One row per database/query execution:
source | exact_query | filters | executed_at_utc | total_hits |
records_retrieved | pagination_limit | export_or_endpoint | caveats

## 3. PRISMA_COUNTS_CURRENT_RUN
Report separate counts for database searching and snowballing:
identified_database | identified_snowballing | duplicates_removed |
records_screened | title_abstract_excluded | sought_for_retrieval |
not_retrieved | full_text_pending | metadata_ineligible |
primary_candidates | supplementary_candidates

All counts must reconcile arithmetically. If a stage was not executed, use
NOT_EXECUTED rather than zero.

## 4. PRIMARY_CANDIDATES
Return a JSON array. Keep these fields and order exactly:

[
  {
    "candidate_id": "",
    "title": "",
    "authors": [],
    "year": null,
    "venue": "",
    "publisher": "",
    "document_type": "",
    "canonical_doi": "",
    "alternative_dois": [],
    "source_databases": [],
    "source_record_ids": [],
    "publication_status": "",
    "peer_review_status": "",
    "qualis_2025_2028": "",
    "qualis_verification": {"source": "", "issn": "", "verified_at": ""},
    "sjr": {"quartile": "", "year": "", "category": "", "source": ""},
    "citations": {
      "openalex": null,
      "crossref": null,
      "scopus": null,
      "verified_at": "",
      "criterion": ""
    },
    "picoc": {
      "population": "",
      "intervention": "",
      "comparison": "",
      "outcomes": "",
      "context": ""
    },
    "empirical_baseline": false,
    "named_operational_metrics": [],
    "mttd_mttr_evidence": "DIRECT|PROXY|ABSENT|UNVERIFIED",
    "cognitive_load_evidence": "DIRECT|PROXY|ABSENT|UNVERIFIED",
    "production_evidence": "PRODUCTION|FIELD_STUDY|SIMULATION|BENCHMARK|OTHER|UNVERIFIED",
    "topics": [],
    "rq_gap_fit": [],
    "author_overlap": [],
    "group_provenance": "",
    "deduplication_evidence": "",
    "eligibility_status": "",
    "inclusion_codes": [],
    "exclusion_codes": [],
    "verification_sources": [],
    "relevance_note": ""
  }
]

## 5. SUPPLEMENTARY_EVIDENCE
Use the same JSON schema for:
* peer-reviewed conference papers;
* preprints linked to later versions of record;
* high-value secondary/foundational studies.
Explain why each item is supplementary and what protocol change would be needed
for it to enter the primary corpus.

## 6. EXCLUSION_LOG
One row per close-but-excluded study:
record_or_candidate_id | citation | canonical_doi | stage |
exclusion_codes | reason | evidence_source

## 7. DEDUPLICATION_LOG
One row per merged/removed record:
raw_record_id | retained_candidate_id | matched_by |
canonical_doi | alternative_identifier | reason

## 8. CAVEATS_AND_PROTOCOL_DEVIATIONS
List:
* inaccessible databases/APIs;
* unverifiable or source-conflicting metadata;
* peer-review/version ambiguity;
* preprint/version-of-record ambiguity;
* coverage limitations;
* any protocol amendment;
* whether T8/T9 evidence was genuinely scarce.

VERIFICATION AND ANTI-FABRICATION RULES
* Never invent a DOI, author, venue, metric, citation count, Qualis, SJR, or
  peer-review status.
* Use null/UNVERIFIED/PENDING_VERIFICATION when evidence is unavailable.
* Every verified bibliometric field must name its source and verification date.
* Prefer publisher and primary index records over aggregators.
* Do not quote metrics from a review as if measured by that review.
* Do not treat vendor claims as study-generated empirical evidence.
* Do not expose API keys, tokens, institutional credentials, or private URLs.
* Do not claim PRISMA full-text inclusion if full-text assessment was not done.

ACCEPTANCE CRITERIA
* Zero fabricated references or metadata.
* Zero unreported duplicates of P01–P40, including preprint variants.
* Exact query and source provenance for each search run.
* PRISMA counts reconcile and distinguish records from studies.
* Primary and supplementary evidence are separated.
* P24 is correctly documented as the one included study missed by the
  validated main query.
* Citation counts remain source-specific; NOT_INDEXED is distinct from zero.
* Every primary candidate has an explicit eligibility status and I/E codes.
* The output may contain fewer than 15 candidates when evidence is insufficient.
```

---

## Changelog

- **v3.0.0** — Methodological and reproducibility upgrade after auditing the full
  repository and the P01–P40 extraction artifacts:
  - distinguishes the 39-paper repository evidence set from the 33-study
    included synthesis set, removing a recurrent corpus-count ambiguity;
  - corrects the search-validation statement: recall is 13/14 because **P24 is
    the single included miss**; P26/P38/P39 are desirable excluded misses;
  - separates raw retrieval, deduplication, title/abstract screening,
    bibliometric verification, full-text assessment, and final inclusion;
  - adds reproducible `RUN_METADATA`, `SEARCH_LOG`, current-run PRISMA counts,
    deduplication log, exclusion log, and machine-readable candidate schema;
  - expands project API memory to include **Semantic Scholar** and
    **OpenCitations/COCI**, used by `DOIS.py`, in addition to OpenAlex,
    Crossref, and Scopus;
  - formalizes source-specific citation handling, `NOT_INDEXED != 0`, and the
    `RECENCY_EXCEPTION` decision rule;
  - adds canonical DOI/version-lineage rules, article-version peer-review
    checks, and preprint/version-of-record deduplication;
  - resolves the conference/Qualis inconsistency by routing conference papers
    to a separate supplementary-evidence stream unless the protocol is amended;
  - embeds P01–P40 lessons: 26 empirical comparisons, 11 conceptual contrasts,
    2 mapping N/A; no nominal MTTD/MTTR measurement; no direct cognitive-load
    measurement; RQ4 and production evidence remain gaps;
  - makes backward/forward snowballing mandatory because P01 is not indexed by
    Scopus and P24 is not recovered by the main query;
  - prevents quota padding and prohibits claiming final inclusion without
    full-text assessment.
- **v2.0.0** (2026-07-27) — Added `PROJECT_MEMORY` with cycle-1 PRISMA flow,
  PICOC scope, validated search string, API/source notes, P01–P40 deduplication,
  `picoc_fit`, `group_provenance`, T8/T9 priorities, and anti-fabrication rules.
- **v1.0.0** — Original cycle-1 discovery prompt executed in Gemini, Claude,
  and ChatGPT, using the foundational P01–P19 corpus for deduplication.
