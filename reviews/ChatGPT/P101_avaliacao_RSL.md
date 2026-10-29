# Parecer de avaliação integral — P101

**Estudo:** Özgözler, E.; Varol, A.; Tanrıverdi, İ. (2026). *Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration*. 14th International Symposium on Digital Forensics and Security (ISDFS), IEEE. DOI: `10.1109/ISDFS69419.2026.11458922`.

**Tipo de estudo:** artigo de conferência, proposta arquitetural com avaliação experimental controlada.  
**Extensão examinada:** PDF integral, 5 páginas.  
**Base da avaliação:** prompt-P101.md e artigo integral, sem complementação bibliométrica externa.  
**Decisão:** **Incluir c/ ressalvas (estrato B4 obrigatório, dados sintéticos, limitações de reprodutibilidade e inconsistência de percentuais).**

> **Nota de rastreabilidade normativa.** O prompt menciona um PICOC “abaixo” e um template `templates/review.md`, mas não fornece a formulação formal dos cinco componentes do PICOC nem o conteúdo do template. A Tabela A usa uma operacionalização explicitamente inferida das RQs e do escopo do estudo, **não substituindo** um PICOC institucional previamente aprovado. Da mesma forma, o prompt determina QA1–QA4 e pontuação, mas não informa os enunciados dos quatro critérios; os critérios operacionais usados na Tabela C são identificados como **provisórios**, até cotejo com a rubrica oficial.

## Tabela A — Identificação, elegibilidade e PICOC

| Campo | Extração e julgamento | Evidência |
|---|---|---|
| Código | P101 | Prompt de avaliação |
| Título | Event-Driven Agentic SOC (ED-ASOC): Supervisor-Based LLM Framework for Dynamic Incident Response and SOAR Orchestration | p. 1 |
| Autores | Enes Özgözler; Asaf Varol; İhsan Tanrıverdi | p. 1 |
| Ano / veículo | 2026; 14th International Symposium on Digital Forensics and Security (ISDFS), IEEE | p. 1 |
| DOI | 10.1109/ISDFS69419.2026.11458922 | p. 1 |
| Tipo | Conference paper; arquitetura implementada e avaliada em testbed controlado | Seções III–IV, pp. 2–4 |
| **P — Population / Problem (operacionalização)** | Analistas e sistemas de Security Operations Centers diante de alertas, sobrecarga de triagem e incidentes de segurança | Introdução, p. 1; seção IV, p. 3 |
| **I — Intervention (operacionalização)** | ED-ASOC, agente supervisor baseado em LLM com webhook, RAG, execução de ferramentas SOAR, validações e aprovações HITL | Seção III, pp. 2–3 |
| **C — Comparison** | **Comparação empírica executada: sim.** Polling tradicional e assistente LLM sem execução autônoma (*LLM-Assist*). Não confundir com a comparação conceitual de playbooks da Tabela I. | Seção IV.C; Tabela IV, pp. 3–4 |
| **O — Outcomes (operacionalização)** | Latência de detecção, MTTR definido pelos autores, acurácia de classificação, resolução automática e redução reportada de intervenções Tier-1 | Seção IV.C; Tabela IV, p. 4 |
| **C — Context (operacionalização)** | Resposta a incidentes cibernéticos em SOC empresarial **simulado**, com FortiSIEM, FortiSOAR, VMware e dados sintéticos | Seção IV.A–B, p. 3 |
| Observação de escopo | Incidentes de cibersegurança, não necessariamente incidentes de disponibilidade, SRE ou operações de produção; transferência para SRE deve ser tratada como hipótese | Seções I, III e IV |
| Bases bibliométricas | OpenAlex: 1; Crossref: 1; Scopus: 0 (dados fornecidos, verificados em 27/10/2026; **não somar entre bases**) | Prompt P101 |
| Estrato | **B4**, percentil CiteScore 11% da série ISDFS; SJR não disponível nos insumos | Prompt P101; PDR-0006 |
| Elegibilidade do veículo | Há percentil Scopus da série informado no prompt; portanto não se aplica o motivo de inelegibilidade “série sem CiteScore” do PDR-0006 | Prompt P101 |
| Restrição normativa | **RESSALVA DE ESTRATO OBRIGATÓRIA** em toda utilização de evidência (B4, fora de A1–A2), conforme PDR-0007 | Prompt P101 |
| Julgamento temático | **Aderente** a capacidades agênticas, arquitetura de orquestração e incident response, com contexto de SOC | Seções I–VI |

