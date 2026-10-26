# Avaliação Sistemática de Estudo Secundário — RSL Agentic AI Copilot para Resposta a Incidentes

---

## Identificação do Estudo
- **ID:** P29
- **Título:** *AIOps for log anomaly detection in the era of LLMs: A systematic literature review*
- **Autores:** Miguel De la Cruz Cabello; Tiago Prince Sales; Marcos R. Machado
- **Periódico/Conferência:** *Intelligent Systems with Applications* (Elsevier), Vol. 28, Artigo 200608, pp. 1–18 (Disponível online em 19 de novembro de 2025)
- **DOI:** `10.1016/j.iswa.2025.200608`
- **Arquivo avaliado:** `P29-A2-1-s2.0-S2667305325001346-main.pdf`

---

## Etapa 0 — Extração Bibliométrica e Escopo
- **Natureza do estudo:** Estudo secundário — Revisão Sistemática da Literatura (*Review* / SLR), sintetizando 33 artigos selecionados via *Scopus* (23 estudos) e *snowballing* no repositório *arXiv* (10 estudos) publicados principalmente entre 2021 e 2025 (Seção 2, Figura 1, pp. 3–5; Apêndice Tabela A1, pp. 15–17), acrescido da proposição de uma taxonomia (Figura 9) e de um framework conceitual baseado no *CRISP-ML* (Figura 10).
- **Foco técnico:** Interseção entre *Artificial Intelligence for IT Operations* (AIOps), Grandes Modelos de Linguagem (LLMs) e *Retrieval-Augmented Generation* (RAG) para detecção de anomalias em *logs*, análise de causa raiz e suporte à decisão operacional em ambientes críticos e de defesa/militar.

## Etapa 1 — Triagem de Elegibilidade (PRISMA)
- **Critérios de Inclusão (IC):**
  - *IC1 (Alinhamento temático):* Atendido. Investiga diretamente o ecossistema de AIOps (percepção de falhas, análise de causa raiz e auto-remediação) potencializado por LLMs e RAG para diagnóstico de anomalias em *logs*, incluindo menções a agentes autônomos (ex.: *ReAct*, *MARL* + LLMs e multiagentes conversacionais).
  - *IC2 (Recorte temporal e revisão por pares):* Atendido (publicado no periódico revisado por pares *Intelligent Systems with Applications*, Vol. 28, 2025).
  - *IC3 (Rigor técnico/metodológico):* Atendido com ressalvas metodológicas (protocolo de busca explícito, matriz de extração detalhada dos 33 estudos na Tabela A1, análise bibliométrica em *VOSviewer* e taxonomia estruturada).
- **Critérios de Exclusão (EC):** Não incide em critério de exclusão, tratando-se de revisão secundária de contextualização e síntese.
- **Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (para confirmação de métricas externas ausentes no PDF: *Citações*, *SJR* e *Qualis*).

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P29 | Intelligent Systems with Applications | 2025 | [VERIFICAR] | Q1 [VERIFICAR] | A2 [VERIFICAR] | Revisão Sistemática da Literatura (Secundário) | `10.1016/j.iswa.2025.200608` |

