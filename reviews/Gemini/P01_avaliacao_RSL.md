# Avaliação Sistemática de Estudo Primário — RSL (Kitchenham et al., 2009 / DARE)

## Identificação do Estudo
- **ID do Artigo:** P01 *(Corpus Fundacional herdado do Trabalho I — avaliação retroativa de padronização)*
- **Arquivo PDF Avaliado:** [P01-A2-Trustworthy agentic AI systems a cross-layer review of architectures threat models and governance strategies for real-world deployment.pdf](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/P01-A2-Trustworthy%20agentic%20AI%20systems%20a%20cross-layer%20review%20of%20architectures%20threat%20models%20and%20governance%20strategies%20for%20real-world%20deployment.pdf)
- **Prompt de Referência:** [prompt-P01.md](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/prompt-P01.md)
- **Título:** *Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment [version 1; peer review: awaiting peer review]*
- **Autores:** Ibrahim Adabara; Bashir Olaniyi Sadiq; Aliyu Nuhu Shuaibu; Yale Ibrahim Danjuma; Venkateswarlu Maninti (Kampala International University - Western Campus, Bushenyi, Western Region, Uganda)
- **Periódico / Fonte:** *F1000Research*, 2025, `14:905`, pp. 1–54 (Publicado em 11 de setembro de 2025; Status: *Awaiting Peer Review*)
- **DOI:** `10.12688/f1000research.169927.1`

---

## Etapa 0 — Extração Bibliométrica e Escopo

- **Metadados verificados no PDF:** Artigo de revisão narrativa (*Review*, versão 1, 54 páginas, 209 referências) publicado na plataforma *F1000Research* (`14:905`, 11 Sep 2025, p. 1), com dados suplementares depositados no *Figshare* (Tabelas A1–A9, Ref. 209, p. 48). Status editorial impresso na p. 1: `Approval Status: AWAITING PEER REVIEW`.
- **Métricas externas (`[VERIFICAR]`):**
  - **Citações:** `[VERIFICAR]` (não consta no PDF; verificar no *Scopus* ou *Google Scholar*).
  - **SJR / Quartil:** Informado como `Q1` no input do protocolo (`[VERIFICAR]` no *Scimago Journal Rank* para *F1000Research*).
  - **Qualis CAPES:** Informado como `A2` no input do protocolo (`[VERIFICAR]` na *Plataforma Sucupira / Qualis Periódicos*).
- **Adequação ao Escopo Temático da RSL:** **Altamente aderente (Estudo Fundacional Transversal e de Segurança/Governança)**. Realiza uma síntese *cross-layer* abrangente de sistemas de IA Agêntica cobrindo arquiteturas (monoagente, multiagente, federada e híbrida/blockchain), taxonomia de ameaças em múltiplas camadas, arquiteturas de defesa cibernética (*SHIELD*, *Zero-Trust*, *SAGA*, *ACD*, *AICA/MAICA*), implantações reais (incluindo *ReliaQuest* em resposta a incidentes de cibersegurança) e mecanismos de governança e revogação (*kill-switch*).

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério PRISMA | Status | Evidência no Texto / Justificativa |
| :--- | :---: | :--- |
| **1. Publicação entre 2020 e 2026** | **Atende** | Publicado em 11 de setembro de 2025 (*F1000Research*, `14:905`, p. 1). |
| **2. Publicação identificável (≠ NULL)** | **Atende** | Periódico *F1000Research* com DOI ativo (`10.12688/f1000research.169927.1`, p. 1). |
| **3. Citações ≥ 1 / SJR Q1–Q2 / Qualis A1–A2** | **`[VERIFICAR]`** | Informados no protocolo como `Qualis A2` e `SJR Q1` (verificados externamente em `papers.csv`; citações a verificar em base indexadora). |
| **4. Escopo: IA Agêntica em redes, segurança ou operações de TI** | **Atende** | Foco central em arquiteturas de IA Agêntica, modelagem de ameaças cibernéticas, defesas *Zero-Trust* e governança em produção (Seções 1–10, pp. 3–48). |
| **5. Regra do Corpus Fundacional (P01–P19)** | **Incluído (Herdado)** | Estudo fundacional herdado do Trabalho I; avaliação retroativa de padronização. |

**Status da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (INCLUÍDO NO CORPUS FUNDACIONAL DO TRABALHO I)**.

---

