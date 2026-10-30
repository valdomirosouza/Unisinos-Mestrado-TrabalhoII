# Relatório de Síntese Consolidado — RSL "Agentic AI Copilot para Resposta a Incidentes" (Ciclos 1 e 2)

> 🧭 **Navegação:** [🏠 README raiz](../README.md) · [📊 Dashboard](DASHBOARD.md) · [📄 Síntese do ciclo 1](relatorio-sintese.md) · [🔀 PRISMA](PRISMA.md) · [🧮 CSV ciclo 1](resultados-consolidados.csv) · [🧮 CSV ciclo 2](resultados-consolidados-ciclo2.csv)

**Data:** 2026-09-10 · **Escopo:** síntese narrativa consolidada dos dois ciclos de atualização da RSL, sobre o corpus fundacional do Trabalho I (P01–P19). O [relatório do ciclo 1](relatorio-sintese.md) permanece como registro histórico; este documento **não o substitui** — consolida.

---

## 1. Resumo executivo

A RSL acumula **dois ciclos de atualização** sobre a revisão fundacional (19 estudos, P01–P19). O **ciclo 1** (jul/2026) triou 20 candidatos e incluiu **14** (7 plenos · 5 com ressalvas · 2 fundacionais condicionais), elevando o corpus a **33**. O **ciclo 2** (set/2026) processou **49 candidatos** identificados pelo autor (P41–P89), excluiu 27 na triagem com evidência PICOC de leitura integral, avaliou 22 na íntegra e incluiu **20, todos com ressalvas** (5 fundacionais condicionais · 3 com ressalva de estrato por emenda de protocolo), levando o **corpus consolidado a 53 estudos**.

Os dois ciclos convergem no achado central da tese: **a literatura quase não mede MTTD/MTTR nominalmente**. No ciclo 1, nenhum dos 39 estudos P01–P40 o fazia. No ciclo 2, um único estudo (P76) mede MTTR de um sistema agêntico — em PoC, contra referência da literatura (não baseline próprio) e com resultado **desfavorável** ao sistema proposto. Em compensação, o ciclo 2 acrescenta duas frentes novas: **evidência secundária quantificada** de MTTD/MTTR em SOC (P79: CyberAlly com MTTR de 8 h → 90 min; GreyMatter com 98% dos alertas automatizados e contenção < 5 min) e um **cluster de medição direta de carga cognitiva/fadiga de operadores** (P62, P69, P81), inexistente no ciclo 1 — fechando parcialmente a segunda lacuna da tese (COGNITIVE_LOAD), ainda que fora do domínio de TI.

## 2. Funil PRISMA consolidado

| Etapa                   | Ciclo 1                                          | Ciclo 2                                                                      |
| ----------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------- |
| Identificados           | ≈51 registros (3 assistentes) → 21 candidatos    | 49 candidatos (P41–P89, `Papers_Index.csv`)                                  |
| Triagem bibliométrica   | 20 triados · 2 inelegíveis (Qualis A3: P39, P40) | 49 triados · 4 fora de estrato **mantidos com ressalva** (emenda 2026-09-09) |
| Triagem temática        | — (E2/E3 aplicados só após avaliação)            | **27 excluídos** com evidência PICOC (E2 = 19 · E3 = 8)                      |
| Avaliados na íntegra    | 18                                               | 22                                                                           |
| Excluídos pós-avaliação | 4 (P26, P29, P30, P38)                           | 2 (P85, P86)                                                                 |
| **Incluídos**           | **14**                                           | **20**                                                                       |
| Corpus acumulado        | 33 (19 + 14)                                     | **53 (33 + 20)**                                                             |

Diagramas completos em [`PRISMA.md`](PRISMA.md). Diferença metodológica relevante: no ciclo 2 a exclusão temática pôde ocorrer **na triagem** porque a extração PICOC de leitura integral ([`picoc-results-consolidated-P41-P89-Claude.md`](../picoc/picoc-results-consolidated-P41-P89-Claude.md)) forneceu evidência auditável antes da avaliação — no ciclo 1, os equivalentes (P26/P29/P30/P38) só caíram após avaliação completa, e são os precedentes citados em cada exclusão do ciclo 2 ([`triagem-ciclo2.md`](triagem-ciclo2.md)).

