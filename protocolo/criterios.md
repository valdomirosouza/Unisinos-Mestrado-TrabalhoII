# Critérios de seleção

> Ratificados; mudanças exigem PDR (Constituição, Art. II). Emendas vigentes e
> regras R1–R3 listadas ao final com seus PDRs.

## Inclusão (todos obrigatórios)

| #   | Critério                                                           | Verificação                                 |
| --- | ------------------------------------------------------------------ | ------------------------------------------- |
| I1  | Ano de publicação ≥ 2020                                           | `Papers_Index.csv`                          |
| I2  | Veículo identificável e revisado por pares                         | DOI, ISSN, venue                            |
| I3  | Qualis ∈ {A1, A2} (2025-2028)                                      | qualis.pages.dev / planilha CAPES           |
| I4  | SJR ∈ {Q1, Q2}                                                     | SCImago/Scopus                              |
| I5  | ≥ 1 citação em qualquer um dos 3 indexadores (exceção: < 12 meses) | OpenAlex · Crossref · Scopus, **por fonte** |
| I6  | Aderência temática: abordagem _agêntica_ no domínio _IR/AIOps/SOC_ | extração PICOC de leitura integral          |

## Exclusão

| #   | Critério                                                                                                                   |
| --- | -------------------------------------------------------------------------------------------------------------------------- |
| E1  | Veículo abaixo dos estratos I3/I4 (salvo [PDR-0002](pdr/PDR-0002-emenda-de-estratos-ciclo-2.md), com ressalva obrigatória) |
| E2  | Abordagem não-agêntica                                                                                                     |
| E3  | Fora do domínio                                                                                                            |
| E4  | Duplicata (interna ou entre bases/ciclos)                                                                                  |
| E5  | Material não revisado por pares                                                                                            |

## Regras ratificadas

- **R1 — secundários não-agênticos** ([PDR-0003](pdr/PDR-0003-r1-secundarios-nao-agenticos.md)):
  excluídos do corpus primário independentemente de qualidade; secundários
  centrados em Agentic AI mantidos como _fundacionais-condicionais_ (P24, P33,
  P52, P54, P72, P77, P79 — migram para background se o protocolo se
  restringir a primários; corpus primário: 46).
- **R2 — colocação normativa de emendas** ([PDR-0004](pdr/PDR-0004-r2-emendas-no-texto-normativo.md)):
  emendas só vinculam no texto normativo da Etapa 1 dos prompts
  (Constituição, Art. II).
- **R3 — fronteira de domínio** ([PDR-0005](pdr/PDR-0005-r3-corte-de-dominio-e-cluster-humano.md)):
  corte estrito; o cluster de fatores humanos (P62, P63, P69, P81) entra
  exclusivamente como evidência complementar do outcome COGNITIVE_LOAD e
  nunca alimenta RQ1/RQ2/RQ4; estudo do cluster sem nenhuma aderência às RQs
  permanece excluído.