## Tabela B — Questões de pesquisa e evidências âncora

Legenda: **T = 1,0** (atende diretamente); **P = 0,5** (atende parcialmente); **N = 0,0** (não atende).

| RQ | Avaliação | Pontuação | Evidência âncora (seção/página) | Fundamentação e limites |
|---|---|---:|---|---|
| **RQ1 — Contexto, capacidades e autonomia** | **T** | **1,0** | III.B–E, pp. 2–3; Tabela III, p. 3 | Supervisor executa classificação contextual, priorização por criticidade e síntese de remediação, usa histórico via RAG e ferramentas SOAR. Aprovação graduada: baixo risco automático, médio com notificação/revisão, alto com aprovação explícita. É descrito um único supervisor, não uma arquitetura multiagente já implementada. |
| **RQ2 — Engenharia e arquitetura** | **T** | **1,0** | Figura 1 e III.A–E, pp. 2–3; V.B–C, p. 4 | Camadas de ingestão por webhook, decisão LLM, Chroma DB/RAG, registro de 47 funções SOAR, validação JSON, sanitização, consistência semântica e rollback descrito. Não há demonstração de operação produtiva sustentada, testes detalhados de escalabilidade ou telemetria de observabilidade do próprio agente. |
| **RQ3 — Evidências e benefícios** | **T** | **1,0** | IV.A–C, pp. 3–4; Tabela IV, p. 4 | Experimento sintético com 1.247 eventos e dois baselines concretos. Latência 34,2/33,8/0,85 s; MTTR 258,4/190,4/71,7 s; acurácia 78,4/84,2/91,3%; resolução automática 0/12,3/45,5% (polling/LLM-Assist/ED-ASOC). Redução aproximada de 45% de intervenções Tier-1, **não mensuração direta de carga cognitiva**. |
| **RQ4 — Segurança, governança e responsabilidade** | **T** | **1,0** | III.E e Tabela III, p. 3; V.B e V.D, pp. 4–5 | Governança HITL proporcional ao risco, validação determinística antes de API, logs de rejeição, mitigação de alucinações e reconhecimento de prompt injection. Não há análise sistemática de ameaça, ensaio adversarial detalhado ou indicadores de falso bloqueio e danos de remediação. |
| **RQ5 — Lacunas e futuro** | **T** | **1,0** | V.C–D, pp. 4–5; VI, p. 5 | Os autores propõem hierarquia multiagente, atualização automática de inteligência de ameaças, testes de robustez adversarial, dados reais de SOC e configurações semiautônomas comparativas. Tais itens são **trabalho futuro**, não resultados demonstrados. |
| **Total RQ** | **Alta** | **5,0 / 5,0** | — | Alta cobertura temática não equivale a força empírica alta ou validade externa estabelecida. |

## Tabela C — Qualidade metodológica QA1–QA4

**Importante:** sem os enunciados institucionais de QA1–QA4 no material fornecido, emprega-se a seguinte **rubrica operacional provisória**, com Y = 1,0, P = 0,5 e N = 0,0. As pontuações deverão ser reconciliadas caso a rubrica oficial tenha significados distintos.

