# Parecer acadêmico de elegibilidade e qualidade — P119

**RSL:** Agentic AI como copiloto na resposta a incidentes  
**Protocolo:** critérios PICOC, RQ1–RQ5, PDR-0006 e PDR-0007 fornecidos no `prompt-P119.md`  
**Data da avaliação:** 29/10/2026  
**Fonte primária:** Tellache et al. (2025), pp. 25–30 do artigo publicado na IEEE GLOBECOM 2025.

> **Nota de rastreabilidade:** o arquivo `templates/review.md` não foi anexado. Este parecer utiliza estrutura equivalente, com Tabelas A, B e C e recomendação final. As definições operacionais de QA1–QA4 abaixo são explicitadas porque o prompt determina sua pontuação, mas não fornece o enunciado desses critérios. A bibliometria e o estrato são reproduzidos dos insumos da triagem, sem verificação bibliométrica independente.

## Síntese do julgamento

O artigo propõe um pipeline de **Retrieval-Augmented Generation (RAG)** para enriquecer alertas SIEM com inteligência de ameaças (CTI) e gerar **planos textuais de resposta a incidentes**. O fluxo combina consulta estruturada a APIs de CTI, especialmente VirusTotal, busca semântica em uma base vetorial de relatórios CTI e geração com GPT-4o. Há avaliação de qualidade sobre 100 alertas reais e 10 simulados, com três LLMs avaliadores e validação manual dos casos simulados por **um especialista** (Seções II e III, pp. 26–30).

**Veredito temático:** aderência parcial e relevante ao PICOC como sistema de apoio à decisão na resposta a incidentes de segurança, não como comprovação de Agentic AI plenamente autônoma. **Veredito metodológico:** avaliação empírica de relevância e groundedness das respostas, sem comparação controlada com baseline e sem medição direta de MTTD, MTTR, carga cognitiva ou tempo de execução operacional. **Estrato:** A4 conforme dados de triagem; ressalva de estrato obrigatória em todo uso da evidência.

## Tabela A — Identificação e PICOC

| Campo | Classificação e evidência |
|---|---|
| Identificador | **P119** |
| Título | *Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence* |
| Autores | Amine Tellache; Abdelaziz Amara Korba; Amdjed Mokhtari; Horea Moldovan; Yacine Ghamri-Doudane |
| Ano / veículo | 2025; IEEE Global Communications Conference (GLOBECOM), trilha Communication & Information Systems Security; conference paper |
| DOI | `10.1109/GLOBECOM59602.2025.11432623` |
| Bibliometria informada | OpenAlex: **12**; Crossref: **13**; Scopus: **1**; dados de triagem verificados em 27/10/2026. **Fontes distintas, contagens não somadas.** |
| Estrato informado | **A4**, percentil CiteScore **54%** da série IEEE GLOBECOM, segundo triagem/PDR-0006; SJR: N/D. PDR-0007 exige **RESSALVA DE ESTRATO OBRIGATÓRIA** por estar fora de A1–A2. |
| **P — Population** | Equipes SOC, analistas CTI e responsáveis pela resposta a incidentes de cibersegurança; alertas SIEM corporativos e de laboratório (Introdução, pp. 25–26; Seção III-A, p. 28). **Atende em domínio adjacente ao SRE**, com foco em segurança, não em confiabilidade de serviços. |
| **I — Intervention** | Pipeline LLM + RAG com recuperação híbrida (API VirusTotal + pesquisa semântica em CTI vetorial) para contextualizar alertas e gerar recomendações/planos de resposta (Seção II, pp. 26–28; Figura 1, p. 27). **Atende parcialmente** ao conceito de agente/copiloto: uso encadeado de ferramentas e geração, sem laço de execução e verificação de ações. |
| **C — Comparison** | **Não demonstrada.** A comparação entre modelos **avaliadores** e entre conjuntos de alertas/fontes de contexto não constitui baseline empírico de desempenho do sistema proposto versus fluxo manual ou solução alternativa. Registrar **sem comparison/baseline**, conforme regra normativa. |
| **O — Outcomes** | Relevância da resposta, relevância do contexto e groundedness, avaliadas em escala 1–5; evidências de qualidade do texto produzido (Seção III-B/C, pp. 29–30). **Não há** métricas numéricas de MTTD, MTTR, latência fim a fim nem carga cognitiva. |
| **C — Context** | Incident response em SOC/ambientes de cibersegurança corporativos; 100 alertas reais de LogPoint SIEM e 10 de experimentos controlados em Proxmox, ELK, Caldera, Windows/Linux (Seção III-A, p. 28). |
| Tipo de estudo | Proposta arquitetural com avaliação experimental de respostas geradas e validação humana limitada. Não é RSL. |
| Elegibilidade | **Elegível com ressalvas:** contribui para arquitetura e apoio à decisão em IR, mas não comprova agência plena nem ganhos operacionais em MTTD/MTTR. |

