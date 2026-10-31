# Sugestões de mudança — artigo da RSL (`artigo/main.tex`)

Fonte para aplicação manual no repositório do artigo, derivada do parecer
PPGCA de 31/10/2026 (`PARECER-revisao-artigo.md`).

**Base:** commit `11f962c` do repositório `Unisinos-Mestrado-TrabalhoII`.
Os **números de linha da Parte A** referem-se a esse commit. Aplique os trechos
**de baixo para cima** ou localize-os **pelo texto** do "Trecho atual", já que as
linhas se deslocam a cada edição.

| Parte | Conteúdo | Situação |
|---|---|---|
| **A** | 35 edições no `main.tex`: LLMs como assistentes supervisionados; decisões humanas (mestrando e orientador) | Aplicadas e testadas no clone (pdflatex sem erros, 13 pp.) |
| **B** | 5 blockquotes do `artigo/proveniencia-paragrafos.md` sincronizados com a Parte A | Aplicadas no clone |
| **C** | Demais sugestões do parecer: C1–C9 com texto pronto, C10–C14 como checklist | Não aplicadas |

> **Atenção:** se adotar o **resumo curto (C1)**, pule **A.1** e **B.1**,
> porque C1 substitui o resumo inteiro.

Depois de aplicar: `pdflatex main && bibtex main && pdflatex main && pdflatex main`
e confira se o log não tem linhas `^!`. Registre o trabalho no `MEMORY.md`
conforme o `CLAUDE.md`.

---

## Parte A — `artigo/main.tex`: LLMs como assistentes supervisionados e decisões humanas

#### A.1. Abstract — linhas 70–72

**Trecho atual:**

```latex
and screened, 74 were assessed in full text by \emph{three independent
evaluators} (agreement 91.9--93.2\% per pair; Fleiss' $\kappa=0.60$;
66/74 unanimous decisions, with a divergence-free third cycle), and
```

**Substituir por:**

```latex
and screened, and 74 were assessed in full text. The review is
LLM-assisted but human-decided: each full-text assessment was drafted
independently by three supervised LLM research assistants (Claude,
ChatGPT, Gemini) under one written protocol (agreement 91.9--93.2\% per
pair; Fleiss' $\kappa=0.60$; 66/74 unanimous, with a divergence-free
third cycle), while every screening, eligibility, inclusion, and
adjudication decision was made and reviewed by the authors.
```

#### A.2. Introduction — linhas 164–168

**Trecho atual:**

```latex
corpus of 19 studies, processing 126 candidate studies in total, and ---
unusually for SLRs in this area --- every full-text assessment was
performed independently by \emph{three evaluators}, with inter-rater
reliability quantified by Cohen's~\cite{cohen1960} and
Fleiss'~\cite{fleiss1971} kappa.
```

**Substituir por:**

```latex
corpus of 19 studies, processing 126 candidate studies in total. The
review is \emph{LLM-assisted and human-decided}. Every full-text
assessment was first drafted by three LLM-based research assistants
from different model families (Claude, ChatGPT, Gemini), run
independently under the same written protocol, and their mutual
agreement was quantified with Cohen's~\cite{cohen1960} and
Fleiss'~\cite{fleiss1971} kappa as a consistency check. The assistants
recommend; they do not decide: all screening, eligibility, and
inclusion decisions, the adjudication of every divergence, and the
review of every assessment were performed by the authors --- the
master's student conducting the review, under the supervision and
review of the advisor.
```

#### A.3. Introduction — linhas 188–189

**Trecho atual:**

```latex
  \item a methodological contribution: a fully reproducible three-rater
        protocol whose residual disagreements (8 of 74 decisions, all
```

**Substituir por:**

```latex
  \item a methodological contribution: an LLM-assisted, human-decided
        assessment protocol --- three supervised LLM assistants whose
        recommendations are adjudicated by the authors --- in which the
        assistants' residual disagreements (8 of 74 assessments, all
```

#### A.4. Review Method — novo parágrafo após "...version-controlled in the research repository." (linha 242), separado por linha em branco

**Inserir:**

```latex
\textbf{Division of roles.} Large language models act in this review
only as \emph{supervised research assistants}: they assisted candidate
identification (cycle~1), drafted the full-text PICOC extractions, and
drafted the full-text assessments. None of them takes a decision. Every
screening, eligibility, and inclusion decision, every protocol
amendment and ratified rule, every adjudication of a divergence among
the assistants, and the review of every LLM-drafted assessment and
extraction were performed by the authors --- the master's student as
review conductor, with each decision reviewed and approved by the
advisor.

```

#### A.5. PICOC — linhas 248–249

**Trecho atual:**

```latex
A protocol rule (v1.1.0), introduced after a three-rater calibration of
the PICOC extraction itself, requires that \emph{Comparison} be recorded
```

**Substituir por:**

```latex
A protocol rule (v1.1.0), introduced after a calibration of the PICOC
extraction itself across the three LLM assistants, requires that \emph{Comparison} be recorded
```

#### A.6. PICOC — linha 253

**Trecho atual:**

```latex
applicable. This rule eliminated 100\% of the inter-rater divergences
```

**Substituir por:**

