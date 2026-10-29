# Parecer acadêmico integral — P123

**Estudo:** Kizhakel, S. P.; Pande, S. D. (2026). *An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response*. **Discover Artificial Intelligence**, 6, artigo 970. DOI: https://doi.org/10.1007/s44163-026-02058-6  
**Tipo:** artigo de periódico, pesquisa experimental de arquitetura/protótipo.  
**Protocolo:** RSL em Computação Aplicada, diretrizes de Kitchenham; regras e PDRs fornecidos no `prompt-P123.md`.  
**Decisão sintética:** **Incluir c/ ressalvas (Qualis A3, PDR-0007; comparações externas indicativas e inconsistência no cálculo do tempo operacional).**

> **Nota de rastreabilidade:** o prompt disponível define as RQs e as regras de pontuação, mas não fornece o arquivo `templates/review.md`, as definições completas do PICOC nem a redação específica de QA1–QA4. Portanto, as tabelas abaixo usam a estrutura solicitada, operacionalizam o PICOC a partir do próprio tema/RQs e aplicam uma rubrica QA explicitamente identificada como operacional, sem atribuí-la indevidamente a um template ausente.

## Tabela A — Identificação e PICOC

| Campo | Extração / julgamento | Base no artigo |
|---|---|---|
| ID | P123 | Capa, p. 1 |
| Título | *An adaptive agentic AI framework for counterfactual validation and adversarial lookahead in automated incident response* | p. 1 |
| Autores | Sheetal Prasad Kizhakel; Sagar Dhanraj Pande | p. 1 |
| Ano / veículo | 2026; *Discover Artificial Intelligence*, vol. 6, artigo 970 | p. 1 |
| DOI | 10.1007/s44163-026-02058-6 | p. 1 |
| Natureza | Estudo primário, proposta arquitetural e avaliação experimental com dados públicos | §§ 3–5, pp. 8–24 |
| **Population** | Sistemas de resposta a incidentes cibernéticos, SOC/SOAR, ambientes corporativos com ataques APT multietapa; analistas humanos como supervisores | §§ 1, 3–4, pp. 2–16 |
| **Intervention** | CIPHER-A: planejamento por LLM, validação contrafactual antes de cada ação, simulação adaptativa do atacante, execução e auditoria em ciclo fechado | §§ 1.1, 4.1–4.6, pp. 3, 10–16 |
| **Comparison** | **Sim, executada**: SOAR baseado em regras, LLM-SOAR e CIPHER-static em avaliação interna de 143 incidentes; os resultados atribuídos a Liu e Babar foram estimados pelos autores do P123 e **não** devem ser classificados como replicações diretas | §§ 5, 5.1–5.4, pp. 16–23 |
| **Outcomes** | RPDR, False Safety Rate (FSR), Escalation Accuracy (EA), Mean Time to Contain (MTTC), precisão da previsão adversarial e da previsão de dano colateral; não há medição direta de MTTD, MTTR ou carga cognitiva | §§ 5.1–5.3, pp. 17–21 |
| **Context** | Operações de segurança e resposta automatizada a incidentes em cenário experimental com DARPA OPTC, CTU-13 e base MITRE ATT&CK; protótipo executado em host com GPU A100 | §§ 3, 4.6, 5.6, pp. 9, 15–16, 24–25 |
| Bibliometria fornecida | OpenAlex: 0; Crossref: 0; Scopus: **não indexado**, segundo triagem de 27/10/2026. Não agregar contagens entre fontes | `prompt-P123.md` |
| Estrato informado | **Qualis A3**, derivado de percentil Scopus 67%, conforme triagem fornecida; SJR N/D. Há aparente tensão entre “Scopus não indexado” para o estudo e o percentil do veículo; preservar os dois dados como declarados e não inferir indexação do artigo | `prompt-P123.md` |
| Regra de estrato | **PDR-0007:** ressalva de estrato obrigatória em todo uso da evidência, pois A3 está fora de A1–A2. PDR-0006 trata de *conference papers* e não é o gatilho principal deste artigo de periódico | `prompt-P123.md` |
| Elegibilidade temática | **Sim.** Estudo diretamente conectado a agentes com autonomia condicionada, arquitetura de execução, segurança e métricas de incident response | §§ 1, 4–5 |

## Tabela B — Atendimento às questões de pesquisa

**Escala:** T = 1,0 (atende diretamente); P = 0,5 (atende parcialmente); N = 0,0 (não atende).