## 3. Composição do corpus consolidado (n = 53)

- **19 fundacionais** do Trabalho I (P01–P19).
- **14 do ciclo 1** (P20–P37): núcleo agêntico×IR — LLM multi-agente (P27, P28, P31, P35), closed-loop (P22), SLM-agente (P21), MAS/RL não-LLM (P25), copilot IR (P34), GNN+LLM (P23, P32), IaC (P20), governança/adoção (P37) + 2 fundacionais (P24, P33).
- **20 do ciclo 2** (P43–P88): Agentic AIOps e SOC (P43, P76, P83, P87), LLM×IR/forense (P53, P78), telemetria agêntica (P55), MAS self-healing (P88, análogo a P25), alert fatigue (P73), LLMOps (P74), predictive maintenance agêntico (P82) + **5 fundacionais** (P52, P54, P72, P77, P79) + **cluster humano/carga cognitiva** (P62, P69, P81) + instrumento HCI (P63).
- **Fundacionais condicionais: 7 no total** (P24, P33, P52, P54, P72, P77, P79) — se o protocolo restringir o corpus a estudos primários, migram para a fundamentação (corpus primário: 46).
- **Ressalvas de estrato (emenda 2026-09-09): 3 incluídos** — P62, P69 (Qualis A3) e P81 (A4); a ressalva é obrigatória em qualquer uso na síntese.

## 4. Cobertura das questões de pesquisa nos dois ciclos

A lacuna sistemática **migrou de RQ4 para RQ3** entre os ciclos:

- **Ciclo 1** (18 avaliados): forte em RQ1–RQ3 (estudos empíricos de sistemas agênticos), fraco em **RQ4 (Ética & Desafios)** — só 4/18 plenas.
- **Ciclo 2** (22 avaliados): perfil invertido — os surveys fundacionais cobrem bem RQ1/RQ4/RQ5 (P79 é o único RQ pleno 5,0/5,0 de toda a RSL; P54 e P55 com 4,5), mas **RQ3 (Evidence Benefits) é a maior lacuna**: nenhum estudo do ciclo 2 recebeu "Incluir" pleno, e QA3 (base de evidências) concentra os N — 8 estudos secundários/conceituais sem validação empírica própria.

Leitura combinada: o corpus consolidado tem **fundamentação conceitual abundante e evidência empírica de benefício escassa** — exatamente a justificativa da pergunta de pesquisa da dissertação. Gráficos: [ciclo 1](graficos.md) · [ciclo 2](graficos-ciclo2.md).

## 5. Qualidade (QA/DARE) comparada

| Métrica                      | Ciclo 1 (18) | Ciclo 2 (22) |
| ---------------------------- | :----------: | :----------: |
| SCORE_RQ médio (mediana)     |  3,83 (4,0)  |  3,16 (3,5)  |
| SCORE_QA médio (mediana)     | 3,50 (3,75)  | 2,75 (2,75)  |
| Banda Alta / Média / Baixa   |  14 / 4 / 0  | 11 / 10 / 1  |
| Recomendação "Incluir" plena |      7       |    **0**     |

A queda de qualidade média do ciclo 2 não é ruído: o lote é dominado por revisões e propostas conceituais (QA3 = N recorrente), enquanto o ciclo 1 concentrava protótipos e experimentos. Destaques de qualidade do ciclo 2: **P73** e **P88** (QA 4,0/4,0), **P78** e **P87** (QA 3,5, Banda Alta). Piores: P74 (QA 1,0, Banda Baixa — mantido só como fonte conceitual LLMOps).

## 6. Evidência sobre MTTD/MTTR e carga cognitiva (núcleo da tese)

**MTTD/MTTR nominal.** Situação consolidada após 89 candidatos avaliados em dois ciclos:

