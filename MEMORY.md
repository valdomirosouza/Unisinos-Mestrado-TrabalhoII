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
| `bdeaeb3` | 2026-08-02 | Add permanent session-memory dump rule (CLAUDE.md) and log item 69                    |

_(O commit desta atualização de MEMORY.md é acrescentado ao final do histórico.)_

---

# Sessão 2026-09-07 → 2026-10-29 — Padronização de prompts, ciclo 2 completo da RSL e artigo IEEE Access (draft v1)

## Linha do tempo (prompts → respostas/ações)

### 70. Persona do prompt PICOC: de professor para pesquisador orientado

**Prompt:** "update the file picoc/picoc-extraction-prompt.md changing the
prompt de 'Aja como Professor Doutor em Computação Aplicada do PPGCA da
Unisinos' por 'Aja como pesquisador em Computação Aplicada do PPGCA da
Unisinos orientado por um professor Doutor em Ciência da Computação'".

**Ações:** Substituída a linha de PAPEL do prompt em
`picoc/picoc-extraction-prompt.md` pela nova persona (pesquisador orientado),
mantendo intacto o restante do prompt (especialista em RSL, Kitchenham &
Charters, PICOC). Como o arquivo é versionado com changelog, a versão foi
elevada de v1.1.0 para **v1.2.0**, com entrada de changelog descrevendo a
mudança e sua motivação (refletir com fidelidade o papel de quem conduz a
extração). Verificado por grep que as referências a "v1.1.0" nos demais
documentos (report/README.md, picoc-comparacao-avaliadores.md, MEMORY.md)
citam a **regra de Comparison introduzida na v1.1.0** — não a versão corrente
do prompt — e portanto permanecem corretas. Commit `a7b2468`.

### 71. Referência metodológica do prompt PICOC: Kitchenham (2009)

**Prompt:** "Agora altere no mesmo arquivo picoc/picoc-extraction-prompt.md
onde diz 'seguindo as diretrizes de Kitchenham & Charters' por 'seguindo as
diretrizes de Kitchenham (2009) no paper/artigo Systematic literature reviews
in software engineering – A systematic literature review'".

**Ações:** Substituída a referência no bloco PAPEL do prompt e, por
consistência, também na linha "Metodologia de referência" do cabeçalho do
arquivo (que citava "Kitchenham & Charters (guia de RSL em Engenharia de
Software)"). Versão elevada de v1.2.0 para **v1.3.0** com entrada de
changelog, alinhando o prompt à referência metodológica adotada na
dissertação — Kitchenham et al. (2009), o mesmo paper que rege a RSL desde a
Etapa 1. Commit `00b3e69`.

### 72. Mesmas alterações no template de extração (report/)

**Prompt:** "Aplique as mesmas alterações no
report/paper-extraction-prompt-template.md".

**Ações:** Aplicadas ao template de extração (arquivo em inglês) as duas
mudanças dos itens 70–71, adaptadas ao idioma: SYSTEM / ROLE reescrito de
"expert academic research assistant (Kitchenham methodology)" para
"researcher in Applied Computing at PPGCA (Unisinos) advised by a professor
holding a Doctorate in Computer Science", com a metodologia ancorada em
Kitchenham (2009), "Systematic literature reviews in software engineering – A
systematic literature review". Versão elevada de 1.0.0 para **1.1.0** e seção
Changelog criada no arquivo (que não tinha), registrando também a 1.0.0
inicial. Commit `4094ce1`.

### 73. Mesmo padrão no prompt de descoberta (research/prompt.md)

**Prompt:** "Sim, aplique o mesmo padrão no research/prompt.md".

**Ações:** Bloco ROLE do prompt de descoberta reescrito com a persona padrão
("researcher in Applied Computing at PPGCA (Unisinos) advised by a professor
holding a Doctorate in Computer Science") e a metodologia — que já citava
Kitchenham et al. (2009) — ancorada explicitamente no título do paper
"Systematic literature reviews in software engineering – A systematic
literature review". Versão elevada de v3.1.0 para **v3.2.0** com entrada de
changelog. O `research/README.md`, que ainda citava "v3.0.0" como versão
corrente (defasado desde a v3.1.0), foi atualizado para "v3 (atual: v3.2.0)"
no título da seção, na árvore de arquivos e na nota de governança de versões.
Commit `88c5412`.

### 74. Mesmo padrão no template de avaliação (consulta ao ChatGPT)

**Prompt:** "Aplique o mesmo padrão no prompts/prompt-chatgpt-consultation.md
também".

**Ações:** O arquivo citado não existe; a pasta `prompts/` contém apenas os
20 prompts históricos `prompt-P20.md`…`prompt-P40.md` efetivamente enviados
ao ChatGPT no ciclo 1 (imutáveis por convenção). Consultado, o usuário
escolheu criar um template novo preservando os históricos. Durante a
indexação, porém, foi identificado que o template canônico de avaliação já
existe: **`prompt-template.md` (raiz)** — é ele que a Etapa 2 preenche para
gerar os prompts por artigo. Para não criar duplicata divergente, o padrão
foi aplicado diretamente nesse arquivo (bloco PAPEL: persona de pesquisador
orientado + Kitchenham 2009 com título completo do paper), e o rascunho
duplicado em `prompts/` foi descartado antes de commit. Os P20–P40
permanecem intactos. O hook formatador reformatou o restante do arquivo
(espaçamento/indentação, sem mudança de conteúdo). Commit `0a07d88`.

### 75. Rename do template de avaliação para prompts/

**Prompt:** "Sim, faça o rename para prompts/prompt-chatgpt-consultation.md".

**Ações:** `git mv prompt-template.md prompts/prompt-chatgpt-consultation.md`
(o nome que o usuário citara no item 74 passa a existir de fato). Referências
atualizadas: `README.md` (árvore de estrutura — entrada movida da raiz para a
subárvore de `prompts/`, agora rotulada "Etapa 2: prompts de avaliação" —,
seção Insumos e fluxo da Etapa 2) e `reviews/DASHBOARD.md` (linha Fontes).
Menções a `prompt-template.md` em itens passados deste MEMORY.md (itens 1 e
74, entre outros) foram preservadas por fidelidade histórica — referem-se ao caminho
vigente à época. Verificação de links em todo o repositório: 0 quebrados
pelo rename (2 apontamentos pré-existentes em
`reviews/COMO-CRIAR-GRAFICOS.md` são exemplos ilustrativos, não links
reais). Commit `5001ac4`.

### 76. Commit dos PDFs candidatos P41–P89 (ciclo 2)

**Prompt:** "Agora commit os novos PDFs P41 em diante na pasta docs/".

**Ações:** Commitados os **49 PDFs novos P41–P89** em `docs/`, adicionados
pelo usuário como candidatos do novo ciclo de descoberta (temas: anomaly
detection, AIOps agêntico, SOC/SIEM/LLM, predictive maintenance, carga
cognitiva/mental workload, observabilidade). Ficaram de fora,
deliberadamente: o PDF do paper de Kitchenham (2009) em `docs/` (não é um
P-file — aguarda instrução), `agentic_ir_corpus-claude-research.xlsx`,
`claude-resume.txt` e o lock temporário `~$agentic...xlsx` do Excel. Os
P41–P89 ainda NÃO estão indexados nos READMEs — a indexação ocorrerá quando
o ciclo 2 definir triagem/avaliação desses candidatos. Commit `6297ef2`.

### 77. Commit do PDF de Kitchenham (2009)

**Prompt:** "Sim, commit o PDF do Kitchenham (2009) também".

**Ações:** Commitado `docs/Systematic literature reviews in software
engineering – A systematic literature review.pdf` — o paper de Kitchenham
et al. (2009) que ancora a metodologia da RSL e que os quatro prompts vivos
passaram a citar pelo título (itens 70–74). Com isso, `docs/` fica sem
arquivos não rastreados. Commit `3c76e22`.

### 78. Extração PICOC do ciclo 2 (P41–P89)

**Prompt:** "Agora que o prompt picoc/picoc-extraction-prompt.md está
atualizado, execute ele para os novos papers/artigos de P41 até P89." (com
"resume" após queda por limite de sessão).

**Ações:** Prompt PICOC v1.3.0 executado sobre os **49 candidatos do ciclo
2** com o padrão de fan-out do ciclo 1: um agente de leitura integral por
PDF, em ondas de ~10, cada um gravando fragmento (raciocínio + linha da
tabela) no scratchpad. **Incidente:** limite de sessão derrubou 10 agentes
(P72–P80 da onda 4 + P73 etc.) após 31/49 fragmentos; recuperação pelo
padrão estabelecido — verificação em disco e relançamento SOMENTE dos 18
faltantes (P71 caiu mas o fragmento já estava íntegro; zero retrabalho).
Fragmentos validados por script (49/49 com ROW única de 8 colunas; 4 com
cabeçalho `#` normalizado para `###` na montagem). Nota operacional nova: o
renderizador de PDF do Read falhou na máquina (poppler ausente) e os agentes
extraíram o texto integral via pypdf. Consolidado em
`picoc/picoc-results-consolidated-P41-P89-Claude.md` (tabela de 49 linhas +
síntese transversal + apêndice de raciocínio por artigo). **Resultados:**
Comparison = 26 DECLARED · 13 N/A (mapeamento) · 9 N/A (contraste
conceitual) · 1 NÃO DECLARADO (P75); MTTD/MTTR nominal segue quase ausente
(apenas P76, contra literatura); surge um **cluster humano** com medição
direta de carga cognitiva/fadiga (P62, P69, P81, P85) — inexistente em
P01–P40; muitos candidatos periféricos ao escopo (P58, P59, P67) sinalizados
para a triagem. README raiz atualizado (seção Etapa 4, árvore e descrição de
`docs/`, que ainda dizia "39 PDFs"). Commit `adeeb78`.

### 79. Ordem do fluxo do ciclo 2 (consulta)

**Prompt:** "read the folder prompts and reviews and told me whats is the
correct order to follow? I executed above the PICOC cycle, and now I need to
go ahead with my research, reading the new papers."

**Ações:** Consulta respondida (sem alteração de artefatos) com base em
`prompts/`, `reviews/README.md` e no fluxo do ciclo 1. Ordem recomendada
para P41–P89: **(1)** bibliometria/elegibilidade (CSV de insumos + Qualis
A1–A2, SJR Q1–Q2, Citações ≥ 1 por fonte) — corte antecipado como o que
eliminou P39/P40; **(2)** triagem PRISMA I1–I6/E1–E5 com registro de
exclusões; **(3)** avaliação individual via
`prompts/prompt-chatgpt-consultation.md` → `prompts/prompt-PNN.md` →
`reviews/review-PNN.md` (Tabelas 3/5/7 + parecer); **(4)** consolidação
(resultados-consolidados.csv, gráficos, síntese, DASHBOARD, PRISMA);
**(5)** comparação entre avaliadores (opcional); **(6)** fichas de extração
em `report/` só para incluídos. Observação: o PICOC (item 78) veio antes da
triagem neste ciclo (inverso do ciclo 1) e atua como insumo do passo 2;
`agentic_ir_corpus-claude-research.xlsx` (não rastreado) pode conter os
insumos do passo 1.

### 80. Passo 1 do ciclo 2 — bibliometria e elegibilidade (P41–P89)

**Prompt:** "Sim, comece pelo passo 1 usando o Papers_Index.csv".

**Ações:** Lido `Papers_Index.csv` (88 linhas P01–P89; título, autores, ano,
veículo, cluster, tipo, citações de 2026-09-06, DOI, percentil Scopus, SJR,
ISSN, arquivo) — cobertura 49/49 do ciclo 2, sem campos vazios. Verificação
externa: **citações OpenAlex e Crossref buscadas por DOI para os 49**
(2026-09-09; 49/49 resolvidos nas duas fontes, nenhum zero/zero; anos
conferem com OpenAlex). Scopus ficou **PENDENTE** (sem chave de API na
sessão — a anterior deveria ser regenerada). **Qualis:** o qualis.pages.dev
não expõe dataset direto (backend Supabase); em vez disso o estrato foi
**derivado do percentil Scopus pela regra CAPES 2025-2028** (A1 ≥ 87,5% ·
A2 ≥ 75% · A3 ≥ 62,5% · A4 ≥ 50% · B1 ≥ 37,5%…), **calibrada e validada
sem exceção nos 39 pares percentil×Qualis verificados de `papers.csv`**.
Gerado **`papers-ciclo2.csv`** (16 colunas, incl. veredito de elegibilidade
pelos critérios do ciclo 1: ano ≥ 2020, veículo, Citações ≥ 1, SJR Q1–Q2,
Qualis A1–A2). **Resultado: 45 ELEGÍVEIS · 4 INELEGÍVEIS** — P62 e P69
(Qualis A3, percentil 74%), P81 (A4, 60%), P86 (B1, 47% + SJR Q3); nota:
3 dos 4 inelegíveis são do cluster humano/carga cognitiva do item 78 (P85
sobrevive, percentil 91% → A1). `Papers_Index.csv` e `papers-ciclo2.csv`
commitados e indexados no README raiz (árvore + seção Insumos). Commit
`c96334e`.

### 81. Passo 2 do ciclo 2 — triagem PRISMA (P41–P89)

**Prompt:** "Sim, siga com a triagem PRISMA dos elegíveis, por enquanto
vamos manter os papers com A3, A4 e B1 do Qualis e Q3 do SLR, incluindo
ressalvas por conta do estrato Qualis e SJR."

**Ações:** Criado `reviews/triagem-ciclo2.md` aplicando os critérios
I1–I6/E1–E5 do PRISMA.md aos 49 candidatos, com **emenda de protocolo
(decisão do autor, 2026-09-09)**: I3/I4 não excluem neste ciclo — P62, P69
(A3), P81 (A4) e P86 (B1 + SJR Q3) mantidos **com ressalva de estrato** (os
vereditos estritos permanecem em papers-ciclo2.csv como registro).
Diferencial metodológico: a triagem usa a **extração PICOC de leitura
integral (item 78)** como evidência, permitindo exclusão temática
antecipada auditável (no ciclo 1, E2/E3 só caíam após avaliação integral).
**Resultado: 22 aprovados para avaliação integral** (18 sem ressalva + os 4
de estrato; inclui o cluster de carga cognitiva P62/P69/P81/P85 e 5
candidatos a fundacionais P52/P54/P72/P77/P79) e **27 excluídos** — E2
não-agêntico = 19 (precedentes P26/P29/P30) · E3 fora de domínio = 8
(manutenção industrial, física de partículas, vídeo, manufatura; precedente
P38). Cada linha das tabelas traz evidência PICOC e flags para os
pareceres. Indexado em reviews/README.md (seção "Ciclo 2"), PRISMA.md
(nota de versão, sem reescrever o diagrama do ciclo 1) e README raiz;
links verificados (0 quebrados). Commit `df57b9c`.

