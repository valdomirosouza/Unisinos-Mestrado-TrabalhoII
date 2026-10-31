# Versões dos LLMs avaliadores por ciclo (insumo da Seção III-I do artigo)

> 🧭 [🏠 README raiz](../README.md) · [📊 Dashboard](DASHBOARD.md) · [📄 Artigo](../artigo/README.md)

Levantamento de **2026-10-31** para responder ao item C10 do parecer PPGCA
("versões dos LLMs: modelo exato, datas, temperatura e modo de entrada do
PDF"). As células do avaliador Claude vêm de registros verificáveis
(trailers `Co-Authored-By` dos commits, transcripts de sessão do Claude
Code e datas de criação dos pareceres no git); as do ChatGPT vêm de
informação do condutor (2026-10-31); as do Gemini estão **pendentes de
verificação no histórico do app** pelo condutor.

## Tabela por ciclo

| Conjunto de pareceres                   | Datas (git) | Claude (avaliador A)                                   | ChatGPT (avaliador B)                          | Gemini (avaliador C) |
| --------------------------------------- | ----------- | ------------------------------------------------------ | ---------------------------------------------- | -------------------- |
| Ciclo 1 — P20–P40 (20)                  | 2026-06-28  | **Claude Opus 4.8 (1M context)**, via Claude Code      | **GPT-5.4** (app ChatGPT)                      | `[verificar no app]` |
| Ciclo 2 — P43–P88 (22)                  | 2026-09-10  | **Claude Fable 5** (`claude-fable-5`), via Claude Code | `[verificar: GPT-5.4 ou posterior — set/2026]` | `[verificar no app]` |
| Fundacionais — P01–P19 (19, retroativa) | 2026-10-26  | **Claude Fable 5** (`claude-fable-5`), via Claude Code | **GPT-6.0** (app ChatGPT)                      | `[verificar no app]` |
| Ciclo 3 — P91–P123 (13)                 | 2026-10-28  | **Claude Fable 5** (`claude-fable-5`), via Claude Code | **GPT-6.0** (app ChatGPT)                      | `[verificar no app]` |

## Condições de execução (todas as células)

- **Claude:** interface Claude Code (CLI); PDF lido na íntegra como arquivo
  (ferramenta de leitura de PDF da sessão); configurações default da
  interface — temperatura não configurável pelo usuário.
- **ChatGPT e Gemini:** apps web/consumer, PDF enviado por upload de
  arquivo; configurações default — temperatura não configurável pelo
  usuário nessas interfaces.
- Prompts idênticos por estudo para os três avaliadores (prompt canônico;
  a partir do ciclo 3, gerado por `scripts/render-prompts.py`).

## Papéis fora da banca de avaliação (para transparência)

| Papel                                                                                        | Modelo                                                                                                            | Registro                                                           |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Copiloto de engenharia da pesquisa (scripts, κ, gráficos, LaTeX, consolidações)              | Claude Opus 4.8 (jun/2026) → Claude Fable 5 (23/07/2026 em diante; 8 chamadas pontuais de Fable 5.1 em ~set/2026) | trailers de commit + transcripts (4.531 chamadas `claude-fable-5`) |
| Revisor independente do draft (parecer PPGCA de 31/10/2026 → `SUGESTOES-mudancas-artigo.md`) | **Claude Opus 5.5** (`claude-opus-5-5`)                                                                           | transcript da sessão "Revisor" (122 chamadas)                      |

## Leitura metodológica

A troca de versão do avaliador Claude entre os ciclos (Opus 4.8 → Fable 5)
e do ChatGPT (GPT-5.4 → GPT-6.0) **não degradou a concordância**: o ciclo 3,
já nas versões novas, saiu unânime (13/13, κ = 1,00). Isso sustenta a
limitação a declarar no artigo — as avaliações atravessam atualizações de
modelo — e, ao mesmo tempo, o argumento de robustez: o resultado não
depende de um build específico, e sim do protocolo escrito.

## Nota histórica

As menções a "Claude Sonnet 3.5" (P20) e "GPT-5/Claude-Opus class" (P100)
nos pareceres e fichas são conteúdo dos papers avaliados, não versões dos
avaliadores desta revisão.

---

_Para o artigo: quando as células do Gemini forem confirmadas, esta tabela
vira a tabela da Seção III-I (mapeamento A/B/C → modelos) e a limitação
entra em Threats to Validity._
