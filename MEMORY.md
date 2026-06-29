# MEMORY.md — Registro da sessão

Memória da sessão de trabalho assistida (Claude Code) sobre a RSL **"Agentic AI Copilot para Resposta a Incidentes"** (PPGCA · Unisinos · Trabalho II). Registra os **prompts do usuário**, as **interações** e as **respostas/ações** realizadas, em ordem cronológica.

- **Período:** 2026-06-28 → 2026-06-29
- **Repositório:** `valdomirosouza/Unisinos-Mestrado-TrabalhoII` (privado, GitHub) · branch `master`
- **Escopo:** geração dos prompts de avaliação, execução dos pareceres dos 20 estudos candidatos (P20–P40, sem P36), consolidação de resultados, gráficos, relatório/PDF, dashboard, índices e comparação entre avaliadores.

---

## Linha do tempo (prompts → respostas/ações)

### 1. Criar os prompts com `# INSUMOS`

**Prompt:** "Read the prompt-template and Artigos-TrabalhoII.csv and create a prompt for each article, and fill `# INSUMOS` in each new prompt using the data in the CSV."
**Ações:** Li `prompt-template.md` e `Artigos-TrabalhoII.csv`. Gerei `prompts/prompt-P20.md … P40.md` (21 arquivos), cada um com o template completo e o bloco `# INSUMOS` preenchido (ID, Artigo, Arquivo, qualis, sjr_quartile). Títulos legíveis derivados; nomes crípticos marcados `[VERIFICAR]`. Sinalizei a duplicata P36 = P31 e o caso A3 (P39/P40).

### 2. Extrair títulos reais dos arquivos crípticos

**Prompt:** "extract the real titles for the cryptic filenames on folder docs."
**Ações:** `pdftoppm`/poppler indisponível; extraí via `mdls` (metadados) e, onde nulo (P25, P33), via PDFKit (JXA). Atualizei o gerador e regenerei os prompts com os títulos reais.

### 3–6. Remoção da duplicata P36 e verificação

- **"remove the duplicate P36 prompt"** → removi `prompts/prompt-P36.md`.
- **"yes, delete the P36 row from the CSV too"** → removi a linha P36 do CSV; corrigi a fusão acidental P35/P37.
- **"regenerate the prompts to confirm P36 is gone"** → regenerei: 20 prompts (P20–P35, P37–P40).
- **"open prompt-P37.md to verify the content"** → conferido (INSUMOS correto).

### 7–12. Execução dos pareceres P20–P25

**Prompt (repetido):** "run the Pxx prompt on its PDF."
**Método estabelecido:** extração de texto do PDF via PDFKit (JXA), leitura integral, e produção do parecer no formato do template (Tabela A bibliométrica, Tabela B RQs T/P/N, Tabela C QA Y/P/N, parecer final).

- **P20** — LLM Agentic Workflow (IaC) · RQ 4,0 · QA 3,0 · Alta · **Incluir c/ ressalvas**.
- **P21** — SLM Agent ICT Ops · RQ 4,5 · QA 4,0 · Alta · **Incluir**.
- **P22** — ARM Autonomous Remediation · RQ 4,5 · QA 4,0 · Alta · **Incluir** (mais aderente a IR até então).
- **P23** — TAMO (RCA) · RQ 3,5 · QA 3,5 · Alta · **Incluir c/ ressalvas** (agêntico limitado).
- **P24** — AgentAI Survey (Industry 4.0) · RQ 4,0 · QA 2,5 · Média · **Incluir c/ ressalvas (fundacional)** — survey/secundário.
- **P25** — AI-Driven MAS (cyber range) · RQ 4,5 · QA 4,0 · Alta · **Incluir** (MAS/RL, não-LLM).

### 13. Criar um arquivo markdown por artigo

**Prompt:** "Create a markdown file per article with the results of each one."
**Ações:** Criei `reviews/review-P20.md … review-P25.md` com os pareceres completos.

### 14–25. Execução dos pareceres P26–P40

(alguns pares processados juntos por mensagens enviadas durante o trabalho)

