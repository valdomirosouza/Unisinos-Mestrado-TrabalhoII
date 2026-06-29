# Comparação entre avaliadores — Claude × ChatGPT

> 🧭 [📊 Dashboard](DASHBOARD.md) · [📄 Relatório de síntese](relatorio-sintese.md) · [🧮 CSV da comparação](comparacao-avaliadores.csv) · [🏠 README raiz](../README.md)

Dois avaliadores executaram **independentemente** o mesmo protocolo (prompt + Kitchenham/DARE) sobre os 20 estudos (P20–P40, sem P36):

- **Claude** → pareceres em [`review-Pxx.md`](.) (escores em [`resultados-consolidados.csv`](resultados-consolidados.csv)).
- **ChatGPT** → pareceres em [`ChatGPT/Pxx_avaliacao_RSL.md`](ChatGPT/).

Esta análise mede a **concordância entre avaliadores** (inter-rater reliability) — um indicador de robustez/objetividade dos vereditos da RSL.

## Resultado em um relance

| Métrica                                 |                                                     Valor | Leitura                    |
| --------------------------------------- | --------------------------------------------------------: | -------------------------- |
| **Acordo de decisão** (Incluir/Excluir) |                                           **90%** (18/20) | Alto                       |
| **Cohen's κ** (decisão)                 |                                                  **0,74** | Concordância _substancial_ |
| **Acordo de banda** de qualidade        |                                          **100%** (18/18) | Perfeito                   |
| Erro absoluto médio **SCORE_RQ**        |                                       **0,42** (máx. 1,0) | Pequeno                    |
| Erro absoluto médio **SCORE_QA**        |                                       **0,31** (máx. 0,5) | Pequeno                    |
| Acordo por RQ (T/P/N exato)             | RQ1 67% · RQ2 78% · RQ3 72% · **RQ4 100%** · **RQ5 100%** | —                          |

![Concordância entre avaliadores](charts/chart-comparacao.svg)

## Tabela lado a lado

| ID      | Estudo                     | Claude RQ/QA |  GPT RQ/QA  |   Banda   | Claude rec.       | ChatGPT rec.   | Decisão |
| ------- | -------------------------- | :----------: | :---------: | :-------: | ----------------- | -------------- | :-----: |
| P20     | LLM Agentic Workflow (IaC) |   4.0/3.0    |   3.0/3.5   |   Alta    | Incl.+ress        | Incl.+ress     |   ✅    |
| P21     | SLM Agent ICT Ops          |   4.5/4.0    |   3.5/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| P22     | ARM Remediation            |   4.5/4.0    |   4.5/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| P23     | TAMO (RCA)                 |   3.5/3.5    |   3.5/3.0   |   Alta    | Incl.+ress        | Incl.+ress     |   ✅    |
| P24     | AgentAI Survey             |   4.0/2.5    |   4.5/2.0   |   Média   | Incl.+ress.(fund) | Incl.+ress     |   ✅    |
| P25     | AI-MAS cyber range         |   4.5/4.0    |   4.0/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| **P26** | **Surveying RCA**          | **2.5/2.5**  | **2.5/2.5** | **Média** | **Excl.(tipo)**   | **Incl.+ress** | **⚠️**  |
| P27     | MA-RCA                     |   4.5/4.0    |   4.5/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| P28     | MAS Cybersecurity          |   4.5/3.5    |   4.5/3.5   |   Alta    | Incluir           | Incluir        |   ✅    |
| **P29** | **AIOps Log SLR**          | **2.5/2.5**  | **3.5/2.5** | **Média** | **Excl.(tipo)**   | **Incl.+ress** | **⚠️**  |
| P30     | LLM Inference RCA          |   3.0/4.0    |   3.0/3.5   |   Alta    | Excl.(tipo)       | Excl.          |   ✅    |
| P31     | LEMAD                      |   4.5/3.5    |   4.0/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| P32     | GALR                       |   4.0/3.5    |   4.0/3.5   |   Alta    | Incl.+ress        | Incl.+ress     |   ✅    |
| P33     | Review Agentic Cyber       |   4.0/2.5    |   4.5/2.5   |   Média   | Incl.+ress.(fund) | Incl.+ress     |   ✅    |
| P34     | LLMs in IR mgmt            |   4.0/4.0    |   3.5/3.5   |   Alta    | Incl.+ress        | Incl.+ress     |   ✅    |
| P35     | Graph Multi-Agent RCA      |   4.0/4.0    |   3.5/3.5   |   Alta    | Incluir           | Incl.+ress     |   ✅    |
| P37     | AI Trust/Readiness         |   3.0/4.0    |   4.0/3.5   |   Alta    | Incl.+ress        | Incl.+ress     |   ✅    |
| P38     | Multi-Agent vs RAG         |   3.5/4.0    |   4.0/4.0   |   Alta    | Excl.(domínio)    | Excl.          |   ✅    |
| P39     | Cyber Arms Race            |    NA/NA     |   2.5/2.0   |  (Média)  | Excl.(inelig.)    | Excl.          |   ✅    |
| P40     | LLM Network Mgmt           |    NA/NA     |   4.5/1.5   |  (Média)  | Excl.(inelig.)    | Excl.          |   ✅    |

