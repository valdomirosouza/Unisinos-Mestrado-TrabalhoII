# Parecer de avaliação integral — P97

**Estudo:** Alhumaidi, A. Y.; Al-Qadda, F. A.; Alsumayt, A.; Alshammari, M. (2026). *Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Conceptual Framework*. **Network**, 6, 84. DOI: https://doi.org/10.3390/network6040084.

**Protocolo aplicado:** prompt-P97.md; avaliação temática das RQ1–RQ5 (T=1; P=0,5; N=0) e apreciação QA1–QA4 (Y=1; P=0,5; N=0). **Nota metodológica:** o prompt recebido não explicita uma matriz PICOC formal nem enuncia os quatro critérios QA; para não atribuir definições inexistentes ao protocolo, o PICOC abaixo é operacionalizado a partir das cinco RQs, e QA1–QA4 são dimensões analíticas declaradas neste parecer, cuja equivalência ao template `templates/review.md` não pôde ser verificada porque o template não foi fornecido.

## Síntese do parecer

**Decisão: Incluir c/ ressalvas (evidência experimental exclusivamente sintética e parcial; sem validação de sistema agêntico fim a fim nem de desempenho em produção).** A contribuição principal é uma arquitetura conceitual de SOC-as-a-Service com IA agêntica e um plano transversal de segurança, governança e confiança. O estudo agrega revisão temática de 33 referências e quatro experimentos de simulação. Existe comparação quantitativa **executada no ambiente simulado** com baselines concretos (SOC manual, narrow-AI e configuração agentic governada), mas a redução de tempo projetada não constitui evidência de MTTR/MTTD real.

## Tabela A — Identificação e PICOC

| Campo | Extração e decisão | Evidência |
|---|---|---|
| ID | P97 | Identificação do protocolo |
| Título | Agentic AI-Driven SOC-as-a-Service for Optimizing Incident Response in Cloud Environments: A Conceptual Framework | p. 1 |
| Autores | Abdulaziz Y. Alhumaidi; Faisal A. Al-Qadda; Albandari Alsumayt; Majid Alshammari | p. 1 |
| Ano / veículo / DOI | 2026; *Network*, 6, 84; 10.3390/network6040084 | p. 1 |
| Tipo de estudo | Misto: revisão de literatura em duas fases, síntese temática, proposta arquitetural e quatro experimentos simulados | §§3, 5 e 6, pp. 3–29 |
| Population | Analistas e operações de SOC/SOCaaS em ambientes de nuvem; tratamento de alertas e incidentes de segurança | §§1–2, pp. 1–3 |
| Intervention | IA agêntica para triagem, recuperação contextual, raciocínio multietapas, orquestração limitada por políticas, aprovação humana e auditoria | §5.4, pp. 18–21 |
| Comparison | **Sim, em simulação:** modelo manual vs. narrow-AI vs. agentic governado no experimento 3; recuperação com vs. sem corpus no experimento 2; políticas de triagem no experimento 1 | §§6.2–6.4, pp. 23–27 |
| Outcomes | Tempo médio de resposta modelado; toques do analista; supressão de alertas; vazamento de ameaças; acurácia de correspondência com playbooks; completude de auditoria. **Sem medição de carga cognitiva ou MTTR/MTTD em produção** | §6, pp. 23–29 |
| Context | SOC de segurança cibernética em cloud e SOCaaS multitenant; relevante por analogia para operações SRE, mas não é avaliação direta de incidentes de confiabilidade de serviços | §§1, 5, pp. 1–2, 16–22 |
| Corpus de revisão | 23 estudos legados + 10 de atualização Scopus = 33; 55/65 relatórios não recuperados na atualização | §§3.1–3.4, pp. 3–5 |
| Indexação / bibliometria | OpenAlex 0; Crossref 0; Scopus **não indexado** (dados fornecidos pela triagem, verificação em 27/10/2026). Qualis derivado **A2**, percentil 79%, SJR N/D. Não somar contagens por bases | Prompt P97; não revalidado externamente |
| Regra de estrato | PDR-0006 referente a conference papers: não aplicável ao artigo de periódico. PDR-0007: nenhuma ressalva **de estrato** para A2 aferido conforme triagem | Prompt P97 |
| Aderência temática | Alta para arquitetura, governança, autonomia limitada e incident response em segurança; indireta para SRE/MTTR e carga cognitiva | §§4–7 |