```latex
applicable. This rule eliminated 100\% of the inter-assistant divergences
```

#### A.7. Search and identification — linhas 314–315

**Trecho atual:**

```latex
identification combined assisted search (cycle~1: three independent LLM
assistants, $\approx$51 raw records), author-driven discovery (cycle~2:
```

**Substituir por:**

```latex
identification combined assisted search (cycle~1: three LLM assistants
supervised by the authors, $\approx$51 raw records), author-driven discovery (cycle~2:
```

#### A.8. Selection criteria — linhas 337–338

**Trecho atual:**

```latex
SJR quartiles as auxiliary input; for international validity the review
conductor later ratified the criterion directly on the Scopus percentile
```

**Substituir por:**

```latex
SJR quartiles as auxiliary input; for international validity the
authors later ratified the criterion directly on the Scopus percentile
```

#### A.9. Selection criteria — linha 346

**Trecho atual:**

```latex
is the root cause of three of the eight residual inter-rater
```

**Substituir por:**

```latex
is the root cause of three of the eight residual inter-assistant
```

#### A.10. Ratified protocol rules (R1--R3) — linhas 366–368

**Trecho atual:**

```latex
The inter-rater analysis (Section~\ref{sec:reliability}) traced every
residual evaluator divergence to three recurring boundary questions.
After that analysis, the review conductor ratified the following rules,
```

**Substituir por:**

```latex
The inter-assistant agreement analysis (Section~\ref{sec:reliability}) traced every
residual divergence among the LLM assistants to three recurring
boundary questions. After adjudicating those cases, the authors
ratified the following rules,
```

#### A.11. Ratified protocol rules (R1--R3) — linha 402

**Trecho atual:**

```latex
cycle produced \emph{zero} inter-rater divergences, which we read as an
```

**Substituir por:**

```latex
cycle produced \emph{zero} inter-assistant divergences, which we read as an
```

#### A.12. Ratified protocol rules (R1--R3) — linha 404

**Trecho atual:**

```latex
evaluator that had halted on sub-stratum candidates in cycle~2 assessed
```

**Substituir por:**

```latex
assistant that had halted on sub-stratum candidates in cycle~2 assessed
```

#### A.13. Selection flow (PRISMA) — linhas 414–417

**Trecho atual:**

```latex
full-text PICOC extraction of every retrievable candidate (one reading
agent per PDF, consolidated and audited) provided per-study evidence
before assessment --- each screening exclusion cites that evidence and a
precedent from an earlier cycle.
```

**Substituir por:**

```latex
full-text PICOC extraction of every retrievable candidate (one LLM
reading agent per PDF, consolidated and audited by the authors)
provided per-study evidence before assessment --- each screening
exclusion, decided by the authors, cites that evidence and a precedent
from an earlier cycle.
```

#### A.14. Selection flow (PRISMA) — linha 438

**Trecho atual:**

```latex
  {Records identified via assisted search\\(3 independent assistants)\\
```

**Substituir por:**

```latex
  {Records identified via assisted search\\(3 LLM assistants, supervised)\\
```

#### A.15. Selection flow (PRISMA) — linha 466

**Trecho atual:**

```latex
  {Assessed in full text\\(3 independent evaluators)\\\textbf{n = 22}};
```

**Substituir por:**

```latex
  {Assessed in full text\\(3 LLM assistants; decisions by authors)\\\textbf{n = 22}};
```

#### A.16. Selection flow (PRISMA) — linha 486

**Trecho atual:**

```latex
  {Assessed in full text\\(3 independent evaluators)\\\textbf{n = 13}};
```

**Substituir por:**

```latex
  {Assessed in full text\\(3 LLM assistants; decisions by authors)\\\textbf{n = 13}};
```

#### A.17. Three-evaluator protocol — linhas 567–570

**Trecho atual:**

```latex
\subsection{Three-evaluator protocol}
Every full-text assessment was executed independently by three LLM-based
evaluators (Claude, ChatGPT, Gemini) from the same written prompt and
PDF. The agreement set comprises 74 decisions: the 19 foundational
```

**Substituir por:**

```latex
\subsection{LLM-assisted assessment under human decision}
Every full-text assessment was drafted independently by three LLM-based
research assistants (Claude, ChatGPT, Gemini) from the same written
prompt and PDF, each without access to the others' outputs. The
assistants' outputs are \emph{inputs to}, not substitutes for, the
authors' judgment: the master's student reviewed every drafted
assessment, recorded the final include/exclude decision, and
adjudicated every divergence, and the advisor reviewed and approved
those decisions, the protocol amendments, and rules R1--R3. The
agreement set comprises 74 assessments: the 19 foundational
```

#### A.18. Three-evaluator protocol — linhas 574–577

**Trecho atual:**

```latex
assessments. Agreement was computed
on collapsed include/exclude decisions with
Cohen's $\kappa$ per pair~\cite{cohen1960} and Fleiss' $\kappa$ overall
\cite{fleiss1971}. Results are reported in
```

**Substituir por:**

```latex
assessments. Agreement among the assistants was computed on their
collapsed include/exclude recommendations with Cohen's $\kappa$ per
pair~\cite{cohen1960} and Fleiss' $\kappa$ overall~\cite{fleiss1971};
it serves as a consistency check that flags ambiguous cases for human
adjudication, not as a measure of decision validity. Results are
reported in
```

