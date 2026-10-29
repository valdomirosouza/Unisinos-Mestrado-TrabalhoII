# Citações cruzadas — extensão ao ciclo 3 (P01–P123)

> 🧭 [🏠 README raiz](README.md) · [🕸️ Base P01–P89](citacoes-cruzadas-P01-P89.md) · [📄 Artigo (Fig. 2)](artigo/README.md)

Extensão da rede interna de citações para incluir os **12 incluídos do
ciclo 3**, computada em **2026-10-30** para a Fig. 2 do draft v2 do artigo.
A base P01–P89 (52 arestas, tripla checagem OpenAlex × Crossref × Scopus)
permanece como registro em [`citacoes-cruzadas-P01-P89.md`](citacoes-cruzadas-P01-P89.md).

## Método (ciclo 3)

União de duas fontes, estudos mais antigos não citam os novos:

1. **Varredura full-text** dos 12 PDFs do ciclo 3 (pypdf): match de título
   normalizado (≥25 caracteres alfanuméricos) ou DOI de qualquer estudo do
   `Papers_Index.csv` no texto das referências — 11 arestas.
2. **OpenAlex `referenced_works`** dos 12 (depósitos incompletos; P102,
   P112 e P121 com 0 referências depositadas) — 9 arestas, 2 delas não
   capturadas pela varredura de texto (P93→P76 e P97→P14, formatos de
   referência que a extração de texto não casou).

## As 13 arestas novas (A → B = "A cita B")

| Citador (ciclo 3) | Citado | Fonte                          |
| ----------------- | ------ | ------------------------------ |
| P93               | P06    | full-text + OA                 |
| P93               | P76    | só OA                          |
| P97               | P14    | só OA                          |
| P97               | P37    | full-text                      |
| P97               | P73    | full-text                      |
| P97               | P76    | full-text + OA                 |
| P97               | P79    | full-text + OA                 |
| P97               | P83    | full-text + OA                 |
| P97               | P121   | full-text + OA (intra-ciclo 3) |
| P101              | P121   | full-text (intra-ciclo 3)      |
| P112              | P05    | full-text                      |
| P121              | P14    | full-text                      |
| P121              | P44    | full-text (P44 entra na rede)  |

## Totais e mudanças estruturais (rede P01–P123, 65 arestas)

- **Hubs (≥3 citações recebidas):** P10 (7) · **P14 (7, era 5 — sobe ao
  nível do P10)** · P09 (6) · P16 (3) · P65 (3) · **P76 (3 — novo hub:**
  P28, P93 e P97 o citam**)**.
- **Maiores citadores (7 arestas de saída):** P15, P28 e **P97 (novo)** —
  o SOC-as-a-Service do ciclo 3 cita 7 estudos do corpus, incluindo o
  survey intra-ciclo P121.
- Nós na rede: 50 (41 da base + P44, P93, P97, P101, P112, P121); os demais
  incluídos do ciclo 3 (P91, P94, P100, P102, P110, P119, P123) não têm
  aresta interna detectada.
- Leitura: cada ciclo segue citando para dentro do corpus
  (P79→P20/P78; P76→P39/P83; P93→P06/P76) — uma conversa de pesquisa em
  evolução, não amostras disjuntas.

---

_Computado em 2026-10-30 (varredura pypdf sobre `docs/` + OpenAlex). Nota:
a extração de texto de PDF pode perder referências (duas arestas vieram só
da OpenAlex); os números são, portanto, um limite inferior._