### 82. Prompts de avaliação do ciclo 2 (22 aprovados)

**Prompt:** "go ahead" (gerar os prompts da Etapa 2 para os 22 aprovados).

**Ações:** Gerados `prompts/prompt-P43.md` … `prompt-P88.md` (22 arquivos) a
partir do template vivo `prompts/prompt-chatgpt-consultation.md`, por
script: CONTEXTO ajustado ao ciclo 2 (corpus prévio P01–P40/33 incluídos;
IDs a partir de P41), INSUMOS preenchidos com `papers-ciclo2.csv` (título,
arquivo PDF conferido em disco, **Qualis derivado do percentil com a regra
CAPES explicitada na própria linha**, SJR) e linha nova `ressalvas_triagem`
transcrevendo as flags de `reviews/triagem-ciclo2.md` — incluindo a
ressalva de estrato obrigatória em P62/P69 (A3), P81 (A4) e P86 (B1+Q3).
Indexados no README raiz (árvore de `prompts/`) e na seção Ciclo 2 de
`reviews/README.md`. Próximo: executar cada prompt contra o PDF para
produzir `reviews/review-P43.md`…. Commit `9fc207d`.

### 83. Pareceres do ciclo 2 (22 avaliações integrais)

**Prompt:** "sim, vá em frente" (executar os 22 prompts contra os PDFs;
"resume" após queda por limite de sessão).

**Ações:** Executados os 22 prompts em fan-out (3 ondas de 8/8/6 agentes;
cada agente leu o prompt preenchido, o modelo de formato `review-P21.md` e o
PDF integral, e gravou `reviews/review-PNN.md` no formato do ciclo 1 —
Tabelas A/B/C + parecer). Particularidades do ciclo 2 aplicadas: Tabela A
com bibliometria verificada citando fonte (OA/CR de papers-ciclo2.csv,
2026-09-09; Scopus pendente), Qualis derivado do percentil, Etapa 1
registrada como ELEGÍVEL (ou "ELEGÍVEL POR EMENDA DE PROTOCOLO" nos 4 de
estrato) e `ressalvas_triagem` incorporada às recomendações. **Incidente:**
limite de sessão derrubou 11 agentes — mas TODOS já tinham gravado seus
pareceres antes de cair (morreram no turno do relatório final); validação
por script confirmou 22/22 íntegros (título, 3 tabelas, escores,
recomendação) — zero relançamento. **Resultado: 20 INCLUIR COM RESSALVAS ·
2 EXCLUIR** (P85 fadiga VTS: SCORE_RQ 0,5, sem aderência às RQs; P86
tracing rule-induction: não-agêntico, estrato B1+Q3). Destaques: P79 (RQ
5,0, fundacional SOC), P73 (QA 4,0, alert fatigue), P88 (QA 4,0, MAS
análogo a P25); os 5 fundacionais confirmados como "Incluir c/ ressalvas
(fundacional)"; cluster carga cognitiva: P62/P69/P81 incluídos com ressalva
de estrato, P85 excluído por não aderência. Tabela-síntese do ciclo 2
adicionada à seção Ciclo 2 de `reviews/README.md`. Commit `99f1e6c`.

### 84. Consolidação do ciclo 2

**Prompt:** "Sim, siga com a consolidação".

**Ações:** Consolidação como novos artefatos (os do ciclo 1 permanecem
imutáveis): **(1)** `reviews/resultados-consolidados-ciclo2.csv` — 22
linhas, mesmas 23 colunas do CSV do ciclo 1, com símbolos RQ/QA extraídos
por script dos próprios pareceres (validação: 22/22 consistentes com os
relatórios dos agentes); **(2)** `reviews/charts-ciclo2/` — 5 SVGs gerados
com o MESMO `scripts/gen_charts.py` do ciclo 1, rodado em cópia
parametrizada apontando para o CSV do ciclo 2; **(3)**
`reviews/graficos-ciclo2.md` — galeria com leitura (lacuna sistemática:
RQ3/QA3, evidência empírica); **(4)** `reviews/PRISMA.md` — seção Ciclo 2
substituída pelo diagrama Mermaid completo do fluxo: 49 → 49 triados
(emenda) → −27 triagem → 22 avaliados → −2 → 20 incluídos → **corpus
consolidado 53** (33 + 20; 7 fundacionais condicionais no total: P24, P33

- P52/P54/P72/P77/P79); **(5)** `reviews/DASHBOARD.md` — nova seção
  "Ciclo 2" com números-chave (SCORE_RQ médio 3,16/mediana 3,5; SCORE_QA
  2,75/2,75; bandas 11 Alta · 10 Média · 1 Baixa) e links; **(6)** README
  raiz e reviews/README atualizados. O relatório de síntese
  (`relatorio-sintese.md`) do ciclo 1 NÃO foi alterado — a síntese
  consolidada dos dois ciclos é etapa futura. Links verificados (0
  quebrados). Commit `891edb1`.

### 85. Fichas de extração do ciclo 2 (20 incluídos)

**Prompt:** "Agora atualize as fichas de extração em report/ para os 20
incluídos".

**Ações:** Fan-out de 20 agentes (ondas de 8/8/4), cada um lendo o template
`report/paper-extraction-prompt-template.md` (v1.1.0) + o PDF integral e
gravando as DUAS fichas (`PNN-extraction.csv` EN e `-ptBR.csv`) no formato
do ciclo 1 (13 linhas RFC 4180, âncoras de evidência nos campos 4–9).
Validação por script: **40/40 CSVs válidos** (linhas, colunas, nomes de
campo, Paper ID). Consolidados novos gerados a partir das fichas:
`consolidated-extraction-ciclo2.csv` + `-ptBR.csv` (20 × 12 colunas; os do
ciclo 1 permanecem imutáveis). **Relevância: 2 High (P76, P79) · 15 Medium
· 3 Low (P63, P69, P82)** — P76 segue como o único estudo de todo o corpus
que mede MTTR nominalmente (~1–1,5 min por fase, comparação vs. Microsoft
Copilot for Security da literatura); P79 traz evidência secundária rica
(CyberAlly: MTTR 8 h → 90 min; GreyMatter: 98% dos alertas automatizados).
Nota de fidelidade do P79: contagens PRISMA do próprio artigo não fecham
aritmeticamente — extraídas com marcação `⚠ Ambiguous`, sem correção.
`report/README.md` ganhou a seção "Índice das fichas — Ciclo 2" (tabela com
PDF/EN/pt-BR/Relevância/Comparison PICOC) e o README raiz atualizou as
contagens (59 fichas). Links verificados (0 quebrados). Commit `d527e60`.

### 86. Síntese consolidada dos dois ciclos

**Prompt:** "Sim, gere a síntese consolidada dos dois ciclos".

**Ações:** Criado `reviews/relatorio-sintese-consolidado.md` (12 seções,
espelhando a estrutura do relatório do ciclo 1, que permanece imutável) +
PDF gerado com cópia parametrizada do `scripts/build_pdf.py` (268 KB).
Conteúdo: funil PRISMA consolidado (tabela dos 2 ciclos), composição do
corpus 53 (19 + 14 + 20; 7 fundacionais condicionais; 3 ressalvas de
estrato), migração da lacuna sistemática RQ4 (ciclo 1) → RQ3/QA3 (ciclo 2),
qualidade comparada (RQ 3,83→3,16; QA 3,50→2,75; zero "Incluir" pleno no
ciclo 2), **seção-núcleo sobre MTTD/MTTR e carga cognitiva** (P76 único
nominal, desfavorável e vs. literatura; P79 evidência secundária CyberAlly/
GreyMatter; proxies P73/P81/P87/P83; cluster COGNITIVE_LOAD P62/P69/P81 +
instrumentos BUS-15/NASA-TLX; conclusão: lacuna triangulada em 89
candidatos — nenhum estudo mede MTTD E MTTR nominalmente com baseline
próprio em produção), taxonomia consolidada de paradigmas, rastreabilidade
das exclusões, confiabilidade (κ = 0,74 no ciclo 1; **avaliador único no
ciclo 2 — comparação pendente**, listada como limitação nº 1), limitações,
próximos passos e nota metodológica com as 4 diferenças do ciclo 2.
Indexado no README raiz ("Comece por aqui"), reviews/README (bloco Ciclo 2)
e DASHBOARD (seção Ciclo 2). Links verificados (0 quebrados). Commit
`129afc8`.

### 87. Comparação entre avaliadores do ciclo 2 — bloqueio metodológico

**Prompt:** "Agora faça a comparação entre avaliadores do ciclo 2 com o
ChatGPT".

**Ações:** Verificado que `reviews/ChatGPT/` contém apenas as 20 avaliações
do ciclo 1 (P20–P40) — as do ciclo 2 não existem no repositório.
**Bloqueio explicado ao usuário:** o assistente não tem acesso ao ChatGPT e
não deve produzir ele próprio o segundo conjunto de pareceres, pois isso
destruiria a independência entre avaliadores que o κ mede (fabricação de
concordância). Entregue o procedimento (mesmo do ciclo 1): usuário executa
os 22 prompts `prompts/prompt-P43…P88.md` no ChatGPT com os PDFs, salva as
saídas como `reviews/ChatGPT/PNN_avaliacao_RSL.md` e avisa; a partir daí o
assistente computa concordância e Cohen's κ (decisão, RQs, QAs), gera
`comparacao-avaliadores-ciclo2.md` + `.csv` e atualiza dashboard/síntese.
Nenhum artefato alterado neste item.

### 88. Conjuntos ChatGPT e Gemini para a comparação (P20–P88)

**Prompt:** "inclui na pasta reviews as novas pastas ChatGPT e Gemini com as
avaliações dos artigos P20 até P88. Faça o push e commit disso no
repositório." (2026-10-25; desbloqueia o item 87)

**Ações:** O usuário depositou os arquivos no working tree: **ChatGPT** — 22
avaliações novas do ciclo 2 (somando-se às 20 do ciclo 1 já versionadas);
**Gemini** — pasta NOVA com 42 avaliações (P20–P40 + os 22 do ciclo 2).
Validação antes do commit: 22/22 por avaliador no ciclo 2, IDs e títulos
conferidos no conteúdo. **Correção:** o arquivo do ChatGPT nomeado
`P84_avaliacao_RSL.md` continha a avaliação do **P85** (P84 foi excluído na
triagem) — renomeado para `P85_avaliacao_RSL.md` conforme o conteúdo, com
nota no README. 7 arquivos do Gemini embutem o prompt no topo (ID aparece no
corpo) — formato aceito como está (artefato de terceiro, imutável). Nota:
avaliações históricas do Gemini (P35, P37–P40) contêm links `file:///...`
locais da máquina do usuário — mantidos intactos por fidelidade.
`reviews/README.md`: seção renomeada para "Avaliações comparativas (ChatGPT
e Gemini)" com o registro do rename. Commit `8f98497` (65 arquivos), push
ok. Próximo: computar concordância/κ do ciclo 2.

### 89. Comparação entre três avaliadores — ciclo 2

**Prompt:** "Sim, siga com a comparação entre avaliadores".

**Ações:** Extraídos por script (regex sobre SCORE_RQ/SCORE_QA/x-de-5/x-de-4
e linhas de recomendação) os escores e vereditos dos 44 arquivos de
terceiros, com inspeção manual dirigida dos casos ambíguos (prompts
embutidos nos arquivos do Gemini poluíam a captura; 7 recomendações e 2
escores confirmados lendo o trecho exato). Gerados
`reviews/comparacao-avaliadores-ciclo2.md` + `.csv` (16 colunas).
**Resultados (decisão Incluir/Excluir):** Claude×Gemini 95,5% (21/22),
κ=0,65; ChatGPT×Gemini 86,4%, κ=0,35; Claude×ChatGPT 81,8%, κ=0,24; Fleiss
κ=0,36 — κs deflacionados pelo paradoxo da prevalência (17/22 inclusões
unânimes), documentado. **As 4 divergências são todas protocolares:**
P62/P69/P81 — ChatGPT aplicou o critério estrito de estrato e parou na
triagem (INELEGÍVEL), ignorando a emenda de 2026-09-09 presente só nos
INSUMOS (reedição invertida do caso P39/P40 do ciclo 1); P85 — mérito
convergente (RQ 0,5/1,5/0,5) mas destino divergente do cluster de carga
cognitiva (Claude exclui; GPT/Gemini mantêm como evidência complementar).
P86 = exclusão unânime. MAE: CL×GPT RQ 0,53/QA 0,31 (n=18); CL×GEM RQ
0,66/QA 0,68 (n=22). Tendências: Gemini o mais generoso (5 INCLUIR plenos;
QA≥3,5 em 11/22); ChatGPT o mais conservador (QA nunca acima do Claude);
achado central (sem MTTD/MTTR com baseline próprio) confirmado pelos três.
Duas regras de protocolo recomendadas: emendas no corpo normativo da ETAPA
1 dos prompts; destino do cluster humano sem aderência às RQs. Indexado em
reviews/README e DASHBOARD; **adendo datado (2026-10-25)** na síntese
consolidada sanando a limitação nº 1, PDF regenerado (274 KB). Commit
`52abc4b`.

### 90. Citações cruzadas do corpus ampliado (P01–P89)

**Prompt:** "Atualize as citações cruzadas do corpus para P01–P89".

**Ações:** Replicado o método do item 64 para os 88 artigos: IDs OpenAlex
resolvidos por DOI (88/88 + alias do preprint do P09),
`referenced_works` (OpenAlex) e listas `reference` (Crossref) cruzados com
o corpus. Scopus **PENDENTE** (sem chave) — contagens por fonte, PENDENTE ≠ 0. Criado **`citacoes-cruzadas-P01-P89.md`** (artefato novo; o histórico
P01–P40 ganhou nota de versão apontando para ele). **Resultados: 49 arestas
na união** (OA 48 · CR 45; vs. 26 no ciclo 1): hubs P10 (7), P09 (6 — com o
alias incluído na correspondência, OA/CR agora enxergam as citações que em
07/2026 só o Scopus via; 2 arestas novas P01→P09 e P55→P09), P14 (5) e o
novo hub **P65** (3). **P28 é o maior citador interno** (7 arestas, incl. 5
candidatos do ciclo 2: P52/P65/P72/P76/P77); o ciclo 2 cita o corpus de
volta (P79→P20/P78; P76→P39/P83; P43→P16/P18; P55→P09/P15) — lote tecido ao
corpus nas duas direções. Arestas entre excluídos também mapeadas
(P41→P45, P26→P68, P73→P80, P89→P65/P70). Indexado no README raiz e
DASHBOARD (link principal atualizado para a versão P01–P89). Links
verificados (0 quebrados; links `file:///` históricos do Gemini excluídos
do checador). Commit `d4f0061`.

