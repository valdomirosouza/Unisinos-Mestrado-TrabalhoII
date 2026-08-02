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

---

# Sessão 2026-07-22 → 2026-08-02 — Etapas 3 e 4: Extração de dados (fichas P01–P40), PICOC e evolução do protocolo

Sessão dedicada à **extração estruturada** dos 39 artigos do corpus (`docs/`, P01–P35 + P37–P40) em fichas CSV, versões pt-BR, relatórios consolidados, versionamento e fechamento de lacunas de documentação.

## Linha do tempo (prompts → respostas/ações)

### 41. Extração dos 39 PDFs em fichas CSV

**Prompt:** "load the paper-extraction-prompt-template.md, reasoning about and read one by one of the PDF Articles on folder ../docs/ … and write the .csv report file for each one in this folder."
**Ações:** Li `report/paper-extraction-prompt-template.md` (schema Kitchenham de 11 campos: bibliometria, problema, solução/papel da Agentic AI, metodologia, impacto MTTD/MTTR, impacto Agentic AI/MAS, limitações, relevância, pontuação). **Fan-out de 39 subagentes** (um por PDF, em 4 lotes), cada um lendo o PDF integral em blocos de 20 páginas e gravando `report/Pxx-extraction.csv` (RFC 4180, 11 campos + Paper ID, âncoras de evidência nos campos 4–9). Validação estrutural via script: 39/39 OK.
**Resultado:** Distribuição de relevância: **2 High** (P22 ARM, P37 AI Trust) · **26 Medium** · **11 Low**. Flags de ambiguidade registradas em P02 (metodologia) e P18 (contagens divergentes). _Nota: docs/ tem 39 PDFs (P36 não existe — duplicata removida)._

### 42. Versões pt-BR das fichas

**Prompt:** "Create a version in pt_BR of each extration file, but keep the Technical words/terms and acronym in english."
**Ações:** 8 subagentes de tradução (~5 arquivos cada) → `Pxx-extraction-ptBR.csv`: prosa em pt-BR acadêmico; termos técnicos/acrônimos (MTTD, MTTR, Agentic AI, LLM, AIOps, RCA…), títulos, autores, veículos, citações verbatim e âncoras mantidos em inglês; rótulos de campo traduzidos (Campo/Extração, Título…); High/Medium/Low → Alta/Média/Baixa.
**Incidente:** os 8 agentes foram interrompidos pelo **limite de sessão** (21/39 arquivos gravados). Após o reset, relancei 4 agentes cobrindo apenas os 18 faltantes. Validação final: 39/39 OK, sem truncamentos.

### 43. Relatório consolidado

**Prompt:** "Create a consolidated .csv report with all papers in one file"
**Ações:** Pivot das fichas (Field/Extraction → colunas) em `report/consolidated-extraction.csv` (EN) e `consolidated-extraction-ptBR.csv` — 39 linhas × 12 colunas (Paper ID + 11 campos), validados e entregues ao usuário.

### 44–47. Versionamento completo

- **"Commit all the report files"** → commit dos 81 arquivos de `report/` (template + 39 EN + 39 pt-BR + 2 consolidados).
- **"Commit the docs/ PDFs and referencias.csv too"** → descoberto que P20–P40 já estavam versionados; commit dos 19 PDFs P01–P19 + `referencias.csv`.
- **"Commit DOIS.py and DOIS.txt too"** → inspecionei e commitei o script de extração de referências (Crossref/OpenAlex/Semantic Scholar/OpenCitations) e a lista de 39 DOIs.
- **"Add .serena/ to .gitignore"** → adicionado ao `.gitignore` existente; árvore limpa.
- **"Push everything to the remote"** → push de 4 commits para `origin/master`.

### 48. Auditoria de documentação

**Prompt:** "Chech all .md files and documentation inserted in each one to check if all files added in the foldes /docs /reports /reviews /prompts are indexed and cited in this .md files."
**Ações:** Script de cobertura cruzando os 199 arquivos das 4 pastas contra todos os `.md` do repo. **Resultado: 79 citados / 120 não indexados** — (1) `report/` inteiro (81 arquivos) ausente de qualquer .md; (2) PDFs P01–P19 de `docs/` sem índice (README dizia "20 PDFs"); (3) os 20 `reviews/ChatGPT/Pxx_avaliacao_RSL.md` citados só como pasta.

### 49. Fechamento das lacunas + commit/push

