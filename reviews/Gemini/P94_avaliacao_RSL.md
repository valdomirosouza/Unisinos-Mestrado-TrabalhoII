# Parecer — P94: Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments

> Avaliador: Gemini · Data: 2026-10-29 · Prompt: prompt-P94.md
> (template v1.1.0)

## Tabela A — Identificação e PICOC

| Campo | Valor |
| :--- | :--- |
| **Veículo / ano / DOI** | *Applied Sciences* (MDPI), Vol. 16, No. 16, Art. 7915 (31 pp.) · 2026 · DOI: `10.3390/app16167915` |
| **Qualis · SJR (insumo)** | Qualis **A2** (derivado do percentil Scopus `85%`) · SJR **N/D** · Citações: OpenAlex `0` · Crossref `0` · Scopus `0` |
| **Tipo / paradigma** | Artigo Primário de Engenharia de Segurança e Avaliação Experimental em Testbed Real (**LLM Multi-Agent System** com **Model Context Protocol [MCP]** integrado ao **Wazuh SIEM** + **Middleware Security Framework** em 5 Camadas) |
| **P · I · C · O · C** | **P (Population):** Pipelines multiagentes baseados em LLMs (`GPT-4o mini`) conectados via **Model Context Protocol (MCP)** a um SIEM real (**Wazuh 4.14.0**) para automação de triagem, enriquecimento e resposta a alertas de Level 1 em SOCs.<br>**I (Intervention):** Arquitetura multiagente sequencial de 3 agentes (*Triage Agent* [3 tools], *Enrichment Agent* [7 tools], *Response Agent* [6 tools]) com memória compartilhada persistente (*alert history log, agent knowledge base, context store*) protegida por um **Security Framework Middleware** *drop-in* composto por um **Validador de Registro de Ferramentas na Conexão (L0)** (regex de descrição, propriedade de namespace e *pinning* SHA-256 de manifesto/binário) e **5 Camadas de Execução**: *L1 Access Control (RBAC em runtime)*, *L2 Rate Limiter* (`20–30 calls/60s` por agente e `10 approvals/h`), *L3 Input Validator* (JSON Schema, regex em argumentos/handoffs/memória/dados externos, sequência de handoff e isolamento de sessão UUID), *L4 Output Validator* (regex anti-injeção/exfiltração/AI virus e limite de `100 KB`) e *L5 Audit Log* (*append-only* com redaction SHA-256).<br>**C (Comparison):** Comparação experimental executada contra o **pipeline baseline desprotegido** (conexão direta aos servidores MCP legítimo e malicioso sem o middleware) e avaliação de **6 suítes de teste (`T00–T05`)** combinando `25` instâncias de ataque com chamadas legítimas pareadas ao longo de `600` execuções, além de testes com `4` técnicas de ofuscação e `8` entradas legítimas de SOC com substrings semelhantes a ataques.<br>**O (Outcome):** Cobertura arquitetural de **29 de 35 vetores de ataque** derivados de 5 taxonomias (OWASP LLM/Agentic, OWASP MCP Top 10, MITRE ATLAS, ATFAA, MCP-38). Nas 6 suítes (`600` decisões): **600/600 ataques bloqueados (`100%`)**, `0` ataques vazados (`Passed = 0`) e `0` falsos bloqueios (`FB = 0`) no conjunto legítimo padrão. *Overhead* local do middleware ($N = 10.000$): **`< 0,6 ms`** por chamada (`546,6 µs` no JSON Schema, caindo para **`< 30 µs`** totais com pré-compilação de schema em `11,4 µs`). Sob **ofuscação** (*Base64, Homoglyph, Espanhol, Paraphrase*): `0/4` bloqueados (`100%` de evasão do filtro léxico); em **tráfego legítimo de SOC com metacaracteres/citações de ataque**: `7/8` bloqueados como falsos positivos pelo filtro léxico.<br>**C (Context):** Testbed laboratorial isolado integrando máquina virtual Vagrant (Ubuntu 22.04 LTS com Wazuh 4.14.0 completo) e 3 segmentos de rede Docker Compose (servidor MCP Wazuh em Rust 1.86, servidor MCP malicioso em Python 3.11 e gateway FastAPI). |

---

## Tabela B — Cobertura das RQs

