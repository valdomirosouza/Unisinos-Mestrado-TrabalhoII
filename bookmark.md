# Bookmarks — Recursos Externos da RSL

Links de referência usados na verificação bibliométrica e na condução da RSL.

## Classificação de veículos

- **QUALIS** — <https://qualis.pages.dev/> — consulta ao estrato Qualis (CAPES 2025-2028) por veículo/ISSN; fonte usada na verificação dos estratos registrados em [`papers.csv`](papers.csv).
- **SCImago Journal & Country Rank** — <https://www.scimagojr.com/> — consulta ao quartil SJR por periódico; fonte usada na verificação dos quartis registrados em [`papers.csv`](papers.csv).

## APIs (validações e bibliometria)

- **OpenAlex API** — <https://api.openalex.org/> (docs: <https://docs.openalex.org/>) — aberta, sem chave; usada na validação externa da [string de busca](picoc/picoc-search-string.md) (recall por DOI) e na contagem de citações (`cited_by_count`) de [`papers.csv`](papers.csv).
- **Crossref API** — <https://api.crossref.org/> (docs: <https://api.crossref.org/swagger-ui/index.html>) — aberta, sem chave; usada na contagem de citações (`is-referenced-by-count`) de [`papers.csv`](papers.csv). Também consultada pelo [`DOIS.py`](DOIS.py) para extração de referências.
- **Elsevier Developer Portal (Scopus APIs)** — <https://dev.elsevier.com/> (Scopus Search API: `https://api.elsevier.com/content/search/scopus`) — requer chave de API com acesso institucional; usada na execução real da [string de busca no Scopus](picoc/picoc-search-string.md) (recall 13/14, volume 12.783) e na contagem de citações (`citedby-count`) de [`papers.csv`](papers.csv). ⚠️ Sintaxe: usar `TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B)` por bloco — a forma aninhada falha silenciosamente combinada com `DOI()`.
