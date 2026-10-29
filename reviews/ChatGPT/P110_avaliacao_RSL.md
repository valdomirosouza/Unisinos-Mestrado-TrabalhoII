# Parecer acadêmico P110

**Revisão Sistemática da Literatura (RSL) | PPGCA Unisinos | 29/10/2026**

**Artigo:** *DevAIOps: A Systematic Literature Review on Integrating Explainable AI Agents into CI/CD Pipelines for Optimization, Security, and Auto-Remediation*  
**Autores:** Othmane Ait Ami, Abderrazak Boumahdi e Mohamed Azmi  
**Fonte:** *Procedia Computer Science*, v. 290, pp. 344–351, 2026  
**DOI:** 10.1016/j.procs.2026.08.403

## Síntese executiva

| Dimensão | Resultado |
|---|---|
| Cobertura RQ1–RQ5 | **4,0/5,0 — Alta** |
| Qualidade QA1–QA4 | **2,0/4,0 — moderada (critérios operacionalizados)** |
| Estrato informado | **A4**, percentil CiteScore 53% da série *Procedia Computer Science* |
| Tipo de evidência | Estudo secundário (RSL baseada em PRISMA) |
| Comparação empírica própria | Não realizada |
| Recomendação | **Incluir c/ ressalvas** |

> **Limite do protocolo disponibilizado:** O prompt menciona o PICOC e o arquivo `templates/review.md`, mas não apresenta a definição completa dos cinco componentes do PICOC nem o modelo de parecer. As dimensões PICOC abaixo são uma operacionalização provisória das RQ1–RQ5. Os critérios QA1–QA4 também são operacionais, não uma transcrição de definições oficiais ausentes. A confirmação da elegibilidade definitiva requer o PICOC oficial.

## 1. Tabela A — Identificação e PICOC

| Campo | Identificação e análise |
|---|---|
| ID | P110 |
| Título | DevAIOps: A Systematic Literature Review on Integrating Explainable AI Agents into CI/CD Pipelines for Optimization, Security, and Auto-Remediation |
| Ano | 2026 |
| Fonte | *Procedia Computer Science*, 290, 344–351 |
| Evento | 23rd International Conference on Mobile Systems and Pervasive Computing (MobiSPC) |
| Tipo | Estudo secundário, RSL baseada em PRISMA |
| Corpus | 222 candidatos; 217 registros únicos; 47 elegíveis; dez estudos analisados em profundidade |
| Período de busca | Janeiro de 2019 a abril de 2026 |
| Citações por fonte | OpenAlex 0; Crossref 0; Scopus 0 (metadados de triagem verificados em 27/10/2026; não somar) |
| Estrato | A4, percentil informado de 53%, conforme PDR-0006 |
| Restrição bibliométrica | PDR-0007: ressalva de estrato obrigatória |

**Fonte:** PDF, pp. 344–347 (páginas 1–4 do arquivo); prompt de triagem P110.

### PICOC operacionalizado

| Elemento | Correspondência | Juízo |
|---|---|---|
| **P — Population** | Sistemas de software, operações cloud, pipelines CI/CD, profissionais de DevOps/DevSecOps | Parcial: ênfase em pipelines, não na atuação de equipes SRE durante incidentes |
| **I — Intervention** | Agentes de IA, LLMs, RCA, automação, remediação e explicabilidade (XAI) | Direta |
| **C — Comparison** | Comparações de estudos anteriores são citadas; autores não realizam comparação empírica própria com baseline | **Não declarar Comparison empírico** |
| **O — Outcomes** | MTTR, acurácia de RCA, detecção de falhas, qualidade de correções e segurança | Parcial: resultados quantitativos de segunda mão |
| **C — Context** | Software operations, CI/CD, DevSecOps, AIOps e infraestrutura cloud-native | Direta, mas com restrição de escopo |

**Síntese:** pertinência temática como referência conceitual e arquitetural. A aplicação diretamente demonstrada à resposta a incidentes e à mensuração do esforço cognitivo é limitada.

## 2. Tabela B — Cobertura das questões de pesquisa

**Escala:** T = 1,0; P = 0,5; N = 0,0. Bandas: Alta ≥ 3,0; Média 1,5–2,5; Baixa < 1,5.

