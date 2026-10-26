# Avaliação Sistemática de Estudo Primário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P34
- **Título:** *Analysing the role of LLMs in cybersecurity incident management*
- **Autores:** Gavin Jones; Dimitrios Kasimatis; Nikolaos Pitropakis; Richard Macfarlane; William J. Buchanan
- **Periódico/Conferência:** *International Journal of Information Security* (Springer), Vol. 24, Artigo 228, pp. 1–14 (Publicado online em 30 de outubro de 2025)
- **DOI:** `10.1007/s10207-025-01144-7`
- **Arquivo avaliado:** `P34-A2-s10207-025-01144-7.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Artigo de pesquisa empírica/experimental (*Regular Contribution*), avaliando quantitativa e qualitativamente quatro Grandes Modelos de Linguagem da OpenAI (`gpt-3.5-turbo`, `gpt-4-0125-preview`, `gpt-4o` e `o1-preview`) como assistentes/copilotos de resposta a incidentes ao longo de 10 cenários reais mapeados no ciclo de vida do NIST SP 800-61 sob três níveis de contexto (totalizando 1.200 invocações de modelo).
- **Foco técnico:** Eficácia prática de diferentes perfis de LLMs (modelos otimizados para velocidade/interatividade vs. modelos de raciocínio *chain-of-thought*) nas fases de preparação, detecção/análise, contenção, erradicação, recuperação e análise pós-incidente, acompanhada de uma análise aprofundada de ética, governança regulatória (*EU AI Act*) e mitigação de riscos operacionais.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Atendido. Desenvolve e avalia experimentalmente um assistente/copiloto de resposta a incidentes baseado em LLMs (*"incident response assistant or copilot"*, Seção 4.1, p. 4) frente a 10 cenários de incidentes cibernéticos estruturados segundo o guia NIST SP 800-61.
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico *International Journal of Information Security*, Vol. 24, outubro de 2025).
  - *IC3 (Rigor técnico/metodológico):* Atendido (1.200 execuções experimentais avaliadas por 3 métricas de PLN e 4 rubricas *LLM-as-a-judge* reportadas integralmente no Apêndice A).
- **Critérios de Exclusão (EC):** Não incide em critério de exclusão, embora o protótipo avalie chamadas diretas de API em três níveis de contexto (*Zero-shot*, *Runbook NIST* e *Runbook + Caso Histórico*) sem orquestração multiagente autônoma.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P34 | International Journal of Information Security | 2025 | [VERIFICAR] | Q2 [VERIFICAR] | A2 [VERIFICAR] | Artigo Experimental / Empírico (Primário) | `10.1007/s10207-025-01144-7` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q2`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF e devem ser verificados em fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P34 | Analysing the role of LLMs in cybersecurity incident management | **RQ1** (Contexto e Definições) | Parcialmente Respondida | **P** (0.5) | Seção 3 (pp. 3–4); Seção 4.1 (pp. 4–5); Seção 6 (p. 10); Seção 6.1.1 (p. 11) | **(a) Definição de autonomia:** Posiciona o sistema como um copiloto consultivo (*incident response assistant or copilot*, p. 4) e recomenda na Seção 6.1.1 (p. 11) operação *human-in-the-loop* com aprovação de analista para ações de alto impacto, controle duplo (*dual control*) para passos irreversíveis, abstenção abaixo de limiar de confiança e implantação gradual em modos *shadow* e *advisory*. **(b) Características centrais:** Discute sistemas multiagentes na revisão de literatura (ex.: *AutoBnB* de Liu Z. [26], p. 3), mas o artefato próprio avaliado realiza *prompting* em passo único sob 3 níveis de contexto (sem memória dinâmica ou uso autônomo de ferramentas). **(c) Modelo decisório:** Distingue o papel decisório de modelos rápidos (`GPT-4o`, `GPT-3.5`) para contenção/erradicação em tempo real versus modelos de raciocínio *chain-of-thought* (`o1-preview`, `GPT-4`) para preparação e análise pós-incidente no ciclo NIST SP 800-61 (p. 10). |
| P34 | Analysing the role of LLMs in cybersecurity incident management | **RQ2** (Arquitetura de Engenharia) | Parcialmente Respondida | **P** (0.5) | Seções 4.1, 4.2 e 4.3 (pp. 4–8); Seção 6.1.1 (p. 11) | **(a) Tipo de arquitetura:** Arquitetura experimental cliente-servidor (Seção 4.2.1, pp. 5–6) que lê cenários de incidentes em JSON, aplica um *prompt wrapper* estruturado pelo framework **CLEAR** [28] em 3 níveis (Nível 1: *Zero-shot*; Nível 2: *Runbook* NIST SP 800-61; Nível 3: *Runbook* + histórico de incidente prévio) e consulta a API OpenAI. **(b) Ferramentas/frameworks:** Avalia `gpt-3.5-turbo`, `gpt-4-0125-preview`, `gpt-4o` e `o1-preview`; emprega `BERTScore` [29], biblioteca `spaCy` (tokenização e *POS tagging*) e avaliação **LLM-as-a-judge** [32]. **(c) Capacidades avançadas:** Não implementa RAG ou *tool calling* no experimento, mas especifica na Seção 6.1.1 (p. 11) *guardrails* de engenharia para produção: *model version pinning*, trilhas completas de auditoria de *prompts*/contexto/ações, segregação de funções, privilégio mínimo e inferência *on-premise*. |
| P34 | Analysing the role of LLMs in cybersecurity incident management | **RQ3** (Benefícios e Evidências) | Respondida Plenamente | **T** (1.0) | Seção 5, Figuras 1–7 (pp. 8–10); Seção 6 (p. 10); Apêndice A, Tabela 1 (p. 12) | **(a) Benefícios qualitativos:** Identifica complementaridade funcional entre LLMs: `GPT-4o` e `GPT-3.5` entregam alta clareza, consistência e coesão textual para tarefas urgentes de contenção, isolamento e recuperação, enquanto `o1-preview` e `GPT-4` entregam superior coerência lógica, concisão e terminologia técnica para preparação, avaliação de vulnerabilidades, RCA pós-incidente e treinamento (p. 10). **(b) Benefícios quantitativos:** Executa **1.200 invocações** (10 cenários $\times$ 4 modelos $\times$ 3 níveis $\times$ 10 repetições, Tabela 1, p. 12): *BERTScore* liderado por `GPT-3.5` (`0.4201–0.4938`) e `GPT-4o` (`0.3568–0.3820`); *Conciseness* (palavras/frase via `spaCy`) liderada por `GPT-4` (`14.696–16.168`) e `o1-preview` (`15.976–17.402`); *Coherence* (`spaCy`) liderada por `GPT-4o` (`26.801–27.605`) e `GPT-3.5` (`26.810–27.514`). Nas métricas *LLM-as-a-judge* (1–10): `GPT-4o` lidera *Clarity* (`8.92–9.04`), enquanto `o1-preview` e `GPT-4` lideram *Relevance* (`9.1483` no `o1` Stage 1), *Domain-Specific Terminology* (`9.2432` no `o1` Stage 2) e *Logical Coherence* (`8.625` no `o1` Stage 1 vs. `7.80–7.88` do `GPT-3.5`). **(c) Nível de evidência:** Avaliação experimental controlada com 1.200 execuções. |
| P34 | Analysing the role of LLMs in cybersecurity incident management | **RQ4** (Desafios e Ética) | Respondida Plenamente | **T** (1.0) | Seção 2.2 (p. 3); Seção 6, 6.1 e 6.1.1 (pp. 10–11) | **(a) Desafios técnicos:** Restrições de janela de tokens (exigindo *chunking*), alucinações e natureza probabilística dos LLMs, sensibilidade a *temperature*/*top-p* e limitações de um único modelo juiz (pp. 3, 10–11). **(b) Desafios éticos/governança:** Discussão ética exemplar na Seção 6.1 (p. 11): (1) risco de analistas juniores agirem com confiança em respostas concisas porém logicamente falhas (`GPT-3.5`) sem cadeia de *accountability*; (2) risco de modelos altamente coerentes induzirem falsa sensação de segurança, rebaixando padrões de contratação/treinamento e causando **erosão de perícia humana e pensamento crítico**; (3) uso malicioso por atacantes; e (4) análise frente ao *GDPR*, *Cyber Resilience Act*, Diretiva *NIS* e **EU AI Act (2024)**. **(c) Mecanismos de governança:** Propõe na Seção 6.1.1 (p. 11) aprovação *human-in-the-loop*, controle duplo, escores de confiança com abstenção, proveniência obrigatória, modos *shadow*/*advisory*, exercícios regulares sem IA para manter a perícia humana, *version pinning*, logs de auditoria, segregação de funções, *red teaming* e inferência privada/*on-premise* com redação de dados. |
| P34 | Analysing the role of LLMs in cybersecurity incident management | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção 7 (*Conclusion*, p. 12) | Aponta quatro direções futuras explícitas para pesquisa em copilotos de resposta a incidentes (p. 12): (1) avaliação de modelos generativos alternativos, incluindo modelos hospedados localmente (*locally hosted alternatives*); (2) experimentação com arquiteturas RAG e métodos de consulta iterativa (*iterative query methods*) para elevar a precisão; (3) investigação de formatos de entrada variados com interações manuais humanas ao vivo para replicar condições operacionais realistas; e (4) incorporação de métricas quantitativas de desempenho operacional (como tempo médio de resposta — *mean response time*) e avaliação qualitativa de usabilidade com *runbooks* customizados. |
| **P34** | **SCORE_RQ Total** | — | **4.0 / 5.0** | — | — | Atende plenamente RQ3 (1.0), RQ4 (1.0) e RQ5 (1.0), e parcialmente RQ1 (0.5) e RQ2 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P34 | Artigo Experimental / Empírico (Primário) | P (0.5) | P (0.5) | Y (1.0) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Objetivos Claros (P = 0.5):** O objetivo de avaliar a aplicabilidade prática de LLMs ao longo das fases de resposta a incidentes (NIST SP 800-61) e discutir suas implicações éticas e de *accountability* é claro (Seção 1, pp. 1–2). Recebe pontuação parcial porque o protótipo avaliado opera via *prompting* direto em passo único sobre modelos da OpenAI, sem implementar agentes autônomos com memória ou execução de ferramentas.
- **QA2 — Metodologia Replicável (P = 0.5):** Explicita os quatro modelos e suas datas de corte, os três níveis de contexto, o *prompt wrapper* CLEAR, o *prompt* e as escalas detalhadas (1–10) do avaliador *LLM-as-a-judge* (Seção 4, pp. 4–8), além de fornecer a tabela consolidada de métricas no Apêndice A (p. 12). Contudo, apresenta limitações de replicabilidade e revisão: (i) não publica a lista completa dos 10 cenários nem as respostas de referência (fazendo referência na p. 5 a uma inexistente *"section 3.3.4"*); (ii) utiliza o próprio `GPT-4o` como juiz único para avaliar respostas do `GPT-4o` (potencial viés de auto-avaliação, reconhecido na p. 10); e (iii) no texto da Seção 5.1.1 (p. 8), reporta os valores de *BERTScore* multiplicados por 10 ("4.9", "3.7", "3.3", "3.2"), divergindo da escala real `0–1` mostrada na Figura 1 e na Tabela 1 (`0.4938`, `0.382`, `0.3394`, `0.3326`).
- **QA3 — Base de Evidências Sólidas (Y = 1.0):** Conduz um experimento sistemático de 1.200 invocações (10 cenários cobrindo DDoS, vazamento em S3, *insider threat*, *ransomware* e aplicação web $\times$ 4 modelos $\times$ 3 estágios de contexto $\times$ 10 repetições), combinando métricas objetivas de PLN (`BERTScore` e `spaCy`) com quatro dimensões qualitativas estruturadas (Tabela 1, p. 12).
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões sobre a adequação de cada classe de modelo às diferentes fases do ciclo de resposta a incidentes são bem fundamentadas nos resultados empíricos, e o artigo discute de forma exemplar as limitações metodológicas e os riscos éticos/organizacionais (Seções 6 e 7, pp. 10–12).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
Este estudo avalia empiricamente quatro modelos OpenAI (`GPT-3.5-turbo`, `GPT-4`, `GPT-4o` e `o1-preview`) em 1.200 execuções ao longo de 10 cenários de resposta a incidentes estruturados pelo guia NIST SP 800-61 sob três níveis de contexto (*zero-shot*, *runbook* geral e *runbook* + histórico). Os resultados demonstram uma divisão clara de especialização: modelos ágeis (`GPT-4o`, `GPT-3.5`) destacam-se em clareza e consistência para contenção, isolamento e recuperação em tempo real, enquanto modelos com raciocínio *chain-of-thought* (`o1-preview`, `GPT-4`) são superiores em coerência lógica, concisão e terminologia técnica para preparação, RCA pós-incidente e avaliação de vulnerabilidades. Adicionalmente, as Seções 6.1 e 6.1.1 oferecem uma contribuição notável sobre ética, erosão de habilidades humanas (*deskilling*), conformidade com o *EU AI Act* e mecanismos de governança (*human-in-the-loop*, *dual control*, *shadow/advisory modes*).

### Recomendação
**INCLUIR COM RESSALVAS** — O artigo atinge `SCORE_RQ = 4.0/5.0` e `SCORE_QA = 3.0/4.0` (Banda Alta). Embora o experimento avalie LLMs via *prompting* estático em vez de agentes autônomos multi-etapa, sua inclusão na RSL é fortemente recomendada por duas contribuições diretas: (1) evidência quantitativa sobre a seleção de modelos de linguagem (rápidos vs. *reasoning* `o1`) conforme a fase do incidente (tempo real vs. pós-incidente) e o impacto da injeção de *runbooks* NIST; e (2) um conjunto completo de recomendações de governança e mitigação de risco operacional para copilotos de resposta a incidentes (RQ3, RQ4 e RQ5).

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q2` para *International Journal of Information Security* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