**Prompt:** "Yes, update the documentation to close these gaps" → "Yes, commit and push"
**Ações:** (1) **Novo `report/README.md`** — tabela P01–P40 ligando PDF, extração EN, extração pt-BR e relevância (indexa também os 39 PDFs); (2) **README raiz** — linha na tabela "Comece por aqui", `report/` (Etapa 3) + `referencias.csv` + `DOIS.py/txt` no diagrama de estrutura, docs/ corrigido para 39 PDFs, nova seção "Extração de dados (Etapa 3)"; (3) **`reviews/README.md`** — seção "Avaliações comparativas (ChatGPT)" com link por estudo. Re-verificação: **200/200 arquivos citados, 0 links quebrados**. Commit + push.

### 50. Esta memória

**Prompt:** "Update MEMORY.md with this session's work" → esta seção; commit e push na sequência (`94a0037`).

### 51. papers.csv — bibliometria verificada (resolve a pendência Qualis/SJR)

**Prompt:** "read the file papers.csv in the root folder and add it the documentation to solve the gap cited in the README.md '⚠️ Pendência transversal…'" → "Yes, commit and push"
**Ações:** Li `papers.csv` (criado pelo usuário na raiz): **bibliometria verificada dos 39 estudos P01–P40** — DOI, veículo, **Qualis 2025-2028**, **percentil Scopus**, **SJR quartile**, ISSN e ano. Cross-check: os 39 estratos Qualis batem com os códigos `A1/A2/A3` dos nomes de arquivo em `docs/`, confirmando a inelegibilidade de P39/P40 (A3). Atualizei a documentação: (1) README raiz — nota ⚠️→✅ ("Pendência transversal **resolvida para Qualis/SJR** via `papers.csv`; só a **contagem de citações** segue pendente"), `papers.csv` no diagrama de estrutura e bullet próprio em "Insumos"; (2) `reviews/README.md` — nota equivalente, com alerta de citações para os estudos de 2026 (P30/P32/P35/P37). **Intocados de propósito:** `relatorio-sintese.md`/`.pdf` e avaliações ChatGPT (artefatos históricos da avaliação, quando os valores eram de fato `[VERIFICAR]`). Verificação: `papers.csv` citado, 0 links quebrados. Commit + push.

### 52. Mendeley RIS → CSV e reposição de PDFs

**Prompts:** "convert the export.ris … to a CSV" → commits e remoção da duplicata → reposição intencional de PDFs.
**Ações:** Converti `export.ris` (38 registros Mendeley) em `export.csv` (14 colunas; AU/KW agregados; SP/EP → Pages), com **Paper ID casado por DOI** contra `papers.csv` — 38/38 casados; **P13 não tem registro no export do Mendeley** (gap sinalizado). Removida a duplicata `docs/export.ris`. Em seguida o usuário substituiu 4 PDFs do corpus (P04, P05, P12, P14) — commitados após confirmação (P04 individual; P05/P12/P14 em lote).

### 53. Extração PICOC (Etapa 4)

**Prompt:** "read the file picoc/picoc-extraction.md reasoning about and create a table with the results." → "Salve a tabela consolidada em picoc/picoc-results.md" → renomeações + commit.
**Ações:** Executei o prompt PICOC (Kitchenham; Petticrew & Roberts) sobre os **39 PDFs** com 39 subagentes (leitura integral, raciocínio com âncoras seção/página, regras antifabricação `NÃO DECLARADO`/`N/A`). Limite de sessão interrompeu 7 agentes; relancei só os faltantes (32 fragmentos preservados). Consolidei em tabela (39×8) + síntese transversal + apêndice de raciocínio por artigo. **Achado central: nenhum estudo mede MTTD/MTTR nominalmente** (primários usam proxies; carga cognitiva nunca medida). Renomeado para `picoc-results-consolidated-P01-P40-Claude.md` (prompt → `picoc-extraction-prompt.md`); usuário adicionou versões **ChatGPT** e **Gemini**; pasta `picoc/` definida como **Etapa 4** no README raiz.

### 54. Comparação PICOC entre avaliadores

