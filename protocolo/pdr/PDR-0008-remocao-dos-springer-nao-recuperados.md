# PDR-0008 — Remoção dos capítulos Springer não recuperados (reports not retrieved)

- **Status:** ratificado
- **Data:** 2026-10-29
- **Condutor:** Valdomiro de Oliveira Souza Jr.
- **Artigos da constituição afetados:** Art. I (fluxo PRISMA — categoria "reports not retrieved")

## Contexto

Cinco capítulos Springer do ciclo 3 (**P92, P95, P109, P122, P126** — volumes
CCIS/LNCS/LNNS de 2026) tiveram a triagem adiada na Etapa 4 por texto
integral não obtido. Segunda tentativa de recuperação executada em
2026-10-29 via Claude in Chrome sobre a sessão autenticada do proxy CAPES
(`ez101.periodicos.capes.gov.br`), pelo fluxo validado no ciclo 3
(`doi-org.<proxy>/<doi>` → `link-springer-com.<proxy>/chapter/<doi>` →
fetch de `/content/pdf/<doi>.pdf` com validação do magic `%PDF-`): os cinco
retornaram **HTTP 204 vazio** no endpoint de PDF e página com "Log in via an
institution" — a assinatura CAPES/Unisinos **não cobre esses volumes**. A
rota alternativa (biblioteca/COMUT) foi descartada pelo condutor.

## Decisão

Candidato aprovado para leitura integral cujo texto não é obtido após as
tentativas documentadas de recuperação (proxy institucional; sem rota
adicional autorizada) é **removido da revisão como "reports not retrieved"
(PRISMA 2020)** — exclusão por indisponibilidade, não por mérito; sem adendo
futuro previsto. Reentrada só por novo PDR, se o texto vier a ser obtido.

## Consequências

- P92, P95, P109, P122 e P126 passam de "triagem adiada (adendo futuro)" a
  **"excluído — texto integral não obtido (reports not retrieved)"** no
  `Papers_Index.csv` e no fluxo PRISMA do ciclo 3 (nota datada; diagramas de
  ciclos anteriores intocados).
- O funil do ciclo 3 fecha definitivo: 19 elegíveis → 5 not retrieved →
  14 triados → 13 avaliados → 12 incluídos. **Corpus consolidado permanece 65.**
- A rota de reavaliação do P90 pela cadeia de citação P92→P90
  (`research/snowballing-ciclo3.md`) **encerra-se** com a remoção do P92.
- Nenhum texto normativo de prompt muda (decisão de fluxo, não de avaliação).

## Aplicação

- [x] Índice de PDRs atualizado
- [x] `Papers_Index.csv` + MD derivado (5 statuses)
- [x] Nota datada no PRISMA do ciclo 3 e no artefato de triagem
- [x] DASHBOARD e síntese consolidada (adendo)
