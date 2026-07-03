# Trabalho I — RSL fundacional (corpus P1–P19)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [🔎 Descoberta de candidatos](../research/README.md) · [📊 Dashboard](../reviews/DASHBOARD.md) · [📚 Pareceres](../reviews/README.md)

Trabalho anterior do mestrado (PPGCA · Unisinos): a **Revisão Sistemática da Literatura (RSL) original** sobre _"Agentic AI como copilot para reduzir MTTD e MTTR na resposta a incidentes"_, com seus **19 estudos incluídos (P1–P19)**. Este é o **corpus fundacional** do Trabalho II.

O artigo e seu corpus serviram de **referência para construir o prompt de busca** ([`../research/prompt.md`](../research/prompt.md)) da Etapa 1 do Trabalho II: o PDF do artigo é o "SLR anexado" tratado como corpus corrente, e os 19 estudos P1–P19 são a base de deduplicação — nenhum candidato novo (P20–P40) pode repetir um estudo daqui.

## 📁 Conteúdo

| Item                                                     | Descrição                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| [`Artigo_Agentic_AI V3.pdf`](Artigo_Agentic_AI%20V3.pdf) | Artigo final da RSL (versão 3) — texto submetido.            |
| `Artigo_Agentic_AI V3_Latex.zip`                         | Fontes LaTeX do artigo (fonte editável da versão 3).         |
| [`References/`](References/)                             | Os **19 estudos incluídos** (P1–P19), um PDF por referência. |

## 📚 Estudos incluídos (P1–P19)

| ID  | Estudo                                                                                             |
| --- | -------------------------------------------------------------------------------------------------- |
| P1  | Trustworthy agentic AI systems — cross-layer review of architectures, threat models & governance   |
| P2  | The role of agentic AI in shaping a smart future — a systematic review                             |
| P3  | A Research Landscape of Agentic AI and LLMs — Applications, Challenges and Future Directions       |
| P4  | LLM-Based Multi-Agent Systems for Software Engineering — Literature Review, Vision & Road Ahead    |
| P5  | A Survey of AIOps in the Era of Large Language Models                                              |
| P6  | Agentic AI — A Comprehensive Survey of Technologies, Applications and Societal Implications        |
| P7  | Artificial Empathy — A New Perspective for Analyzing and Designing Multi-Agent Systems             |
| P8  | Applications, Challenges and Future Directions of Human-in-the-Loop Learning                       |
| P9  | AI Agents vs. Agentic AI — A Conceptual taxonomy, applications and challenges                      |
| P10 | Agentic AI — Autonomous Intelligence for Complex Goals — A Comprehensive Survey                    |
| P11 | Co-Evolving Multi-Agent Transfer RL via Scenario-Independent Representation                        |
| P12 | Enhancing autonomous system security and resilience with generative AI — a comprehensive survey    |
| P13 | Retail Resilience Engine — An Agentic AI Framework with Test-Driven Development                    |
| P14 | Transforming Cybersecurity with Agentic AI to Combat Emerging Cyber Threats                        |
| P15 | The Rise of Agentic AI — Definitions, Frameworks, Architectures, Applications, Metrics, Challenges |
| P16 | A Joint Study of the Challenges, Opportunities and Roadmap of MLOps and AIOps — Systematic Survey  |
| P17 | A Review of Trustworthy and Explainable Artificial Intelligence (XAI)                              |
| P18 | An architecture for model-based and intelligent automation in DevOps                               |
| P19 | Agent System Mining — Vision, Benefits and Challenges                                              |

> ℹ️ O corpus P1–P19 do Trabalho I é a base de deduplicação da Etapa 1 do Trabalho II. Estudos posteriores do mesmo grupo de autores são admissíveis como candidatos novos, mas marcados com `author_overlap` no [prompt de busca](../research/prompt.md).

## 🔁 De onde vem, para onde vai

```
TrabalhoI/  (RSL fundacional: artigo + 19 estudos P1–P19)
     │  serve de referência e corpus corrente
     ▼
research/prompt.md  (Etapa 1 do Trabalho II: busca de novos candidatos, sem repetir P1–P19)
     │
     ▼
corpus P20–P40  ──►  prompts/ + docs/ + reviews/  (avaliação detalhada)
```