## Tabela B — Questões de pesquisa (RQ)

**Escala:** T = atende (1,0); P = atende parcialmente (0,5); N = não atende (0,0).

| RQ | Nota | Evidência âncora (seção/página) | Justificativa e limite de inferência |
|---|---:|---|---|
| **RQ1 — Capacidades/autonomia** | **P (0,5)** | Seção II-A, pp. 26–27; Figura 1, p. 27; Seção II-D, p. 28 | Encadeia consultas a ferramentas e geração de plano; a equipe humana recebe a saída. Não define taxonomia de autonomia, memória persistente ou execução autônoma com feedback. Base para **copiloto de análise**, não para agência plena. |
| **RQ2 — Engenharia/arquitetura** | **T (1,0)** | Seções II-A–D, pp. 26–28; Figura 1, p. 27; Seção III-A, p. 28 | Descreve módulos de ingestão de relatórios CTI, chunking, embeddings, base Chroma, busca via VirusTotal, busca vetorial e GPT-4o; apresenta configuração experimental. Evidência arquitetural forte para RAG, porém **sem descrição de guardrails, observabilidade operacional, controles de ação ou implantação contínua em produção**. |
| **RQ3 — Benefícios/evidência** | **P (0,5)** | Seções III-A–C, pp. 28–30; Tabelas I–III, pp. 29–30 | Avalia 100 alertas reais e 10 simulados; especialista atribui médias **4,20** (answer relevance), **4,10** (context relevance) e **4,10** (groundedness) nos simulados. Há evidência de avaliação subjetiva de qualidade, **não** comprovação de redução de MTTD, MTTR, carga operacional ou tempo de resposta. |
| **RQ4 — Riscos/governança** | **P (0,5)** | Seção III-C, pp. 29–30; Seção IV, p. 30 | Evidencia falhas de recuperação de contexto em alertas reais, inclusive falsos positivos e IOCs desconhecidos; reconhece segurança e resiliência a ataques adversariais como trabalho futuro. Não apresenta auditoria de segurança, accountability, governança ou validação de guardrails. |
| **RQ5 — Lacunas/futuro** | **T (1,0)** | Seção III-C, pp. 29–30; Seção IV, p. 30 | Identifica cobertura insuficiente de CTI, limitações de IOCs, necessidade de expandir fontes privadas, personalizar saídas para diferentes funções, melhorar raciocínio e robustez ante ataques adversariais. Lacunas úteis para agenda da RSL. |
| **Total RQ** | **3,5/5,0 — Alta** | | A banda representa **cobertura das perguntas da RSL**, não qualidade causal nem nível de autonomia. |

## Tabela C — Avaliação da qualidade metodológica (QA)

> **Operacionalização adotada por ausência do enunciado dos QA no prompt:** QA1 = objetivos e contribuição claramente apresentados; QA2 = método e ambiente suficientemente descritos; QA3 = rigor da avaliação e existência de comparador apropriado; QA4 = resultados, limitações e validade das conclusões. Se a RSL possuir definições oficiais diferentes, remapear estas notas antes de consolidar a planilha-mestra.

| QA | Nota | Evidência âncora | Justificativa |
|---|---:|---|---|
| **QA1 — Objetivos claros** | **Y (1,0)** | Resumo e Introdução, pp. 25–26 | Problema, hipótese aplicada e contribuições explícitos: enriquecer SIEM com CTI via RAG e produzir estratégias de resposta. |
| **QA2 — Método reproduzível** | **P (0,5)** | Seção II, pp. 26–28; Seção III-A, p. 28 | Arquitetura, ferramentas, origem dos dados e cenários descritos; faltam detalhes suficientes sobre prompts integrais, hiperparâmetros, corpus exato/indexação e disponibilização do conjunto de dados para replicação integral. |
| **QA3 — Rigor da validação/comparação** | **P (0,5)** | Seções III-B/C, pp. 29–30; Tabelas I–III | Três avaliadores LLM e avaliação humana dos 10 simulados fornecem triangulação parcial. Ausência de baseline de IR, amostra humana restrita a um avaliador e ausência de testes de significância/consistência interavaliador limitam força causal. |
| **QA4 — Resultados e limites** | **P (0,5)** | Seção III-C e Conclusão, pp. 29–30 | Tabelas com resultados por métrica e discussão sobre baixa relevância do contexto. Porém o texto faz alegações amplas de efetividade e redução de latência sem aferição operacional correspondente. |
| **Total QA** | **2,5/4,0 — Média** | | Pontuação dependente da operacionalização declarada acima. |

