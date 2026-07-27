# Bookmarks — Recursos Externos da RSL

Links de referência usados na verificação bibliométrica, recuperação de metadados, extração de referências e condução da RSL.

## Classificação de veículos

- **QUALIS** — <https://qualis.pages.dev/> — consulta ao estrato Qualis (CAPES 2025–2028) por veículo/ISSN; fonte usada na verificação dos estratos registrados em [`papers.csv`](papers.csv).
- **SCImago Journal & Country Rank** — <https://www.scimagojr.com/> — consulta ao quartil SJR por periódico, ano e categoria; fonte usada na verificação dos quartis registrados em [`papers.csv`](papers.csv).

## Acesso a bases e textos completos

- **Portal de Periódicos da CAPES** — <https://www.periodicos.capes.gov.br/> — acesso às bases assinadas (Scopus, Web of Science, IEEE Xplore, ScienceDirect etc.) e aos textos completos dos artigos; acesso via **login CAFe** integrado à base de usuários da **Unisinos**.

## APIs de busca, validação e bibliometria

- **OpenAlex API** — <https://api.openalex.org/> (docs: <https://docs.openalex.org/>) — aberta, sem chave; usada na validação externa da [string de busca](picoc/picoc-search-string.md), resolução por DOI, contagem de citações (`cited_by_count`) e extração de referências (`referenced_works`) em [`DOIS.py`](DOIS.py).
- **Crossref REST API** — <https://api.crossref.org/> (docs: <https://api.crossref.org/swagger-ui/index.html>) — aberta, sem chave; usada na resolução de metadados, contagem de citações (`is-referenced-by-count`) de [`papers.csv`](papers.csv) e extração das referências depositadas pelos editores em [`DOIS.py`](DOIS.py).
- **Elsevier Developer Portal / Scopus APIs** — <https://dev.elsevier.com/> (Scopus Search API: `https://api.elsevier.com/content/search/scopus`) — requer chave de API com acesso institucional; usada na execução real da [string de busca no Scopus](picoc/picoc-search-string.md), consulta por DOI e contagem de citações (`citedby-count`) de [`papers.csv`](papers.csv). A chave nunca deve ser versionada. ⚠️ Usar `TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B)` por bloco; a forma aninhada apresentou falso-zero quando combinada com `DOI()`.
- **Semantic Scholar Graph API** — <https://api.semanticscholar.org/> (docs: <https://api.semanticscholar.org/api-docs/graph>) — usada por [`DOIS.py`](DOIS.py) para recuperar listas de referências e relacionar preprints, versões e identificadores externos. A chave é opcional, mas melhora limites de uso.
- **OpenCitations COCI API** — <https://opencitations.net/index/coci/api/v1> — usada por [`DOIS.py`](DOIS.py) como fonte complementar de relações DOI→DOI para referências e citações, preservando proveniência entre fontes.

## Regras de uso

- Manter contagens de citações separadas por fonte; não somar OpenAlex, Crossref e Scopus.
- Registrar `NÃO INDEXADO` como ausência de cobertura, não como zero.
- Preferir páginas do editor e índices primários para DOI canônico, versão do artigo, peer review, correções ou retratações.
- Nunca salvar chaves, tokens, credenciais institucionais ou URLs privadas no repositório.
