# Avaliação Sistemática de Estudo Primário/Secundário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P26
- **Título:** *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications*
- **Autores:** Zhijing Li; Jianbo Yu; Zhijun Huang; Yusheng Huang
- **Periódico/Conferência:** *IEEE Transactions on Services Computing*, Vol. 19, No. 1, pp. 808–825 (Publicado em 13 de novembro de 2025; versão atual em 5 de fevereiro de 2026)
- **DOI:** `10.1109/TSC.2025.3631913`
- **Arquivo avaliado:** `P26-A1-Surveying_Root_Cause_Analysis_Techniques_A_Comprehensive_Review_of_Aspects_for_Multi-Service_Applications.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Estudo secundário (*Survey Paper* / Revisão Sistemática da Literatura seguindo diretrizes de Kitchenham et al. [6], cobrindo artigos de 2017 a 2025 em 5 bases: Google Scholar, IEEE Xplore, ACM Digital Library, DBLP e Scopus; Seção II, pp. 809–811).
- **Foco técnico:** Revisão abrangente de técnicas de Análise de Causa Raiz (*Root Cause Analysis* — RCA) para aplicações multi-serviço (*microservices* / *Service-Oriented Architecture*), categorizadas por tipo de dado de entrada (*logs*, *execution traces*, métricas/KPIs, relatórios de *bugs* e abordagens híbridas/LLMs), além de levantamento de *datasets*, ferramentas e métricas de avaliação.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Atendido parcialmente. O artigo foca diretamente em Análise de Causa Raiz (RCA) e diagnóstico de falhas em aplicações multi-serviço (núcleo de resposta a incidentes em *cloud/microservices*), dedicando parte da Seção VII (p. 815) e da Seção XII (pp. 822–823) a métodos baseados em LLMs e agentes (como agentes *ReAct* e o benchmark *OpenRCA*).
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *IEEE Transactions on Services Computing*, 2025/2026).
  - *IC3 (Rigor técnico/metodológico):* Atendido com ressalvas editoriais (revisão estruturada com critérios de busca, seleção, extração de dados e 15 tabelas comparativas).
- **Critérios de Exclusão (EC):** Não incide em exclusão direta por fora de escopo, embora seja um estudo secundário cujo foco predominante recai sobre métodos estatísticos, de grafos e *deep learning* tradicional, tratando *Agentic AI* de modo incipiente.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P26 | IEEE Transactions on Services Computing | 2026 (online 2025) | [VERIFICAR] | Q1 [VERIFICAR] | A1 [VERIFICAR] | Survey / Revisão Sistemática (Secundário) | `10.1109/TSC.2025.3631913` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A1`) não constam no corpo do PDF e devem ser auditados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *IEEE Xplore / Google Scholar / Scopus*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P26 | Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications | **RQ1** (Contexto e Definições) | Não atendido | **N** (0.0) | Seção I (pp. 808–809); Seção VII (p. 815) | O *survey* revisa algoritmos estatísticos, de grafos e de aprendizado profundo para RCA classificados por modalidade de dado (*logs*, *traces*, métricas e *bug reports*). Apenas um único parágrafo na Seção VII (p. 815) menciona 3 trabalhos recentes baseados em LLMs/agentes (Ahmed et al. [64], Roy et al. [65] com agente *ReAct* e Xu et al. [66] com *OpenRCA*). Não define níveis de autonomia agêntica, memória, planejamento ou modelos de tomada de decisão de *Agentic AI*. |
| P26 | Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications | **RQ2** (Arquitetura de Engenharia) | Parcialmente atendido | **P** (0.5) | Seção II-C, Figuras 1 e 2 (pp. 810–811); Seções III–VII, Tabelas IV–VII (pp. 810–815); Seção IX-B, Tabela XIV (pp. 819–820) | Embora não descreva arquiteturas de agentes autônomos (orquestração, memória, *guardrails*), mapeia de forma estruturada o fluxo geral de engenharia de RCA em três fases (detecção de erro, análise de causa raiz com triagem/localização e resolução de problema, Figuras 1–2), a taxonomia técnica por modalidade de telemetria (*Logs*, *Traces*, Métricas, *Bug Reports* e Híbridos nas Tabelas IV–VII) e ferramentas de APM/RCA como *SkyWalking*, *Alibaba ARMS*, *Pinpoint*, *Fault Tree Analysis*, *5 Whys*, *FMEA*, *Fishbone* e *Pareto* (Tabela XIV). |
| P26 | Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications | **RQ3** (Benefícios e Evidências) | Parcialmente atendido | **P** (0.5) | Seção II-C, Figura 5 (p. 811); Seção VII (p. 815); Seção X, Tabela XV (pp. 820–822) | Como estudo secundário, sistematiza as métricas de avaliação utilizadas em RCA na Tabela XV e Figura 5 (`Top@N` em 57% dos estudos, `Precision/Recall/F1-Score` em 29%, `MRR` em 19%, além de `AC@k`, `MAP`, `EXAM Score`, `AUROC`, *Purity* e *BCubed*). Na Seção VII (p. 815), reporta pontualmente evidências de estudos com LLMs: modelos *fine-tuned* em 40K+ incidentes da Microsoft superam *baselines* *encoder-decoder* [64]; agentes *ReAct* igualam *baselines* fortes em cenários *out-of-distribution* [65]; porém, no benchmark *OpenRCA* (335 falhas, 68 GB de telemetria), o melhor agente LLM resolve apenas 11,3% dos casos [66]. |
| P26 | Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications | **RQ4** (Desafios e Ética) | Parcialmente atendido | **P** (0.5) | Seção VIII (pp. 816–817); Seção IX-A (pp. 818–819); Seção XII (pp. 822–823) | Identifica desafios técnicos críticos em sistemas multi-serviço: origens diversas de anomalias, topologia dinâmica de invocação, propagação em cascata de falhas, explosão dimensional de KPIs, privacidade e escassez de rotulagem em *datasets* industriais. Especificamente para métodos baseados em LLMs (Seção XII, p. 822), aponta restrição de janela de contexto, suscetibilidade a alucinações, baixa eficácia em cenários reais complexos (11,3% no *OpenRCA*) e ausência de interpretabilidade causal. Não aborda desafios éticos amplos nem governança agêntica. |
| P26 | Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications | **RQ5** (Lacunas de Pesquisa) | Totalmente atendido | **T** (1.0) | Seção XII (*Open Issues and Research Trend*, pp. 822–823) | Delimita lacunas e tendências futuras diretamente alinhadas à evolução de agentes para RCA: (1) evolução de métodos baseados em LLMs com compreensão contextual aprimorada, mitigação de alucinações, raciocínio causal robusto, janelas de contexto estendidas e integração de conhecimento de domínio via *prompt design*, *fine-tuning* e arquiteturas híbridas; (2) fusão multimodal de telemetria (*logs*, *traces*, métricas e topologia); (3) criação de *benchmarks* e *datasets* públicos multimodais em larga escala; (4) generalização *cross-domain* diante de mudanças dinâmicas de topologia; e (5) combinação de inferência causal com processamento em *streaming* em tempo real e explicabilidade. |
| **P26** | **SCORE_RQ Total** | — | **2.5 / 5.0** | — | — | Atende integralmente RQ5 (1.0), parcialmente RQ2 (0.5), RQ3 (0.5) e RQ4 (0.5), e não atende RQ1 (0.0). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P26 | Survey / Revisão Sistemática (Estudo Secundário) | P (0.5) | P (0.5) | Y (1.0) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Clareza e relevância dos objetivos / critérios de inclusão (P = 0.5):** O objetivo de revisar técnicas de RCA em aplicações multi-serviço sob a ótica de modalidades de dados e cenários de falha é claramente definido nas Seções I e II (pp. 808–810), com protocolo baseado em Kitchenham et al. [6]. Contudo, em relação ao escopo específico de *Agentic AI*, a cobertura é tangencial (restrita a um parágrafo na Seção VII e discussões futuras na Seção XII).
- **QA2 — Adequação da estratégia de busca e desenho metodológico (P = 0.5):** A busca abrangeu 5 bases indexadoras entre 2017 e 2025 com 96 combinações de palavras-chave e veículos (Seção II-A, pp. 809–810). Entretanto, o artigo apresenta inconsistências quantitativas e editoriais internas: o texto da Seção II-B (p. 810) declara 845 artigos coletados e 97 selecionados, ao passo que a Tabela II (p. 811) totaliza 893 artigos coletados e a Tabela III (p. 811) soma 104 artigos selecionados; há também referências cruzadas de tabelas trocadas no texto das pp. 811–813 e uma sentença incompleta na p. 815 (*"We give some examples in Table."*).
- **QA3 — Qualidade da avaliação / síntese dos estudos e evidências (Y = 1.0):** Sintetiza um corpo expressivo de literatura revisada por pares em veículos de primeira linha (ICSE, FSE, ASE, ISSRE, TSE, TSC), estruturando tabelas comparativas detalhadas por técnica (Tabelas IV–X), catálogo de *datasets* públicos, industriais e simulados como *TrainTicket* e *Sock Shop* (Tabelas XI–XIII), ferramentas de mercado (Tabela XIV) e formulações matemáticas das métricas de avaliação (Tabela XV, pp. 820–821).
- **QA4 — Consistência entre evidências coletadas e conclusões (Y = 1.0):** As discussões de desafios abertos e conclusões (Seções XII e XIII, pp. 822–823) decorrem diretamente da síntese comparativa apresentada e reconhecem explicitamente as limitações de escopo da busca realizada (como a restrição a veículos específicos e a necessidade futura de incluir literatura cinzenta).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
Este *survey* publicado no *IEEE Transactions on Services Computing* oferece uma sistematização ampla das técnicas de Análise de Causa Raiz (RCA) em arquiteturas de microsserviços e multi-serviço (2017–2025), organizando a literatura por modalidade de telemetria (*logs*, *traces*, métricas, relatórios de *bugs* e métodos híbridos), além de catalogar *datasets*, ferramentas de APM e métricas de avaliação (`Top@N`, `MRR`, `MAP`, `AC@k`). Embora a discussão sobre agentes baseados em LLMs seja reduzida (Seção VII, p. 815), o estudo documenta gargalos práticos cruciais — como a taxa de resolução de apenas 11,3% do melhor agente LLM no benchmark *OpenRCA* [66], restrições de janela de contexto e alucinações — e traça uma agenda de pesquisa convergente com arquiteturas agênticas multimodais e causais (Seção XII, pp. 822–823).

### Recomendação
**INCLUIR COM RESSALVAS** — Embora apresente `SCORE_RQ = 2.5/5.0` devido ao foco secundário em *Agentic AI* propriamente dita, possui qualidade global Alta (`SCORE_QA = 3.0/4.0`) e alto valor instrumental como referência de contextualização na RSL para fundamentar: (i) a taxonomia de fontes de observabilidade em RCA; (ii) o catálogo de *datasets* e *benchmarks* (*TrainTicket*, *Sock Shop*, *OpenRCA*); (iii) a padronização das métricas de avaliação de diagnóstico (`Top@N`, `MRR`); e (iv) as limitações atuais de agentes LLM puros frente a falhas complexas em produção (RQ4/RQ5).

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Google Scholar*, *Scopus* ou *IEEE Xplore* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *IEEE Transactions on Services Computing* no portal *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A1` na *Plataforma Sucupira / Qualis CAPES* vigente (`[VERIFICAR]`).
