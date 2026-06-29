# Relatório de Síntese — RSL "Agentic AI Copilot para Resposta a Incidentes"

**Lote avaliado:** estudos candidatos **P20–P40** (20 estudos; P36 era duplicata de P31/LEMAD, removida).
**Fonte:** [`resultados-consolidados.csv`](resultados-consolidados.csv) + pareceres individuais [`review-Pxx.md`](.).
**Método de avaliação:** prompt por estudo (`../prompts/`) executado contra o PDF (`../docs/`), seguindo Kitchenham et al. (2009) e a lógica DARE (QA1–QA4). Vereditos de RQ em T/P/N (1,0 / 0,5 / 0,0) e QA em Y/P/N.

> ⚠️ **Ressalva transversal:** Citações, SJR e Qualis **não são verificáveis nos PDFs**. Todos os valores de Qualis/SJR vêm dos **insumos** do CSV e permanecem **pendentes de verificação externa** (Scimago; Plataforma Sucupira/Qualis CAPES; base indexadora).

---

## 1. Resumo executivo

- **20 estudos** processados; **18 avaliados integralmente**; **2 inelegíveis** na triagem (P39, P40 — **Qualis A3 < A1–A2**).
- **Aderência geral alta:** SCORE_RQ médio **3,83/5,0** (mediana 4,0); SCORE_QA médio **3,50/4,0** (mediana 3,75). **14 de 18** em **Banda Alta**, 4 em Média, nenhum em Baixa.
- **Decisão de inclusão:** **14 Incluir** (7 plenos + 5 com ressalvas + 2 fundacionais), **4 Excluir** por relevância/tipo/domínio, **2 Inelegíveis**.
- **Eixo organizador das decisões:** _agêntico × domínio-IR_. Incluídos são **agênticos e** próximos de IR/AIOps/SOC; exclusões recaem em não-agênticos, off-domain ou inelegíveis.
- **Lacuna sistemática identificada:** **RQ4 (Desafios & Ética)** é a questão menos coberta — apenas **4/18** plenamente respondidas; **14/18 parciais**. Ética/governança é o ponto fraco recorrente dos estudos técnicos de sistema.

---

## 2. Funil de elegibilidade (ETAPA 1)

| Etapa                                   | Qtde | IDs                             |
| --------------------------------------- | :--: | ------------------------------- |
| Candidatos recebidos                    |  20  | P20–P40 (P36 já removido)       |
| **Inelegíveis (Qualis A3)**             |  2   | P39, P40                        |
| **Elegíveis (avaliados)**               |  18  | demais                          |
| → Incluídos (qualquer forma)            |  14  | P20–P25, P27, P28, P31–P35, P37 |
| → Excluídos por relevância/tipo/domínio |  4   | P26, P29, P30, P38              |

**Critérios verificáveis no PDF** (Ano ≥ 2020; veículo ≠ NULL) **atendidos por todos**. Os critérios **Citações ≥ 1, SJR Q1–Q2 e Qualis A1–A2** ficam **pendentes** — exceto Qualis A3 de P39/P40 (insumo), que motiva a inelegibilidade.

![Distribuição das recomendações](charts/chart-recommendations.svg)

---

## 3. Cobertura por questão de pesquisa (RQ)

Distribuição de vereditos entre os **18 estudos avaliados**:

| RQ      | Tema                                                                            | T (1,0) | P (0,5) | N (0,0) | Leitura                                                   |
| ------- | ------------------------------------------------------------------------------- | :-----: | :-----: | :-----: | --------------------------------------------------------- |
| **RQ1** | Context Definitions (autonomia, planejamento, memória, ferramentas, supervisão) |    9    |    6    |    3    | Boa, mas heterogênea: 3 estudos sem conteúdo agêntico (N) |
| **RQ2** | Engineering Architecture (orquestração, memória, guardrails, observabilidade)   |   11    |    6    |    1    | **Forte** — núcleo dos estudos de sistema                 |
| **RQ3** | Evidence Benefits (métricas, tempo de resposta, qualidade de decisão)           |   12    |    6    |    0    | **Mais coberta** — evidência empírica abundante           |
| **RQ4** | Challenges & Ethics (segurança, robustez, governança, accountability)           |  **4**  | **14**  |    0    | **Lacuna sistemática** — ética/governança rasa            |
| **RQ5** | Research Gaps (avaliação, threat models, governança, observabilidade)           |   16    |    2    |    0    | **Quase universal** — direções futuras bem articuladas    |