- **P26** — Surveying RCA (survey) · RQ 2,5 · QA 2,5 · Média · **Excluir** (secundário + não-agêntico).
- **P30** — LLM Inference Engine RCA · RQ 3,0 · QA 4,0 · Alta · **Excluir** (não-agêntico; bug-triage).
- **P27** — MA-RCA (LLM multi-agente) · RQ 4,5 · QA 4,0 · Alta · **Incluir**.
- **P28** — MAS Cybersecurity (LLM) · RQ 4,5 · QA 3,5 · Alta · **Incluir** (melhor fit SOC/IR; copilot).
- **P29** — AIOps Log Anomaly SLR · RQ 2,5 · QA 2,5 · Média · **Excluir** (SLR + não-agêntico).
- **P31** — LEMAD (LLM multi-agente, rede elétrica) · RQ 4,5 · QA 3,5 · Alta · **Incluir** (= ex-P36).
- **P32** — GALR (GNN+LLM agent) · RQ 4,0 · QA 3,5 · Alta · **Incluir c/ ressalvas** (recuperação offline).
- **P33** — Review of Agentic AI in Cyber (narrativa) · RQ 4,0 · QA 2,5 · Média · **Incluir c/ ressalvas (fundacional)**.
- **P34** — LLMs in IR management (copilot) · RQ 4,0 · QA 4,0 · Alta · **Incluir c/ ressalvas** (IR puro, não-agêntico).
- **P35** — Graph-Augmented Multi-Agent RCA · RQ 4,0 · QA 4,0 · Alta · **Incluir** (t-tests, rigoroso).
- **P37** — AI Trust & Framework Readiness (survey de percepção) · RQ 3,0 · QA 4,0 · Alta · **Incluir c/ ressalvas**.
- **P38** — Multi-Agent vs RAG (agricultura) · RQ 3,5 · QA 4,0 · Alta · **Excluir (domínio)** — fora de IR.
- **P39** — Agentic AI and the Cyber Arms Race (opinião) · **INELEGÍVEL (Qualis A3)** · **Excluir**.
- **P40** — LLM-Based Network Mgmt Survey · **INELEGÍVEL (Qualis A3)** · **Excluir**.

Cada parecer foi salvo em `reviews/review-Pxx.md`.

### 26–28. Versionamento inicial

- **"sim, faça o commit"** → `git init`, `.gitignore` (.DS_Store), 1º commit com prompts + PDFs + CSV; depois commit dos 20 pareceres.
- **"gere o reviews/README.md consolidado e commite"** → criei o índice/tabela-síntese; corrigi a contagem (14 Incluir).
- **"push it"** → criado repositório **privado** no GitHub via `gh` (decisão do usuário: criar repo + privado com PDFs) e push.

### 29. CSV consolidado

**Prompt:** "create a consolidated results CSV with all scores."
**Ações:** `reviews/resultados-consolidados.csv` (20×23): RQ1-5, SCORE_RQ, QA1-4, SCORE_QA, banda, elegibilidade, recomendação + bibliometria. Validado.

### 30. Relatório de síntese

**Prompt:** "generate a synthesis report from the consolidated CSV."
**Ações:** Calculei estatísticas e escrevi `reviews/relatorio-sintese.md` (funil, cobertura por RQ, qualidade, ranking, taxonomia, achados, exclusões, limitações, próximos passos). **Achado central: lacuna de RQ4 (ética/governança) — só 4/18 plenas.**

### 31–33. Gráficos, embutir no relatório, PDF

- **"add a charts/visualizations of the scores"** → 5 gráficos **SVG** (sem dependências) + galeria `graficos.md`. Iteração visual (Quick Look) corrigindo margens/legendas; scatter trocado por **mapa em grade** (empates).
- **"add the charts to the synthesis report"** → embutidos nas seções relevantes.
- **"generate a PDF of the synthesis report"** → conversor Markdown→HTML próprio (SVGs em base64) + **Chrome headless** `--print-to-pdf`; `reviews/relatorio-sintese.pdf` (8 páginas). Corrigido bug de detecção de tabela (`:-:`).

### 34. Versionar os geradores

**Prompt:** "versione o script gerador em reviews/."
**Ações:** `reviews/scripts/gen_charts.py` e `build_pdf.py` com caminhos relativos (`__file__`), `build_pdf.py` completo (md→html→pdf, autodetecta Chrome), + `scripts/README.md`. Reprodutibilidade verificada (SVGs byte-idênticos).

### 35. Dashboard + How-to + README raiz

**Prompt:** "add a results dashboard linking all artifacts and create a How to create the charts. After that create a README on the root folder with the links and index to all documents."
**Ações:** `reviews/DASHBOARD.md` (hub), `reviews/COMO-CRIAR-GRAFICOS.md` (how-to), `README.md` (raiz, índice completo com links parecer/prompt/PDF por estudo, PDFs com encoding correto). Detectada e versionada a pasta `reviews/ChatGPT/` (avaliações comparativas). 146 links validados.

### 36. Completar conjunto ChatGPT

**Prompt:** "I added some new files on folder reviews/ChatGPT, commit these ones."
**Ações:** Commit dos 8 novos (P32–P40); conjunto ChatGPT completo (20). Atualizei referências "P20–P31" → "P20–P40".

### 37. Comparar os dois conjuntos de avaliadores