**Prompt:** "create the PICOC inter-evaluator comparison" → commit.
**Ações:** Normalizei os 3 consolidados em matriz de status por elemento (3 agentes) e computei acordo: **100% (κ=1,00)** em Population/Intervention/Outcomes/Context; **Comparison 82%, Cohen/Fleiss κ=0,42** — as 10 divergências são **definicionais** (fronteira do contraste conceitual em estudos secundários; ChatGPT permissivo, Gemini restritivo, Claude intermediário). Alertas: **Gemini não cobre P01–P09**; outcome de P14 no Gemini ("MTTR −30%") vem de claims de fornecedores. Os três avaliadores **triangulam a lacuna de MTTD/MTTR**. Recomendação de protocolo registrada (Comparison=DECLARED só com baseline empírico). Saídas: `picoc-comparacao-avaliadores.{md,csv}`.

### 55. Correção da cobertura do Gemini e recomputação da comparação PICOC

**Prompt:** "O arquivo picoc-results-consolidated-P01-P40-Gemini.md está incompleto e por conta disso publiquei uma nova versão … incluindo os artigos de P01 até P10 … aplique as atualizações nos demais arquivos." + "Atualize também o MEMORY.md com esta correção e commit"
**Ações:** O usuário publicou `picoc-results-consolidated-P01-P40-Gemini-Atualizado.md` (39 artigos, corrigindo a ausência de P01–P09). Re-normalizei o arquivo atualizado (status por elemento) e **recomputei a comparação sobre os 39 artigos**: Population/Intervention/Outcomes/Context seguem 100% (κ=1,00); **Comparison caiu para 79%, Fleiss κ=0,37** (era 82%/0,42 com 30 artigos) — os P01–P09 recém-incluídos adicionaram 4 divergências novas (P01, P03, P04, P08), total 12, todas definicionais. Pares: Claude×ChatGPT 0,42 · Claude×Gemini 0,47 · **ChatGPT×Gemini 0,22** (menor acordo). Atualizados `picoc-comparacao-avaliadores.{md,csv}` e o README raiz (aviso de cobertura removido; Atualizado como versão canônica; original mantido como registro histórico, seguindo a convenção de não reescrever artefatos).

### 56. Regra de protocolo aplicada — reclassificação dos 12 casos de Comparison

**Prompt:** "Aplique a regra de protocolo recomendada e reclassifique os 12 casos divergentes"
**Ações:** Formalizei a recomendação como **Regra 5 do prompt PICOC (v1.1.0)**: Comparison = DECLARED **somente com baseline empírico**; contraste conceitual/paradigmático → `N/A (contraste conceitual)`. Adjudiquei os 12 casos: **11 → N/A (contraste conceitual)** (P01, P03, P04, P08, P12, P15, P16, P17, P29, P33, P40 — todos secundários/conceituais) e **1 → DECLARED** (P18, única exceção: comparação experimental de componente ML vs. rule-based no caso AVL, Seç. 6.2.1, com ressalva de escopo). Distribuição final de Comparison (39 artigos): **26 DECLARED · 11 N/A conceitual · 2 N/A mapeamento** — classificação determinística registrada na coluna `Comparison_Final_Protocolo` do CSV. Atualizados: prompt (v1.1.0 + changelog), relatório de comparação (seção "Regra aplicada e reclassificação"), CSV e README raiz.

### 57. Coluna Comparison (PICOC v1.1.0) no índice das fichas

**Prompt:** "Atualize o report/README.md com a nova pontuação de Comparison"
**Ações:** Adicionei à tabela P01–P40 do `report/README.md` a coluna **"Comparison (PICOC v1.1.0)"** com o status adjudicado por artigo (✅ DECLARED ×26 · ⚪ N/A conceitual ×11 · ⚪ N/A mapeamento ×2), gerada programaticamente a partir da coluna `Comparison_Final_Protocolo` de `picoc/picoc-comparacao-avaliadores.csv` (consistência por construção), mais legenda com links para a regra de protocolo e o relatório de comparação. O índice das fichas passa a cruzar as duas dimensões de triagem: relevância (High/Medium/Low) × natureza da comparação (empírica vs. conceitual). Validação: 39 linhas, colunas corretas, 0 links quebrados.

### 58. String de busca da RSL derivada do PICOC e calibrada no corpus

