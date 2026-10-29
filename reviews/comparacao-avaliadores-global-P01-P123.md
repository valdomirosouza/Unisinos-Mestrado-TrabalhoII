# Comparação Global entre Avaliadores — P01–P123 (Claude × ChatGPT × Gemini)

> 🧭 [📊 Dashboard](DASHBOARD.md) · [🧮 CSV global](comparacao-avaliadores-global-P01-P123.csv) · [📐 Ciclo 1](comparacao-avaliadores.md) · [📐 Ciclo 2](comparacao-avaliadores-ciclo2.md) · [📐 Ciclo 3](comparacao-avaliadores-ciclo3.md) · [📐 Global P01–P88 (histórico)](comparacao-avaliadores-global.md) · [🏠 README raiz](../README.md)

Comparação consolidada das **74 avaliações** de cada um dos três avaliadores sobre todo o corpus avaliado da RSL — **19 fundacionais** (retroativos), **20 do ciclo 1**, **22 do ciclo 2** e **13 do ciclo 3**. Substitui, como retrato corrente, a [comparação global P01–P88](comparacao-avaliadores-global.md) (2026-10-26), que permanece como registro histórico (Art. VI). Fontes: [`resultados-consolidados-claude-P01-P123.csv`](resultados-consolidados-claude-P01-P123.csv) · [`-chatgpt-`](resultados-consolidados-chatgpt-P01-P123.csv) · [`-gemini-`](resultados-consolidados-gemini-P01-P123.csv). Computado em **2026-10-29** com `scripts/compute-kappa.py`; decisão colapsada em Incluir/Excluir ("Mantido (fundacional)" = Incluir; case-insensitive).

## Resultado em um relance

| Métrica (decisão, n = 74) |       Claude × ChatGPT       |     Claude × Gemini     |    ChatGPT × Gemini     |
| ------------------------- | :--------------------------: | :---------------------: | :---------------------: |
| **Acordo**                |        91,9% (68/74)         |      93,2% (69/74)      |      93,2% (69/74)      |
| **Cohen's κ**             |           **0,62**           |        **0,58**         |        **0,58**         |
| Divergências              | P26, P29, P62, P69, P81, P85 | P26, P29, P38, P40, P85 | P38, P40, P62, P69, P81 |

**Fleiss' κ (3 avaliadores, 74 estudos) = 0,60** — concordância _moderada_ no limiar exato de _substancial_ (Landis & Koch) · **66/74 decisões unânimes** (62 inclusões + 4 exclusões: P30, P39, P86, P106) · prevalência de Incluir: 200/222 vereditos (90,1%).

| Acordo unânime por conjunto | Fundacional | Ciclo 1 | Ciclo 2 |  Ciclo 3  |
| --------------------------- | :---------: | :-----: | :-----: | :-------: |
| Decisões unânimes           |  **19/19**  |  16/20  |  18/22  | **13/13** |

| Erro absoluto médio (estudos avaliados em comum) | CL×GPT (n=68) | CL×GEM (n=72) | GPT×GEM (n=70) |
| ------------------------------------------------ | :-----------: | :-----------: | :------------: |
| SCORE_RQ                                         |     0,43      |     0,52      |      0,61      |
| SCORE_QA                                         |   **0,31**    |     0,45      |      0,61      |

> ⚠️ O κ segue deflacionado pelo **paradoxo da prevalência** (90,1% dos vereditos são Incluir) — mas **todos os indicadores subiram** com o ciclo 3: κ de Cohen 0,51–0,57 → **0,58–0,62** (Claude×ChatGPT agora _substancial_), Fleiss 0,53 → **0,60**, acordo bruto 90,2–91,8% → 91,9–93,2%.

## As 8 divergências — todas anteriores ao ciclo 3, famílias fechadas por PDRs

As divergências são **as mesmas 8 da comparação P01–P88** (nenhuma nova no ciclo 3), nas três famílias protocolares já mapeadas — e cada família agora tem a regra registrada:

| Família                                  | Estudos       | Quem diverge                                                                 | Regra que a fecha                                                                                        |
| ---------------------------------------- | ------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **A. Estudos secundários não-agênticos** | P26, P29      | Claude exclui · ChatGPT e Gemini incluem c/ ressalvas                        | [PDR-0003 (R1)](../protocolo/pdr/PDR-0003-r1-secundarios-nao-agenticos.md)                               |
| **B. Emenda de estratos (2026-09-09)**   | P62, P69, P81 | ChatGPT aplicou I3 estrito e parou na triagem (`NA`)                         | [PDR-0004 (R2)](../protocolo/pdr/PDR-0004-r2-emendas-no-texto-normativo.md) — emendas no texto normativo |
| **C. Fronteiras de domínio/estrato**     | P38, P40, P85 | Gemini inclui off-domain/A3 c/ ressalvas · Claude exclui o cluster cognitivo | [PDR-0005 (R3)](../protocolo/pdr/PDR-0005-r3-corte-de-dominio-e-cluster-humano.md)                       |

**O ciclo 3 é o teste empírico dessas regras — e elas passaram:** com as emendas PDR-0006/0007 renderizadas no corpo normativo (R2), o ChatGPT avaliou todos os 13 (zero `NA`, família B zerada); com R1 explícito, os três convergiram nos secundários fundacionais-condicionais (P110, P112, P121); com R3, a exclusão de domínio do P106 (E2) foi **unânime**. Nenhuma divergência decorre de leitura diferente do conteúdo — nos 8 casos históricos, os escores contam a mesma história e o que mudava era a regra de consequência, agora registrada.

## Perfis dos avaliadores (74 avaliações cada)

1. **ChatGPT — o protocolar estrito.** QA sistematicamente ≤ Claude (no ciclo 3: mediana 2,5 e só 5 bandas Alta vs. 9); menor MAE contra o Claude (QA 0,31) — quando ambos avaliam sob a mesma regra, quase coincidem. Os 4 `NA` do ciclo 2 não se repetiram no ciclo 3 (R2 em vigor).
2. **Gemini — o inclusivo/generoso, convergindo.** Segue com os escores mais altos do trio, mas no ciclo 3 as bandas coincidiram 13/13 com as do Claude — a generosidade residual está na intensidade (RQ 5,0 frequente), não mais na decisão.
3. **Claude — o intermediário com corte temático mais duro.** Mantém as exclusões temáticas mais estritas (P26/P29/P85 históricos); no ciclo 3 ficou no centro exato (bandas idênticas às do Gemini, MAE mínimo com ambos).
4. **A hierarquia de acordo subiu em bloco:** pares em 91,9–93,2% e κ 0,58–0,62; o par Claude×ChatGPT cruzou para _substancial_ (0,62).

## Conclusões para a RSL

- **O corpus central é avaliador-independente:** 62 inclusões e 4 exclusões unânimes (89% do total, ante 87% em P01–P88). As decisões da RSL não dependem do avaliador escolhido.
- **A divergência residual é histórica e fechada:** as 8 divergências são todas pré-ciclo 3 e cada família tem PDR registrado (R1/R2/R3); o ciclo 3, conduzido já sob essas regras, saiu **100% unânime** (κ = 1,00).
- **Validação tripla completa de P01–P123:** com κ global 0,58–0,62, Fleiss 0,60 e um ciclo inteiro sem divergências, a limitação de "avaliador único" está encerrada para todo o corpus avaliado da revisão.

---

_Computado em 2026-10-29 a partir dos três consolidados por avaliador P01–P123 (os consolidados P01–P88 e a comparação global anterior permanecem como registros históricos). Dados crus lado a lado (74 linhas × 12 colunas): [`comparacao-avaliadores-global-P01-P123.csv`](comparacao-avaliadores-global-P01-P123.csv)._