| RQ | T/P/N | Evidência (seção/página) |
| :--- | :---: | :--- |
| **RQ1** | **T** (`1.0`) | **Seções 1, 2 e 3.1, Figura 1 (pp. 2–7):** Caracteriza com precisão a evolução de LLMs isolados e SOAR estático para **sistemas multiagentes baseados em MCP** capazes de planejamento, invocação padronizada de ferramentas e acúmulo de contexto entre sessões. Define especialização de papéis com privilégio mínimo (*Triage, Enrichment, Response*), memória persistente em três repositórios e **supervisão humana no loop (HITL)** obrigatória (o *Response Agent* nunca executa ações diretamente; `propose_wazuh_rule` apenas gera proposta estruturada com flags de aprovação e escalonamento para revisão do analista, p. 6). |
| **RQ2** | **T** (`1.0`) | **Seções 3.1 a 3.3, Figuras 1 a 9, Tabelas 3 e 4 (pp. 5–18):** Detalha de ponta a ponta a engenharia do pipeline multiagente e do middleware de segurança em Python 3.11 / FastAPI e Rust 1.86: controle de fase de conexão (**L0**: regex em metadados de ferramentas, propriedade de namespace contra *tool shadowing*, *pinning* SHA-256 de manifesto contra *rug pull* e verificação binária SHA-256 do container MCP), cinco camadas sequenciais de execução (**L1 RBAC**, **L2 Rate Limiter** por agente e por pipeline de aprovação, **L3 Input Validator** com JSON Schema e isolamento de *context store* por UUID de sessão, **L4 Output Validator** com limite de `100 KB` e **L5 Audit Log** *append-only* com hash SHA-256 de argumentos sensíveis) e controles transversais (*Safe Error Handling* com opacidade de falha e autenticação `X-MCP-API-Key` + `Origin`). Mapeia todos os controles ao guia *OWASP Practical Guide for Secure MCP Server Development v1.0* (Tabela 3, p. 14). |
| **RQ3** | **T** (`1.0`) | **Seções 3.4, 3.5 e 4.1 a 4.5, Tabelas 5 a 15 (pp. 18–26):** Reporta avaliação experimental completa: (i) **600/600 bloqueios (`100%`)** em `25` subtestes $\times$ `20` execuções cobrindo 29 vetores, com `0` falsos bloqueios em chamadas benignas padrão (Tabela 12, p. 23); (ii) demonstração *full-pipeline* contra alerta real do Wazuh e alerta sintético de SSH brute-force comparando condição desprotegida vs. protegida, preservando 100% da saída operacional legítima (Seção 4.2, pp. 23–24); (iii) micro-benchmark de latência ($N = 10.000$, Tabela 13, p. 24) provando *overhead* desprezível (`0,2 µs` em L1, `0,9 µs` em L2, `5,6–16,5 µs` em scans L3, `14,4 µs` em L4 e `546,6 µs` $\to$ `11,4 µs` no JSON Schema); e (iv) avaliação quantitativa dos limites do filtro léxico sob ofuscação (`0/4` bloqueados, Tabela 14, p. 25) e tráfego legítimo de SOC com substrings de comando/ataque (`7/8` falsos positivos, Tabela 15, pp. 25–26). |
| **RQ4** | **T** (`1.0`) | **Seções 1, 2, 3.1, 3.2.8 e 5, Tabelas 2 e 5–11 (pp. 2–4, 6–7, 12–14, 19–22, 26–28):** Constrói um modelo de ameaças sistemático e reprodutível de **35 vetores de ataque** para sistemas multiagentes MCP em SOCs, distribuídos em 8 categorias (*Prompt-based, Tool & MCP, Memory & Data, Multi-Agent, Protocol, Exfiltration, Infrastructure, Autonomy & Governance*, Tabela 2, p. 13), cobrindo *tool poisoning*, *tool shadowing*, *rug pull*, *confused deputy*, *inter-agent trust exploitation*, *memory poisoning*, *AI virus/self-propagation*, *oversight saturation* e *consent fatigue*. |
| **RQ5** | **T** (`1.0`) | **Seções 5 e 6 (pp. 26–29):** Identifica com precisão cirúrgica as lacunas abertas e direções futuras: (1) substituição da inspeção léxica (regex) em L3/L4 por **detecção semântica baseada em classificadores ou LLMs** para mitigar tanto a evasão por ofuscação/paráfrase/multilíngue quanto os falsos positivos em logs técnicos de SOC; (2) generalização do validador de sequência de *handoff* (de lista linear para grafo de transição) para suportar topologias multiagentes não-sequenciais, hierárquicas ou descentralizadas e endereçar *consensus manipulation* e *covert coordination*; (3) proteção anti-*replay* com *nonce/timestamp* no servidor MCP; (4) avaliação cruzada em múltiplos LLMs além do `GPT-4o mini`; e (5) *hash chaining* criptográfico (*tamper-evidence*) e integração do log de auditoria ao próprio SIEM em tempo real. |

**SCORE_RQ:** `5.0` (`5.0 / 5.0`)

---

## Tabela C — Qualidade (DARE)