| QA provisório | Critério operacional adotado | Avaliação | Pontos | Justificativa / âncora |
|---|---|---|---:|---|
| **QA1** | Objetivo e contribuição claramente definidos | **Y** | **1,0** | Problema de polling, rigidez dos playbooks, proposta ED-ASOC e quatro contribuições identificáveis; Introdução e seção II.D, pp. 1–2. |
| **QA2** | Método e configuração suficientemente descritos | **P** | **0,5** | Produtos, versões, modelo Claude 3.5 Sonnet, Chroma DB, 1.247 eventos, cinco categorias e intensidade Poisson são declarados; faltam artefatos reproduzíveis, prompts, parametrizações, critérios de rotulagem, desenho de amostragem e detalhes de avaliação das baselines; seção IV.A–B, p. 3. |
| **QA3** | Resultados e comparações empíricas suficientemente sustentados | **P** | **0,5** | A Tabela IV apresenta três condições e números comparáveis, porém não informa intervalos de confiança, dispersão, repetição, testes estatísticos ou isolamentos fatoriais da ingestão e execução; há discrepância de redução percentual de latência; seção IV.C e V.A, pp. 3–4. |
| **QA4** | Limitações, riscos e validade externa explicitados | **P** | **0,5** | Limitações de agente único, RAG desatualizado, prompt injection, dataset sintético e baselines adicionais são reconhecidas, mas ainda faltam análise formal de validade, resultados de segurança adversarial e validação em produção; V.B–D, pp. 4–5. |
| **Total QA provisório** | — | **Média** | **2,5 / 4,0** | Não apresentar como pontuação QA oficial sem a definição normativa dos quatro critérios. |

## Extração quantitativa estruturada

### Ambiente e base experimental

- **Testbed:** FortiSIEM 7.1.1 em VMware ESXi; FortiSOAR 7.4.1; conectores de firewall, EDR e Active Directory; 12 segmentos de rede simulados.
- **Agente:** Claude 3.5 Sonnet; latência média de resposta informada de 1,2 s.
- **Conhecimento:** Chroma DB com 2.847 registros históricos e 156 documentos de políticas.
- **Amostra sintética:** 1.247 eventos, distribuídos em brute force (312), phishing (287), lateral movement (198), exfiltração (243), privilege escalation (207); injeção Poisson com λ = 4,2 eventos/min.
- **Automação por risco:** 567 eventos automáticos (45,5%), 412 com notificação (33,0%) e 268 com aprovação (21,5%). Dos 268 casos de alto risco, 23 decisões foram modificadas e 7 rejeitadas pelos analistas.

### Métricas comparativas

| Métrica | Polling | LLM-Assist | ED-ASOC |
|---|---:|---:|---:|
| Latência de detecção | 34,2 s | 33,8 s | 0,85 s |
| MTTR (termo adotado pelos autores) | 258,4 s | 190,4 s | 71,7 s |
| Acurácia de classificação | 78,4% | 84,2% | 91,3% |
| Incidentes resolvidos automaticamente | 0% | 12,3% | 45,5% |

**Comparações calculadas dos valores publicados:** latência −97,5% versus polling; MTTR −72,3% versus polling e −62,3% versus LLM-Assist; acurácia +12,9 pontos percentuais versus polling; auto-resolução +33,2 pontos percentuais versus LLM-Assist. São resultados do **ambiente de teste**, sem evidência de generalização para produção.

## Avaliação crítica e ameaças à validade

1. **Inconsistência numérica interna.** Resumo (p. 1) e seção V.A (p. 4) mencionam redução de **89%** de latência; a seção IV.C, a Tabela IV e a conclusão registram **97,5%**. Com os valores 34,2 s e 0,85 s, a redução é de cerca de 97,5%. Para extração da RSL, priorizar os valores brutos e sinalizar a divergência textual.
2. **Dependência de contexto sintético.** A amostra de 1.247 eventos e 12 segmentos simulados não representa diversidade, sazonalidade, falhas de integração ou consequências de uma operação empresarial real. A generalização dos efeitos é limitada.
3. **Comparação não inteiramente fatorial.** O tratamento ED-ASOC combina webhooks, RAG, autonomia, integrações e governança. Embora o baseline LLM-Assist use o mesmo modelo subjacente, não isola causalmente a contribuição individual de cada componente. A própria discussão solicita baselines intermediários.
4. **Limitações de inferência estatística.** Não são apresentados, no artigo, intervalos de confiança, desvios-padrão, testes de significância ou avaliação interexecuções. Resultados percentuais reportados devem ser tratados como estimativas descritivas.
5. **Cognitive load não mensurada diretamente.** Redução de ~45% de intervenções Tier-1 é um proxy de esforço operacional, não avaliação psicométrica ou observacional da carga cognitiva dos analistas. Não converter em evidência direta de redução de *cognitive overhead*.
6. **Validação de segurança parcial.** A seção V.B anuncia redução de 94% de alucinações, mas não especifica baseline, tamanho de amostra, protocolo de medição ou incerteza para essa métrica. Guardrails e rollback são descritos arquiteturalmente, não demonstrados por testes completos de falha adversarial.
7. **Escalabilidade não comprovada no mesmo regime.** A seção V.C discute capacidade acima de 10.000 eventos/min e V.D reconhece possível gargalo nesse patamar, enquanto a carga experimental declarada é λ = 4,2 eventos/min. Não interpretar a menção de 10.000 eventos/min como benchmark comprovado.
8. **Terminologia de MTTR.** O artigo utiliza *Mean Time to Response*. Não equiparar automaticamente à métrica SRE *Mean Time to Recovery/Restore* sem redefinir o indicador e seus marcos temporais.
9. **Taxonomia de autonomia.** O Supervisor executa ações sob níveis de risco; os agentes especializados hierárquicos da seção V.C ainda são proposta futura. Não classificar a implementação avaliada como sistema multiagente.
10. **Validade bibliométrica.** O veículo tem estrato B4 segundo os insumos da triagem. Toda citação dos resultados deverá trazer **ressalva de estrato obrigatória** por PDR-0007.

