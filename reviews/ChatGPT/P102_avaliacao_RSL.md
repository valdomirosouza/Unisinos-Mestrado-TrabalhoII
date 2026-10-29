# Parecer de avaliação integral — P102

**Protocolo:** RSL em Engenharia de Software, diretrizes de Kitchenham (2009), conforme `prompt-P102.md`.  
**Estudo:** Kataria, V. (2025). *Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination*. *International Journal of Intelligent Engineering and Systems*, 18(11), pp. 450–466. DOI: 10.22266/ijies2025.1231.28.  
**Natureza do estudo:** Proposta arquitetural com avaliação experimental e baseline humano.  
**Decisão:** **Incluir c/ ressalvas (estrato não indexado, PDR-0007; limites de validade e escopo das métricas).**

## 1. Tabela A — Identificação, PICOC e elegibilidade

| Dimensão | Extração | Decisão / evidência âncora |
|---|---|---|
| Identificação | P102; Vipin Kataria; 2025; *International Journal of Intelligent Engineering and Systems*, v. 18, n. 11; DOI 10.22266/ijies2025.1231.28 | Capa, p. 450 |
| Tipo | Artigo de periódico; arquitetura multiagente com validação experimental | §§ 3–4, pp. 453–462 |
| **P — Population** | Engenheiros SRE e sistemas distribuídos de microsserviços; sete serviços IoT e ambiente de réplica de produção com mais de 50 | Atende; §§ 1, 4.1, pp. 450, 457 |
| **I — Intervention** | Master LLM Agent que planeja e orquestra cinco agentes especializados (logs, métricas, traces, infraestrutura e ML), com MCP, memória contextual, ferramentas e recomendações | Atende; §§ 3.1–3.8, pp. 453–457 |
| **C — Comparison** | Diagnóstico manual realizado paralelamente por três engenheiros SRE seniores com mais de cinco anos de experiência; referência de 67,3% de acurácia e 47,2 min para diagnóstico | **Atende com comparação empírica executada**, não meramente proposta; § 4.1.3 e Tabela 4, p. 459 |
| **O — Outcomes** | Acurácia de causa raiz, tempo médio de diagnóstico, correspondência com incidentes históricos, falsos positivos, completude e desempenho dos agentes | Atende; Tabelas 4–7, pp. 459–461 |
| **C — Context** | Incident response e análise diagnóstica em infraestrutura cloud-native e microsserviços; chaos engineering e observabilidade operacional | Atende; §§ 3–4, pp. 453–462 |
| Qualis / estrato | **NÃO INDEXADO**, conforme metadados fornecidos no protocolo: periódico sem CiteScore Scopus para aferição do estrato | **Ressalva de estrato obrigatória, PDR-0007**. Não converter em A1/A2 nem excluir automaticamente |
| PDR-0006 | Regra para séries de proceedings de congressos | **Não aplicável**, pois P102 é artigo de periódico |
| Citações por fonte | OpenAlex: 0; Crossref: 0; Scopus: 2 (verificação informada em 27/10/2026) | Manter separadas, sem agregação |
| SJR | N/D segundo insumos do protocolo | Sem inferência de estrato |
| Triagem temática | Alinhamento direto com Agentic AI, SRE, análise de incidentes, causa raiz, cooperação homem–IA e métricas temporais | **Elegível pelo PICOC** |

**Nota de escopo:** O prompt não traz uma tabela PICOC separada com critérios formais adicionais. A correspondência acima operacionaliza P/I/C/O/C a partir das cinco questões de pesquisa e dos dados explicitamente fornecidos, sem introduzir limiares novos de elegibilidade.

## 2. Tabela B — Cobertura das questões de pesquisa

**Escala:** T = 1,0 (atende de modo substancial); P = 0,5 (parcial); N = 0 (não atende).

