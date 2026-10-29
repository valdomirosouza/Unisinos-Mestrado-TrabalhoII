# Artigo — RSL "Agentic AI as a Copilot to Reduce MTTD and MTTR During Incident Response"

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](../reviews/DASHBOARD.md) · [📄 Síntese consolidada](../reviews/relatorio-sintese-consolidado.md)

**Draft v2 (2026-10-30)** do artigo da RSL para submissão à **IEEE Access**, em inglês, no formato IEEE — incorpora o **ciclo 3 completo**: corpus 53 → **65** (126 candidatos, 74 avaliações por avaliador), PRISMA de 3 colunas (+ "reports not retrieved", PDR-0008), regra de estrato de proceedings (PDR-0006/0007), o **primeiro cluster de primários com MTTD/MTTR/MTTC nominal vs. baseline executado** (P100/P101/P102/P123 — reescreve o resultado central §IV-C, o abstract e a conclusão: de "unverified" para "supported by early, low-stratum evidence"), figura de cobertura de RQs com 4 conjuntos, confiabilidade atualizada (n=74: acordo 91,9–93,2%, κ 0,58–0,62, Fleiss 0,60, ciclo 3 unânime 13/13 = verificação empírica das regras R1–R3) e +12 referências (P91–P123, bib com 68 estudos + 6 metodológicas). O draft v1 permanece no histórico git (commit `da6c3f7` e anteriores). **Fig. 2 (rede de citações) estendida ao ciclo 3** em 2026-10-30: 65 arestas, 50 nós, estilo tracejado para o ciclo 3 — dados em [`../citacoes-cruzadas-P01-P123.md`](../citacoes-cruzadas-P01-P123.md). **Seção Nomenclature** adicionada após o abstract (2026-10-30): 30 siglas do domínio e do método (HITL/HOTL, MTTD/MTTR, SRE/NOC/SOC, PICOC/PRISMA/DARE etc.).

> Compilado em 2026-10-30 (TinyTeX): **11 páginas**, 0 citações não resolvidas, 2 overfull boxes pré-existentes do template (par benigno do `\maketitle`, presente também no v1).

## Arquivos

- [`main.tex`](main.tex) — o artigo, agora na **classe oficial `ieeeaccess.cls`** (template IEEE Access de 2026-05-13, baixado de ieeeaccess.ieee.org); a pasta inclui a classe, `spotcolor.sty`, as fontes proprietárias (Formata/Giovanni/Times, .pfb/.tfm/.map/.fd) e os logos exigidos pelo template.
  - **Workaround documentado no fonte:** a `ieeeaccess.cls` redefine o primitivo TeX `\year` como macro, o que quebra o seed do RNG do pgf no load ("Missing number" em cascata); o `main.tex` restaura o primitivo via `\pdfprimitive` ao redor do `\usepackage{tikz}` e devolve a macro da classe em seguida.
  - **Aviso benigno conhecido:** com tikz carregado, a classe emite ~22 `Overfull \hbox ... while \output is active` (2 por página) — artefato do hook de shipout do pgf medindo as caixas de cabeçalho de largura total do template; ocorre igualmente no sample oficial + tikz e não afeta o layout.
- [`referencias.bib`](referencias.bib) — 62 estudos do corpus/hubs (gerado de [`../Papers_Index.csv`](../Papers_Index.csv), com autores faltantes completados via Crossref) + 6 referências metodológicas (Kitchenham 2009, PRISMA 2020, Petticrew & Roberts, DARE, Cohen, Fleiss).

## Como compilar

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

(Compilado e validado em 2026-10-27 com **TinyTeX** — `~/Library/TinyTeX/bin/universal-darwin/` nesta máquina — + pacote `ieeetran` via tlmgr: **[`main.pdf`](main.pdf), 9 páginas (layout oficial da Access) (Fig. 1 PRISMA + Fig. 2 rede de citações + Fig. 3 cobertura de RQs, todas em TikZ; Tabela IV toolbox de carga cognitiva; §V-B eixos de lacunas)**, 0 citações não resolvidas, 0 overfull boxes, 0 avisos de BibTeX; 48 chaves de citação resolvidas.)

## Estrutura e proveniência do conteúdo

| Seção                                                                            | Fonte no repositório                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I. Introduction / II. Background                                                 | Síntese consolidada; hubs das [citações cruzadas](../citacoes-cruzadas-P01-P89.md)                                                                                                                                                                       |
| III. Method (PICOC, RQs, string, critérios, PRISMA, QA, 3 avaliadores)           | [`picoc/`](../picoc/), [`picoc-search-string.md`](../picoc/picoc-search-string.md), [`reviews/PRISMA.md`](../reviews/PRISMA.md), [`triagem-ciclo2.md`](../reviews/triagem-ciclo2.md), [template de avaliação](../prompts/prompt-chatgpt-consultation.md) |
| IV. Results (taxonomia, RQ/QA, MTTD/MTTR, carga cognitiva, citações cruzadas, κ) | CSVs consolidados em [`reviews/`](../reviews/), [fichas de extração](../report/README.md), [comparação global](../reviews/comparacao-avaliadores-global.md)                                                                                              |
| V–VII. Discussion, Threats, Conclusion                                           | [Síntese consolidada + adendos](../reviews/relatorio-sintese-consolidado.md)                                                                                                                                                                             |

## Pendências para a submissão (TODO)

1. ~~Trocar `IEEEtran` pela `ieeeaccess.cls` oficial~~ (feito, 2026-10-27). ~~Biografias dos autores~~ (feitas, 2026-10-27, em `IEEEbiographynophoto` — a do autor redigida a partir de [`../bio/ValdomiroSouza.pdf`](../bio/ValdomiroSouza.pdf), a do orientador a partir do perfil público acadêmico). Restam as **fotos** dos autores (trocar para `IEEEbiography` com `\includegraphics` quando houver fotos).
2. ~~Adicionar o orientador como coautor~~ (feito, 2026-10-27: Prof. Dr. Rafael Kunst, PPGCA/Unisinos, mesma afiliação `\address[1]`; e-mails do autor correspondente valdomirojr@gmail.com e valdomiro.souza@gmail.com; running head "Souza Jr. and Kunst").
3. ~~Diagrama PRISMA~~, ~~rede de citações~~ e ~~gráfico de RQ coverage~~ (feitos: Figs. 1–3 em TikZ, 2026-10-26).
4. ~~Decidir as 3 regras de protocolo~~ (feito: §III-E "Ratified protocol rules R1–R3", 2026-10-26 — secundários não-agênticos excluídos do corpus primário; emendas no texto normativo da Etapa 1; corte de domínio estrito com cluster humano restrito ao outcome de carga cognitiva).
5. ~~Revisão de inglês~~ (feita, 2026-10-27: gramática/idiomaticidade, ortografia americana, "Acknowledgment" no singular, e correção da banda do κ — _moderate_, não _substantial_, para κ 0.51–0.57). ~~Verificação final das contagens contra os CSVs~~ (feita, 2026-10-27: ~40 números recomputados dos CSVs canônicos — PRISMA, corpus 53/46, κ/Fleiss/prevalência, médias por conjunto, cobertura de RQs, 52 arestas, bib 62+6; 3 correções aplicadas: média QA do ciclo 2 **2,73** — 2,75 era a mediana, errata no DASHBOARD e na síntese —, faixa "QA 3.5–4.0 of 4.0" no núcleo empírico e composição explícita do n=61 no método).