**Prompt:** "Gere a string de busca da RSL a partir da síntese PICOC"
**Ações:** Derivei a string booleana dos blocos da síntese transversal PICOC — **Bloco A** (Intervention dominante: agentic AI, AI/LLM agents, multi-agent, copilots, L/SLMs) **AND Bloco B** (Contexts recorrentes: incident response, AIOps, SRE, RCA, anomaly detection, observability, microservices, cybersecurity…) — com filtros do protocolo (≥2020, inglês, peer-reviewed) e sintaxes para Scopus/WoS/IEEE/ACM. **Calibração empírica** via matching sobre título+abstract+keywords do `export.csv`: **recall 13/14 nos estudos incluídos**; os candidatos não recuperados (P26, P38, P39) são exatamente os excluídos/inelegíveis. Evidências registradas: (i) bloco Outcomes obrigatório recuperaria **1/38** — quantifica a lacuna de MTTD/MTTR e justifica o bloco como refinamento opcional; (ii) trade-off P24 documentado (recuperá-lo exigiria "autonomous system*", que captura AS/BGP em redes e degradaria a precisão). Saída: `picoc/picoc-search-string.md`, indexada no README raiz.

### 59. Validação externa da string de busca (OpenAlex; Scopus pendente de credencial)

**Prompt:** "Execute a string de busca no Scopus e valide o recall"
**Ações:** A API do Scopus exige chave institucional Elsevier (`401` sem credencial; nenhuma chave no ambiente) — execução no Scopus **pendente**. Como validação em base real, executei a query (blocos A×B, ≥2020) na **OpenAlex** com verificação por DOI artigo a artigo: **recall 13/14 nos incluídos** (única perda: P24, trade-off já documentado), **P26/P38/P39 (excluídos/inelegíveis) não recuperados** (comportamento desejável confirmado), **P13 recuperado** (não era testável na calibração local) e **volume ≈ 49.700 trabalhos** — a execução externa **replicou exatamente a calibração local**, validando o método. Documentei na Seção 5 do `picoc-search-string.md`: resultados, refinamentos de precisão (Bloco B em título; corte de `resilience`/`SOC`/`SRE`; `SUBJAREA(COMP)`) e os dois caminhos para o Scopus real (chave da API em dev.elsevier.com ou export CSV da interface para cruzamento com `papers.csv`). README raiz atualizado.

### 60. Execução da string no Scopus (API Elsevier) — recall validado

**Prompt:** usuário forneceu a chave da API Elsevier (mantida fora do repositório).
**Ações:** Executei a query no **Scopus Search API** com verificação por DOI. **Bug de sintaxe descoberto e documentado:** `TITLE-ABS-KEY((A) AND (B))` aninhado retorna falso-zero quando combinado com `DOI()`; a forma por bloco `TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B)` funciona e passou a ser a canônica na Seção 3. **Resultados:** recall **13/14 nos incluídos** (única perda: P24 — mesmo trade-off), excluídos/inelegíveis P26/P38/P39 não recuperados, P13 recuperado, **volume 12.783** (2020+, EN; ~4× menor que a OpenAlex). **As três validações convergem** (calibração local, OpenAlex, Scopus) — string validada na base primária do protocolo. Achado adicional: **P01 (F1000Research) não é indexado pelo Scopus** — limitação de cobertura da base, cobrir via OpenAlex/snowballing. Seções 5.1 e 6 do `picoc-search-string.md` e README raiz atualizados.

### 61. Diagrama PRISMA 2020 do fluxo de seleção

**Prompt:** "Monte o diagrama PRISMA com todos os critérios de inclusão, exclusão e quantidade de artigos."
**Ações:** Criei `reviews/PRISMA.md` (Mermaid, formato PRISMA 2020 adaptado para atualização de revisão): **≈51 registros** identificados via busca assistida por IA (Gemini ≈20, Claude 16, ChatGPT 15) → **21 candidatos** pós-deduplicação/verificação → −1 duplicata interna (P36=P31) → **20 triados** → −2 inelegíveis (Qualis A3: P39/P40) → **18 avaliados na íntegra** → −4 excluídos com razões (P26/P29/P30 não-agênticos; P38 fora de domínio) → **14 incluídos** (7 plenos + 5 ressalvas + 2 fundacionais condicionais) + 19 do corpus prévio (Trabalho I) = **corpus final 33**. Critérios tabelados: I1–I6 (ano, veículo peer-reviewed, Qualis A1–A2, SJR Q1–Q2, citações ≥1 c/ `RECENCY_EXCEPTION`, aderência agêntica×IR) e E1–E5, cada um com ponteiro para o artefato de verificação. Indexado no README raiz.

### 62. Contagem de citações por estudo — pendência transversal FECHADA

