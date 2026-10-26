# Avaliação Sistemática de Estudo Primário — RSL (Kitchenham et al., 2009 / DARE)

## Identificação do Estudo
- **ID do Artigo:** P38
- **Arquivo PDF Avaliado:** [P38-A2-electronics-14-04883-v2.pdf](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/P38-A2-electronics-14-04883-v2.pdf)
- **Prompt de Referência:** [prompt-P38.md](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/prompt-P38.md)
- **Título:** *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation*
- **Autores:** Irina Radeva; Ivan Popchev; Lyubka Doukovska; Miroslava Dimitrova (Institute of Information and Communication Technologies, Bulgarian Academy of Sciences, Sofia; Faculty of Informatics and Mathematics, Trakia University, Stara Zagora, Bulgaria)
- **Periódico / Fonte:** *Electronics* (MDPI), Vol. 14, No. 24, Art. 4883, pp. 1–35, 2025
- **DOI:** `10.3390/electronics14244883`

---

## Etapa 0 — Extração Bibliométrica e Escopo

- **Metadados verificados no PDF:** Artigo de pesquisa original (*Article*) publicado em *Electronics* (MDPI), Vol. 14, No. 24, Art. 4883, pp. 1–35, 2025 (Recebido em 15 de novembro de 2025; Revisado em 7 de dezembro de 2025; Aceito em 8 de dezembro de 2025; Publicado em 11 de dezembro de 2025, p. 1).
- **Métricas externas (`[VERIFICAR]`):**
  - **Citações:** `[VERIFICAR]` (não consta no PDF; verificar no *Scopus* ou *Google Scholar*).
  - **SJR / Quartil:** Informado como `Q2` no input do protocolo (`[VERIFICAR]` no *Scimago Journal Rank* para *Electronics*, ISSN 2079-9292).
  - **Qualis CAPES:** Informado como `A2` no input do protocolo (`[VERIFICAR]` na *Plataforma Sucupira / Qualis Periódicos* na área de Ciência da Computação).
- **Adequação ao Escopo Temático da RSL:** **Tangencial / Fora do Domínio de Aplicação Alvo (Domínio Avaliado: Agricultura / QA Factual Genérico)**. Embora o artigo realize uma avaliação experimental rigorosa de quatro estratégias de coordenação multiagente (*Collaborative*, *Sequential*, *Competitive* e *Hierarchical*) contra *Retrieval-Augmented Generation* (RAG) de agente único em três LLMs *open-source* de 7B–8B parâmetros (*Mistral 7B*, *Llama 3.1 8B* e *Granite 3.2 8B*), o cenário de aplicação e o corpus experimental pertencem integralmente ao domínio de **agricultura** (*FAO Climate-Smart Agriculture Sourcebook*, Seção 1.1, p. 2; Seção 3.2, p. 6), sem experimentos em gerência de redes, cibersegurança ou operações de TI (apenas cita brevemente na Seção 2, p. 4, trabalhos correlatos em gerência ágil de projetos [31] e detecção de anomalias em redes elétricas [32]).

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério PRISMA | Status | Evidência no Texto / Justificativa |
| :--- | :---: | :--- |
| **1. Publicação entre 2020 e 2026** | **Atende** | Publicado em dezembro de 2025 (*Electronics*, Vol. 14, Art. 4883, p. 1). |
| **2. Qualis A1–A2** | **`[VERIFICAR]`** | Informado no metadado do protocolo como `A2` (requer verificação externa na Plataforma Sucupira). |
| **3. Escopo: IA Agêntica em redes, segurança ou operações de TI** | **Não Atende (Domínio Alvo)** | Investiga arquiteturas de coordenação multiagente baseadas em LLMs e RAG (com registro de auditoria em blockchain Antelope), mas o domínio experimental é **resposta a perguntas factuais sobre agricultura** (*Climate-Smart Agriculture Sourcebook*, p. 2), sem aplicação direta em redes, cibersegurança ou gerência de serviços de TI. |
| **4. Texto completo disponível e acessível** | **Atende** | Texto integral de 35 páginas analisado via PDF, incluindo Apêndice A (pp. 29–32) e repositório GitHub público. |
| **5. Sem critérios de exclusão (não é apenas ML clássico, IoT puro, resumo ou duplicata)** | **Atende** | Artigo experimental completo sobre coordenação multiagente em LLMs. |

**Status da Triagem:** **ELEGIBILIDADE COMPROMETIDA POR ESCOPO DE DOMÍNIO** (embora atenda aos critérios formais de período, completude e investigação de sistemas multiagentes baseados em LLMs, falha no recorte de domínio vertical em redes, segurança ou operações de TI; recomenda-se **EXCLUIR** da síntese vertical de redes/segurança ou **INCLUIR COM RESSALVAS** exclusivamente como evidência transversal de engenharia de coordenação multiagente vs. RAG em modelos locais de 7–8B). A extração completa é apresentada a seguir conforme o protocolo.

