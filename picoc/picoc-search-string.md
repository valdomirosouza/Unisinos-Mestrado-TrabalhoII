# String de Busca da RSL — Derivada da Síntese PICOC

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [Prompt PICOC](picoc-extraction-prompt.md) · [Tabela PICOC](picoc-results-consolidated-P01-P40-Claude.md) · [Comparação de avaliadores](picoc-comparacao-avaliadores.md)

String de busca da RSL **"Agentic AI Copilot para Resposta a Incidentes"**, derivada de forma auditável da
**síntese transversal PICOC** dos 39 artigos do corpus ([tabela consolidada](picoc-results-consolidated-P01-P40-Claude.md))
e **calibrada empiricamente** contra os metadados do corpus conhecido ([`../export.csv`](../export.csv): título + abstract + keywords).

## 1. Derivação a partir do PICOC (auditável)

| Bloco                              | Elemento PICOC de origem | Evidência na síntese transversal                                                                                                                                                                                         |
| ---------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **A — Intervenção agêntica**       | Intervention             | Padrão dominante: sistemas multiagente baseados em LLM com orquestração e ferramentas (P20, P22, P23, P25, P27, P28, P31, P32, P35, P38); variantes SLM (P21) e copilots (P34); frameworks de Agentic AI nos secundários |
| **B — Contexto operacional**       | Context + Population     | Ciclo de resposta a incidentes (P22, P25, P28, P34, P37), AIOps/RCA cloud-native (P23, P26, P32, P35), redes/ICT (P21, P22, P40), SOC/cibersegurança (P14, P25, P28, P33, P34, P37)                                      |
| **C — Outcomes (NÃO obrigatório)** | Outcomes                 | **Nenhum estudo mede MTTD/MTTR nominalmente** — a calibração confirma: com o bloco C obrigatório, apenas **1/38** artigos do corpus seria recuperado. O bloco fica disponível só como refinamento opcional               |

## 2. String genérica (booleana)

```text
( "agentic AI" OR "AI agent*" OR "LLM agent*" OR "language model agent*"
  OR "multi-agent" OR multiagent OR "autonomous agent*" OR copilot*
  OR "large language model*" OR "small language model*" OR "intelligent agent*" )
AND
( "incident response" OR "incident management" OR AIOps OR "IT operations"
  OR "site reliability" OR SRE OR "security operations" OR SOC
  OR cybersecurity OR "cyber security" OR "cyber threat*"
  OR "root cause" OR "anomaly detection" OR observability
  OR microservice* OR "cloud-native" OR "network management"
  OR "network operations" OR DevOps OR remediation
  OR "threat detection" OR resilience OR vulnerabilit* )
```

**Bloco C opcional (refinamento, não obrigatório):**
`AND ( MTTD OR MTTR OR "mean time to detect*" OR "mean time to recover*" OR "alert fatigue" OR "cognitive load" OR "resolution time" )`

**Filtros do protocolo:** ano ≥ 2020 · idioma inglês · peer-reviewed (journal/conference).

## 3. Sintaxe por base

**Scopus** (forma validada na API em 2026-07-27 — usar `TITLE-ABS-KEY` **separado por bloco**; a forma aninhada `TITLE-ABS-KEY((A) AND (B))` apresentou falha silenciosa do parser quando combinada com outros campos, p.ex. `DOI()`):

```text
TITLE-ABS-KEY ( "agentic AI" OR "AI agent*" OR "LLM agent*" OR "language model agent*" OR "multi-agent" OR multiagent OR "autonomous agent*" OR copilot* OR "large language model*" OR "small language model*" OR "intelligent agent*" )
AND TITLE-ABS-KEY ( "incident response" OR "incident management" OR aiops OR "IT operations" OR "site reliability" OR sre OR "security operations" OR soc OR cybersecurity OR "cyber security" OR "cyber threat*" OR "root cause" OR "anomaly detection" OR observability OR microservice* OR "cloud-native" OR "network management" OR "network operations" OR devops OR remediation OR "threat detection" OR resilience OR vulnerabilit* )
AND PUBYEAR > 2019 AND LANGUAGE ( english )
```

**Web of Science:** mesma expressão com `TS=( bloco A ) AND TS=( bloco B )` e refinamento `PY=(2020-2026)`.

**IEEE Xplore:** usar a string genérica em "Command Search" com `("All Metadata": …)` por termo; wildcards `*` suportados.

**ACM DL:** usar a string genérica no campo "Title, Abstract, Keywords"; substituir wildcards por variantes explícitas (`copilot OR copilots`, `microservice OR microservices`).

## 4. Calibração contra o corpus (validação empírica)

**Método:** matching (substring, case-insensitive) dos blocos sobre título + abstract + keywords dos 38 artigos com metadados em [`../export.csv`](../export.csv) (P13 sem registro no export do Mendeley — não testável).

| Conjunto                          | Recuperados | Observação                                                                 |
| --------------------------------- | :---------: | -------------------------------------------------------------------------- |
| **Estudos incluídos na RSL (14)** |  **13/14**  | Única perda: P24 (ver trade-off abaixo)                                    |
| Candidatos P20–P40 testáveis (20) |    16/20    | Não recuperados: P24, P26, P38, P39                                        |
| Fundacionais P01–P19              |    7/18     | Esperado — entraram via Trabalho I (snowballing), não por busca de domínio |

