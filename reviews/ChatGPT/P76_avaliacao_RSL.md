# Avaliação crítica do estudo P76 — Ciclo 2 da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**ID:** P76  
**Artigo:** *Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence*  
**Autores:** Ismail et al.  
**Fonte:** *Information*, v. 16, artigo 365, 2025, 35 páginas.  
**DOI:** https://doi.org/10.3390/info16050365  
**Base de avaliação:** exclusivamente o PDF anexado. Os dados externos informados no prompt de triagem não foram tratados como confirmados pelo PDF.

## Etapa 0 — Tabela A: extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P76 | Information | 2025 | [VERIFICAR] | [VERIFICAR] | [VERIFICAR] | Pesquisa aplicada; proposta arquitetural com prova de conceito/piloto experimental controlado | 10.3390/info16050365 |

**Rastreabilidade:** cabeçalho e referência editorial, p. 1; modalidade de validação, seção 4, pp. 24–30. O prompt informa SJR Q2 e Qualis A2, mas estes metadados não são verificáveis no PDF e permanecem **[VERIFICAR]**. Fontes: **Scimago Journal Rank** (SJR), **Plataforma Sucupira / Qualis CAPES** (Qualis) e **base indexadora** (número de citações).

## Etapa 1 — Triagem de elegibilidade (PRISMA)

| Critério | Situação | Evidência |
|---|---|---|
| Publicação em 2020 ou depois | Atende | Publicado em 29 abr. 2025, p. 1. |
| Veículo de publicação identificável | Atende | Periódico *Information*, v. 16, artigo 365, p. 1. |
| Pelo menos uma citação | [VERIFICAR] | Não demonstrável no próprio PDF; consultar base indexadora. |
| SJR Q1–Q2 | [VERIFICAR] | Quartil fornecido pelo prompt, não pelo artigo; consultar Scimago. |
| Qualis A1–A2 | [VERIFICAR] | Estrato fornecido pelo prompt, não pelo artigo; consultar Sucupira/Qualis aplicável. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (citações, SJR e Qualis). A extração prossegue conforme a regra do protocolo para candidatos pendentes. Não há decisão definitiva de inclusão bibliométrica antes dessas verificações.

## Etapa 2 — Tabela B: classificação das questões de pesquisa (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo | Evidência (seção/página) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P76 | Ismail et al. (2025) | RQ1 — Context Definitions | Respondida Plenamente | **T (1,0)** | Seções 2.5.2 e 3.2, pp. 8–16; Figura 2, p. 9; Figura 4, p. 17; seções 3.2.2 e 3.4, pp. 17–24. | Define agentes com autonomia para analisar, decidir e agir, descreve planejamento, memória, uso de ferramentas e decisão contextual; incorpora revisão humana antes da execução no fluxo proposto. A validação piloto também descreve execução autônoma, sugerindo diferentes graus de autonomia conforme a configuração do fluxo. |
| P76 | Ismail et al. (2025) | RQ2 — Engineering Architecture | Respondida Plenamente | **T (1,0)** | Seções 3.2.1–3.4, pp. 16–24; Figuras 4–6, pp. 17–19; Tabela 1, p. 16; Algoritmos 1 e 2, pp. 20–24. | Descreve arquitetura modular em camadas, roteamento entre LLMs, banco vetorial, recuperação por similaridade, decomposição de tarefas, execução remota por WebSocket/Go/shell, avaliação de resultados, fluxos de aprovação e feedback. Observabilidade e guardrails são tratados sobretudo como monitoramento, validação e revisão humana, sem uma especificação completa de controles de segurança de produção. |
| P76 | Ismail et al. (2025) | RQ3 — Evidence Benefits | Respondida Plenamente | **T (1,0)** | Seções 4.1–4.6, pp. 25–30; Figuras 7–10; Tabelas 2–3; seção 5, pp. 30–31. | Relata piloto controlado com Wazuh, enriquecimento de eventos, redução de 38 etapas de um playbook de referência para 10 ações consolidadas e tempos por fase rotulados MTTR (90 s, 60 s, 90 s). Também relata benefícios qualitativos; não mede diretamente a carga cognitiva, e a comparação temporal é indireta e desfavorável ao sistema proposto. |
| P76 | Ismail et al. (2025) | RQ4 — Challenges & Ethics | Parcialmente Respondida | **P (0,5)** | Seção 3.2.1, p. 17; seção 3.2.2, pp. 19–20; seção 4.5 e Tabela 3, pp. 29–30; seções 5–6, pp. 30–31. | Expõe falhas por privilégios insuficientes, limitações de integração e de resposta ativa por WebSocket, erros de classificação, interpretabilidade, dependência dos dados e necessidade de aprovação/intervenção humana. Entretanto, não formaliza uma política abrangente de governança, responsabilização, controle de privilégios, auditoria ou modelo de ameaças para agentes em produção. |
| P76 | Ismail et al. (2025) | RQ5 — Research Gaps | Respondida Plenamente | **T (1,0)** | Seção 4.1, p. 25; seção 4.6, p. 30; seções 5–6, pp. 30–31. | Aponta necessidade de benchmarks diretos e métricas operacionais, validação em conjuntos de ataques reais e ambientes diversos, maior explicabilidade, mecanismos human-in-the-loop, aprendizagem contínua e expansão para phishing, escalonamento de privilégios e ransomware. A lacuna de dados abertos para comparação do MTTR é reconhecida. |
| **P76** | **Total** | **SCORE_RQ** | | **4,5 / 5,0** | | **Cobertura temática forte; evidência experimental restrita a cenário controlado.** |