| RQ | Julgamento | Pontos | Evidência âncora |
|---|---|---:|---|
| RQ1 — Contexto, capacidades e autonomia | P | 0,5 | Introdução e seção 3.5; pp. 345 e 349 (páginas 2 e 6 do PDF) |
| RQ2 — Engenharia e arquitetura | T | 1,0 | Figura 1 e seções 4.1–4.3; pp. 345, 349–350 (páginas 2, 6 e 7) |
| RQ3 — Evidências e benefícios | P | 0,5 | Seções 3.2, 3.3 e 3.5; pp. 348–349 (páginas 5 e 6) |
| RQ4 — Desafios, riscos e governança | T | 1,0 | Seções 4.2, 4.3 e 5; p. 350 (página 7) |
| RQ5 — Lacunas e direções futuras | T | 1,0 | Seção 4; pp. 349–350 (páginas 6–7) |
| **Total** | **Alta** | **4,0/5,0** | |

### RQ1 — Contexto e autonomia: Parcial (0,5)

O artigo apresenta agentes especializados para construção, testes, segurança, implantação e remediação. Discute agentes LLM com ferramentas e supervisão humana conforme o risco das ações. Entretanto, não formula uma taxonomia detalhada de planejamento, memória e níveis de autonomia nem avalia seu efeito causal sobre decisões operacionais.

**Âncoras:** Figura 1, p. 345; seção 3.5, p. 349.

### RQ2 — Engenharia e arquitetura: Total (1,0)

A arquitetura de referência da Figura 1 combina agentes especializados, governança de explicabilidade, guardrails OWASP, monitoramento e infraestrutura cloud-native. A Figura 4 apresenta um circuito de confiança: diagnóstico por agente, explicações vinculadas a artefatos, validação multicamadas, controle humano proporcional ao risco, aplicação e monitoramento. A cobertura é arquitetural e propositiva, **não validação de uma implementação em produção**.

**Âncoras:** Figura 1, p. 345; seções 4.1–4.3 e Figura 4, pp. 349–350.

### RQ3 — Evidências e benefícios: Parcial (0,5)

O artigo compila indicadores de pesquisas anteriores, mas não executa experimentos próprios nem mede MTTD, MTTR ou carga cognitiva em um protocolo primário.

| Indicador | Resultado descrito pelo P110 | Proveniência |
|---|---|---|
| Classificação de falhas (LogSage) | 82% de acurácia | Estudo citado (Xu et al.) |
| RCA (LogSage) | 74% de acurácia | Estudo citado |
| Aceitação de correções | 61% | Estudo citado |
| RCA com GPT-4 | 35% de melhora de acurácia versus método baseado em regras | Estudo citado (Zhang et al.) |
| MTTR para RCA | Redução de 42% | Estudo citado |
| MTTR de ponta a ponta (X-Lifecycle) | Redução de 31% | Estudo citado (Goel et al.) |
| RCA com ferramentas | 68% de acurácia top-1 versus 45% sem agentes | Estudo citado (Roy et al.) |
| Resumos úteis para profissionais de plantão | 78% | Estudo citado (Jin et al.) |

Os resultados não podem ser apresentados como eficácia experimental **do P110**. Sua utilização quantitativa na dissertação requer leitura e verificação das fontes primárias.

**Âncoras:** seções 3.2 e 3.5, p. 349; ameaças à validade, p. 351.

### RQ4 — Segurança e governança: Total (1,0)

São discutidos riscos de alucinação, remediações incorretas, execução não autorizada, falhas em cascata, transparência insuficiente e ausência de explicações auditáveis. Como resposta, os autores propõem análise estática, diretrizes OWASP, explicações vinculadas a artefatos e aprovação humana por nível de risco. Trata-se de mecanismos propostos, sem teste experimental integrado demonstrado no artigo.

**Âncoras:** seções 4.2–4.3 e Figura 4, p. 350.

### RQ5 — Lacunas e agenda futura: Total (1,0)

O estudo identifica quatro lacunas: (1) ausência de arquitetura DevAIOps unificada; (2) inexistência de benchmarks padronizados; (3) explicabilidade insuficiente no nível do agente; e (4) carência de quantificação do risco de alucinações em remediação autônoma. Recomenda métricas multidimensionais, validação reprodutível, explicações auditáveis e controles graduados.

**Âncoras:** seção 4, pp. 349–350.

## 3. Tabela C — Qualidade metodológica

**Nota:** Como o prompt não define semanticamente QA1–QA4, adotam-se critérios operacionais explicitados abaixo. A pontuação não deve ser confundida com aplicação de rubrica oficial não disponibilizada.