## Tabela B — Atendimento às questões de pesquisa

| Questão | Nota | Evidência âncora (seção/página) | Fundamentação |
|---|---:|---|---|
| **RQ1 — Contexto/definições** | **T (1,0)** | §§4.4–4.5, pp. 10–11; §§5.2–5.3, pp. 16–18 | Caracteriza decomposição de tarefas, raciocínio multietapas, recuperação contextual, uso de ferramentas e autonomia limitada. Explicita o papel da supervisão humana e a separação entre recomendação do agente e autorização externa. Não apresenta taxonomia formal exaustiva de níveis de autonomia, mas atende substancialmente à pergunta. |
| **RQ2 — Engenharia/arquitetura** | **T (1,0)** | §§5.1, 5.3–5.5, pp. 16–22; Fig. 4 e Tabela 4, pp. 18–19 | Propõe seis camadas: ingestão de telemetria; triagem/enriquecimento; recuperação/contexto; raciocínio/orquestração; governança/supervisão; execução/auditoria. Um plano transversal prevê isolamento de locatários, proveniência, restrições de ferramentas e autorização determinística. Trata-se de **arquitetura proposta**, não demonstrada em produção. |
| **RQ3 — Evidência/benefícios** | **T (1,0)** | §§6.2–6.5, pp. 23–28; Tabelas 5–8 | Contém comparação simulada com baselines declarados e resultados quantitativos: tempo médio de 59,5 min (manual), 23,4 min (narrow-AI), 8,8 min (agentic governado), fator 6,8; 59,5% de supressão conservadora de alertas com 4,81% de ameaças indevidamente suprimidas; correspondência top-1 de playbooks de 0,317 para 0,850. **Nota mede cobertura da RQ, não força probatória**. Não reporta redução observada de carga cognitiva, MTTD ou MTTR operacional. |
| **RQ4 — Desafios/ética** | **T (1,0)** | §§4.7–4.8, pp. 12; §§5.1, 5.4.1, pp. 16–19; §6.6, p. 28 | Examina prompt injection, envenenamento de recuperação, manipulação de chamadas de ferramentas, vazamento entre locatários, alucinações, autorização, transparência, auditabilidade e responsabilização; reconhece que o plano de segurança não foi testado adversarialmente. |
| **RQ5 — Lacunas** | **T (1,0)** | §§6.6–7, pp. 28–30 | Define agenda explícita: protótipos operacionais, comparações entre IA estreita/LLM/RAG/agentes, teste adversarial, isolamento multitenant, governança por políticas, fatores humanos, ampliação do corpus e replicabilidade. |
| **Total** | **5,0/5,0 — Alta** | | A pontuação mede **relevância e cobertura**, não validade externa dos experimentos. |

## Tabela C — Avaliação da qualidade (critérios operacionais explicitados)

| Critério analítico | Nota | Justificativa e evidência |
|---|---:|---|
| **QA1 — Objetivos e contribuição claros** | **Y (1,0)** | Objetivos e cinco questões próprias são explicitados; contribuições e escopo conceitual delimitados em §2, p. 3. |
| **QA2 — Método suficientemente reproduzível** | **P (0,5)** | Atualização Scopus documenta 2181 registros, 70 duplicatas e 10 estudos adicionados; experimentos declaram parâmetros. Contudo, faltam contagens intermediárias dos 23 estudos legados; não houve registro prospectivo do protocolo e 55 dos 65 textos procurados na fase 2 não foram recuperados (§§3.1–3.8, pp. 3–7; §7, p. 29). |
| **QA3 — Evidência adequada à força das conclusões** | **P (0,5)** | Há baselines e indicadores quantitativos, mas baseados em geração sintética, TF–IDF e filas modeladas, sem execução real fim a fim da arquitetura; vários riscos de validade foram reconhecidos (§§6.2–6.6, pp. 23–28). Adequado para plausibilidade inicial, insuficiente para inferência de eficácia operacional. |
| **QA4 — Limitações, riscos e implicações transparentes** | **Y (1,0)** | Apresenta ameaças à validade, limitações de cobertura, ausência de teste de resistência a ataques e agenda detalhada de pesquisa (§§6.6–7, pp. 28–30). |
| **Total analítico** | **3,0/4,0** | Avaliação com critérios operacionais deste parecer, **não** apresentada como rubrica QA original indisponível. |