**Prompt:** "faça a busca a computação da contagem total de citações por estudo."
**Ações:** Busquei as citações dos 39 artigos em **três fontes** (OpenAlex `cited_by_count`, Crossref `is-referenced-by-count`, Scopus `citedby-count` via API) e gravei em 4 novas colunas do `papers.csv` (+ data de verificação 2026-07-27). **Critério "Citações ≥ 1" verificado para todos os 14 incluídos** — única exceção: **P35 (0 nas três fontes)**, elegível pela `RECENCY_EXCEPTION` (CMC 2026, <12 meses); dos "em risco" de 2026: P32=1, P37=5. Extremos: P10 ≈500 · P17 ≈300 · P02 ≈180. P01 confirmado não indexado no Scopus (coberto por OpenAlex/Crossref). Com isso a **pendência transversal está integralmente resolvida** (Qualis ✓ SJR ✓ citações ✓) — notas do README raiz e `reviews/README.md` atualizadas para "RESOLVIDA".

### 63. bookmark.md — recursos externos da RSL

**Prompts:** "crie o arquivo de bookmark.md e adicione o QUALIS" → SCImago → APIs → Portal CAPES.
**Ações:** Criei `bookmark.md` na raiz (indexado no diagrama de estrutura do README) e o populei em quatro incrementos, com cada entrada anotando **onde o recurso foi usado na RSL** (proveniência): (1) **Classificação de veículos** — QUALIS (qualis.pages.dev; estratos de `papers.csv`) e SCImago JCR (scimagojr.com; quartis SJR); (2) **Acesso a bases e textos completos** — Portal de Periódicos da CAPES (periodicos.capes.gov.br; login **CAFe** integrado à base de usuários da Unisinos); (3) **APIs de validação** — OpenAlex (validação da string por DOI; `cited_by_count`), Crossref (`is-referenced-by-count`; usada pelo `DOIS.py`) e Elsevier Developer Portal/Scopus Search API (execução da string: recall 13/14, volume 12.783; `citedby-count`), incluindo o alerta da sintaxe `TITLE-ABS-KEY` por bloco (falso-zero da forma aninhada com `DOI()`).

### 64. Citações cruzadas no corpus (tripla checagem)

**Prompt:** "monte um novo documento com o números de vezes que cada um dos 39 artigos é citados pelos seus pares … tripla checagem OpenAlex, Crossref e Scopus … e uma coluna com a lista de artigos em que o artigo par foi citado."
**Ações:** Criei `citacoes-cruzadas.md` (raiz, indexado no README) com a matriz quem-cita-quem do corpus: **OpenAlex 20 · Crossref 21 · Scopus 25 · União 26 pares** citador→citado. Apenas 10 artigos são citados por pares; **hubs = surveys fundacionais**: P10 (7), P14 (5), P09 (4), P02/P13/P16 (2), P12/P24/P31/P39 (1). Método por fonte: OpenAlex `referenced_works`; Crossref lista `reference` (DOIs); Scopus `REF("<título>")` × OR de DOIs do corpus. **Descobertas metodológicas documentadas:** (i) `REF()` do Scopus casa por **título**, não por DOI (falso-zero silencioso com DOIs — validado com pares positivo/negativo); (ii) **caso P09**: as 4 citações usam DOI de preprint `10.70777/…` — invisíveis ao casamento por DOI canônico em OpenAlex/Crossref; Scopus e S2 (corroborado em `referencias.csv`) resolvem para a versão do periódico; (iii) P01 não indexado no Scopus oculta a aresta P01→P10; P38→P31 falta só na OpenAlex.

### 65. Citações cruzadas no dashboard

**Prompt:** "Adicione as citações cruzadas ao DASHBOARD.md"
**Ações:** Acrescentei ao `reviews/DASHBOARD.md` uma linha na "Navegação rápida" e a seção "🔁 Citações cruzadas no corpus (P01–P40)": totais por fonte (OpenAlex 20 · Crossref 21 · Scopus 25 · **União 26 pares**), tabela dos mais citados com lista de citadores (P10=7, P14=5, P09=4 com nota do DOI de preprint) e a leitura-chave (hubs = surveys fundacionais; os 14 incluídos de 2025–2026 ainda não se citam entre si), com links para `citacoes-cruzadas.md`, `papers.csv` e `referencias.csv`. O painel passa a cobrir também a bibliometria interna do corpus.

### 66. Citações cruzadas no relatório de síntese (§10)

