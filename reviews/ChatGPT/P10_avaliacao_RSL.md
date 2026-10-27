# Avaliação de Qualidade e Aderência — P10

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**Estudo:** P10 — *Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey*  
**Autores:** Deepak Bhaskar Acharya; Karthigeyan Kuppan; B. Divya.  
**Base de avaliação:** exclusivamente o artigo em PDF anexado e a rubrica do protocolo `prompt-P10(1).md`.  
**Natureza:** estudo fundacional herdado do Trabalho I; avaliação retroativa, sem rediscussão da inclusão original.

## Etapa 0 — Extração bibliométrica: Tabela A (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P10 | IEEE Access, v. 13 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Survey abrangente, síntese conceitual | 10.1109/ACCESS.2025.3532853 |

**Evidência:** cabeçalho, identificação de periódico, datas, DOI e resumo, p. 18912 (página 1 do PDF). O próprio artigo se identifica como *survey*. Os rótulos A1 e Q1 constantes no protocolo são informações externas pré-fornecidas, não verificáveis no PDF; por isso permanecem **[VERIFICAR]** na tabela, sem reclassificação por inferência. Citações recebidas pelo artigo também não constam do documento.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Fundamentação |
|---|---|---|
| Ano ≥ 2020 | Atendido | Ano de publicação: 2025, p. 18912. |
| Publicação identificável | Atendido | Periódico IEEE Access, v. 13, p. 18912. |
| Citações ≥ 1 | [VERIFICAR] | O PDF não informa a contagem de citações recebidas. |
| SJR Q1–Q2 | [VERIFICAR] | Quartil não consta do PDF. |
| Qualis A1–A2 | [VERIFICAR] | Estrato não consta do PDF. |

**Resultado formal: ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações recebidas, quartil SJR e estrato Qualis). Prossegue-se com a avaliação integral conforme o protocolo, preservando o status de estudo fundacional incluído no Trabalho I. As verificações externas devem ser conduzidas em base indexadora de citações, SCImago Journal Rank e Plataforma Sucupira/Qualis CAPES, respectivamente.

## Etapa 2 — Classificação das questões de pesquisa: Tabela B (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P10 | Acharya et al. (2025) | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | II.B–D, pp. 18914–18915; III.A–C, pp. 18915–18917; Tabelas 1–3 e Figura 1 | Define autonomia orientada a objetivos e diferencia sistemas tradicionais e agênticos; descreve adaptação, aprendizado, planejamento, decomposição de objetivos, tomada de decisão contextual e graus de intervenção humana. Há cobertura explícita das três subdimensões. |
| P10 | Acharya et al. (2025) | RQ2 — Engineering Architecture | Parcialmente Respondida | **P (0,5)** | IV.A–E, pp. 18917–18920; Figura 2 (p. 18918), Figura 3 (p. 18920); IX, pp. 18926–18928 | Apresenta MAS, HRL, arquiteturas modulares, raciocínio/planejamento, ferramentas/APIs, memória episódica e semântica, RAG e frameworks de desenvolvimento. Descreve supervisão/controle em alto nível, mas não especifica uma arquitetura operacional integrada e reproduzível com observabilidade de produção e guardrails instrumentados. |
| P10 | Acharya et al. (2025) | RQ3 — Evidence Benefits | Parcialmente Respondida | **P (0,5)** | V.A–E, pp. 18919–18922; VI.A–D, pp. 18922–18924; Tabelas 7–9 | Discute benefícios qualitativos em produtividade, flexibilidade e suporte à decisão; enumera métricas como eficiência no alcance de objetivos, adaptabilidade, robustez, aprendizado e satisfação. Apresenta cenários e estudos citados, mas não fornece experimento próprio, medições numéricas comparáveis nem MTTD/MTTR ou carga cognitiva medidos em resposta a incidentes. |
| P10 | Acharya et al. (2025) | RQ4 — Challenges & Ethics | Respondida Plenamente | **T (1,0)** | VII, pp. 18924–18926; VIII, pp. 18925–18927; IX, pp. 18926–18928; Tabela 12, p. 18928 | Examina alinhamento de objetivos, adaptação, escalabilidade, recursos, segurança, privacidade, transparência, justiça e responsabilização, além de padrões de governança, supervisão humana e protocolos de intervenção. Abrange riscos técnicos, ético-governamentais e mecanismos de mitigação. |
| P10 | Acharya et al. (2025) | RQ5 — Research Gaps | Respondida Plenamente | **T (1,0)** | X.A–J, pp. 18928–18933; Tabela 13, p. 18931; XI, p. 18933 | Explicita agenda de pesquisa em alinhamento, adaptabilidade, resiliência, escalabilidade, eficiência energética, modelos teóricos, avaliação/benchmarks e governança. Não desenvolve especificamente um programa de medição de observabilidade e IR, mas aborda diversas lacunas solicitadas. |
| **P10** | **TOTAL** | **SCORE_RQ** | | **4,0 / 5,0** | | **Alta aderência temática, com limitação de evidência empírica em resposta a incidentes.** |