### Observações críticas por RQ

**RQ1.** O trabalho usa uma definição operacional de agência: percepção/análise de alertas, planejamento de mitigação, escolha de ferramentas, execução e avaliação. A Figura 4 prevê autorização por analista antes da execução, enquanto a seção 4.1 relata um piloto autônomo sem intervenção humana. Essa diferença deve ser entendida como variação do grau de autonomia, e não como prova de que todos os cenários empregam a mesma política de supervisão.

**RQ2.** A Figura 5 separa planejamento/gestão de dados, orquestração/decomposição e ferramentas/execução. A seção 3.2.2 especifica os modelos **Llama-3.3-70B-Instruct** e **DeepSeek-R1-Distill-Llama-70B**. O artigo traz fluxos e algoritmos, mas não apresenta todos os parâmetros indispensáveis para reprodução integral, como configuração completa de inferência, dados, prompts e ambiente de execução.

**RQ3.** A Tabela 2 compara **38 etapas** do playbook XSOAR citado com **10 ações de alto nível** do agente: a redução indica consolidação e abstração das tarefas, não redução comprovada equivalente do tempo, esforço ou complexidade de execução. Na seção 4.6 são reportados aproximadamente **1 min 30 s** para análise, **1 min** para atualização de comandos e **1 min 30 s** para compilação. Os valores de referência extraídos de outro estudo são **45 s, 30 s e 45 s**, respectivamente. O próprio artigo destaca que a disponibilidade limitada de dados das plataformas alternativas impede comparação direta e explicação conclusiva da diferença. Embora denomine as medições de MTTR, são tempos por atividade, sem evidência suficiente de que representem um MTTR ponta a ponta ou de que permitam inferir redução de MTTR.

**RQ4.** A Figura 6 prevê *Human Interrupt* antes da execução. A Tabela 3 documenta uma sequência de falhas de autenticação por `sudo` que culmina em solicitação de intervenção humana. Isso fornece evidência concreta de limite operacional e escalonamento, mas não demonstra uma arquitetura robusta de autorização, isolamento ou segurança dos comandos gerados.

**RQ5.** Os próprios autores propõem medir em trabalhos futuros tempos de resposta, taxas de êxito da mitigação e redução da participação de analistas, com comparação a plataformas SOAR tradicionais. Isso limita conclusões sobre benefício quantitativo já demonstrado.

