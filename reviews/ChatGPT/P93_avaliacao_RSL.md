# Parecer de avaliação integral — P93

**Estudo:** Wahed, Mutaz Abdel; Aljawarneh, Nader Mohammad. *From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures*. **Journal of Information & Knowledge Management**, v. 25, n. 9, artigo 2650039, 2026. DOI: 10.1142/S0219649226500395.

**Decisão proposta:** **Incluir c/ ressalvas (Qualis A3, PDR-0007; avaliação exclusivamente simulada; inconsistências quantitativas; evidência insuficiente de redução real de carga cognitiva).**

> **Limites de aplicação do protocolo.** O arquivo `prompt-P93.md` menciona um “PICOC abaixo”, mas não contém a definição formal dos cinco elementos; também não fornece os enunciados de QA1–QA4 nem o arquivo `templates/review.md`. Assim, a matriz PICOC abaixo é **descritiva, não uma verificação normativa definitiva de elegibilidade**; os critérios QA são **operacionalizações provisórias e explicitadas**, não substitutos silenciosos dos critérios oficiais. A recomendação é, portanto, **provisória**, sujeita à conferência desses elementos do protocolo.

## Tabela A — Identificação, bibliometria e PICOC

| Campo | Registro fundamentado |
|---|---|
| Identificador | P93 |
| Título | From Manual to Agentic Security Operations: A Multi-Dimensional Evaluation of AI-Driven SOC Architectures |
| Autores | Mutaz Abdel Wahed; Nader Mohammad Aljawarneh |
| Ano / periódico | 2026; *Journal of Information & Knowledge Management*, 25(9), 2650039 |
| DOI | 10.1142/S0219649226500395 |
| Tipo | Artigo de periódico; avaliação comparativa com simulação e discussão sociotécnica |
| Publicação | Recebido 23 jan. 2026; aceito 1 mar. 2026; publicado 22 jun. 2026 (p. 1) |
| P — Population | Operações de Security Operations Centers (SOC), analistas de segurança e processos de resposta a incidentes; ambiente corporativo modelado de médio/grande porte (seção 3, pp. 8–10). **Aderência temática aparente; PICOC oficial ausente.** |
| I — Intervention | SOC aprimorado com IA agêntica: percepção de telemetria, raciocínio contextual, orquestração, execução de remediações e supervisão humana (seção 3, pp. 10–11). |
| C — Comparison | **Sim.** SOC tradicional centrado em analistas, SIEM e triagem manual versus SOC com agentes, sob fontes de alertas e distribuições comparáveis, por 90 dias simulados (seção 3, pp. 6, 8–10; Tabelas 3 e 9). É comparação executada contra baseline concreto **dentro do modelo sintético**, não comparação de implantação real. |
| O — Outcomes | MTTD, MTTR (definido como Mean Time to Respond no artigo), falsos positivos, sucesso de remediação, escalonamento, alertas por analista e indicadores/proxies de experiência (seções 3–4, pp. 11–22). |
| C — Context | Cibersegurança corporativa/SOC; incident response; telemetria SIEM, EDR e sensores de rede; simulação, **não produção** (pp. 8–11). |
| Janela e amostra | 90 dias operacionais sintéticos; 5.571 observações de alertas declaradas no SEM e na matriz de confusão (pp. 8, 11, 22). |
| OpenAlex | 0 citações, conforme metadados fornecidos no prompt, conferidos em 27 out. 2026 |
| Crossref | 0 citações, conforme prompt, em 27 out. 2026 |
| Scopus | 0 citações, conforme prompt, em 27 out. 2026 |
| Qualis informado | **A3**, derivado do percentil Scopus de 65% segundo o protocolo informado; não revalidado independentemente neste parecer |
| SJR | N/D, conforme prompt |
| PDR-0006 | Não aplicável: publicação em periódico, não em série de proceedings |
| PDR-0007 | **Aplicável: RESSALVA DE ESTRATO OBRIGATÓRIA** em qualquer uso da evidência (A3, fora de A1–A2) |
| Elegibilidade temática | **Potencialmente elegível**, mas a conclusão normativa depende do texto PICOC oficial ausente do prompt. |

## Delineamento e resultados extraídos

A avaliação compara dois cenários modelados, usando a mesma base de telemetria sintética e distribuições de alertas. O framework **3E** estrutura *Efficiency* (latências), *Effectiveness* (qualidade da detecção e remediação) e *Experience* (intervenção, carga operacional e governança). A arquitetura proposta dispõe de camadas de percepção, raciocínio, orquestração/ação e supervisão humana (Fig. 3, p. 11). A Fig. 3 apresenta, porém, **duas caixas com o mesmo rótulo “Action & Orchestration Layer”**, o que reduz a clareza da decomposição arquitetural.