## Extração de evidências úteis à dissertação

### Funcionamento observado

1. Entrada de alerta SIEM.
2. Extração de indicadores de comprometimento (IOCs) e busca estruturada em plataforma CTI (VirusTotal).
3. Enriquecimento do alerta e busca por similaridade de embeddings em relatórios CTI indexados em banco vetorial.
4. Composição do prompt com alerta e contexto recuperado; GPT-4o gera **plano textual** a ser consumido pela equipe de resposta.

**Atenção à Figura 1 (p. 27):** a saída se destina ao *incident response team*. O fluxograma não demonstra execução de comandos, remediação, confirmação de recuperação, planejamento iterativo com observação de estado ou aprendizagem contínua de incidentes em produção. Portanto, classificar como **RAG orientado à resposta, com agência limitada**, em vez de agente operacional autônomo.

### Resultados quantitativos que podem ser citados

| Medida | Resultado relatado | Interpretação correta |
|---|---|---|
| Dados de avaliação | 100 alertas corporativos reais + 10 simulados | São alertas e não 110 incidentes remediados. |
| Avaliação manual dos simulados | 1 especialista; 10 alertas | Validação humana limitada, sem concordância entre especialistas. |
| Answer relevance, especialista | Média **4,20/5** | Julgamento da pertinência do plano gerado. |
| Context relevance, especialista | Média **4,10/5** | Julgamento de adequação do contexto fornecido. |
| Groundedness, especialista | Média **4,10/5** | Julgamento de suporte das respostas nas fontes recuperadas. |
| MTTD / MTTR | **Não medidos** | Não converter alegações narrativas de eficiência em ganhos quantitativos. |
| Tempo humano / carga cognitiva / latência do pipeline | **Não reportados numericamente** | Não há evidência quantitativa de economia de tempo ou esforço. |

Os três valores de avaliação manual são os da **Tabela III, p. 30**. Os valores de tabelas automatizadas dependem do LLM avaliador e do subconjunto de alertas; não devem ser agregados como se fossem um único índice de desempenho.

## Apreciação crítica e uso na RSL

**Contribuição:** exemplo aplicado de uma arquitetura RAG híbrida para enriquecimento de alertas de segurança e geração de orientação contextual. É especialmente pertinente a **RQ2**, à discussão de qualidade de recomendações em **RQ3** e às lacunas de confiabilidade de recuperação e segurança em **RQ4/RQ5**.

**Risco de extrapolação:** o título contém “Autonomous”, mas o experimento avalia **texto de planos de resposta**. Não demonstra tomada de ação autônoma, ciclo fechado de observação–decisão–execução–verificação ou redução medida de tempos de detecção e recuperação. A comparação entre LLMs que **julgam as saídas** não atende ao critério normativo de _Comparison_ empírica contra baseline concreto.

**Validade externa:** alertas reais são de uma única organização; os incidentes simulados são dez e partem de laboratório controlado. O estudo não prova transferência dos resultados para SRE, incidentes de disponibilidade, plataformas CPaaS ou ambientes multi-cloud em produção.

**Validade interna e de mensuração:** avaliações automáticas baseadas em LLMs podem apresentar vieses; um único avaliador humano limita a triangulação. As métricas medem a relevância e o lastro de recomendações, não eficácia de remediação ou causalidade sobre resultados operacionais.

**Ressalva de estrato obrigatória (PDR-0006/PDR-0007):** a triagem informa série IEEE GLOBECOM com percentil CiteScore 54%, convertida a **A4**. Consequentemente, **toda utilização da evidência P119 na síntese da RSL deve identificar explicitamente o estrato A4 e sua posição fora de A1–A2**, sem equivalê-la à força de estudos com estrato superior ou comparação operacional controlada. O valor bibliométrico não substitui avaliação metodológica.

## Recomendação final

**Incluir c/ ressalvas (RESSALVA DE ESTRATO OBRIGATÓRIA: IEEE GLOBECOM A4, fora de A1–A2, conforme PDR-0006/PDR-0007; agência limitada a pipeline RAG com geração de planos, sem remediação autônoma; ausência de baseline empírico e de MTTD/MTTR numéricos).**