**Prompt:** "Adicione as citações cruzadas ao relatório de síntese"
**Ações:** Inseri a **§10 "Citações cruzadas no corpus"** no `relatorio-sintese.md` (após a confiabilidade entre avaliadores; antigas §10–§12 renumeradas para §11–§13, incluindo subseções da nota metodológica), com a tabela dos hubs e três leituras para a síntese: (i) surveys fundacionais como espinha dorsal conceitual; (ii) os 14 incluídos (2025–2026) ainda não se citam entre si; (iii) **sem citação mútua entre os estudos State Grid** (só P38→P31) — atenua a preocupação de independência da §7. **PDF regenerado** via `build_pdf.py` (MD e PDF em sincronia).

### 67. Prompt de descoberta v2.0.0 → v2.1.0 (lições do ciclo 1 + framing do resumo)

**Prompts:** "Act as an expert in SLR … improve the research/prompt.md …" → "Read this text and reasoning how to improve the prompt.md …"
**Ações:** **v2.0.0**: reescrevi o `research/prompt.md` embutindo a **PROJECT_MEMORY** do ciclo 1 (PRISMA I1–I6/E1–E5 com casos concretos; PICOC com regra v1.1.0 e lacuna de MTTD/MTTR; string validada 13/14 com caveat de sintaxe do Scopus; APIs/fontes com quirks e armadilha do DOI de preprint), dedup ampliada para P01–P40, campos `picoc_fit`/`group_provenance`, DOI de versão de registro, T8 prioridade máxima + novo T9 (produção), cota ≥1/3 T8/T9. **v2.1.0**: incorporado o resumo da revisão — copiloto **cognitivo** em ambientes de alta criticidade; escopo com **LLMOps** e **autonomia adaptativa**; **eixo de evolução S1→S2→S3** (S2→S3 = Comparison ideal); tríade de outcomes (MTTD/MTTR × observabilidade × carga cognitiva); campos **`evidence_type`** (demonstrado-produção/simulação vs. proposto; claims de fornecedor nunca viram demonstrado) e **`evolution_stage`**; `CAVEATS` com balanço de evidência. `research/README.md` atualizado; commits `6e948cc` e `36b724a`.

### 68. Prompt v3.0.0 (PR externo) e v3.1.0 (Semantic Layer × Ontology × Context Layer)

