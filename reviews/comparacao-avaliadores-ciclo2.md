# Comparação entre avaliadores — Ciclo 2 (Claude × ChatGPT × Gemini)

> 🧭 [📊 Dashboard](DASHBOARD.md) · [📄 Síntese consolidada](relatorio-sintese-consolidado.md) · [🧮 CSV da comparação](comparacao-avaliadores-ciclo2.csv) · [📐 Comparação do ciclo 1](comparacao-avaliadores.md) · [🏠 README raiz](../README.md)

**Três avaliadores** executaram independentemente o mesmo protocolo (prompts [`prompt-P43…P88.md`](../prompts/) + Kitchenham/DARE) sobre os **22 estudos aprovados na triagem do ciclo 2**:

- **Claude** → pareceres oficiais em [`review-Pxx.md`](.) (escores em [`resultados-consolidados-ciclo2.csv`](resultados-consolidados-ciclo2.csv)), 2026-09-10.
- **ChatGPT** → [`ChatGPT/Pxx_avaliacao_RSL.md`](ChatGPT/), entregues em 2026-10-25.
- **Gemini** → [`Gemini/Pxx_avaliacao_RSL.md`](Gemini/), entregues em 2026-10-25.

Computado em 2026-10-25. Decisão colapsada em **Incluir/Excluir** (como no ciclo 1); escores extraídos dos arquivos de cada avaliador e conferidos manualmente nos casos ambíguos.

## Resultado em um relance

| Métrica (decisão Incluir/Excluir) |  Claude × ChatGPT  |  Claude × Gemini  | ChatGPT × Gemini |
| --------------------------------- | :----------------: | :---------------: | :--------------: |
| **Acordo**                        |   81,8% (18/22)    | **95,5% (21/22)** |  86,4% (19/22)   |
| **Cohen's κ**                     |        0,24        |     **0,65**      |       0,35       |
| Divergências                      | P62, P69, P81, P85 |        P85        |  P62, P69, P81   |

**Fleiss' κ (3 avaliadores) = 0,36** · acordo bruto médio por par = 87,9%.

> ⚠️ **Paradoxo da prevalência** (mesmo fenômeno da [comparação PICOC](../picoc/picoc-comparacao-avaliadores.md)): com 17/22 estudos incluídos por unanimidade, a prevalência altíssima de "Incluir" deflaciona o κ — 4 divergências em 22 casos derrubam o κ de Claude×ChatGPT para 0,24 apesar de 81,8% de acordo bruto. O κ deve ser lido junto do acordo e, principalmente, da **natureza das divergências** (abaixo: todas protocolares, nenhuma de mérito).

| Escores (estudos avaliados em comum) | Claude × ChatGPT (n=18) | Claude × Gemini (n=22) |
| ------------------------------------ | :---------------------: | :--------------------: |
| Erro absoluto médio SCORE_RQ         |          0,53           |          0,66          |
| Erro absoluto médio SCORE_QA         |        **0,31**         |          0,68          |
| Acordo de banda de qualidade         |       72% (13/18)       |      64% (14/22)       |

## Tabela lado a lado