![Cobertura por RQ](charts/chart-rq-coverage.svg)

**Achados-chave:**

- **RQ3 e RQ5 são os pontos fortes** do corpus: os estudos reportam métricas (F1, MTTD/MTTR, latência, acurácia de localização) e propõem direções futuras de forma consistente.
- **RQ4 é o gargalo.** Apenas **P24, P33, P34, P37** respondem RQ4 plenamente — justamente os estudos **conceituais/governança/humano-organizacionais**. Os **sistemas agênticos técnicos** (P21–P23, P25, P27, P28, P31, P32, P35) recebem majoritariamente **P** por discutirem desafios técnicos mas **omitirem ética/governança/accountability** — notável dado que vários atuam em **infraestrutura crítica** (rede elétrica: P31, P32, P35) ou têm **caráter dual-use** (P25 ofensivo).
- **RQ1 (N=3):** os três sem conteúdo agêntico são **P26** (survey de RCA), **P29** (SLR) e **P30** (pipeline LLM) — coerente com suas exclusões.

---

## 4. Avaliação de qualidade (QA / DARE)

| Critério                          |  Y  |  P  |   N   | Observação                                                                                                |
| --------------------------------- | :-: | :-: | :---: | --------------------------------------------------------------------------------------------------------- |
| **QA1** Objetivos claros          | 18  |  0  |   0   | Universal — todos enunciam problema/objetivos                                                             |
| **QA2** Metodologia replicável    | 11  |  7  |   0   | 7 parciais: dados proprietários / sem código / prompts não publicados (P20, P26, P28, P29, P31, P32, P33) |
| **QA3** Base de evidências sólida | 13  |  1  | **4** | **4 N = estudos secundários** sem validação empírica própria (P24, P26, P29, P33)                         |
| **QA4** Conclusões coerentes      | 16  |  2  |   0   | 2 parciais (P23, P26): limitações pouco discutidas                                                        |

![Cobertura por QA (DARE)](charts/chart-qa-coverage.svg)

- **Banda de qualidade:** **14 Alta** (≥3,0) · **4 Média** (1,5–2,5) · **0 Baixa**. As 4 Médias são **P24, P26, P29, P33** — todos **secundários** (QA3 = N puxa o escore).
- **Reprodutibilidade (QA2)** é o calcanhar recorrente dos estudos primários: **dados de produção proprietários** (SGCC em P31/P32/P35; SpamAssassin/custom em P28) e **ausência de repositórios de código/prompts** limitam a replicação plena. Exceções positivas: P35 (templates de prompt no apêndice), P38 (base pública + métricas definidas), P34/P37 (protocolos detalhados).

---

## 5. Ranking de aderência (SCORE_RQ + SCORE_QA)

![Aderência por estudo](charts/chart-scores-by-study.svg)

| Pos. | ID      | SCORE_RQ | SCORE_QA |  Σ  | Recomendação                 |
| :--: | ------- | :------: | :------: | :-: | ---------------------------- |
|  1   | **P21** |   4,5    |   4,0    | 8,5 | Incluir                      |
|  1   | **P22** |   4,5    |   4,0    | 8,5 | Incluir                      |
|  1   | **P25** |   4,5    |   4,0    | 8,5 | Incluir                      |
|  1   | **P27** |   4,5    |   4,0    | 8,5 | Incluir                      |
|  5   | **P28** |   4,5    |   3,5    | 8,0 | Incluir                      |
|  5   | **P31** |   4,5    |   3,5    | 8,0 | Incluir                      |
|  5   | **P34** |   4,0    |   4,0    | 8,0 | Incluir c/ ressalvas         |
|  5   | **P35** |   4,0    |   4,0    | 8,0 | Incluir                      |
|  9   | P32     |   4,0    |   3,5    | 7,5 | Incluir c/ ressalvas         |
|  9   | _P38_   |   3,5    |   4,0    | 7,5 | _Excluir (domínio)_          |
|  11  | P20     |   4,0    |   3,0    | 7,0 | Incluir c/ ressalvas         |
|  11  | P23     |   3,5    |   3,5    | 7,0 | Incluir c/ ressalvas         |
|  11  | _P30_   |   3,0    |   4,0    | 7,0 | _Excluir (tipo)_             |
|  11  | P37     |   3,0    |   4,0    | 7,0 | Incluir c/ ressalvas         |
|  15  | P24     |   4,0    |   2,5    | 6,5 | Incluir c/ ressalvas (fund.) |
|  15  | P33     |   4,0    |   2,5    | 6,5 | Incluir c/ ressalvas (fund.) |
|  17  | _P26_   |   2,5    |   2,5    | 5,0 | _Excluir_                    |
|  17  | _P29_   |   2,5    |   2,5    | 5,0 | _Excluir_                    |

