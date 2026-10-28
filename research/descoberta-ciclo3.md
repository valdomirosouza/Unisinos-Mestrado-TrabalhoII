# Descoberta — Ciclo 3 (2026-10-27)

> 🧭 [🏠 README raiz](../README.md) · [🔎 Descoberta](README.md) · [⚖️ Protocolo](../protocolo/constituicao.md) · [🧩 String de busca](../picoc/picoc-search-string.md)

Etapa 1 do ciclo 3 (`WORKFLOW.md`), executada via API com a **string canônica**
derivada do PICOC ([picoc-search-string.md](../picoc/picoc-search-string.md)),
sob a camada Template-RSL (skill `/rsl-descoberta`). Objetivo: capturar o que
foi publicado/indexado **após o fechamento da descoberta do ciclo 2**
(~2026-09-07), mais o estrato de alta precisão do bloco C (Outcomes) em todo o
período.

## Varreduras executadas (2026-10-27)

| Varredura | Base | Query | Filtros | Volume | Coletados |
| --- | --- | --- | --- | --- | --- |
| O (outcome) | OpenAlex `title_and_abstract.search` | A ∩ B ∩ C | 2020+, EN | 207 | 207 (todos) |
| R (recência) | OpenAlex | A ∩ B | 2026-06+, EN, top relevância | 2.552 | 100 |
| R2 (impacto) | OpenAlex | A ∩ B | 2026+, EN, top citações | 5.791 | 100 |
| O | Scopus `TITLE-ABS-KEY` por bloco | A ∩ B ∩ C | 2020+, EN | 177 | 177 (todos) |
| R | Scopus | A ∩ B | PUBYEAR > 2025, top citações + relevância | 7.073 | 100 |

Blocos A/B/C conforme a string canônica; na OpenAlex, termos de palavra única
sem aspas e frases entre aspas, **com variantes plurais explícitas** (a forma
com maior recall testada hoje). Volume A∩B 2020+ hoje: **14.952** na forma
usada (≈49.700 na execução de 2026-07-27 — diferença atribuível à forma da
query e à evolução da base; ver recall abaixo, que é o critério do protocolo).

## Recall de calibração (por DOI, OpenAlex, 2026-10-27)

- **Incluídos dos ciclos 1+2 com DOI (34):** 24/34 recuperados.
- Perdas **esperadas por design** (rota de descoberta dirigida/snowballing,
  não de query): P24 (trade-off "autonomous system*" documentado), cluster de
  fatores humanos P62, P63, P69, P81 (entra só pelo outcome complementar —
  PDR-0005), P73, P77, P82, P88 (ciclo 2, descoberta dirigida).
- **Achado novo:** P21 (recuperado na validação de 2026-07) hoje **não casa o
  bloco B** no abstract indexado da OpenAlex (bisseção: casa A, falha B
  inclusive em "network operations") — mudança de indexação da base. Recall
  nos 14 incluídos do ciclo 1: **12/14** (perde P24 e P21). Mitigação: P21 já
  está no corpus; snowballing permanece obrigatório.

## Funil de deduplicação e triagem de título

| Estágio | n |
| --- | --- |
| Registros brutos coletados (5 varreduras) | 684 |
| Únicos após dedup (DOI/título) vs. P01–P89 e entre bases | 584 |
| Pré-filtro temático de título (sinal A ∧ B, ou varredura O) | 435 |
| Após corte de tipo (E5/I2: fora preprint, dissertação, other) ∧ sinal A∧B no título | 218 |
| **Candidatos admitidos (triagem manual de título)** | **37** (P90–P126) |

Classes de não-admissão na triagem manual (auditáveis em
[`ciclo3-data/`](ciclo3-data/) — dumps brutos das varreduras e da lista pontuada): repositório sem
revisão por pares (Zenodo — falha I2/E5 prima facie), veículos com padrão
editorial frágil, duplicatas internas de título, e fora de domínio no título
(ex.: transporte público, hospitalar). Casos-limite mantidos para a Etapa 2
decidir (ex.: P91, veículo de estrato provavelmente baixo — PDR-0002 exige
ressalva, não exclusão na descoberta).

## Candidatos P90–P126

Citações **por fonte** (Art. V — nunca somar; `NÃO INDEXADO` ≠ 0), snapshot 2026-10-27:

