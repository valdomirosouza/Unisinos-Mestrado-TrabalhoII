# Parecer acadêmico de avaliação integral — P121

**Estudo:** Habibzadeh, A.; Feyzi, F.; Atani, R. E. (2026). *Large Language Models for Security Operations Centers: A Comprehensive Survey*. *Journal of Electrical and Computer Engineering*, 2026, art. 3383674. DOI: https://doi.org/10.1155/jece/3383674  
**Tipo:** estudo secundário (survey/revisão da literatura; síntese de 216 publicações).  
**Protocolo:** triagem PICOC, RQ1–RQ5, QA1–QA4; regras PDR-0006 e PDR-0007 conforme `prompt-P121.md`.  
**Nota metodológica:** o prompt não traz o texto literal do PICOC completo nem as definições operacionais de QA1–QA4, e o arquivo `templates/review.md` não foi fornecido. As correspondências PICOC e os quatro indicadores QA abaixo são **operacionalizações transparentes e provisórias**, não uma reconstrução de regras não disponibilizadas. O julgamento final deve ser reconciliado com esses documentos, caso tenham critérios diferentes.

## Síntese executiva

O P121 organiza 216 estudos sobre aplicação de LLMs em operações de segurança (SOC), distinguindo **Detecção, Análise e Resposta**, relacionando os estudos às funções do **NIST CSF** e às técnicas do **MITRE ATT&CK**. Sua principal contribuição para a RSL é **contextual, arquitetural e de identificação de lacunas**, especialmente a baixa maturidade e cobertura de *Respond/Recover*, a necessidade de supervisão humana e os desafios de avaliação, segurança e integração. O artigo **não propõe nem avalia experimentalmente um novo copiloto agêntico**, tampouco executa, por si, uma comparação controlada contra baseline operacional. Métricas numéricas citadas são resultados de **estudos primários referenciados**, não resultados experimentais do survey.

**Relevância temática calculada:** **3,5/5,0 (Alta)**. **Qualidade metodológica operacionalizada:** **3,0/4,0**. **Estrato:** A3, **fora de A1–A2**, com **RESSALVA DE ESTRATO OBRIGATÓRIA (PDR-0007)**. Indicação: **inclusão condicional como fonte secundária/fundacional**, sem equiparar evidência sintetizada a validação empírica primária.

## Tabela A — Identificação e PICOC

| Campo | Registro e avaliação |
|---|---|
| ID / título | P121 — *Large Language Models for Security Operations Centers: A Comprehensive Survey* |
| Autoria / ano | Ali Habibzadeh; Farid Feyzi; Reza Ebrahimi Atani; 2026 |
| Veículo | *Journal of Electrical and Computer Engineering*; artigo de revisão; acesso aberto |
| DOI | 10.1155/jece/3383674 |
| Cobertura do corpus | 216 estudos; busca declarada em ScienceDirect, SpringerLink, IEEE Xplore, ACM DL, arXiv e apoio do Google Scholar; publicações de 2021–2025; seção 3, pp. 4–6 |
| População (*Population*) | Analistas e operações de SOC, atividades de triagem, detecção, investigação e resposta a incidentes cibernéticos. **Aderência parcial** à população mais ampla de SRE/incident response operacional |
| Intervenção (*Intervention*) | LLMs, agentes com ferramentas, RAG, fine-tuning, prompting e sistemas multiagentes aplicados ao fluxo do SOC. **Aderência parcial/alta por subgrupo**, pois a maior parte do levantamento não é especificamente Agentic AI |
| Comparação (*Comparison*) | **Não declarada como comparação empírica própria**: o survey sintetiza resultados de trabalhos com ou sem baselines. A existência de uma tabela comparativa ou de números citados não torna o survey um experimento comparativo |
| Resultados (*Outcomes*) | Desempenho de classificação/detecção, precisão, recall, F1; eficiência da mitigação e automação reportadas por trabalhos referenciados; supervisão humana, confiabilidade, alucinação, custo e lacunas. **MTTD, MTTR e carga cognitiva não são conjuntamente validados pelo survey em experimento próprio** |
| Contexto (*Context*) | SOCs e cibersegurança; analogia pertinente a resposta a incidentes em operações críticas, mas não equivalência direta a SRE, observabilidade ou produção CPaaS |
| Desenho | Estudo secundário com enquadramento declarado nas diretrizes de Kitchenham (seção 3, p. 4); não é ensaio de implantação ou benchmark primário |
| Bibliometria (fornecida na triagem) | OpenAlex: **13**; Crossref: **15**; Scopus: **1**. Verificação informada: 27/10/2026. **Fontes não somadas** |
| Classificação do veículo (fornecida) | Qualis derivado **A3**, percentil Scopus **71%**; SJR N/D. Ressalva obrigatória sob PDR-0007. PDR-0006 refere-se especificamente a proceedings de conferência e não modifica diretamente este artigo de periódico |
| Papel sugerido | **Fundacional-condicional / estudo secundário** para taxonomia, panorama de métodos e lacunas; rastrear estudos primários relevantes para a síntese quantitativa |