| QA | Y/P/N | Justificativa |
| :--- | :---: | :--- |
| **QA1 Objetivos claros** | **Y** (`1.0`) | Define objetivos altamente específicos e aplica 3 critérios explícitos e reprodutíveis de inclusão para derivar os 35 vetores do modelo de ameaças (*Architectural relevance, Empirical grounding, SOC applicability*, Seção 3.2.8, p. 12), além de 4 critérios formais de sucesso por subteste (Seção 3.5.4, p. 23). |
| **QA2 Metodologia replicável** | **Y** (`1.0`) | Reprodutibilidade exemplar: descreve toda a topologia de rede, versões de pacotes (`Python 3.11`, `Rust 1.86`, `Wazuh 4.14.0`, `gpt-4o-mini-2024-07-18`, `MCP 2025-06-18`, Tabela 4, p. 17) e disponibiliza publicamente todo o código-fonte dos agentes, do middleware, do servidor MCP malicioso e do *test harness* (`run_tests.py`) no GitHub (`https://github.com/UPM-RSTI/MCP_Sec_Framework`, Seção 3.3, p. 18 e *Data Availability Statement*, p. 29). |
| **QA3 Base de evidência sólida** | **Y** (`1.0`) | Combina 600 execuções em 6 suítes isoladas (Tabela 12), demonstração *end-to-end* contra SIEM Wazuh real (Seção 4.2), benchmark de latência com `10.000` repetições (Tabela 13) e testes adversariais de transparência exemplar que demonstram empiricamente onde o controle léxico falha (Tabelas 14 e 15, pp. 25–26). |
| **QA4 Conclusões coerentes** | **Y** (`1.0`) | As conclusões (Seções 5 e 6, pp. 26–29) delimitam com rigor absoluto as condições de contorno sob as quais as garantias do framework se sustentam e onde não se aplicam (adversários adaptativos/ofuscados, topologias não-sequenciais e tráfego legítimo contendo substrings de ataque). |

**SCORE_QA:** `4.0` (`4.0 / 4.0`) · **Banda:** Alta

---

## Detalhamento Analítico (Etapa 0 e Etapa 1)

### Elegibilidade e Alinhamento ao Protocolo (PDR-0006 / PDR-0007)
- **Aderência Temática (PICOC):** O artigo situa-se exatamente na interseção central da RSL: engenharia e segurança de sistemas multiagentes baseados em LLM e **Model Context Protocol (MCP)** operando sobre alertas reais de um SIEM (**Wazuh**) em ambiente de SOC.
- **Avaliação de Comparison:** Executa comparação experimental direta entre o pipeline desprotegido (baseline) e o pipeline protegido pelo middleware (Seção 3.5.1 e Seção 4.2), além de parear cada vetor de ataque com chamadas legítimas e avaliar variações ofuscadas vs. literais.
- **Avaliação de Estrato:** Publicado no periódico *Applied Sciences* (MDPI), classificado como **Qualis A2** (percentil Scopus `85%`), não exigindo qualquer ressalva de estrato sob os PDRs vigentes.

---

## Síntese do avaliador

O estudo **P94 (Simões et al., 2026)** é uma das contribuições técnicas e experimentais mais sólidas e diretamente aplicáveis de todo o corpus da RSL para o projeto de um *Agentic AI Copilot para Resposta a Incidentes*. Os autores projetam, implementam em código aberto e validam experimentalmente um pipeline multiagente (*Triage, Enrichment, Response*) conectado a um **Wazuh SIEM 4.14.0** via **Model Context Protocol (MCP)** e protegido por um middleware de segurança em cinco camadas de execução mais validação de registro na conexão. Além de sistematizar um modelo de ameaças de **35 vetores de ataque** específicos para sistemas multiagentes MCP em SOCs e comprovar bloqueio de `100%` (`600/600`) dos payloads em claro com *overhead* inferior a `30 µs` (com JSON Schema pré-compilado), o artigo destaca-se pela honestidade científica ao demonstrar experimentalmente os dois modos de falha da inspeção léxica baseada em regex: a evasão total (`100%`) por payloads ofuscados/parafraseados (Tabela 14) e a ocorrência de falsos positivos (`7/8`) quando os agentes manipulam logs legítimos de SOC contendo metacaracteres shell ou citações de ataques (Tabela 15). Embora não meça MTTD/MTTR operacional de analistas humanos (seu *outcome* é a eficácia de guardrails e o *overhead* de processamento), o trabalho fornece uma arquitetura de referência imediatamente reutilizável para as Questões de Pesquisa **RQ1, RQ2, RQ3, RQ4 e RQ5**.

## Recomendação

`Incluir`