> **Nota sobre campos `[VERIFICAR]`:** *Citações*, *SJR* (informado no insumo como `Q1`) e *Qualis* (informado no insumo como `A2`) não constam no corpo do PDF referentes ao próprio artigo e devem ser verificados nas fontes externas oficiais (*Scimago Journal Rank*, *Plataforma Sucupira / Qualis CAPES* e *Scopus / Google Scholar*).

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P29 | AIOps for log anomaly detection in the era of LLMs: A systematic literature review | **RQ1** (Contexto e Definições) | Parcialmente Respondida | **P** (0.5) | Seção 1 (pp. 1–2); Seção 4.1, Figura 6 (pp. 6–8); Seção 4.3 (p. 11); Seção 4.4 (p. 12); Tabela A1 (p. 15) | Contextualiza o ciclo contínuo de AIOps em 3 estágios (*Monitoring*, *Engaging*, *Automating*, Figura 6, p. 7) cobrindo pré-processamento, percepção de falhas, RCA e auto-remediação (geração de *scripts*, recomendação de comandos e execução automática, p. 2). Sintetiza pontualmente estudos com arquiteturas agênticas — como agentes autônomos de defesa cibernética combinando MARL, LLMs e regras em redes militares (Loevenich et al., 2024, p. 12), colaboração multiagente com 3 agentes no *ChatCNC* (Jeon et al., 2025, p. 11) e raciocínio *ReAct* em AIOps corporativo (Vitui & Chen, 2025, Tabela A1, p. 15) —, mas não aprofunda uma definição formal de níveis de autonomia agêntica. |
| P29 | AIOps for log anomaly detection in the era of LLMs: A systematic literature review | **RQ2** (Arquitetura de Engenharia) | Respondida Plenamente | **T** (1.0) | Seções 4.2 e 4.3, Figuras 8–9 (pp. 8–13); Seção 4.4, Figura 10 (pp. 12–14); Tabela A1 (pp. 15–17) | **(a) Tipo de arquitetura:** Propõe uma taxonomia em 3 eixos para sistemas LLM/RAG de detecção de anomalias em *logs* (Figura 9, pp. 12–13): *Model Architecture* (*Transformers*, *Adapter/LoRA-Tuned*, *Prompt-Based*), *Knowledge Augmentation Strategy* (*No External Knowledge*, *Implicit/Fine-Tuning*, *Explicit/RAG Sparse, Dense, Hybrid*) e *Inference Objective* (*Classification*, *Ranking*, *Explanatory*). Propõe também um framework em 3 fases baseado no *CRISP-ML* (Figura 10, p. 14). **(b) Ferramentas/frameworks:** Cataloga *parsers* (*Drain*, *Spell*, *LogCluster*, *MoLFI*), frameworks de *logs* (*LogBERT*, *DeepLog*, *LogAnomaly*, *LogLLM*, *LogFormer*, *OWL*, *LogFiT*, *LogPrompt*, *LogExpert*, *RAPID*, *RAG4ITOps*, *OMAI*), bancos vetoriais (*FAISS*), *retrievers* (*BM25*, *TF-IDF*, *DPR*) e avaliadores RAG (*RAGAS*, *ARES*, *TruLens*). **(c) Capacidades avançadas:** *Chain-of-Thought*, *self-prompting*, *query refinement*, *reranking*/fusão híbrida (Figura 8) e explicabilidade *ante-hoc* (*deep unrolling*) e *post-hoc* (*saliency maps*, *attention heatmaps*, *token-level importance*, p. 12). |
| P29 | AIOps for log anomaly detection in the era of LLMs: A systematic literature review | **RQ3** (Benefícios e Evidências) | Parcialmente Respondida | **P** (0.5) | Seções 4.1–4.3 (pp. 7–11); Tabela A1 (pp. 15–17) | Como revisão secundária (sem experimentos próprios), sistematiza os benefícios qualitativos (eliminação de engenharia manual de *features*, mitigação de alucinações via RAG, adaptabilidade *zero/few-shot* e explicabilidade operacional) e consolida as métricas de avaliação da literatura: detecção (`F1-score`, `Precision`, `Recall`, `AUROC`, `AUPR`, `FPR`), recuperação RAG (`MRR`, `Hit Rate`, `NDCG`) e geração (`BLEU`, `ROUGE`, `Exact Match`, avaliação por GPT-4 e humana) (pp. 10–11, Tabela A1). Reporta ganhos quantitativos de estudos primários (ex.: *LogLLM* supera *baselines* em 6,6% no F1-score; *RAPID* atinge `F1 = 0.97` sem treinamento; *OMAI* obtém >90% de respostas efetivas, pp. 9, 16). |
| P29 | AIOps for log anomaly detection in the era of LLMs: A systematic literature review | **RQ4** (Desafios e Ética) | Respondida Plenamente | **T** (1.0) | Seção 4.1 (p. 7); Seção 4.2 (pp. 8–10); Seção 4.3 (pp. 10–12); Seção 4.4 (p. 12) | **(a) Desafios técnicos:** Analisa *concept drift* por atualizações de software (p. 7), desbalanceamento severo de classes e escassez de rótulos (p. 8), tokens fora do vocabulário (*OOV*), alto custo computacional/financeiro (GPUs, APIs, indexação *FAISS*), latência de inferência incompatível com tempo real estrito (inferência < 1s para janelas de 10s, p. 13) e alucinações (pp. 10, 12). **(b) Desafios éticos/governança:** Destaca riscos de privacidade e confidencialidade no envio de *logs* sensíveis a LLMs proprietários de terceiros, potencial violação regulatória e riscos à segurança nacional em sistemas militares (pp. 2, 9–12), além do conflito do modelo "caixa-preta" com auditoria e conformidade. **(c) Mecanismos de governança:** Uso de LLMs compactos *open-source* ajustados localmente via LoRA (ex.: *Mistral-7B*), validação por especialistas humanos, técnicas de explicabilidade *ante-hoc*/*post-hoc* e ciclos *input-interpretation-feedback* (p. 12). |
| P29 | AIOps for log anomaly detection in the era of LLMs: A systematic literature review | **RQ5** (Lacunas de Pesquisa) | Respondida Plenamente | **T** (1.0) | Seção 4.2 (p. 10); Seção 4.3 (pp. 11–12); Seção 4.4 (pp. 12–14) | Aponta lacunas de pesquisa explícitas e relevantes: (1) desenvolvimento de *pipelines* de detecção de anomalias em *logs* em tempo real (*online streaming*) com latência sub-segundo (combinando *parsers* leves como *Drain* com LLMs otimizados, p. 13); (2) criação de arquiteturas RAG especializadas na indexação vetorial de *templates* de *logs* em vez de Q&A textual genérico (p. 13); (3) superação da baixa diversidade dos *datasets* clássicos (*HDFS*, *BGL*, *Thunderbird*, *Liberty*) por meio de *benchmarks* multi-domínio abrangendo IoT, nuvem híbrida e sistemas militares (pp. 11–12); (4) adoção de métricas robustas ao desbalanceamento e ao risco assimétrico de falsos negativos, como *Matthews Correlation Coefficient* (MCC), `AUC-PR` e funções de custo específicas de domínio (p. 10); e (5) validação empírica em operações militares e de defesa (pp. 12–14). |
| **P29** | **SCORE_RQ Total** | — | **4.0 / 5.0** | — | — | Atende plenamente RQ2 (1.0), RQ4 (1.0) e RQ5 (1.0), e parcialmente RQ1 (0.5) e RQ3 (0.5). |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| P29 | Revisão Sistemática da Literatura (Estudo Secundário) | Y (1.0) | P (0.5) | P (0.5) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (QA1–QA4)
- **QA1 — Clareza e relevância dos objetivos / critérios de inclusão (Y = 1.0):** Define claramente quatro questões norteadoras (*Knowledge Questions*, Seção 1, p. 2) e explicita os critérios de inclusão e exclusão na Tabela 1 e Figura 2 (pp. 3–4), articulando bem o problema da análise de grandes volumes de *logs* não estruturados em AIOps.
- **QA2 — Adequação da estratégia de busca e desenho metodológico (P = 0.5):** Documenta as *strings* de busca e o fluxo de seleção em 5 etapas (826 resultados iniciais no *Scopus* $\to$ 593 após filtros $\to$ 23 selecionados + 10 via *snowballing* no *arXiv* = 33 artigos, Figura 1, p. 3). Todavia, apresenta limitações metodológicas importantes: (i) busca primária restrita a uma única base indexadora (*Scopus*) complementada por *preprints* do *arXiv*; (ii) cerca de 30% dos artigos incluídos (10 de 33, Tabela 2, p. 5) são *preprints* sem revisão por pares; (iii) exclusão de artigos sem versão aberta gratuita (Tabela 1), gerando potencial viés de seleção; e (iv) ausência de pontuação formal de qualidade metodológica individual para os 33 estudos incluídos.
- **QA3 — Qualidade da avaliação / síntese dos estudos e evidências (P = 0.5):** Apresenta uma síntese qualitativa e comparativa detalhada (Tabela A1 nas pp. 15–17), mapeamento bibliométrico de coocorrência de palavras-chave via *VOSviewer* (Figuras 4 e 5) e uma taxonomia original de métodos LLM/RAG (Figura 9). Entretanto, o framework proposto na Seção 4.4 (Figura 10, pp. 13–14) é puramente conceitual e carece de validação experimental ou estudo de caso prático.
- **QA4 — Consistência entre evidências coletadas e conclusões (Y = 1.0):** As conclusões respondem sistematicamente às quatro questões de pesquisa propostas na introdução (Seção 5, p. 14) e os autores reconhecem com transparência as limitações da revisão (como o viés de cobertura *Scopus*/*arXiv* na nota 11 da p. 3 e a escassez de literatura empírica específica sobre análise de *logs* com LLMs no setor militar na Seção 4.4, p. 12).

