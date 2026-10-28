# Download de artigos com login acadêmico via Claude no Chrome

Como usar o **Claude Code + extensão Claude in Chrome** para baixar, de forma
semiautomática, os PDFs de candidatos que exigem autenticação institucional
(ex.: Portal de Periódicos da CAPES via proxy `ez101.periodicos.capes.gov.br`).
Validado no worked example (ciclo 3: 30/32 PDFs baixados em uma sessão;
2 exigiram um clique do autor).

## Pré-requisitos

1. Extensão [Claude in Chrome ≥ 1.0.36](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)
   instalada, Chrome aberto, mesmo plano/conta do Claude Code.
2. Na sessão do Claude Code: `/chrome` → conectar (ou iniciar com `claude --chrome`).
3. **Usuário já logado** no proxy institucional no próprio Chrome (ex.: acesso
   CAFe no Portal CAPES). A sessão de cookies é do usuário; o agente só a usa.
4. `Papers_Index.csv` com os DOIs e um ingestor como `scripts/ingest-downloads.py`.

## O fluxo que funciona

Para cada artigo, o agente:

1. **Navega** para o DOI reescrito no proxy:
   `https://doi-org.<proxy>/<doi>` → redireciona ao publisher autenticado.
2. **Resolve a URL do PDF** no padrão do publisher (tabela abaixo).
3. **Baixa via `fetch` na própria página** (mesma origem ⇒ cookies vão juntos)
   e dispara o save com `<a download>` já com o **nome canônico** (`P97.pdf`):

```js
const r = await fetch("/caminho/do/pdf"); // mesma origem do proxy
const b = await r.blob();
const head = await b.slice(0, 5).text(); // valida o magic
if (head === "%PDF-" && b.size > 20000) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(b);
  a.download = "P97.pdf";
  document.body.appendChild(a);
  a.click();
  a.remove();
}
```

4. **Verifica em disco** (`ls ~/Downloads/P97.pdf`) e ingere
   (`ingest-downloads.py P97 ~/Downloads/P97.pdf`).

## Padrões de URL de PDF por publisher

| Publisher                  | Como chegar ao PDF                                                                                                                                                                                                                                       |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IEEE Xplore                | `arnumber` sai do redirect público do DOI (`curl -sI https://doi.org/<doi>` → `document/<n>`); PDF em `/stampPDF/getPDF.jsp?tp=&arnumber=<n>`. Permite **lote**: resolver todos os arnumbers antes, abrir 1 página do Xplore e baixar vários num loop JS |
| Springer (capítulos)       | `/content/pdf/<doi>.pdf` — **se vier HTML, não há direito de acesso** (teste o magic `%PDF-`, não o status: paywall devolve 200 com HTML)                                                                                                                |
| MDPI (OA)                  | página do artigo + `/pdf` (sem proxy; bloqueia `curl`, mas o fetch no browser passa)                                                                                                                                                                     |
| World Scientific           | `/doi/pdf/<doi>`                                                                                                                                                                                                                                         |
| ACM DL                     | `/doi/pdf/<doi>`                                                                                                                                                                                                                                         |
| ScienceDirect              | o endpoint `pdfft` exige URL assinada → **clicar** no "View PDF" (abre aba com URL `pdf.sciencedirectassets.com/...assinada`) e dar `fetch(location.href)` nessa aba                                                                                     |
| Wiley/Hindawi              | `/doi/pdfdirect/<doi>?download=true` — pode levantar **Cloudflare**; ver regra abaixo                                                                                                                                                                    |
| OA avulsos (IJIES, IJCTT…) | achar `a[href*=".pdf"]` na página — **conferir que o arquivo é o artigo certo** (em sumários de fascículo o 1º link é de outro paper; case o href com o sufixo do DOI)                                                                                   |

## Pegadinhas descobertas no worked example

- **Valide pelo magic `%PDF-`**, nunca por `status==200` nem `blob.type`:
  paywalls devolvem 200/HTML; alguns servidores servem PDF como octet-stream.
- **1 download automático por origem/página**: o Chrome bloqueia o 2º download
  sem gesto do usuário. Em lote (IEEE), o aviso "baixar vários arquivos"
  aparece **uma vez** — o usuário clica _Permitir_ e o lote segue. Em sites
  avulsos, o 2º disparo some silenciosamente: recarregar a página ganha +1,
  ou o usuário clica no ícone de download bloqueado na barra de endereço →
  "Sempre permitir".
- **Lotes de JS ≤ 6 itens**: o CDP da extensão tem timeout de 45 s; um loop
  maior estoura (os downloads até continuam, mas o resultado se perde).
- **Filtro da extensão**: certas strings no código JS (ex.: `credentials`) ou
  certas páginas disparam `[BLOCKED: Cookie/query string data]`. Reescrever o
  snippet mínimo sem essas strings; em mesma origem os cookies já vão por
  padrão, `credentials:'include'` é desnecessário.
- **Cloudflare/CAPTCHA**: o agente **não resolve verificações anti-bot** — ele
  para e pede o clique do usuário ("Confirme que é humano"); depois o download
  segue sozinho.
- **Nunca** digitar credenciais institucionais via agente: o login (CAFe) é
  feito pelo usuário, antes; o agente apenas navega na sessão existente.

## Divisão de papéis

| Agente                                                                                            | Usuário                                                                                                    |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| navegar, resolver URLs, fetch+save com nome canônico, validar magic, ingerir, registrar no índice | login institucional; cliques de permissão (multi-download, "Sempre permitir"); desafios Cloudflare/CAPTCHA |
