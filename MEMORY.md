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

# Sessão 2026-09-07 — Ajuste de persona no prompt PICOC (v1.2.0)

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
- `MEMORY.md` — itens 70–78; commit `bdeaeb3` acrescentado à tabela da sessão
  anterior (conforme nota daquela tabela).

## Histórico de commits da sessão

| Hash      | Data       | Mensagem                                                                                      |
| --------- | ---------- | --------------------------------------------------------------------------------------------- |
| `a7b2468` | 2026-09-07 | Adjust PICOC prompt persona to advised researcher (v1.2.0)                                    |
| `eba2a7d` | 2026-09-07 | Log PICOC prompt persona change (item 70) in MEMORY.md                                        |
| `00b3e69` | 2026-09-07 | Anchor PICOC prompt methodology to Kitchenham (2009) SLR paper (v1.3.0)                       |
| `06de0fa` | 2026-09-07 | Log Kitchenham (2009) reference update (item 71) in MEMORY.md                                 |
| `4094ce1` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to extraction template (v1.1.0) |
| `c4aa322` | 2026-09-07 | Log extraction-template persona/reference update (item 72) in MEMORY.md                       |
| `88c5412` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to discovery prompt (v3.2.0)    |
| `f338f34` | 2026-09-07 | Log discovery-prompt persona/reference update (item 73) in MEMORY.md                          |
| `0a07d88` | 2026-09-07 | Apply advised-researcher persona and Kitchenham (2009) anchor to evaluation prompt template   |
| `b031031` | 2026-09-07 | Log evaluation-template persona update (item 74) in MEMORY.md                                 |
| `5001ac4` | 2026-09-07 | Rename evaluation template to prompts/prompt-chatgpt-consultation.md                          |
| `5ae1e48` | 2026-09-07 | Log evaluation-template rename (item 75) in MEMORY.md                                         |
| `6297ef2` | 2026-09-07 | Add docs/ P41-P89 candidate PDFs from cycle-2 discovery                                       |
| `6d9e4a9` | 2026-09-07 | Log P41-P89 candidate PDFs commit (item 76) in MEMORY.md                                      |
| `3c76e22` | 2026-09-07 | Add Kitchenham (2009) SLR methodology reference paper to docs/                                |
| `d9e023d` | 2026-09-07 | Log Kitchenham (2009) PDF commit (item 77) in MEMORY.md                                       |
| `adeeb78` | 2026-09-07 | Add cycle-2 PICOC extraction (P41-P89) with cross-cutting synthesis                           |
| `906b582` | 2026-09-07 | Log cycle-2 PICOC extraction (item 78) in MEMORY.md                                           |
| `57aaa88` | 2026-09-09 | Log cycle-2 workflow-order consultation (item 79) in MEMORY.md                                |
| `c96334e` | 2026-09-09 | Add cycle-2 stage-1 eligibility (papers-ciclo2.csv) from Papers_Index.csv                     |
| `560b874` | 2026-09-09 | Log cycle-2 stage-1 eligibility (item 80) in MEMORY.md                                        |
| `df57b9c` | 2026-09-09 | Add cycle-2 PRISMA screening: 22 approved, 27 excluded, strata amendment                      |
| `9defea8` | 2026-09-09 | Log cycle-2 PRISMA screening (item 81) in MEMORY.md                                           |
| `9fc207d` | 2026-09-09 | Generate 22 cycle-2 evaluation prompts for screening-approved candidates                      |
| `c618846` | 2026-09-09 | Log cycle-2 evaluation prompts (item 82) in MEMORY.md                                         |
| `99f1e6c` | 2026-09-10 | Add 22 cycle-2 review reports: 20 include-with-caveats, 2 exclude                             |

_(O commit desta atualização de MEMORY.md é acrescentado ao final do histórico.)_