#### A.19. Evidence on MTTD and MTTR — linhas 818–819

**Trecho atual:**

```latex
assessment. Third, \emph{independence}: the three evaluators unanimously
included all four studies, with the applicable caveats attached. Outside this cluster, proxies still dominate: a
```

**Substituir por:**

```latex
assessment. Third, \emph{assessment}: the three LLM assistants
unanimously recommended all four studies for inclusion, and the
authors confirmed the inclusions with the applicable caveats attached. Outside this cluster, proxies still dominate: a
```

#### A.20. Inter-rater reliability — linha 1096

**Trecho atual:**

```latex
\subsection{Inter-rater reliability}
```

**Substituir por:**

```latex
\subsection{Agreement among the LLM assistants}
```

#### A.21. Inter-rater reliability — linhas 1099–1103

**Trecho atual:**

```latex
Table~\ref{tab:kappa} reports agreement over the 74 collapsed
include/exclude decisions. Pairwise agreement is 91.9--93.2\%
($\kappa$ 0.58--0.62, with the strictest pair reaching the
\emph{substantial} band); Fleiss' $\kappa=0.60$; \textbf{66/74 decisions
are unanimous} (62 inclusions and 4 exclusions), including all 19
```

**Substituir por:**

```latex
Table~\ref{tab:kappa} reports agreement among the three LLM assistants
over their 74 collapsed include/exclude recommendations; the final
decision in every case was taken by the authors. Pairwise agreement is
91.9--93.2\% ($\kappa$ 0.58--0.62, with one pair reaching the
\emph{substantial} band); Fleiss' $\kappa=0.60$; \textbf{66/74
recommendations are unanimous} (62 inclusions and 4 exclusions), including all 19
```

#### A.22. Inter-rater reliability — linha 1109

**Trecho atual:**

```latex
three evaluators' scores agree and only the consequence rule differs.
```

**Substituir por:**

```latex
three assistants' scores agree and only the consequence rule differs.
```

#### A.23. Inter-rater reliability — linha 1112

**Trecho atual:**

```latex
binds, which one evaluator --- applying the strict criterion --- did
```

**Substituir por:**

```latex
binds, which one assistant --- applying the strict criterion --- did
```

#### A.24. Inter-rater reliability — linha 1114

**Trecho atual:**

```latex
These three families were ratified as protocol rules R1--R3
```

**Substituir por:**

```latex
The authors adjudicated all eight cases, and the three families were
ratified as protocol rules R1--R3
```

#### A.25. Inter-rater reliability — linha 1121

**Trecho atual:**

```latex
(RQ 0.43--0.61; QA 0.31--0.61), with stable evaluator profiles:
```

**Substituir por:**

```latex
(RQ 0.43--0.61; QA 0.31--0.61), with stable assistant profiles:
```

#### A.26. Inter-rater reliability — linha 1123

**Trecho atual:**

```latex
quality bands matched the intermediate evaluator's exactly in cycle~3),
```

**Substituir por:**

```latex
quality bands matched the intermediate assistant's exactly in cycle~3),
```

#### A.27. Inter-rater reliability — linha 1127

**Trecho atual:**

```latex
\caption{Inter-rater agreement on include/exclude decisions (n=74).}
```

**Substituir por:**

```latex
\caption{Agreement among the three LLM assistants on include/exclude
recommendations (n=74; final decisions by the authors).}
```

#### A.28. Inter-rater reliability — linhas 1137–1138

**Trecho atual:**

```latex
\multicolumn{4}{l}{Fleiss' $\kappa$ (three raters): \textbf{0.60};
unanimous decisions: \textbf{66/74}} \\
```

**Substituir por:**

```latex
\multicolumn{4}{l}{Fleiss' $\kappa$ (three assistants): \textbf{0.60};
unanimous recommendations: \textbf{66/74}} \\
```

#### A.29. Methodological lessons for LLM-assisted SLRs — linhas 1240–1241

**Trecho atual:**

```latex
Three findings generalize beyond this topic. First, three independent
LLM evaluators under one written protocol achieve high percentage
```

**Substituir por:**

```latex
Three findings generalize beyond this topic. First, three
independently run LLM assistants under one written protocol, supervised
by human reviewers who keep every decision, achieve high percentage
```

#### A.30. Methodological lessons for LLM-assisted SLRs — linha 1245

**Trecho atual:**

```latex
effective audit mechanism. Second, protocol amendments must be placed in
```

**Substituir por:**

```latex
effective mechanism for directing human attention to the cases that
need adjudication. Second, protocol amendments must be placed in
```

#### A.31. Methodological lessons for LLM-assisted SLRs — linha 1247

**Trecho atual:**

```latex
the one evaluator that missed the cycle-2 stratum amendment read it as
```

**Substituir por:**

```latex
the one assistant that missed the cycle-2 stratum amendment read it as
```

#### A.32. Threats to Validity — linhas 1270–1271

**Trecho atual:**

```latex
percentile in quartiles (Q1--Q3 eligible), ratified by the review
conductor for international validity; the first three cycles
```

