# Comparação entre avaliadores — Ciclo 3 (Claude × ChatGPT × Gemini)

> 🧭 [📊 Dashboard](DASHBOARD.md) · [📄 Síntese consolidada](relatorio-sintese-consolidado.md) · [🧮 CSV da comparação](comparacao-avaliadores-ciclo3.csv) · [📐 Comparação do ciclo 2](comparacao-avaliadores-ciclo2.md) · [🏠 README raiz](../README.md)

**Três avaliadores** executaram independentemente o mesmo protocolo (prompts imutáveis [`prompt-P91…P123.md`](../prompts/README.md), template v1.1.0 com as emendas PDR-0006/0007 **no texto normativo**, + Kitchenham/DARE) sobre os **13 estudos aprovados na triagem do ciclo 3**:

- **Claude** → pareceres oficiais em [`review-Pxx.md`](.) (escores em [`resultados-consolidados-ciclo3.csv`](resultados-consolidados-ciclo3.csv)), 2026-10-28.
- **ChatGPT** → [`ChatGPT/Pxx_avaliacao_RSL.md`](ChatGPT/README.md), entregues em 2026-10-29.
- **Gemini** → [`Gemini/Pxx_avaliacao_RSL.md`](Gemini/README.md), entregues em 2026-10-29.

Computado em 2026-10-29 com `scripts/compute-kappa.py` (decisão colapsada em **Incluir/Excluir**, regra: recomendação iniciada por "incluir"/"mantido" = Incluir). Dados crus: [`comparacao-avaliadores-ciclo3.csv`](comparacao-avaliadores-ciclo3.csv).

## Resultado em um relance

| Métrica (decisão Incluir/Excluir) | Claude × ChatGPT | Claude × Gemini | ChatGPT × Gemini |
| --------------------------------- | :--------------: | :-------------: | :--------------: |
| **Acordo**                        |   100% (13/13)   |  100% (13/13)   |   100% (13/13)   |
| **Cohen's κ**                     |     **1,00**     |    **1,00**     |     **1,00**     |
| Divergências de decisão           |     nenhuma      |     nenhuma     |     nenhuma      |

**Fleiss' κ (3 avaliadores) = 1,00** · prevalência de Incluir 92,3% (36/39) · **unanimidade nos 13 estudos** (12 Incluir · 1 Excluir — P106, E2). Na escala Landis & Koch, κ = 1,00 é o teto da banda _almost perfect_ (0,81–1,00) — e, ao contrário dos ciclos 1–2, aqui o κ não é deflacionado pelo paradoxo da prevalência porque não há **nenhum** desacordo a penalizar.

| Escores (n = 13 em todos os pares) | Claude × ChatGPT | Claude × Gemini  | ChatGPT × Gemini |
| ---------------------------------- | :--------------: | :--------------: | :--------------: |
| Erro absoluto médio SCORE_RQ       |       0,42       |     **0,38**     |       0,50       |
| Erro absoluto médio SCORE_QA       |       0,31       |     **0,23**     |       0,54       |
| Acordo de banda de qualidade       |    62% (8/13)    | **100% (13/13)** |    62% (8/13)    |

## Tabela lado a lado

| ID       | Claude RQ/QA |  GPT RQ/QA  |  GEM RQ/QA  | Claude rec.            | ChatGPT rec.     | Gemini rec.       |        Decisão        |
| -------- | :----------: | :---------: | :---------: | ---------------------- | ---------------- | ----------------- | :-------------------: |
| P91      |   2.5/2.5    |   3.0/2.5   |   2.5/2.5   | Incl.+ress ⚠️estrato   | Incl.+ress       | Incl.+ress        |          ✅           |
| P93      |   3.5/2.0    |   3.5/2.0   |   3.5/2.5   | Incl.+ress ⚠️A3        | Incl.+ress       | Incl.+ress        |          ✅           |
| P94      |   4.0/3.5    |   4.0/3.5   |   5.0/4.0   | **Incluir**            | Incl.+ress       | **Incluir**       |          ✅           |
| P97      |   4.5/3.0    |   5.0/3.0   |   4.5/3.0   | Incl.+ress             | Incl.+ress       | Incl.+ress        |          ✅           |
| P100     |   4.5/2.5    |   5.0/2.5   |   4.5/2.5   | Incl.+ress ⚠️B2        | Incl.+ress       | Incl.+ress        |          ✅           |
| P101     |   5.0/3.0    |   5.0/2.5   |   5.0/3.5   | Incl.+ress ⚠️B4        | Incl.+ress       | Incl.+ress        |          ✅           |
| P102     |   5.0/3.0    |   5.0/3.0   |   4.5/3.5   | Incl.+ress ⚠️estrato   | Incl.+ress       | Incl.+ress        |          ✅           |
| **P106** | **2.0/1.0**  | **2.5/2.5** | **1.5/1.0** | **Excluir (E2)**       | **Excluir (E2)** | **Excluir (E2)**  | ✅ (exclusão unânime) |
| P110     |   3.5/3.0    |   4.0/2.0   |   3.0/3.0   | Incl.+ress (fund)      | Incl.+ress       | Incl.+ress (fund) |          ✅           |
| P112     |   4.5/3.5    |   4.5/3.5   |   4.0/3.0   | Incl.+ress (fund)      | Incl.+ress       | Incl.+ress (fund) |          ✅           |
| P119     |   2.5/3.0    |   3.5/2.5   |   2.5/3.0   | Incl.+ress ⚠️A4        | Incl.+ress       | Incl.+ress        |          ✅           |
| P121     |   4.5/3.0    |   3.5/3.0   |   3.5/3.0   | Incl.+ress ⚠️A3 (fund) | Incl.+ress       | Incl.+ress (fund) |          ✅           |
| P123     |   4.0/3.0    |   5.0/2.5   |   5.0/3.5   | Incl.+ress ⚠️A3        | Incl.+ress       | Incl.+ress        |          ✅           |

