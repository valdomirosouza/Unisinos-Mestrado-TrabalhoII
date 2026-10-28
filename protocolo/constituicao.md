# Constituição da Revisão — Agentic AI as a Copilot to Reduce MTTD and MTTR During Incident Response

> Raiz de autoridade do protocolo. Toda avaliação, triagem e síntese é conferida
> contra estes artigos. Mudanças exigem um PDR (`pdr/`) e incremento da versão.

**Versão:** 1.0.0 · **Ratificada em:** 2026-10-27 · **Condutor da revisão:** Valdomiro de Oliveira Souza Jr.

## Metodologia de referência

Kitchenham et al. (2009), _"Systematic literature reviews in software
engineering – A systematic literature review"_; seleção reportada em PRISMA 2020
(adaptado para update review quando houver corpus fundacional); escopo por PICOC
(Petticrew & Roberts); qualidade nos moldes DARE.

## Questões de pesquisa

- **RQ1 (Contexto/Definições):** quais capacidades e níveis de autonomia
  (planejamento, memória, uso de ferramentas, supervisão humana) caracterizam
  Agentic AI e como afetam a tomada de decisão em ambientes complexos?
- **RQ2 (Engenharia/Arquitetura):** quais arquiteturas e mecanismos
  (orquestração, memória, ferramentas, guardrails, observabilidade) sustentam
  Agentic AI em produção?
- **RQ3 (Evidência/Benefícios):** quais evidências quantitativas e
  qualitativas reportam benefícios, e com quais métricas (tempo de resposta,
  qualidade de decisão, carga operacional), especialmente em incident response?
- **RQ4 (Desafios/Ética):** quais riscos e desafios (segurança, robustez,
  governança, accountability) limitam o uso responsável em sistemas críticos?
- **RQ5 (Lacunas):** quais lacunas e direções futuras
  (avaliação/benchmarking, modelos de ameaça, governança, observabilidade,
  alinhamento) são identificadas?

## Artigos

### I. Escopo pelo PICOC (INEGOCIÁVEL)

A elegibilidade temática é julgada exclusivamente contra `protocolo/picoc.md`.
_Comparison_ só é registrado como declarado quando o estudo **executa uma
comparação empírica contra baseline concreto**; contrastes puramente conceituais
são "não se aplica".

### II. Emendas só no texto normativo

Uma emenda de protocolo (ex.: exceção de estrato de veículo) só vincula os
avaliadores quando escrita no **texto normativo dos prompts de avaliação**
(Etapa 1), nunca apenas nos metadados/insumos. Toda emenda nasce como PDR datado.

### III. Três avaliadores independentes

Toda avaliação integral é executada de forma independente por **três
avaliadores LLM** a partir do mesmo prompt e PDF. A decisão colapsada
(Incluir/Excluir) alimenta κ de Cohen por par e κ de Fleiss; divergências são
classificadas como _protocolares_ (viram PDR) ou _de mérito_ (reavaliação).

### IV. Pontuação padronizada

SCORE_RQ (RQ1–RQ5; T/P/N = 1.0/0.5/0.0; máx. 5.0) e SCORE_QA (QA1 objetivos
claros, QA2 metodologia replicável, QA3 base de evidência sólida, QA4 conclusões
coerentes; Y/P/N = 1.0/0.5/0.0; máx. 4.0; bandas Alta ≥ 3.0 · Média 1.5–2.5 ·
Baixa < 1.5).

### V. Bibliometria por fonte, nunca somada

Contagens de citações são mantidas **por fonte** (OpenAlex, Crossref, Scopus) e
jamais somadas; `NÃO INDEXADO` ≠ 0. Peculiaridades de cada fonte relevantes à
reprodutibilidade são documentadas na trilha de auditoria.

### VI. Artefatos históricos são imutáveis

Pareceres publicados, avaliações de terceiros e saídas de ciclos anteriores não
são reescritos. Correções entram como **errata datada** ou artefato novo com
nota de versão.

### VII. Todo número deriva de um CSV canônico

Nenhum número da síntese ou do artigo é digitado de memória: médias, κ,
contagens PRISMA e arestas de citação derivam dos CSVs canônicos e são
conferíveis por `scripts/check-rsl.sh` e `scripts/compute-kappa.py`.

### VIII. Segredos fora do repositório

Chaves de API vivem em arquivos ignorados pelo git (`.scopus_key`, `.env`) e
nunca transitam por chat ou log. Varredura de vazamento antes de todo commit que
envolveu credenciais.

### IX. Rastreabilidade total

Toda sessão de trabalho vira item numerado no log de memória do projeto
(prompt → ações → comandos → incidentes), commitado. Toda exclusão cita o
critério (E1–E5) ou o PDR que a fundamenta.

## Governança

- Emendas: PDR aprovado pelo condutor → texto normativo → incremento MINOR.
- Conflito entre artefato e constituição: a constituição prevalece; o artefato
  ganha errata.