---

## Parecer Final do Revisor

### Síntese (3–5 linhas)
Esta Revisão Sistemática da Literatura analisa 33 estudos sobre a aplicação de Grandes Modelos de Linguagem (LLMs) e *Retrieval-Augmented Generation* (RAG) na detecção de anomalias em *logs* dentro do ciclo operacional de AIOps (percepção de falhas, RCA e auto-remediação). O artigo contribui com uma taxonomia clara em três dimensões (*Model Architecture*, *Knowledge Augmentation Strategy* e *Inference Objective*, Figura 9), uma análise crítica dos *trade-offs* práticos de adoção (latência em tempo real vs. janelas de percepção sub-segundo, custos de GPU/APIs/bancos vetoriais, *concept drift* e riscos de privacidade) e um mapeamento de ferramentas estado da arte (*LogLLM*, *LogFormer*, *OWL*, *LogFiT*, *LogPrompt*, *LogExpert*, *RAPID*, *RAG4ITOps*).

### Recomendação
**INCLUIR COM RESSALVAS** — O estudo atinge `SCORE_RQ = 4.0/5.0` e `SCORE_QA = 3.0/4.0` (Banda Alta), sendo altamente valioso como estudo secundário para fundamentar na RSL o papel de LLMs, *Prompt Engineering* e RAG na camada de percepção de anomalias em *logs* e os desafios de operação em tempo real e privacidade (RQ2, RQ4 e RQ5). A ressalva deve-se ao fato de ser um estudo secundário focado primordialmente em *pipelines* LLM+RAG para classificação de *logs* (tratando agentes autônomos apenas pontualmente) e cujo framework próprio (Figura 10) não possui validação empírica.

### Pendências de Verificação Externa
- **Citações:** Verificar contagem atualizada no *Scopus* ou *Google Scholar* (`[VERIFICAR]`).
- **SJR:** Confirmar quartil `Q1` para *Intelligent Systems with Applications* no *Scimago Journal Rank* (`[VERIFICAR]`).
- **Qualis:** Confirmar estrato `A2` na *Plataforma Sucupira / Qualis CAPES* (`[VERIFICAR]`).