- **P76** (ciclo 2) — único estudo que **mede MTTR** de um sistema agêntico: fases de ~1 min a 1,5 min em PoC de SOC (brute-force SSH), comparadas ao Microsoft Copilot for Security **via literatura** (~30–45 s) — sem baseline próprio e com o sistema proposto mais lento que a referência.
- **P79** (ciclo 2, secundário) — evidência citada de estudos primários: CyberAlly (MTTR 8 h → 90 min; falsos positivos 70% → 35%), GreyMatter (98% dos alertas automatizados, contenção < 5 min), baseline setorial de 277 dias (204 detectar + 73 conter).
- **Proxies quantitativos** — P73: redução global de alertas de 74–84% (alert fatigue, Outcome nomeado); P81: reaction time do operador de ~276 s → ~107 s com DSS (Wilcoxon p = 0,00); P87: latência ponta a ponta de 2,9–11,6 s por incidente com pré-detecção em 0,3 s; P83: qualidade de resposta do copilot (BERTScore ≈ 85–87%), sem tempos.
- **Todo o restante do corpus** reporta proxies de detecção (accuracy/F1/AUC) ou alegações qualitativas ("reduces response time") sem medição.

**Conclusão que os dois ciclos sustentam:** não existe, no corpus, um estudo que meça MTTD **e** MTTR nominalmente, com baseline próprio, em ambiente de produção — a lacuna que a dissertação ataca permanece aberta e agora está **triangulada em 89 candidatos**.

**Carga cognitiva (COGNITIVE_LOAD).** O ciclo 1 não tinha nenhuma medição direta. O ciclo 2 incorpora, com ressalvas de estrato e domínio: **P62** (fundamentos de neuroergonomia e mental workload), **P69** (WAUC — base multimodal com AUC de classificação de workload até 0,998), **P81** (experimento humano com DSS em sala de controle) e **P63** (BUS-15, instrumento de usabilidade de conversational agents — candidato a instrumento de avaliação do copilot da tese, junto com NASA-TLX usado em P69). Nenhum desses mede carga cognitiva **em resposta a incidentes de TI** — a interseção exata (copilot × IR × carga cognitiva medida) segue vazia, reforçando a RQ da dissertação.

## 7. Taxonomia consolidada dos paradigmas agênticos

- **LLM multi-agente:** P27, P28, P31, P35 (ciclo 1) · P76 (SOAR hyper-automation) — maduro em RCA/SOC, evidência em simulação/PoC.
- **Copilot / agente único LLM+RAG:** P34 (ciclo 1) · P78, P83, P87 (ciclo 2) — o paradigma da tese; evidência limitada a qualidade de resposta e latência, nunca MTTD/MTTR.
- **SLM / modelos compactos:** P21 (ciclo 1) — segue único; relevante para custo/confidencialidade.
- **MAS/RL e auto-organização não-LLM:** P25 (ciclo 1) · P88 (ciclo 2) — self-healing com garantias empíricas fortes (QA 4,0), lembrando que agência não implica LLM.
- **Frameworks conceituais Agentic AIOps/PdM:** P43, P82 (ciclo 2) — definem níveis de autonomia e alinhamento ITIL, sem evidência.
- **Fundacionais (surveys de agentes/LLM em segurança e operações):** P24, P33 (ciclo 1) · P52, P54, P72, P77, P79 (ciclo 2).
- **Fatores humanos:** P37 (percepção/adoção, ciclo 1) · P62, P63, P69, P81 (ciclo 2) — novo eixo do corpus.
- **Procedência a monitorar:** cluster State Grid (P31, P32, P35) no ciclo 1; NICT (P73/P80 — este excluído) no ciclo 2.

## 8. Rastreabilidade das exclusões

- **Ciclo 1:** P39/P40 (inelegíveis, Qualis A3); P26, P29, P30 (não-agênticos), P38 (fora de domínio) — após avaliação integral.
- **Ciclo 2 — triagem (27):** E2 não-agêntico = 19 (P41, P42, P44–P51, P64–P66, P70, P71, P75, P80, P84, P89; precedentes P26/P29/P30) · E3 fora de domínio = 8 (P56–P61, P67, P68; precedente P38) — tabelas com evidência PICOC em [`triagem-ciclo2.md`](triagem-ciclo2.md).
- **Ciclo 2 — pós-avaliação (2):** P85 (SCORE_RQ 0,5 — sólido metodologicamente, sem aderência às RQs) e P86 (não-agêntico; agravante de estrato B1 + SJR Q3).

## 9. Confiabilidade e validação cruzada

