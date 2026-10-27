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

(Compilado e validado em 2026-10-26 com **TinyTeX** — `~/Library/TinyTeX/bin/universal-darwin/` nesta máquina — + pacote `ieeetran` via tlmgr: **[`main.pdf`](main.pdf), 8 páginas (Fig. 1 PRISMA + Fig. 2 rede de citações + Fig. 3 cobertura de RQs, todas em TikZ; Tabela IV toolbox de carga cognitiva; §V-B eixos de lacunas)**, 0 citações não resolvidas, 0 overfull boxes, 0 avisos de BibTeX; 48 chaves de citação resolvidas.)

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
3. ~~Diagrama PRISMA~~, ~~rede de citações~~ e ~~gráfico de RQ coverage~~ (feitos: Figs. 1–3 em TikZ, 2026-10-26).
4. Decidir as 3 regras de protocolo em aberto (famílias A–C da comparação global) e registrar no texto.
5. Revisão de inglês e verificação final das contagens contra os CSVs.
