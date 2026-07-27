# Comparação entre Avaliadores — Extração PICOC (Claude × ChatGPT × Gemini)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [Prompt PICOC](picoc-extraction-prompt.md) · [Claude](picoc-results-consolidated-P01-P40-Claude.md) · [ChatGPT](picoc-results-consolidated-P01-P40-ChatGPT.md) · [Gemini](picoc-results-consolidated-P01-P40-Gemini.md) · dados em [CSV](picoc-comparacao-avaliadores.csv)

Comparação da extração PICOC executada com o mesmo prompt ([`picoc-extraction-prompt.md`](picoc-extraction-prompt.md) v1.0.0) por **três avaliadores** (Claude, ChatGPT, Gemini) sobre o corpus de 39 artigos (P01–P35, P37–P40). A unidade de comparação é o **status atribuído a cada elemento PICOC** por artigo: `DECLARED` (conteúdo substantivo extraído), `NA` (registrado como "N/A", p.ex. estudo de mapeamento) ou `NÃO DECLARADO` (elemento ausente do artigo). A matriz completa de status está em [`picoc-comparacao-avaliadores.csv`](picoc-comparacao-avaliadores.csv).

## Cobertura

| Avaliador | Artigos cobertos | Observação                                                                       |
| --------- | :--------------: | -------------------------------------------------------------------------------- |
| Claude    |      39/39       | P01–P35, P37–P40                                                                 |
| ChatGPT   |      39/39       | P01–P35, P37–P40                                                                 |
| Gemini    |    **30/39**     | ⚠️ **P01–P09 ausentes** do arquivo entregue — a extração do Gemini começa em P10 |

As métricas de 3 avaliadores usam os **30 artigos comuns** (P10–P35, P37–P40); a comparação Claude × ChatGPT usa os 39.

## Acordo por elemento PICOC

| Elemento       | Claude × ChatGPT (39) | Cohen's κ | 3 avaliadores (30) | Fleiss' κ |
| -------------- | :-------------------: | :-------: | :----------------: | :-------: |
| Population     |         100%          |   1,00    |        100%        |   1,00    |
| Intervention   |         100%          |   1,00    |        100%        |   1,00    |
| **Comparison** |        **82%**        | **0,42**  |      **82%**       | **0,42**  |
| Outcomes       |         100%          |   1,00    |        100%        |   1,00    |
| Context        |         100%          |   1,00    |        100%        |   1,00    |

- **Population, Intervention, Outcomes e Context:** acordo perfeito de status — os três avaliadores classificaram todos esses elementos como `DECLARED` em todos os artigos cobertos. Nota metodológica: com distribuição quase uniforme, o κ = 1,00 é trivial (não há variância a explicar); o acordo relevante aqui é o de **conteúdo**, tratado qualitativamente abaixo.
- **Comparison é o único elemento discriminante:** 82% de acordo e **κ = 0,42 (moderado)**, tanto no par Claude × ChatGPT quanto no trio (Fleiss).

## Distribuição de Comparison por avaliador

| Avaliador | DECLARED | N/A | Universo |
| --------- | :------: | :-: | :------: |
| Claude    |    31    |  8  |    39    |
| ChatGPT   |    32    |  7  |    39    |
| Gemini    |    22    |  8  |    30    |

## Divergências em Comparison (10 artigos)