| ID      | Claude RQ/QA |  GPT RQ/QA  |  GEM RQ/QA  | Claude rec.         | ChatGPT rec.              | Gemini rec.                  | Decisão |
| ------- | :----------: | :---------: | :---------: | ------------------- | ------------------------- | ---------------------------- | :-----: |
| P43     |   3.0/2.0    |   3.0/2.0   |   4.5/2.5   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P52     |   3.5/2.5    |   3.0/2.0   |   3.5/3.5   | Incl.+ress (fund)   | Incl.+ress (fund)         | **Incluir** (fund)           |   ✅    |
| P53     |   3.5/3.0    |   2.0/2.5   |   4.0/4.0   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P54     |   4.5/2.0    |   4.0/2.0   |   4.5/3.0   | Incl.+ress (fund)   | Incl.+ress (fund)         | **Incluir** (fund)           |   ✅    |
| P55     |   4.5/2.5    |   4.5/2.5   |   4.5/2.5   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| **P62** | **2.0/1.5**  |   **NA**    | **3.5/2.5** | **Incl.+ress ⚠️A3** | **Excl. (INELEGÍVEL A3)** | **Incl.+ress ⚠️A3**          | **⚠️**  |
| P63     |   2.0/3.5    |   1.5/3.0   |   1.5/4.0   | Incl.+ress (instr.) | Incl.+ress                | Incl.+ress                   |   ✅    |
| **P69** | **1.0/3.5**  |   **NA**    | **1.5/4.0** | **Incl.+ress ⚠️A3** | **Excl. (INELEGÍVEL A3)** | **Incl.+ress ⚠️A3**          | **⚠️**  |
| P72     |   3.5/1.5    |   3.0/1.5   |   4.0/3.5   | Incl.+ress (fund)   | Incl.+ress (fund)         | Incl.+ress (fund)            |   ✅    |
| P73     |   3.5/4.0    |   3.5/3.0   |   3.5/4.0   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P74     |   3.0/1.0    |   2.0/1.0   |   1.5/2.0   | Incl.+ress (LLMOps) | Incl.+ress                | Incl.+ress                   |   ✅    |
| P76     |   4.0/2.5    |   4.5/3.0   |   5.0/3.5   | Incl.+ress          | Incl.+ress                | **Incluir**                  |   ✅    |
| P77     |   3.5/1.5    |   2.5/1.0   |   3.5/3.0   | Incl.+ress (fund)   | Incl.+ress (fund)         | Incl.+ress (fund)            |   ✅    |
| P78     |   4.0/3.5    |   3.5/3.0   |   5.0/3.5   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P79     |   5.0/3.0    |   4.5/3.0   |   5.0/3.5   | Incl.+ress (fund)   | Incl.+ress (fund)         | **Incluir** (fund)           |   ✅    |
| **P81** | **3.0/3.5**  |   **NA**    | **5.0/4.0** | **Incl.+ress ⚠️A4** | **Excl. (INELEGÍVEL A4)** | **Incl.+ress ⚠️A4**          | **⚠️**  |
| P82     |   3.5/2.5    |   4.0/2.5   |   4.5/3.0   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P83     |   3.5/2.5    |   3.5/3.0   |   4.0/3.5   | Incl.+ress          | Incl.+ress                | **Incluir**                  |   ✅    |
| **P85** | **0.5/3.5**  | **1.5/2.5** | **0.5/3.0** | **Excluir (RQs)**   | **Incl.+ress (cluster)**  | **Incl.+ress (condicional)** | **⚠️**  |
| P86     |   2.0/3.0    |     NA      |   2.0/3.5   | Excluir ⚠️B1+Q3     | Excluir (INELEGÍVEL)      | Excluir                      |   ✅    |
| P87     |   3.5/3.5    |   3.0/3.5   |   5.0/4.0   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |
| P88     |   3.0/4.0    |   2.5/4.0   |   4.0/4.0   | Incl.+ress          | Incl.+ress                | Incl.+ress                   |   ✅    |

_(`NA` = ChatGPT encerrou na triagem por inelegibilidade de estrato; ver divergência metodológica.)_

## As 4 divergências — todas protocolares, nenhuma de mérito

### 1. P62, P69, P81 — aplicação da emenda de estratos (Claude+Gemini × ChatGPT)

O ChatGPT aplicou o **critério estrito I3** (Qualis A1–A2) aos três estudos fora de estrato, declarou-os **INELEGÍVEIS na Etapa 1 e encerrou sem avaliar** (por isso `NA`), apesar de a linha `ressalvas_triagem` dos prompts registrar a [emenda de protocolo de 2026-09-09](triagem-ciclo2.md). Claude e Gemini honraram a emenda e avaliaram com ressalva de estrato. É a **reedição invertida** da divergência metodológica de P39/P40 no ciclo 1 — lá o _Claude_ parou na triagem e o _ChatGPT_ avaliou até o fim. A lição é a mesma: **emendas de protocolo precisam estar no corpo normativo do prompt (ETAPA 1), não apenas nos insumos**, para serem aplicadas uniformemente.