**Substituir por:**

```latex
percentile in quartiles (Q1--Q3 eligible), ratified by the authors
for international validity; the first three cycles
```

#### A.33. Threats to Validity — linhas 1281–1288

**Trecho atual:**

```latex
\textbf{Evaluator validity.} All three raters are LLM systems;
they are independent of each other but share potential model-family
biases. The unanimity of the core corpus (89\%), the protocol-only
nature of divergences, per-claim evidence anchors in every assessment,
and a divergence-free third cycle under the ratified rules mitigate ---
but do not eliminate --- this threat; the three protocol questions
exposed by the divergences were adjudicated by the (human) review
conductor and ratified as rules R1--R3 (Section~\ref{sec:rules}).
```

**Substituir por:**

```latex
\textbf{Assistant validity.} The three assessment assistants are LLM
systems; they run independently of each other but may share
model-family biases (training data, sensitivity to the shared prompt)
and may misread or misreport content. The main mitigation is the
human-decision design: no screening, inclusion, exclusion, or
adjudication was delegated to an LLM --- all were taken by the authors
(the master's student, reviewed by the advisor) --- and per-claim
evidence anchors (section/page) in every assessment allow each claim
to be traced to its source during that review. The unanimity of the
core corpus (89\%), the protocol-only nature of the divergences, and a
divergence-free third cycle under the ratified rules indicate
consistency among the assistants, not by themselves correctness; the
three protocol questions exposed by the divergences were adjudicated
by the authors and ratified as rules R1--R3 (Section~\ref{sec:rules}).
```

#### A.34. Conclusion — linhas 1299–1301

**Trecho atual:**

```latex
for incident response across three update cycles, assessed by three
independent evaluators with high agreement (66 of 74 decisions
unanimous; the third cycle divergence-free). The field has matured
```

**Substituir por:**

```latex
for incident response across three update cycles, through an
LLM-assisted, human-decided protocol: three supervised LLM assistants
drafted each full-text assessment with high mutual agreement (66 of 74
unanimous; the third cycle divergence-free), and every decision was
taken and reviewed by the authors. The field has matured
```

#### A.35. Acknowledgment — linha 1371

**Trecho atual:**

```latex
doctoral researchers in technology and innovation. Review artifacts
```

**Substituir por:**

```latex
doctoral researchers in technology and innovation. LLM-based assistants
(Claude, ChatGPT, Gemini) were used as described in
Section~\ref{sec:method}; all decisions, analyses, and conclusions were
reviewed by the authors, who take full responsibility for the content
of this article. Review artifacts
```

---

## Parte B — `artigo/proveniencia-paragrafos.md`: sincronização dos blockquotes

Os números de linha referem-se ao arquivo no commit `11f962c`.

#### B.1. Parágrafo #1 — Abstract — linhas 65–67

**Trecho atual:**

```markdown
> and screened, 74 were assessed in full text by three independent
> evaluators (agreement 91.9–93.2% per pair; Fleiss' κ=0.60;
> 66/74 unanimous decisions, with a divergence-free third cycle), and
```

**Substituir por:**

```markdown
> and screened, and 74 were assessed in full text. The review is
> LLM-assisted but human-decided: each full-text assessment was drafted
> independently by three supervised LLM research assistants (Claude,
> ChatGPT, Gemini) under one written protocol (agreement 91.9–93.2% per
> pair; Fleiss' κ=0.60; 66/74 unanimous, with a divergence-free
> third cycle), while every screening, eligibility, inclusion, and
> adjudication decision was made and reviewed by the authors.
```

#### B.2. Parágrafo #12 — Evidence on MTTD and MTTR — linhas 593–594

**Trecho atual:**

```markdown
> assessment. Third, independence: the three evaluators unanimously
> included all four studies, with the applicable caveats attached. Outside this cluster, proxies still dominate: a
```

**Substituir por:**

```markdown
> assessment. Third, assessment: the three LLM assistants
> unanimously recommended all four studies for inclusion, and the
> authors confirmed the inclusions with the applicable caveats attached. Outside this cluster, proxies still dominate: a
```

#### B.3. Parágrafo #19 — Threats to Validity — linhas 1056–1057

**Trecho atual:**

```markdown
> percentile in quartiles (Q1–Q3 eligible), ratified by the review
> conductor for international validity; the first three cycles
```

**Substituir por:**

```markdown
> percentile in quartiles (Q1–Q3 eligible), ratified by the authors
> for international validity; the first three cycles
```

#### B.4. Parágrafo #19 — Threats to Validity — linhas 1067–1074

**Trecho atual:**

```markdown
> Evaluator validity. All three raters are LLM systems;
> they are independent of each other but share potential model-family
> biases. The unanimity of the core corpus (89%), the protocol-only
> nature of divergences, per-claim evidence anchors in every assessment,
> and a divergence-free third cycle under the ratified rules mitigate —
> but do not eliminate — this threat; the three protocol questions
> exposed by the divergences were adjudicated by the (human) review
> conductor and ratified as rules R1–R3 (Section (ref.)).
```

**Substituir por:**