| ID | Título | Ano | Veículo | DOI | Citações (OA · CR · SC) | Varredura | PDF |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P90 | Demonstrating Multi-Agent Collaboration via Agent-to-Agent and Model Context Protocols: An IT I | 2025 | IEEE International Conference on Service-Orie | `10.1109/sose67019.2025.00013` | OA 7 · CR 7 · SC 6 | O | PENDENTE |
| P91 | Autonomous Agentic AI Architectures for Optimizing Security Operations Centers (SOC) KPIS: Meth | 2025 | Revista Academiei Forţelor Terestre | `10.2478/raft-2025-0046` | OA 5 · CR 5 · SC NÃO INDEXADO | O | ✅ |
| P92 | AIRIN: An LLM-Driven Multi-agent Framework for Augmenting Human Expertise in IT Service Inciden | 2026 | Communications in computer and information sc | `10.1007/978-3-032-30836-8_20` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P93 | From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Arc | 2026 | Journal of Information & Knowledge Management | `10.1142/s0219649226500395` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P94 | Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC E | 2026 | Applied Sciences | `10.3390/app16167915` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P95 | AIOps for Reliability: Evaluating Large Language Models for Automated Root Cause Analysis in Ch | 2025 | Lecture notes in computer science | `10.1007/978-3-031-97564-6_25` | OA 4 · CR 5 · SC 7 | O | PENDENTE |
| P96 | AI Agents for Cloud Reliability: Autonomous Threat Detection and Mitigation Aligned with Site R | 2025 | IEEE International Conference on AI in Cybers | `10.1109/icaic63015.2025.10849322` | OA 12 · CR 12 · SC 11 | O | PENDENTE |
| P97 | Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Co | 2026 | Network | `10.3390/network6040084` | OA 0 · CR 0 · SC NÃO INDEXADO | O,R_rel | PENDENTE |
| P98 | GraphRCA-Chorus: Choreographed Multi-Agent Graph Transformers for Root Cause Analysis in Micros | 2026 | Proceedings of 2026 International Conference  | `10.1109/emc68537.2026.11441735` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P99 | InfraAgent: A Multi-Agent AI Framework for Predictive Deployment Failure Detection and Autonomo | 2026 | Proceedings of the 18th International Confere | `10.1109/ecai69016.2026.11613753` | OA 1 · CR 1 · SC 1 | O | PENDENTE |
| P100 | AIDR-Cloud: An Agentic AI - Driven Incident Response Framework for Cloud Failures | 2026 | Conference Proceedings IEEE SOUTHEASTCON | `10.1109/southeastcon63549.2026.11476571` | OA 1 · CR 1 · SC 0 | O | PENDENTE |
| P101 | Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Respons | 2026 | Proceedings of the International Symposium on | `10.1109/isdfs69419.2026.11458922` | OA 1 · CR 1 · SC 0 | O | PENDENTE |
| P102 | Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident An | 2025 | International Journal of Intelligent Engineer | `10.22266/ijies2025.1231.28` | OA 0 · CR 0 · SC 2 | O | PENDENTE |
| P103 | From Alert Fatigue to Augmented Defense: A Case for AI Copilots in Cybersecurity Operation Cent | 2025 | 2025 10th International Conference on Informa | `10.1109/itt69610.2025.11352895` | OA 1 · CR 1 · SC 2 | O | PENDENTE |
| P104 | Agentic SOC: A Hierarchical Swarm-Orchestrated Multi-Agent LLM Architecture for Autonomous OT C | 2026 | 2026 International Wireless Communications an | `10.1109/iwcmc69287.2026.11579813` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P105 | Enhancing Cybersecurity Incident Response Efficiency Through Autonomous Agentic AI: Design, Imp | 2026 | 2026 Silicon Valley Cybersecurity Conference  | `10.1109/svcc69905.2026.11642294` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P106 | Agentic AI for Autonomous Cyber Threat Hunting and Adaptive Defense in Dynamic Security Environ | 2025 | IEEE International Conference on Electro Info | `10.1109/eit64391.2025.11103697` | OA 7 · CR 8 · SC 7 | O | PENDENTE |
| P107 | Agentic AI with Chatops for Large Scale Network Operations | 2025 | IEEE Conference on Artificial Intelligence (C | `10.1109/cai64502.2025.00242` | OA 3 · CR 3 · SC 1 | O | PENDENTE |
| P108 | ResilioMate: A Resilient Multi-Agent Task Executing Framework for Enhancing Small Language Mode | 2025 | IEEE Access | `10.1109/access.2025.3567244` | OA 4 · CR 4 · SC 4 | O | PENDENTE |
| P109 | Using Large Language Models to Support Human Decision-Making in SOC Infrastructure Management | 2026 | Lecture notes in computer science | `10.1007/978-3-032-29723-5_8` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P110 | DevAIOps: A Systematic Literature Review on Integrating Explainable AI Agents into CI/CD Pipeli | 2026 | Procedia Computer Science | `10.1016/j.procs.2026.08.403` | OA 0 · CR 0 · SC 0 | O,R_rel | PENDENTE |
| P111 | Integrating Large Language Models with Cloud-Native Observability for Automated Root Cause Anal | 2026 | Proceedings of 2025 3rd International Confere | `10.1145/3797161.3797213` | OA 10 · CR 11 · SC 5 | O | PENDENTE |
| P112 | Large language models for agentic NetOps and AIOps: Architectures, evaluation, and safety | 2026 | Computer Science Review | `10.1016/j.cosrev.2026.101075` | OA 0 · CR 0 · SC 0 | R_rel | ✅ |
| P113 | Reducing Incident Mean Time to Resolution Using Elasticsearch and Large Language Models | 2025 | International Journal of Computer Trends and  | `10.14445/22312803/ijctt-v73i3p116` | OA 0 · CR 0 · SC NÃO INDEXADO | O | PENDENTE |
| P114 | Debugmate: an AI agent for efficient on-call debugging in complex production systems | 2025 | Discover Data | `10.1007/s44248-025-00074-y` | OA 0 · CR 0 · SC NÃO INDEXADO | O | ✅ |
| P115 | Evidence-Verified LLM Agents for Safe Backend Incident Remediation | 2026 | 2026 3rd International Conference on Image Pr | `10.1109/icipai70034.2026.11605740` | OA 6 · CR 6 · SC 0 | O,R_rel | PENDENTE |
| P116 | LLM Based Cognitive AIOps Autonomous Cloud Incident Management | 2026 | 2026 International Conference on Emerging Tre | `10.1109/icemcsi67638.2026.11603148` | OA 0 · CR 0 · SC 0 | O | PENDENTE |
| P117 | Reducing Mean Time to Respond Using Large Language Model-Driven Incident Response with the Aid  | 2025 | 3rd International Conference on Intelligent M | `10.1109/imsa65733.2025.11167573` | OA 1 · CR 1 · SC 2 | O | PENDENTE |
| P118 | LLMDebug: Prompt-Engineered Large Language Models for Automated Root Cause Analysis in Microser | 2026 | 2026 International Conference on Advances in  | `10.1109/aaiml67890.2026.11498111` | OA 1 · CR 1 · SC 1 | O | PENDENTE |
| P119 | Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence | 2025 | Proceedings IEEE Global Communications Confer | `10.1109/globecom59602.2025.11432623` | OA 12 · CR 13 · SC 1 | O | PENDENTE |
| P120 | Real-Time Topology-Aware Log-Metric Correlation for LLM-based Root Cause Analysis in Distribute | 2026 | International Conference on Communication Sys | `10.1109/comsnets67989.2026.11418075` | OA 0 · CR 0 · SC 1 | O | PENDENTE |
| P121 | Large Language Models for Security Operations Centers: A Comprehensive Survey | 2026 | Journal of Electrical and Computer Engineerin | `10.1155/jece/3383674` | OA 13 · CR 15 · SC 1 | O,R_cit | PENDENTE |
| P122 | Integrating Agentic AI with NIST Frameworks: KPI Driven Detection and Response Improvements in  | 2026 | Lecture notes in networks and systems | `10.1007/978-3-032-34132-7_18` | OA 0 · CR 0 · SC NÃO INDEXADO | O | PENDENTE |
| P123 | An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in aut | 2026 | Discover Artificial Intelligence | `10.1007/s44163-026-02058-6` | OA 0 · CR 0 · SC NÃO INDEXADO | R_rel | ✅ |
| P124 | BudgetSRE: Budget-Aware Multi-Agent Incident Response for Backend Operations | 2026 | International Conference on Image Processing, | `10.1109/ipmml71439.2026.11682590` | OA 0 · CR 0 · SC NÃO INDEXADO | R_rel | PENDENTE |
| P125 | In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Appro | 2026 | Proceedings of the AAAI Symposium Series | `10.1609/aaaiss.v9i1.42938` | OA 0 · CR 2 · SC NÃO INDEXADO | R_rel | ✅ |
| P126 | Multiagent Incident Response Planning with Code Models | 2026 | Lecture notes in computer science | `10.1007/978-3-032-40367-4_21` | OA 0 · CR 0 · SC NÃO INDEXADO | R_rel | PENDENTE |

**PDFs:** 5 baixados automaticamente (open access com link direto); **32
pendentes** — download via Portal CAPES (como no ciclo 2), nomes-alvo
`P<ID>_<slug>.pdf` em `docs/`.

## Próximos passos (WORKFLOW)

1. Usuário: baixar os 32 PDFs pendentes (`Papers_Index.csv`, filtro
   "PENDENTE").
2. Etapa 2 (`/rsl-triagem`): elegibilidade bibliométrica I1–I5 →
   `papers-ciclo3.csv` (Qualis/SJR/citações por fonte).
3. Etapa 3 (`/rsl-extracao`): extração PICOC de leitura integral.