## Tabela B — Respostas às questões de pesquisa

**Escala:** T = atende diretamente (1,0); P = atende parcialmente (0,5); N = não atende (0,0). As RQs abaixo são as **da presente RSL**, não as RQs internas numeradas no artigo.

| RQ | Julgamento | Nota | Evidência âncora (seção/página do PDF) | Justificativa e limite |
|---|---|---:|---|---|
| **RQ1 — Contexto/definições e autonomia** | **P** | **0,5** | §2.1, pp. 2–3 (agentes com ferramentas, múltiplas etapas, custos); §8.2, pp. 26–28 (HITL, autonomia crescente) | Apresenta capacidades de agentes, raciocínio e interação com ferramentas, mais recomendações de supervisão. Não oferece uma taxonomia rigorosa de níveis de autonomia agêntica, memória e delegação decisória em ambientes de produção. |
| **RQ2 — Engenharia/arquiteturas** | **T** | **1,0** | §2.1, pp. 2–3 (RAG e agents); §5.1, p. 8 (multiagentes e recuperação de logs); §6, pp. 16–22 (análise, conhecimento e RCA); §8.2, pp. 26–28 (integração, Agent-Based RAG, HITL) | Sintetiza padrões de agentes, recuperação, combinação com sistemas existentes, integração e mecanismos de controle. O atendimento é temático: **não comprova operação confiável em produção** para todas as arquiteturas apresentadas. |
| **RQ3 — Benefícios e métricas** | **P** | **0,5** | §5.1, pp. 8–9 e Tabela 3 (resultados de detecção/F1); §7, pp. 23–25, sobretudo pp. 24–25 (mitigação de incidentes por estudos citados) | Oferece dados quantitativos **de terceiros**: para Nissist, reporta reduções de tempo de mitigação de **98,93% (incidentes simples)** e **94,85% (complexos)** versus mitigação manual, além de taxas de automação. São resultados **atribuídos ao estudo referenciado**, não medidos pelo P121. Não há comprovação própria de redução de MTTD/MTTR nem avaliação estruturada de carga cognitiva. |
| **RQ4 — Desafios, ética e governança** | **T** | **1,0** | §8.1, pp. 25–26 (alucinações, explicabilidade, prompt injection, privacidade, regulação, integração e decisão humana); §9, p. 28 | Cobertura explícita de robustez, segurança, vazamento de dados, opacidade, compliance e limites à autonomia. Recomenda revisão humana e salvaguardas. |
| **RQ5 — Lacunas e direções futuras** | **T** | **1,0** | §3.4–4, pp. 6–7 (distribuição de trabalhos); §8.2, pp. 26–28 (benchmarks, XAI, Agent-Based RAG, HITL, Recover); §9, p. 28 | Identifica ausência de benchmarks realistas, desafios de confiança, necessidade de protocolos HITL e concentração de trabalhos em Detecção, com lacunas notáveis em Resposta/Recuperação. |
| **Total** | **Alta** | **3,5 / 5,0** | | Escala normativa: Alta ≥3,0; Média 1,5–2,5; Baixa <1,5. |

## Tabela C — Qualidade metodológica (QA1–QA4)

*Como não foram anexadas as definições normativas de QA1–QA4, as dimensões abaixo são hipóteses operacionais explícitas e devem ser ajustadas se o checklist original divergir. Y = 1,0; P = 0,5; N = 0,0.*