| RQ | Nota | Evidência âncora (seção/página) | Fundamentação crítica |
|---|---:|---|---|
| **RQ1 — Contexto, capacidades e autonomia** | **T (1,0)** | §§ 3.1–3.3, pp. 453–455; §§ 3.5, 3.7–3.8, pp. 455–457 | Master Agent planeja, seleciona ferramentas/agentes, faz introspecção, correlaciona evidências e usa memória/contexto. Define modo consultivo read-only por padrão e escalonamento com aprovação humana para P0/P1. Diferencia apoio decisório de execução autônoma irrestrita. Não oferece taxonomia formal abrangente de níveis de autonomia. |
| **RQ2 — Engenharia e arquitetura** | **T (1,0)** | §§ 3.1–3.8, pp. 453–457; Fig. 1, p. 454 | Quatro camadas; cinco agentes especializados; MCP; Elasticsearch, Prometheus, Jaeger, PostgreSQL; 2–10 réplicas em Kubernetes; circuit breakers, timeouts, retry, logs, métricas, health checks; validação cruzada, grounding e controles de segurança. Descreve arquitetura de implantação, sem disponibilizar artefato reproduzível suficiente no artigo. |
| **RQ3 — Benefícios e métricas** | **T (1,0)** | § 4.1.3, Tabelas 4–6, pp. 459–460; Tabela 7, p. 461; § 5.1, p. 463 | Comparação executada com SREs: acurácia 67,3% → 92,1% no testbed principal e 89,4% no estendido; tempo de diagnóstico 47,2 → 8,5 e 11,2 min; matching histórico 43,1% → 96,3% e 93,7%; falsos positivos 28,7% → 4,2% e 6,8%. **Não equivale a provar menor MTTR completo ou menor carga cognitiva.** |
| **RQ4 — Riscos, ética e governança** | **T (1,0)** | §§ 3.8.1–3.8.5, p. 457; §§ 5.2–5.4, p. 463 | Alucinações, prompt injection, vazamento de dados, não determinismo, escalabilidade; scores de confiança, exigência de três agentes para conclusões de alta confiança, sanitização, rate limiting, aprovação humana P0/P1, auditoria, rollback, fallback e criptografia. Riscos nomeados e controles descritos, mas sem benchmark adversarial próprio. |
| **RQ5 — Lacunas e pesquisa futura** | **T (1,0)** | §§ 5.2–5.4, p. 463 | Sugere formalização matemática da coordenação, extensão para 100+ microsserviços, avaliação de segurança adversarial e alucinações, predição de incidentes e aprendizado federado preservando privacidade. Lacunas explícitas, embora sem desenho experimental detalhado para todos os tópicos. |
| **TOTAL** | **5,0 / 5,0** | | **Cobertura Alta (≥ 3,0)** |

## 3. Tabela C — Avaliação de qualidade metodológica

**Observação:** O arquivo `prompt-P102.md` exige QA1–QA4 e escala Y/P/N, mas **não define o texto dos quatro critérios**. Para evitar atribuir ao protocolo critérios inexistentes, utiliza-se abaixo uma operacionalização analítica explícita e provisória: clareza do estudo, adequação metodológica, solidez dos resultados e limitações/reprodutibilidade. Se houver rubrica oficial distinta em `templates/review.md`, esta tabela deve ser remapeada antes da consolidação entre estudos.

| QA | Critério operacional utilizado | Nota | Justificativa e evidência |
|---|---|---:|---|
| **QA1** | Objetivo, contexto e arquitetura claramente definidos | **Y (1,0)** | Problema, proposta, funções de cada agente e fluxo de investigação são descritos em §§ 1 e 3, pp. 450–457, com diagrama de arquitetura na p. 454. |
| **QA2** | Desenho experimental e comparação apropriados | **Y (1,0)** | Dois testbeds; 150 + 200 cenários injetados; ferramentas de chaos engineering e categorias de falha; baseline manual de três SREs; §§ 4.1–4.1.3, pp. 457–459. Há, contudo, limitação de representatividade por serem ambientes controlados/staging. |
| **QA3** | Resultados quantitativos suficientes e transparentes para fundamentar as conclusões | **P (0,5)** | Tabelas 4–9 informam várias métricas por ambiente, categoria e modelo, pp. 459–462. Não ficam claros intervalos de confiança, testes estatísticos, dispersão e disponibilização de dados por incidente. Há inconsistência de apresentação entre redução de 82% no ambiente principal e 79,1% agregada nas tabelas/texto, que precisa ser contextualizada. |
| **QA4** | Limitações e condições de reprodução/generalização explicitadas | **P (0,5)** | § 5.2–5.4, p. 463 reconhece queda de desempenho, dificuldades com dependências externas e lacuna de formalização. Não há validação em operação real independente nem informação completa sobre datasets, prompts, código e custos operacionais que permita reprodução rigorosa. |
| **TOTAL** | | **3,0 / 4,0** | **Qualidade Alta segundo bandas fornecidas**, sujeita à rubrica QA oficial não anexada. |

## 4. Síntese dos resultados empíricos

| Indicador | Baseline manual | Testbed primário (7 serviços) | Validação estendida (50+ serviços) |
|---|---:|---:|---:|
| Acurácia da causa raiz | 67,3% | 92,1% | 89,4% |
| Tempo médio de diagnóstico | 47,2 min | 8,5 min | 11,2 min |
| Precisão do matching histórico | 43,1% | 96,3% | 93,7% |
| Taxa de falsos positivos | 28,7% | 4,2% | 6,8% |
| Completude da investigação | 72,4% | 94,7% | 91,8% |

*Fonte: Tabela 4, p. 459. Valores conforme reportados pelo artigo; não interpretados como replicação independente.*