## Síntese interpretativa para a RSL

O P101 oferece evidência pertinente de que uma arquitetura agêntica pode conectar percepção de eventos, raciocínio contextual e ação operacional supervisionada, superando um assistente LLM estritamente consultivo em um *testbed* de segurança. Seu diferencial está na comparação empírica com dois baselines e na separação explícita entre ações automáticas e decisões sujeitas a aprovação humana. A arquitetura combina padrões potencialmente transferíveis para operações SRE, tais como ingestão orientada a eventos, recuperação contextual de conhecimento, interfaces determinísticas de ferramentas e avaliação de risco.

Contudo, os resultados não comprovam redução do tempo de recuperação de serviços SRE nem da carga cognitiva em condições reais. O estudo mede tempos em resposta a eventos cibernéticos, com incidente e mecanismo de resolução próprios de SOC, e usa intervenções evitadas como indicador indireto de esforço. Portanto, deve ser aproveitado como evidência de **viabilidade arquitetural e benefício experimental contextualizado**, não como comprovação de eficácia operacional generalizável.

### Extração recomendada para matriz de evidências

- **Contribuição principal:** arquitetura supervisora orientada a eventos com LLM + RAG + Tool Calling SOAR + HITL por risco.
- **Evidência de comparação:** sim, execução de baselines polling e LLM-Assist no mesmo estudo.
- **Benefícios reportados:** MTTR de resposta 71,7 s; latência 0,85 s; classificação 91,3%; resolução automática 45,5%; intervenções Tier-1 aproximadamente −45%.
- **Natureza da evidência:** experimento controlado sintético; resultados quantitativos descritivos.
- **Validade externa:** limitada; requer replicação em SOC real e análise de transferência para incidentes SRE.
- **Lacunas relevantes:** benchmarking independente, avaliação de carga cognitiva, robustez a prompt injection, validação da governança, ablação arquitetural, escalabilidade e observabilidade da própria operação agêntica.
- **Rastreabilidade:** seção III, pp. 2–3; seção IV, pp. 3–4; seção V, pp. 4–5.

## Pontuação consolidada e recomendação final

| Dimensão | Resultado |
|---|---|
| Aderência temática | Alta |
| RQ1–RQ5 | **5,0 / 5,0 — Alta** |
| QA1–QA4 | **2,5 / 4,0 — Média (rubrica operacional provisória)** |
| Comparison empírico | **Sim** (polling e LLM-Assist) |
| Evidência em produção | **Não** (testbed enterprise simulado) |
| Estrato | **B4**, percentil CiteScore Scopus informado de 11% |
| PDR-0006 | Percentil disponível; estrato aferido a partir da série |
| PDR-0007 | **RESSALVA DE ESTRATO OBRIGATÓRIA** |

**Recomendação final: `Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA — ISDFS B4, conforme PDR-0006/PDR-0007; avaliação em testbed com dados sintéticos; inconsistência entre 89% e 97,5% de redução de latência; ausência de validação produtiva, estatística inferencial e medição direta de carga cognitiva).`**