| Critério operacional | Julgamento | Pontos | Justificativa |
|---|---|---:|---|
| QA1 — Clareza de objetivos e questões | Y | 1,0 | Três perguntas de pesquisa e objetivos delimitados |
| QA2 — Rigor e reprodutibilidade | P | 0,5 | Protocolo PRISMA, fontes e fórmula de pontuação descritos; triagem por um único revisor e corpus integral não publicado no artigo |
| QA3 — Validação empírica própria | N | 0,0 | Sem experimento original, baseline próprio ou implementação validada da arquitetura proposta |
| QA4 — Clareza e fundamentação dos resultados | P | 0,5 | Métricas e lacunas explicitadas, porém com evidência quantitativa secundária e limites de verificabilidade |
| **Total** | | **2,0/4,0** | **Qualidade moderada nos critérios operacionalizados** |

**Pontos fortes:** descrição de bases e janela temporal, critérios de seleção, fórmula de relevância, fluxo PRISMA e reconhecimento de ameaças à validade (pp. 346–347 e 350–351).

**Limitações:** seleção em profundidade de dez estudos entre 47 elegíveis, com ranking próprio; revisor único; lista completa disponível apenas mediante solicitação; riscos de cobertura e publicação; ausência de verificação independente dos benefícios quantitativos e de avaliação experimental da arquitetura (pp. 347 e 350–351).

## 4. Relevância para a dissertação sobre Agentic AI em resposta a incidentes

| Eixo | Relevância | Utilização sugerida |
|---|---|---|
| Arquitetura de agentes | Alta | Fundamentar agentes especializados, governança e observabilidade |
| Explicabilidade e supervisão humana | Alta | Derivar requisitos para rastreabilidade, validação de ações e aprovação por risco |
| MTTD e MTTR | Indireta | Identificar estudos primários e métricas; não usar o P110 como experimento próprio |
| Sobrecarga cognitiva | Indireta | Fundamentar motivação para apoio às decisões; não atribuir mensuração de carga cognitiva |
| Segurança e guardrails | Alta | Apoiar requisitos de mitigação de ações não autorizadas, remediações incorretas e alucinações |

Entre os estudos primários a verificar diretamente estão os trabalhos sobre RCA com GPT-4, X-Lifecycle, LogSage e agentes com ferramentas, referenciados pelo P110. Recomenda-se verificar tanto as métricas quanto seus baselines e contextos antes de sintetizar seus resultados na RSL.

## 5. Emendas e enquadramento

| Regra | Aplicação ao P110 | Consequência |
|---|---|---|
| PDR-0006 | Série *Procedia Computer Science* com percentil CiteScore informado de 53%, classificada A4 | Não se aplica exclusão por ausência de CiteScore |
| PDR-0007 | Estrato aferido fora de A1–A2 | **Ressalva de estrato obrigatória em todo uso da evidência** |
| Comparison | Não há comparação empírica executada pelos autores contra baseline concreto | **Comparison não declarado** |
| Natureza da evidência | RSL PRISMA | Identificar como estudo secundário; métricas de segunda mão |
| Regra R1 | Candidato fundacional-condicional segundo a triagem | Classificação provisória: texto integral da R1 não disponível |

A bibliometria desta avaliação reproduz os metadados disponibilizados no prompt (verificação declarada de 27/10/2026); não houve nova consulta externa às bases.

## 6. Conclusão e recomendação

O P110 apresenta alta cobertura das questões sobre arquitetura agêntica, governança, explicabilidade, segurança e lacunas de pesquisa, sendo útil como referência de fundamentação conceitual e arquitetural. Em contrapartida, não oferece validação empírica própria das propostas e não mede diretamente MTTD, MTTR ou carga cognitiva. As métricas quantitativas são reproduzidas de trabalhos anteriores, e a revisão apresenta limitações relacionadas à triagem por um único revisor e à rastreabilidade integral do corpus.

A elegibilidade temática conclusiva depende da disponibilização do PICOC oficial; sob a operacionalização aqui descrita, a inclusão é justificada com restrições claras ao peso da evidência.

**Recomendação final: Incluir c/ ressalvas (estudo secundário com métricas de MTTD/MTTR exclusivamente de segunda mão, ausência de validação empírica própria, limitações metodológicas e RESSALVA DE ESTRATO OBRIGATÓRIA: Procedia Computer Science A4, conforme PDR-0006 e PDR-0007; enquadramento fundacional-condicional sujeito à regra R1 e confirmação pelo PICOC oficial).**

---

**Materiais-base:** `prompt-P110.md` e `P110_DevAIOps_A_Systematic_Literature_Review_on_Integrating_Explainable_AI_Agents_int.pdf` (8 páginas).  
**Escopo:** leitura e avaliação documental, sem verificação bibliométrica externa independente.