- **Ciclo 1:** avaliação com comparação Claude × ChatGPT (concordância 90%, κ = 0,74); extração PICOC com três avaliadores (P/I/O/C 100%; Comparison κ Fleiss 0,37 → originou a regra de protocolo v1.1.0).
- **Ciclo 2:** extração PICOC e pareceres produzidos por **avaliador único** (Claude, prompts v1.3.0 com persona padronizada) — a comparação entre avaliadores do ciclo 2 está **pendente** e é o principal reforço de confiabilidade recomendado antes de fechar a síntese da dissertação.

## 10. Limitações e ameaças à validade

1. **Avaliador único no ciclo 2** (ver §9).
2. **Qualis derivado do percentil Scopus** (regra CAPES 2025-2028) — calibrado sem exceção nos 39 pares verificados do ciclo 1, mas não confirmado individualmente na Plataforma Sucupira para P41–P89.
3. **Emenda de protocolo (2026-09-09):** 3 incluídos fora dos estratos I3/I4 — sensibilidade da síntese a esses estudos deve ser reportada.
4. **Citações Scopus pendentes** para P41–P89 (OpenAlex/Crossref verificadas em 2026-09-09; sem chave de API).
5. **Evidência do ciclo 2 majoritariamente conceitual/PoC** — nenhuma inclusão plena; generalizações de benefício devem citar o nível de evidência da ficha de extração.
6. Exclusão temática na triagem (ciclo 2) apoiada em PICOC de leitura integral — mais forte que title/abstract, mas sem segundo avaliador.

## 11. Próximos passos recomendados

1. Comparação entre avaliadores do ciclo 2 (ChatGPT/Gemini) — pareceres e/ou PICOC.
2. Completar citações Scopus (nova chave de API) e, se desejado, confirmar Qualis na Sucupira para os 20 incluídos.
3. Atualizar as citações cruzadas do corpus para P01–P89.
4. Decidir formalmente o tratamento dos 7 fundacionais condicionais (corpus 53 vs. primário 46).
5. Incorporar esta síntese à dissertação, usando P76/P79/P73/P81 como âncoras da discussão de MTTD/MTTR e o cluster P62/P69/P63 como base instrumental para medir carga cognitiva no experimento da tese.

## 12. Nota metodológica

Protocolo idêntico ao do ciclo 1 ([§13 do relatório histórico](relatorio-sintese.md)): Kitchenham et al. (2009), DARE QA1–QA4, SCORE_RQ (T/P/N → 1,0/0,5/0,0, máx. 5,0), SCORE_QA (Y/P/N, máx. 4,0), bandas Alta ≥ 3,0 / Média 1,5–2,5 / Baixa < 1,5. Diferenças do ciclo 2: (i) bibliometria verificada **antes** da avaliação ([`papers-ciclo2.csv`](../papers-ciclo2.csv)) — Tabela A dos pareceres cita valores verificados em vez de `[VERIFICAR]`; (ii) triagem temática antecipada com evidência PICOC; (iii) prompts padronizados com persona de pesquisador orientado e Kitchenham (2009) pelo título ([template](../prompts/prompt-chatgpt-consultation.md)); (iv) emenda de protocolo de estratos registrada e datada. Dados: [`resultados-consolidados.csv`](resultados-consolidados.csv) (ciclo 1) · [`resultados-consolidados-ciclo2.csv`](resultados-consolidados-ciclo2.csv) (ciclo 2) · fichas em [`../report/`](../report/README.md).

---

## Adendo (2026-10-25) — comparação entre avaliadores do ciclo 2 concluída

A limitação nº 1 (§9/§10: avaliador único no ciclo 2) foi **sanada**: o autor executou os 22 prompts no **ChatGPT** e no **Gemini**, e a [comparação entre três avaliadores](comparacao-avaliadores-ciclo2.md) foi computada em 2026-10-25. Resultado: acordo de decisão **81,8–95,5% por par** (Claude×Gemini κ = 0,65 "substancial"; Fleiss κ = 0,36 sob o mesmo paradoxo de prevalência da comparação PICOC); **as 4 divergências são todas protocolares** — 3 pela aplicação estrita do critério de estrato pelo ChatGPT (P62/P69/P81, que ignorou a emenda de 2026-09-09) e 1 pelo destino do cluster de carga cognitiva (P85) — **nenhuma de mérito**. O achado central (nenhum estudo do ciclo 2 mede MTTD/MTTR com baseline próprio) foi confirmado de forma independente pelos três avaliadores. Duas regras de protocolo a registrar pelo condutor: emendas de elegibilidade no corpo normativo dos prompts; destino dos estudos do cluster humano sem aderência às RQs.