```markdown
> Assistant validity. The three assessment assistants are LLM
> systems; they run independently of each other but may share
> model-family biases (training data, sensitivity to the shared prompt)
> and may misread or misreport content. The main mitigation is the
> human-decision design: no screening, inclusion, exclusion, or
> adjudication was delegated to an LLM — all were taken by the authors
> (the master's student, reviewed by the advisor) — and per-claim
> evidence anchors (section/page) in every assessment allow each claim
> to be traced to its source during that review. The unanimity of the
> core corpus (89%), the protocol-only nature of the divergences, and a
> divergence-free third cycle under the ratified rules indicate
> consistency among the assistants, not by themselves correctness; the
> three protocol questions exposed by the divergences were adjudicated
> by the authors and ratified as rules R1–R3 (Section (ref.)).
```

#### B.5. Parágrafo #20 — Conclusion — linhas 1102–1104

**Trecho atual:**

```markdown
> for incident response across three update cycles, assessed by three
> independent evaluators with high agreement (66 of 74 decisions
> unanimous; the third cycle divergence-free). The field has matured
```

**Substituir por:**

```markdown
> for incident response across three update cycles, through an
> LLM-assisted, human-decided protocol: three supervised LLM assistants
> drafted each full-text assessment with high mutual agreement (66 of 74
> unanimous; the third cycle divergence-free), and every decision was
> taken and reviewed by the authors. The field has matured
```

---

## Parte C — Demais sugestões do parecer (ainda não aplicadas)

Estas mudanças **não** estão no clone. Os trechos atuais são identificados
**pelo texto**, e não pelo número da linha, porque os números mudam depois da
Parte A. Os itens C1–C9 trazem texto pronto. Os itens C10–C14 dependem de dados
ou de decisões dos autores e vêm como checklist.

### C1. Resumo com menos de 250 palavras (limite do IEEE Access)

Se adotar este resumo, **pule A.1 e B.1**: ele substitui o bloco
`\begin{abstract}…\end{abstract}` inteiro e já contém o enquadramento
"LLM-assisted, human-decided". Tem 246 palavras e corrige também o −91% (p90)
para o valor agregado (−63%) e o termo "author-affiliated" (ver C5).

```latex
\begin{abstract}
Incident response (IR) in IT operations is measured by Mean Time to Detect
(MTTD) and Mean Time to Recovery (MTTR) and burdened by operator cognitive
load. Agentic AI systems, which combine Large Language Models (LLMs) with
planning, memory, tool use, and human oversight, are increasingly proposed
as copilots for SRE, NOC, and SOC teams. This systematic literature review
(SLR), following Kitchenham's guidelines and the PRISMA~2020 statement,
asks whether the published evidence supports that promise. Across three
update cycles over a foundational corpus, 126~candidate studies
(2020--2026) were screened, 74 were assessed in full text, and
\textbf{65} were included. The review is LLM-assisted but human-decided:
three supervised LLM assistants (Claude, ChatGPT, Gemini) drafted each
assessment independently (Fleiss' $\kappa=0.60$; 66/74 unanimous), and
every decision was made and reviewed by the authors. Four primary studies
measure time metrics against executed baselines, reporting reductions in
MTTD (82--83\%), MTTR (63--72\%), and time-to-containment (38\%); two of
them appear in bottom-quartile or unindexed venues, and the only
production deployment is vendor-affiliated. Elsewhere, the evidence
consists of detection proxies (accuracy, F1, AUC) and qualitative claims.
Within the review's scope, no study measured operator cognitive load in
the presence of an agentic copilot in IT incident response, although
validated instruments exist in adjacent domains. The claim that agentic
copilots reduce MTTD and MTTR is therefore supported by early primary
evidence only. We outline an agenda of multi-site field evaluations that
report nominal MTTD and MTTR against their own baselines together with
validated workload measures.
\end{abstract}
```

> Atenção: confira com os autores se "63--72\%" é a faixa que querem para
> MTTR. 63\% é o agregado de P100 e 72,3\% é o de P101. Se preferirem
> manter o p90 de P100, escrevam "p90" explicitamente.

### C2. Citação correta das diretrizes de Kitchenham

**Problema:** `kitchenham2009` é um estudo terciário, não as diretrizes.

**Em `referencias.bib`, acrescentar:**

```bibtex
@techreport{kitchenham2007,
  author      = {Barbara Kitchenham and Stuart Charters},
  title       = {{Guidelines for Performing Systematic Literature Reviews in Software Engineering}},
  institution = {Keele University and Durham University},
  number      = {EBSE-2007-01},
  year        = {2007}
}
```

**Em `main.tex` (Introdução e Seção III), trocar:**

```latex
guidelines of Kitchenham et al.~\cite{kitchenham2009}
```

por:

```latex
guidelines of Kitchenham and Charters~\cite{kitchenham2007}
```

e

```latex
The protocol follows Kitchenham et al.~\cite{kitchenham2009}: planning
```

por:

```latex
The protocol follows Kitchenham and Charters~\cite{kitchenham2007}: planning
```

Remova `kitchenham2009`, a menos que ele seja citado com outro propósito.

### C3. Rede de citações: hub fora do corpus e frase factualmente errada (Seção IV-E)

**Trecho atual:**

