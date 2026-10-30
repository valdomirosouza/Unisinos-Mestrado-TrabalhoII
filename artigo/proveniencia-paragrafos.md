# Proveniência parágrafo a parágrafo — artigo da RSL (draft v2)

> 🧭 [📄 Artigo](README.md) · [🗂️ Fichas de extração](../report/README.md) · [🏠 README raiz](../README.md)

Rastreabilidade da escrita do artigo (`main.tex`, draft v2 pós-PDR-0009):
para **cada parágrafo que usa informação extraída dos papers**, os
trechos-fonte — tomados das **fichas de extração** (`report/PXX-extraction.csv`),
que registram cada claim **com a âncora de seção/página do paper original** —
seguidos do parágrafo escrito no artigo.

Como ler cada entrada:

- **Fontes:** um bloco por paper citado, com o ID, o título do paper, o campo
  da ficha de onde o trecho vem e o trecho em si (as âncoras "§X, p. Y"
  internas ao trecho apontam o parágrafo/página do paper original).
- **Texto do artigo:** o parágrafo correspondente do `main.tex` (LaTeX
  convertido para leitura; `[PXX]` marca as citações).

Parágrafos **sem fonte em papers** (método, protocolo, PRISMA, estatísticas
κ) derivam dos artefatos do próprio repositório — `protocolo/` (PDRs),
`reviews/*.csv` (escores e comparações), `picoc/` e `research/` — e não são
listados aqui. A menção ao hub [P65] (§IV-E) deriva do artefato
[`citacoes-cruzadas-P01-P89.md`](../citacoes-cruzadas-P01-P89.md), não de
ficha. O Abstract e a Conclusão não usam `\cite`, mas derivam do cluster
MTTD/MTTR e do survey de SOC — mapeados manualmente.

---

## Parágrafo #1 — Abstract

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only (survey reports results of cited primary studies; no own measurements): CyberAlly's AI-driven triage "halved false positives from 70% to 35% and reduced Mean Time To Respond (MTTR) from 8 h to 90 min", with automated ticketing rising from 10% to 75% (Sec. 3.2, p. 6); alert-fatigue baseline: SOCs process over 10,000 daily alerts, more than half false positives (Sec. 3.2, p. 5); […]
- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> Incident response (IR) in modern IT operations is constrained by two
> time-based indicators — Mean Time to Detect (MTTD) and Mean Time to
> Recovery (MTTR) — and by the cognitive load imposed on operations teams
> (SRE, NOC, SOC) by alert fatigue and telemetry complexity. Agentic AI
> systems, which combine Large Language Models (LLMs) with planning, memory,
> tool use, and human supervision, are increasingly proposed as
> copilots for these teams. This article reports a systematic
> literature review (SLR), conducted under the guidelines of Kitchenham et
> al. and the PRISMA 2020 flow, that consolidates the evidence on Agentic
> AI copilots for incident response, with cognitive-load reduction treated
> as a complementary outcome. Across three update cycles over a
> foundational corpus, 126 candidate studies (2020–2026) were identified
> and screened, 74 were assessed in full text by three independent
> evaluators (agreement 91.9–93.2% per pair; Fleiss' κ=0.60;
> 66/74 unanimous decisions, with a divergence-free third cycle), and
> 65 studies were included. Three findings result. First, through
> two cycles no included study measured MTTD or MTTR nominally against its
> own executed baseline; the third cycle surfaces a first cluster of four
> primary studies that do — MTTD reduced by 82–83%, MTTR by 72–91%,
> and time-to-containment by 38% against executed human, polling, or SOAR
> baselines — two of the four below the review's venue bar (bottom-quartile
> or unindexed venues) under a mandatory caveat, and production evidence
> from a single vendor, moving the headline claim from unverified to
> supported by early primary evidence. Second, outside that cluster the evidence
> remains dominated by detection proxies (accuracy, F1, AUC) and
> qualitative claims, while secondary sources relay dramatic gains (e.g.,
> MTTR from 8 hours to 90 minutes) that primary experiments are only
> beginning to approach. Third, direct measurement of operator cognitive
> load exists in adjacent domains but has never been combined with an
> agentic copilot in IT incident response — a gap all three cycles leave
> untouched. These findings define a concrete agenda: venue-quality,
> multi-site field evaluations of agentic copilots instrumented for
> nominal MTTD/MTTR with their own baselines and validated cognitive-load
> instruments.

---

## Parágrafo #2 — Introduction

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only (survey reports results of cited primary studies; no own measurements): CyberAlly's AI-driven triage "halved false positives from 70% to 35% and reduced Mean Time To Respond (MTTR) from 8 h to 90 min", with automated ticketing rising from 10% to 75% (Sec. 3.2, p. 6); alert-fatigue baseline: SOCs process over 10,000 daily alerts, more than half false positives (Sec. 3.2, p. 5); […]

**Texto do artigo:**

> IT operations teams face a structural asymmetry:
> distributed, cloud-native systems generate telemetry at machine speed,
> while detection, diagnosis, and remediation remain bounded by human
> cognition. The operational cost of this asymmetry is captured by two
> indicators — Mean Time to Detect (MTTD) and Mean Time to
> Recovery (MTTR) — and by a human cost that is harder to see on
> dashboards: alert fatigue and sustained cognitive load on SRE, NOC, and
> SOC personnel. Industry reports cited in the corpus place average breach
> identification and containment at 277 days (204 to detect, 73 to
> contain) [P79], while SOC analysts discard the majority of alerts as
> false positives.

---