**Prompt:** "compare the two evaluator sets."
**Ações:** `reviews/scripts/gen_comparison.py` extrai escores do ChatGPT e cruza com o CSV do Claude → `comparacao-avaliadores.{md,csv}` + `charts/chart-comparacao.svg`.
**Resultado:** **acordo de decisão 90%** (18/20), **Cohen's κ = 0,74** (substancial), **banda 100%**, erro abs. médio SCORE_RQ 0,42 / SCORE_QA 0,31; **RQ4 e RQ5 com 100% de acordo**. Únicas divergências: **P26 e P29** (surveys/SLR — ChatGPT inclui c/ ressalvas, Claude exclui). ChatGPT é mais conservador em QA e rotula quase tudo "com ressalvas".

### 38–39. Integrar a comparação

- **"add the comparison chart to the synthesis report"** → nova **§9 Confiabilidade entre avaliadores** com o gráfico; renumeração; PDF regenerado (6 gráficos).
- **"add the comparison metrics to the dashboard"** → tabela de métricas + gráfico no dashboard + linha de navegação.

### 40. Esta memória

**Prompt:** "Save the entire memory of this session including Prompts, Interactions and answers on the file MEMORY.md. After that commit all changes and push."
**Ações:** Este arquivo; commit e push.

---

## Decisões e convenções estabelecidas

- **Eixo de decisão:** _agêntico × domínio-IR_. Incluídos = agênticos **e** próximos de IR/AIOps/SOC; excluídos = não-agênticos (P26/P29/P30), off-domain (P38) ou inelegíveis (P39/P40).
- **Qualis A3 (P39/P40):** tratado como **inelegível** na ETAPA 1 (Claude encerra na triagem); ChatGPT avaliou e depois excluiu.
- **Estudos secundários (P24/P33):** incluídos como **fundacionais** (condicional ao protocolo) — único ponto de protocolo em aberto.
- **Pendência transversal:** Citações/SJR/Qualis não verificáveis nos PDFs → toda elegibilidade dependente disso é provisória.
- **Antifabricação:** dados não verificáveis marcados `[VERIFICAR]`; classificações ancoradas em evidência do PDF.
- **Ferramentas:** extração de PDF via PDFKit (JXA); gráficos SVG à mão (sem matplotlib); PDF via Chrome headless (sem pandoc/LaTeX). Repositório **privado** (PDFs com copyright).

## Resultado quantitativo

20 estudos · 18 avaliados + 2 inelegíveis · **14 Incluir** (7 plenos + 5 ressalvas + 2 fundacionais) · **4 Excluir** (relevância/domínio) · **2 Inelegíveis** · SCORE_RQ médio **3,83** · SCORE_QA médio **3,50** · 14 Banda Alta.

## Artefatos produzidos (em `reviews/`, salvo indicado)

- `review-P20.md … P40.md` (20 pareceres) · `README.md` (índice) · `DASHBOARD.md` (hub)
- `resultados-consolidados.csv` · `relatorio-sintese.md` / `.pdf`
- `graficos.md` · `charts/*.svg` (6 gráficos) · `COMO-CRIAR-GRAFICOS.md`
- `comparacao-avaliadores.md` / `.csv` · `ChatGPT/Pxx_avaliacao_RSL.md` (20)
- `scripts/` (`gen_charts.py`, `build_pdf.py`, `gen_comparison.py`, `README.md`)
- Raiz: `README.md`, `MEMORY.md`, `prompt-template.md`, `Artigos-TrabalhoII.csv`, `prompts/`, `docs/`

## Histórico de commits

| Hash      | Data       | Mensagem                                                     |
| --------- | ---------- | ------------------------------------------------------------ |
| `de28b59` | 2026-06-28 | Add RSL evaluation prompts for candidate articles P20-P40    |
| `3d9f94c` | 2026-06-28 | Add RSL reviewer evaluations for candidate studies P20-P40   |
| `a53f900` | 2026-06-28 | Add consolidated reviews/README.md synthesis index           |
| `3264b3f` | 2026-06-28 | Add consolidated results CSV with all RSL scores (P20-P40)   |
| `5923f36` | 2026-06-28 | Add synthesis report from consolidated RSL results           |
| `993e4a3` | 2026-06-28 | Add SVG charts/visualizations of RSL scores                  |
| `1e277c6` | 2026-06-28 | Embed score charts into the synthesis report                 |
| `2ea45ee` | 2026-06-28 | Add PDF export of the synthesis report                       |
| `405b738` | 2026-06-28 | Version the artifact generators under reviews/scripts/       |
| `8a8c936` | 2026-06-29 | Add root README index, results dashboard, and charts how-to  |
| `de6bdec` | 2026-06-29 | Complete ChatGPT comparison set (P32-P40)                    |
| `65f7c4a` | 2026-06-29 | Add inter-evaluator comparison (Claude vs ChatGPT)           |
| `d52dee3` | 2026-06-29 | Add inter-evaluator comparison chart to the synthesis report |
| `b4ca724` | 2026-06-29 | Surface inter-evaluator comparison metrics on the dashboard  |

_(Este commit de MEMORY.md é acrescentado ao final do histórico.)_