---

## Tabela A — Extração Bibliométrica (Tabela 3 do Protocolo)

| ID | Autores | Título | Ano | Fonte | Qualis | SJR | Citações | Escopo_Resumo |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **P38** | Radeva, I.; Popchev, I.; Doukovska, L.; Dimitrova, M. | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | 2025 | *Electronics* (MDPI, Vol. 14, No. 24, Art. 4883, pp. 1–35) | A2 `[VERIFICAR]` | Q2 `[VERIFICAR]` | `[VERIFICAR]` | Avalia empiricamente 4 estratégias de coordenação multiagente (*Collaborative*, *Sequential*, *Competitive*, *Hierarchical*) contra RAG de agente único em 3 LLMs *open-source* locais (*Mistral 7B*, *Llama 3.1 8B*, *Granite 3.2 8B*) ao longo de 3.100 avaliações (100 pares Q&A do *FAO Climate-Smart Agriculture Sourcebook*), demonstrando que todas as 28 configurações multiagentes sofrem degradação estatisticamente significativa (`-4,39%` a `-35,31%`) frente ao RAG de agente único devido ao *overhead* de coordenação e fragmentação de recuperação. |

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5 do Protocolo)

| Questão de Pesquisa (RQ) | Classificação | Pontuação | Evidências e Justificativa Detalhada (com páginas, seções, tabelas e figuras) |
| :--- | :---: | :---: | :--- |
| **RQ1 (Adaptação e autonomia de modelos fundacionais como agentes para gestão de redes/TI)** | **P** | **0.5** | **Analisa profundamente a coordenação de LLMs como agentes, mas fora do domínio de redes/TI.** Avalia três modelos fundacionais *open-source* ajustados por instrução de 7–8B parâmetros (*Mistral 7B-instruct-v0.3*, *Llama 3.1 8B-instruct* e *Granite 3.2 8B-instruct*, Seção 3.1, p. 5) atuando em equipes homogêneas de 3 agentes sob quatro protocolos de decisão coletiva (Seção 3.2, pp. 6–8; Apêndice A.4–A.7, pp. 30–31): *Collaborative* (*Analyzer*, *Critic*, *Synthesizer* com agregação simples ou *Two-Phase Consensus*), *Competitive* (*Expert A, B, C* com seleção pelo maior *score* de confiança 0–100), *Hierarchical* (*Specialist 1, 2* em paralelo + síntese por *Manager* com janela expandida $1,5\times$) e *Sequential* (refinamento em pipeline *Analyzer $\to$ Processor $\to$ Reviewer*). Contudo, os agentes operam sobre consultas factuais agrícolas e não executam ações autônomas em infraestrutura de redes ou TI. |
| **RQ2 (Arquiteturas, padrões de design e integração com infraestrutura de TI)** | **P** | **0.5** | **Arquitetura de software multiagente/RAG bem especificada, porém voltada a QA documental.** Estende o framework modular em três camadas *PaSSER / maPaSSER* (Figura 1, p. 6; Apêndice A.1, p. 29): (1) *LLM Infrastructure Layer* (inferência local via `Ollama` em CPU Intel Xeon e `MLX` com Metal Performance Shaders em Apple M1, banco vetorial `ChromaDB` com embeddings `sentence-transformers`/Mistral, e motor multiagente em `FastAPI`/`WebSocket`); (2) *Web Application Layer* (frontend `React`/`PrimeReact` com pipeline RAG em `LangChain`, limiar de similaridade cosseno 0,90–0,95 e $k=5$ ou $7$); e (3) *Evaluation & Storage Layer* (API `Flask` em Python 3.11.14 com `NLTK` e `PyTorch 2.5.1`, persistência em `MongoDB` e integração com blockchain `Antelope`/`IPFS` para verificação imutável de resultados). Compara dois modos de entrega de contexto (Seção 3.2.6, p. 8): *Independent Retrieval* vs. *Shared Context Retrieval* (SCR). Não integra ferramentas de gerência de redes ou segurança. |
| **RQ3 (Cenários de avaliação, métricas de desempenho e eficácia)** | **P** | **0.5** | **Avaliação quantitativa e estatística exemplar de LLMs multiagentes, mas em corpus não pertencente a TI/Redes.** Executa 3.100 avaliações em 31 configurações (Tabela 1, p. 7) sobre 100 pares Q&A (subconjunto de 369 pares usados na calibração de baseline, Seção 3.4, pp. 13–14). Propõe duas métricas compostas via *Simple Additive Weighting* (SAW / MCDM, Seção 3.3, Eqs. 1–3, Tabelas 2–3, pp. 10–14) agregando 9 métricas (`F1`, `METEOR`, `BLEU`, `Cosine Similarity`, `Pearson Correlation`, `ROUGE-1/2`, `ROUGE-L`, `Laplace Perplexity` e `Lidstone Perplexity`): o *Composite Performance Score* (`CPS`) e o *Threshold-Aware CPS* (`T-CPS`, que recompensa estabilidade $\alpha=0,10$ e penaliza variância quadrática $\beta=0,05 \cdot CV^2$). **Principais achados (Tabela 4, pp. 16–17):** (1) **Todas as 28 configurações multiagentes apresentaram degradação estatisticamente significativa ($p < 0,01$ no teste-$t$ pareado)** em relação ao baseline RAG de agente único, variando de `-4,39%` (*Mistral-Opt Hierarchical*, $p=0,007$, $|d|=0,28$) e `-4,85%` (*Llama Sequential Original*, $p=0,004$, $|d|=0,30$) até `-35,31%` (*Granite Collaborative Original*, $p < 0,001$, $|d|=6,09$); (2) *Isolamento de fragmentação de recuperação* (Fase 3, *Granite-SCR*, Seção 4.6, p. 21): o contexto compartilhado melhorou o desempenho em `4,2 a 12,5 pp`, mas manteve degradação residual de `-14,21% a -31,08%`, provando que o *overhead* de coordenação é o fator limitante dominante; (3) *Consumo computacional* (Tabela 5, pp. 18–19): configurações multiagentes exigem 3 a 4 chamadas de inferência por consulta, e a estratégia *Collaborative* consome em média `2.656 tokens` (`+58,2%` de *overhead* sobre as demais estratégias, que consomem `1.658–1.717 tokens`); e (4) *Análise de sensibilidade* (Tabela 6, p. 22): estabilidade de ranking em `93,5%` (29/31 configurações) ao longo de 25 combinações de $(\alpha, \beta)$. |
| **RQ4 (Desafios de segurança, confiabilidade, alucinação, guarda-corpos e limitações)** | **P** | **0.5** | **Identifica modos de falha críticos de confiabilidade e consistência em coordenação multiagente, sem abordar segurança cibernética ou ética.** Demonstra empiricamente o fenômeno de *"stable mediocrity"* (mediocridade estável, Seção 4.5, p. 19; Seção 5.1, p. 24): estratégias colaborativas baseadas em consenso reduzem a variabilidade (baixo $CV$, ganho de `~8,0%` do T-CPS sobre o CPS), mas convergem consistentemente para respostas de baixa qualidade (`-20,68% a -35,31%`) por perda de informação na síntese e homogeneização de saídas (consenso próximo a 100%, p. 25). Também analisa propagação sequencial de erros, *deadlock* de consenso e fragmentação de contexto (Seção 5.2, p. 25), além de documentar rigorosamente as limitações do estudo (domínio único, modelos de 7–8B, agentes homogêneos, *prompts* gerados com auxílio de IA e heterogeneidade de hardware CPU Intel Xeon vs. Apple M1, Seção 5.3, p. 26). |
| **RQ5 (Tendências futuras e direções de pesquisa abertas)** | **P** | **0.5** | **Propõe direções futuras para sistemas multiagentes RAG genéricos (Seção 6, p. 27):** (1) *role-specific prompting* com especialização explícita de agentes; (2) mecanismos avançados de consenso com argumentação estruturada, votação ponderada ou agregação aprendida; (3) seleção adaptativa de estratégia de coordenação baseada nas características da consulta (*query-aware routing*); (4) ajuste conjunto (*joint tuning*) de limiares de recuperação vetorial e parâmetros de coordenação; e (5) avaliação de modelos de grande porte (`70B+`) e equipes de agentes heterogêneos (combinando modelos de famílias distintas). Não direciona a agenda especificamente para redes ou segurança. |
| **Pontuação Total (`SCORE_RQ`)** | — | **2.5 / 5.0** | **Média de aderência às RQs: 50,0% (0 T, 5 Ps, 0 N — penalizado pelo desalinhamento do domínio de aplicação com Redes/Segurança/Operações de TI).** |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 do Protocolo)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências do Artigo |
| :--- | :---: | :---: | :--- |
| **QA1 (Clareza e explicitação dos objetivos e questões da pesquisa)** | **Y** | **1.0** | A Seção 1.1 (*Research Objectives*, p. 2) define quatro objetivos específicos (avaliação comparativa, isolamento de fontes de degradação, interação modelo-estratégia e *trade-off* consistência-desempenho) e três questões práticas de implantação claramente estruturadas. |
| **QA2 (Descrição adequada do método, arquitetura e reprodutibilidade)** | **Y** | **1.0** | **Reprodutibilidade exemplar.** Além de detalhar toda a arquitetura e equações nas Seções 3.1–3.4 (pp. 5–14) e todos os hiperparâmetros, papéis e templates de *prompts* no Apêndice A (Tabelas A1–A5, pp. 29–32), disponibiliza código-fonte completo (`maPaSSER` e `PaSSER`), scripts de análise estatística, corpus de 100 pares Q&A e resultados brutos em CSV em repositório GitHub público (`https://github.com/scpdxtest/maPaSSER`, Seção *Data Availability Statement*, p. 28). |
| **QA3 (Suficiência da validação empírica, cenários e métricas)** | **Y** | **1.0** | Executa 3.100 avaliações controladas em 31 configurações, aplicando 9 métricas complementares agregadas via MCDM/SAW (`CPS` e `T-CPS`), testes-$t$ pareados, tamanhos de efeito $d$ de Cohen, intervalos de confiança de 95%, análise de sensibilidade em 25 combinações paramétricas (Tabela 6, p. 22) e análise de correlação de Spearman e ablação *leave-one-out* no material suplementar (Tabelas S1–S3, p. 11, 27–28). |
| **QA4 (Consistência entre resultados obtidos e conclusões reportadas)** | **Y** | **1.0** | Reporta resultados negativos (100% das 28 configurações multiagentes tiveram desempenho inferior ao RAG de agente único calibrado) com total integridade científica, sem inflar benefícios e delimitando com precisão as condições de contorno (*boundary conditions*) para modelos de 7–8B parâmetros (Seções 5 e 6, pp. 23–27). |
| **Pontuação Total (`SCORE_QA`)** | **Banda Alta** | **4.0 / 4.0** | **Qualidade metodológica Máxima (`SCORE_QA = 4.0`, faixa $\ge 3.0$).** |