### Fundamentação analítica por RQ

**RQ1 — T (1,0).** As seções II e III estabelecem a definição de Agentic AI e o contraste com IA tradicional. As Tabelas 1 a 3 comparam autonomia, adaptabilidade e decisão; a Figura 1 sintetiza aprendizagem por reforço, arquiteturas orientadas a objetivos e controle adaptativo. A tomada de decisão é apresentada como contextual e orientada por objetivos de diferentes horizontes. A autonomia não elimina necessariamente a supervisão humana: a seção III.A admite intervenção em situações apropriadas.

**RQ2 — P (0,5).** A seção IV.A enumera abordagens arquiteturais como sistemas multiagentes, aprendizagem hierárquica por reforço e módulos orientados a objetivos. A seção IV.C detalha planejamento, uso de ferramentas e APIs, memória episódica/semântica, RAG e ajuste de instruções; a seção IV.E apresenta OpenAI Gym, Unity ML-Agents, TensorFlow Agents, PyMARL e Rasa. A seção IX trata da supervisão e de controles humanos. O material, porém, não constitui especificação ou validação de uma arquitetura observável de produção voltada a incidentes, com pipelines de telemetria, auditoria e controles executáveis descritos em nível de implementação.

**RQ3 — P (0,5).** As seções V e VI discutem aplicações e indicadores de adaptabilidade, eficiência, robustez, aprendizagem e colaboração humano–IA. A Tabela 8 apresenta uma taxonomia de métricas; a seção VI.C enumera datasets e ambientes de benchmark, como MIMIC-III/PhysioNet, CARLA e MultiWOZ. Essas referências e exemplos não equivalem à apresentação de resultados próprios ou a uma análise quantitativa agregada. A ausência de números primários, comparação controlada e métricas de operações de TI limita a resposta à RQ3.

**RQ4 — T (1,0).** As seções VII e VIII cobrem obstáculos técnicos, riscos éticos e questões regulatórias. A seção IX apresenta frameworks de segurança/governança e mecanismos de supervisão, monitoramento e intervenção humana, com síntese de exemplos na Tabela 12. São discussões conceituais, não demonstrações de eficácia quantitativa desses mecanismos.

**RQ5 — T (1,0).** A seção X e a Tabela 13 sistematizam lacunas: generalização/adaptação, alinhamento com valores humanos, normas éticas, coordenação de múltiplos agentes, escalabilidade, resiliência, eficiência e avaliação de agência. O roteiro da seção X.J consolida prioridades futuras. Para a RSL em resposta a incidentes, o principal desdobramento é a oportunidade de testar tais conceitos em cenários operacionais verificáveis, não uma conclusão experimental já demonstrada pelo artigo.

## Etapa 3 — Avaliação da qualidade DARE: Tabela C (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---:|---:|---:|---:|---:|---|
| P10 | Survey abrangente, conceitual | **Y (1,0)** | **N (0,0)** | **N (0,0)** | **Y (1,0)** | **2,0 / 4,0** | **Média** |