```latex
\cite{P09} (6) --- followed by the AIOps/MLOps and log-anomaly surveys
\cite{P16,P65} and the SOC hyper-automation study \cite{P76} (3 each).
```

**Substituir por:**

```latex
\cite{P09} (6) --- followed by the AIOps/MLOps survey \cite{P16} and the
SOC hyper-automation study \cite{P76} (3 each; the log-anomaly survey
\cite{P65}, a screened candidate outside the corpus, also receives 3).
```

**Trecho atual:**

```latex
the cycle-3 surveys cite both the definitional layer and cycle-2 studies
\cite{P101,P112,P121}.
```

**Substituir por:**

```latex
the cycle-3 surveys cite back into the definitional layer
(\cite{P112}$\rightarrow$\cite{P05}; \cite{P121}$\rightarrow$\cite{P14}),
and the event-driven SOC \cite{P101} cites the intra-cycle survey
\cite{P121}.
```

**Legenda da Fig. 4:** acrescente esta frase para explicar os nós que estão fora do corpus:

```latex
Nodes marked $^{\ddagger}$ in Table~\ref{tab:pids} are screened
candidates or excluded studies that take part in citation edges but are
not part of the included corpus; included studies without internal edges
are omitted.
```

### C4. Conclusão: não agregar métricas incomparáveis

**Trecho atual:**

```latex
four primary studies reports nominal MTTD, MTTR, and time-to-containment
reductions of 38--91\% against executed baselines --- half of it below
```

**Substituir por:**

```latex
four primary studies reports nominal reductions against executed
baselines --- MTTD by 82--83\%, MTTR by 63--72\%, and time-to-containment
by 38\%, in settings ranging from one production deployment to testbeds
and a public dataset --- half of it below
```

### C5. "author-affiliated" → "vendor-affiliated" (4 ocorrências)

A expressão sugere que o estudo é afiliado aos autores desta revisão. Substitua
nas quatro ocorrências:

| Trecho atual                                                      | Substituir por                                              |
| ----------------------------------------------------------------- | ----------------------------------------------------------- |
| `a single, author-affiliated one;` (IV-C)                         | `a single, vendor-affiliated one;`                          |
| `author-affiliated deployment. Reviewers and practitioners` (V-A) | `vendor-affiliated deployment. Reviewers and practitioners` |
| `flagged as author-affiliated and single-vendor.` (VI)            | `flagged as vendor-affiliated and single-site.`             |
| `author-affiliated deployment, and still without` (VII)           | `vendor-affiliated deployment, and still without`           |

### C6. Dado de 277 dias: citar a fonte primária (Introdução)

**Trecho atual:**

```latex
SOC personnel. Industry reports cited in the corpus place average breach
identification and containment at 277~days (204 to detect, 73 to
contain)~\cite{P79}, while SOC analysts discard the majority of alerts as
false positives.
```

**Substituir por** (confira o ano do relatório citado em P79):

```latex
SOC personnel. In security operations, industry data place the average
data-breach life cycle at 277~days (204 to identify, 73 to
contain)~\cite{ibm2023breach}, as relayed in the corpus~\cite{P79}; this
security-breach life cycle is related to, but distinct from, the
availability-incident MTTR of SRE practice.
```

```bibtex
@techreport{ibm2023breach,
  author      = {{IBM Security and Ponemon Institute}},
  title       = {{Cost of a Data Breach Report 2023}},
  institution = {IBM Corporation},
  year        = {2023}
}
```

A frase "_SOC analysts discard the majority of alerts as false positives_" está
sem citação: cite uma fonte ou remova.

### C7. Página de rosto e agradecimentos (conformidade IEEE)

1. Remova `\IEEEmembership{Master's Degree Student}` (não é um grau de membro
   IEEE). Se o autor for membro, use `\IEEEmembership{Student Member, IEEE}`.
2. **Trecho atual** (`\tfootnote`):
   ```latex
   \tfootnote{This work was conducted within the Applied Computing Graduate
   Program (PPGCA) at Unisinos, Brazil --- a program of excellence dedicated
   to educating master's and doctoral researchers in technology and
   innovation.}
   ```
   **Substituir por** (ajuste o financiamento à realidade):
   ```latex
   \tfootnote{This work was supported in part by [FUNDING AGENCY / PROGRAM,
   grant no.\ XXX]. (If none: ``This research received no specific
   grant.'')}
   ```
3. Nos agradecimentos, **trecho atual**:
   ```latex
   The authors thank the Applied Computing Graduate Program (PPGCA) at
   Unisinos, a program of excellence dedicated to educating master's and
   doctoral researchers in technology and innovation.
   ```
   **Substituir por:**
   ```latex
   The authors thank the Applied Computing Graduate Program (PPGCA) at
   Unisinos.
   ```
4. **Disponibilidade dos dados.** Troque "_available from the authors upon
   reasonable request_" por um depósito com DOI:
   ```latex
   Review artifacts (protocol, prompts, assessments, extraction sheets, and
   machine-readable tables) are openly available at
   \url{https://doi.org/10.5281/zenodo.XXXXXXX}.
   ```