## Tabela A — Bibliométrica (Tabela 3 do Protocolo)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P01** | *F1000Research* (`14:905`, pp. 1–54) | 2025 | `[VERIFICAR]` | Q1 `[VERIFICAR]` | A2 `[VERIFICAR]` | *Review* (Revisão Narrativa Cross-Layer) | `10.12688/f1000research.169927.1` |

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5 do Protocolo)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **P01** | Adabara et al. (2025) | **RQ1** (Context Definitions: a. Autonomy definition; b. Core characteristics; c. Decision-making model) | Respondida Plenamente | **T (1.0)** | Seção 3 (Seções 3.1–3.4, pp. 7–10); Figuras 2 e 3 (pp. 8–9). | **(a)** Diferencia formalmente IA Agêntica de LLMs reativos e de agentes tradicionais baseados em regras fixas pela presença de autonomia dirigida a metas, autodecomposição de tarefas e ação proativa com mínima intervenção humana (Seção 3.1, pp. 7–8). **(b)** Detalha os 4 pilares fundamentais (Seção 3.2, pp. 8–9): *Memória* persistente episódica/semântica (ex.: *UserCentrix*), *Raciocínio* multi-etapas reflexivo e metacognitivo, *Planejamento* dinâmico e antecipatório com replanejamento (ex.: *Magentic-One*) e *Uso/Orquestração de Ferramentas* (APIs, bancos de dados). **(c)** Fundamenta os modelos decisórios em arquiteturas cognitivas (*ACT-R*, *Soar*, ciclo *observe–decide–act*), Aprendizado por Reforço (*DQN*, *PPO*, RL principal-agente), Teoria dos Jogos (*Theory of Mind* — ToM) e controle adaptativo distribuído (Seção 3.4, p. 10). |
| **P01** | Adabara et al. (2025) | **RQ2** (Engineering Architecture: a. Architecture type; b. Tools/frameworks; c. Advanced capabilities) | Respondida Plenamente | **T (1.0)** | Seção 4 (Seções 4.1–4.5, Tabela 1, pp. 10–13); Diagrama de 5 camadas (p. 7); Seção 6.3 (pp. 22–23); Seção 8 (Tabela 4, pp. 31–37); Seção 9.2 (p. 39). | **(a)** Propõe um modelo arquitetural em 5 camadas (*Governance*, *Cognition*, *Memory*, *Interaction* e *Secure Execution Layer* com *Trusted I/O*, *Policy Enforcement* e *Sandboxing*, diagrama na p. 7) e compara sistematicamente 4 paradigmas na Tabela 1 (p. 13): *Mono-Agent* (ex.: meta-agente hormonal *S-AI*), *Multi-Agent (MAAs)* (Figura 4, p. 12), *Decentralized/Federated* e *Hybrid/Blockchain-Enabled* (ex.: *SharHSC* com *sharding* e *state channels*). **(b)** Mapeia motores avançados de memória (*MARK*, *SemanticCommit*, grafo temporal *Zep* superando *MemGPT*, e índice semântico hierárquico *SHIMI*, Seção 9.2, p. 39), descoberta e identidade (*Agent Name Service — ANS* via PKI, *eSIM* telecom e *Accountability Fabric*, Seção 6.3, pp. 22–23) e frameworks de defesa (*SHIELD*, *Zero-Trust Architecture — ZTA*, *SAGA*, *ATFAA*, *CLASA*, *MELON*, *Task Shield*, *ShadowNet*, *AICA/MAICA*, Seção 8 e Tabela 4, pp. 31–36). **(c)** Aborda observabilidade em tempo de execução, *sandboxing*, revogação criptográfica e *kill-switches* (Seções 8.2, 9.4 e 9.8). |
| **P01** | Adabara et al. (2025) | **RQ3** (Evidence Benefits: a. Qualitative benefits; b. Quantitative benefits/metrics; c. Evidence level) | Parcialmente Respondida | **P (0.5)** | Seção 5.2–5.3 (p. 15); Seção 7 (Seções 7.1–7.4, pp. 27–30); Seção 8.3 (p. 34); Seção 9.8 (pp. 43–44). | **(a)** Documenta benefícios qualitativos em implantações reais na Seção 7 (pp. 27–30), destacando na área de Resposta a Incidentes e SecOps o caso industrial da **ReliaQuest** (Seção 7.1, p. 27), que emprega agentes autônomos para análise de telemetria, detecção de ameaças, priorização de risco e fluxos de remediação (elevando a velocidade de detecção e reduzindo a carga humana), além de *Twine's Alex*, *SAP Finance*, *Rockwell Automation* e suporte a decisões militares em redes 6G. **(b)** Reporta métricas quantitativas de vulnerabilidade e benchmarks extraídas da literatura primária (ex.: `10%` de envenenamento degradando enxames cooperativos; `~100%` de sucesso em ataques *backdoor* em agentes embarcados; `24%` de sucesso de injeção indireta no benchmark *InjecAgent*; e `>99%` de sucesso do ataque *AI²* no sequestro de memória orientada a ação, Seções 5.2–5.3, p. 15), além de catalogar plataformas de benchmark como *OSUniverse*, *REALM-Bench*, *CORE-Bench* e *EXACT* (Seção 9.8, p. 44). **(c)** Como revisão narrativa secundária, não executa experimentos próprios nem reporta tabelas comparativas de métricas operacionais de IR (como redução percentual de MTTR/MTTD). |
| **P01** | Adabara et al. (2025) | **RQ4** (Challenges & Ethics: a. Technical challenges; b. Ethical/governance challenges; c. Governance mechanisms) | Respondida Plenamente | **T (1.0)** | Seção 5 (Seções 5.1–5.9, Tabela 2, pp. 13–19); Seção 6 (Seções 6.1–6.6, Tabela 3, pp. 20–27); Seção 7.3 (pp. 29–30); Seção 8 (pp. 31–37). | **(a)** Constrói uma taxonomia de ameaças em 7 categorias (Seção 5 e Tabela 2, p. 19): (1) *Cognitive Exploits* (alucinação, *goal drift*, *reward hacking*); (2) *Memory Poisoning & Knowledge Manipulation* (*AI²*, *CrAIBench*); (3) *Tool Misuse, Prompt Injection & Action Trace Hijacking* (*ToolHijacker*, *Prompt Infection* autorreplicante entre agentes, *Foot-in-the-door* em agentes ReAct); (4) *Shadow Agents, Insider Risks & Stealth Execution* (*ATFAA*, *LibVulnWatch*, *AEIA*); (5) *Federated Governance Risks* (ataques Sybil, captura de governança em DAOs); (6) *Cross-Layer Threat Propagation* (*CLASA*); e (7) *Adversarial ML Exploits*, além de analisar falhas reais (*RealHarm*, *AI Incident Database*, Seção 7.3, pp. 29–30). **(b)** Examina lacunas éticas e jurídicas (Seção 6.2, p. 22): *"moral crumple zones"* (difusão de responsabilidade entre desenvolvedores, operadores e agentes), opacidade emergente, captura regulatória e personificação jurídica. **(c)** Compara modelos de governança (*OECD*, *EU AI Act*, *NIST AI RMF*, *DAOs/ETHOS*, *Federated Governance*, Tabela 3, p. 26) e propõe fluxos formais de identidade criptográfica (*SAGA*, *ANS*), auditoria semântica (*Accountability Fabric*), incorporação normativa (*MAPA*, *Gracenote.ai*) e revogação/*kill-switch* (Figura 10, p. 37). |
| **P01** | Adabara et al. (2025) | **RQ5** (Research Gaps: benchmarking, threat models, governança, observabilidade, alinhamento) | Respondida Plenamente | **T (1.0)** | Seção 9 (Seções 9.1–9.9, Tabela 5, pp. 38–45); Seção 10.2 (pp. 46–47). | Sistematiza na Seção 9 e na Tabela 5 (p. 45) seis domínios críticos de lacunas e direções futuras: (1) *Cybersecurity*: falta de relato padronizado de incidentes *cross-domain* e necessidade de defesas proativas adaptativas; (2) *Governance*: operacionalização fraca de ética e necessidade de governança policêntrica e prontidão institucional (*AFII*, *UNESCO RAM*, Seção 9.7); (3) *Ethics & Alignment*: superação das *moral crumple zones* e manipulação de recompensa via *Expectation Alignment (EAL)*, *SALMON*, IRL e raciocínio normativo sensível ao contexto (*MAPA*, Seções 9.1 e 9.6); (4) *Memory Integrity*: resolução semântica e temporal de conflitos (*MARK*, *SemanticCommit*, *Zep*, *SHIMI*, Seção 9.2); (5) *Multi-Agent Systems*: algoritmos de coordenação cientes de conflito e revogação criptográfica rápida (*BELIEFS*, Seção 9.4); e (6) *Benchmarking & Observability*: transição de testes caixa-preta para benchmarks orientados a observabilidade e segurança multiobjetivo (*REALM-Bench*, *OSUniverse*, *CORE-Bench*, *EXACT*, Seção 9.8). |
| **Total** | — | **`SCORE_RQ`** | — | **4.5 / 5.0** | **Média de aderência: 90,0% (4 Ts, 1 P, 0 N).** | Estudo fundacional de altíssima cobertura conceitual, arquitetural, de ameaças e de governança para a RSL. |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 do Protocolo)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :-: | :-: | :-: | :-: | :-: | :---: |
| **P01** | *Review* (Revisão Narrativa Cross-Layer, 54 pp., 209 refs.) | **Y (1.0)** | **P (0.5)** | **P (0.5)** | **Y (1.0)** | **3.0 / 4.0** | **Alta** |

### Justificativa Detalhada dos Critérios DARE (`QA1–QA4`)
- **QA1 — Objetivos Claros (`Y = 1.0`):** A Seção 1 (pp. 3–4) define com clareza o problema da ampliação da superfície de ataque e das lacunas de governança em sistemas de IA Agêntica e explicita quatro contribuições centrais (integração *cross-layer*, taxonomia de ameaças em camadas, síntese de governança com salvaguardas técnicas e mapeamento de lacunas de pesquisa).
- **QA2 — Metodologia Replicável (`P = 0.5`):** A Seção 2 (pp. 4–5) explicita as bases consultadas (*IEEE Xplore*, *ACM Digital Library*, *SpringerLink*, *ScienceDirect*, *arXiv*, além de relatórios da *OECD*, *NIST* e *Comissão Europeia*), os *clusters* de palavras-chave e os cinco critérios temáticos de relevância, disponibilizando tabelas suplementares no *Figshare* (Ref. 209, p. 48). Contudo, os autores declaram explicitamente adotar uma **revisão narrativa** em vez de uma RSL formal (p. 3 e diagrama na p. 24: *"No formal criteria; studies chosen based on coverage of relevant topics"*), sem reportar quantitativos PRISMA de triagem. Além disso, há trocas editoriais entre figuras e legendas ao longo do PDF (ex.: o diagrama da p. 7 mostra a arquitetura de 5 camadas sobre a legenda do *Flowchart 1*, enquanto o fluxograma da revisão aparece na p. 24 sobre a legenda do *Flowchart 4*).
- **QA3 — Base de Evidências Sólidas (`P = 0.5`):** O artigo sintetiza um amplo corpo de 209 referências, estruturando tabelas comparativas densas de arquiteturas (Tabela 1, p. 13), ameaças e lacunas de mitigação (Tabela 2, p. 19), governança (Tabela 3, p. 26), frameworks de defesa (Tabela 4, p. 36) e lacunas de pesquisa (Tabela 5, p. 45), além de discutir casos industriais reais como *ReliaQuest*, *CrAIBench* e *RealHarm* (Seção 7, pp. 27–30). Recebe `P (0.5)` por não conter validação empírica primária própria e por encontrar-se na versão 1 com status `AWAITING PEER REVIEW` na plataforma *F1000Research* (p. 1).
- **QA4 — Conclusões Coerentes (`Y = 1.0`):** As conclusões e recomendações estratégicas (Seções 9 e 10, pp. 38–48) derivam de maneira lógica, equilibrada e consistente das evidências multidisciplinares sintetizadas nas seções anteriores.

---

## Parecer Final do Revisor

### Síntese Crítica (3–5 linhas)
O estudo **P01** (integrante do Corpus Fundacional herdado do Trabalho I) oferece uma revisão *cross-layer* abrangente (54 páginas e 209 referências) que conecta arquiteturas de IA Agêntica (monoagente, multiagente, federada e híbrida/blockchain), modelagem de ameaças em múltiplas camadas, arquiteturas de defesa cibernética (*SHIELD*, *Zero-Trust*, *SAGA*, *ACD*, *AICA/MAICA*) e governança regulatória (*OECD*, *EU AI Act*, *NIST AI RMF*, *ETHOS*). O trabalho destaca-se pela profundidade na caracterização de ataques específicos a agentes (como *ToolHijacker*, *Prompt Infection* autorreplicante, sequestro de memória *AI²* e *shadow agents*) e mecanismos de controle como identidade criptográfica (*SAGA*, *ANS*) e *kill-switches* de revogação, alcançando `SCORE_RQ = 4.5/5.0` e `SCORE_QA = 3.0/4.0` (Banda Alta).

### Recomendação Final
- **Decisão:** **INCLUIR COM RESSALVAS** *(Estudo Fundacional do Trabalho I mantido no corpus; ressalva quanto à natureza narrativa da revisão e ao status `AWAITING PEER REVIEW` da versão 1 no F1000Research)*
- **Justificativa:** Como artigo fundacional já incorporado à RSL, **P01** fornece alicerce conceitual e taxonômico direto para responder plenamente às questões **RQ1, RQ2, RQ4 e RQ5**, além de contribuir parcialmente para **RQ3** com casos reais de implantação em cibersegurança (como *ReliaQuest* em detecção e resposta a incidentes).

### Pendências de Verificação Externa (`[VERIFICAR]`)
1. **Status de Revisão por Pares (*F1000Research*):** Verificar na página oficial do artigo (`https://doi.org/10.12688/f1000research.169927.1`) se a versão 1 já obteve relatórios de aprovação dos revisores após 11/09/2025.
2. **Qualis CAPES e SJR:** Confirmar externamente o estrato `A2` na *Plataforma Sucupira* e o quartil `Q1` no *Scimago Journal Rank* (registrados em `papers.csv`).
3. **Citações:** Atualizar a contagem de citações no *Scopus* ou *Google Scholar*.