| RQ | Nota | Evidência âncora (seção/página) | Fundamentação crítica |
|---|---:|---|---|
| **RQ1 — Capacidades, autonomia e decisão** | **T (1,0)** | §§ 1.1, 4.1–4.5, pp. 3, 10–15 | Planejador LLM, contexto persistido, ferramentas de execução e roteamento por risco `EXECUTE`, `MODIFY/HOLD`, `ESCALATE`; supervisão humana seletiva. Demonstra autonomia condicionada, não autonomia irrestrita. |
| **RQ2 — Engenharia e arquitetura** | **T (1,0)** | §§ 4.2–4.6, pp. 11–16; Tabelas 3–4 e Figuras 1–2, pp. 13–15 | LangGraph com estado tipado, Wazuh, Claude 3 Sonnet, Mistral-7B, MITRE ATT&CK, APIs CrowdStrike/AWS/AD e trilha PostgreSQL. Inclui guardrail de risco, auditoria e replanejamento. Operação produtiva em escala não foi validada. |
| **RQ3 — Benefícios e métricas** | **T (1,0)** | §§ 5.1–5.3, pp. 17–21; Tabelas 5–8 | RPDR 38,2% → 15,6% frente ao CIPHER-static (redução relativa de 59,2%); FSR 22,7% → 3,2% versus SOAR; EA 91,7%; MTTC 14,3 → 8,9 min (37,8% relatados). Há avaliação controlada e Wilcoxon p<0,001, mas **não** avaliação direta de carga cognitiva, MTTD ou MTTR. |
| **RQ4 — Riscos, robustez e governança** | **T (1,0)** | §§ 4.1–4.5, 5.2–5.6, pp. 10–15, 18–25 | Formaliza risco de ação, severidade, blast radius, reversibilidade, ações de contenção equivocadas, supervisão humana, auditabilidade e limitações de concorrência/contexto. Não oferece avaliação ampla de privacidade, conformidade ou accountability institucional. |
| **RQ5 — Lacunas e pesquisa futura** | **T (1,0)** | §§ 2.2, 5.4–5.6, 7, pp. 7–8, 21–25 | Identifica lacunas em validação pré-execução e replanejamento após adaptação do adversário; propõe grafos de dependência, cooperação federada, modelos causais formais e necessidade de validar escalabilidade. |
| **Total** | **5,0/5,0 — Alta** | | Aderência ampla às cinco RQs. Esta pontuação indica pertinência informacional, não prova de elevada validade externa. |

## Tabela C — Qualidade metodológica (rubrica operacional)

**Advertência metodológica:** Como o prompt não descreve o enunciado dos itens QA1–QA4, as perguntas abaixo são critérios operacionais de avaliação, a confirmar no protocolo da RSL. **Escala:** Y = 1,0; P = 0,5; N = 0,0.

| QA | Critério operacional adotado | Nota | Justificativa com âncora |
|---|---|---:|---|
| **QA1** | Objetivo e método claramente descritos? | **Y (1,0)** | Problema, contribuições, equações, pipeline, componentes e implementação documentados, §§ 1.1 e 4, pp. 3, 10–16. |
| **QA2** | Dados, comparadores e avaliação adequadamente especificados? | **P (0,5)** | Informa 143 incidentes, 3 cenários, conjuntos DARPA/CTU-13 e baselines internos; porém comparadores externos são estimados a partir de publicações e não reexecutados, §§ 3 e 5.4, pp. 9, 21–23. |
| **QA3** | Resultados são quantificados e analisados com suporte estatístico? | **P (0,5)** | Médias, desvios, ICs, ablação, sensibilidade e Wilcoxon são reportados, §§ 5.1–5.5, pp. 17–24. Contudo, há inconsistência em tempo de pipeline na Tabela 5 e limitações de reprodutibilidade dos comparadores externos. |
| **QA4** | Limitações, validade externa e reprodução são suficientemente tratadas? | **P (0,5)** | Reconhece estimativas externas e ausência de teste de concorrência; disponibiliza fontes dos datasets, mas não identifica pacote reprodutível do código experimental, parâmetros e traces de execução, §§ 5.4, 5.6, p. 25. |
| **Total** | | **2,5/4,0 — Média** | Qualidade metodológica aproveitável sob leitura crítica, não evidência conclusiva de resultados de produção. |

## Síntese das evidências extraídas

| Medida | CIPHER-A | Comparador | Leitura apropriada |
|---|---:|---:|---|
| RPDR médio | **15,6% ± 3,1** | CIPHER-static **38,2% ± 6,6** | Redução relativa **59,2%** com adição do ASA; comparação interna por ablação, Tabela 6, p. 17 |
| FSR | **3,2% ± 1,1** | SOAR **22,7% ± 4,2** | Menos decisões executadas e posteriormente revertidas, Tabela 7, p. 19 |
| Acurácia da escalada (EA) | **91,7% ± 3,2** | CIPHER-static **74,2% ± 5,4** | Efetividade do encaminhamento a analistas, Tabela 7, p. 19 |
| MTTC | **8,9 ± 1,4 min** | SOAR **14,3 ± 2,1 min** | Redução relatada de **37,8%**, Tabelas 5 e 7, pp. 16, 19; verificar decomposição temporal |
| Predição de dano colateral | **94,3%**, IC95% [92,5%; 95,6%] | CIPHER-static **61,2%** | 847 testes CTU-13, § 5.3, pp. 20–21 |
| Validação RPDR frente a logs red team | **97,2%** de concordância relatada | logs DARPA OPTC | Evidência complementar de consistência da métrica, § 4.4, p. 12 |
| Testes estatísticos | Wilcoxon **p < 0,001** | baselines internos e externos nas condições descritas | A tabela não elimina as limitações de construção dos comparadores externos, Tabela 8, p. 20 |

