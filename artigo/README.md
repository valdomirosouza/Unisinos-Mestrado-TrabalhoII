# Artigo — RSL "Agentic AI as a Copilot to Reduce MTTD and MTTR During Incident Response"

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](../reviews/DASHBOARD.md) · [📄 Síntese consolidada](../reviews/relatorio-sintese-consolidado.md)

**Primeira versão (draft v1, 2026-10-26)** do artigo da RSL para submissão à **IEEE Access**, em inglês, no formato IEEE.

## Arquivos

- [`main.tex`](main.tex) — o artigo (classe `IEEEtran` em modo journal; **para a submissão final, trocar pela classe oficial `ieeeaccess.cls` do template da IEEE Access** — o conteúdo é compatível).
- [`referencias.bib`](referencias.bib) — 62 estudos do corpus/hubs (gerado de [`../Papers_Index.csv`](../Papers_Index.csv), com autores faltantes completados via Crossref) + 6 referências metodológicas (Kitchenham 2009, PRISMA 2020, Petticrew & Roberts, DARE, Cohen, Fleiss).

## Como compilar

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

(Requer uma distribuição LaTeX com `IEEEtran` — TeX Live/MacTeX. Não há LaTeX instalado nesta máquina; o draft foi validado estruturalmente: 48 chaves de citação, todas presentes no `.bib`.)

## Estrutura e proveniência do conteúdo

| Seção                                                                            | Fonte no repositório                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I. Introduction / II. Background                                                 | Síntese consolidada; hubs das [citações cruzadas](../citacoes-cruzadas-P01-P89.md)                                                                                                                                                                       |
| III. Method (PICOC, RQs, string, critérios, PRISMA, QA, 3 avaliadores)           | [`picoc/`](../picoc/), [`picoc-search-string.md`](../picoc/picoc-search-string.md), [`reviews/PRISMA.md`](../reviews/PRISMA.md), [`triagem-ciclo2.md`](../reviews/triagem-ciclo2.md), [template de avaliação](../prompts/prompt-chatgpt-consultation.md) |
| IV. Results (taxonomia, RQ/QA, MTTD/MTTR, carga cognitiva, citações cruzadas, κ) | CSVs consolidados em [`reviews/`](../reviews/), [fichas de extração](../report/README.md), [comparação global](../reviews/comparacao-avaliadores-global.md)                                                                                              |
| V–VII. Discussion, Threats, Conclusion                                           | [Síntese consolidada + adendos](../reviews/relatorio-sintese-consolidado.md)                                                                                                                                                                             |

## Pendências para a submissão (TODO)

1. Trocar `IEEEtran` pelo template oficial da IEEE Access (`ieeeaccess.cls`) e adicionar biografia/foto do autor.
2. Adicionar o orientador como coautor (placeholder marcado no `.tex`).
3. Figuras: diagrama PRISMA (adaptar o Mermaid de `reviews/PRISMA.md` para TikZ/PNG) e 1–2 gráficos (RQ coverage; recomendações) a partir dos SVGs de `reviews/charts*/`.
4. Decidir as 3 regras de protocolo em aberto (famílias A–C da comparação global) e registrar no texto.
5. Revisão de inglês e verificação final das contagens contra os CSVs.