### 2. P85 — tratamento do cluster de carga cognitiva (Claude × ChatGPT+Gemini)

Os três avaliadores **concordam no mérito** — nenhuma aderência às RQs agênticas (RQ: Claude 0,5 · Gemini **0,5** · ChatGPT 1,5). Divergem na **consequência**: Claude exclui; ChatGPT e Gemini incluem com ressalvas "exclusivamente como evidência complementar do cluster carga cognitiva/fadiga", o Gemini explicitamente **condicionando ao comitê da RSL** manter o cluster sociotécnico. É a decisão de protocolo em aberto análoga à de P26/P29 no ciclo 1 (lá: surveys não-agênticos; aqui: **estudos do cluster humano sem aderência direta às RQs**) — cabe ao condutor da RSL registrar a regra.

### 3. P86 — exclusão unânime

Único estudo excluído pelos três (Claude e Gemini após avaliação; ChatGPT na triagem). Reforça a robustez do corte: não-agêntico + estrato B1/SJR Q3.

## Tendências sistemáticas

1. **Gemini é o avaliador mais generoso.** SCORE_RQ ≥ 4,5 em 9/22 (Claude: 3; ChatGPT: 3) e QA ≥ 3,5 em 11/22; único a conceder **5 "INCLUIR" plenos** (P52, P54, P76, P79, P83) onde Claude e ChatGPT dão zero. MAE de QA vs. Claude = 0,68 e acordo de banda de só 64%.
2. **ChatGPT segue o mais conservador** — mesma tendência do ciclo 1: QA nunca acima do Claude em 14/18 estudos comuns e rigor protocolar máximo (único a aplicar o corte estrito de estrato). MAE de QA vs. Claude = **0,31**, o menor dos pares: quando ambos avaliam, quase coincidem.
3. **Claude fica no centro** — e o par Claude×Gemini tem o maior acordo de decisão (95,5%, κ = 0,65, "substancial").
4. **Convergência onde importa para a tese:** os três avaliadores (i) incluem por unanimidade os **17 estudos do núcleo**; (ii) dão escores baixos de RQ ao P85 e altos ao P79 (RQ 4,5–5,0 nos três — o survey de SOC é o consenso de maior aderência); (iii) confirmam de forma independente que **nenhum estudo do ciclo 2 mede MTTD/MTTR com baseline próprio** — o achado central é avaliador-independente também no ciclo 2.

## Conclusão

O acordo bruto é alto (81,8–95,5% por par; 87,9% médio) e **todas as divergências são protocolares** — aplicação da emenda de estratos (3 casos) e tratamento do cluster de carga cognitiva (1 caso) — não havendo nenhuma divergência de mérito sobre conteúdo. O κ mais baixo (Fleiss 0,36) reflete o paradoxo da prevalência já documentado na comparação PICOC, não desacordo substantivo. Duas regras de protocolo devem ser registradas pelo condutor da RSL para eliminar as divergências remanescentes: **(a)** emendas de elegibilidade entram no texto normativo da ETAPA 1 dos prompts; **(b)** definição explícita do destino dos estudos do cluster humano sem aderência às RQs (excluir × manter como evidência complementar).

---

_Computado em 2026-10-25 a partir de `resultados-consolidados-ciclo2.csv` (Claude), `ChatGPT/*.md` e `Gemini/*.md`. Dados crus: [`comparacao-avaliadores-ciclo2.csv`](comparacao-avaliadores-ciclo2.csv). A comparação do ciclo 1 (Claude × ChatGPT, κ = 0,74) permanece em [`comparacao-avaliadores.md`](comparacao-avaliadores.md)._
