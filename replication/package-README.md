# Replication Package — Agentic AI Copilots for Incident Response: A Systematic Literature Review

This package contains the full audit trail of the systematic literature
review (SLR) reported in _"Agentic AI Copilots for Incident Response: A
Systematic Literature Review"_ (Souza Jr. & Kunst, PPGCA/Unisinos): the
review protocol and its dated amendments, the canonical prompts, every
LLM-drafted assessment with the authors' decisions, the structured
extraction sheets, the agreement analyses, the PRISMA flow, and the
bibliometric data. It is deposited in compliance with the research-data
management directive of CNPq Ordinance No. 2,664/2026 (Art. 9-I-g).

## What is NOT included — and why

- **Full texts of the reviewed studies (PDFs).** They are copyrighted
  by their publishers. Every study is identified by DOI, title, venue,
  and per-source citation counts in `papers*.csv`, `Papers_Index.*`,
  and `referencias.csv`, which is sufficient to retrieve each document
  through a subscribing library.
- **API credentials** (e.g., Scopus). Scripts read keys from local
  files that are excluded; see each script's header.

## Structure

| Path                                                                                      | Content                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `protocolo/`                                                                              | Review constitution, eligibility criteria, PICOC definition, and dated protocol-decision records (PDR-0001…0009)                                                                                       |
| `templates/`                                                                              | Canonical templates: assessment prompt, PICOC-extraction prompt, review form, screening form, CSV schemas                                                                                              |
| `prompts/`                                                                                | Rendered per-study assessment prompts (P01–P88) and cycle-3 PICOC prompts — the exact inputs given to the LLM assistants                                                                               |
| `picoc/`                                                                                  | PICOC search string, full-text PICOC extractions per assistant, and inter-assistant comparison                                                                                                         |
| `reviews/`                                                                                | Per-study assessments (`review-Pxx.md`) with the authors' decisions, screening records per cycle, PRISMA flow, dashboard, agreement CSVs, charts, and assistant-version log (`versoes-avaliadores.md`) |
| `report/`                                                                                 | Structured extraction sheets per study (EN and pt-BR) and consolidated CSVs                                                                                                                            |
| `research/`                                                                               | Assisted-identification audit trail: research prompts (v1–v3.1), per-assistant discovery reports, cycle-3 discovery log                                                                                |
| `scripts/`, `DOIS.py`                                                                     | Tooling: `compute-kappa.py` (Cohen's and Fleiss' kappa), `check-rsl.sh` (consistency checks), chart/PDF generators (`reviews/scripts/`), reference extraction                                          |
| `papers*.csv`, `Papers_Index.*`, `referencias.csv`, `citacoes-cruzadas*.md`, `export.ris` | Bibliometrics per source (OpenAlex/Crossref/Scopus, never summed), corpus index, cross-citation network, reference-manager export                                                                      |
| `WORKFLOW.md`, `CHANGELOG.md`                                                             | The nine-step review cycle and its change log                                                                                                                                                          |

## Reproducing the key results

- **Agreement (Table "Agreement among the three LLM assistants"):** run
  `scripts/compute-kappa.py` over the comparison CSVs in `reviews/`
  (`comparacao-avaliadores*.csv`).
- **PRISMA counts:** `reviews/PRISMA.md` and `reviews/triagem-*.md`
  document every identification, screening, retrieval, and inclusion
  number per cycle, with per-study justifications.
- **Assistant versions per assessment set:** `reviews/versoes-avaliadores.md`
  (matches the article's Table of LLM assistant versions).
- **Search-string validation:** `picoc/picoc-search-string.md` (13/14
  recall on OpenAlex and Scopus; syntax caveats documented).
- **Consistency checks:** `scripts/check-rsl.sh` validates the
  cross-artifact invariants (counts, identifiers, CSV schemas).

## Language note

Working documents are written in Brazilian Portuguese (pt-BR) with all
technical terms, metrics, and acronyms in English (MTTD, MTTR, PICOC,
PRISMA, etc.); extraction sheets and the article are in English. File
and column names are language-stable across versions.

## Provenance and integrity

The package is exported from the review's private Git repository; every
artifact's full history (including failures and reworks) is preserved
there and summarized in the per-session work log. The SHA-256 of the
archive is published alongside the deposit. Generative-AI use in the
review is declared in the article's _Declaration of Generative AI Use_
(CNPq Ordinances No. 2,664/2026 and No. 3,004/2026).

## Citation and license

Cite the article (see `CITATION.cff`) and this deposit's DOI. Code is
released under the repository `LICENSE`; data and documents under
CC BY 4.0 unless noted otherwise in the deposit record.

## Contact

Valdomiro de Oliveira Souza Jr. — PPGCA, Universidade do Vale do Rio
dos Sinos (Unisinos), São Leopoldo, Brazil.