> Nota: a pontuação **não substitui** a decisão de relevância. P38 e P30 pontuam alto (Σ 7,5 e 7,0) mas são **excluídos** por domínio/tipo — escore alto ≠ aderência ao escopo da RSL.

**Núcleo recomendado (top tier):** **P21, P22, P25, P27, P28, P31, P35** — sistemas agênticos, IR/AIOps/SOC, evidência empírica robusta. **P34** complementa pelo lado _copilot/IR puro_ (NIST 800-61).

O mapa abaixo cruza os dois escores: o quadrante superior-direito (SCORE_RQ ≥ 4,0 e SCORE_QA ≥ 3,5) concentra o núcleo de inclusão; exclusões por tipo/domínio (P30, P38) aparecem com alta qualidade mas fora do escopo, e os secundários (P24, P33, P26, P29) caem na faixa de QA ≤ 2,5.

![Mapa SCORE_RQ × SCORE_QA](charts/chart-grid-rq-qa.svg)

---

## 6. Taxonomia do corpus incluído

**Por paradigma de agente** (eixo a registrar no mapeamento, pois afeta comparabilidade):

| Paradigma                                            | Estudos            |
| ---------------------------------------------------- | ------------------ |
| **LLM multi-agente** (orquestrador + especializados) | P27, P28, P31, P35 |
| **LLM-agente closed-loop** (sense→act autônomo)      | P22                |
| **SLM-agente** (modelos pequenos, on-prem)           | P21                |
| **LLM + GNN / tools** (agente sobre núcleo DL)       | P23, P32           |
| **LLM+RAG multiagente**                              | P20                |
| **MAS/RL não-LLM** (RL/ML, IR baseado em regras)     | P25                |
| **LLM copilot / baixa autonomia**                    | P34                |
| **Survey de percepção** (lado da demanda)            | P37                |
| **Survey/Review agêntico** (fundacional)             | P24, P33           |

**Por domínio:** RCA/diagnóstico (P23, P27, P32, P35) · AIOps/operações (P21, P31) · SOC/detecção & IR de segurança (P25, P28, P34, P37) · remediação (P22) · prevenção IaC (P20) · fundamentação (P24, P33).

**Espectro de autonomia** (útil para a discussão): **remediação autônoma closed-loop (P22)** → **multi-agente RCA com validação adversarial (P27/P35)** → **GNN+agente de recuperação offline (P32)** → **copilot humano-no-loop (P34)** → **percepção de adoção/confiança (P37)**.

---

## 7. Achados transversais e implicações para a RSL

1. **A maturidade está na arquitetura e na evidência (RQ2/RQ3), não na governança (RQ4).** O campo entrega sistemas agênticos funcionais e bem medidos, mas **subtrata ética, accountability e governança** — gap a destacar como contribuição/lacuna da RSL, sobretudo para infraestrutura crítica e usos dual-use.
2. **Convergência forte em RCA/AIOps.** Metade dos incluídos ataca **localização de causa raiz** (P23, P27, P32, P35) — sinal de sub-tarefa madura do IR; a **remediação autônoma** (P22) e a **detecção/correlação em SOC** (P28) são menos povoadas, indicando frente promissora.
3. **Dois paradigmas concorrentes de "agente":** LLM-agêntico (maioria) vs **MAS/RL não-LLM** (P25) — comparáveis em desempenho de IR, mas distintos em autonomia/explicabilidade; e o extremo **copilot** (P34) alinhado ao próprio título da RSL.
4. **Procedência concentrada:** P31, P32, P35 vêm de equipes ligadas à **State Grid (China)** — registrar ao analisar independência/viés do corpus.
5. **Risco temporal de elegibilidade:** **5 estudos de 2026** (P25, P30, P32, P35, P37) podem ter **0 citações** — o critério "Citações ≥ 1" deve ser verificado antes de confirmar inclusão (pode reclassificar P30/P32/P35/P37).