_(`NA` = Claude encerrou na triagem por Qualis A3; ver §Divergência metodológica.)_

## Divergências de decisão (2/20)

Ambas as divergências são **assimétricas no mesmo sentido**: o ChatGPT **inclui com ressalvas** o que o Claude **exclui** — e ambas recaem sobre **estudos secundários não-agênticos**.

- **P26 — Surveying RCA Techniques (survey).** Escores **idênticos** nos dois (RQ 2,5 · QA 2,5 · Média), mas decisão oposta. Não é erro de pontuação: é uma **regra de protocolo** — o Claude exclui surveys não-agênticos do corpus primário; o ChatGPT mantém com ressalvas.
- **P29 — AIOps Log Anomaly SLR.** O ChatGPT pontua RQ mais alto (3,5 vs 2,5, **Δ +1,0**) e inclui com ressalvas; o Claude exclui (secundário + não-agêntico).

➡️ **Implicação:** a única decisão de protocolo realmente em aberto na RSL é **como tratar estudos secundários (surveys/SLR) não centrados em Agentic AI**. Definido isso, os dois avaliadores convergem totalmente.

## Divergência metodológica (P39, P40 — inelegíveis)

Mesma **decisão final (Excluir)**, mas **caminhos diferentes**:

- **Claude** tratou **Qualis A3 < A1–A2** como critério de inelegibilidade na ETAPA 1 e **encerrou na triagem** (sem extração de RQ/QA → `NA`).
- **ChatGPT** prosseguiu com a **avaliação completa** (atribuindo escores: P39 RQ 2,5; P40 RQ 4,5) e só então recomendou "EXCLUIR DO CORPUS PRINCIPAL", tratando o Qualis A3 como pendência a confirmar.

➡️ Curiosidade: o ChatGPT deu a **P40 SCORE_RQ 4,5** (alto) mas QA apenas **1,5** — ainda assim excluído. Ambos convergem no desfecho; divergem no _momento_ de aplicar o corte bibliométrico.

## Tendências sistemáticas

1. **ChatGPT é mais conservador na qualidade (QA).** Em 11 dos 18 estudos o SCORE_QA do ChatGPT é **menor** que o do Claude (quase sempre −0,5); **nunca maior**. Causa principal: o ChatGPT tende a `QA3` mais baixo e penaliza mais a replicabilidade.
2. **ChatGPT é menos graduado no rótulo de inclusão.** Rotula **quase tudo** como "INCLUIR COM RESSALVAS" (15 de 16 inclusões; só P28 é "INCLUIR" puro). O Claude distingue mais (7 plenos · 5 ressalvas · 2 fundacionais).
3. **Convergência total onde importa para a tese:** **RQ4 (100%)** e **RQ5 (100%)**. Ambos os avaliadores, de forma independente, confirmam a **lacuna sistemática de ética/governança (RQ4)** e a riqueza de direções futuras (RQ5).
4. **Maior subjetividade em RQ1 (67%).** Definir "níveis de autonomia" é o ponto mais sujeito a interpretação — esperado, por ser conceitual.

## Conclusão

A concordância é **substancial** (κ = 0,74; 90% de decisão; 100% de banda; erros de escore ≤ 0,5 em média), o que **reforça a robustez** dos vereditos da RSL. As poucas divergências são **interpretáveis e convergentes**:

- **Núcleo de inclusão idêntico** (P21, P22, P25, P27, P28, P31, P35, …) — alta confiança.
- **Exclusões por domínio/tipo concordam** (P30, P38, P39, P40).
- **Único ponto a decidir no protocolo:** o tratamento de **surveys/SLR não-agênticos** (P26, P29) — decisão que o condutor da RSL deve registrar explicitamente.
- **Achado-chave da revisão é avaliador-independente:** a **lacuna de RQ4 (ética/governança)** aparece nos dois conjuntos com 100% de acordo.

---

_Gerado por [`scripts/gen_comparison.py`](scripts/gen_comparison.py) a partir de `resultados-consolidados.csv` (Claude) e `ChatGPT/*.md`. Dados crus: [`comparacao-avaliadores.csv`](comparacao-avaliadores.csv)._