### Justificativa da pontuação

- **QA1 — Y (1,0): objetivos claros.** O resumo, a seção I.C (*Objectives and Contributions*, p. 18913) e a organização em I.D explicitam o propósito de definir o paradigma, comparar abordagens, caracterizar aplicações, desafios e governança. O problema não é especificamente fadiga de alertas ou análise de logs; a rubrica é atendida quanto à clareza do problema geral e da abordagem agêntica.
- **QA2 — N (0,0): metodologia replicável.** Embora IV.A–E (pp. 18917–18920) descreva métodos e ferramentas encontrados na literatura, não há protocolo de busca/seleção da revisão, procedimento operacional reproduzível ou configuração experimental própria com parâmetros e ambiente suficientemente especificados. A exposição de frameworks existentes não equivale a método replicável do estudo.
- **QA3 — N (0,0): base de evidências sólidas.** VI.B–C (pp. 18922–18924) relata exemplos e benchmarks de terceiros, mas o survey não documenta experimento próprio, estudo industrial próprio, simulação executada pelos autores, tabelas de resultados medidos ou comparação estatística. A Tabela 8 lista **tipos de métricas**, não valores observados. Em aplicação da rubrica estrita, a base é secundária e ilustrativa, insuficiente para pontuar validação empírica própria.
- **QA4 — Y (1,0): conclusões coerentes.** A seção XI (p. 18933) retoma autonomia, objetivos, adaptabilidade, benefícios potenciais, restrições técnicas e preocupações éticas, em concordância com as seções II–X; as seções VII e X explicitam desafios e limitações do campo. Ressalva: a coerência é predominantemente **conceitual**, não comprovação causal ou quantitativa de benefícios.

**SCORE_QA = 1,0 + 0,0 + 0,0 + 1,0 = 2,0 / 4,0. Banda: MÉDIA** (faixa 1,5–2,5 do protocolo).

## Parecer final do revisor

O P10 é um estudo fundacional de elevada aderência às dimensões conceituais da RSL, sobretudo definição de Agentic AI, autonomia, arquiteturas, ética e agenda de pesquisa. Sua contribuição para resposta a incidentes é **indireta**, ao oferecer mecanismos potencialmente aplicáveis a decisões em ambientes complexos e críticos. A revisão não testa um copiloto SRE/IR e não demonstra reduções mensuradas de MTTD, MTTR ou carga cognitiva. Por isso, serve como embasamento teórico e identificação de desafios, mas não como evidência empírica de desempenho operacional.

**Recomendação: INCLUIR COM RESSALVAS.** Preservar a inclusão herdada do Trabalho I. Utilizar o P10 na síntese de conceitos, arquiteturas, autonomia responsável e lacunas, separando suas proposições gerais de resultados de trabalhos experimentais. Não atribuir ao artigo benefícios quantitativos ou validação operacional que ele não apresenta.

### Pendências de verificação externa

1. **Citações recebidas pelo artigo:** [VERIFICAR] em base indexadora (por exemplo, Scopus, Web of Science ou Google Scholar), com data da consulta.
2. **Quartil SJR do veículo no ano pertinente:** [VERIFICAR] no SCImago Journal Rank; o protocolo informa Q1, mas esse dado não está no PDF.
3. **Estrato Qualis CAPES do veículo no período adotado pela RSL:** [VERIFICAR] na Plataforma Sucupira/Qualis CAPES; o protocolo informa A1, mas esse dado não está no PDF.

> **Nota de integridade:** o artigo cita aplicações, ferramentas e datasets de terceiros. A simples descrição de um caso ou benchmark no survey não demonstra que os autores tenham executado tal experimento. As avaliações de QA2, QA3 e RQ3 distinguem expressamente essas situações.

## Referência bibliográfica extraída do artigo

ACHARYA, Deepak Bhaskar; KUPPAN, Karthigeyan; DIVYA, B. *Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey*. **IEEE Access**, v. 13, 2025. DOI: https://doi.org/10.1109/ACCESS.2025.3532853.