---

## Parecer Final do Revisor

### Síntese Crítica (3–5 linhas)
O artigo **P38** possui qualidade metodológica, estatística e de reprodutibilidade impecável (`SCORE_QA = 4.0/4.0`), apresentando um resultado empírico fundamental sobre sistemas multiagentes baseados em LLMs locais de 7–8B parâmetros (*Mistral 7B*, *Llama 3.1 8B*, *Granite 3.2 8B*): **todas as 28 configurações multiagentes avaliadas apresentaram degradação estatisticamente significativa (`-4,39%` a `-35,31%`, $p < 0,01$) frente a um pipeline RAG de agente único bem calibrado**, demonstrando que o *overhead* de coordenação e o fenômeno de *"mediocridade estável"* em consensos colaborativos superam os ganhos em tarefas de QA factual sob restrição computacional. Entretanto, o domínio experimental utilizado para o benchmark é a **agricultura** (*FAO Climate-Smart Agriculture Sourcebook*), sem experimentos em redes de computadores, cibersegurança ou operações de TI.

### Recomendação Final
- **Decisão:** **INCLUIR COM RESSALVAS** *(ou **EXCLUIR** caso o protocolo PRISMA seja aplicado com restrição estrita ao domínio vertical de teste)*
- **Justificativa:** Embora o dataset avaliado pertença ao domínio agrícola (o que reduz seu `SCORE_RQ` para `2.5/5.0` nas dimensões específicas de redes/TI), o estudo possui rigor metodológico máximo (`SCORE_QA = 4.0/4.0`) e fornece evidência quantitativa crítica e contraintuitiva sobre padrões arquiteturais multiagentes (*Collaborative*, *Sequential*, *Competitive*, *Hierarchical*), fragmentação de RAG e *overhead* de tokens em LLMs locais de pequeno porte (7–8B) — um cenário diretamente análogo à implantação de agentes locais em borda/infraestrutura de TI com restrição de recursos. Recomenda-se sua inclusão com ressalva explícita para fundamentar as discussões arquiteturais de **RQ2, RQ3 e RQ4** sobre *quando não usar coordenação multiagente* em LLMs pequenos.

### Pendências de Verificação Externa (`[VERIFICAR]`)
1. **Qualis CAPES:** Confirmar a classificação `A2` do periódico *Electronics* (MDPI, ISSN 2079-9292) na *Plataforma Sucupira (Qualis Periódicos)* na área de Ciência da Computação.
2. **SJR / Quartil:** Confirmar o quartil `Q2` e o índice SJR vigente no portal *Scimago Journal Rank*.
3. **Citações:** Levantar o número atual de citações do artigo (`DOI: 10.3390/electronics14244883`) no *Scopus* ou *Google Scholar*.
