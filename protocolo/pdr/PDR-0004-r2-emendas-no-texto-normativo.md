# PDR-0004 — R2: emendas só vinculam no texto normativo da Etapa 1

- **Status:** ratificado em 2026-10-26 (registro retroativo em 2026-10-27)
- **Condutor:** Valdomiro de Oliveira Souza Jr.
- **Artigos da constituição afetados:** Art. II (é a origem do artigo)

## Contexto

Família B das divergências globais (P62, P69, P81): a emenda de estratos
([PDR-0002](PDR-0002-emenda-de-estratos-ciclo-2.md)) estava escrita nos
insumos dos prompts, não no texto normativo. O avaliador que aplicou o
critério estrito (ChatGPT) leu a emenda como advisória e excluiu os três
estudos na triagem — 3 das 8 divergências residuais.

## Decisão

Emendas de elegibilidade **só vinculam quando escritas no texto normativo da
Etapa 1** do protocolo de avaliação, nunca apenas nos metadados/insumos. A
emenda de estratos do ciclo 2 é ratificada sob esta regra: os quatro
candidatos sub-estrato mantêm suas avaliações integrais com ressalva
obrigatória.

## Consequências

- Virou o Art. II da constituição e o campo `{{EMENDAS_NORMATIVAS}}` do
  template canônico de prompt (preenchido pelo `scripts/render-prompts.py`).
- Formalizada no artigo IEEE Access, §III-E (regra R2) e na lição metodológica
  de §V-E.