_Todos os 12 incluídos carregam a **ressalva de estrato obrigatória** (PDR-0006/0007) nos três avaliadores, exceto onde a inclusão é fundacional-condicional (R1)._

## Divergências: nenhuma de decisão — e a lição protocolar do ciclo 2 fechou

**Não há divergência a classificar** (protocolar ou de mérito): os três avaliadores colapsam para a mesma decisão nos 13 estudos, incluindo a **exclusão unânime do P106** (E2 — "Agentic AI" nominal: CNN/RNN/DRL sem agência no sentido do protocolo), que confirma o flag registrado na triagem. **Nenhum PDR novo é necessário.**

O resultado valida a correção protocolar do ciclo 2: lá, a maior família de divergências (P62/P69/P81) nasceu de emendas de elegibilidade fora do texto normativo — o ChatGPT aplicou o corte estrito e **encerrou na triagem sem avaliar** (`NA`). No ciclo 3, com as emendas PDR-0006/0007 injetadas **no corpo normativo** dos prompts pelo render (`--emendas`, regra R2/PDR-0004), o ChatGPT avaliou todos os 13 — **zero `NA`** — e aplicou a ressalva de estrato em vez do corte. A recomendação (a) da conclusão do ciclo 2 está, portanto, verificada empiricamente.

## Diferenças de intensidade (não afetam a decisão)

1. **ChatGPT: RQ mais alto, QA mais baixo.** Média RQ 4,12 (Claude 3,85; Gemini 3,77), mas QA mediana 2,5 e só **5 bandas Alta** contra 9 de Claude e Gemini (acordo de banda 62% com ambos). Os próprios pareceres declaram a rubrica QA como "operacional provisória", o que explica a tendência conservadora — mesmo padrão do ciclo 2 (QA do ChatGPT raramente acima do Claude).
2. **Claude × Gemini praticamente coincidem.** Menor MAE de RQ (0,38) e de QA (0,23) e **acordo de banda 13/13** — as distribuições de banda são idênticas (9 Alta · 3 Média · 1 Baixa). É o par mais próximo, como no ciclo 2 (lá 95,5%, κ 0,65).
3. **P94 é o único pleno** para Claude e Gemini; o ChatGPT o inclui com ressalvas (cautela sobre validação em produção) — diferença de intensidade, não de decisão.
4. **Convergência onde importa para a tese:** os três confirmam, de forma independente, o primeiro cluster de primários com **MTTD/MTTR nominal contra baseline executado** (P100, P101, P102, P123) — o achado que encerra o "nenhum estudo mede MTTD/MTTR nominalmente" dos ciclos 1–2 é **avaliador-independente**, sempre sob ressalva de estrato.

## Conclusão

Acordo perfeito na decisão colapsada (100% nos três pares; Cohen's κ = 1,00; Fleiss' κ = 1,00; 13/13 unânimes), sem nenhuma divergência protocolar ou de mérito — resultado inédito nos três ciclos, atribuível (i) à injeção das emendas no texto normativo dos prompts (lição do ciclo 2, agora automatizada pelo render) e (ii) à triagem com evidência PICOC de leitura integral, que já havia sinalizado o caso-limite P106. As diferenças remanescentes entre avaliadores são de intensidade de escore (sobretudo a rubrica QA conservadora do ChatGPT) e ficam documentadas para a síntese. Com a Etapa 8 fechada, o ciclo 3 incorpora **12 estudos** ao corpus consolidado da RSL.

---

_Computado em 2026-10-29 a partir de `resultados-consolidados-ciclo3.csv` (Claude), `ChatGPT/*.md` e `Gemini/*.md`, via `scripts/compute-kappa.py --evaluators Claude,ChatGPT,Gemini`. Dados crus: [`comparacao-avaliadores-ciclo3.csv`](comparacao-avaliadores-ciclo3.csv). Comparações anteriores: [ciclo 1](comparacao-avaliadores.md) · [ciclo 2](comparacao-avaliadores-ciclo2.md) · [global P01–P88](comparacao-avaliadores-global.md)._