## Análise crítica das evidências

**Experimento 1 (triagem; pp. 23–24).** Classificador Random Forest treinado sobre 20.000 eventos sintéticos, com conjunto de teste de 6.000 eventos; macro-F1 0,907, acurácia 0,945. Política conservadora reduz encaminhamento de alertas em 59,5%, com 4,81% de ameaças não escaladas. O componente avaliado é ML supervisionado, não IA agêntica completa.

**Experimento 2 (recuperação; pp. 24–25).** Sessenta descrições e doze playbooks; TF–IDF melhora correspondência top-1 de 31,7% para 85,0% e top-3 de 58,3% para 93,3%. Compara recuperação lexical com condição sem corpus; **não** compara RAG denso atual ou agente implantado.

**Experimento 3 (orquestração governada; pp. 25–27).** Simulação de eventos discretos sobre 2.000 incidentes com modelos manual, narrow-AI e agentic governado. Médias: 59,5; 23,4; e 8,8 minutos, respectivamente. Essa comparação cumpre o critério *Comparison* do prompt, porém os tempos de serviço e o comportamento dos componentes são assumidos, não observados. A métrica denominada *mean response time* não pode ser automaticamente equiparada a MTTR ou MTTD reais.

**Experimento 4 (auditoria; pp. 27–28).** Simulação de rastros de execução; 95,5% de cadeias completas e sobrecarga média de 1,79%. A completude de campos não demonstra inviolabilidade ou não repúdio criptográfico.

**Risco metodológico central.** O plano transversal de segurança não foi implementado nem submetido a testes adversariais. As simulações não incorporam integralmente falhas de ferramentas, variação de latência de inferência, limites de contexto, iterações de raciocínio, fadiga dos analistas ou adaptação do adversário (§6.6, p. 28). Logo, resultados promissores devem ser registrados como **viabilidade interna condicionada**.

**Qualidade da revisão secundária.** A fase legada (23 estudos) não conserva trilha completa de triagem; na atualização, 55 de 65 relatórios não foram recuperados. Há vieses de cobertura e recuperação. Seis fontes legadas eram preprints (18,2% do corpus total), exigindo prudência na síntese (§7, p. 29). A revisão é útil para mapear padrões, mas não estabelece metanálise de eficácia.

## Contribuição para a dissertação e extração recomendada

O artigo sustenta a construção de um **copiloto agêntico governado para resposta a incidentes**, especialmente nos eixos de contexto operacional, recuperação com proveniência, autorização externa ao modelo, supervisão humana, auditoria de decisões e separação entre dados observados e comandos executáveis. Seus controles e a arquitetura em camadas podem subsidiar requisitos de um protótipo aplicado a ambientes SRE. No entanto, a generalização de resultados de SOC de cibersegurança para incidentes de disponibilidade, performance e confiabilidade de serviços deve ser **tratada como transferência conceitual**, não como comprovação empírica.

Para a matriz de extração da RSL, classificar: **tipo híbrido (revisão + framework + simulação)**; **maturidade empírica: simulação sintética**; **baseline: sim, simulado**; **benefício quantitativo: condicionado**; **MTTD real: não medido**; **MTTR real: não medido**; **carga cognitiva: não mensurada**; **governança/guardrails: arquiteturalmente especificados**; **robustez adversarial: não testada**; **validação em produção: ausente**.

## Rastreabilidade e interpretação do estrato

Os valores bibliométricos e o estrato A2 foram recebidos **como dados da triagem** e não confirmados independentemente nesta avaliação. A indicação simultânea de periódico A2 por percentil e de estudo individual não indexado na Scopus exige manter separados **estrato do veículo** e **indexação do documento**; uma condição não prova a outra. Pelas premissas fornecidas, **não há ressalva obrigatória de estrato** no sentido do PDR-0007, mas permanecem as ressalvas de validade metodológica.

## Recomendação final

**Incluir c/ ressalvas (arquitetura conceitual robusta e aderente às RQ1–RQ5, com baselines comparativos executados somente em simulações sintéticas; ausência de implementação e validação agêntica fim a fim, de eficácia em produção, de testes adversariais e de medições reais de MTTD, MTTR ou carga cognitiva).**