## Etapa 3 — Tabela C: avaliação da qualidade metodológica (Tabela 7)

**Escala:** Y = 1,0; P = 0,5; N = 0,0. **Bandas:** Alta ≥ 3,0; Média 1,5–2,5; Baixa < 1,5.

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P76 | Pesquisa aplicada com prova de conceito e piloto experimental controlado | **Y (1,0)** | **P (0,5)** | **Y (1,0)** | **P (0,5)** | **3,0 / 4,0** | **Alta** |

### Justificativa detalhada

- **QA1 — Y (1,0), objetivos claros.** Resumo e introdução (pp. 1–2) identificam limitações de playbooks rígidos de SOAR e propõem uma plataforma de hiperautomação com LLMs/agentes e o framework IVAM. O problema e a contribuição pretendida são explícitos.
- **QA2 — P (0,5), metodologia parcialmente replicável.** As seções 3.1–3.4 (pp. 10–24), as Figuras 3–6 e os Algoritmos 1–2 expõem estrutura, componentes e fluxos. A seção 4.1 (p. 25) descreve VirtualBox, Ubuntu 22.04.5 LTS, processador Intel Core i7 de 13ª geração e Wazuh. Faltam, porém, condições experimentais suficientemente completas e parâmetros essenciais para replicar integralmente os resultados, como dados de entrada, configurações completas dos LLMs e repetição/amostragem dos tempos.
- **QA3 — Y (1,0), evidência empírica existente, mas limitada.** A seção 4 (pp. 24–30) apresenta uma prova de conceito executada em ambiente controlado, com alertas processados, automação, falhas reais de permissões, avaliação relativa de risco e valores de tempo. A nota Y reconhece a existência de validação empírica, **não** implica generalização nem superioridade demonstrada.
- **QA4 — P (0,5), conclusões parcialmente proporcionais às evidências.** As seções 5 e 6 (pp. 30–31) reconhecem riscos de classificação, interpretabilidade, restrições de integração e validação limitada. Contudo, alegações amplas de eficiência e efetividade não são plenamente sustentadas por comparação experimental direta; os tempos reportados na seção 4.6 são maiores que as referências bibliográficas utilizadas.

## Parecer final do revisor

O P76 tem **aderência direta e elevada** ao escopo da RSL por investigar Agentic AI aplicada à orquestração e execução da resposta a incidentes em SOC/SOAR. O framework **IVAM** estrutura investigação, validação quantitativa de riscos e monitoramento ativo, enquanto a arquitetura incorpora LLMs, memória vetorial, ferramentas e mecanismos de intervenção humana. A validação piloto em força bruta SSH apresenta execução observável e medidas operacionais, mas não estabelece superioridade em MTTR, generalização a outros incidentes ou redução quantitativa da carga cognitiva. A ausência de comparação controlada direta e de especificação integral de replicabilidade deve acompanhar a extração do estudo.

**Recomendação:** **INCLUIR COM RESSALVAS**, condicionada à confirmação dos três critérios bibliométricos pendentes. Manter no corpus se o número de citações for ≥ 1, o SJR for Q1 ou Q2 e o Qualis for A1 ou A2, conforme o protocolo da RSL. Caso alguma dessas condições falhe, reclassificar a elegibilidade.

**Pendências externas obrigatórias:**
1. **Citações [VERIFICAR]:** verificar pelo menos uma citação em base indexadora.
2. **SJR [VERIFICAR]:** consultar Scimago Journal Rank e confirmar quartil aplicável ao veículo/período.
3. **Qualis [VERIFICAR]:** consultar Plataforma Sucupira / Qualis CAPES e confirmar enquadramento no estrato requerido.

**Advertência de interpretação:** no estudo, “MTTR” é explicitado como *Mean Time to Remediate*. Não equiparar automaticamente esses valores a *Mean Time to Respond*, *Mean Time to Repair* ou ao MTTR end-to-end adotado em outros trabalhos. Comparações precisam explicitar definição, fases incluídas e protocolo de medição.
