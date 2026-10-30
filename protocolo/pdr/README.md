# PDRs — Protocol Decision Records

Registros numerados e **imutáveis** de toda decisão que mudou o protocolo
desta revisão. PDR-0001 a PDR-0005 são **registros retroativos** (2026-10-27)
de decisões tomadas e documentadas ao longo dos ciclos (MEMORY.md e artigo
§III-E); novos PDRs nascem **antes** de a decisão ser aplicada
(Constituição, Art. II).

Regras:

1. Numeração contígua `PDR-0001`, `PDR-0002`, … (verificada pelo `check-rsl.sh`).
2. PDRs não são editados após ratificação — um PDR novo pode _substituir_
   outro (`status: superseded-by PDR-NNNN`).
3. Toda divergência protocolar entre avaliadores cita o PDR que a resolve.

## Índice

| PDR                                                              | Título                                                                  | Status     | Data da decisão |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------- | --------------- |
| [PDR-0001](PDR-0001-comparison-somente-com-baseline-empirico.md) | Comparison somente com baseline empírico executado (regra v1.1.0)       | ratificado | ciclo 1         |
| [PDR-0002](PDR-0002-emenda-de-estratos-ciclo-2.md)               | Emenda de estratos do ciclo 2 (ressalva obrigatória)                    | ratificado | 2026-09-09      |
| [PDR-0003](PDR-0003-r1-secundarios-nao-agenticos.md)             | R1: secundários não-agênticos fora do corpus primário                   | ratificado | 2026-10-26      |
| [PDR-0004](PDR-0004-r2-emendas-no-texto-normativo.md)            | R2: emendas só no texto normativo da Etapa 1                            | ratificado | 2026-10-26      |
| [PDR-0005](PDR-0005-r3-corte-de-dominio-e-cluster-humano.md)     | R3: corte de domínio estrito e cluster humano restrito a COGNITIVE_LOAD | ratificado | 2026-10-26      |
| [PDR-0006](PDR-0006-estrato-de-conference-papers-pelo-percentil-da-serie.md) | Estrato de conference papers pelo percentil Scopus da série | ratificado | 2026-10-28 |
| [PDR-0007](PDR-0007-renovacao-da-emenda-de-estratos-para-o-ciclo-3.md) | Renovação da emenda de estratos para o ciclo 3 | ratificado | 2026-10-28 |
| [PDR-0008](PDR-0008-remocao-dos-springer-nao-recuperados.md) | Remoção dos capítulos Springer não recuperados (reports not retrieved) | ratificado | 2026-10-29 |
| [PDR-0009](PDR-0009-elegibilidade-por-quartil-do-percentil-scopus.md) | Elegibilidade por quartil do percentil Scopus (Q1–Q3); Qualis/SJR informativos | ratificado | 2026-10-30 |

Template para novos PDRs: [`PDR-TEMPLATE.md`](PDR-TEMPLATE.md).
