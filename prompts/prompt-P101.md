# Prompt de avaliação integral — P101


## PAPEL

Aja como pesquisador em Computação Aplicada do PPGCA da Unisinos orientado por um professor Doutor em Ciência da Computação, especialista em Revisão Sistemática da Literatura (RSL) em Engenharia de Software, conduzindo uma RSL seguindo as diretrizes de Kitchenham (2009) no paper
"Systematic literature reviews in software engineering – A systematic
literature review".

## TEXTO NORMATIVO (vincula o veredito — Constituição Art. II)

1. Julgue a elegibilidade temática exclusivamente contra o PICOC abaixo.
2. _Comparison_ declarado **somente** com comparação empírica executada contra
   baseline concreto.
3. Emendas vigentes (texto de cada PDR ratificado, via `--emendas`):
   PDR-0006 — o estrato de um conference paper é derivado do percentil CiteScore (Scopus) da série de proceedings em que foi publicado, pela mesma régua percentil→Qualis dos journals; evento cuja série não possui CiteScore é INELEGÍVEL na Etapa 1. PDR-0007 (renova o PDR-0002 para o ciclo 3) — candidatos com estrato aferido fora de A1–A2, e journals sem indexação de estrato, são avaliados com RESSALVA DE ESTRATO OBRIGATÓRIA em todo uso da evidência; a ressalva deve constar explicitamente na recomendação final do parecer.
4. Pontue RQ1–RQ5 (T/P/N = 1.0/0.5/0.0) e QA1–QA4 (Y/P/N = 1.0/0.5/0.0);
   bandas Alta ≥ 3.0 · Média 1.5–2.5 · Baixa < 1.5.

## INSUMOS

- **Estudo:** P101 — Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration (2026, Proceedings of the International Symposium on Digital Forensics and Security Isdfs, DOI 10.1109/isdfs69419.2026.11458922)
- **Bibliometria (por fonte, nunca somar):** OpenAlex 1 (verif. OA/CR/Scopus 2026-10-27) · Crossref
  1 (verif. OA/CR/Scopus 2026-10-27) · Scopus 0 (verif. OA/CR/Scopus 2026-10-27) · Qualis B4 (percentil 11% da série ISDFS — PDR-0006) · SJR N/D (estrato aferido pelo percentil Scopus — PDR-0006/0007)
- **Ressalvas da triagem:** RESSALVA DE ESTRATO OBRIGATÓRIA (série ISDFS B4; PDR-0006/0007). Flags da triagem: Comparison executado vs. polling e vs. LLM-Assist; testbed enterprise simulado (FortiSIEM/FortiSOAR).
- **PDF:** P101_Event_Driven_Agentic_SOC_ED_ASOC_Supervisor_Based_LLM_Framework_for_Dynamic_Inci.pdf

## QUESTÕES DE PESQUISA

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

## TAREFA

1. Leia o PDF na íntegra.
2. Preencha: Tabela A (identificação e PICOC do estudo), Tabela B (RQ1–RQ5 com
   evidência âncora seção/página), Tabela C (QA1–QA4 com justificativa).
3. Emita o parecer no formato de `templates/review.md`, terminando com a
   recomendação: `Incluir` | `Incluir c/ ressalvas (motivo)` | `Excluir
(critério ou PDR)`.