5. **Conflito de interesses.** Acrescente nos agradecimentos, ou numa seção própria:
   ```latex
   \textbf{Competing interests.} The first author is employed in IT
   operations leadership at a communications-platform company; the company
   had no role in the design, conduct, or reporting of this review. The
   authors declare no other competing interests.
   ```
6. **E-mail correspondente:** use só o institucional
   (`valdomiros@edu.unisinos.br`) em `\corresp`.

### C8. Concordância: estatísticas robustas à prevalência (Seção IV-F)

Acrescente ao final do primeiro parágrafo da seção (calcule os valores com os
dados do repositório):

```latex
Because 90.1\% of the recommendations are ``include'', we also report
prevalence-robust coefficients: Gwet's AC1~\cite{gwet2008} of [X.XX] and
PABAK~\cite{byrt1993} of [X.XX] (95\% CI [X.XX--X.XX]); interpretation
bands follow Landis and Koch~\cite{landis1977}.
```

```bibtex
@article{gwet2008,
  author  = {Kilem Li Gwet},
  title   = {{Computing inter-rater reliability and its variance in the presence of high agreement}},
  journal = {British Journal of Mathematical and Statistical Psychology},
  volume  = {61}, number = {1}, pages = {29--48}, year = {2008}
}
@article{byrt1993,
  author  = {Ted Byrt and Janet Bishop and John B. Carlin},
  title   = {{Bias, prevalence and kappa}},
  journal = {Journal of Clinical Epidemiology},
  volume  = {46}, number = {5}, pages = {423--429}, year = {1993}
}
@article{landis1977,
  author  = {J. Richard Landis and Gary G. Koch},
  title   = {{The measurement of observer agreement for categorical data}},
  journal = {Biometrics},
  volume  = {33}, number = {1}, pages = {159--174}, year = {1977}
}
```

Também na Seção III, logo após "_mirroring the DARE criteria~\cite{dare}_",
justifique o uso de um instrumento pensado para revisões, ou adote o checklist de
Dybå e Dingsøyr para estudos primários:

```bibtex
@article{dyba2008,
  author  = {Tore Dyb{\aa} and Torgeir Dings{\o}yr},
  title   = {{Empirical studies of agile software development: A systematic review}},
  journal = {Information and Software Technology},
  volume  = {50}, number = {9--10}, pages = {833--859}, year = {2008}
}
```

### C9. Referências metodológicas que faltam

Acrescente e cite onde indicado:

```bibtex
@inproceedings{wohlin2014,
  author    = {Claes Wohlin},
  title     = {{Guidelines for snowballing in systematic literature studies and a replication in software engineering}},
  booktitle = {Proc. 18th Int. Conf. Evaluation and Assessment in Software Engineering (EASE)},
  year      = {2014}
}
@article{mendes2020update,
  author  = {Emilia Mendes and Claes Wohlin and Katia Felizardo and Marcos Kalinowski},
  title   = {{When to update systematic literature reviews in software engineering}},
  journal = {Journal of Systems and Software},
  volume  = {167}, pages = {110607}, year = {2020}
}
@article{rethlefsen2021prismas,
  author  = {Melissa L. Rethlefsen and others},
  title   = {{PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews}},
  journal = {Systematic Reviews},
  volume  = {10}, pages = {39}, year = {2021}
}
```

- `wohlin2014`: na frase "_Backward/forward snowballing is mandatory in the protocol_".
- `mendes2020update`: na Introdução, junto de "_executed as an \emph{update review}_".
- `rethlefsen2021prismas`: na Seção III-D, ao apresentar a string de busca (ver C10).

> Confira volume e páginas no DOI antes de submeter. Os metadados acima foram
> escritos de memória.

### C10. Checklist: itens que dependem de dados ou decisões dos autores

- [ ] **String de busca completa** (Seção III-D ou apêndice), por base, com
      data de execução e filtros (PRISMA item 7 / PRISMA-S).
- [ ] **Fluxo PRISMA com os registros brutos.** Para o ciclo 3, mostrar
      12.783 (Scopus) / ≈49.700 (OpenAlex) → deduplicação → triagem por
      título/resumo → 37 candidatos.
- [ ] **Corrigir o PRISMA do ciclo 3:**
  - Na Tabela 2, "Screened 19" e "Excluded at screening 19 (18 E1, 1 E3)" não fecham.
  - Na Fig. 2, o nó ao lado de "Assessed n=13" diz "Excluded at screening: 1 (E3)",
    mas o estudo foi avaliado e excluído. Mova-o para "Excluded after assessment".
  - "15 sub-threshold kept with caveat" e "11 kept with caveat" vêm da escala
    Qualis antiga e conflitam com as **3** ressalvas atuais. Atualize ou explique.
- [ ] **Ciclo 1 na Fig. 2:** "Assessed n=18", mas 20 foram avaliados (os 2
      inelegíveis também). Mostre isso no diagrama.
- [ ] **Critério I4:** está ausente na lista (I1, I2, I3, I5, I6), mas é citado
      como "_I3/I4 strata_". Defina-o ou renumere.
- [ ] **Versões dos LLMs:** modelo exato, datas, temperatura e modo de entrada
      do PDF (Seção III-I), com mapeamento A/B/C → modelos na Tabela 4.
