# Snowballing do ciclo 3 — rota de recaptura do P90

> 🧭 [🏠 README raiz](../README.md) · [🔎 Descoberta do ciclo 3](descoberta-ciclo3.md) · [📜 PDR-0006](../protocolo/pdr/PDR-0006-estrato-de-conference-papers-pelo-percentil-da-serie.md) · [📊 Dashboard](../reviews/DASHBOARD.md)

Executado em **2026-10-29**, após o fecho das Etapas 8–9 do ciclo 3. Objeto: a
**nota do condutor no PDR-0006** — o P90 ("Demonstrating Multi-Agent
Collaboration via Agent-to-Agent and Model Context Protocols: An IT Incident
Response Case Study", Tupe & Thube, IEEE SOSE 2025, DOI
`10.1109/sose67019.2025.00013`), candidato mais citado da descoberta do ciclo
(OA 7 · CR 7 · SC 6), saiu INELEGÍVEL na Etapa 1 por série de proceedings sem
CiteScore, com o snowballing obrigatório do protocolo registrado como rota de
recaptura.

O protocolo ([`prompt-v3.md`](prompt-v3.md), PM-3) exige snowballing backward
e forward a partir do conjunto incluído, com **contagens PRISMA separadas**
dos registros de busca em base.

## Método

1. **Backward (o corpus referencia o P90?):**
   - Referências depositadas na OpenAlex para os 12 incluídos do ciclo 3
     (`referenced_works`); depósito incompleto em vários registros (P102,
     P112, P121 com 0 referências depositadas), então com fallback de
     **varredura full-text dos 121 PDFs do acervo `docs/`** (pypdf) pelos
     padrões: sobrenomes dos autores (Tupe, Thube), título ("Agent-to-Agent
     and Model Context Protocols"), fragmento do DOI (`sose67019`,
     `10.1109/sose`).
2. **Forward (quem cita o P90?):** citantes do P90 na OpenAlex
   (`cites:W4413680021`), com checagem de sobreposição por DOI contra o
   `Papers_Index.csv`.

## Resultados

### Backward — nenhuma recaptura

- OpenAlex: **nenhum** dos 12 incluídos do ciclo 3 referencia o P90.
- Varredura full-text dos 121 PDFs: **nenhum estudo do acervo cita o P90**.
  Única menção aos autores: o **P09** cita _outro_ trabalho de Tupe & Thube
  ("AI agentic workflows and enterprise APIs", arXiv 2502.17443) — não é o
  P90.

### Forward — 7 citantes, nenhum candidato novo no domínio

| Citante (ano)                                                                | Veículo             | DOI                                       | Domínio IR/ITOps?                                        |
| ---------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | -------------------------------------------------------- |
| An MCP Tool for Bug Localization… (2026)                                     | IEEE Access         | `10.1109/access.2026.3665337`             | ❌ SE/bug localization                                   |
| A Data-Driven Distributed Autonomous Architecture for the 6G Network (2025)  | Electronics         | `10.3390/electronics15010102`             | ❌ redes 6G                                              |
| Emerging Agent Communication Protocols for Healthcare AI… (2026)             | preprint (JMIR)     | `10.2196/preprints.93344`                 | ❌ saúde                                                 |
| Advance LLM-based MCP and A2A Protocol for Child Medical Emergency… (2025)   | ICIC                | `10.1109/icic68258.2025.11413209`         | ❌ saúde                                                 |
| Operationalizing Multi-Agent Interoperability via Contract-Driven MCP (2026) | IEEE SoutheastCon   | `10.1109/southeastcon63549.2026.11476405` | ❌ interoperabilidade genérica (sem IR)                  |
| Conversational IoT — MCP-Orchestrated LLMs… (2026)                           | ICICI               | `10.1109/icici68773.2026.11581082`        | ❌ IoT                                                   |
| **AIRIN: An LLM-Driven Multi-agent Framework… IT Service Incident…** (2026)  | **CCIS (Springer)** | `10.1007/978-3-032-30836-8_20`            | ✅ **já no acervo: é o P92** (triagem adiada — Springer) |

Contagens PRISMA (separadas da busca em base, conforme PM-3):
`identified_snowballing = 7` (forward) · `0` (backward) → duplicados/já no
acervo: 1 (P92) → fora de domínio: 6 → **candidatos novos elegíveis à
triagem: 0**.

## Conclusão e encaminhamento

1. **O P90 permanece INELEGÍVEL (PDR-0006), sem recaptura:** a rota prevista
   na nota do condutor foi executada e deu negativo — nenhum estudo do corpus
   (incluídos dos ciclos 0–3 e demais PDFs do acervo) o referencia, e seus
   citantes não trazem candidato novo no domínio. Não há base para PDR de
   revisitação.
2. **Vínculo registrado:** o único citante em domínio é o **P92** (Springer,
   triagem adiada), que cita o P90. Quando o texto integral do P92 for obtido
   (biblioteca/COMUT) e triado em adendo, o caso P90 pode ser reavaliado à
   luz dessa cadeia de citação — reavaliação condicionada a nova decisão do
   condutor, como prevê o PDR-0006.
3. **Escopo:** esta execução cobre a rota de recaptura do P90. O snowballing
   backward/forward **completo** do conjunto incluído (65 estudos) é insumo
   da descoberta de um eventual ciclo 4, fora do escopo desta nota.

---

_Fontes: OpenAlex (`works/doi:…`, `cites:W4413680021`, consulta 2026-10-29) e
varredura full-text do acervo local (`docs/`, 121 PDFs, pypdf). Dados crus da
consulta forward no scratchpad da sessão (não versionados; tabela acima é o
registro)._

> **Nota datada (2026-10-29):** com a remoção definitiva do P92
> ([PDR-0008](../protocolo/pdr/PDR-0008-remocao-dos-springer-nao-recuperados.md),
> reports not retrieved), a rota de reavaliação do P90 pela cadeia P92→P90
> do item 2 acima **encerra-se**. P90 permanece INELEGÍVEL.