| Indicador | SOC tradicional | SOC agêntico | Local | Leitura crítica |
|---|---:|---:|---|---|
| MTTD | 6–12 h | 30–90 min | Tabela 3, p. 14 | Redução de **75% declarada**, baseada na simulação; não diretamente conciliável com a Tabela 9 |
| MTTR | 12–24 h | 2–6 h | Tabela 3, p. 14 | Redução de **80% declarada**; artigo define MTTR como tempo entre detecção e fechamento (p. 12) |
| Falsos positivos | 35–45% | 10–15% | Tabela 3, p. 14 | Redução de **65% declarada**; medida distinta da “False-Positive Reduction Rate” na Tabela 9 |
| Alertas por analista | >500/dia | 120–150/dia | Tabela 3, p. 14; texto p. 15 | Redução de **70% declarada**; não concilia com índice de alertas/turno da Tabela 9 |
| MTTD | 18,2 min | 10,2 min | Tabela 9, p. 20 | Redução de 44% declarada, **outra escala** |
| MTTR | 32,5 min | 17,2 min | Tabela 9, p. 20 | Redução de 47% declarada, **outra escala** |
| Analyst Workload Index | 35 alertas/turno | 20 alertas/turno | Tabela 9, p. 20 | Redução de 43% declarada, operacionalização distinta da Tabela 3 |
| Fadiga cognitiva | 7,2/10 | 5,0/10 | Tabela 9, p. 20 | Índice de natureza simulada/proxy; **sem mensuração direta com participantes** |
| Confusão de classificação | — | TP=1.240; TN=4.056; FP=180; FN=95 | Fig. 10, p. 23; texto p. 22 | Precision ≈87,3%; recall ≈92,9%; F1≈90,0%; accuracy≈95,1%, computados da matriz sintética |
| Contenção em ataque simulado *zero-day* | 42 min | 9 min | Tabela 10, p. 21 | Diferença equivalente a **78,6%**, embora a tabela informe 76% na linha de total e 79% na linha de contenção |

**Advertência metodológica central:** os percentuais apresentados no artigo são resultados de um cenário sintético parametrizado com normas da literatura e da indústria. Não equivalem a efeito causal estabelecido em SOC de produção, e a descrição não fornece elementos suficientes para reprodução integral da geração de dados e das políticas dos agentes.

## Tabela B — Aderência às questões de pesquisa da RSL

Escala do prompt: **T = 1,0; P = 0,5; N = 0,0**. As questões abaixo são as da RSL, **não** as RQ1–RQ4 internas do artigo.

| RQ da RSL | Nota | Evidência âncora | Justificativa e limite |
|---|---:|---|---|
| **RQ1 — Capacidades e autonomia** | **P (0,5)** | Seção 2, p. 5; seção 3, pp. 10–11; Fig. 3, p. 11; seção 4, p. 17 | Descreve raciocínio contextual, planejamento, feedback, decisão limitada e supervisão humana. Não especifica mecanismo de memória persistente, níveis formais de autonomia ou implementação detalhada de ferramentas. |
| **RQ2 — Engenharia/arquitetura** | **P (0,5)** | Seção 3, pp. 10–11; Fig. 3, p. 11; Tabela 6, p. 15 | Identifica camadas de percepção, raciocínio, orquestração, remediação, SIEM/EDR/SOAR e aprovação humana. É arquitetura **conceitual/modelada**; não demonstra pipeline produtivo, guardrails detalhados, gestão de estado/memória, observabilidade do próprio agente ou requisitos de implantação. |
| **RQ3 — Benefícios e métricas** | **T (1,0)** | Seção 3, pp. 11–12; Tabelas 3–5, pp. 14–15; Tabela 9, p. 20; Fig. 10, p. 23 | Apresenta baseline, comparação executada e métricas de detecção, resposta, falsos positivos, remediação e carga operacional. **Aderência temática total não implica qualidade probatória alta**: simulação e divergência entre tabelas reduzem a confiabilidade. |
| **RQ4 — Riscos, ética e governança** | **T (1,0)** | Seção 4, pp. 16–18; seção 5, pp. 24–25; seção 6, pp. 25–26 | Discute autonomia limitada, checkpoints humanos para incidentes de alto impacto, confiança, accountability e restrições organizacionais. Modelos de ameaça e verificação de segurança são pouco detalhados, mas o tema é abordado expressamente. |
| **RQ5 — Lacunas e agenda** | **P (0,5)** | Seção 2, pp. 4–5; seção 3, p. 8; seção 6, p. 26 | Reconhece escassez de avaliações de autonomia, limitações da telemetria sintética e necessidade de explicabilidade, estudos longitudinais e melhor controle humano. Não oferece agenda sistemática de benchmarking, segurança e ameaças. |
| **Total** | **3,5/5,0** | | **Banda Alta** (≥3,0) para **relevância/cobertura temática** conforme a escala fornecida. |

## Tabela C — Qualidade metodológica (QA1–QA4)

**Importante:** o prompt especifica apenas os identificadores QA1–QA4, sem seus enunciados. Para não atribuir ao protocolo definições inexistentes, os itens abaixo são **critérios provisórios de leitura crítica**, a serem recalculados quando fornecida a rubrica oficial. Escala Y/P/N = 1,0/0,5/0,0.

