# Avaliação do artigo P01 — Corpus fundacional

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P01  
**Artigo:** Adabara et al., *Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment*  
**Fonte examinada:** PDF disponibilizado, versão 1, publicada em 11 de setembro de 2025.  
**Regra de evidência:** classificações fundamentadas somente no PDF; informações bibliométricas externas não foram reconfirmadas.

## Etapa 0 — Tabela A: Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P01 | F1000Research, v. 14, artigo 905 | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Revisão narrativa (survey conceitual, não RSL) | 10.12688/f1000research.169927.1 |

**Evidência:** folha de rosto e resumo (pp. 1–2), seção 1 (p. 3) e seção 2 (pp. 4–6). O artigo declara expressamente que se trata de uma síntese narrativa, não de uma revisão sistemática. A capa informa *peer review: awaiting peer review* para esta versão, condição que não equivale a uma certificação de revisão por pares concluída.

**Metadados fornecidos no prompt:** Qualis A2 e SJR Q1, descritos como verificados em fonte externa, porém não atestáveis pelo próprio PDF. Por exigência da regra de extração, as células da tabela permanecem **[VERIFICAR]**, sem substituir os valores declarados no protocolo por uma confirmação independente inexistente.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência/observação |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicação em 2025, p. 1 |
| Veículo identificável | Atendido | F1000Research, v. 14:905, pp. 1–2 |
| Citações ≥ 1 | [VERIFICAR] | Número de citações recebidas não comprovado no PDF; consultar base indexadora |
| SJR Q1–Q2 | [VERIFICAR] | Prompt registra Q1, mas requer conferência no SCImago Journal Rank |
| Qualis A1–A2 | [VERIFICAR] | Prompt registra A2, mas requer conferência na Plataforma Sucupira / Qualis CAPES |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações recebidas, quartil SJR e estrato Qualis). O P01 já integra o **corpus fundacional** do Trabalho I. Portanto, o resultado não reabre nem desfaz a decisão de inclusão herdada; serve apenas para rastreabilidade e harmonização dos critérios.

## Etapa 2 — Tabela B: Extração e classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P01 | Trustworthy agentic AI systems | RQ1 | Respondida Plenamente | **T (1,0)** | §§ 3.1–3.4, pp. 7–10; Figuras 2–3, pp. 8–9 | Define autonomia, planejamento, memória, raciocínio e uso de ferramentas. Explica decomposição de tarefas, ciclos adaptativos de decisão, coordenação de agentes e necessidade de supervisão humana. Cobre as dimensões (a), (b) e (c), em perspectiva conceitual. |
| P01 | Trustworthy agentic AI systems | RQ2 | Respondida Plenamente | **T (1,0)** | §§ 4.1–4.5, pp. 10–13; Tabela 1, p. 13; §§ 8.1–8.5, pp. 31–38; Figuras 2, 8–10 | Compara arquiteturas monoagente, multiagente, federadas e híbridas; descreve memória, orquestração, APIs/ferramentas, zero trust, monitoramento em execução, identidade criptográfica e defesas em camadas. Cobre tipos, exemplos de tecnologias/frameworks e capacidades avançadas. Não fornece implementação reprodutível própria. |
| P01 | Trustworthy agentic AI systems | RQ3 | Parcialmente Respondida | **P (0,5)** | §§ 4.5, 7.1–7.4, pp. 13, 27–31; Tabela 1, p. 13; § 8.3, pp. 33–35 | Reúne benefícios qualitativos relatados para escalabilidade, resiliência, coordenação e segurança, além de comentar implantações e estudos de terceiros. Não apresenta experimento próprio nem comparação consolidada de MTTD, MTTR, qualidade de decisão ou carga cognitiva em resposta a incidentes. Evidência essencialmente secundária. |
| P01 | Trustworthy agentic AI systems | RQ4 | Respondida Plenamente | **T (1,0)** | §§ 5.1–5.5, pp. 13–19; §§ 6.1–6.6, pp. 20–27; §§ 8.1–8.5, pp. 31–38; Figuras 5–10 | Detalha alucinação, goal drift, reward hacking, injeção e envenenamento de memória, ameaças entre camadas, prestação de contas e riscos institucionais. Discute mecanismos de mitigação: zero trust, defesa em profundidade, monitoramento, auditoria, gestão de identidades e revogação. Cobertura explícita das três subdimensões. |
| P01 | Trustworthy agentic AI systems | RQ5 | Respondida Plenamente | **T (1,0)** | §§ 9.1–9.9, pp. 38–45; Tabela 5, p. 45; §§ 10.1–10.3, pp. 46–48 | Identifica lacunas de alinhamento de objetivos, integridade de memória, auditabilidade, governança federada, revogação, shadow agents, incorporação de normas e validação. Recomenda benchmarking dinâmico, observabilidade e pesquisas interdisciplinares. |
| **P01** | **TOTAL** | **SCORE_RQ** | **4,5 / 5,0** | **T/T/P/T/T** | **Síntese das cinco RQs** | **Alta aderência conceitual, com limitação na demonstração empírica de benefícios operacionais específicos de IR.** |

### Fundamentação complementar por RQ

**RQ1 — Context Definitions.** A seção 3.1 define Agentic AI como sistemas capazes de autonomia, memória, raciocínio, planejamento e uso proativo de ferramentas. A seção 3.2 relaciona essas capacidades à tomada de decisão em ambientes dinâmicos, e a Figura 3 representa ciclos cognitivos com percepção, memória, raciocínio e planejamento. A discussão de supervisão aparece, adicionalmente, nas seções de governança. A definição é explícita, ainda que sem escala formal de níveis de autonomia.