---

## 8. Decisões de exclusão (rastreabilidade)

| ID      | Motivo                                                                       | Natureza                 |
| ------- | ---------------------------------------------------------------------------- | ------------------------ |
| P26     | Secundário (survey de RCA) **e** não-agêntico (RQ1=N)                        | Relevância/tipo          |
| P29     | Secundário (SLR) **e** não-agêntico (RQ1=N)                                  | Relevância/tipo          |
| P30     | Não-agêntico (pipeline LLM; RQ1=N) + domínio bug-triage de inference engines | Relevância/tipo          |
| P38     | Agêntico, alta qualidade, mas **domínio agricultura** (0 menções a IR)       | Domínio                  |
| **P39** | **Qualis A3** (< A1–A2) + artigo de opinião (não-empírico)                   | **Inelegível (ETAPA 1)** |
| **P40** | **Qualis A3** (< A1–A2) + survey secundário não-agêntico                     | **Inelegível (ETAPA 1)** |

_Estudos fundacionais (P24, P33):_ incluídos **com ressalva** — se o protocolo restringir o corpus primário a **estudos primários**, migram para a **fundamentação**, resultando em **12 estudos no corpus primário**.

---

## 9. Confiabilidade entre avaliadores (Claude × ChatGPT)

Os 20 estudos foram avaliados **independentemente** por dois avaliadores (Claude e ChatGPT) sob o mesmo protocolo. A concordância é **substancial**, o que reforça a robustez dos vereditos:

- **Decisão (Incluir/Excluir): 90%** (18/20) · **Cohen's κ = 0,74**.
- **Banda de qualidade: 100%** (18/18) · erro absoluto médio **SCORE_RQ 0,42 / SCORE_QA 0,31**.
- **RQ4 e RQ5: 100% de acordo** — ambos os avaliadores confirmam, de forma independente, a **lacuna sistemática de ética/governança (RQ4)**, tornando esse achado avaliador-robusto.
- Únicas 2 divergências de decisão: **P26 e P29** (surveys/SLR não-agênticos) — o ChatGPT inclui com ressalvas; o Claude exclui. Reforça que o único ponto de protocolo em aberto é o **tratamento de estudos secundários**.

![Concordância entre avaliadores](charts/chart-comparacao.svg)

> Detalhes e tabela lado a lado: **[comparacao-avaliadores.md](comparacao-avaliadores.md)** · dados em [`comparacao-avaliadores.csv`](comparacao-avaliadores.csv).

---

## 10. Limitações desta avaliação

- **Extração de texto via PDFKit** (sem renderização de página): tabelas/figuras com layout complexo podem ter perdido valores tabulares — vereditos ancorados no texto corrido e nas tabelas legíveis.
- **Qualis/SJR/Citações não confirmados** (insumos): toda decisão de elegibilidade dependente desses itens é **provisória**.
- **Julgamento de relevância** (agêntico × IR) é interpretativo; casos-limite (P30, P34, P37, P38) foram explicitados nos pareceres individuais para auditabilidade.

---

## 11. Próximos passos recomendados

1. **Verificar externamente** Citações/SJR/Qualis dos 18 elegíveis (atenção a P30/P32/P35/P37 — 2026, possível 0 citações; e confirmar A3 de P39/P40).
2. **Decidir no protocolo** o tratamento de estudos secundários (P24, P33): corpus primário vs fundamentação.
3. **Anexar os escores** às Tabelas 3, 5 e 7 da RSL existente (IDs já sequenciais a partir de P20).
4. **Destacar a lacuna de RQ4** (ética/governança) como achado/contribuição da revisão.
5. **Registrar o eixo de paradigma de agente** (Seção 6) no mapeamento, para comparabilidade entre LLM-agêntico, MAS/RL e copilot.

---

_Gerado a partir de `reviews/resultados-consolidados.csv` (20 estudos). Estatísticas: SCORE_RQ médio 3,83; SCORE_QA médio 3,50; 14 Banda Alta; RQ4 plenamente respondida em apenas 4/18._
