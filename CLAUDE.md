# Instruções do Projeto — RSL Agentic AI Copilot (PPGCA · Unisinos)

## REGRA OBRIGATÓRIA — Dump de memória de sessão em MEMORY.md

Toda sessão de trabalho assistida neste repositório DEVE registrar sua memória
completa em **`MEMORY.md` (raiz do projeto)**, preservando o histórico de
conversas, iterações e respostas. Esta regra não é opcional.

### O que registrar (por item de trabalho)

Cada unidade de trabalho vira um **item numerado** (sequência contínua entre
sessões — verificar o último número usado antes de acrescentar), contendo:

1. **Prompt do usuário** — citação literal ou resumo fiel do pedido.
2. **Contexto** — o que motivou o pedido, quando não for óbvio.
3. **Ações/Respostas** — o que foi feito e respondido, incluindo achados,
   números-chave, decisões tomadas e arquivos criados/alterados.
4. **Comandos e ferramentas executados** — scripts, APIs chamadas, validações
   (com resultados relevantes: recall, contagens, κ etc.).
5. **Incidentes e recuperações** — limites de sessão, conflitos de rebase,
   bugs de API descobertos, e como foram resolvidos.

### Quando registrar

- **Incrementalmente**, ao concluir cada unidade de trabalho relevante — não
  apenas no fim da sessão (sessões podem ser interrompidas).
- **Sempre antes de encerrar a sessão**, garantindo que nada ficou de fora.
- Quando o usuário pedir ("Atualize o MEMORY.md"), registrar e **commitar +
  push** imediatamente.

### Formato (seguir o padrão já existente no MEMORY.md)

- **Nova sessão** = novo bloco `# Sessão AAAA-MM-DD → AAAA-MM-DD — <tema>`,
  com as subseções:
  - `## Linha do tempo (prompts → respostas/ações)` — itens numerados
    `### NN. <título curto>` com `**Prompt:**` e `**Ações:**`;
  - `## Decisões e convenções da sessão` — regras/convenções que valem para o
    futuro (nomenclatura, protocolos, políticas);
  - `## Artefatos produzidos` — arquivos novos/alterados, por pasta;
  - `## Histórico de commits da sessão` — tabela `| Hash | Data | Mensagem |`,
    incluindo commits externos (PRs do usuário) marcados como tal, encerrada
    com a nota de que o commit do próprio MEMORY.md é acrescentado ao final.
- **Sessão continuada** = acrescentar itens ao bloco corrente e estender o
  intervalo de datas do cabeçalho.

### Regras de fidelidade

- O MEMORY.md é **registro histórico**: nunca reescrever itens passados —
  correções entram como itens novos referenciando o item corrigido.
- Registrar fielmente falhas e retrabalho (não só sucessos).
- Nunca registrar segredos (chaves de API, tokens, credenciais) — referir-se a
  eles apenas como "chave mantida fora do repositório".
- Após atualizar o MEMORY.md, **commitar e fazer push** (mensagem padrão:
  `Log <tema> (item NN) in MEMORY.md`).

## Convenções gerais do repositório

- Documentação em pt-BR; termos técnicos e acrônimos (MTTD, MTTR, Agentic AI,
  LLM, AIOps, PICOC, PRISMA…) permanecem em inglês.
- Todo arquivo novo em `docs/`, `prompts/`, `report/`, `reviews/`, `picoc/` e
  `research/` deve ser indexado na documentação (README raiz e README da
  pasta); verificar links relativos antes de commitar.
- Artefatos históricos (relatório de síntese publicado, avaliações de
  terceiros, saídas de ciclos anteriores) não são reescritos — atualizações
  viram artefatos novos ou seções novas com nota de versão.
- Contagens de citações são sempre por fonte (OpenAlex/Crossref/Scopus),
  nunca somadas; `NÃO INDEXADO` ≠ 0.
- Chaves de API nunca são versionadas; rodar varredura de vazamento antes de
  commits que envolveram credenciais.