**Prompts:** evolução externa via PR do usuário + "Read the file Semantic_Layer_Ontology_Context_Layer_Prompt.md … and apply improvements on the file research/prompt.md"
**Ações:** O usuário evoluiu o prompt para **v3.0.0** via PR (#1, branch de agente em nuvem): PM-0 (terminologia: 39 do repositório ≠ 33 incluídos), I/E refinados (I5 por fonte, `NOT_INDEXED ≠ 0`; E6/E7), fluxos `SUPPLEMENTARY_EVIDENCE`/`FOUNDATIONAL_SUPPLEMENTARY`, snowballing obrigatório, saída auditável (RUN_METADATA, SEARCH_LOG, logs de dedup/exclusão, schema JSON) e proibição de quota-padding — além de `bookmark.md` e `research/README.md` expandidos (S2/OpenCitations). Sobre ela apliquei a **v3.1.0** (novo **PM-8**), traduzindo o padrão do guia `Semantic_Layer_Ontology_Context_Layer_Prompt.md`: **camada semântica** (registro canônico de outcomes com mapa de proxies; DIRECT só se o estudo mede a métrica; `named_operational_metrics` com IDs canônicos), **ontologia** (resolução de entidades WORK/VENUE-por-ISSN/ACTOR-GROUP/CONCEPT; caso P09 como falha de entity resolution; aliases usados em busca E normalização) e **camada de contexto** (PROJECT_MEMORY como memória de decisão com emenda datada; linhagem fonte→resposta; **fronteira de permissão do agente** — recomendar, nunca decidir inclusão). Push inicial rejeitado (remoto adiante); **rebase com conflito resolvido** preservando a v3.0.0 remota + adições (diff final = só as 88 linhas do PM-8). Versionados também o guia-fonte e os snapshots `prompt-v1/v2/v3.md`. Commit `2a99f20`.

### 69. Regra permanente de dump de memória por sessão (CLAUDE.md)

**Prompt:** "before finish this session, include a rule to dump the memory of each session, include the contexts, iterations, prompts, answers and commands executed and store all of these conversations on file MEMORY.md in the root folder of the project"
**Ações:** Criei o **`CLAUDE.md`** na raiz do projeto — carregado automaticamente em toda sessão futura — com a **regra obrigatória de dump de memória**: cada unidade de trabalho vira item numerado (sequência contínua entre sessões) registrando prompt, contexto, ações/respostas, comandos/ferramentas executados e incidentes/recuperações; registro **incremental** e sempre antes de encerrar; formato codificado a partir do padrão já existente no MEMORY.md (bloco de sessão com Linha do tempo, Decisões, Artefatos e Histórico de commits, incluindo commits externos); regras de fidelidade (nunca reescrever itens passados; registrar falhas; nunca registrar segredos; commit + push após cada atualização). O arquivo também consolida as convenções gerais do repositório (pt-BR com termos técnicos em EN, indexação obrigatória de arquivos novos, artefatos históricos imutáveis, citações por fonte, chaves fora do repo).

## Decisões e convenções da sessão

- **Nomenclatura das fichas:** `Pxx-extraction.csv` (EN) / `Pxx-extraction-ptBR.csv` (pt-BR) / `consolidated-extraction[-ptBR].csv`, em `report/`.
- **Tradução pt-BR:** termos técnicos, acrônimos, títulos, autores, veículos, citações verbatim e âncoras de evidência permanecem em inglês; escores traduzidos (Alta/Média/Baixa).
- **Execução em escala:** leitura/extração dos PDFs delegada a subagentes paralelos (um por artigo), com validação estrutural centralizada por script (RFC 4180, 11 campos, âncoras).
- **Recuperação de falha:** interrupção por limite de sessão tratada com relançamento apenas dos itens faltantes (18/39), sem retrabalho.
- **Higiene do repo:** `.serena/` (cache do Serena MCP) ignorado; `report/` definido como **Etapa 3** na estrutura do repositório.
- **Pendência transversal (FECHADA em 2026-07-27):** Qualis/SJR/percentil **e citações** (3 fontes: OpenAlex/Crossref/Scopus) resolvidos via `papers.csv`; P35 elegível por `RECENCY_EXCEPTION`. Artefatos históricos (relatório de síntese, avaliações ChatGPT) não são reescritos — o registro da avaliação com `[VERIFICAR]` é preservado.

## Artefatos produzidos (em `report/`, salvo indicado)

- `P01…P40-extraction.csv` (39 fichas EN) · `P01…P40-extraction-ptBR.csv` (39 fichas pt-BR)
- `consolidated-extraction.csv` / `consolidated-extraction-ptBR.csv` (39×12)
- `README.md` (índice das fichas + PDFs + relevância)
- Raiz: `docs/` P01–P19 versionados · `referencias.csv` · `DOIS.py` · `DOIS.txt` · `papers.csv` (bibliometria verificada) · `export.ris`/`export.csv` (Mendeley) · `.gitignore` (+.serena/) · README raiz e `reviews/README.md` atualizados
- `picoc/`: `picoc-extraction-prompt.md` · `picoc-results-consolidated-P01-P40-{Claude,ChatGPT,Gemini,Gemini-Atualizado}.md` · `picoc-comparacao-avaliadores.{md,csv}` (recomputada sobre 39 artigos)

## Histórico de commits da sessão

| Hash      | Data       | Mensagem                                                                              |
| --------- | ---------- | ------------------------------------------------------------------------------------- |
| `0c876d6` | 2026-07-25 | Add report/ SLR extraction sheets (P01-P40) with pt-BR versions and consolidated CSVs |
| `043438c` | 2026-07-25 | Add docs/ P01-P19 survey PDFs and referencias.csv                                     |
| `21d8637` | 2026-07-25 | Add DOIS.py reference-extraction script and DOIS.txt DOI list                         |
| `15ba93b` | 2026-07-25 | Ignore .serena/ (Serena MCP local cache)                                              |
| `e427439` | 2026-07-25 | Index report/ extraction sheets and close documentation gaps                          |
| `94a0037` | 2026-07-25 | Log session 2026-07-22..25 (Etapa 3: extraction sheets) in MEMORY.md                  |
| `ef5f99a` | 2026-07-25 | Add papers.csv verified bibliometrics; resolve Qualis/SJR pendency                    |
| `91ea72e` | 2026-07-25 | Log papers.csv verification work (item 51) in MEMORY.md                               |
| `b363f9d` | 2026-07-26 | Add Mendeley export.ris and its CSV conversion (export.csv)                           |
| `009d91b` | 2026-07-26 | Update P04 PDF with replacement copy                                                  |
| `be53c16` | 2026-07-26 | Update P05, P12, P14 PDFs with replacement copies                                     |
| `0a05761` | 2026-07-26 | Add picoc/ PICOC extraction (Etapa 4) with per-evaluator consolidated tables          |
| `b2711fb` | 2026-07-26 | Add PICOC inter-evaluator comparison (Claude x ChatGPT x Gemini)                      |
| `60d38e9` | 2026-07-26 | Log RIS conversion, PDF replacements, and PICOC work (items 52-54) in MEMORY.md       |
| `2aad34f` | 2026-07-27 | Recompute PICOC comparison with full-coverage Gemini file (39 papers)                 |
| `4f55b3c` | 2026-07-27 | Apply Comparison protocol rule (v1.1.0) and reclassify the 12 divergent cases         |
| `3cee765` | 2026-07-27 | Add final Comparison (PICOC v1.1.0) column to report/README index                     |
| `eed9f33` | 2026-07-27 | Log Comparison column work (item 57) in MEMORY.md                                     |
| `7c3ccf1` | 2026-07-27 | Derive RSL search string from PICOC synthesis, calibrated on the corpus               |
| `b10556e` | 2026-07-27 | Log search string derivation (item 58) in MEMORY.md                                   |
| `377eed6` | 2026-07-27 | Validate search string externally on OpenAlex (13/14 included recall)                 |
| `f50ae72` | 2026-07-27 | Log OpenAlex validation of the search string (item 59) in MEMORY.md                   |
| `9a693c2` | 2026-07-27 | Execute search string on Scopus API: 13/14 included recall, 12,783 volume             |
| `6da2f21` | 2026-07-27 | Append Scopus execution commit (9a693c2) to MEMORY.md session table                   |
| `aef452e` | 2026-07-27 | Add PRISMA 2020 flow diagram with criteria and counts                                 |
| `8d94d73` | 2026-07-27 | Add per-study citation counts (OpenAlex/Crossref/Scopus); close pendency              |
| `d59e90a` | 2026-07-27 | Log PRISMA diagram and citation counts (items 61-62) in MEMORY.md                     |
| `92ee2aa` | 2026-07-27 | Add bookmark.md with QUALIS reference link                                            |
| `9f932fd` | 2026-07-27 | Add SCImago Journal & Country Rank to bookmark.md                                     |
| `fa7a193` | 2026-07-27 | Add validation APIs (OpenAlex, Crossref, Elsevier/Scopus) to bookmark.md              |
| `f776c72` | 2026-07-27 | Add Portal de Periodicos CAPES (CAFe/Unisinos login) to bookmark.md                   |
| `1801757` | 2026-07-27 | Log bookmark.md creation and entries (item 63) in MEMORY.md                           |
| `75e1fb0` | 2026-07-27 | Add corpus cross-citation matrix with triple-source verification                      |
| `e4b95d9` | 2026-07-27 | Log corpus cross-citation matrix (item 64) in MEMORY.md                               |
| `eab830e` | 2026-07-27 | Surface corpus cross-citations on the dashboard                                       |
| `97630d4` | 2026-07-27 | Log dashboard cross-citations section (item 65) in MEMORY.md                          |
| `5520442` | 2026-07-27 | Add corpus cross-citations section (S10) to the synthesis report                      |
| `6e948cc` | 2026-07-27 | Upgrade discovery prompt to v2.0.0 with PROJECT_MEMORY of cycle 1                     |
| `36b724a` | 2026-07-27 | Incorporate review-abstract framing into discovery prompt (v2.1.0)                    |
| `ee9e9fc` | 2026-07-28 | Upgrade SLR discovery prompt to v3.0.0 _(PR #1 do usuário, agente em nuvem)_          |
| `59d09af` | 2026-07-28 | Complete API provenance bookmarks _(PR #1 do usuário)_                                |
| `2a99f20` | 2026-07-28 | Apply Semantic Layer x Ontology x Context Layer pattern to prompt (v3.1.0)            |
| `4cbd3b2` | 2026-07-28 | Log synthesis-report S10 and prompt evolution v2->v3.1 (items 66-68)                  |

_(O commit desta atualização de MEMORY.md é acrescentado ao final do histórico.)_