**RQ2 — Engineering Architecture.** A Figura 2 apresenta cinco camadas (governança, cognição, memória, interação e execução segura). A Tabela 1 compara quatro famílias arquiteturais e respectivas vantagens/limitações. A seção 8 consolida mecanismos de defesa e supervisão, incluindo SHIELD, zero trust e SAGA. A nota T indica cobertura temática das subdimensões, não prontidão comprovada de um sistema implementado pelo artigo.

**RQ3 — Evidence Benefits.** A seção 7 reúne exemplos de implantação e incidentes. A seção 8.3 menciona validação empírica de SAGA realizada em trabalho referenciado, mas o artigo P01 não reproduz protocolos, dados ou métricas suficientes para que essa validação seja atribuída ao estudo avaliado. Também não apresenta resultados originais específicos para redução de MTTD, MTTR ou esforço cognitivo de analistas de IR. Assim, evidências qualitativas secundárias sustentam P, não T.

**RQ4 — Challenges & Ethics.** A taxonomia de ameaças da seção 5 e da Figura 5 separa riscos cognitivos, de memória/conhecimento, execução e governança. As seções 6 e 8 aproximam a análise técnica de modelos institucionais de responsabilidade, políticas, controle do ciclo de vida, revogação e mecanismos de execução segura.

**RQ5 — Research Gaps.** A seção 9 estrutura o debate sobre lacunas e a seção 9.8 explicita problemas de benchmarking de sistemas não determinísticos e a necessidade de testes guiados por observabilidade. A Tabela 5 da página 45 consolida domínios e avanços necessários, incluindo segurança, governança, ética, multiagentes e validação.

## Etapa 3 — Tabela C: Avaliação de qualidade DARE (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P01 | Revisão narrativa | **Y (1,0)** | **P (0,5)** | **N (0,0)** | **Y (1,0)** | **2,5 / 4,0** | **Média** |

**QA1 — Objetivos claros (Y = 1,0).** A introdução (pp. 3–4) delimita o problema da confiabilidade em sistemas agênticos e anuncia integração de arquiteturas, ameaças e governança. O resumo (p. 1) e as contribuições (p. 4) são explícitos. O problema não é exclusivamente resposta a incidentes, mas está claramente formulado para o escopo declarado pelo estudo.

**QA2 — Metodologia replicável (P = 0,5).** A seção 2 (pp. 4–7) informa tipo de revisão, fontes consultadas, agrupamentos de palavras-chave e princípios flexíveis de seleção. Entretanto, por ser narrativa, não fornece uma estratégia de busca integralmente reproduzível, período fechado de execução, quantitativos completos de seleção ou protocolo experimental para repetir a arquitetura como sistema operacional. Há transparência parcial, insuficiente para Y.

**QA3 — Base de evidências sólidas (N = 0,0).** O estudo sintetiza referências e descreve casos/avaliações produzidos por terceiros (§ 7, pp. 27–31; § 8, pp. 31–38), mas não apresenta experimento, simulação quantitativa ou estudo de caso industrial **original e mensurado**. Pelos critérios fornecidos, evidência conceitual/secundária, sem validação empírica própria, recebe N. Isso não significa que a bibliografia citada não contenha estudos empíricos.

**QA4 — Conclusões coerentes (Y = 1,0).** As conclusões das seções 10.1–10.3 (pp. 46–48) retomam as ameaças, abordagens de mitigação e lacunas discutidas nas seções anteriores, sem reivindicar um ganho quantitativo original. A seção 9 (pp. 38–45) explicita limitações do campo em alinhamento, observabilidade, governança e benchmarking. A coerência é avaliada em relação à natureza narrativa do estudo, não como confirmação experimental de suas propostas.

## Parecer final do revisor

**Síntese.** P01 oferece uma síntese conceitual abrangente de Agentic AI, com forte contribuição para definições, arquiteturas, ameaças, governança e agenda de pesquisa. As seções sobre segurança entre camadas, supervisão contínua, auditabilidade e avaliação dinâmica ajudam a contextualizar a construção de copilotos agênticos confiáveis para resposta a incidentes. A aderência às RQs é alta (**4,5/5,0**), mas a qualidade metodológica fica na banda **Média (2,5/4,0)** devido à replicabilidade apenas parcial e à ausência de evidência empírica original. Não é adequado utilizá-lo como prova quantitativa de redução de MTTD, MTTR ou carga cognitiva.

**Recomendação:** **INCLUIR COM RESSALVAS**. Manter no corpus fundacional herdado, como referência de síntese teórica e de governança, sem tratá-lo como estudo de validação operacional. Registrar que a versão 1 de 11/09/2025 apresenta o status *awaiting peer review* no próprio PDF (p. 1). A recomendação não reabre a seleção original do Trabalho I.

**Pendências de verificação externa:**

1. **Citações recebidas:** conferir em uma base indexadora e registrar data da consulta.
2. **SJR:** conferir quartil da F1000Research no **SCImago Journal Rank**, com ano de referência explícito; valor Q1 declarado no prompt, mas não verificável no PDF.
3. **Qualis CAPES:** conferir estrato e área/período de avaliação na **Plataforma Sucupira / Qualis CAPES**; valor A2 declarado no prompt, mas não verificável no PDF.
4. **Estado editorial:** caso a RSL exija revisão por pares concluída, verificar se foi publicada versão posterior com pareceres ou aprovação. A única versão avaliada aqui consta como **aguardando revisão por pares**.

**Observação de integridade:** índices de qualidade do periódico e citações recebidas não devem ser confundidos com referências bibliográficas citadas no artigo. Afirmações sobre benefícios de frameworks externos são resultados relatados pela revisão, não medidas observadas diretamente em P01.