| ID  |  Claude  | ChatGPT  |  Gemini   | Natureza da divergência                                                                                       |
| --- | :------: | :------: | :-------: | ------------------------------------------------------------------------------------------------------------- |
| P01 |   N/A    | DECLARED |     —     | ChatGPT aceita contraste arquitetural interno (4 tipos de arquitetura) como Comparison                        |
| P03 |   N/A    | DECLARED |     —     | ChatGPT aceita comparação exploratória GPT-4o vs. DeepSeek-R1 (sem baseline central)                          |
| P12 |   N/A    | DECLARED |    N/A    | ChatGPT aceita contraste conceitual GenAI vs. AI/ML tradicional                                               |
| P15 | DECLARED | DECLARED |    N/A    | Gemini rejeita o contraste de paradigmas (Agentic AI vs. GenAI/MAS) por ser não-experimental                  |
| P16 | DECLARED | DECLARED |    N/A    | Gemini rejeita o framework conceitual MLOps vs. AIOps como Comparison                                         |
| P17 |   N/A    | DECLARED |    N/A    | ChatGPT aceita o contraste XAI vs. black-box como Comparison                                                  |
| P18 | DECLARED |   N/A    |    N/A    | Claude aceita a comparação pontual ML vs. rule-based (AVL); os demais exigem baseline da arquitetura completa |
| P29 | DECLARED | DECLARED |    N/A    | Gemini trata a SLR como mapeamento; os demais aceitam o contraste ML/DL vs. LLM-driven                        |
| P33 | DECLARED |   N/A    | DECLARED* | *Gemini contraditório: raciocínio diz N/A, tabela consolidada declara ("defesas convencionais reativas")      |
| P40 | DECLARED |   N/A    | DECLARED  | Claude/Gemini aceitam o contraste com métodos manual/rule-based/ML-DL; ChatGPT classifica como survey N/A     |

## Interpretação

1. **A divergência é definicional, não factual.** Todos os 10 casos divergentes são estudos secundários ou com comparação **conceitual/paradigmática** (não empírica). Os avaliadores discordam sobre a fronteira "contraste conceitual conta como Comparison?" — não sobre o conteúdo dos artigos. Nenhum estudo primário com baseline experimental gerou divergência.
2. **Vieses de fronteira distintos:** ChatGPT é o mais permissivo (aceita contrastes internos/exploratórios: P01, P03, P12, P17); Gemini é o mais restritivo (exige experimento: rejeita P15, P16, P29); Claude fica no meio (aceita contraste conceitual quando o artigo o estrutura explicitamente como comparação: P33, P40, P18).
3. **Acordo de conteúdo onde ambos declaram:** nos artigos em que os avaliadores coincidem em `DECLARED`, os gists convergem semanticamente (p.ex. P29: "ML tradicional e deep learning vs. LLM-driven" ≈ "ML/DL e métodos tradicionais vs. LLMs") — a leitura dos PDFs é consistente.
4. **Achado central preservado nos três:** nenhum avaliador encontrou medição nominal de **MTTD/MTTR** no corpus; o padrão "outcomes substantivos + MTTD/MTTR NÃO DECLARADO" repete-se nos três conjuntos, o que **triangula a lacuna** que fundamenta a RSL.

## Ressalvas

- **Cobertura do Gemini:** a ausência de P01–P09 reduz o universo do Fleiss' κ para 30 artigos e impede conclusões do trio sobre a base fundacional (P01–P09). Recomenda-se reexecutar o prompt no Gemini para os 9 artigos faltantes.
- **Comparação em nível de status, não de texto:** as métricas medem acordo sobre a _classificação_ dos elementos; equivalência textual fina das células não foi quantificada (apenas amostrada via gists).
- **Cautela de conteúdo (exemplo):** para P14, o Gemini reporta "redução do MTTR em 30%" como outcome — número que o artigo atribui a **claims de fornecedores**, não a medição própria; o conjunto do Claude registra essa procedência. Ao usar os outcomes do Gemini, verificar a origem dos números no PDF.
- **κ com prevalência alta:** em Comparison, a predominância de `DECLARED` deprime o κ (paradoxo de prevalência); o valor 0,42 deve ser lido junto com o acordo bruto de 82%.

## Recomendação para o protocolo da RSL

Adotar regra explícita para Comparison em estudos secundários — p.ex. **"Comparison = DECLARED somente com baseline empírico; contraste conceitual/paradigmático registra-se como `N/A (contraste conceitual)`"** — e reclassificar os 10 casos divergentes com essa regra. Isso deve elevar o κ de Comparison ao patamar dos demais elementos e tornar a extração auditável em banca.

---

_Gerado a partir dos três arquivos consolidados em `picoc/`, normalizados para status por elemento (matriz em [`picoc-comparacao-avaliadores.csv`](picoc-comparacao-avaliadores.csv)). Metodologia: acordo bruto, Cohen's κ (pares) e Fleiss' κ (trio) sobre P10–P35, P37–P40._