---

## Adendo (2026-10-26) — corpus P01–P88 com validação tripla completa

Após o adendo anterior, três marcos fecharam a validação de todo o corpus avaliado:

1. **Avaliação retroativa dos fundacionais (P01–P19):** os 19 estudos herdados do Trabalho I receberam pareceres padronizados (inclusão não rediscutida; SCORE_RQ médio 3,66 · SCORE_QA médio 2,53 · 9 Alta/10 Média) — [tabela](README.md) · [CSV](resultados-consolidados-fundacionais.csv) · [gráficos](graficos-fundacionais.md). Com isso, **os 61 pareceres (P01–P88) usam as mesmas Tabelas 3/5/7**.
2. **Três avaliadores sobre o corpus inteiro:** ChatGPT e Gemini completaram os conjuntos P01–P88 (61 avaliações cada), consolidados por avaliador em [CSVs próprios](resultados-consolidados-claude-P01-P88.csv).
3. **[Comparação global](comparacao-avaliadores-global.md):** acordo de decisão **90,2–91,8% por par** · κ 0,51–0,57 · **Fleiss 0,53** · **53/61 decisões unânimes** (fundacionais 19/19; exclusões unânimes: P30, P39, P86). As **8 divergências formam 3 famílias protocolares** — (A) estudos secundários não-agênticos (P26, P29); (B) emenda de estratos de 2026-09-09 (P62, P69, P81); (C) fronteiras de domínio/estrato (P38, P40, P85) — **nenhuma de mérito**: nos 8 casos os escores dos três avaliadores convergem e o que varia é a regra aplicada à consequência.

**Implicações para a síntese:** (i) a seção 9 e as limitações 1 e 6 do corpo deste relatório estão **superadas** — a validação cruzada agora cobre fundacionais, ciclo 1 e ciclo 2; (ii) o corpus central da RSL (50 inclusões + 3 exclusões unânimes = 87%) é **avaliador-independente**; (iii) as 3 famílias de divergência são a lista fechada de decisões de protocolo a registrar pelo condutor (tratamento de secundários não-agênticos; posição normativa da emenda de estratos nos prompts; rigor do corte de domínio e destino do cluster de carga cognitiva); (iv) o achado central — nenhum estudo mede MTTD/MTTR nominalmente com baseline próprio em produção — permanece confirmado de forma independente pelos três avaliadores em todo o corpus. O [`Papers_Index.csv`](../Papers_Index.csv) consolida por estudo o status RSL e os escores dos três avaliadores.

---

## Adendo (2026-10-26, nº 3) — tripla checagem bibliométrica completa (Scopus)

Com a chave Scopus regenerada (mantida fora do repositório), as duas pendências bibliométricas remanescentes foram encerradas:

1. **Citações por estudo (P41–P89):** coluna Scopus completada em [`papers-ciclo2.csv`](../papers-ciclo2.csv) — **49/49 resolvidos, todos com Citações ≥ 1, nenhum NÃO INDEXADO** (verificação de 2026-10-26). O critério I5 agora está confirmado em **três fontes para todo o corpus P01–P89**.
2. **Citações cruzadas ([`citacoes-cruzadas-P01-P89.md`](../citacoes-cruzadas-P01-P89.md)):** coluna Scopus preenchida via `REF()` por título — **48 arestas no Scopus, união final de 52** (era 49 com OA/CR). O Scopus agregou 3 arestas exclusivas (destaque: **P54←P06 e P54←P15**, elevando o survey "LLM Reasoning → AI Agents" a estudo citado por dois fundacionais) e confirmou os hubs P10 (7), P09 (6), P14 (5), P16 e P65 (3).

