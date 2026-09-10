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

_Gerado em 2026-09-10 a partir dos artefatos versionados dos dois ciclos. Este documento consolida; os relatórios e avaliações de cada ciclo permanecem como registros históricos imutáveis._