### 91. Planilha do corpus de descoberta commitada; resume notes ignoradas

**Prompt:** "Commit o agentic_ir_corpus-claude-research.xlsx e adicione
claude-resume-history.txt ao .gitignore". (Pedido anterior "Faça o push e
commit" verificado: nada pendente — tudo já estava commitado
incrementalmente e master == origin/master.)

**Ações:** `agentic_ir_corpus-claude-research.xlsx` (176 KB, planilha do
ciclo de descoberta do usuário, na raiz desde 2026-09-06) commitado.
`.gitignore` ganhou `claude-resume-history.txt` e também `~$*` (locks
temporários do Excel, flagados no item 76 — pertinente agora que um xlsx é
versionado). Working tree limpo pela primeira vez desde o início do ciclo 2. Commit `c73fbb7`.

### 92. Prompts retroativos do corpus fundacional (P01–P19)

**Prompt:** "Agora preciso montar o prompt .MD para cada um dos artigo P01
até P19 usando como template os prompts que estão na pasta prompts."
(2026-10-26)

**Ações:** Gerados `prompts/prompt-P01.md` … `prompt-P19.md` (19 arquivos)
por script, a partir do template vivo `prompt-chatgpt-consultation.md`.
Adaptações: **CONTEXTO** reescrito para avaliação **retroativa de
padronização** — os fundacionais já estão incluídos (herança do Trabalho I)
e o prompt instrui explicitamente a NÃO rediscutir a inclusão, apenas medir
RQs/QA para tornar as Tabelas 3/5/7 comparáveis com P20–P88; **INSUMOS**
preenchidos com título, arquivo PDF (existência conferida nos 19),
**Qualis/SJR verificados de papers.csv (2026-07-27)** — citados como
verificados, não "[VERIFICAR]" — e linha nova `observacao_corpus`.
Indexados no README raiz (árvore de `prompts/` e seção Insumos: agora 61
prompts preenchidos). Links verificados (0 quebrados). Commit `4eaf0ce`.

### 93. Pareceres retroativos do corpus fundacional (P01–P19)

**Prompt:** "Sim, execute os 19 prompts e um por vez e gere os pareceres
review-P01 até P19 dentro da pasta reviews/".

**Ações:** Executados os 19 prompts em fan-out (3 ondas de 7/6/6 agentes,
um artigo por agente; sem quedas por limite desta vez), cada agente lendo o
prompt + modelo `review-P21.md` + PDF integral e gravando
`reviews/review-PNN.md`. Particularidades: Tabela A com bibliometria
verificada **nas três fontes** (papers.csv 2026-07-27, incl. Scopus — P01
anotado como NÃO INDEXADO), Etapa 1 = "FUNDACIONAL — inclusão herdada do
Trabalho I (não rediscutida)", e parecer final com **"STATUS: MANTIDO NO
CORPUS (fundacional)"** em vez de Incluir/Excluir. Validação por script:
19/19 íntegros. **Resultados:** SCORE_RQ médio 3,66 (mediana 4,0) · QA
médio 2,53 (mediana 2,5) · bandas 9 Alta / 10 Média — RQ alto e QA baixo,
coerente com o perfil de surveys conceituais; destaques P04 (4,5/3,5) e
P13 (4,0/3,5); QA mais baixos nos surveys amplos (P02/P06/P10/P14/P17 com
QA 1,5). Com isso, **todos os 60 estudos avaliados da RSL (P01–P88) têm
parecer padronizado** nas Tabelas 3/5/7. Tabela-síntese adicionada como
nova seção "Corpus fundacional — avaliação retroativa" em
reviews/README.md. Commit `2091253`.

### 94. Consolidação dos fundacionais (CSV + gráficos) e Gemini P01–P19

**Prompt:** "Sim, estenda o resultados-consolidados e os gráficos com as
linhas P01–P19".

**Ações:** Seguindo a convenção de imutabilidade, criado
`reviews/resultados-consolidados-fundacionais.csv` (19 × 23 colunas, mesmo
esquema dos ciclos; símbolos RQ/QA extraídos dos pareceres e **conferidos
por script contra os escores — 0 divergências**; Recomendacao = "Incluir
(mantido - fundacional)") e `reviews/charts-fundacionais/` (5 SVGs) +
`reviews/graficos-fundacionais.md`, gerados com cópia parametrizada do
`gen_charts.py` (categoria "Mantido — fundacional" adicionada à cópia).
Leitura: RQ alto × QA baixo; a lacuna de RQ3/QA3 (evidência de benefício) é
transversal aos três conjuntos. Indexado em reviews/README (bloco
fundacional) e DASHBOARD (nova seção "Corpus fundacional").
**Incidente/achado no commit:** o `git add reviews/` capturou **19
avaliações novas do Gemini (P01–P19)** que o usuário havia depositado em
`reviews/Gemini/` — validadas pós-commit e antes do push (19/19 com ID e
título corretos no corpo) e mantidas no mesmo commit: o conjunto Gemini
agora cobre P01–P88 (61 avaliações). Commit `2e52101`.

### 95. Consolidados por avaliador — P01–P88 (três fontes)

**Prompt:** "Agora já tenho os reviews... do Claude (review-P01 até
review-P88), Gemini... e os do ChatGPT... revise e atualize os arquivos de
resultados consolidados das três fontes avaliadoras."

**Ações:** Confirmado que os três conjuntos estão completos (61 avaliações
por avaliador; os **P01–P19 do ChatGPT** chegaram não rastreados e foram
validados — 19/19 com ID/título corretos — e commitados junto). Extraídos
por script escores/recomendações dos arquivos de terceiros que ainda não
estavam curados (GPT P01–P19; Gemini P01–P40), com inspeção dirigida dos
ambíguos (recomendações no corpo/cauda; Gemini fundacionais usam "Status:
FUNDACIONAL/INCLUÍDO"; Gemini-P38 decide ICR com alternativa Excluir;
GEM-P28 RQ 5,0 — o 4,6 extraído era ruído). Gerados **3 CSVs novos de 61
linhas** (IDs idênticos verificados): `resultados-consolidados-claude-
P01-P88.csv` (merge dos 3 CSVs oficiais + coluna Conjunto),
`-chatgpt-P01-P88.csv` e `-gemini-P01-P88.csv` (8 colunas: escores, banda
derivada do QA pela rubrica, recomendação, observação; `NA` onde o ChatGPT
parou na triagem por estrato). Dados do ciclo 1 (GPT) e ciclo 2 (GPT/GEM)
reutilizados dos CSVs de comparação existentes. CSVs por conjunto
permanecem como registros históricos. Indexado em reviews/README e
DASHBOARD. Commit `837fb70`.

### 96. Comparação global P01–P88 e Papers_Index enriquecido

**Prompt:** "Sim, compute a comparação global entre avaliadores P01–P88 e
atualize o Papers_Index.csv na raiz do repositório."