**Registro metodológico:** a rodada documentou dois quirks novos da Scopus Search API — **(a)** o nível de serviço da chave limita **`count ≤ 25`** por requisição (HTTP 400 "Exceeds the maximum number allowed for the service level" acima disso; duas varreduras completas falharam até o diagnóstico); **(b)** títulos de índice com sufixos editoriais (caso P14, "(Kshetri)") zeram silenciosamente o `REF()` — soma-se aos quirks do ciclo 1 (`REF()` por título, não DOI; forma aninhada com falso-zero). Com isso, a **limitação nº 4 do corpo deste relatório (citações Scopus pendentes) está superada** — das limitações originais, permanecem apenas as decisões de protocolo das 3 famílias de divergência (adendo nº 2) e a confirmação individual de Qualis na Sucupira, opcional.

---

_Gerado em 2026-09-10 a partir dos artefatos versionados dos dois ciclos (adendos de 2026-10-25 e 2026-10-26 acima). Este documento consolida; os relatórios e avaliações de cada ciclo permanecem como registros históricos imutáveis._

---

## Errata (2026-10-27)

- Na tabela comparativa dos ciclos, o **SCORE_QA médio do ciclo 2** correto é
  **2,73** (soma 60,0 ÷ 22 avaliados, conferida em
  [`resultados-consolidados-ciclo2.csv`](resultados-consolidados-ciclo2.csv));
  o valor 2,75 ali exibido como média é a **mediana**. Detectado na
  verificação final de contagens do artigo IEEE Access (2026-10-27). O texto
  histórico acima não foi reescrito, conforme a convenção do repositório.

---

## Adendo (2026-10-28, nº 4) — ciclo 3 até a avaliação parcial (Claude)

O **ciclo 3** (atualização de revisão, descoberta de 2026-10-27) avançou até a
avaliação integral pelo primeiro avaliador:

1. **Funil:** 37 candidatos novos (P90–P126) → 19 elegíveis na Etapa 1
   ([PDR-0006](../protocolo/pdr/PDR-0006-estrato-de-conference-papers-pelo-percentil-da-serie.md)
   introduz o estrato de conference papers pelo percentil Scopus da série;
   [PDR-0007](../protocolo/pdr/PDR-0007-renovacao-da-emenda-de-estratos-para-o-ciclo-3.md)
   renova a emenda de estratos) → 14 com extração PICOC de leitura integral
   (5 capítulos Springer sem acesso, *reports not retrieved*) → triagem:
   **13 aprovados** · 1 excluído (E3: P108) — [`triagem-ciclo3.md`](triagem-ciclo3.md).
2. **Avaliação (Claude, 13/13):** 1 Incluir (P94) · 11 Incluir c/ ressalvas ·
   1 Excluir (P106, E2 — "Agentic AI" nominal: ML/DRL sem LLM/arquitetura de
   agentes). SCORE_RQ **média 3,85 · mediana 4,0**; SCORE_QA **média 2,77 ·
   mediana 3,0**; bandas 9 Alta · 3 Média · 1 Baixa
   ([`resultados-consolidados-ciclo3.csv`](resultados-consolidados-ciclo3.csv),
   [gráficos](graficos-ciclo3.md)).