| QA | Critério operacional adotado | Julgamento | Nota | Evidência / justificativa |
|---|---|---|---:|---|
| **QA1** | Objetivos e questões claramente definidos | **Y** | **1,0** | §3.1, p. 5: cinco RQs do survey, vinculadas às fases SOC e desafios futuros; introdução e contribuições nas pp. 1–2. |
| **QA2** | Estratégia de busca e seleção reproduzível | **P** | **0,5** | §§3.2–3.3, p. 6: fontes, string de busca, período 2021–2025 e critérios gerais de inclusão/exclusão são informados. Entretanto, não fica demonstrado um fluxo auditável completo de identificação, deduplicação e exclusões com contagens por etapa, nem avaliação do viés de seleção independente. |
| **QA3** | Extração, classificação e síntese de evidências | **Y** | **1,0** | §§3.1–3.4, pp. 5–6, e tabelas/figuras das §§4–7: categorização por fases, métodos e maturidade TRL; consolidação de 216 trabalhos. A nota reflete a sistematização descritiva, **não uma metanálise causal**. |
| **QA4** | Limites, validade e aplicabilidade criticamente discutidos | **P** | **0,5** | §8, pp. 25–28: extensa discussão de riscos e lacunas; porém, a heterogeneidade dos estudos e a falta de uma avaliação formal explícita de qualidade/risco de viés dos estudos primários limitam a força de generalização. |
| **Total** | | | **3,0 / 4,0** | Pontuação provisória, dependente da rubrica QA original. |

## Parecer crítico

### Contribuições aproveitáveis

O estudo ajuda a delimitar onde **LLMs e agentes** apoiam o ciclo operacional: análise de logs, detecção de anomalias, triagem, enriquecimento de inteligência, RCA, planejamento de resposta e mitigação assistida. A organização NIST CSF + MITRE ATT&CK facilita distinguir detecção, análise e resposta, evitando tratar toda tarefa de SOC como remediação autônoma (§§2–7, pp. 3–25). A discussão de **Agent-Based RAG**, integração a ferramentas, trilhas de fontes, avaliação contínua e **human-in-the-loop** sustenta o desenho de guardrails e a formulação de requisitos, mas deve ser citada como **orientação sintetizada**, não como sistema de referência já validado universalmente (§8.2, pp. 26–28).

A evidência mais próxima do resultado operacional da RSL aparece nos estudos resumidos em resposta a incidentes. Em particular, os números atribuídos a **Nissist** na seção 7 (pp. 24–25) devem ser extraídos diretamente do artigo primário antes de entrar em comparação quantitativa, verificando definição de tempo, amostra, tipos de incidente, baseline manual e condições experimentais. **Tempo de mitigação não deve ser convertido automaticamente em MTTD ou MTTR padronizado.** Também não há mensuração direta da redução de sobrecarga cognitiva pelo P121.

### Limitações e risco de interpretação

O corpus reúne aplicações de **modelos de linguagem** em geral, incluindo BERT/classificadores e métodos não agênticos. Portanto, classificar todos os 216 trabalhos como evidência de *Agentic AI* inflaria a base de estudos. A ênfase em SOC/cibersegurança requer ressalva de transferência ao ciclo SRE de incidentes de disponibilidade, confiabilidade e operação de serviços. A revisão declara inspiração em Kitchenham, mas as informações metodológicas apresentadas não bastam para verificar integralmente a reprodutibilidade, independência da seleção e risco de viés dos estudos incluídos. Por fim, as diferenças entre arquiteturas, datasets e métricas tornam imprópria uma agregação quantitativa informal.

### Diretriz de extração para a RSL

Registrar P121 como **estudo secundário com função de contextualização/fundamentação**, aplicando sua pontuação temática **3,5/5** e a ressalva permanente de **Qualis A3 / PDR-0007**. Usar o survey para localizar literatura primária sobre agentes, RCA, HITL, benchmarks e incident response. **Não duplicar** no conjunto de evidência empírica resultados de estudos já incluídos separadamente; **não declarar Comparison empírico do próprio P121**; **não apresentar percentuais agregados ou ganhos operacionais próprios**. Se o protocolo da RSL excluir estudos secundários do conjunto principal, utilizar P121 apenas na fundamentação e busca reversa, conforme a regra fundacional-condicional R1 indicada na triagem.

## Recomendação final

**Incluir c/ ressalvas (estudo secundário/fundacional-condicional; ausência de comparação empírica própria e de validação direta de MTTD, MTTR e carga cognitiva; extrapolação SOC→SRE limitada; RESSALVA DE ESTRATO OBRIGATÓRIA: Qualis A3, fora de A1–A2, conforme PDR-0007).**