| Critério provisório | Nota | Evidência e julgamento |
|---|---:|---|
| **QA1 — Objetivos e perguntas claros?** | **Y (1,0)** | Seção 1, pp. 3–4: quatro RQs internas; Tabela 1, p. 7: mapeamento das dimensões 3E às métricas. |
| **QA2 — Método e baseline descritos adequadamente?** | **P (0,5)** | Seção 3, pp. 6–12: duas condições de SOC, 90 dias, telemetria sintética e métricas definidas. Falta especificação suficiente do gerador, parâmetros, código e replicações para auditoria independente. |
| **QA3 — Resultados internamente consistentes e verificáveis?** | **N (0,0)** | Tabelas 3 e 9, pp. 14 e 20: escalas incompatíveis para MTTD, MTTR e carga operacional. Tabela 10, p. 21: 42→9 min representa 78,6%, não 76%. Não é possível reconciliar agregações pela descrição disponível. |
| **QA4 — Limitações, validade e inferência tratadas?** | **P (0,5)** | Seção 3, pp. 8–10, reconhece limitações da síntese de telemetria e ausência de levantamento com analistas, mas o texto associa proxies a fadiga e confiança e expressa conclusões mais fortes que o desenho permite. |
| **Total provisório** | **2,0/4,0** | Pontuação **não normativa**; banda “Média” apenas se a régua do prompt também for aplicada aos QAs. |

## Avaliação crítica de validade

### Pontos fortes

1. **Comparison efetivo dentro da simulação:** definição explícita de baseline tradicional e condição assistida por agentes, com janelas e distribuições de alertas harmonizadas (seção 3, pp. 6, 8–10).
2. **Métricas operacionais pertinentes:** MTTD, MTTR, FPR, escalonamento e sucesso de remediação são operacionalizados (p. 12), com resultados comparativos e matriz de confusão (pp. 14–23).
3. **Perspectiva sociotécnica 3E:** integra desempenho técnico, experiência operacional e governança, útil para formular dimensões de avaliação de copilotos em resposta a incidentes (pp. 3–7).
4. **Supervisão humana:** propõe pontos de aprovação e escalonamento para cenários críticos e ambíguos (Fig. 3, p. 11; pp. 16–17).

### Fragilidades e riscos de viés

1. **Validade externa limitada:** telemetria inteiramente sintética e interações de trabalho modeladas, sem implantação longitudinal observada nem entrevistas/questionários de analistas (pp. 8–10).
2. **Inconsistência entre métricas:** Tabela 3 apresenta tempos e carga de trabalho em ordens de grandeza distintas da Tabela 9 (pp. 14, 20). Não é apropriado consolidar essas séries, calcular um efeito global ou escolher a cifra mais favorável.
3. **Redução de carga cognitiva não demonstrada diretamente:** a metodologia afirma que a dimensão Experience usa proxies operacionais, sem participantes reais (pp. 6, 10). A Tabela 9, contudo, apresenta *Cognitive Fatigue Score* e *Trust-in-AI Perception Score* sem evidência de mensuração direta correspondente (p. 20).
4. **Descrição incompleta para replicação:** faltam detalhes sobre agentes, política de decisão, configuração de classificadores, parametrização e dados/código para reprodução independente (seção 3, pp. 8–12).
5. **Inconsistências aritméticas/rotulagem:** o tempo de 42 para 9 min equivale a redução de aproximadamente 78,6%, e não 76%; a Tabela 10 apresenta ambos 79% e 76% para essa comparação (p. 21). A Tabela 6 (p. 15) rotula categorias de ações, apesar do título “Analyst workload comparison”.
6. **SEM e extrapolação:** há PLS-SEM e coeficientes na Tabela 8 (pp. 11, 20), mas suporte estatístico em dados simulados não estabelece por si só efeitos na operação real ou validade de construtos humanos.

## Síntese para extração na RSL

**Contribuição mais relevante:** framework 3E para avaliar a transição entre SOC manual/centrado no analista e SOC agêntico, com métricas operacionais, comparação contra baseline sintético e autonomia limitada por supervisão humana.

**Uso recomendado:** evidência **exploratória/modelada** para RQ1, RQ2, RQ4 e RQ5; fonte de métricas e de hipótese quantitativa para RQ3. Registrar os valores numéricos como **“reportados pelos autores sob simulação”**, mantendo Tabelas 3 e 9 separadas; evitar afirmar que houve redução validada de MTTD/MTTR ou da carga cognitiva em produção.

**Ponte com resposta a incidentes operacionais:** o desenho 3E, a comparação com baseline e a definição de *human oversight* são transferíveis como ideias de avaliação de copilotos em incidentes de TI/SRE; **não** há validação empírica dessa transferência do domínio SOC de cibersegurança para SRE.

**Questão pendente do protocolo:** conferir PICOC oficial, a definição original de QA1–QA4 e o template `templates/review.md` antes de considerar esta classificação definitiva.

## Recomendação final

**Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA: Qualis A3, PDR-0007; telemetria e interações simuladas sem validação em produção; discrepâncias de MTTD/MTTR e carga operacional entre as Tabelas 3 e 9; medidas de experiência/carga cognitiva não aferidas diretamente; confirmação normativa condicionada ao PICOC e QA oficiais ausentes).**