3. **Achado que altera o quadro dos ciclos 1–2:** o ciclo 3 traz o primeiro
   cluster de **primários com MTTD/MTTR nominal medido contra baseline
   executado** — P100 (AIDR-Cloud: MTTR −63% vs. SREs; MTTD p90 −83% em
   incidentes reais), P101 (ED-ASOC: MTTR −72,3%), P102 (Intelligent SRE:
   MTTD −82% vs. SREs sêniores) e P123 (CIPHER-A: MTTC −37,8%, DARPA OPTC).
   O achado central dos ciclos anteriores ("nenhum estudo mede MTTD/MTTR
   nominalmente com baseline próprio") **deixa de valer para o corpus do
   ciclo 3** — porém **todos os quatro estudos carregam ressalva de estrato
   obrigatória** (séries B2–B4/A4 ou journals A3/não indexados), o que deve
   qualificar qualquer síntese de benefícios.
4. **Pendências:** avaliações ChatGPT e Gemini (mesmos prompts imutáveis),
   consolidação tripla e comparação entre avaliadores (κ); 5 Springer via
   biblioteca/COMUT; snowballing (rota de recaptura do P90, nota no PDR-0006).
   **O corpus consolidado da RSL permanece 53** até o fecho das Etapas 7–8
   com os três avaliadores.



## Adendo (2026-10-29, nº 5) — ciclo 3: avaliação tripla concluída (Etapa 7)

As avaliações **ChatGPT** e **Gemini** dos 13 aprovados na triagem chegaram em
2026-10-29 (mesmos prompts imutáveis de `prompts/prompt-PXX.md`, template
v1.1.0), fechando a consolidação da Etapa 7 com os três avaliadores
independentes:

| Avaliador | SCORE_RQ média (mediana) | SCORE_QA média (mediana) | Bandas (Alta·Média·Baixa) | Recomendações |
| --- | --- | --- | --- | --- |
| Claude | 3,85 (4,0) | 2,77 (3,0) | 9 · 3 · 1 | 1 Incluir · 11 c/ ressalvas · 1 Excluir |
| ChatGPT | 4,12 (4,0) | 2,69 (2,5) | 5 · 8 · 0 | 12 Incluir c/ ressalvas · 1 Excluir |
| Gemini | 3,77 (4,0) | 2,92 (3,0) | 9 · 3 · 1 | 1 Incluir · 11 c/ ressalvas · 1 Excluir |

Leituras principais (fonte: `resultados-consolidados-ciclo3.csv` +
`Papers_Index.csv`, escores dos três avaliadores):

1. **Unanimidade no colapso Incluir/Excluir:** os três avaliadores convergem
   nos 13 estudos — 12 Incluir (P94 pleno por Claude e Gemini; com ressalvas
   pelo ChatGPT) e **1 Excluir (P106, E2 — agência nominal, DRL/CNN sem
   Agentic AI)**, confirmando o flag da triagem. O κ formal por par, o Fleiss
   e a análise de divergências de escore são da Etapa 8.
2. **O cluster MTTD/MTTR nominal sobrevive aos três avaliadores:** P100, P101,
   P102 e P123 mantêm recomendação de inclusão pelos três, sempre com a
   **ressalva de estrato obrigatória** (PDR-0006/0007) — o achado do adendo
   nº 4 permanece, agora com validação tripla.
3. **Divergências de intensidade, não de decisão:** o ChatGPT pontua RQ mais
   alto (média 4,12) e QA mais baixo (mediana 2,5; 5 bandas Alta contra 9 de
   Claude/Gemini), refletindo rubrica QA "operacional provisória" declarada
   nos próprios pareceres; Gemini e Claude praticamente coincidem nas bandas
   (9·3·1). Nenhuma divergência atinge o colapso de decisão.
4. **Próximos passos:** comparação entre avaliadores (Etapa 8 — κ de Cohen
   por par, Fleiss, prevalência) e fichas de extração (Etapa 9); só então o
   corpus consolidado (hoje **53**) incorpora o ciclo 3. Permanecem as
   pendências dos 5 Springer (biblioteca/COMUT) e do snowballing (P90).


## Adendo (2026-10-29, nº 6) — ciclo 3: comparação entre avaliadores (Etapa 8) e fecho do ciclo

A comparação formal dos três avaliadores sobre os 13 estudos do ciclo 3
(`scripts/compute-kappa.py`, decisão colapsada Incluir/Excluir) fecha a
Etapa 8 com resultado inédito nos três ciclos:

| Métrica | Claude × ChatGPT | Claude × Gemini | ChatGPT × Gemini |
| --- | :---: | :---: | :---: |
| Acordo | 100% (13/13) | 100% (13/13) | 100% (13/13) |
| Cohen's κ | 1,00 | 1,00 | 1,00 |
| MAE SCORE_RQ / SCORE_QA | 0,42 / 0,31 | 0,38 / 0,23 | 0,50 / 0,54 |

**Fleiss' κ = 1,00 · 13/13 unânimes · prevalência de Incluir 92,3%** —
*almost perfect* (Landis & Koch), sem a deflação do paradoxo da prevalência
dos ciclos 1–2 porque não há desacordo algum a penalizar. Leituras:

1. **Nenhuma divergência protocolar ou de mérito; nenhum PDR novo.** A
   exclusão do P106 (E2 — Agentic AI nominal) é unânime e confirma o flag da
   triagem com evidência PICOC.
2. **A lição protocolar do ciclo 2 está verificada:** com as emendas
   PDR-0006/0007 injetadas no texto normativo dos prompts pelo render
   (regra R2/PDR-0004), o ChatGPT avaliou todos os fora-de-estrato com
   ressalva (zero `NA`), em vez de encerrá-los na triagem como fez com
   P62/P69/P81 no ciclo 2.
3. **Diferenças restantes são de intensidade:** rubrica QA do ChatGPT mais
   conservadora (5 bandas Alta vs. 9; acordo de banda 62%); Claude × Gemini
   com bandas idênticas (13/13) e menores MAEs — detalhes em
   [`comparacao-avaliadores-ciclo3.md`](comparacao-avaliadores-ciclo3.md).
4. **Corpus consolidado: 53 → 65.** Com a Etapa 8 fechada, o ciclo 3
   incorpora seus 12 incluídos (P91, P93, P94, P97, P100, P101, P102, P110,
   P112, P119, P121, P123 — todos com ressalva de estrato obrigatória,
   PDR-0006/0007, exceto a dimensão fundacional-condicional R1 de
   P110/P112/P121). O cluster MTTD/MTTR nominal (P100/P101/P102/P123) entra
   no corpus com validação tripla. Pendências que podem alterar o corpus em
   adendos futuros: 5 capítulos Springer adiados (biblioteca/COMUT),
   snowballing obrigatório (rota de recaptura do P90) e fichas de extração
   (Etapa 9).


## Adendo (2026-10-29, nº 7) — fecho do ciclo 3: Springer não recuperados removidos (PDR-0008)

Segunda tentativa de obtenção dos 5 capítulos Springer adiados (P92, P95,
P109, P122, P126 — volumes CCIS/LNCS/LNNS de 2026), executada via Claude in
Chrome sobre a sessão autenticada do proxy CAPES, falhou nos cinco (endpoint
de PDF em 204 vazio; páginas com "Log in via an institution" — assinatura não
cobre os volumes). Por decisão do condutor
([PDR-0008](../protocolo/pdr/PDR-0008-remocao-dos-springer-nao-recuperados.md)),
os cinco saem da revisão como **"reports not retrieved" (PRISMA 2020)** —
exclusão por indisponibilidade, não por mérito, sem adendo futuro previsto.

Consequências: o funil do ciclo 3 fecha **definitivo** (37 identificados →
19 elegíveis → 5 not retrieved → 14 triados → 13 avaliados → **12
incluídos**); o **corpus consolidado permanece 65**; a rota de reavaliação do
P90 pela cadeia de citação P92→P90 (adendo do snowballing) encerra-se. Com
isso, **o ciclo 3 não tem pendências abertas**.


## Adendo (2026-10-30, nº 8) — PDR-0009: régua internacional de elegibilidade (percentil Scopus Q1–Q3)

Por decisão do condutor
([PDR-0009](../protocolo/pdr/PDR-0009-elegibilidade-por-quartil-do-percentil-scopus.md)),
a revisão passa a usar como critério de qualidade de veículo **apenas o
percentil CiteScore (Scopus), em quartis — Q1–Q3 elegíveis** (séries de
proceedings seguem o PDR-0006). O Qualis/CAPES, classificação nacional sem
validade internacional, e o quartil SJR tornam-se informativos. Aplicação
**retroativa com ressalva**: nenhum estudo sai do corpus (65 mantido;
distribuição 53 Q1 · 8 Q2 · 1 Q3 · 1 Q4 · 2 não indexados); as ressalvas de
estrato Qualis dissolvem-se para os estudos em Q1–Q3; **P91, P101 e P102**
(Q4/não indexados) permanecem com **ressalva obrigatória reformulada**.
Efeito central na síntese: no cluster MTTD/MTTR nominal, **P100 (Q3) e P123
(Q2) ficam dentro da régua sem ressalva de veículo** — a qualificação
"todos sob ressalva de estrato" dos adendos nº 4–6 é re-lida: ela valia na
régua Qualis; na régua internacional, metade do cluster está dentro da
barra, e P101/P102 seguem ressalvados. Vereditos, funis e κ dos ciclos 1–3
não são reabertos (Art. VI).