**Interpretação dos percentuais:** A redução de 47,2 para 8,5 minutos é de aproximadamente **82,0%**, específica do testbed principal. A redução para 11,2 minutos é de aproximadamente **76,3%**, específica do ambiente estendido. O valor de **79,1%** apresentado na Tabela 4 corresponde aproximadamente à média simples dessas reduções, não a uma estimativa consolidada com distribuição e ponderação documentadas. A melhoria da acurácia de 67,3% para 92,1% corresponde a **24,8 pontos percentuais** (ou ~36,8% relativos); o artigo apresenta “+34,5% avg” para o conjunto dos ambientes. Não confundir variação em pontos percentuais com variação relativa.

**Distinção das métricas:** O paper chama de “MTTD” o *Mean Time to Diagnosis*. Nesta revisão, essa sigla deve ser explicitada como **tempo médio de diagnóstico**, para evitar equipará-la ao tradicional *Mean Time to Detect*. O estudo não mede empiricamente tempo até a detecção inicial nem MTTR total, tampouco carga cognitiva via escala, experimento com operadores ou outro instrumento específico.

## 5. Validade da evidência e limitações

1. **Validade interna:** A execução paralela de análise manual por três engenheiros seniores é um baseline concreto. Contudo, faltam detalhes suficientes sobre aleatorização, ordem de casos, cegamento, independência entre julgadores e estatística inferencial. A definição de ground truth por consenso dos mesmos especialistas que compõem o baseline merece esclarecimento metodológico.
2. **Validade externa:** O ambiente estendido é uma **réplica de produção em staging**, não evidência de implantação contínua em produção real. Os 350 cenários são injeções controladas; a aplicação a incidentes orgânicos, múltiplas equipes e ambientes externos permanece aberta.
3. **Segurança:** Os mecanismos de prevenção de prompt injection, auditoria, HITL, rollback e confiança são descritos, mas não há apresentação de testes quantitativos de resistência a ataques nem comparação longitudinal de incidentes de segurança.
4. **Escalabilidade:** Entre 7 e 50+ microsserviços, a acurácia decresce (92,1% → 89,4%) e o diagnóstico aumenta (8,5 → 11,2 min). Traces e ML Services sofrem degradações adicionais (§ 4.1.3, Tabela 6, p. 460).
5. **Custos e reprodutibilidade:** Não são suficientemente reportados consumo de tokens, custo por incidente, impacto de latência e variabilidade em execuções repetidas, nem há pacote de reprodução identificado no texto analisado.
6. **Causalidade arquitetural:** A avaliação compara sistema multiagente contra investigação manual e compara modelos LLM, mas não isola, por ablação, a contribuição específica de cada agente/MCP nem estabelece comparação experimental controlada com uma solução single-agent equivalente.

## 6. Contribuição para a dissertação e uso na síntese

O estudo pode sustentar a discussão de **arquiteturas agentic como copilotos de investigação SRE**, especialmente a correlação de logs, métricas, traces e informações de infraestrutura; seleção adaptativa de agentes; geração de hipótese de causa raiz; controles de autonomia e aprovação humana; e métricas de acurácia e tempo de diagnóstico.

Na síntese quantitativa, registrar os resultados como **relatos dos autores em ambiente experimental controlado**, nunca como ganho esperado universal em produção. É metodologicamente adequado usar o tempo de diagnóstico como resultado correlato à eficiência de resposta a incidentes; é inadequado classificá-lo automaticamente como redução de *Mean Time to Detect*, *Mean Time to Recover/Resolve* ou de carga cognitiva. Para estes desfechos, marcar **não mensurado diretamente**.

Na síntese qualitativa, o papel de copiloto é compatível com o modo consultivo *read-only*, emissão de relatórios e aprovação humana para incidentes críticos. A possibilidade de ações semiautônomas é discutida como evolução condicionada à validação, não como demonstração de remediação autônoma generalizada.

## 7. Parecer final

**Elegibilidade PICOC:** Atende.  
**Comparison:** Sim, comparação empírica executada contra baseline manual de três SREs seniores.  
**Cobertura das RQs:** 5,0/5,0 — **Alta**.  
**Qualidade metodológica (rubrica operacional provisória):** 3,0/4,0 — **Alta**, com limites de validade/reprodutibilidade.  
**Estrato:** **NÃO INDEXADO**, com **RESSALVA DE ESTRATO OBRIGATÓRIA** conforme **PDR-0007**. PDR-0006 não se aplica a periódico.  
**Peso recomendado na RSL:** Evidência experimental relevante para diagnóstico e causa raiz em SRE, com interpretação cautelosa sobre generalização, custo e métricas não aferidas.

### Recomendação

**Incluir c/ ressalvas (PDR-0007: periódico sem estrato indexado, ressalva de estrato obrigatória em todo uso da evidência; validação baseada em testbeds controlados e réplica de produção, sem medição direta de MTTR completo, tempo de detecção ou carga cognitiva).**