## Parágrafo #3 — Introduction

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable (conceptual review; no MTTD/MTTR measurements or baselines reported). Qualitative claims relevant to incident response: in an enterprise cybersecurity incident response example, the agentic model "enhances decision latency, reduces false positives, and supports proactive threat containment" versus rule-based systems (Sec. 4.0.2, p. 16); […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no MTTD, MTTR, alert-fatigue, or incident-resolution measurements are reported. Only qualitative adjacent claims: a hospital Agentic AI case study "improves the time taken to respond to various health issues" (Sec. VI.B, p. 18922); customer-service agents "enhancing response time and client satisfaction" (Sec. V.B, p. 18919); […]

**Texto do artigo:**

> Agentic AI — AI systems that pursue goals with some degree of
> autonomy by combining LLM-based reasoning with planning, memory, tool
> use, and human oversight [P09,P10] — has been proposed as a new
> operating model for incident response: not full automation, but a
> copilot that perceives, reasons, acts, and learns alongside the
> human operator. The promise is threefold: earlier detection (MTTD),
> faster remediation (MTTR), and a lighter day-to-day workload for
> operations teams.

---

## Parágrafo #4 — From AIOps to Agentic AI

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P05 — A Survey of AIOps in the Era of Large Language Models**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Tool-Augmented Generation lets LLMs query monitoring systems, execute diagnostic scripts, and automate workflows (RCAgent, RCACopilot, LLexus, AIOpsLab, a GPT-4 agent "competently using 150 distinct tools across nine categories"); however, for the highest automation level (Automatic Execution) "related work is limited, and its practical effectiveness remains to be verified"; […]
- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Provides a multi-dimensional comparative framework (Tables 1-9) distinguishing Generative AI, AI Agents, Agentic AI, and Generative Agents across autonomy, memory, orchestration, and coordination (Sec. 3.0.2, pp. 8-12). […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Proposes evaluation metrics for agentic deployments: adaptability, goal achievement efficiency, learning rate/convergence, robustness and resilience, scalability, user satisfaction/human-AI collaboration efficiency (Sec. VI.A, Table 8, p. 18922-18923). Critical evaluation: hybrid classical+agentic models "often yield superior results"; […]
- **P15 — The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Architecture trade-offs: ReAct offers fast iteration but "little parallelism, weak long-horizon coordination"; supervisor/hierarchical scales but risks supervisor bottleneck/single point of failure; hybrid needs arbitration design; reflection reduces hallucination "while adding computational overhead" (Sec. 3.3.2, pp. 14-17; Table 4, p. 21). […]
- **P16 — A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Not applicable — no agentic or multi-agent systems are evaluated. Related findings: prior work observes that in AIOps "many of the solutions focus on detection and root cause analysis, but automation is still limited" [25] (Sec. 5, p. 21); AIOps monitoring can free IT professionals for more innovative tasks (Sec. 4.3.1, p. 15); LLM challenges now center on "the trustworthiness of the results" (Sec. 4.1.4, p. 12)
- **P54 — From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > Reports third-party results: Agent-as-a-Judge reaches 90% alignment with human judgments vs. 60–70% for LLM-as-a-Judge, cutting evaluation cost to approx. 2.29% ($30.58 vs. $1,297.50) and time to 118.43 minutes vs. 86.5 hours (Sec. III-H, p. 84246); in MultiAgentBench, cognitive planning gives a 3% improvement in milestone achievement while "adding more agents can decrease performance" (Sec. III-U, p. 84249); […]

**Texto do artigo:**

> AIOps applies machine learning to IT operations data — logs, metrics,
> traces — for anomaly detection, root cause analysis (RCA), and
> remediation. Surveys in the corpus trace its evolution from
> knowledge-based automation to ML pipelines [P16] and, after 2023,
> to LLM-centered architectures [P05]. The agentic turn adds goal
> pursuit under governance: taxonomies distinguish AI agents
> (tool-using, single-task) from Agentic AI (multi-step autonomy
> with planning and memory) [P09], and reference surveys map its
> technologies, applications, and societal implications [P10,P15,P54].

---

## Parágrafo #5 — Incident response and its metrics

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P28 — A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not measured by name (Not specified as formal metrics); adjacent incident-handling results: analyst triage time "decreased by 38.5% on average due to clear, contextual explanations"; false positive alerts reduced by 41.3% versus a traditional SIEM baseline (alert-fatigue proxy); analyst confidence averaged 4.6 on a 5-point scale; […]
- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only (survey reports results of cited primary studies; no own measurements): CyberAlly's AI-driven triage "halved false positives from 70% to 35% and reduced Mean Time To Respond (MTTR) from 8 h to 90 min", with automated ticketing rising from 10% to 75% (Sec. 3.2, p. 6); alert-fatigue baseline: SOCs process over 10,000 daily alerts, more than half false positives (Sec. 3.2, p. 5); […]

**Texto do artigo:**

> Incident response spans detection, triage, diagnosis (RCA), remediation,
> and post-incident learning. MTTD and MTTR are its canonical outcome
> metrics; alert fatigue and operator cognitive load are its canonical
> human costs. In security operations, the same cycle appears as SOC
> triage and SOAR playbooks [P28,P79]. A persistent finding of this
> review — anticipated here — is that primary studies rarely
> instrument these nominal metrics, reporting detection-quality proxies
> instead.

---

## Parágrafo #6 — The foundational corpus and its hubs

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > A structured conceptual taxonomy separating AI Agents (modular, single-entity, LLM/LIM-driven, tool-augmented systems for narrow task automation) from Agentic AI (orchestrated multi-agent ecosystems with goal decomposition, dynamic role assignment, persistent episodic/semantic/vector memory, and coordinated autonomy) (Sec. 3.0.1-3.1, pp. 7-13). […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Survey (no system proposed). Synthesizes technical foundations: reinforcement learning, goal-oriented architectures, adaptive control (Sec. II.D, p. 18915); architectural approaches: Multi-Agent Systems (MAS), Hierarchical Reinforcement Learning (HRL), goal-oriented modular architectures (Sec. IV.A, p. 18917); […]
- **P14 — Transforming cybersecurity with agentic AI to combat emerging cyber threats (Kshetri)**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Conceptual analysis of agentic AI automating SOC decision-making, threat detection, alert triage, and incident response; describes AI agent modules (Interfaces, Memory, Profile, Planning, Action); surveys vendor solutions — ReliaQuest GreyMatter (multiple agents/models executing tasks simultaneously), CrowdStrike Charlotte AI Detection Triage, Twine digital employee Alex (creates task plans, seeks human approval befo […]

**Texto do artigo:**

> The present review updates a foundational SLR (19 studies, P01–P19;
> the protocol identifiers Pxx used throughout, notably in
> Figs. (ref.) and (ref.), are mapped to the
> bibliography in the Appendix, Table (ref.)).
> Cross-citation analysis over the full corpus (Section (ref.))
> shows that three foundational surveys act as conceptual hubs —
> [P10] and [P14] (7 internal citations each) and [P09] (6)
> — confirming their role as the definitional substrate on which the
> empirical studies build.

---

## Parágrafo #7 — Ratified protocol rules (R1–R3)

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P24 — AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0**
  — _campo da ficha: Methodology_
  > SLR following PRISMA guidelines; search of Scopus, Web of Science, IEEE Xplore, and ScienceDirect with query TITLE-ABS-KEY ("AgentAI" OR "AgenticAI" OR "Agentic AI"); 255 initial articles (130 Scopus, 64 WoS, 25 ScienceDirect, 36 IEEE Xplore) reduced to 144 after removing non-English and duplicates, then to a final set of 66 experimental articles (reviews/surveys excluded, past decade only); […]
- **P33 — A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense**
  — _campo da ficha: Methodology_
  > Narrative review (explicitly not systematic) of literature 2005-2025 (eligibility window 2010-2025); databases IEEE Xplore, Scopus, Web of Science, ACM Digital Library plus grey literature (reports, policy briefs); Boolean search with iterative refinement, reference chaining, and selective use of generative AI tools for thematic clustering; […]
- **P52 — Application of Large Language Models in Cybersecurity: A Systematic Literature Review**
  — _campo da ficha: Methodology_
  > Systematic Literature Review (simplified adaptation of the Kitchenham Guidelines and PRISMA); 8 databases/platforms (arXiv, IEEE Xplore, ResearchGate, Scopus, Google Scholar, ScienceDirect, SpringerLink, ACM Digital Library) queried with 26 keyword sets; 250 articles screened, 177 (2018-March 2024) retained and classified into 7 topical categories; 68% of the reviewed literature published in 2023 (Abstract; Sec. […]
- **P54 — From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review**
  — _campo da ficha: Methodology_
  > Comprehensive literature review (secondary study) with comparative tables and a taxonomy covering approx. 60 benchmarks (2019–2025), AI-agent frameworks and applications (2023–2025), 3 agent protocols, and 3 training datasets; no empirical experiment of its own and no formal SLR protocol (search strings, inclusion/exclusion criteria) is reported (Sec. I, p. 84238; Sec. III, p. 84242; Sec. IV, p. 84251).
- **P62 — A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance**
  — _campo da ficha: Methodology_
  > Narrative (non-systematic) literature review with conceptual framework synthesis; maps psycho-physiological and behavioral markers of five degraded mental states in Table 1 and a countermeasure typology in Figure 4; no SLR protocol, dataset, environment, or sample size reported (article type REVIEW, p. 1; Sec. Understanding Performance Related Mental States, pp. 5-8; Sec. […]
- **P63 — The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents**
  — _campo da ficha: Methodology_
  > Scale development via four sequential studies: (1) systematic literature review following PRISMA guidelines (final database of 34 literature items; revised list of 27 attributes from Radziwill and Benton's 38); (2) online consensus survey with 29 completing participants of 50 invited experts and end-users (Krippendorff's Alpha = 0.780; 17 attributes retained); […]
- **P69 — WAUC: A Multi-Modal Database for Mental Workload Assessment Under Physical Activity**
  — _campo da ficha: Methodology_
  > Database/resource paper with a controlled laboratory experiment and validation study; 48 participants (22 treadmill: 9 male/13 female; 26 bike: 16 male/10 female; average age 27.4 ± 6.6 years), full factorial 2 MW x 3 physical strain within-subject design, six 18-min sessions (~2 h total per participant), counterbalanced order; […]
- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Methodology_
  > ⚠ Ambiguous: reported screening counts do not reconcile arithmetically (510 screened; 300 eliminated; 105 included). Systematic literature review (survey) following PRISMA 2020, preregistered at OSF (DOI 10.17605/OSF.IO/9QC7V); […]
- **P81 — Enhancing Control Room Operator Decision Making**
  — _campo da ficha: Methodology_
  > Controlled between-subjects experiment in a simulated formaldehyde-production control room (production of 10,000 kg/h of 30% formaldehyde solution; 80 alarms of different priority levels incl. nuisance alarms; 3 fault scenarios); 48 volunteer participants, predominantly chemical-engineering master's students: Group G1 without DSS n=23, Group G2 with DSS n=25; […]

**Texto do artigo:**

> - R1 (non-agentic secondary studies). Secondary studies
> (surveys/SLRs) whose object is not Agentic AI are
> excluded from the primary corpus regardless of methodological
> quality; agentic-centered secondary studies are retained as
> foundational-conditional background
> (e.g., [P24,P33,P52,P54,P79]). This ratifies the exclusion
> of the non-agentic RCA and log-anomaly reviews assessed in
> cycle 1.
>
> - R2 (normative placement of amendments). Eligibility
> amendments bind only when written into the normative
> Stage-1 text of the assessment protocol, not into its input
> metadata. The cycle-2 stratum amendment is ratified under this
> rule: the four sub-stratum candidates keep their full
> assessments with a mandatory stratum caveat attached to any use
> of their evidence.
>
> - R3 (domain boundary and the human-factors cluster).
> Out-of-domain studies are excluded from the primary corpus even
> when methodologically strong; the human-factors cluster
> [P62,P63,P69,P81] is retained strictly as
> complementary evidence for the cognitive-load outcome
> (Table (ref.)) and never feeds the agentic research
> questions (RQ1, RQ2, RQ4); a cluster study with no RQ adherence
> at all remains excluded.

---

## Parágrafo #8 — Selection flow (PRISMA)

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P24 — AgentAI: A comprehensive survey on autonomous agents in distributed AI for industry 4.0**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Survey (no new system): synthesizes AgentAI architecture as perception, cognition, and action modules (Sec. 3.1, p. 4); core techniques RL/DRL/MARL (QMIX, G2ANet), transformers, and LLMs (GPT-3/4, Llama, Gemini, DeepSeek) plus alternative paradigms (symbolic reasoning, graph-based policies, behaviour trees, probabilistic/Bayesian agents) (Sec. 3.2, pp. 4-6); […]
- **P33 — A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Not a system proposal but a synthesis of Agentic AI (autonomous, adaptable, goal-directed agents) for cyber defense across three pillars: cognitive autonomy, ethical governance, quantum-resilient defense. Catalogs design patterns (reactive agents, proactive goal-seeking, learning-based, Human-in-the-Loop SOC threat-triage assistants, federated agent networks, reflexive cognitive loops; […]
- **P52 — Application of Large Language Models in Cybersecurity: A Systematic Literature Review**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Not applicable (secondary study; no system is proposed). The SLR catalogs AI/LLM uses in defensive and offensive cybersecurity, cyberethics, law, and governance; agent-style approaches surveyed include LLM agents in the NetSecGame environment, PENTESTGPT (Reasoning, Generation, and Parsing modules), Auto-GPT, Wintermute (LLM-guided privilege escalation), and the Cyber Sentinel GPT-4 dialogue system integrating an IoC […]
- **P54 — From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Survey that consolidates the field: side-by-side comparison of benchmarks (2019–2025); taxonomy of approx. 60 LLM/AI-agent benchmarks in 8 categories; review of AI-agent frameworks (2023–2025) integrating LLMs with modular toolkits for autonomous decision-making and multi-step reasoning (LangChain, LlamaIndex, CrewAI, Swarm, OpenAI Agents SDK); […]
- **P72 — From Vulnerability to Defense: The Role of Large Language Models in Enhancing Cybersecurity**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Review article — no single system is proposed; it surveys LLMs (GPT, BERT, PaLM, T5, etc.) applied to threat identification, phishing/malware/intrusion detection, vulnerability management, threat intelligence, incident response, cloud security, compliance and endpoint security, and distills generic LLM-based frameworks (Algorithms 1-3) for malware detection, intrusion detection, and cloud security; […]
- **P77 — Generative AI revolution in cybersecurity: a comprehensive review of threat intelligence and operations**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > No new system is proposed (survey); it reviews GAI/LLM uses in cybersecurity — threat intelligence and threat hunting, honeypots, phishing detection and resilience training, vulnerability scanning/filtering, automated incident response — plus customized security LLMs (Sec-PaLM, SlashNext Generative Human AI, Big Data AI LLM) and commercial LLM copilots: SentinelOne Purple AI (GPT-4-based natural-language threat hunti […]
- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > No new system; the survey contributes (i) an integrated taxonomy of LLM and AI-agent applications across eight SOC tasks (log summarization, alert triage, threat intelligence, ticket handling, incident response, report generation, asset discovery and management, vulnerability management), in which AI agents orchestrate data collection, tool use, memory, and planning while LLMs (GPT-3.5/4/4o, LLaMA, Claude, Gemini, Mi […]
- **P110 — DevAIOps: A Systematic Literature Review on Integrating Explainable AI Agents into CI/CD Pipelines for Optimization, Security, and Auto-Remediation**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > As an SLR, the paper's contribution is conceptual, not a system: a reproducible review over 217 unique records, a thematic taxonomy over five dimensions (T1 AIOps, T2 AI-driven CI/CD optimization, T3 DevSecOps, T4 XAI in software operations, T5 LLM agents for autonomous software operations), a four-gap analysis, and a research agenda (§1, p. 345; §2.1, p. 346). It motivates a reference DevAIOps architecture (Fig. […]
- **P112 — Large language models for agentic NetOps and AIOps: Architectures, evaluation, and safety**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > Not a new system but a contract-centred taxonomy that treats agentic NetOps/AIOps as constrained operational control (SS I.D, p. 6; Table I, p. 7). Autonomy is modelled as a ladder of four rungs - read-only copilot, tool-grounded analyst, write-limited planner-executor, and closed-loop self-healing controller (Fig. 5, p. […]
- **P121 — Large Language Models for Security Operations Centers: A Comprehensive Survey**
  — _campo da ficha: Proposed Solution / Agentic AI Role_
  > A SECONDARY STUDY — no new system is built. The survey contributes (i) a foundational overview of SOC operations, analyst Tiers 1-4 and challenges (§2.2, pp. 3-4; Figure 2, p. 4); (ii) a dual-framework structured analysis mapping LLM applications across the SOC Detection/Analysis/Response phases to the NIST CSF functions, with MITRE ATT&CK as a granular lens for detection capabilities (§2.3, p. 4; Table 1, p. 5); […]

**Texto do artigo:**

> The 65-study corpus comprises the 19 foundational studies, 14 cycle-1,
> 20 cycle-2, and 12 cycle-3 inclusions; ten of these are secondary
> ``foundational-conditional'' studies
> [P24,P33,P52,P54,P72,P77,P79,P110,P112,P121] that migrate to
> background material if the protocol is restricted to primary studies
> (primary corpus: 55). Under the ratified percentile scale, three
> inclusions in the whole corpus (one Q4 series and two unindexed venues,
> all from cycle 3) carry the mandatory venue caveat; the other 62 sit at
> Q1–Q3 (53 Q1, 8 Q2, 1 Q3).

---

## Parágrafo #9 — Corpus overview and taxonomy

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P01 — Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable as quantitative evidence: the paper reports no MTTD, MTTR, alert-fatigue, or resolution-time measurements. Qualitative mentions only: ReliaQuest's agentic AI for threat detection and incident response "has improved detection speed and reduced human workload" (Sec. 7.1, pp. 27-28); […]
- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable (conceptual review; no MTTD/MTTR measurements or baselines reported). Qualitative claims relevant to incident response: in an enterprise cybersecurity incident response example, the agentic model "enhances decision latency, reduces false positives, and supports proactive threat containment" versus rule-based systems (Sec. 4.0.2, p. 16); […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no MTTD, MTTR, alert-fatigue, or incident-resolution measurements are reported. Only qualitative adjacent claims: a hospital Agentic AI case study "improves the time taken to respond to various health issues" (Sec. VI.B, p. 18922); customer-service agents "enhancing response time and client satisfaction" (Sec. V.B, p. 18919); […]
- **P15 — The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable (review paper; MTTD/MTTR are never measured or named). Related qualitative content: agentic AI for "real-time incident detection, prediction, and resolution" in autonomous IT operations and SOC automation (Table 5, Sec. 3.4, p. 23); alert-based inputs trigger autonomous "Tier 1 and Tier 2 Incident response actions" (Sec. 3.5.11, p. 32); […]
- **P17 — A Review of Trustworthy and Explainable Artificial Intelligence (XAI)**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable; the paper reports no MTTD, MTTR, alert-fatigue, or incident-resolution-time metrics of any kind (entire paper; Secs. I-VII, pp. 78994-79011)
- **P21 — Small Language Model Agent for the Operations of Continuously Updating ICT Systems**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, alert fatigue, or resolution time metrics are reported; the paper qualitatively states autonomous operation "has the potential to reduce the time and burden of human endeavors" (Abstract, p. 37522) and that the SLM agent is expected to "mitigate the time-intensive endeavors of system operators" (Sec. VI, p. 37532).
- **P22 — ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not reported by name, but detection/identification and resolution-time results are given: the agent "identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully" (Abstract, p. 1); the GPT-5 agent "restores SLA metrics in roughly 80% of fault injection runs" with correct identification "in about 78% of cases" (Sec. VII, p. 9). […]
- **P27 — Leveraging multi-agent framework for root cause analysis**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, alert-fatigue, or resolution-time measurements are reported; qualitative statements only: "the Report Agent reduces manual report generation time" (Report Agent, p. 7), and the authors acknowledge data collection/validation "introduce additional latency compared to direct inference methods" in time-sensitive scenarios (Conclusions, p. 12)
- **P28 — A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not measured by name (Not specified as formal metrics); adjacent incident-handling results: analyst triage time "decreased by 38.5% on average due to clear, contextual explanations"; false positive alerts reduced by 41.3% versus a traditional SIEM baseline (alert-fatigue proxy); analyst confidence averaged 4.6 on a 5-point scale; […]
- **P31 — LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD, MTTR, alert fatigue, and resolution time are not measured; the paper reports detection quality instead: best F1 = 88.78% (P = 92.16%, R = 85.63%) on customer service platform vs. baselines, with average inference latency of 3156 ms (highest of all methods; PCA 165 ms, LogGPT 1782 ms); […]
- **P35 — Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > No quantitative MTTD/MTTR results reported. MTTR is cited qualitatively as motivation: the human-centric process is "labor-intensive and time-consuming, often leading to prolonged Mean Time To Repair (MTTR)" (Sec. 4.2, p. 10). Related time indicators: average end-to-end diagnosis latency of 21.4 s per fault (3.3 s AFG build + 18.1 s reasoning) and cost of approximately $0.15 per fault at GPT-4 Turbo pricing (Sec. […]
- **P54 — From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — theoretical survey of LLM/agent benchmarks, frameworks, and protocols; incident response, MTTD, MTTR, and alert fatigue are not addressed, and reported quantitative results concern benchmark performance only (Sec. III, pp. 84242–84250).
- **P62 — A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no MTTD, MTTR, or incident-resolution metrics are reported; closest adjacent evidence is cited work on alarm attention: motor-cue pop-up videos "drastically reduced reaction time to alerts during complex situations" and inattentional deafness explains failure to detect auditory alarms (Sec. Adaptation of the User Interface, p. 7; Sec. Understanding Performance Related Mental States, p. 7)
- **P63 — The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — HCI scale-design and pilot study; no MTTD, MTTR, alert fatigue, or incident resolution time metrics are reported anywhere in the paper (results report only psychometric properties, Sec. 5.2, pp. 108-109)
- **P69 — WAUC: A Multi-Modal Database for Mental Workload Assessment Under Physical Activity**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no incident-response, MTTD, MTTR, or alert-fatigue metrics are reported; the quantitative results are mental workload classification AUCs (e.g., EEG mixed-subjects AUC 0.945 ± 0.004 under high physical activity; multi-modal fusion cross-subject AUC up to 0.998 ± 0.001; leave-one-subject-out near chance, e.g., 0.500 ± 0.049 for EEG all conditions) (Sec. 5.2-5.4, pp. 9-12)
- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD: Not specified. MTTR (defined here as Mean Time to Remediate) measured across three remediation activities: analysis "approximately 1 min and 30 s on average", update command execution "around 1 min", compilation "approximately 1 min and 30 s"; […]
- **P78 — Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD/MTTR are not measured; only a qualitative claim that GenDFIR leverages the LLM's contextual understanding to "accelerate and improve incident analysis, minimising reliance on manual intervention" (Sec. 3.4, p. 17); motivation cites investigators spending an average of 45 h per case on digital evidence examination (Sec. 1, p. 2); […]
- **P81 — Enhancing Control Room Operator Decision Making**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable for MTTD/MTTR as such (industrial control-room study, not IT incident response); analogous time-to-detect/act metrics improved with the DSS: mean reaction time S1 106.96 (G2) vs 276.30 (G1), S2 63.43 vs 266.91, S3 117.38 vs 190.17; mean response time S1 259.04 vs 339.30, S2 154.83 vs 361.48, S3 680.00 vs 787.87 (units not stated in Table 5); […]
- **P83 — Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, response-time, or latency measurements are reported; benefits to incident response speed are qualitative only (LLMs in SOC workflows can "mitigate analyst fatigue", reduce cognitive load, and accelerate decision-making) (Sec. 2.2, p. 4; Sec. 2.8, p. 10); […]
- **P87 — An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD, MTTR, alert fatigue, and resolution-time metrics are not reported; as efficiency proxies, end-to-end inference from traffic ingestion to final report takes 2.9-11.6 s per malicious sample, pre-detection alone rendered 0.3 s latency, and the summary agent is framed as "reducing cognitive load and moving a step towards explainable and actionable network defense" (Sec. 4.4, p. 28; Sec. 4.5, p. 28; […]
- **P91 — Autonomous Agentic AI Architectures for Optimizing Security Operations Centers (SOC) KPIS: Methodology, Impact on Detection, Response, and Recovery**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper executes no empirical comparison against a concrete baseline (no before/after measurement and no non-agentic control), so no MTTD/MTTR reduction can be attributed. The abstract's claim of "reduced detection and response times" (Abstract, p. 479) is supported only by (a) internal model-quality metrics — TTR regressor MAE 18%, MSE 1000, R² 0.85; […]
- **P93 — From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Central metrics, empirically compared against a concrete baseline (the traditional analyst-centric SOC workflow) — but both arms run on synthetic/simulated 90-day telemetry, not production data, so gains are comparative-in-simulation (§3, p. 8). Headline results: MTTD fell from 6-12 h (traditional) to 30-90 min (agentic) and MTTR from 12-24 h to 2-6 h, reported as 75% and 80% improvements (§4, p. 13; Table 3, p. […]
- **P94 — Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper does not measure MTTD or MTTR and performs no empirical time-to-detect/time-to-respond comparison against a baseline; its motivation invokes triage delay and alert fatigue only qualitatively (§1, p. 2). […]
- **P97 — Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Conceptual Framework**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not demonstrated empirically — no real-world comparison against a concrete deployed baseline is executed; all response-time figures are outputs of a seeded discrete-event simulation under declared synthetic assumptions, which the authors frame as "internal feasibility rather than production efficacy" (Abstract, p. 1; §6, p. 22; §6.7, p. 29). […]
- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P110 — DevAIOps: A Systematic Literature Review on Integrating Explainable AI Agents into CI/CD Pipelines for Optimization, Security, and Auto-Remediation**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only — the review runs no experiment of its own and states that all quantitative figures (such as MTTR decreases) are reported as stated by the original researchers (§5 Conclusion validity, p. 351). MTTR numbers aggregated from reviewed primaries: Zhang et al. […]
- **P112 — Large language models for agentic NetOps and AIOps: Architectures, evaluation, and safety**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only - this survey executes no empirical comparison of its own and reports no primary MTTD/MTTR reductions. It treats detection and recovery times as the operational objective ('organizations aim to minimise detection and recovery times', SS I, p. 2; improving 'diagnostic and mitigation times' as the measurable goal, SS I.A(d), p. […]
- **P119 — Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper measures no detection or response times and executes no empirical comparison against a concrete baseline (human analysts or an alternative system), so no comparative MTTD/MTTR benefit can be asserted (Art. I). The Abstract's claims of 'alleviating analyst workload and reducing response latency' (p. 1) are motivational, not measured. […]
- **P121 — Large Language Models for Security Operations Centers: A Comprehensive Survey**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only — the survey runs no empirical comparison of its own and reports no MTTD/MTTR measurements; all figures below are relayed from referenced primary studies. (1) Nissist [272] (LLM multi-agent incident mitigation at enterprise cloud scale): time-to-mitigate reduction of 98.93% for simple incidents and 94.85% for hard ones versus manual mitigation, with 77.19% / 52.63% full-automation success rate […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> Table (ref.) organizes the 65 included studies by agentic
> paradigm. Four observations structure the corpus. First, the
> foundational layer is dominated by definitional surveys
> [P09,P10,P15,P54] and governance/trust reviews [P01,P17];
> these answer RQ1/RQ4/RQ5 strongly but contribute no empirical benefit
> evidence. Second, the first empirical core is concentrated in
> cycle 1: multi-agent LLM systems for RCA and SOC [P27,P28,P31,P35],
> closed-loop remediation [P22], and a small-language-model agent for
> ICT operations [P21] — the methodological high-water marks of the
> first two cycles (QA 3.5–4.0 of 4.0). Third, cycle 2 adds the
> copilot pattern proper — RAG-based security copilots
> [P78,P83,P87] and SOC hyper-automation [P76] — plus a
> human-factors cluster absent from earlier cycles
> [P62,P63,P69,P81]. Fourth, cycle 3 adds a time-instrumented
> cluster: supervisor- and multi-agent LLM frameworks for cloud incident
> response and SRE that, for the first time in the corpus, measure nominal
> time metrics against executed baselines [P100,P101,P102,P123],
> alongside an MCP-based security framework for agent pipelines
> [P94], agentic SOC evaluation and SOC-as-a-service frameworks
> [P93,P97], a consultative RAG responder [P119], a non-LLM
> rules-plus-ML agent architecture [P91], and three agentic-centered
> surveys [P110,P112,P121] — with [P91,P101,P102] under the
> venue caveat (bottom-quartile or unindexed venues).

---

## Parágrafo #10 — Evidence on MTTD and MTTR

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD: Not specified. MTTR (defined here as Mean Time to Remediate) measured across three remediation activities: analysis "approximately 1 min and 30 s on average", update command execution "around 1 min", compilation "approximately 1 min and 30 s"; […]
- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only (survey reports results of cited primary studies; no own measurements): CyberAlly's AI-driven triage "halved false positives from 70% to 35% and reduced Mean Time To Respond (MTTR) from 8 h to 90 min", with automated ticketing rising from 10% to 75% (Sec. 3.2, p. 6); alert-fatigue baseline: SOCs process over 10,000 daily alerts, more than half false positives (Sec. 3.2, p. 5); […]

**Texto do artigo:**

> This is the review's central result, and the one the third cycle
> materially changes. Through the first two cycles (89 candidates
> screened, 61 assessed in full text), no study measured MTTD or
> MTTR nominally against its own executed baseline: the single nominal
> MTTR datapoint — the SOC hyper-automation agent of [P76],
> ≈1–1.5 min per phase in a proof of concept compared against
> literature values for a commercial copilot (≈30–45 s)
> — had no baseline of its own and was unfavorable to the proposed
> agent, while secondary sources relayed dramatic but unreproduced gains
> (MTTR from 8 hours to 90 minutes; 98% auto-triage with sub-5-minute
> containment; a 277-day industry detect-and-contain
> baseline) [P79].

---

## Parágrafo #11 — Evidence on MTTD and MTTR

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> - Production, human baseline. The agentic SRE copilot
> of [P100] (five LLM agents over a knowledge graph, with a
> guarded action layer) reports production p90 MTTD falling from
> 30 to 5 minutes (-83%) and p90 MTTR from 240 to 20 minutes
> (-91%; ≈-63% in the paper's aggregate figure)
> against experienced human SREs with dashboards and runbooks,
> at a reported LLM cost of 0.079 per incident.
>
> - Testbed, ablated baselines. The event-driven SOC
> with a supervisor agent of [P101] reports MTTR of 71.7 s
> vs. 258.4 s for a polling baseline (-72.3%) and 190.4 s for
> an LLM-assist (advisory-only) ablation (-62.3%), over 1,247
> synthetic events drawn from MITRE ATT&CK scenarios. The multi-agent SRE framework
> of [P102] reports MTTD of 8.5 vs. 47.2 minutes (-82%)
> against a consensus baseline of three senior SREs — MTTR
> itself is not measured.
>
> - Public dataset, internal baseline. The adaptive
> counterfactual-validation framework of [P123] reports mean
> time-to-containment of 8.9 vs. 14.3 minutes (-37.8%,
> Wilcoxon p<0.001$) against a SOAR baseline executed by the
> authors on the same 143 DARPA OpTC alerts; its external
> baselines are literature-derived and explicitly indicative only.

---

## Parágrafo #12 — Evidence on MTTD and MTTR

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P73 — Breaking Alert Fatigue: AI-Assisted SIEM Framework for Effective Incident Response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD/MTTR not measured; alert-fatigue results: IWSVM achieved best filtering on NSOC2017 with Recall 99.643%, Precision 99.687%, FPR 0.001%, F1 99.665% (Table 3, p. 20); on NSOC2022 under ROV, F1 over 99.3% in all settings (Table 5, p. 21); […]
- **P81 — Enhancing Control Room Operator Decision Making**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable for MTTD/MTTR as such (industrial control-room study, not IT incident response); analogous time-to-detect/act metrics improved with the DSS: mean reaction time S1 106.96 (G2) vs 276.30 (G1), S2 63.43 vs 266.91, S3 117.38 vs 190.17; mean response time S1 259.04 vs 339.30, S2 154.83 vs 361.48, S3 680.00 vs 787.87 (units not stated in Table 5); […]
- **P83 — Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, response-time, or latency measurements are reported; benefits to incident response speed are qualitative only (LLMs in SOC workflows can "mitigate analyst fatigue", reduce cognitive load, and accelerate decision-making) (Sec. 2.2, p. 4; Sec. 2.8, p. 10); […]
- **P87 — An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD, MTTR, alert fatigue, and resolution-time metrics are not reported; as efficiency proxies, end-to-end inference from traffic ingestion to final report takes 2.9-11.6 s per malicious sample, pre-detection alone rendered 0.3 s latency, and the summary agent is framed as "reducing cognitive load and moving a step towards explainable and actionable network defense" (Sec. 4.4, p. 28; Sec. 4.5, p. 28; […]
- **P93 — From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Central metrics, empirically compared against a concrete baseline (the traditional analyst-centric SOC workflow) — but both arms run on synthetic/simulated 90-day telemetry, not production data, so gains are comparative-in-simulation (§3, p. 8). Headline results: MTTD fell from 6-12 h (traditional) to 30-90 min (agentic) and MTTR from 12-24 h to 2-6 h, reported as 75% and 80% improvements (§4, p. 13; Table 3, p. […]
- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P119 — Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper measures no detection or response times and executes no empirical comparison against a concrete baseline (human analysts or an alternative system), so no comparative MTTD/MTTR benefit can be asserted (Art. I). The Abstract's claims of 'alleviating analyst workload and reducing response latency' (p. 1) are motivational, not measured. […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> Three qualifications bound this cluster, and they are the reason the
> review's conclusion changes in degree rather than in kind. First,
> venue tier: under the review's percentile criterion,
> [P123] (a Q2 journal) and [P100] (a Q3 proceedings series)
> are eligible outright, while [P101] (a bottom-quartile series) and
> [P102] (a journal not indexed in Scopus) sit below the Q1–Q3 bar
> and carry the mandatory venue caveat — so half of the cluster, and in
> particular all of its testbed MTTR evidence, remains below the
> bar, and none of it yet appears in a top-quartile venue. Second,
> setting: only [P100] is a production deployment, and it is
> a single, author-affiliated one; [P101,P102] are testbeds and
> [P93] (which reports MTTD/MTTR reductions of 44–80% for an
> agentic SOC against a traditional-SOC arm) runs both arms on synthetic
> telemetry with internally inconsistent tables, recorded in its
> assessment. Third, independence: the three evaluators unanimously
> included all four studies, with the applicable caveats attached. Outside this cluster, proxies still dominate: a
> 74–84% alert-volume reduction in a national SOC [P73], operator
> reaction time falling from ≈276 s to ≈107 s with
> decision support [P81], report latency of
> 2.9–11.6 s [P87], and answer quality without
> timing [P83,P119]; detection studies report accuracy/F1/AUC only.

---

## Parágrafo #13 — Cognitive load: the complementary outcome

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P05 — A Survey of AIOps in the Era of Large Language Models**
  — _campo da ficha: Limitations / Future Work_
  > Four open challenges: (1) time-efficiency and cost-effectiveness of LLM-based AIOps (inference cost may make small models + OCEs preferable); (2) deeper use of diverse failure data — "no current work has effectively incorporated traces data" and incident-report-driven RCA "disrupts the automation flow of AIOps"; (3) generalizability and model adaptability under software evolution lack empirical validation; […]
- **P16 — A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge relevant manuscripts may have been missed by the automated process, and gray literature was excluded (Sec. 3.2, p. 9); geographical skew (~51% Europe, none from South America/Africa) plausibly due to query alignment (Sec. 3.3, p. 9); AIOps manuscripts are scarce/underrepresented, so challenges cannot yet be distinguished from MLOps ones — future AIOps literature should enable this; […]
- **P62 — A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance**
  — _campo da ficha: Limitations / Future Work_
  > Authors state the framework "remains at the conceptual level and minimizes connections to the complexity of brain functioning"; most neuroadaptive studies are limited to human-machine dyads; long-term efficiency and side effects of tDCS and light exposure require investigation; […]
- **P63 — The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents**
  — _campo da ficha: Limitations / Future Work_
  > BUS-15 "requires further testing and validation" and "currently cannot be used as an off-the-shelf product for user research and usability tests"; participants were mainly young (below 35 years old) and people with disabilities were not included (attribute 'Meets neurodiverse needs' postponed); further validation is needed with a larger number of chatbots and a more diverse range of participants; […]
- **P69 — WAUC: A Multi-Modal Database for Mental Workload Assessment Under Physical Activity**
  — _campo da ficha: Limitations / Future Work_
  > Achieving state-of-the-art MW prediction was explicitly not a priority ("achieving state-of-the-art MW level prediction performance is not a priority"); leave-one-subject-out classifiers performed poorly, showing features "are not robust to cross-subject variability"; artifact-removal literature is scarce for physiological signals under high physical workload; […]
- **P73 — Breaking Alert Fatigue: AI-Assisted SIEM Framework for Effective Incident Response**
  — _campo da ficha: Limitations / Future Work_
  > Scope limited to eliminating redundant/irrelevant alerts; results biased by the specific SOC's escalation set, security policy, and analyst condition (including alert fatigue during labeling); eliminating all false positives risks increased false negatives (recommend recall threshold such as 99%); emerging threats and adversarial attacks can cause false negatives; […]
- **P81 — Enhancing Control Room Operator Decision Making**
  — _campo da ficha: Limitations / Future Work_
  > Scalability: constructing a DID covering the entire process from physical equations is challenging and time-intensive, forcing focus on parts of the plant or more generic models/recommendations; participants were mostly chemical-engineering students who "lack real-world experience as control room operators"; physiological data analyzed raw, without accounting for individual differences; […]
- **P119 — Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence**
  — _campo da ficha: Limitations / Future Work_
  > Acknowledged limitations: low Context Relevance on real-world alerts caused by false positives, IOCs not recognized in VirusTotal and CTI reports lacking detail on specific campaigns (§III.C.1, p. 5; §III.C.3, p. 6) — in those cases the system generates coherent output not grounded in retrieved context (§III.C.3, p. 6). […]

**Texto do artigo:**

> The second gap concerns an outcome this review treats as complementary
> rather than incidental: operator cognitive load. The motivating
> observation was already present in the foundational review — the
> explosion of observability data (metrics, logs, traces) has raised the
> cognitive load of operations teams faster than tooling has relieved
> it [P05,P16] — yet, within IT incident response, no corpus
> study measures cognitive load directly; alert fatigue appears only as
> an alert-volume proxy [P73]. Direct measurement does exist in
> adjacent domains, and cycle 2 deliberately retained this human-factors
> cluster (under a dated protocol amendment):
> neuroergonomic foundations of mental workload and
> engagement [P62]; a multimodal workload database with
> classification AUC up to 0.998 and NASA-TLX ground truth [P69];
> and a human experiment in which an AI decision-support system improved
> control-room operator performance [P81]. The corpus also offers a
> validated usability instrument for conversational agents
> (BUS-15) [P63]. Cycle 3 does not change this picture: its
> time-instrumented cluster measures system latencies, not operator state,
> and its one human-facing evaluation scores answer quality with
> LLM-as-judge rubrics rather than workload [P119].

---

## Parágrafo #14 — Cross-citation structure of the corpus

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P06 — Agentic AI: A Comprehensive Survey of Technologies, Applications, and Societal Implications**
  — _campo da ficha: Limitations / Future Work_
  > Open problems listed by the author: transparent/causal agentic AI, neuro-symbolic hybrid agents, multi-agent cooperation and negotiation, human-AI collaboration adapting to feedback and emotion, energy-efficient architectures, Sim2Real transfer, quantum computing for scalability, and robustness against adversarial attacks; […]
- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge field-wide limitations: overreliance on hallucination-prone LLMs lacking causal reasoning; non-standardized orchestration protocols hindering interoperability and reproducibility; and that "many benchmark evaluations for agentic systems rely on artificial environments" while frameworks emphasize "architectural novelty over rigorous empirical validation" (Sec. 5.1, p. 22). […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: Limitations / Future Work_
  > Authors identify open challenges: goal alignment with human values (IRL/CIRL), environmental/situational adaptability, resource constraints, scalability, accountability, bias/fairness/transparency, privacy/security, and evolving regulation (Sec. VII, pp. 18924-18925; Sec. VIII, pp. 18925-18926). […]
- **P14 — Transforming cybersecurity with agentic AI to combat emerging cyber threats (Kshetri)**
  — _campo da ficha: Limitations / Future Work_
  > No explicit limitations section; paper flags itself as a non-peer-reviewed preprint; future research proposed: evolution of autonomous AI agents in cybercrime organizations, whether attacker-defender asymmetry shifts with agentic AI, and applying principal-agency theory to how criminals manage AI agents; notes criminal use of autonomous agents is still hindered by unreliability (Sec. 6, Future research, pp. 24-26)
- **P16 — A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge relevant manuscripts may have been missed by the automated process, and gray literature was excluded (Sec. 3.2, p. 9); geographical skew (~51% Europe, none from South America/Africa) plausibly due to query alignment (Sec. 3.3, p. 9); AIOps manuscripts are scarce/underrepresented, so challenges cannot yet be distinguished from MLOps ones — future AIOps literature should enable this; […]
- **P20 — LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in IaC**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: dependency on an up-to-date knowledge base (outdated entries cause false positives/missed issues); poor handling of conditional logic and specialized templates; small 10-template evaluation with manual annotation. […]
- **P28 — A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: reliance on third-party tools/APIs (Nmap, Groq) can "cause latency issues" and become single points of failure; LLM explanation generation adds computational cost and potential unpredictability across prompt construction or model updates; legacy datasets (SpamAssassin, CIC-IDS 2017) limit evaluation against emerging threats. […]
- **P39 — Agentic AI and the Cyber Arms Race**
  — _campo da ficha: Limitations / Future Work_
  > No formal limitations section (magazine column); authors note a single agent capable of replacing a skilled human "is likely still be a decade or more away" (p. 83); state that "Countering adversarial AI and guaranteeing agent robustness will be essential to the future of agentic AI in cyber" (p. 83); […]
- **P65 — Deep learning for anomaly detection in log data: A survey**: sem ficha (estudo excluído); fonte: rede de citações cruzadas.
- **P73 — Breaking Alert Fatigue: AI-Assisted SIEM Framework for Effective Incident Response**
  — _campo da ficha: Limitations / Future Work_
  > Scope limited to eliminating redundant/irrelevant alerts; results biased by the specific SOC's escalation set, security policy, and analyst condition (including alert fatigue during labeling); eliminating all false positives risks increased false negatives (recommend recall threshold such as 99%); emerging threats and adversarial attacks can cause false negatives; […]
- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: risk of misclassification/false positives requiring human validation; effectiveness depends on quality/completeness of training data; interpretability and trust of AI-generated recommendations; integration with third-party tools; limited direct access to agentless devices such as OT systems; constraints of WebSocket-based active responses; […]
- **P78 — Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: novelty of applying LLMs to timeline analysis (few guidelines/benchmarks); synthetic, simplified scenarios excluding anti-forensics techniques; data volume/heterogeneity and scalability challenges (token limits, hardware); privacy and data-security constraints (GDPR, NIS2); evaluation methods still manual and deemed insufficient by the authors; […]
- **P79 — AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation**
  — _campo da ficha: Limitations / Future Work_
  > Five stated threats to validity: selection bias (post-2022, English-only filtering), ecological validity (most studies use simulated/benchmarked environments, so metrics may not extrapolate to operational SOCs), measurement inconsistency (heterogeneous metrics and datasets hinder cross-comparison), evolving baselines (findings are a snapshot prone to obsolescence), and human-AI integration uncertainty (few empirical  […]
- **P83 — Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot**
  — _campo da ficha: Limitations / Future Work_
  > Both models "demonstrate room for improvement" where alignment with ground truth proved challenging: Pixtral's performance plateaued in certain scenarios and OpenAI showed inconsistency balancing precision and recall; […]
- **P93 — From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge external-validity constraints of synthetic telemetry: it cannot reproduce the ambiguity of novel attacks requiring human intuition, and the simulation omits organisational factors such as team dynamics and communication overhead (§3, p. 8). […]
- **P97 — Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Conceptual Framework**
  — _campo da ficha: Limitations / Future Work_
  > Review limitations: intermediate counts of the 23-study legacy phase were not preserved; 55 of 65 Scopus reports could not be retrieved (possible underrepresentation of subscription-only research); Web of Science was not searched; six legacy sources (18.2% of corpus) remain preprints; no quantitative meta-analysis was possible (§7, pp. 29-30; §3.2, p. 4). […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge five limitations (§V.D, pp. 4-5): (1) the single-agent architecture may hit throughput constraints above 10,000 events/minute — to be addressed by hierarchical multi-agent coordination; (2) the RAG knowledge base requires periodic updates — future automated threat-intelligence ingestion pipelines; […]
- **P112 — Large language models for agentic NetOps and AIOps: Architectures, evaluation, and safety**
  — _campo da ficha: Limitations / Future Work_
  > Stated method limits: many operational agent systems are deployed inside companies and described only through engineering reports or not at all, and the LLM-agent literature is changing quickly, so the authors separate stable claims from current observations (SS I.C, p. 5); raw search hit counts are not reported (p. 5); […]
- **P121 — Large Language Models for Security Operations Centers: A Comprehensive Survey**
  — _campo da ficha: Limitations / Future Work_
  > Challenges catalogued for LLMs in SOCs (§8.1, pp. 25-26): resource intensity and financial barriers; hallucination and bias (fabricated threat indicators, false-positive escalations); black-box opacity and catastrophic forgetting; attack-surface expansion (prompt injection, data poisoning, model inversion); a data trilemma (availability, relevance/concept drift, text-vs-nonlinguistic structure mismatch); […]

**Texto do artigo:**

> Internal citation analysis over the full corpus (through cycle 2:
> triple-checked across OpenAlex referenced_works, Crossref
> reference lists, and Scopus REF() by title; cycle-3 additions:
> union of a full-text reference scan of each included PDF and
> OpenAlex-deposited references; 65 citing edges in total) shows a
> coherent field rather than a disconnected collection of papers. The hubs are the definitional
> surveys — [P10] and [P14] (7 internal citations each),
> [P09] (6) — followed by the AIOps/MLOps and log-anomaly surveys
> [P16,P65] and the SOC hyper-automation study [P76] (3 each).
> The most connected citers are the multi-agent SOC system of [P28]
> (7 outgoing edges, five of them to cycle-2 candidates) and the cycle-3
> SOC-as-a-service framework of [P97] (7 outgoing edges, all into
> earlier cycles or intra-cycle), and each cycle's studies cite back into
> the corpus ([P79]→[P20,P78];
> [P76]→[P39,P83];
> [P93]→[P06,P76]), indicating that the cycles
> sample one evolving conversation. Source-specific quirks are material
> to reproducibility: Scopus resolves references by title, not
> DOI; one open-access venue is not indexed there at all; and preprint
> DOIs can split citation identity across sources (handled here by alias
> resolution). Fig. (ref.) renders the full network. The
> cycle-3 inclusions add 13 edges and deepen the pattern: the
> SOC-as-a-service framework [P97] cites seven corpus studies —
> among them [P14,P73,P76,P79] and the intra-cycle survey [P121]
> — tying the multi-agent SOC system [P28] as the most connected
> citer; the agentic-SOC evaluation [P93] cites [P06,P76]; and
> the cycle-3 surveys cite both the definitional layer and cycle-2 studies
> [P101,P112,P121]. Two consequences for the hub structure: the SOC
> hyper-automation study [P76], cited by [P28,P93,P97], becomes
> a hub, and [P14] rises to 7 internal citations, level with
> [P10].

---

## Parágrafo #15 — What the evidence supports — and what it does not

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P01 — Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable as quantitative evidence: the paper reports no MTTD, MTTR, alert-fatigue, or resolution-time measurements. Qualitative mentions only: ReliaQuest's agentic AI for threat detection and incident response "has improved detection speed and reduced human workload" (Sec. 7.1, pp. 27-28); […]
- **P09 — AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable (conceptual review; no MTTD/MTTR measurements or baselines reported). Qualitative claims relevant to incident response: in an enterprise cybersecurity incident response example, the agentic model "enhances decision latency, reduces false positives, and supports proactive threat containment" versus rule-based systems (Sec. 4.0.2, p. 16); […]
- **P10 — Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no MTTD, MTTR, alert-fatigue, or incident-resolution measurements are reported. Only qualitative adjacent claims: a hospital Agentic AI case study "improves the time taken to respond to various health issues" (Sec. VI.B, p. 18922); customer-service agents "enhancing response time and client satisfaction" (Sec. V.B, p. 18919); […]
- **P12 — Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — the survey reports no MTTD, MTTR, alert fatigue, or incident-resolution-time metrics; closest analogues are qualitative/indirect: BERTery detects battery behavior changes indicating "an imminent failure up to 24 hours in advance" (Sec. IV-A.5, p. 10); FPGA porting of fault-detection algorithms gave "a fortyfold increase in processing speed and a 50% reduction in power consumption" (Sec. IV-A.5, p. […]
- **P14 — Transforming cybersecurity with agentic AI to combat emerging cyber threats (Kshetri)**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD/MTTR not named; vendor-claimed (not independently measured) time metrics: ReliaQuest GreyMatter "processes security alerts 20 times faster", automates 98% of security alerts, "reduces threat containment time to under five minutes", improves detection accuracy by 30%; CrowdStrike Charlotte AI triages detections with over 98% accuracy eliminating more than 40 hours of manual work per week; […]
- **P15 — The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable (review paper; MTTD/MTTR are never measured or named). Related qualitative content: agentic AI for "real-time incident detection, prediction, and resolution" in autonomous IT operations and SOC automation (Table 5, Sec. 3.4, p. 23); alert-based inputs trigger autonomous "Tier 1 and Tier 2 Incident response actions" (Sec. 3.5.11, p. 32); […]
- **P17 — A Review of Trustworthy and Explainable Artificial Intelligence (XAI)**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable; the paper reports no MTTD, MTTR, alert-fatigue, or incident-resolution-time metrics of any kind (entire paper; Secs. I-VII, pp. 78994-79011)
- **P21 — Small Language Model Agent for the Operations of Continuously Updating ICT Systems**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, alert fatigue, or resolution time metrics are reported; the paper qualitatively states autonomous operation "has the potential to reduce the time and burden of human endeavors" (Abstract, p. 37522) and that the SLM agent is expected to "mitigate the time-intensive endeavors of system operators" (Sec. VI, p. 37532).
- **P22 — ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not reported by name, but detection/identification and resolution-time results are given: the agent "identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully" (Abstract, p. 1); the GPT-5 agent "restores SLA metrics in roughly 80% of fault injection runs" with correct identification "in about 78% of cases" (Sec. VII, p. 9). […]
- **P27 — Leveraging multi-agent framework for root cause analysis**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, alert-fatigue, or resolution-time measurements are reported; qualitative statements only: "the Report Agent reduces manual report generation time" (Report Agent, p. 7), and the authors acknowledge data collection/validation "introduce additional latency compared to direct inference methods" in time-sensitive scenarios (Conclusions, p. 12)
- **P28 — A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not measured by name (Not specified as formal metrics); adjacent incident-handling results: analyst triage time "decreased by 38.5% on average due to clear, contextual explanations"; false positive alerts reduced by 41.3% versus a traditional SIEM baseline (alert-fatigue proxy); analyst confidence averaged 4.6 on a 5-point scale; […]
- **P31 — LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD, MTTR, alert fatigue, and resolution time are not measured; the paper reports detection quality instead: best F1 = 88.78% (P = 92.16%, R = 85.63%) on customer service platform vs. baselines, with average inference latency of 3156 ms (highest of all methods; PCA 165 ms, LogGPT 1782 ms); […]
- **P35 — Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > No quantitative MTTD/MTTR results reported. MTTR is cited qualitatively as motivation: the human-centric process is "labor-intensive and time-consuming, often leading to prolonged Mean Time To Repair (MTTR)" (Sec. 4.2, p. 10). Related time indicators: average end-to-end diagnosis latency of 21.4 s per fault (3.3 s AFG build + 18.1 s reasoning) and cost of approximately $0.15 per fault at GPT-4 Turbo pricing (Sec. […]
- **P54 — From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — theoretical survey of LLM/agent benchmarks, frameworks, and protocols; incident response, MTTD, MTTR, and alert fatigue are not addressed, and reported quantitative results concern benchmark performance only (Sec. III, pp. 84242–84250).
- **P94 — Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper does not measure MTTD or MTTR and performs no empirical time-to-detect/time-to-respond comparison against a baseline; its motivation invokes triage delay and alert fatigue only qualitatively (§1, p. 2). […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P112 — Large language models for agentic NetOps and AIOps: Architectures, evaluation, and safety**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Secondary evidence only - this survey executes no empirical comparison of its own and reports no primary MTTD/MTTR reductions. It treats detection and recovery times as the operational objective ('organizations aim to minimise detection and recovery times', SS I, p. 2; improving 'diagnostic and mitigation times' as the measurable goal, SS I.A(d), p. […]

**Texto do artigo:**

> The corpus firmly supports three claims: (i) a consolidated conceptual
> model of Agentic AI for operations (autonomy levels, orchestration,
> guardrails, HITL) [P09,P10,P15,P54,P112]; (ii) technical
> feasibility of agentic RCA, triage, and remediation at prototype level,
> with strong detection-quality results
> [P21,P22,P27,P28,P31,P35,P102]; and (iii) a well-articulated risk
> and governance agenda [P01,P12,P17,P14,P94]. The headline
> operational claim now has its first primary support — the cycle-3
> cluster of Section (ref.) — but that support is early,
> partly below the venue bar, and production-grade in exactly one
> author-affiliated deployment. Reviewers and practitioners should
> still treat vendor-scale numbers (e.g., 8h → 90min MTTR) as
> hypotheses under test: the cycle-3 measurements are the first tests, not
> yet the established effect.

---

## Parágrafo #16 — Why the measurement gap persisted — and where it is closing

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: General Impact on Agentic AI / Multi-Agent Systems_
  > The pilot "successfully processed real-time security alerts and autonomously executed mitigation workflows without human intervention", providing empirical evidence of operational viability of an autonomous agent-based SOAR architecture; workflow condensation from 38 XSOAR steps to ten actions with more granular tool recommendations (Fail2Ban, AIDE, auditd, Google Authenticator MFA); […]

**Texto do artigo:**

> Three causes were visible through cycle 2: production access (most
> studies evaluate on public datasets or testbeds; industrial deployments
> are rare and rarely instrumented for time metrics); benchmark culture
> (detection communities optimize F1/AUC, which do not compose into
> end-to-end time outcomes); and the autonomy–accountability tension
> (studies that deploy agents constrain them to low-risk actions, making
> time gains modest and hard to attribute). That the only pre-cycle-3
> nominal measurement [P76] was unfavorable to the agent
> remains a useful counterweight to publication bias. Cycle 3 adds a
> fourth, sociological observation: the first time-instrumented studies
> are appearing in early-stage venues — regional conference series and
> recently launched journals — ahead of the top-quartile literature. A
> review that dropped every below-bar candidate without the caveat
> mechanism would have seen only half of the cluster; the dated-amendment
> design is what keeps the field's actual turning point visible while
> keeping the evidence grade explicit.

---

## Parágrafo #17 — Research gaps consolidated across the reviews

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P01 — Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment**
  — _campo da ficha: Limitations / Future Work_
  > Authors identify open gaps rather than a study-limitations section: incomplete alignment and meta-reasoning safeguards; hard-to-detect long-term memory corruption; high false negatives against indirect prompt attacks; weak insider governance; lack of holistic cross-layer anomaly correlation (Table 2, p. 19); lack of standardized cross-domain incident reporting; weak operationalization of governance; […]
- **P05 — A Survey of AIOps in the Era of Large Language Models**
  — _campo da ficha: Limitations / Future Work_
  > Four open challenges: (1) time-efficiency and cost-effectiveness of LLM-based AIOps (inference cost may make small models + OCEs preferable); (2) deeper use of diverse failure data — "no current work has effectively incorporated traces data" and incident-report-driven RCA "disrupts the automation flow of AIOps"; (3) generalizability and model adaptability under software evolution lack empirical validation; […]
- **P08 — Applications, Challenges, and Future Directions of Human-in-the-Loop Learning**
  — _campo da ficha: Limitations / Future Work_
  > Challenges acknowledged: human bias/subjectivity/inconsistency, scalability bottlenecks of human input, high cost of experts and training, complexity of managing conflicting expert feedback, data quality, interpretability, online learning, unclear human-machine collaboration models, validation without ground truth, and ethical/legal issues (privacy, bias); […]
- **P12 — Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey**
  — _campo da ficha: Limitations / Future Work_
  > Author-acknowledged challenges: high cost and compute (LLMs restricted to high-end servers; edge cases still require human intervention), model accuracy degradation and hallucinations, privacy risks and data extraction attacks, adversarial vulnerabilities (jailbreak, prompt injection, multimodal and complex-system attacks), and size/scalability limits for edge deployment (Sec. V, pp. 17-18); […]
- **P14 — Transforming cybersecurity with agentic AI to combat emerging cyber threats (Kshetri)**
  — _campo da ficha: Limitations / Future Work_
  > No explicit limitations section; paper flags itself as a non-peer-reviewed preprint; future research proposed: evolution of autonomous AI agents in cybercrime organizations, whether attacker-defender asymmetry shifts with agentic AI, and applying principal-agency theory to how criminals manage AI agents; notes criminal use of autonomous agents is still hindered by unreliability (Sec. 6, Future research, pp. 24-26)
- **P15 — The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges**
  — _campo da ficha: Limitations / Future Work_
  > Challenges identified: architectural/technical limits in dynamic task decomposition and long-term planning; ethical/governance issues ("almost 78% of organizations reported problems with data safety"); performance and tool-integration delays with no standard interfaces; multi-agent coordination and synchronization failures; human-AI interaction transparency gaps; […]
- **P17 — A Review of Trustworthy and Explainable Artificial Intelligence (XAI)**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge: "the replicability of the post-hoc explainability methodologies, the absence of a unified understanding, set of criteria, and set of metrics" for interpretability, the friction between efficiency and predictability, and limitations in explaining deep neural networks; future work is stated only generically as identifying potential relevant studies and open challenges (Sec. VI, p. 79011)
- **P21 — Small Language Model Agent for the Operations of Continuously Updating ICT Systems**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: the agent cannot handle situations not covered by the extended trajectories, and manually or heuristically augmenting thoughts/tags to operational histories is costly; some manuals are free-format with charts/diagrams, making mechanical trajectory generation a challenging problem; verification requires building an interactive environment, which demands extensive system knowledge and development effort. […]
- **P22 — ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control**
  — _campo da ficha: Limitations / Future Work_
  > Acknowledged limitations: "nonnegligible wall-clock remediation times for the largest topology, and a distinct performance gap between model sizes", suggesting zero-touch control currently requires frontier-class models (Sec. VII, p. 9); binary success metric obscures partial recovery, and constrained emulated VMs sometimes make full return to baseline physically impossible (Sec. VI-A, p. 7); […]
- **P32 — GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservices**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: fault injection "does not fully cover the diversity and long-tail characteristics of production incidents"; window-level labels anchored at injection time may miss delayed or cascading effects; recovery plans evaluated offline via action-overlap without live execution, so accuracy reflects action validity not operational success; […]
- **P35 — Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps**
  — _campo da ficha: Limitations / Future Work_
  > Failure rates 8.2%-11.3% per dataset; primary failure mode is ambiguous propagation chains (59% of failures) where simultaneous similar symptoms mislead the Diagnoser; insufficient log semantics (28%) with generic messages like "Error occurred"; in dense topologies (fan-out > 10) backtracking "degrades to near-exhaustive search"; […]
- **P37 — Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response**
  — _campo da ficha: Limitations / Future Work_
  > Binary Yes/No format may reduce "complex practitioner perspectives into oversimplified dichotomies"; possible sampling bias (AI-engaged respondents overrepresented) and purposive/convenience sampling via professional networks, so the 4.97% margin of error should be interpreted with caution; U.S.-only sample limits global generalizability; self-reported perception data carry response bias; […]
- **P53 — Anomaly Detection and Root Cause Analysis in Cloud-Native Environments Using Large Language Models and Bayesian Networks**
  — _campo da ficha: Limitations / Future Work_
  > False positives persist and false negatives are the primary issue (low recall on Mongo IO 0.71 and Queue Disconnect 0.83); perfect Cache Disconnected score may indicate overfitting and needs validation; the LLM neglects numerically significant log values (IPs, response times, status codes), for which LSTM networks are suggested; […]
- **P72 — From Vulnerability to Defense: The Role of Large Language Models in Enhancing Cybersecurity**
  — _campo da ficha: Limitations / Future Work_
  > Limitations of LLMs (not of the review itself): interpretability ("black boxes"), lack of domain-specific knowledge, scalability/computational cost, adversarial attacks, plus ethical issues of bias, privacy, misuse, and accountability (Sec. 5.6-5.7, pp. 41-43); […]
- **P73 — Breaking Alert Fatigue: AI-Assisted SIEM Framework for Effective Incident Response**
  — _campo da ficha: Limitations / Future Work_
  > Scope limited to eliminating redundant/irrelevant alerts; results biased by the specific SOC's escalation set, security policy, and analyst condition (including alert fatigue during labeling); eliminating all false positives risks increased false negatives (recommend recall threshold such as 99%); emerging threats and adversarial attacks can cause false negatives; […]
- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: Limitations / Future Work_
  > Limitations: risk of misclassification/false positives requiring human validation; effectiveness depends on quality/completeness of training data; interpretability and trust of AI-generated recommendations; integration with third-party tools; limited direct access to agentless devices such as OT systems; constraints of WebSocket-based active responses; […]
- **P77 — Generative AI revolution in cybersecurity: a comprehensive review of threat intelligence and operations**
  — _campo da ficha: Limitations / Future Work_
  > Author-acknowledged GAI limitations: wrong/unethical outputs, cost inefficiency, high setup time (weeks to months of training), easy exploitability by malicious actors, weak interpretability/explainability, contextual and long-range-dependency limits, multi-turn conversation failures, data-privacy risks (breaches, inadequate anonymization, bias, lack of consent), lack of user control, and need for empirical evaluatio […]
- **P87 — An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense**
  — _campo da ficha: Limitations / Future Work_
  > End-to-end latency of 2.9-11.6 s may not meet sub-second production IDS requirements (future: response caching, model distillation, asynchronous tool calls); SHAP and RAG contributions not formally ablated; SHAP unsupported for the MLP model (future: Integrated Gradients) and MLP remains weak on UDP Flood (F1: 0.4828); […]
- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Limitations / Future Work_
  > Acknowledged limitations (§VI, pp. 5-6): hypotheses are incomplete or overly narrow for novel failure modes or external dependencies not represented in the knowledge graph, so human expertise remains essential; reliance on observability means missing or misleading telemetry creates blind spots; […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Limitations / Future Work_
  > Authors acknowledge five limitations (§V.D, pp. 4-5): (1) the single-agent architecture may hit throughput constraints above 10,000 events/minute — to be addressed by hierarchical multi-agent coordination; (2) the RAG knowledge base requires periodic updates — future automated threat-intelligence ingestion pipelines; […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Limitations / Future Work_
  > The external baseline comparisons (Liu [10], Babar et al. [23]) are indicative cross-framework estimates computed by the present authors and 'cannot serve as independently replicable evaluations' (§5.4, pp. 22-23); the CVE/ASA ablation attribution is incremental within a fixed sequence, not an interaction-free causal estimate (§5.2, pp. 19-20). […]

**Texto do artigo:**

> The foundational review synthesized six gap axes for agentic IR; the
> three update cycles allow each to be re-examined against newer evidence.
> (i) From recommendation to safe autonomous execution.
> Remediation in LLM4AIOps was found to stop at recommendation and
> triage [P05,P15]; cycles 1–2 confirmed the axis — closed-loop
> execution at prototype level [P22,P32] and at proof-of-concept
> level in SOC hyper-automation [P76] — and cycle 3 moves it
> furthest: guarded production execution with human gates [P100],
> event-driven SOAR tool-calling [P101], and counterfactual
> pre-execution validation with adaptive re-planning [P123].
> Verifiable, auditable execution beyond a single vendor deployment
> remains unreported.
> (ii) Complex telemetry (traces). The difficulty of feeding
> distributed traces to LLMs [P05] persists: cycle-2 primary studies
> operate on logs, alerts, and flows [P53,P73,P87]; trace-native
> agentic RCA remains open.
> (iii) Memory integrity and contradictory knowledge.
> Memory poisoning and conflicting sources were flagged as structural
> risks [P01]; no update-cycle study evaluates agent-memory integrity
> empirically — the axis is untouched.
> (iv) Governance, accountability, and adversarial risk.
> The richest axis in volume: governance frameworks and threat
> taxonomies [P01,P12,P14,P17,P72,P77] and HITL adoption
> factors [P08,P37], yet still without quantitative evaluation of
> governance mechanisms under incident conditions.
> (v) Causal reasoning vs. statistical correlation.
> Agentic RCA advanced with graph- and Bayesian-structured
> approaches [P32,P35,P53], partially addressing the axis, though
> evaluation remains on curated failure sets.
> (vi) Resource efficiency and sustainability.
> The SLM agent of [P21] is still the corpus's only direct response
> (compact models, confidentiality, cost); the axis otherwise remains a
> statement of intent. Axes (i), (iii), and (vi) are therefore the least
> served by three years of literature — a concrete map for future
> primary studies, to which this review adds a seventh axis:
> measured cognitive-load outcomes
> (Section (ref.)).

---

## Parágrafo #18 — Implications for research and practice

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P08 — Applications, Challenges, and Future Directions of Human-in-the-Loop Learning**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no MTTD, MTTR, alert fatigue, or incident resolution time metrics are reported; the closest operational results are from reviewed HITL studies in other domains, e.g., RUN dataset annotation "64% faster compared to fully manual methods" and DaME saving "14,000 hours of manual mapping work over a period of ten months" (Sec. III-D, p. 75746; Sec. III-E, p. 75746)
- **P22 — ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD and MTTR are not reported by name, but detection/identification and resolution-time results are given: the agent "identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully" (Abstract, p. 1); the GPT-5 agent "restores SLA metrics in roughly 80% of fault injection runs" with correct identification "in about 78% of cases" (Sec. VII, p. 9). […]
- **P37 — Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Perception-based only, no measured time values: 92% of respondents affirmed that "automation has significantly reduced the mean time to detect and respond (MTTD/MTTR)" in their organizations vs. 8% No; 95% CI for n=194: [88.2%, 95.8%]; the paper also identifies an "efficiency-capability paradox": despite the 92% MTTD/MTTR result, 70% believe current automation tools cannot keep pace with evolving AI-driven attacks; […]
- **P63 — The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — HCI scale-design and pilot study; no MTTD, MTTR, alert fatigue, or incident resolution time metrics are reported anywhere in the paper (results report only psychometric properties, Sec. 5.2, pp. 108-109)
- **P69 — WAUC: A Multi-Modal Database for Mental Workload Assessment Under Physical Activity**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not applicable — no incident-response, MTTD, MTTR, or alert-fatigue metrics are reported; the quantitative results are mental workload classification AUCs (e.g., EEG mixed-subjects AUC 0.945 ± 0.004 under high physical activity; multi-modal fusion cross-subject AUC up to 0.998 ± 0.001; leave-one-subject-out near chance, e.g., 0.500 ± 0.049 for EEG all conditions) (Sec. 5.2-5.4, pp. 9-12)
- **P76 — Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD: Not specified. MTTR (defined here as Mean Time to Remediate) measured across three remediation activities: analysis "approximately 1 min and 30 s on average", update command execution "around 1 min", compilation "approximately 1 min and 30 s"; […]
- **P83 — Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — no MTTD, MTTR, response-time, or latency measurements are reported; benefits to incident response speed are qualitative only (LLMs in SOC workflows can "mitigate analyst fatigue", reduce cognitive load, and accelerate decision-making) (Sec. 2.2, p. 4; Sec. 2.8, p. 10); […]
- **P87 — An LLM-Based Agentic Network Traffic Incident-Report Approach Towards Explainable-AI Network Defense**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified — MTTD, MTTR, alert fatigue, and resolution-time metrics are not reported; as efficiency proxies, end-to-end inference from traffic ingestion to final report takes 2.9-11.6 s per malicious sample, pre-detection alone rendered 0.3 s latency, and the summary agent is framed as "reducing cognitive load and moving a step towards explainable and actionable network defense" (Sec. 4.4, p. 28; Sec. 4.5, p. 28; […]
- **P94 — Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper does not measure MTTD or MTTR and performs no empirical time-to-detect/time-to-respond comparison against a baseline; its motivation invokes triage delay and alert fatigue only qualitatively (§1, p. 2). […]
- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P119 — Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Not specified quantitatively — the paper measures no detection or response times and executes no empirical comparison against a concrete baseline (human analysts or an alternative system), so no comparative MTTD/MTTR benefit can be asserted (Art. I). The Abstract's claims of 'alleviating analyst workload and reducing response latency' (p. 1) are motivational, not measured. […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> For researchers, the agenda is concrete: replicate the cycle-3 cluster
> at this review's venue-quality bar — field studies that instrument
> MTTD and MTTR nominally, pre/post or A/B against the team's own
> baseline, multi-site rather than single-vendor
> [P100,P101,P102,P123] — and pair time metrics with validated
> human-factors instruments (NASA-TLX [P69], BUS-15 [P63]) to
> test the cognitive-load ``bonus'' that no study has yet measured. For
> practitioners, the corpus supports piloting copilots on triage and
> report drafting (where latency and quality evidence exists
> [P83,P87,P119]) under HITL governance [P08,P37], now with
> early quantitative guidance on attainable time reductions and their
> cost [P100,P101], while treating full-loop autonomous remediation
> as experimental [P22,P76,P123] and securing the agent pipeline
> itself [P94].

---

## Parágrafo #19 — Threats to Validity

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> Selection. Assisted identification (LLM search in cycle 1,
> author-driven discovery in cycle 2, query re-execution in cycle 3) may
> bias candidate coverage; this is mitigated by dual-engine string
> validation (13/14 recall on OpenAlex and Scopus), mandatory snowballing
> (executed in cycle 3 with a negative result), and full audit trails, but
> a database-exhaustive census was not the goal of the update design. Five
> cycle-3 candidates were removed as PRISMA ``reports not retrieved''
> after two documented access attempts — an unavailability exclusion
> whose effect on the synthesis is unknowable by construction.
> Venue criteria. The venue bar is the Scopus CiteScore
> percentile in quartiles (Q1–Q3 eligible), ratified by the review
> conductor for international validity; the first three cycles
> operationalized the same cut through the Brazilian Qualis
> classification with SJR as auxiliary input, and every dated amendment
> that retained below-bar studies is explicit in the audit trail. All
> conclusions hold with the three below-bar inclusions removed, with one
> quantified consequence: the cycle-3 nominal-metric cluster narrows from
> four studies to two ([P100,P123]), losing its testbed MTTR
> evidence — which is precisely why the evidence grade is reported
> alongside the effect sizes, and why the one production deployment is
> flagged as author-affiliated and single-vendor.
> Evaluator validity. All three raters are LLM systems;
> they are independent of each other but share potential model-family
> biases. The unanimity of the core corpus (89%), the protocol-only
> nature of divergences, per-claim evidence anchors in every assessment,
> and a divergence-free third cycle under the ratified rules mitigate —
> but do not eliminate — this threat; the three protocol questions
> exposed by the divergences were adjudicated by the (human) review
> conductor and ratified as rules R1–R3 (Section (ref.)).
> Bibliometric sources. Citation counts are kept per source and
> never summed; source quirks (title-based reference resolution, unindexed
> venues, preprint DOI splits, API service-level limits) are documented in
> the audit trail.

---

## Parágrafo #20 — Conclusion

**Fontes (trechos extraídos dos papers, via fichas de extração):**

- **P100 — AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against a concrete human-SRE baseline (Art. I satisfied). Synthetic fault-injection: MTTR falls 'from a baseline on the order of tens of minutes to single-digit minutes in many cases', with bootstrap CIs for the difference in means excluding zero, RCA explanations reached 'several times faster' than humans, tighter MTTR distributions (less variance), and statistically and practically sig […]
- **P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > Executed empirical comparison against two concrete baselines (satisfies RSL Art. I). MTTD proxy (mean detection latency): 0.85 s for ED-ASOC vs 34.2 s for the polling baseline — a 97.5% reduction — and 33.8 s for LLM-Assist (§IV.C, pp. 3-4; Table IV, p. 4). MTTR: average 71.7 s vs 258.4 s for polling, a 72.3% reduction (§IV.C, p. 3; Table IV, p. 4; §VI, p. […]
- **P102 — Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > MTTD is measured directly as Mean Time to Diagnosis against an executed manual baseline (Art. I satisfied): 47.2 min (manual, 3 senior SREs) reduced to 8.5 min in the primary testbed — the 82% reduction claimed in the abstract and conclusion (Abstract, p. 1; §5.1, p. 14) — and to 11.2 min in the extended 50+ microservice validation, reported as a 79.1% overall reduction across both testbeds (Table 4, p. 10). […]
- **P123 — An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response**
  — _campo da ficha: Impact on MTTD & MTTR Metrics_
  > The paper reports neither MTTD nor MTTR by name: detection is delegated to the Wazuh SIEM (MTTD out of scope), and the time metric is MTTC — mean time to contain, from alert ingestion to full containment, in minutes (Table 7 note, §5.2, p. 18) — a containment-side proxy for MTTR. CIPHER-A reduces MTTC from 14.3 ± 2.1 min (Baseline SOAR) to 8.9 ± 1.4 min, a 37.8% reduction (Table 5, p. 16; Table 7, p. 19; Fig. 6, p. […]

**Texto do artigo:**

> This SLR consolidated 65 studies (2020–2026) on Agentic AI as a copilot
> for incident response across three update cycles, assessed by three
> independent evaluators with high agreement (66 of 74 decisions
> unanimous; the third cycle divergence-free). The field has matured
> conceptually — shared definitions, reference architectures, governance
> agendas, and a coherent citation structure — and demonstrates
> prototype-level feasibility of agentic detection, RCA, and remediation.
> Its motivating claim is now beginning to be measured: a first cluster of
> four primary studies reports nominal MTTD, MTTR, and time-to-containment
> reductions of 38–91% against executed baselines — half of it below
> the review's venue bar, with production evidence from a single
> author-affiliated deployment, and still without any measurement of
> operator cognitive load in the presence of an agentic copilot. The most
> valuable next contribution to this literature is therefore a field
> evaluation that clears the bar the early evidence does not: an agentic
> copilot deployed with operations teams beyond a single vendor,
> instrumented for MTTD/MTTR with its own baseline, paired with validated
> workload instruments, and reported at a venue-quality level that lets
> systematic reviews count it without caveat. That study is the direct
> continuation of this review.

---