**Ações:** **(1) Comparação global** — computada sobre as 61 decisões × 3
avaliadores (fontes: os três consolidados do item 95). **Incidente
corrigido antes da publicação:** a 1ª rodada classificou errado as
recomendações do ChatGPT no ciclo 1 (grafadas em MAIÚSCULAS — "EXCLUIR DO
CORPUS PRINCIPAL" não casava com startswith("Excluir")), inflando as
divergências de 6 para 10; refeito com comparação case-insensitive e a
correção registrada no próprio documento. **Resultados:** acordo 90,2–91,8%
por par; κ CL×GPT 0,57 · CL×GEM 0,51 · GPT×GEM 0,51; **Fleiss 0,53**;
**53/61 decisões unânimes** (fundacionais 19/19; exclusões unânimes P30,
P39, P86); MAE: CL×GPT QA 0,31 (menor). As **8 divergências formam 3
famílias protocolares** — A: secundários não-agênticos (P26, P29); B:
emenda de estratos (P62, P69, P81 — só o ChatGPT exclui); C: fronteiras de
domínio/estrato (P38, P40 — só o Gemini inclui; P85 — só o Claude exclui) —
nenhuma de mérito (escores contam a mesma história; muda a regra aplicada).
Perfis: ChatGPT protocolar estrito · Gemini inclusivo/generoso · Claude
intermediário com corte temático mais duro. Artefatos:
`reviews/comparacao-avaliadores-global.md` + `.csv` (61 × 12). **(2)
Papers_Index.csv** atualizado in loco (pedido explícito): 88 linhas × 24
colunas — 10 novas: `Status RSL (2026-10-26)` (fundacional mantido /
incluído / excluído com motivo / excluído na triagem E2/E3) e
RQ/QA/Recomendação dos três avaliadores (— para os 27 excluídos na
triagem). Indexado em reviews/README, DASHBOARD e README raiz. Commit
`f28f8dc`.

### 97. Adendo da comparação global na síntese consolidada

**Prompt:** "Atualize a síntese consolidada com a comparação global e
commit".

**Ações:** Acrescentado o **Adendo (2026-10-26)** a
`reviews/relatorio-sintese-consolidado.md` (corpo histórico intocado;
rodapé atualizado para citar os dois adendos): registra os três marcos
pós-adendo anterior — avaliação retroativa dos fundacionais, conjuntos
completos dos três avaliadores (61 cada) e a comparação global (acordo
90,2–91,8%; Fleiss 0,53; 53/61 unânimes; 8 divergências em 3 famílias
protocolares) — e as implicações: seção 9 e limitações 1 e 6 do corpo
superadas; corpus central avaliador-independente (87% unânime); lista
fechada das 3 decisões de protocolo pendentes; achado central de MTTD/MTTR
confirmado pelos três avaliadores em todo o corpus. PDF regenerado
(282 KB). Commit `2b89358`.

### 98. Papers_Index.md — versão Markdown do índice

**Prompt:** "Crie uma versão markdown do arquivo Papers_Index.csv".

**Ações:** Gerado `Papers_Index.md` na raiz por script a partir do CSV
canônico (88 artigos, 24 colunas): duas tabelas unidas pelo Paper ID —
**Tabela 1** identificação/bibliometria (com DOI linkado ao doi.org e PDF
linkado a `docs/`, nomes URL-encoded; percentis multilinha achatados com
"·") e **Tabela 2** resultados da RSL (status + RQ/QA/recomendação dos 3
avaliadores). Nota explícita de que **o CSV é a fonte canônica** e o .md é
derivado (regenerar quando o CSV mudar); campo esparso
`classification_evidence` omitido por concisão (nota no rodapé). Validação:
176 linhas de tabela (88 × 2), 0 links de PDF quebrados. Indexado no README
raiz (árvore + seção Insumos). Commit `eb15fa4`.

### 99. Chave Scopus local e citações P41–P89 completas

**Prompt:** "API KEY Scopus está comigo, onde posso passar ela?" → "A chave
já está no arquivo .scopus_key, pode seguir".

**Ações:** Estabelecido o canal seguro: `.scopus_key` adicionado ao
`.gitignore` ANTES de a chave existir (commit `d12941f`); usuário criou o
arquivo via `!` (a chave nunca passou pela conversa; lida só do disco,
nunca ecoada — regra do CLAUDE.md). Buscadas as citações Scopus dos 49
candidatos P41–P89 por DOI: 46/49 na primeira rodada + 3 retries por
timeout (P51, P54, P58) = **49/49, todos ≥ 1, nenhum NÃO INDEXADO**.
`papers-ciclo2.csv` atualizado (coluna Citações Scopus + data "OA/CR
2026-09-09; Scopus 2026-10-26"); nota de pendência removida do README raiz.
Varredura de vazamento da chave: limpa. Commit `c9bc0fa`.

### 100. Coluna Scopus nas citações cruzadas P01–P89 (tripla checagem)

**Prompt:** "Atualize também as citações cruzadas com a coluna Scopus".

**Ações:** Varredura `REF("<título>") AND (DOI(...) OR ...)` para os 88
alvos. **Incidentes e diagnóstico:** duas varreduras completas falharam com
HTTP 400 "Exceeds the maximum number allowed for the service level" — após
sondagens contraditórias (blocos de 30 OK na calibração; até n=8 falhando
no lote) isolou-se o parâmetro: **`count ≤ 25` é o limite do nível de
serviço da nova chave** (a calibração usava count=25 e o lote count=50) —
quirk documentado no método do documento. **Correção de dado:** o título do
P14 no Papers_Index traz o sufixo "(Kshetri)", que zerava o REF() —
consulta refeita com o título real (recuperou os 5 citadores).
**Resultados:** Scopus **48 arestas** (0 erros), **3 exclusivas** (P54←P06,
P54←P15, P16←P29) e 4 invisíveis (P01→P09/P10 — citador não indexado;
P79→P20 e P28→P76 — não resolvidas por título). **União final: 52
arestas**; P16 e P65 consolidados como hubs (3 cada).
`citacoes-cruzadas-P01-P89.md` regravado com a coluna Scopus e marcadores
por fonte (†/‡/§); README raiz e DASHBOARD atualizados; varredura de chave
limpa. Commit `81bd595`.

### 101. Adendo nº 3 na síntese consolidada — tripla checagem Scopus

**Prompt:** "Atualize a síntese consolidada com a tripla checagem e commit".

**Ações:** Acrescentado o **Adendo (2026-10-26, nº 3)** a
`reviews/relatorio-sintese-consolidado.md` (corpo e adendos anteriores
intocados): registra o fechamento das duas pendências bibliométricas
(citações por estudo 49/49 ≥ 1 em três fontes; citações cruzadas com união
de 52 arestas e 3 exclusivas do Scopus, destaque P54←P06/P15), o registro
metodológico dos dois quirks novos da API (`count ≤ 25` por nível de
serviço; sufixos editoriais em títulos zeram o REF() — caso P14) e declara
**superada a limitação nº 4** do corpo — restando só as 3 decisões de
protocolo (adendo nº 2) e a confirmação opcional de Qualis na Sucupira.
PDF regenerado (312 KB). Commit `803bef6`.

### 102. Draft v1 do artigo IEEE Access (LaTeX, inglês)

**Prompt:** "Preciso submeter um artigo de RSL seguindo Kitchenham et al.
(2009) para a IEEE Access, com o tema 'Agentic AI as a copilot to reduce
MTTD and MTTR during incident response'... carga cognitiva como bônus...
Gere primeira versão do artigo em Latex no idioma inglês, com a formatação
IEEE, trazendo o conteúdo dos artigos, as avaliações, revisões e PICOC."

**Ações:** Criada a pasta `artigo/` com: **`main.tex`** — artigo completo
em inglês, classe IEEEtran em modo journal (nota no fonte e no README:
trocar por `ieeeaccess.cls` oficial na submissão), ~7 seções: Introduction
(5 contribuições), Background (AIOps→Agentic, hubs), Method (PICOC com
regra v1.1.0, RQ1–RQ5, string validada 13/14 em 2 bases, critérios
I1–I6/E1–E5 com a emenda de estratos, PRISMA dos 2 ciclos em tabela,
QA/DARE, protocolo de 3 avaliadores), Results (taxonomia do corpus 53 em
tabela, migração do gap RQ4→RQ3/QA3, **seção central de MTTD/MTTR** com
P76/P79/P73/P81/P87/P83, cluster de carga cognitiva, citações cruzadas 52
arestas, κ global em tabela), Discussion (o que a evidência sustenta;
por que o gap persiste; implicações; lições metodológicas de SLR com
LLMs), Threats to Validity e Conclusion; **`referencias.bib`** — 62
entradas de estudos geradas do Papers_Index.csv (15 listas de autores
faltantes completadas via Crossref; P65 adicionado após validação de
chaves: 48 \cite, todas resolvidas) + 6 metodológicas; **`README.md`** da
pasta com proveniência seção→artefato e TODOs de submissão (classe
oficial, coautor orientador, figuras PRISMA/gráficos, 3 regras de
protocolo, revisão de inglês). pdflatex não está instalado na máquina —
draft validado estruturalmente, instruções de build no README. Indexado
no README raiz (árvore + "Comece por aqui"). Commit `fa8abfb`.

### 103. LaTeX instalado e artigo compilado (main.pdf, 6 páginas)

**Prompt:** "Instale o pdflatex e compile o artigo para validar".

**Ações:** **Incidente de instalação:** o BasicTeX via Homebrew cask falhou
silenciosamente (o instaldor `.pkg` exige senha sudo interativa,
indisponível na sessão — /Library/TeX nunca foi criado). **Solução:**
**TinyTeX** instalado no diretório do usuário sem sudo
(`~/Library/TinyTeX/`; apenas o ajuste de PATH, opcional, pedia sudo —
contornado usando o caminho completo dos binários). `tlmgr update --self`
(exigido pelo repositório) + `tlmgr install ieeetran` (classe e .bst).
Compilação completa (pdflatex → bibtex → 2× pdflatex): **`artigo/main.pdf`
com 6 páginas (173 KB), 0 citações não resolvidas, 0 overfull boxes, 0
avisos de BibTeX**. Artefatos de build (aux/log/bbl/blg/out) adicionados
ao .gitignore; PDF versionado; README do artigo atualizado com o registro
da validação. Commit `b9e7b95`.

### 104. Figura PRISMA (TikZ) no artigo

**Prompt:** "Gere a figura do diagrama PRISMA para o artigo".

**Ações:** Criada a **Fig. 1** do artigo em TikZ nativo (vetorial), como
`figure*` de página inteira: duas colunas paralelas (Ciclo 1: ≈51→21→20→18
→14; Ciclo 2: 49→49→22→20, com caixas laterais de exclusão E1/E2/E3 e a
nota da emenda de estratos) convergindo com o corpus fundacional (n=19)
para o **corpus consolidado n=53**; legenda registra a evidência PICOC das
exclusões da triagem. Texto do método atualizado para referenciar
Fig.~1 + Tabela. **Incidentes de build corrigidos:** (i) faltava a
biblioteca `calc` do TikZ (coordenadas `$(a)!0.5!(b)$`); (ii) fonte
Courier ausente no TinyTeX (`tlmgr install courier` — exigida pelos
`\texttt` do texto); (iii) figura 427pt mais larga que o texto —
envolvida em `\resizebox{\textwidth}`. Build final: **7 páginas, 0 erros,
0 overfull, 0 indefinidos**. README do artigo atualizado (TODO da figura
marcado como feito). Commit `2afd172`.

### 105. Designação do autor ajustada no artigo

**Prompt:** "Ajuste o Graduate Student to Master Degree Student".

**Ações:** Linha `\author` do `artigo/main.tex` alterada de
`\IEEEmembership{Graduate Student}` para `\IEEEmembership{Master Degree
Student}`; PDF recompilado (7 páginas, 0 erros, 0 overfull). Commit
`99c31d6`.

### 106. Consulta — reaproveitamento do Trabalho I no artigo IEEE

**Prompt:** "o que eu posso aproveitar em termos de formatação, diagramas,
conteúdo do primeiro artigo TrabalhoI/Artigo_Agentic_AI V3.pdf? A ideia é
enriquecer e tornar este artigo mais robusto... nos aspectos de redução de
carga cognitiva com o uso de agentic ai."

**Ações:** Consulta (sem alteração de artefatos). Analisadas as fontes
LaTeX do Trabalho I (template SBC 12pt pt-BR; 2 PNGs: google-trends e
mapa-de-ligação; 8 tabelas; lacunas em 6 eixos). **Recomendações
entregues:** aproveitar (1) os 6 eixos de lacunas (execução autônoma
segura; traces; integridade de memória; governança/shadow agents; causal
vs. correlação; eficiência) cruzados com a evidência dos ciclos 1–2 na
Discussion; (2) a narrativa de carga cognitiva da introdução, promovendo o
outcome a co-primário com subseção/tabela "cognitive-load measurement
toolbox" (NASA-TLX/P69, BUS-15/P63, reaction-time/P81); (3) redesenhar o
mapa de ligação como Fig. 2 em TikZ usando o grafo de 52 arestas; (4)
padrões das Tabelas 3/5/7 como apêndice dos 53 incluídos; (5) tabela da
rubrica QA no método. NÃO aproveitar: template SBC, texto pt-BR (reescrever
citando o Trabalho I como prior review — evita autoplágio) e números
antigos. Priorização sugerida: 1–3 primeiro.

### 107. Artigo enriquecido — toolbox, eixos de lacunas e Fig. 2

**Prompt:** "Sim, implemente nessa ordem".

**Ações:** Implementadas as 3 prioridades do item 106 no `artigo/main.tex`:
**(1)** §IV-D reescrita elevando carga cognitiva a outcome co-primário,
com a **Tabela IV "cognitive-load measurement toolbox"** (NASA-TLX,
fisiológico multimodal, reaction time, exposição a alertas, BUS-15 —
cada instrumento com evidência do corpus e uso recomendado com copilot);
**(2)** nova §V-B "Research gaps consolidated across both reviews" — os 6
eixos do Trabalho I cruzados com a evidência dos ciclos (eixos i/iii/vi
identificados como os menos servidos; sétimo eixo adicionado: outcomes de
carga cognitiva medidos); **(3)** **Fig. 2** — rede de citações internas
em TikZ gerada programaticamente do grafo final (44 nós em layout
circular agrupado por ciclo, 52 arestas, hubs ≥3 destacados, legenda).
**Incidentes de build:** (a) âncora de inserção com quebra de linha
("alias\nresolution") fez o primeiro replace falhar silenciosamente —
detectado porque a compilação "limpa" rodou sem a figura; (b) legenda em
`\matrix` quebrou com "Single ampersand used with wrong catcode" —
substituída por nós simples; (c) o replace da legenda cortou no `};`
errado deixando fragmento órfão (44 erros) — removido. Build final:
**8 páginas, 0 erros, 0 overfull, 0 indefinidos**. README do artigo
atualizado. Commit `c7c2352`.

### 108. Fig. 3 — cobertura de RQs por conjunto

**Prompt:** "Gere os gráficos opcionais de RQ coverage para o artigo".

**Ações:** Computada do zero (dos 3 CSVs oficiais do Claude) a distribuição
T/P/N por RQ por conjunto — Fundacionais n=19, Ciclo 1 n=18, Ciclo 2 n=22
— e gerada programaticamente a **Fig. 3** em TikZ: barras empilhadas
normalizadas (5 grupos de RQ × 3 barras F/C1/C2; T cinza-escuro, P
cinza-claro, N branco; legenda), inserida na §IV-B com referência no
texto. Os dados sustentam a narrativa com precisão: RQ3 pleno em 1/19
(fundacionais), 12/18 (ciclo 1 — núcleo empírico) e 4/22 (ciclo 2); RQ4
é o gap do ciclo 1 (4/18); RQ5 forte nos três. Build: 8 páginas, 0 erros,
0 overfull. README do artigo atualizado (Figs. 1–3 concluídas — TODO de
figuras encerrado). Commit `c579d38`.

### 109. Regras de protocolo R1–R3 ratificadas no artigo

**Prompt:** "Aplique as 3 decisões de protocolo pendentes no artigo".

**Ações:** As 3 famílias de divergência da comparação global foram
ratificadas como **regras formais R1–R3**, consistentes com os vereditos
oficiais já publicados do corpus, em nova subseção do método (§III-E
"Ratified protocol rules"): **R1** — secundários não-agênticos excluídos
do corpus primário independentemente de qualidade; secundários centrados
em Agentic AI mantidos como fundacionais-condicionais; **R2** — emendas
de elegibilidade só vinculam quando escritas no texto normativo da Etapa
1 (não nos insumos); emenda de estratos do ciclo 2 ratificada com
ressalva obrigatória; **R3** — corte de domínio estrito; cluster humano
mantido exclusivamente como evidência complementar do outcome de carga
cognitiva (nunca alimenta RQ1/RQ2/RQ4); exclusão por não-aderência às
RQs mantida. Seção de confiabilidade e Threats atualizadas ("would
eliminate"/"planned next step" → regras ratificadas e referenciadas).
Build: 8 páginas, 0 erros. TODO nº 4 do artigo encerrado — restam só
classe oficial da Access, coautor orientador e revisão de inglês. Commit
`62bfc4f`.

### 110. Troca da IEEEtran pela classe oficial da IEEE Access

**Prompt:** "Troque a classe IEEEtran pelo template oficial da IEEE Access".

**Ações:** O template oficial não existe no CTAN/tlmgr (`tlmgr install
ieeeaccess` falha; página CTAN 404) — localizado via busca web o zip
oficial `ACCESS_latex_template_20260513-1-1.zip` em ieeeaccess.ieee.org.
Copiados para `artigo/`: `ieeeaccess.cls`, `spotcolor.sty`, 16 fontes
.pfb + 16 .tfm + 4 .map + 4 .fd (Formata/Giovanni/Times) e 3 logos
(`logo.png`, `notaglinelogo.png`, `bullet.png`). Front matter do
`main.tex` reescrito nas convenções da Access: `\history` (draft, não
submetido), `\doi{10.1109/ACCESS.2026.DOI}`, autor em `\uppercase` +
`\authorrefmark{1}` + `\IEEEmembership{Master Degree Student}`,
`\address[1]`, `\tfootnote`, `\corresp`, ambiente `keywords`,
`\titlepgskip=-21pt`, `\maketitle` após keywords, `\PARstart`, `\EOD`;
`hyperref` removido (incompatível com a classe).

**Incidente (root cause):** primeira compilação com a classe gerou
cascata de 58 erros "Missing number, treated as zero" dentro de
`pgfmathfunctions.random.code.tex` — causa isolada na **linha 512 da
`ieeeaccess.cls`**, que redefine o primitivo TeX `\year` como macro
(`\def\year#1{\gdef\theyear{#1}}`), quebrando o seed do RNG do pgf
(`\multiply...by\year`). Tentativa de carregar tikz antes da classe
causou option clash de graphics + erros do spotcolor. **Fix final:**
shim no preâmbulo — salvar a macro da classe, `\def\year{\pdfprimitive
\year}` ao redor de `\usepackage{tikz}`, restaurar a macro depois.
Dependências novas instaladas via tlmgr: `grfext`, `cite`, `textcomp`,
`algorithms`. Os 22 `Overfull \hbox` (~505pt) restantes em `\output`
foram provados benignos por bissecção com o sample oficial: sample puro
= 0 overfull; sample + tikz = 21 — artefato cosmético do hook de
shipout do pgf medindo as caixas de cabeçalho do template.

**Resultado:** `main.pdf` com **9 páginas, 0 erros, 0 citações não
resolvidas**; página 1 verificada via pypdf (ABSTRACT, INDEX TERMS,
título, autor e "Corresponding author" presentes). `artigo/README.md`
atualizado (TODO nº 1 encerrado; workaround e aviso benigno
documentados). Commit `d1dd7ea` (48 arquivos). Restam no TODO:
biografia/foto do autor, coautor orientador e revisão de inglês.

### 111. Orientador como coautor e e-mails do autor correspondente

**Prompt:** "Adicione o orientador como coautor no artigo Rafael Kunst
(Prof. Doutor do PPGCA da Unisinos - RAFAELKUNST@unisinos.br) e na minha
identificação pode incluir valdomiro.souza@gmail.com".

**Ações:** `artigo/main.tex` — Prof. Dr. Rafael Kunst adicionado como
segundo autor com a mesma afiliação (`\authorrefmark{1}`,
PPGCA/Unisinos), e-mail rafaelkunst@unisinos.br na `\address[1]`;
placeholder TODO de coautor removido. Identificação do autor
correspondente passou a listar os dois e-mails (valdomirojr@gmail.com e
valdomiro.souza@gmail.com) na `\address` e no `\corresp`. Running head
(`\markboth`) atualizado para "Souza Jr. and Kunst: …" e Acknowledgments
ajustados para plural ("The authors thank…"). Recompilado: 9 páginas,
0 erros, 0 citações não resolvidas; verificação via pypdf — RAFAEL
KUNST, os dois e-mails e rafaelkunst@unisinos.br presentes na página 1;
running head com os dois nomes confirmado na página 2. TODO nº 2 do
`artigo/README.md` encerrado. Commit `dc84850`. Restam no TODO:
biografia/foto dos autores e revisão de inglês.

### 112. Biografias dos autores no artigo

**Prompt:** "Agora adicione as biografias dos autores no artigo. A
minha está aqui bio/ValdomiroSouza.pdf".

**Ações:** Duas seções `IEEEbiographynophoto` adicionadas ao final do
`main.tex` (antes do `\EOD`), ambiente nativo confirmado na
`ieeeaccess.cls`. A biografia do autor foi **redigida em estilo IEEE
(terceira pessoa, ~150 palavras)** a partir do export do LinkedIn em
`bio/ValdomiroSouza.pdf` (lido via pypdf): formação em Gestão de TI
(Unisinos, 2025) + mestrando do PPGCA; 30+ anos em tecnologia; Head of
IT da BU CPaaS da Zenvia (desde 2013) com plataformas de 1M+
transações/min; SRE org de 9 squads, postmortems, migrações
zero-downtime, ISO 27001; interesses de pesquisa alinhados à RSL. A
biografia do orientador (Prof. Dr. Rafael Kunst) foi redigida a partir
do **perfil público acadêmico** (busca web — SciProfiles/Loop/Unisinos):
M.Sc. e Ph.D. em Ciência da Computação pela UFRGS; professor e
coordenador do PPGCA/Unisinos; SOFTWARELAB; professor visitante no IBM
Watson IoT Center (Munique, 2020); consultor ad hoc do MEC; interesses
em 5G/6G, Industry 4.0, smart cities, IoT e ML aplicado a telecom.
Recompilado: **9 páginas, 0 erros**; ambas as biografias verificadas na
última página via pypdf. Pasta `bio/` nova indexada na árvore do README
raiz; TODO nº 1 do `artigo/README.md` atualizado (restam só as **fotos**
— trocar para `IEEEbiography` com `\includegraphics` quando houver).
Commit `843a041`.

### 113. Revisão de inglês do artigo

**Prompt:** "Agora faça a revisão de inglês do artigo".

**Ações:** Leitura integral do `main.tex` (~1090 linhas) e aplicação de
~20 correções, em três categorias. **(a) Gramática/idiomaticidade:**
"The review makes three findings" → "yields three main findings";
"organized in a taxonomy" → "organized into"; "no own baseline" → "no
baseline of its own"; "applied already at screening" → "applied as early
as the screening stage"; "Three corpus-visible causes:" (fragmento) →
"Three causes are visible in the corpus:"; "The one nominal measurement
available being unfavorable…" → "That the only available nominal
measurement is unfavorable…"; "evidencing" → "indicating"; "material
for" → "material to"; "not established effects" → "not as established
effects"; "corpus'" → "corpus's"; "a bag of papers" → "a disconnected
collection of papers"; "Master Degree Student" → "Master's Degree
Student"; "PoC" expandido para "proof-of-concept" (2 ocorrências).
**(b) Convenção IEEE:** "catalogue" → "catalog" (ortografia americana);
"Acknowledgments" → "Acknowledgment" (singular, padrão IEEE).
**(c) Correções semânticas:** rotulagem do κ corrigida — "substantial
agreement" estava estatisticamente incorreto para κ 0.51–0.57/0.53
(banda _moderate_ em Landis & Koch): §V-E agora diz "high percentage
agreement (90.2–91.8% pairwise) with moderate chance-corrected κ" e a
Conclusão "high agreement (53 of 61 decisions unanimous)"; e
"co-primary" em §IV-D trocado por "complementary", alinhando ao abstract
e à tabela PICOC (que tratam carga cognitiva como _complementary
outcome_). Nenhum número ou achado técnico alterado. Recompilado:
**9 páginas, 0 erros, 0 citações não resolvidas**; todas as frases
novas verificadas no PDF via pypdf (com desifenização) e ausência dos
trechos antigos confirmada. Commit `4cc4c97`. TODO do artigo: resta só
a verificação final das contagens contra os CSVs e as fotos dos autores.

### 114. Conferência de contagens do artigo contra os CSVs canônicos

**Prompt:** "Faça a conferência de contagens".

**Ações:** Auditoria por script Python recomputando ~40 números do
artigo a partir dos artefatos canônicos. **Conferiram (OK):** universo
P01–P89 (88 linhas + P36 duplicata); 61 avaliações (19 F + 20 C1 + 22
C2); 53/61 unânimes (86,9% ≈ 87%); acordos de pares 90,2/91,8/91,8% e
κ 0,57/0,51/0,51; Fleiss κ 0,53; prevalência Incluir 164/183 = 89,6%
(regra de colapso oficial: "Mantido (fundacional)" = Incluir,
case-insensitive); diffs médios |RQ| 0,44/0,55/0,63 e |QA|
0,31/0,50/0,63 (pares com NA excluídos); 8 divergências nas famílias
A = P26, P29 (2) · B = P62, P69, P81 (3) · C = P38, P40, P85 (3);
médias C1 RQ 3,83/QA 3,50 e F RQ 3,66/QA 2,53; cobertura de RQs da
Fig. 3 (RQ3 fully 1/19 F, 12/18 C1, 4/22 C2; RQ4 fully 4/18 C1);
corpus 53 = 19+14+20; 7 fundacionais-condicionais (P24, P33, P52, P54,
P72, P77, P79); corpus primário 46; 3 incluídos com ressalva de
estrato (P62, P69, P81); exclusões unânimes P30, P39, P86; PRISMA do
ciclo 1 (≈51→21→20→18→14) e ciclo 2 (49→22→20; E2=19, E3=8) contra
PRISMA.md e Papers_Index; taxonomia (36 citados, todos no corpus);
rede de citações — 52 arestas na união do md == 52 arestas da Fig. 2
do tex, hubs P10=7/P09=6/P14=5/P16=3/P65=3, P28 com 7 saídas (5 para o
ciclo 2), P79→P20,P78, P76→P39,P83; string de busca (≈49.700 OpenAlex,
12.783 Scopus, recall 13/14); números de MTTD/MTTR e carga cognitiva
(277d = 204+73, 8h→90min, 98%/<5min, ~1–1,5min vs ~30–45s, 74–84%,
276→107s com Wilcoxon, 2,9–11,6s + 0,3s, BERTScore 85–87%, AUC 0,998,
NASA-TLX, BUS-15) contra a síntese consolidada; bib 62 corpus + 6
metodológicas, zero \cite sem entrada.

**3 divergências encontradas e corrigidas no artigo:** (1) média QA do
ciclo 2 é **2,73** (60,0÷22, idêntica nos dois CSVs), não 2,75 — o
DASHBOARD exibia a **mediana** (2,75) como média e o artigo herdou;
corrigido no `main.tex`, no DASHBOARD (valor + nota datada) e via seção
**Errata (2026-10-27)** na síntese consolidada (artefato histórico não
reescrito), com PDF da síntese regenerado (errata verificada via
pypdf); (2) "(QA 4.0/4.0)" atribuído ao núcleo empírico que inclui P28
e P31 com QA 3,5 → "(QA 3.5–4.0 of 4.0)"; (3) a composição do n=61
agora é explícita no método (19 F + 20 C1 triados, incluindo os 2
inelegíveis de estrato avaliados como exclusões + 22 C2), eliminando a
aparente tensão com os "18 assessed" do PRISMA do ciclo 1.
Recompilado: 9 páginas, 0 erros; "mean QA 2.73" e a frase do n=61
verificadas no PDF. TODO nº 5 do `artigo/README.md` encerrado — do
artigo restam apenas as fotos dos autores. Commit `12f0758`.

**Incidentes:** primeira rodada do script divergiu em κ/prevalência por
regra de colapso incompleta (rótulo "Mantido (fundacional)" do Gemini
não começa com "Incluir") — corrigida replicando o mapeamento documentado
no próprio `comparacao-avaliadores-global.md`; scores `NA` (P39/P40 no
Claude; P62/P69/P81/P86 no ChatGPT) exigiram médias NA-safe, como no
documento oficial.

### 115. Biografia do autor substituída por texto fornecido pelo autor

**Prompt:** "Ajuste a minha Bio no artigo para VALDOMIRO DE OLIVEIRA
SOUZA JR. received the B.S. degree…" (texto integral fornecido).

**Ações:** A biografia do primeiro autor em `artigo/main.tex` foi
substituída integralmente pelo texto fornecido pelo autor: nome por
extenso no argumento do ambiente (`Valdomiro de Oliveira Souza Jr.`),
B.S. em Gestão de TI (Unisinos, 2025), trajetória 1997–2012 (incluindo
Pure Bros, adquirida pela Zenvia em 2013), Head of Information
Technology desde 2025, SRE org de 35 engenheiros em 9 squads, ISO/IEC
27001 em 2022, integração técnica de dez empresas adquiridas e
interesses de pesquisa (agentic AI, AI-assisted incident response,
MTTD/MTTR, carga cognitiva). Adaptações apenas tipográficas: acentos em
LaTeX (`S\~ao`), `B.S.\`/`M.Sc.\` com espaço forçado, `ISO/IEC~27001`.
Recompilado: 9 páginas, 0 erros; nome, Pure Bros, ISO/IEC 27001 (2022),
"ten acquired companies" e "mean time to recover (MTTR)" verificados no
PDF via pypdf. Commit `3d54c6c`.

### 116. Nome por extenso no byline e no corresponding author

**Prompt:** "Alinhe o nome por extenso no byline também".

**Ações:** "Valdomiro de O. Souza Jr." → "Valdomiro de Oliveira Souza
Jr." nas duas ocorrências restantes do `main.tex`: o `\author` (byline
da primeira página) e o `\corresp` (nota de autor correspondente),
alinhando com a biografia (item 115). Running head (`\markboth`)
permanece "Souza Jr. and Kunst" (sobrenome apenas, convenção IEEE).
Recompilado: 9 páginas, 0 erros; byline e corresp por extenso
verificados na página 1 via pypdf, nenhuma ocorrência abreviada
restante. Commit `1a0af97`.

### 117. Placeholder de volume/ano no rodapé

**Prompt:** "no rodapé Volume 11, 2023 troque para Volume NN, YYYY".

**Ações:** O rodapé "VOLUME 11, 2023" vem dos defaults da
`ieeeaccess.cls` (`\def\thevol{11}` / `\def\theyear{2023}`, linhas
509–510), com setters `\vol{}` e `\year{}` — esta última é exatamente a
macro do workaround do item 110 (restaurada após o load do tikz, por
isso funciona normalmente no corpo). Adicionados `\vol{NN}` e
`\year{YYYY}` logo após `\begin{document}` no `main.tex`, sem tocar na
classe oficial. Recompilado: 9 páginas, 0 erros; "VOLUME NN, YYYY"
presente no PDF e nenhum "VOLUME 11, 2023" restante. Commit `69e1563`.

### 118. PDF final para revisão visual do autor

**Prompt:** "Gere o PDF final do artigo para eu revisar visualmente".

**Ações:** Rebuild limpo (aux/bbl/blg/log/out removidos antes) com o
ciclo completo pdflatex → bibtex → pdflatex ×2. Validação: **0 erros
LaTeX, 0 citações indefinidas, 0 warnings de BibTeX, 9 páginas**;
conferidos via pypdf a página 1 (ambos os autores por extenso, ABSTRACT,
INDEX TERMS), o rodapé "VOLUME NN, YYYY" e as biografias na última
página. PDF aberto no visualizador do autor (`open artigo/main.pdf`)
para a revisão visual — a conferência de layout/figuras renderizadas é
do autor, pois a validação via pypdf cobre apenas o texto extraído.
Commit `1af8058` (PDF regenerado).

### 119. Consulta: melhorias do Spec-Agentic-SDLC replicáveis para um Template de RSL

**Prompt:** "Leia o repositório https://github.com/valdomirosouza/Spec-Agentic-SDLC
e avalie quais melhorias poderiam ser replicadas neste repositório…
para transformá-lo em um Template para RSL".

**Ações:** Clone raso do repo no scratchpad e leitura dos artefatos
estruturais (README, CITATION.cff, CUSTOMISING, `memory/constitution.md`,
`check-corpus.sh`, `corpus-check.yml`, `adopt.sh`, CLAUDE.md, estrutura
de skills/ADRs/templates). Avaliação entregue no chat (consulta — nada
implementado): mapa conceitual SDLC→RSL (constitution→protocolo
normativo; ADRs→registros de decisão de protocolo numerados;
check-corpus→validação determinística de links/índices/contagens contra
os CSVs; sdd-skills→skills por etapa do ciclo RSL;
render-commands→renderização dos prompts por avaliador a partir de um
template canônico; adopt.sh→bootstrap do template com camadas;
CITATION.cff; templates/ central; CHANGELOG do protocolo;
hooks de guarda→imutabilidade de artefatos históricos e varredura de
segredos) e lista do que NÃO replicar (compliance corporativo, SRE/
runbooks, harness de produto, multi-IDE). Recomendação: extrair um repo
**Template-RSL** novo com este repositório como "worked example",
priorizando CI de validação, templates canônicos e skills do ciclo.

### 120. Esqueleto do Template-RSL criado

**Prompt:** "Sim, crie o esqueleto do Template-RSL para eu revisar".

**Ações:** Criado o repositório irmão **`~/Projects/Template-RSL`** (33
arquivos, commit inicial local `24bf3c3`; sem remote — criação no GitHub
fica a cargo do autor). Estrutura: `protocolo/` (constituição com 9
artigos extraídos das convenções desta pesquisa — PICOC/Comparison
empírico, emendas só no texto normativo, 3 avaliadores, SCORE_RQ/QA,
bibliometria por fonte, imutabilidade de históricos, números derivam de
CSV, segredos fora do repo, rastreabilidade; PICOC e critérios I1–I6/
E1–E5 com placeholders; `pdr/` com template e PDR-0001 de exemplo
narrando a emenda de estratos e a lição da regra R2); `templates/`
(prompt de avaliação canônico com marcadores {{...}} e seção de texto
normativo, prompt de extração PICOC, parecer, triagem, headers dos 3
CSVs canônicos); `scripts/` (`check-rsl.sh` com checks C1 links, C2
índice de PDRs contíguo, C3 indexação de artefatos, C4 varredura de
segredos, C5 parecer-a-parecer vs CSV; `render-prompts.py`;
`derive-index.py`; `compute-kappa.py` com a regra de colapso e o
tratamento de NA validados no item 114); 6 skills `.claude/skills/rsl-*`
(descoberta, triagem, extração, avaliação, consolidação, comparação —
cada uma amarrada ao WORKFLOW e à constituição); CI
(`.github/workflows/rsl-check.yml`); `WORKFLOW.md` (tabela das 9 etapas
com skills/entradas/saídas); `adopt.sh` (instancia tema/autor/data e
cria a estrutura de dados); CITATION.cff, CHANGELOG, LICENSE MIT,
`docs/estrutura.md` e `docs/worked-example.md` (mapa etapa→artefato
desta pesquisa + 5 lições que viraram regra). **Validação:**
`check-rsl.sh` passou no próprio template; smoke tests dos 4 scripts OK
(render preencheu marcadores/emendas/ressalvas; derive gerou MD; kappa
reproduziu colapso, NA-safe e divergências; adopt --dry-run).

### 121. Repositório Template-RSL criado no GitHub

**Prompt:** "Crie o repositório no GitHub e faça o push".

**Ações:** A criação como repositório **público** foi negada pelo
classificador de permissões do Claude Code ("Create Public Surface");
caminho mais seguro adotado: criado como **privado** —
`https://github.com/valdomirosouza/Template-RSL` (PRIVATE, branch
master), push do commit inicial `24bf3c3` (33 arquivos) via
`gh repo create --private --source . --push`. Tornar público fica a
cargo do autor (`gh repo edit valdomirosouza/Template-RSL
--visibility public` ou pela UI), decisão deliberadamente humana.

### 122. Template-RSL aplicado neste repositório (beta test)

**Prompt:** "Aplique o Template-RSL no repo ~/Projects/Unisinos-Mestrado-
TrabalhoII e vamos usar este repo com Beta Tester."

**Ações:** `adopt.sh --here` executado contra este repositório
(tema/autor reais) e a camada instanciada com os dados da pesquisa:
`protocolo/constituicao.md` (RQs reais preenchidas), `protocolo/picoc.md`
(PICOC ratificado, apontando para a string canônica em `picoc/`),
`protocolo/criterios.md` (I1–I6/E1–E5 reais + R1–R3 com links),
**PDR-0001..0005** (registro retroativo: regra Comparison v1.1.0; emenda
de estratos 2026-09-09; R1; R2; R3 — cada um com contexto, decisão e
consequências rastreáveis às famílias de divergência), CHANGELOG do
protocolo, CITATION.cff da instância (dataset; Souza Jr. & Kunst),
LICENSE MIT, WORKFLOW, skills `/rsl-*`, scripts e CI `rsl-check.yml`.
Removidos da instância: `adopt.sh`, `docs/worked-example.md`
(auto-referente) e o PDR de exemplo. **Dívida de indexação paga:**
READMEs-índice gerados para `prompts/` (61), `reviews/ChatGPT/` e
`reviews/Gemini/` (61 cada, preservando a nota histórica do rename
P84→P85 por referência), 3 pastas de charts, `reviews/scripts/`,
`picoc/` e `docs/` (aponta para `Papers_Index.csv` como índice canônico).
README raiz com a árvore atualizada. **Validações:** `check-rsl.sh` **OK**
nos 5 checks sobre o repositório inteiro; `compute-kappa.py --evaluators
Claude,ChatGPT,Gemini` **reproduziu exatamente** a comparação global
publicada (90,2/91,8/91,8%; κ 0,57/0,51/0,51; Fleiss 0,53; prevalência
89,6%; diffs 0,44–0,63/0,31–0,63; as 8 divergências). Commit `7f925a3`
(43 arquivos).

**Beta findings → 4 correções no Template-RSL** (commit `b6b410b`,
CHANGELOG 0.1.1): `adopt.sh --here` não copiava os arquivos do template;
C1 não decodificava links percent-encoded e marcava `file:///` históricos
como quebrados (agora ignora qualquer esquema de URI); C1/C3 passam a
varrer só arquivos rastreados pelo git (`.DS_Store` fora) e o C3 aceita
índices em READMEs de subpasta; `compute-kappa.py` ganhou `--evaluators`.

### 123. Ciclo 3 iniciado — descoberta via query canônica (P90–P126)

**Prompt:** "Execute o /rsl-descoberta para iniciar o ciclo 3, mas antes
me explique o que é o ciclo 3?" (explicação dada: nova rodada da update
review para capturar o publicado/indexado após o fechamento da
descoberta do ciclo 2, ~2026-09-07).

**Ações (skill `/rsl-descoberta`, primeira execução sob o Template-RSL):**
5 varreduras via API com a string canônica do PICOC — OpenAlex
`title_and_abstract.search` (O: A∩B∩C 2020+ = 207, todos; R: A∩B
2026-06+ top-100 relevância; R2: A∩B 2026+ top-100 citações) e Scopus
`TITLE-ABS-KEY` por bloco (O: 177, todos; R: PUBYEAR>2025, 100). Funil:
684 brutos → 584 únicos (dedup DOI/título vs. P01–P89 e entre bases) →
435 pré-filtro de título → 218 após corte de tipo (E5/I2) → **37
candidatos admitidos (P90–P126)** em triagem manual de título; classes
de não-admissão documentadas (Zenodo/repositório, veículos frágeis,
duplicatas, off-domain). **Recall de calibração (por DOI):** 24/34
incluídos dos ciclos 1+2; perdas esperadas por design (P24, cluster
humano P62/63/69/81, descoberta dirigida do ciclo 2) + **achado novo:
P21 não casa mais o bloco B no abstract da OpenAlex** (casava em
2026-07; bisseção A✓/B✗ — mudança de indexação da base; 12/14 no
conjunto do ciclo 1). Volume A∩B 2020+ hoje: 14.952 na forma usada vs.
≈49.700 em 2026-07 (forma da query + evolução da base; registrado).
**Entregas:** 37 linhas novas no `Papers_Index.csv` (autores via
OpenAlex/Crossref; citações POR FONTE no relatório — coluna datada de
2026-09-06 deixada vazia por ser snapshot histórico); `Papers_Index.md`
re-derivado pelo `derive-index.py` (125 linhas, 24 colunas); **5 PDFs OA
baixados** em `docs/` e 32 marcados PENDENTE (Portal CAPES, como no
ciclo 2); `research/descoberta-ciclo3.md` (queries, volumes, recall,
funil, tabela completa) + `research/ciclo3-data/` (4 dumps JSON brutos
auditáveis); READMEs atualizados. `check-rsl.sh` OK. Commit `1aa96ea`.

**Incidentes:** OpenAlex 401 com cursor+sort de relevância (trocado por
paginação por página); 429 rate-limits com retry; forma da query afeta
volume (aspas desligam stemming — plurais explícitos adotados);
downloads OA bloqueados por vários publishers (5/15 diretos).

### 124. Tentativa de download via Claude no Chrome; helpers de ingestão

**Prompt:** "já estou logado no Chrome no site [proxy CAPES ez101]…
Faça isso via o plugin Claude para o Chrome".

**Ações:** As ferramentas `mcp__claude-in-chrome__*` não estão
disponíveis nesta sessão (ToolSearch vazio). Consulta ao agente
claude-code-guide (docs oficiais): a integração exige sessão iniciada
com `claude --chrome` OU o comando `/chrome` na sessão corrente
(Reconnect extension / Enabled by default), com a extensão ≥ 1.0.36
instalada, Chrome aberto e login no mesmo plano/organização — orientação
repassada ao usuário. **Preparado o caminho independente do plugin:**
`research/downloads-ciclo3.md` (checklist dos 32 PDFs pendentes com
links DOI pelo proxy `ez101.periodicos.capes.gov.br`) e
`scripts/ingest-downloads.py` (pega o PDF mais recente de ~/Downloads,
valida magic %PDF, move para `docs/P<ID>_<slug>.pdf` sem sobrescrever e
atualiza a coluna File name do `Papers_Index.csv`; `--list` mostra os
pendentes; recusa arquivo com >10 min sem confirmação explícita).
READMEs indexados; `check-rsl.sh` OK. Commit `127390b`. Download via
plugin fica aguardando o usuário ativar `/chrome`.

### 125. Downloads do ciclo 3 via Claude in Chrome + documentação do fluxo

**Prompts:** "/chrome ativado" e, durante a execução, "Documente esta
descoberta de uso do claude-in-chrome no template-RSL e aqui no
repositório do artigo…".

**Ações:** Com a extensão conectada, **30 dos 32 PDFs pendentes
baixados** na sessão autenticada do proxy CAPES (`ez101`): fluxo
navegar DOI proxied → resolver URL do PDF por publisher → `fetch` na
própria página + `<a download>` com nome canônico `P<ID>.pdf` →
verificação em disco → `ingest-downloads.py`. IEEE (19) em **lote por
arnumber** (resolvidos antes via redirect público do doi.org; 3 lotes
JS de ≤6); MDPI, World Scientific, ACM e IJCTT por padrão de URL;
ScienceDirect via clique no "View PDF" (URL assinada) e fetch na aba do
viewer; Wiley após o **usuário** resolver o Cloudflare; IJIES com
correção de alvo (1º link do fascículo era outro paper — casado pelo
sufixo do DOI). **5 sem acesso:** capítulos Springer 2025–2026 não
licenciados pela CAPES (P92/P95/P109/P122/P126 — `content/pdf` devolve
HTML; marcados SEM ACESSO no índice; rota: biblioteca/COMUT). docs/
agora com 121 PDFs (32/37 do ciclo 3).

**Pegadinhas documentadas:** validação pelo magic `%PDF-` (paywall
devolve 200/HTML); 1 download automático por origem/página (aviso
"baixar vários" no lote IEEE → Permitir; releitura da página ganha +1);
timeout de 45 s do CDP (lotes ≤6; o lote 2 completou após o timeout);
filtro da extensão `[BLOCKED: Cookie/query string data]` (evitar a
string `credentials`; em mesma origem cookies vão por padrão); CAPTCHAs
são do usuário (Prohibited p/ o agente). **Documentação criada:**
`docs/download-via-claude-chrome.md` canônico no Template-RSL
(+ cópia na instância), referenciado na skill `rsl-descoberta` dos dois
repos; CHANGELOG do template 0.1.2. Downloads errados/duplicados
removidos de ~/Downloads (P102 do paper 01; duplicata 1-s2.0 do P110).
Commits: instância `81c00e4`; template `4b6d923`. `check-rsl.sh` OK nos
dois.

### 126. Ciclo 3, Etapa 1 — elegibilidade bibliométrica e PDR-0006/0007

**Prompt:** "Execute o /rsl-triagem para o ciclo 3".

**Ações (skill `/rsl-triagem`, Etapa 2 do WORKFLOW):** O ciclo 3 trouxe
o primeiro caso sem regra no protocolo — **26 dos 37 candidatos são
conference papers** e I3/I4 são estratos de periódico (ciclos 1–2 foram
100% journals). Conforme a constituição, a execução **parou e levou a
decisão ao condutor** (AskUserQuestion), que ratificou: **PDR-0006**
(estrato de conferência = percentil CiteScore da série de proceedings;
série sem CiteScore → INELEGÍVEL) e **PDR-0007** (renovação da emenda
de estratos do PDR-0002 para o ciclo 3). Levantamento: Scopus Serial
Title API por ISSN + busca por título para as séries (LNCS 44/B1, CCIS
28/B2, LNNS 22/B3, Procedia 53/A4, SOUTHEASTCON 37/B2, EIT 42/B1,
GLOBECOM 54/A4, ISDFS 11/B4) e para os 11 journals (IEEE Access 91/A1,
CS Review 98/A1, Applied Sciences 85/A2, Network 79/A2; A3: JIKM 65,
JECE 71, Discover AI 67; não indexados: Land Forces, IJIES, IJCTT,
Discover Data). **Resultado (papers-ciclo3.csv):** 4 ELEGÍVEIS (P94,
P97, P108, P112) · 15 c/ ressalva de estrato (P91, P92, P93, P95,
P100, P101, P102, P106, P109, P110, P119, P121, P122, P123, P126) ·
16 INELEGÍVEIS por série sem CiteScore · 2 INELEGÍVEIS por I5 com
datas reais conferidas no Crossref (P113 2025-03/0 cit; P114
2025-08/0 cit). **19 seguem para a extração PICOC.** Nota do condutor
registrada no PDR-0006: P90 (candidato mais citado, 7/7/6) sai pela
regra da série; snowballing segue como rota de recaptura.
Papers_Index com os 37 status + MD re-derivado; PDRs indexados;
`check-rsl.sh` OK. Commit `2787ef0`.

**Incidentes:** `citedby-count` do Scopus vem como string — a 1ª rodada
marcou P102 (SC=2) como I5 indevidamente; corrigido com coerção
numérica. Datas de publicação ausentes no dump da descoberta exigiram
consulta Crossref para selar os vereditos de I5 (e o 1º teste do P114
usou DOI errado, detectado pelo título divergente).

### 127. Ciclo 3, Etapa 3 — extração PICOC de leitura integral (14/19)

**Prompt:** "sim" (autorização para executar o `/rsl-extracao` proposto ao
final do item 126).

**Ações (skill `/rsl-extracao`, Etapa 3 do WORKFLOW):** primeira execução da
extração PICOC pelo fluxo do Template-RSL: (1) `FIELD_MAP` do
`scripts/render-prompts.py` ajustado às colunas reais do `Papers_Index.csv`
(ajuste de instância previsto no template); (2) 19 prompts renderizados do
template canônico `templates/prompt-extracao-picoc.md` em
`prompts/picoc-ciclo3/` (marcador `PERSONA` preenchido por pós-processamento —
o render só resolve marcadores mapeados a colunas do índice); (3) fan-out de
**um agente de leitura integral por PDF** (2 lotes de 7; todos via pypdf),
fragmentos em `picoc/fragments-ciclo3/PXX.md`; (4) validação por script
(14/14: cabeçalho + raciocínio + linha única de tabela com 10 células);
(5) consolidação em `picoc/picoc-results-ciclo3.md` com apêndice de raciocínio
e seção de pendentes. Os 5 capítulos Springer sem acesso (P92, P95, P109,
P122, P126) ficam registrados como pendentes — extração futura entra como
adendo datado (Art. VI).

**Achados-chave para a triagem (Etapa 4):** Comparison empírico executado em
P93, P94, P97, P100 (MTTR −63% vs. SREs humanos; MTTD p90 −83%), P101 (MTTR
−72,3%), P102 (MTTD −82%), P106, P108 e P123 (MTTC −37,8%); "não se aplica"
em P91, P110, P112, P119, P121 (secundários/sem baseline). Sinais de exclusão:
P108 não trata de incident response (AgentBench/SLMs) e P106 é "Agentic AI"
só nominal (ML/DRL sem LLM) — candidatos a E2/E3. Registro de qualidade: P93
tem inconsistência interna de escala entre Tabelas 3 e 9 (anotada no
raciocínio do fragmento).

**Comandos:** `render-prompts.py` (19 renders), fan-out de 14 agentes,
validador em scratchpad (14/14 OK), `check-rsl.sh` OK.

### 128. Ciclo 3, Etapa 4 — triagem PRISMA com evidência PICOC

**Prompt:** "Execute o /rsl-triagem para a Etapa 4 do ciclo 3".

**Ações (skill `/rsl-triagem`, Etapa 4 do WORKFLOW):** triagem dos 19
elegíveis da Etapa 1 ancorada na extração PICOC de leitura integral (item
127): **13 aprovados para avaliação integral** (P94 e P97 plenos; P91, P93,
P100, P101, P102, P106, P110, P119, P121, P123 com ressalva de estrato
PDR-0006/0007; P112 pleno A1), **1 excluído** (P108, **E3** — ResilioMate
avalia resiliência de SLMs no AgentBench, sem relação com IR/AIOps/SOC;
precedente P38/E3 ciclo 2 — único A1 do ciclo, exclusão temática e não de
estrato) e **5 adiados** (P92, P95, P109, P122, P126 — PRISMA "reports not
retrieved", Springer; triagem entra como adendo quando os PDFs chegarem).
Caso-limite P106 ("Agentic AI" nominal — ML/DRL sem LLM) **aprovado com flag**
pelos precedentes P73 (agência limitada) e P88 (agêntico não-LLM), sem
necessidade de PDR novo; a avaliação integral decide E2. Secundários P110,
P112 e P121 aprovados como candidatos a fundacionais-condicionais (R1).
Artefatos: `reviews/triagem-ciclo3.md` (resumo, mermaid, tabelas com
critério+evidência+precedente, notas), seção nova do ciclo 3 em
`reviews/PRISMA.md` (Art. VI — ciclos anteriores intocados), 19 statuses no
`Papers_Index.csv` (+ MD re-derivado), READMEs de `picoc/fragments-ciclo3/` e
`prompts/picoc-ciclo3/` (exigência C3 do check-rsl, que só aflora após o
`git add` — C3 varre `git ls-files`).

**Incidentes:** (1) primeiro update de status esqueceu P112 (18/19) — pego
pela contagem e corrigido; (2) `derive-index.py` exige `--csv/--out`
explícitos; (3) check-rsl C3 falhou pós-commit da Etapa 3 porque os arquivos
novos só entram no escopo do C3 depois de rastreados — resolvido com READMEs
por pasta no commit da Etapa 4.

**Comandos:** `check-rsl.sh` OK; commit `5ca23f4` + push.

### 129. Ciclo 3, Etapas 5–6 — prompts de avaliação e pareceres Claude

**Prompt:** "Execute o /rsl-avaliacao para o ciclo 3".

**Ações (skill `/rsl-avaliacao`):**

- **Etapa 5:** mais um bug de template achado no beta test — os marcadores do
  `templates/prompt-avaliacao.md` v1.0.0 eram instrucionais
  (`{{PERSONA — ex.: …}}`) e irresolvíveis pelo render; corrigidos para
  `{{PERSONA}}`/`{{EMENDAS_NORMATIVAS}}`/`{{RQS}}` (v1.1.0, não normativo,
  changelog). `FIELD_MAP` ganhou `CIT_OA/CIT_CR/CIT_SC`. Como o
  `Papers_Index.csv` não tem percentil/citações dos P90+, o render usou um
  **índice aumentado** (scratchpad): Papers_Index + citações por fonte e
  Qualis derivado do `papers-ciclo3.csv` (verif. 2026-10-27) + ressalvas/flags
  da triagem por estudo. 13 prompts em `prompts/prompt-PXX.md` com emendas
  PDR-0006/0007 via `--emendas`, PERSONA/RQS preenchidos pós-render e
  comentários HTML do template removidos das cópias enviadas. Commit `2172585`.
- **Etapa 6 (avaliador Claude):** fan-out de 13 agentes independentes (um por
  estudo; cada um lê só o próprio prompt + PDF + `templates/review.md`), saída
  em `reviews/review-PXX.md`; validação por script (estrutura, soma exata dos
  scores, banda, ressalva obrigatória na recomendação) — 13/13 OK. Resultado:
  **1 Incluir** (P94) · **11 Incluir c/ ressalvas** · **1 Excluir** (P106,
  E2 — parecer confirmou a agência nominal flagada na triagem; RQ 2.0, QA 1.0
  Baixa). Faixas: RQ 2.0–5.0 (P101/P102 = 5.0); QA 1.0–3.5 (8 Alta · 4 Média ·
  1 Baixa). Seção do ciclo 3 em `reviews/README.md`. Commit `6c0d8fc`.

**Pendências:** avaliações paralelas ChatGPT e Gemini com os mesmos prompts
(executadas pelo condutor nas plataformas, como nos ciclos 1–2), depois
Etapas 7–9 (`/rsl-consolidacao`, `/rsl-comparacao`, fichas). Replicar o fix
do template v1.1.0 no repo Template-RSL.

### 130. Ciclo 3, Etapa 7 — consolidação parcial (avaliador Claude)

**Prompt:** "Execute o /rsl-consolidacao para o ciclo 3".

**Ações (skill `/rsl-consolidacao`, consolidação PARCIAL — ChatGPT/Gemini
pendentes):** (1) `reviews/resultados-consolidados-ciclo3.csv` (header do
template canônico, 13 linhas parseadas por script dos próprios pareceres —
símbolos RQ/QA, scores, banda, recomendação; insumos do índice aumentado);
coluna `Conjunto` marca a parcialidade. (2) Gráficos: cópia adaptada do
`gen_charts.py` (CSV/OUT/títulos/buckets de recomendação/valores do grid) →
5 SVGs em `reviews/charts-ciclo3/` + `graficos-ciclo3.md` + README da pasta.
(3) Seção datada do ciclo 3 no `DASHBOARD.md` (funil completo + escores).
(4) `Papers_Index.csv`: Claude RQ/QA/Rec preenchidos e status
"Ciclo 3: avaliacao parcial — Claude: …; ChatGPT/Gemini pendentes" nos 13;
MD re-derivado. (5) **Adendo nº 4** na síntese consolidada (Art. VI) + PDF
regenerado (build_pdf_cons.py do scratchpad, headless Chrome): registra que
o achado central dos ciclos 1–2 ("nenhum estudo mede MTTD/MTTR nominal com
baseline próprio") **deixa de valer no ciclo 3** (P100/P101/P102/P123), todos
sob ressalva de estrato. Estatísticas rotuladas média≠mediana (RQ 3,85/4,0;
QA 2,77/3,0).

**Correção ao item 129:** a contagem de bandas publicada no resumo e no
`reviews/README.md` ("8 Alta · 4 Média · 1 Baixa") estava errada — o CSV
(fonte de verdade, Art. VII) dá **9 Alta · 3 Média · 1 Baixa** (P119 QA 3,0 =
Alta). README corrigido; o item 129 permanece como registro histórico.

**Comandos:** parser/consolidador em python; gen_charts adaptado;
`derive-index.py`; `check-rsl.sh` OK (C5 confere parecer-a-parecer).
Commit `ba2e282` + push.

**Pendências:** reconsolidação tripla + `/rsl-comparacao` quando ChatGPT e
Gemini entregarem; replicar fix do template v1.1.0 no Template-RSL.

### 131. Replicação do fix do template v1.1.0 no Template-RSL

**Prompt:** "Aplique o fix do template v1.1.0 no repo Template-RSL".

**Contexto:** pendência registrada no item 130 — achado do beta test no
ciclo 3 (item 129): os marcadores instrucionais do
`templates/prompt-avaliacao.md` não casam com o replace nem com o regex de
sobras (`{{[A-Z_0-9]+}}`) do `render-prompts.py`, então não eram resolvidos
nem reportados, e vazavam para os prompts renderizados.

**Ações (repo irmão `~/Projects/Template-RSL`, externo a este):**
(1) `templates/prompt-avaliacao.md` v1.0.0 → **v1.1.0**: marcadores
instrucionais ({{PERSONA — ex.: …}}, {{EMENDAS_NORMATIVAS — ex.: …}},
{{RQ1..RQ5 — …}}) trocados pelos limpos `{{PERSONA}}`,
`{{EMENDAS_NORMATIVAS}}` e `{{RQS}}`, com changelog no próprio arquivo (não
normativo, sem PDR). (2) Entrada [0.1.3] no `CHANGELOG.md` do template.
(3) `prompt-extracao-picoc.md` verificado: já usava `{{PERSONA}}` limpo —
sem mudança. (4) Validação: render de teste com índice sintético de 1 linha
no scratchpad — `PERSONA`/`RQS` reportados como "preencher na instância",
emenda resolvida via `--emendas`, sobras `{{…}}` restantes só em comentários
HTML (removidos pós-render na instância).

**Comandos:** `render-prompts.py` (render de teste); commit `8b0ce41` + push
no Template-RSL.

## Decisões e convenções da sessão

- Mudanças de persona/redação nos prompts (PICOC e template de extração) são
  mudanças versionadas: incrementam a versão MINOR e ganham entrada no
  changelog do próprio arquivo (criando a seção Changelog quando ausente).
- Persona padrão dos prompts do projeto (aplicada aos quatro prompts vivos:
  PICOC, template de extração, descoberta e template de avaliação):
  pesquisador em Computação Aplicada do PPGCA/Unisinos orientado por um
  professor Doutor em Ciência da Computação; metodologia ancorada em
  Kitchenham (2009), "Systematic literature reviews in software engineering –
  A systematic literature review".
- Os prompts históricos `prompts/prompt-P20..P40.md` NÃO recebem o novo
  padrão: são registro imutável do que foi enviado ao revisor externo no
  ciclo 1. O template vivo correspondente é `prompt-template.md` (raiz).
- **Emenda de protocolo do ciclo 2 (2026-09-09):** os critérios I3 (Qualis
  A1–A2) e I4 (SJR Q1–Q2) não excluem na triagem do ciclo 2 — estudos fora
  do estrato (P62, P69, P81, P86) seguem para avaliação **com ressalva de
  estrato obrigatória** nos pareceres/inclusões. Vale até nova decisão do
  autor.
- **Regras de protocolo R1–R3 ratificadas (2026-10-26, item 109):** R1
  secundários não-agênticos fora do corpus primário; R2 emendas só valem
  no texto normativo da Etapa 1 dos prompts; R3 corte de domínio estrito
  com o cluster humano restrito ao outcome COGNITIVE_LOAD.
- Triagem do ciclo 2 pode excluir por E2/E3 já na triagem (antes da
  avaliação integral) **desde que ancorada na extração PICOC de leitura
  integral** e nos precedentes do ciclo 1 (P26/P29/P30/P38).
- Referências históricas a "PICOC v1.1.0" na documentação designam a regra de
  Comparison (baseline empírico), não a versão corrente do prompt, e não são
  atualizadas quando o prompt evolui.

## Artefatos produzidos

- `picoc/picoc-extraction-prompt.md` — persona atualizada (v1.2.0) e
  referência metodológica ancorada em Kitchenham (2009) (v1.3.0); changelog
  estendido.
- `report/paper-extraction-prompt-template.md` — persona e referência
  metodológica atualizadas; versão 1.1.0; seção Changelog criada.
- `research/prompt.md` — ROLE com persona padrão e paper de Kitchenham (2009)
  nomeado; versão v3.2.0; changelog estendido.
- `research/README.md` — menções de versão corrente atualizadas para
  "v3 (atual: v3.2.0)".
- `prompt-template.md` (raiz) — bloco PAPEL com persona padrão e Kitchenham
  (2009) pelo título completo; restante reformatado pelo hook (cosmético);
  em seguida renomeado para `prompts/prompt-chatgpt-consultation.md`
  (item 75).
- `README.md` e `reviews/DASHBOARD.md` — referências e árvore de estrutura
  atualizadas para o novo caminho do template de avaliação.
- `docs/P41…P89` — 49 PDFs candidatos do ciclo 2 (adicionados pelo usuário,
  commitados sob demanda; indexação pendente do início da triagem).
- `docs/Systematic literature reviews in software engineering – A systematic
literature review.pdf` — paper metodológico de Kitchenham et al. (2009).
- `picoc/picoc-results-consolidated-P41-P89-Claude.md` — extração PICOC do
  ciclo 2 (49 candidatos, prompt v1.3.0, pré-triagem) com síntese
  transversal e apêndice de raciocínio.
- `Papers_Index.csv` — índice P01–P89 do usuário (insumo do ciclo 2),
  commitado.
- `papers-ciclo2.csv` — elegibilidade Etapa 1 do ciclo 2 (P41–P89):
  citações OpenAlex/Crossref (2026-09-09), Qualis derivado do percentil
  (regra CAPES calibrada em papers.csv), 45 elegíveis · 4 inelegíveis.
- `reviews/triagem-ciclo2.md` — triagem PRISMA do ciclo 2: 22 aprovados
  (4 com ressalva de estrato) · 27 excluídos (E2 = 19 · E3 = 8), com
  evidência PICOC; `reviews/PRISMA.md` ganhou nota de versão do ciclo 2.
- `prompts/prompt-P43.md` … `prompt-P88.md` — 22 prompts de avaliação do
  ciclo 2 preenchidos (INSUMOS + ressalvas_triagem).
- `reviews/review-P43.md` … `review-P88.md` — 22 pareceres do ciclo 2
  (20 Incluir c/ ressalvas · 2 Excluir); tabela-síntese na seção Ciclo 2
  de `reviews/README.md`.
- `reviews/resultados-consolidados-ciclo2.csv`, `reviews/charts-ciclo2/`
  (5 SVGs) e `reviews/graficos-ciclo2.md` — consolidação do ciclo 2;
  `reviews/PRISMA.md` com o diagrama do ciclo 2 (corpus consolidado 53) e
  `reviews/DASHBOARD.md` com a seção Ciclo 2.
- `report/P43…P88-extraction[.csv|-ptBR.csv]` (40 fichas) +
  `report/consolidated-extraction-ciclo2[.csv|-ptBR.csv]` — extração
  estruturada dos 20 incluídos do ciclo 2; índice no `report/README.md`.
- `reviews/relatorio-sintese-consolidado.md` + `.pdf` — síntese narrativa
  consolidada dos ciclos 1 e 2 (corpus 53; lacuna MTTD/MTTR triangulada em
  89 candidatos).
- `MEMORY.md` — itens 70–78; commit `bdeaeb3` acrescentado à tabela da sessão
  anterior (conforme nota daquela tabela).
- `picoc/`: `picoc-results-ciclo3.md` · `fragments-ciclo3/` (14 fragmentos) · `prompts/picoc-ciclo3/` (19 prompts renderizados); `scripts/render-prompts.py` (FIELD_MAP da instância)
- `reviews/`: `triagem-ciclo3.md` · seção ciclo 3 em `PRISMA.md`; READMEs de `picoc/fragments-ciclo3/` e `prompts/picoc-ciclo3/`; 19 statuses ciclo 3 em `Papers_Index.csv`/`.md`
- Ciclo 3, Etapas 5–6: `prompts/prompt-P91…P123.md` (13), `reviews/review-P91…P123.md` (13), `templates/prompt-avaliacao.md` v1.1.0, seção ciclo 3 em `reviews/README.md`
- Ciclo 3, Etapa 7 (parcial): `reviews/resultados-consolidados-ciclo3.csv` · `graficos-ciclo3.md` · `charts-ciclo3/` (5 SVGs + README) · seção ciclo 3 no `DASHBOARD.md` · adendo nº 4 na síntese consolidada (+PDF) · escores Claude no `Papers_Index`

- (repo Template-RSL, externo) `templates/prompt-avaliacao.md` v1.1.0 (marcadores limpos) · entrada [0.1.3] no `CHANGELOG.md`

## Histórico de commits da sessão

| Hash      | Data       | Mensagem                                                                                                      |
| --------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| `a7b2468` | 2026-09-07 | Adjust PICOC prompt persona to advised researcher (v1.2.0)                                                    |
| `eba2a7d` | 2026-09-07 | Log PICOC prompt persona change (item 70) in MEMORY.md                                                        |
| `00b3e69` | 2026-09-07 | Anchor PICOC prompt methodology to Kitchenham (2009) SLR paper (v1.3.0)                                       |
| `06de0fa` | 2026-09-07 | Log Kitchenham (2009) reference update (item 71) in MEMORY.md                                                 |
| `4094ce1` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to extraction template (v1.1.0)                 |
| `c4aa322` | 2026-09-07 | Log extraction-template persona/reference update (item 72) in MEMORY.md                                       |
| `88c5412` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to discovery prompt (v3.2.0)                    |
| `f338f34` | 2026-09-07 | Log discovery-prompt persona/reference update (item 73) in MEMORY.md                                          |
| `0a07d88` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to evaluation prompt template                   |
| `b031031` | 2026-09-07 | Log evaluation-template persona update (item 74) in MEMORY.md                                                 |
| `5001ac4` | 2026-09-07 | Rename evaluation template to prompts/prompt-chatgpt-consultation.md                                          |
| `5ae1e48` | 2026-09-07 | Log evaluation-template rename (item 75) in MEMORY.md                                                         |
| `6297ef2` | 2026-09-07 | Add docs/ P41-P89 candidate PDFs from cycle-2 discovery                                                       |
| `6d9e4a9` | 2026-09-07 | Log P41-P89 candidate PDFs commit (item 76) in MEMORY.md                                                      |
| `3c76e22` | 2026-09-07 | Add Kitchenham (2009) SLR methodology reference paper to docs/                                                |
| `d9e023d` | 2026-09-07 | Log Kitchenham (2009) PDF commit (item 77) in MEMORY.md                                                       |
| `adeeb78` | 2026-09-07 | Add cycle-2 PICOC extraction (P41-P89) with cross-cutting synthesis                                           |
| `906b582` | 2026-09-07 | Log cycle-2 PICOC extraction (item 78) in MEMORY.md                                                           |
| `57aaa88` | 2026-09-09 | Log cycle-2 workflow-order consultation (item 79) in MEMORY.md                                                |
| `c96334e` | 2026-09-09 | Add cycle-2 stage-1 eligibility (papers-ciclo2.csv) from Papers_Index.csv                                     |
| `560b874` | 2026-09-09 | Log cycle-2 stage-1 eligibility (item 80) in MEMORY.md                                                        |
| `df57b9c` | 2026-09-09 | Add cycle-2 PRISMA screening: 22 approved, 27 excluded, strata amendment                                      |
| `9defea8` | 2026-09-09 | Log cycle-2 PRISMA screening (item 81) in MEMORY.md                                                           |
| `9fc207d` | 2026-09-09 | Generate 22 cycle-2 evaluation prompts for screening-approved candidates                                      |
| `c618846` | 2026-09-09 | Log cycle-2 evaluation prompts (item 82) in MEMORY.md                                                         |
| `99f1e6c` | 2026-09-10 | Add 22 cycle-2 review reports: 20 include-with-caveats, 2 exclude                                             |
| `85179ca` | 2026-09-10 | Log cycle-2 review reports (item 83) in MEMORY.md                                                             |
| `891edb1` | 2026-09-10 | Consolidate cycle 2: CSV, charts, PRISMA flow, dashboard; corpus 53                                           |
| `b8bbc1d` | 2026-09-10 | Log cycle-2 consolidation (item 84) in MEMORY.md                                                              |
| `d527e60` | 2026-09-10 | Add extraction sheets (EN+ptBR) and consolidated CSVs for 20 cycle-2 included studies                         |
| `00ca1b7` | 2026-09-10 | Log cycle-2 extraction sheets (item 85) in MEMORY.md                                                          |
| `129afc8` | 2026-09-10 | Add consolidated two-cycle synthesis report (MD + PDF)                                                        |
| `362faf2` | 2026-09-10 | Log consolidated synthesis report (item 86) in MEMORY.md                                                      |
| `91eb5cb` | 2026-09-12 | Log evaluator-comparison blocker and procedure (item 87) in MEMORY.md                                         |
| `8f98497` | 2026-10-25 | Add ChatGPT and Gemini evaluator sets for cycle 2 (P43-P88; Gemini also P20-P40)                              |
| `6e07b65` | 2026-10-25 | Log evaluator sets commit (item 88) in MEMORY.md                                                              |
| `52abc4b` | 2026-10-25 | Add cycle-2 three-evaluator comparison (Claude x ChatGPT x Gemini)                                            |
| `5983930` | 2026-10-25 | Log cycle-2 evaluator comparison (item 89) in MEMORY.md                                                       |
| `d4f0061` | 2026-10-25 | Update corpus cross-citations to P01-P89 (49 edges; OpenAlex+Crossref)                                        |
| `3a555e7` | 2026-10-25 | Log P01-P89 cross-citations update (item 90) in MEMORY.md                                                     |
| `c73fbb7` | 2026-10-25 | Add cycle-2 discovery corpus spreadsheet; ignore local resume notes                                           |
| `f454026` | 2026-10-25 | Log corpus spreadsheet commit (item 91) in MEMORY.md                                                          |
| `4eaf0ce` | 2026-10-26 | Generate 19 retroactive evaluation prompts for foundational corpus P01-P19                                    |
| `3f4b834` | 2026-10-26 | Log foundational-corpus prompts (item 92) in MEMORY.md                                                        |
| `2091253` | 2026-10-26 | Add 19 retroactive review reports for foundational corpus P01-P19                                             |
| `0f9b4b5` | 2026-10-26 | Log foundational retroactive reviews (item 93) in MEMORY.md                                                   |
| `2e52101` | 2026-10-26 | Add foundational-corpus consolidated CSV and charts (P01-P19)                                                 |
| `edce337` | 2026-10-26 | Log foundational consolidation and Gemini P01-P19 (item 94) in MEMORY.md                                      |
| `837fb70` | 2026-10-26 | Add per-evaluator consolidated CSVs P01-P88 and ChatGPT foundational evaluations                              |
| `d3c3ae5` | 2026-10-26 | Log per-evaluator consolidated CSVs (item 95) in MEMORY.md                                                    |
| `f28f8dc` | 2026-10-26 | Add global three-evaluator comparison P01-P88; enrich Papers_Index with outcomes                              |
| `2b4c235` | 2026-10-26 | Log global evaluator comparison and index update (item 96) in MEMORY.md                                       |
| `2b89358` | 2026-10-26 | Add global-comparison addendum to consolidated synthesis; rebuild PDF                                         |
| `af1e452` | 2026-10-26 | Log synthesis addendum (item 97) in MEMORY.md                                                                 |
| `eb15fa4` | 2026-10-26 | Add Markdown version of Papers_Index (derived from canonical CSV)                                             |
| `cee616d` | 2026-10-26 | Log Papers_Index markdown version (item 98) in MEMORY.md                                                      |
| `d12941f` | 2026-10-26 | Ignore local Scopus API key file                                                                              |
| `c9bc0fa` | 2026-10-26 | Complete Scopus citation counts for P41-P89 (49/49, all >= 1)                                                 |
| `81bd595` | 2026-10-26 | Complete Scopus column in P01-P89 cross-citations (triple-check, 52 edges)                                    |
| `09a22da` | 2026-10-26 | Log Scopus key setup and triple-check completion (items 99-100) in MEMORY.md                                  |
| `803bef6` | 2026-10-26 | Add Scopus triple-check addendum to consolidated synthesis; rebuild PDF                                       |
| `51869d3` | 2026-10-26 | Log Scopus addendum (item 101) in MEMORY.md                                                                   |
| `fa8abfb` | 2026-10-26 | Add IEEE Access SLR article draft v1 (main.tex + referencias.bib)                                             |
| `325e0a9` | 2026-10-26 | Log IEEE Access article draft (item 102) in MEMORY.md                                                         |
| `b9e7b95` | 2026-10-26 | Compile article draft with TinyTeX: 6-page PDF, zero warnings                                                 |
| `6ba0487` | 2026-10-26 | Log LaTeX install and article compilation (item 103) in MEMORY.md                                             |
| `23cbdbe` | 2026-10-26 | Extend session header through 2026-10-26 (article draft) in MEMORY.md                                         |
| `2afd172` | 2026-10-26 | Add TikZ PRISMA flow figure to the article (Fig. 1); clean 7-page build                                       |
| `2253601` | 2026-10-26 | Log PRISMA figure (item 104) in MEMORY.md                                                                     |
| `99c31d6` | 2026-10-26 | Adjust author designation to Master Degree Student                                                            |
| `0cc6fa4` | 2026-10-26 | Log author designation fix (item 105) in MEMORY.md                                                            |
| `53bd765` | 2026-10-26 | Log Trabalho I reuse consultation (item 106) in MEMORY.md                                                     |
| `c7c2352` | 2026-10-26 | Enrich article: cognitive-load toolbox table, six gap axes, citation-network figure                           |
| `81f5ed8` | 2026-10-26 | Log article enrichment (item 107) in MEMORY.md; fix page count in article README                              |
| `c579d38` | 2026-10-26 | Add RQ-coverage stacked-bar figure (Fig. 3) to the article                                                    |
| `5bb7b7e` | 2026-10-26 | Log RQ-coverage figure (item 108) in MEMORY.md                                                                |
| `62bfc4f` | 2026-10-26 | Ratify protocol rules R1-R3 in the article (method, reliability, threats)                                     |
| `3e96b18` | 2026-10-26 | Log protocol rules ratification (item 109) in MEMORY.md                                                       |
| `d1dd7ea` | 2026-10-27 | Switch article to official IEEE Access class (ieeeaccess.cls) with pgf year-primitive workaround              |
| `bc07d4f` | 2026-10-27 | Log IEEE Access class swap (item 110) in MEMORY.md                                                            |
| `dc84850` | 2026-10-27 | Add advisor Rafael Kunst as co-author and corresponding-author e-mails                                        |
| `73a1cbb` | 2026-10-27 | Log advisor co-author addition (item 111) in MEMORY.md                                                        |
| `843a041` | 2026-10-27 | Add author biographies (IEEEbiographynophoto) and bio/ source folder                                          |
| `7df3c37` | 2026-10-27 | Log author biographies (item 112) in MEMORY.md                                                                |
| `4cc4c97` | 2026-10-27 | English review of the article: grammar, idiom, IEEE style, kappa band accuracy                                |
| `0a352fc` | 2026-10-27 | Mark English review done in article README TODO                                                               |
| `12f0758` | 2026-10-27 | Verify article counts against canonical CSVs; fix cycle-2 mean QA (2.73) with errata                          |
| `05efa56` | 2026-10-27 | Log article count verification (item 114) in MEMORY.md                                                        |
| `3d54c6c` | 2026-10-27 | Replace first author's biography with author-provided text                                                    |
| `5bb889c` | 2026-10-27 | Log author-provided biography update (item 115) in MEMORY.md                                                  |
| `1a0af97` | 2026-10-27 | Use full author name in byline and corresponding-author line                                                  |
| `0552ac1` | 2026-10-27 | Log full-name byline alignment (item 116) in MEMORY.md                                                        |
| `69e1563` | 2026-10-27 | Use volume/year placeholders (VOLUME NN, YYYY) in the page footer                                             |
| `5ba3f61` | 2026-10-27 | Log footer volume/year placeholder (item 117) in MEMORY.md                                                    |
| `1af8058` | 2026-10-27 | Rebuild final article PDF from clean state for visual review                                                  |
| `19e8a4b` | 2026-10-27 | Log final PDF rebuild for visual review (item 118) in MEMORY.md                                               |
| `e7183ff` | 2026-10-27 | Log Spec-Agentic-SDLC reuse consultation (item 119) in MEMORY.md                                              |
| `099e74c` | 2026-10-27 | Log Template-RSL skeleton creation (item 120) in MEMORY.md                                                    |
| `52c0da6` | 2026-10-27 | Log Template-RSL GitHub repo creation (item 121) in MEMORY.md                                                 |
| `7f925a3` | 2026-10-27 | Adopt Template-RSL governance layer (beta test): constitution, PDRs 0001-0005, validation scripts, skills, CI |
| `1aa400a` | 2026-10-27 | Log Template-RSL adoption and beta findings (item 122) in MEMORY.md                                           |
| `1aa96ea` | 2026-10-27 | Cycle-3 discovery via canonical query: 37 candidates P90-P126, audit trail and raw sweep data                 |
| `07f57a1` | 2026-10-27 | Log cycle-3 discovery (item 123) in MEMORY.md                                                                 |
| `127390b` | 2026-10-27 | Add cycle-3 download checklist (CAPES proxy links) and PDF ingest helper                                      |
| `dcb28d1` | 2026-10-27 | Log Chrome plugin attempt and ingest helpers (item 124) in MEMORY.md                                          |
| `81c00e4` | 2026-10-28 | Download 30 cycle-3 PDFs via Claude in Chrome over CAPES proxy; document the flow                             |
| `14fbbfd` | 2026-10-28 | Log Claude in Chrome downloads and flow documentation (item 125) in MEMORY.md                      |
| `2787ef0` | 2026-10-28 | Cycle-3 stage-1 eligibility: 4 eligible, 15 with stratum caveat, 18 ineligible; ratify PDR-0006/0007 |
| `3b41dbe` | 2026-10-28 | Log cycle-3 stage-1 eligibility and PDR-0006/0007 (item 126) in MEMORY.md |
| `cfce70c` | 2026-10-28 | Cycle-3 stage-3 PICOC extraction: 14 of 19 candidates (5 Springer pending) |
| `a15bdc8` | 2026-10-28 | Log cycle-3 PICOC extraction (item 127) in MEMORY.md |
| `5ca23f4` | 2026-10-28 | Cycle-3 stage-4 PRISMA screening: 13 approved for full evaluation, 1 excluded (E3), 5 deferred |
| `01784eb` | 2026-10-28 | Log cycle-3 PRISMA screening (item 128) in MEMORY.md |
| `2172585` | 2026-10-28 | Cycle-3 stage-5 evaluation prompts: 13 rendered from canonical template v1.1.0 |
| `6c0d8fc` | 2026-10-28 | Cycle-3 stage-6 Claude evaluations: 13 reviews (1 include, 11 include-with-caveats, 1 exclude E2) |
| `3f2caf0` | 2026-10-28 | Log cycle-3 evaluation prompts and Claude reviews (item 129) in MEMORY.md |
| `ba2e282` | 2026-10-28 | Cycle-3 stage-7 partial consolidation (Claude evaluator) |
| `6c579a6` | 2026-10-28 | Log cycle-3 partial consolidation (item 130) in MEMORY.md |
| —         | 2026-10-27 | (repo Template-RSL, commit local `24bf3c3`) Initial skeleton — repositório irmão, externo a este              |
| —         | 2026-10-29 | (repo Template-RSL, commit `8b0ce41`) Template prompt-avaliacao v1.1.0: clean markers resolvable by render-prompts.py — repositório irmão, externo a este |

_(O commit desta atualização de MEMORY.md é acrescentado ao final do histórico.)_