- [ ] **Validação humana independente** de uma amostra estratificada (20–30%)
      com κ humano×LLM, e conferência dos números do resultado central.
      Quando houver o resultado, acrescente ao resumo: "_validated against
      independent human assessment on a stratified sample (κ = …)_".

### C11. Checklist: método e escopo

- [ ] **Busca retroativa:** re-executar a string validada para todo o período
      2020–2026 e informar quantos estudos dos ciclos 1 e 2 ela recupera.
- [ ] **Bases:** incluir IEEE Xplore e ACM DL, ou justificar a ausência; e
      justificar a exclusão de _preprints_/arXiv.
- [ ] **Verificar trabalhos conhecidos** e, se forem excluídos, dizer por qual
      critério:
  - RCACopilot (EuroSys 2024);
  - Ahmed et al. (ICSE 2023);
  - RCAgent (CIKM 2024);
  - AIOpsLab, ITBench e OpenRCA;
  - ensaio randomizado do Microsoft Security Copilot (Edelman et al., 2023).
- [ ] **Snowballing** sobre todo o conjunto incluído (Wohlin), ou declarar a limitação.
- [ ] **Quadro de desvios do protocolo:** protocolo _a priori_ × emendas datadas
      × justificativa, mais uma análise de sensibilidade com e sem os estudos
      admitidos por emenda.
- [ ] **Justificar I5** (≥1 citação) e a janela de 2020 (o fenômeno começa em 2023).
- [ ] **Definição operacional de "agentic"**, aplicada de forma consistente.
      P25, P88 e P91 não usam LLM; o _cluster_ de fatores humanos entrou por emenda.
- [ ] **Busca dirigida a carga cognitiva** (workload, NASA-TLX, alert fatigue,
      CHI/CSCW). Sem ela, troque "_the intersection … is empty_" por
      "_no study within our search scope …_".

### C12. Checklist: síntese e resultados

- [ ] **RQs** alinhadas ao título (MTTD/MTTR, carga cognitiva, arquiteturas,
      riscos), ou ajustar o título.
- [ ] **Uma subseção por RQ** em Resultados, em especial RQ2 (arquiteturas e
      mecanismos) e RQ4 (riscos).
- [ ] **Tabela de extração dos estudos com métrica de tempo**
      (P100, P101, P102, P123, e P93 à parte), com colunas: cenário, dados,
      baseline, métrica e definição, valores, teste estatístico, veículo,
      afiliação, QA e risco de viés.
- [ ] **Definições de MTTR** (Recovery/Repair/Resolve/Respond) padronizadas
      numa subseção do Background; "p90" sempre nomeado como percentil.
- [ ] **Graduação da evidência** (GRADE/CERQual adaptado).
- [ ] **P93:** explicar como um estudo com tabelas internamente inconsistentes
      passou no QA e como foi tratado na síntese.
- [ ] **Taxonomia completa** dos 65 estudos (a Tabela 3 cobre 48) num apêndice.
- [ ] **Tabela comparativa com revisões existentes** (P24, P33, P52, P54, P79,
      P110, P112, P121 e surveys de AIOps com LLM), mostrando a novidade.
- [ ] **Definição de copilot vs. agente autônomo** (níveis de autonomia,
      HITL/HOTL) como eixo de classificação.

### C13. Checklist: ameaças à validade

- [ ] **Construto:** heterogeneidade das definições de MTTD/MTTR; proxies vs.
      métricas nominais; p90 vs. média.
- [ ] **Viés de publicação e de fornecedor**; testbeds sintéticos.
- [ ] **Validade externa:** peso de SOC/segurança em relação a SRE/NOC.
- [ ] **Reescrever** "_All conclusions hold with the three below-bar inclusions
      removed_": o _cluster_ central cai de 4 para 2 estudos, então a conclusão
      central **não** se mantém intacta. Sugestão:
  ```latex
  Removing the three below-bar inclusions leaves the qualitative
  conclusions unchanged but materially weakens the central one: the
  cycle-3 nominal-metric cluster narrows from four studies to two
  (\cite{P100,P123}), losing its testbed MTTR evidence ---
  ```

### C14. Checklist: apresentação

- [ ] Reduzir a narrativa ciclo a ciclo; consolidar Métodos e Resultados e
      levar a evolução por ciclo para uma subseção curta ou para o suplemento.
- [ ] Definir ou substituir o jargão interno: "foundational-conditional",
      "stratum", "normative Stage-1 text", "series-stratum rule", "mandatory
      caveat".
- [ ] Remover o tom autopromocional ("_fully reproducible_", "_unusually_").
- [ ] Fig. 3 com valores rotulados (pgfplots) ou como tabela; Fig. 4 em layout
      por camadas ou como matriz.
- [ ] Novas figuras e tabelas: distribuição por ano, por tipo de veículo e por
      domínio (SRE/NOC vs. SOC); mapa RQ × estudo; QA por estudo (suplemento).
- [ ] Completar volume, número e páginas nas 88 entradas do `referencias.bib`.
- [ ] Checklist PRISMA 2020 como suplemento; registrar o protocolo (OSF) ou
      declarar que não houve registro.