- **P26, P38, P39 não recuperados = comportamento desejável:** são estudos **excluídos/inelegíveis** da RSL (P26 RCA não-agêntico; P38 fora de domínio/agricultura; P39 opinião Qualis A3). A string filtra na fonte o que a triagem descartaria.
- **Trade-off documentado (P24):** o survey AgentAI (Industry 4.0, fundacional condicional) só seria recuperado adicionando `"autonomous system*"` ao bloco B — termo que em bases de redes captura AS/BGP (_autonomous systems_) e degradaria fortemente a precisão. Mantido fora; P24 permanece no corpus pela rota de descoberta/triagem da Etapa 1.
- **Bloco C (Outcomes) como obrigatório recuperaria 1/38** — evidência quantitativa da lacuna de MTTD/MTTR que fundamenta a RSL e justifica o bloco ser apenas refinamento opcional.

## 5. Validação externa — execução na OpenAlex (2026-07-27)

A query foi **executada em base real** via API da OpenAlex (`title_and_abstract.search`, filtro ≥ 2020; blocos sem wildcards — stemming automático da base), com verificação de recuperação **por DOI** de cada artigo do corpus:

| Métrica                                | Resultado                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| **Recall nos 14 estudos incluídos**    | **13/14** — única perda: P24 (trade-off "autonomous system*" já documentado) |
| Excluídos/inelegíveis P26, P38, P39    | **Não recuperados** — comportamento desejável confirmado em base real        |
| P13 (não testável na calibração local) | **Recuperado** na OpenAlex ✅                                                |
| Fundacionais P01–P19                   | 6/19 recuperados — esperado (rota de snowballing)                            |
| **Volume total da query (2020+)**      | **≈ 49.700 trabalhos**                                                       |

- A validação externa **replica a calibração local** (13/14; mesmas perdas), confirmando que o matching por substring foi boa aproximação do motor real.
- **Precisão:** o volume de ~49,7 mil impõe custo de triagem. Refinamentos possíveis sem perda de recall dos incluídos: restringir o Bloco B ao título (`TITLE(...)` no Scopus) ou remover os termos mais genéricos (`resilience`, `vulnerabilit*`, `SOC`, `SRE`) — retestar recall a cada corte. Filtros de tipo de documento e área (Scopus `SUBJAREA(COMP)`) também reduzem o universo.
- ~~**Scopus propriamente dito:** pendente de credencial da API Elsevier.~~ **Executado — ver Seção 5.1.**

### 5.1. Execução no Scopus (API Elsevier, 2026-07-27)

A query foi **executada no Scopus via Scopus Search API** (sintaxe da Seção 3, forma por bloco), com verificação de recuperação **por DOI** de cada artigo do corpus:

| Métrica                                |           Scopus            | OpenAlex (referência) |
| -------------------------------------- | :-------------------------: | :-------------------: |
| **Recall nos 14 estudos incluídos**    |          **13/14**          |         13/14         |
| Única perda entre incluídos            | P24 (trade-off documentado) |          P24          |
| Excluídos/inelegíveis P26, P38, P39    |     Não recuperados ✅      |  Não recuperados ✅   |
| P13 (não testável na calibração local) |      **Recuperado** ✅      |     Recuperado ✅     |
| **Volume total (2020+, EN)**           |         **12.783**          |       ≈ 49.700        |

- **As três validações convergem** (calibração local, OpenAlex e Scopus): recall 13/14 nos incluídos, com a mesma e única perda (P24) e os mesmos misses desejáveis — a string está validada na base primária do protocolo.
- **Volume no Scopus (12.783)** é ~4× menor que na OpenAlex (campos controlados TITLE-ABS-KEY + cobertura curada) — universo de triagem viável para a RSL; os refinamentos de precisão da Seção 5 seguem disponíveis se necessário.
- **Nota de indexação:** P01 (F1000Research) **não está indexado no Scopus** (DOI não encontrado na base) — irrecuperável por qualquer string; registrar como limitação de cobertura da base, não da string.
- **Nota de sintaxe:** a forma aninhada `TITLE-ABS-KEY((A) AND (B))` retornou falso-zero quando combinada com `DOI()` na API; a forma por bloco (`TITLE-ABS-KEY(A) AND TITLE-ABS-KEY(B)`) é a recomendada e foi a validada.

## 6. Limitações

- A calibração local usa matching por substring sobre metadados; as validações externas (OpenAlex e Scopus) usam os motores reais — todas convergiram (13/14), mas as validações medem apenas _recall_ sobre o corpus conhecido.
- A _precisão_ real (proporção de ruído nos 12.783 resultados do Scopus) só é mensurável na triagem; se o volume for impraticável, aplicar os refinamentos da Seção 5 retestando o recall a cada corte.
- P01 (F1000Research) não é indexado pelo Scopus — cobrir via base complementar (a OpenAlex o recupera) ou snowballing.

---

_Derivada da síntese transversal PICOC (v1.1.0); calibrada no corpus e validada na OpenAlex e no Scopus (Scopus Search API) em 2026-07-27. Metodologia de derivação prevista nas Notas de uso do [prompt PICOC](picoc-extraction-prompt.md): "a síntese transversal de Intervention + Context é o argumento auditável para a string de busca da RSL"._
