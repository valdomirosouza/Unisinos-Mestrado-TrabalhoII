# PICOC Extraction Prompt — Agentic AI Copilot SLR

**Versão:** v1.0.0
**Escopo:** Extração PICOC de todos os estudos da pasta `docs/` para a RSL
"Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura".
**Metodologia de referência:** Kitchenham & Charters (guia de RSL em Engenharia
de Software); PICOC conforme Petticrew & Roberts.
**Uso recomendado:** processar a pasta inteira em uma execução; se o volume de
PDFs degradar a fidelidade, dividir em lotes e concatenar as tabelas.

---

## PROMPT (copiar a partir daqui)

```text
# PAPEL
Aja como Professor Doutor em Computação Aplicada do PPGCA da Unisinos,
especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de
Software, seguindo as diretrizes de Kitchenham & Charters. Você domina o
framework PICOC (Population, Intervention, Comparison, Outcomes, Context) como
instrumento para delimitar escopo e derivar termos de busca.

# CONTEXTO DA RSL
Esta extração integra o artigo "Agentic AI Copilot para Resposta a Incidentes:
Uma Revisão da Literatura". O tema investiga como a Agentic AI atua como
copiloto ou agente autônomo na resposta a incidentes, com foco em redução de
MTTD/MTTR, observabilidade e carga cognitiva de equipes (SRE, NOC, Suporte).

# TAREFA
1. Leia TODOS os artigos (PDFs) presentes na pasta `docs/`.
2. Para CADA artigo, raciocine explicitamente antes de classificar (ver
   ETAPA DE RACIOCÍNIO).
3. Ao final, consolide os resultados em UMA tabela PICOC (ver SAÍDA).

# REGRAS INVIOLÁVEIS (ANTIFABRICAÇÃO)
1. Extraia EXCLUSIVAMENTE o conteúdo presente em cada PDF. Não use
   conhecimento externo nem suponha o que o artigo "provavelmente" contém.
2. Não invente dados. Se um elemento PICOC não estiver presente no artigo,
   registre "NÃO DECLARADO" — nunca preencha por inferência.
3. Toda célula preenchida deve ser ancorável a evidência do texto (seção,
   figura, tabela ou página).
4. O elemento "Comparison" frequentemente não se aplica a estudos que mapeiam
   o estado da arte. Nesse caso registre "N/A (estudo de mapeamento)" em vez
   de forçar uma comparação inexistente.

# DEFINIÇÃO DOS ELEMENTOS PICOC (âncoras para este domínio)
- Population: o que/quem é objeto do estudo — ex.: sistemas complexos de
  software, ambientes SRE/NOC, microsserviços, pipelines de operação de TI.
- Intervention: a solução agêntica investigada — ex.: Agentic AI como copiloto
  ou agente autônomo; loop PRAL (perceber, raciocinar, agir, aprender);
  sistemas multiagentes; LLM4AIOps.
- Comparison: a alternativa contrastada — ex.: automação tradicional, AIOps
  não-agêntico, baseline humano; ou "N/A" se ausente.
- Outcomes: efeitos/métricas reportados — ex.: MTTD/MTTR, observabilidade,
  carga cognitiva, acurácia de detecção, autonomia sob governança.
- Context: cenário/domínio — ex.: ciclo de vida de resposta a incidentes,
  cibersegurança, modo HITL/HOTL, produção vs. simulação.

# ETAPA DE RACIOCÍNIO (por artigo, antes da tabela)
Para cada artigo produza um bloco curto:
- ID e título.
- 3–5 linhas explicando como você identificou cada elemento PICOC no texto,
  citando a evidência (seção/página).
- Quais elementos ficaram "NÃO DECLARADO" ou "N/A" e por quê.

# SAÍDA — Tabela PICOC consolidada
Uma linha por artigo, todas as colunas abaixo:

| ID | Artigo | Population | Intervention | Comparison | Outcomes | Context | Evidência (seção/pág.) |

Após a tabela, inclua:
- Síntese transversal (5–8 linhas): padrões recorrentes de Population,
  Intervention e Context no conjunto; lacunas de Comparison e Outcomes.
- Observações metodológicas: artigos com PICOC incompleto e implicação para o
  escopo da RSL.
```

---

## Notas de uso

- **Raciocínio antes da tabela.** A etapa de raciocínio por artigo não é
  enfeite: ela torna cada célula auditável e reduz preenchimento por inferência.
  Em banca, é o que sustenta "por que este artigo entra e como ele responde ao
  escopo".
- **"Comparison" costuma ser N/A** em revisões de mapeamento — o que é aceito
  na literatura. Forçar comparação inexistente é pior que registrar a ausência.
- **`NÃO DECLARADO` é intencional.** Mantém honesta a extração e sinaliza onde o
  artigo é silencioso, alimentando a discussão de lacunas (RQ5).
- **Derivação de busca.** A síntese transversal de Intervention + Context é o
  argumento auditável para a string de busca da RSL (por que estes termos e não
  outros).

## Changelog

- **v1.0.0** — Versão inicial. Leitura em lote da pasta `docs/`, raciocínio
  explícito por artigo, tabela PICOC consolidada com âncoras de evidência,
  guarda antifabricação (`NÃO DECLARADO` / `N/A`) e síntese transversal.
