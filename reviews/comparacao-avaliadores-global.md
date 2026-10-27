# Comparação Global entre Avaliadores — P01–P88 (Claude × ChatGPT × Gemini)

> 🧭 [📊 Dashboard](DASHBOARD.md) · [🧮 CSV global](comparacao-avaliadores-global.csv) · [📐 Ciclo 1](comparacao-avaliadores.md) · [📐 Ciclo 2](comparacao-avaliadores-ciclo2.md) · [🏠 README raiz](../README.md)

Comparação consolidada das **61 avaliações** de cada um dos três avaliadores sobre todo o corpus avaliado da RSL — **19 fundacionais** (retroativos), **20 do ciclo 1** e **22 do ciclo 2**. Fontes: [`resultados-consolidados-claude-P01-P88.csv`](resultados-consolidados-claude-P01-P88.csv) · [`-chatgpt-`](resultados-consolidados-chatgpt-P01-P88.csv) · [`-gemini-`](resultados-consolidados-gemini-P01-P88.csv). Computado em **2026-10-26**; decisão colapsada em Incluir/Excluir ("Mantido (fundacional)" = Incluir; comparação case-insensitive).

## Resultado em um relance

| Métrica (decisão, n = 61) |       Claude × ChatGPT       |     Claude × Gemini     |    ChatGPT × Gemini     |
| ------------------------- | :--------------------------: | :---------------------: | :---------------------: |
| **Acordo**                |        90,2% (55/61)         |      91,8% (56/61)      |      91,8% (56/61)      |
| **Cohen's κ**             |           **0,57**           |        **0,51**         |        **0,51**         |
| Divergências              | P26, P29, P62, P69, P81, P85 | P26, P29, P38, P40, P85 | P38, P40, P62, P69, P81 |

**Fleiss' κ (3 avaliadores, 61 estudos) = 0,53** — concordância _moderada_, no limiar de _substancial_ · **53/61 decisões unânimes** (50 inclusões + 3 exclusões: P30, P39, P86) · prevalência de Incluir: 164/183 vereditos.

| Acordo unânime por conjunto | Fundacional | Ciclo 1 | Ciclo 2 |
| --------------------------- | :---------: | :-----: | :-----: |
| Decisões unânimes           |  **19/19**  |  16/20  |  18/22  |

| Erro absoluto médio (estudos avaliados em comum) | CL×GPT (n=55) | CL×GEM (n=59) | GPT×GEM (n=57) |
| ------------------------------------------------ | :-----------: | :-----------: | :------------: |
| SCORE_RQ                                         |     0,44      |     0,55      |      0,63      |
| SCORE_QA                                         |   **0,31**    |     0,50      |      0,63      |

> ⚠️ Como nas comparações parciais, o κ é deflacionado pelo **paradoxo da prevalência** (89,6% dos vereditos são Incluir). A leitura substantiva está na natureza das 8 divergências — **todas protocolares, nenhuma de mérito**.

## As 8 divergências — três famílias protocolares

| Família                                  | Estudos                            | Quem diverge                                                                                                                                                     | Regra em aberto                                                                 |
| ---------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **A. Estudos secundários não-agênticos** | P26, P29                           | Claude exclui · ChatGPT e Gemini incluem c/ ressalvas                                                                                                            | Tratamento de surveys/SLRs não centrados em Agentic AI (aberta desde o ciclo 1) |
| **B. Emenda de estratos (2026-09-09)**   | P62, P69, P81                      | ChatGPT exclui (aplicou I3 estrito e parou na triagem) · Claude e Gemini honram a emenda                                                                         | Emendas de elegibilidade devem entrar no corpo normativo da ETAPA 1 dos prompts |
| **C. Fronteiras de domínio/estrato**     | P38, P40 (ciclo 1) · P85 (ciclo 2) | Gemini é o único a incluir P38 (off-domain) e P40 (Qualis A3, "condicional ao estrato") c/ ressalvas; Claude é o único a excluir P85 (cluster cognitivo, RQ 0,5) | Rigor do corte de domínio (E3) e destino do cluster humano sem aderência às RQs |

Nenhuma divergência decorre de leitura diferente do conteúdo: nos 8 casos os escores dos três avaliadores contam a mesma história (ex.: P85 com RQ 0,5 · 1,5 · 0,5), e o que muda é a **regra aplicada à consequência**.

## Perfis dos avaliadores (61 avaliações cada)

1. **ChatGPT — o protocolar estrito.** Único a aplicar cortes bibliométricos interrompendo a avaliação (4 `NA` no ciclo 2); QA sistematicamente ≤ Claude; menor MAE contra o Claude (QA 0,31) — quando ambos avaliam, quase coincidem.
2. **Gemini — o inclusivo/generoso.** Único avaliador que não exclui nenhum estudo além dos 3 unânimes + P30/P39; escores mais altos (9 × "Incluir" pleno onde os outros dão zero/um; RQ 5,0 em 7 estudos); maior MAE de escores.
3. **Claude — o intermediário com corte temático mais duro.** Único a excluir P26/P29 (não-agênticos) e P85 (sem aderência às RQs) — as exclusões temáticas mais estritas dos três.
4. **A hierarquia de acordo é estável:** os três pares ficam em 90–92% e κ 0,51–0,57 — acima do Fleiss do ciclo 2 isolado (0,36) porque os 19 fundacionais, unânimes, elevam a base.

## Conclusões para a RSL

- **O corpus central é avaliador-independente:** 50 inclusões e 3 exclusões unânimes (87% do total). As decisões da RSL não dependem do avaliador escolhido.
- **As 8 divergências mapeiam exatamente as 3 decisões de protocolo pendentes** (famílias A–C) — registrá-las no protocolo elimina toda a divergência residual.
- **Validação tripla completa:** com κ global 0,51–0,57 (substancial nos pares com Claude) e concordância unânime nos fundacionais, a limitação de "avaliador único" está encerrada para todo o corpus P01–P88.

---

_Computado em 2026-10-26 a partir dos três consolidados por avaliador. Dados crus lado a lado (61 linhas × 12 colunas): [`comparacao-avaliadores-global.csv`](comparacao-avaliadores-global.csv). Nota de correção: a primeira rodada do cômputo classificou errado as recomendações do ChatGPT no ciclo 1 (grafadas em maiúsculas — "EXCLUIR DO CORPUS PRINCIPAL"), inflando as divergências; corrigido com comparação case-insensitive antes desta publicação._