## Análise crítica e riscos de interpretação

1. **Comparação empírica efetiva, mas heterogênea.** A avaliação em 143 incidentes executa as configurações internas SOAR, LLM-SOAR, CIPHER-static e CIPHER-A. Isso satisfaz a exigência de *Comparison* com baseline concreto. Já as métricas atribuídas a Liu [10] e Babar et al. [23] foram reconstruídas pelos autores do P123 a partir de indicadores publicados, e **não** constituem execução independente dos sistemas externos (nota da Tabela 6, § 5.4, pp. 17, 21–23).
2. **Inconsistência aritmética verificável.** A Tabela 4 indica **2,45 segundos por ação**. A Tabela 5 apresenta **7,2 ações por incidente** e registra “**2,1 min (7.2 × 2.45 s)**”. Entretanto, `7,2 × 2,45 s = 17,64 s = 0,294 min`, e não 2,1 min. Assim, a decomposição apresentada para o MTTC de 8,9 minutos requer esclarecimento; **não** se deve recalcular o MTTC completo sem dados adicionais (§§ 4.6–5, pp. 15–16).
3. **Possível tensão entre definição e implementação do roteamento.** A Equação 4 apresenta decisão baseada em `RS`, enquanto o texto e o algoritmo operacional aplicam a decisão ao `CVS`, com diferenças de nomenclatura entre `MODIFY` e `HOLD`. A explicação operacional existe, mas a notação dificulta uma reprodução literal (§§ 4.1–4.5, pp. 10–15).
4. **Escopo de métricas.** *Mean Time to Contain* (MTTC) não equivale automaticamente a *Mean Time to Recover* (MTTR). O estudo tampouco apresenta mensuração direta de MTTD ou sobrecarga cognitiva. Pode embasar benefícios em contenção e supervisão, mas não uma alegação quantitativa de redução de MTTD/MTTR ou carga cognitiva.
5. **Validade externa limitada.** A avaliação envolve traces históricos, três cenários APT, um host A100 e nenhum teste experimental de alta concorrência; o próprio artigo adverte contra extrapolar os 8,9 minutos a implantações maiores (§ 5.6, pp. 24–25). Conectividade com APIs operacionais, por si só, não comprova validação em produção organizacional real.
6. **Risco de circularidade/calibração.** Pesos e limiares foram selecionados por otimização sobre recortes do DARPA OPTC (§§ 4.1–4.2, pp. 10–11). Embora o artigo relate validação por logs independentes do adversário (§ 4.4, p. 12), é preciso verificar separação entre ajuste, seleção de limiares e avaliação final, antes de generalizar as taxas observadas.
7. **Ressalva bibliométrica vinculante.** **Qualis A3** informado na triagem é inferior ao intervalo A1–A2; toda reutilização deste artigo na síntese de evidências deve indicar **RESSALVA DE ESTRATO OBRIGATÓRIA (PDR-0007)**. Contagens de citações OpenAlex e Crossref permanecem 0 na data informada, sem agregação.

## Contribuição para a RSL

O estudo é especialmente útil como **evidência arquitetural e experimental condicionada** sobre segurança de ações agênticas: validação pré-execução, antecipação de consequências, atualização de estado adversarial, replanejamento sequencial, supervisão humana seletiva e persistência de trilhas de auditoria. As métricas RPDR, FSR, EA e MTTC oferecem instrumentos analíticos que podem orientar um protocolo de avaliação de copilotos para resposta a incidentes. Para trabalhos concentrados em confiabilidade/SRE, a transferência deve ser justificada: a avaliação original trata de incidentes de **cibersegurança**, não diretamente de indisponibilidade de serviços e restauração de SLOs.

**Extrações recomendadas para a matriz da RSL:** arquitetura do ciclo fechado (Figuras 1–2, pp. 13–14); componentes (Tabela 3, p. 15); orçamento de inferência (Tabela 4, p. 15); métricas e ablação (Tabelas 5–8, pp. 16–20); limitações (5.4–5.6, pp. 21–25). Registrar a procedência de cada comparador antes de sintetizar efeitos.

## Recomendação final

**Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA: Qualis A3, PDR-0007; resultados de baselines externos são estimativas indicativas não reexecutadas; inconsistência aritmética na decomposição do MTTC; ausência de medição direta de MTTD, MTTR, carga cognitiva e validação de escala produtiva).**

**Classificação:** elegibilidade temática **SIM**; *Comparison* **SIM** para baselines internos; aderência às RQs **5,0/5,0, Alta**; qualidade metodológica pela rubrica operacional **2,5/4,0, Média**. Este parecer não substitui eventual avaliação com as definições formais de QA e o arquivo `templates/review.md`, que não foram anexados.
