# Avaliação do estudo P83 — Ciclo 2 da RSL

**Artigo:** Ismail et al. (2025), *Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot*.

**Protocolo:** `prompt-P83.md`; análise restrita ao PDF fornecido. As classificações dizem respeito ao conteúdo demonstrado pelo artigo, não à capacidade potencial da tecnologia.

## Etapa 0 — Tabela A: Extração bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P83 | *Sensors*, 25(3), artigo 870 | 2025 | [VERIFICAR] | [VERIFICAR] (Q1 informado no protocolo, não comprovável no PDF) | [VERIFICAR] (A1 informado no protocolo, não comprovável no PDF) | Pesquisa aplicada com desenvolvimento de protótipo e avaliação experimental por simulação | https://doi.org/10.3390/s25030870 |

**Evidência:** capa, p. 1, para periódico, ano e DOI; seções 3 e 4, pp. 11–21, para caracterização metodológica.

## Etapa 1 — Triagem de elegibilidade

| Critério | Resultado | Evidência / pendência |
|---|---|---|
| Ano ≥ 2020 | Atendido | Publicado em 31 jan. 2025, p. 1. |
| Publicação identificável | Atendido | *Sensors*, v. 25, artigo 870, p. 1. |
| Citações ≥ 1 | [VERIFICAR] | Contagem de citações não demonstrada no PDF; consultar base indexadora. |
| SJR Q1–Q2 | [VERIFICAR] | O protocolo informa Q1, porém requer confirmação em SCImago Journal Rank. |
| Qualis A1–A2 | [VERIFICAR] | O protocolo informa A1, porém requer confirmação na Plataforma Sucupira / Qualis CAPES. |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações, SJR e Qualis)**. A extração prossegue, conforme a regra do protocolo para estudos pendentes.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P83 | SERC / Wazuh RAG Copilot | RQ1 — Context Definitions | Parcialmente Respondida | P (0,5) | Seções 2.7–2.8, pp. 9–10; seção 3.4, pp. 15–16; seção 4.1, pp. 16–17 | A assistência contextual e o diálogo com o analista sustentam um modelo de decisão apoiada por LLM. Não há definição operacional de autonomia agêntica, planejamento independente, memória persistente ou política de supervisão para ações autônomas. |
| P83 | SERC / Wazuh RAG Copilot | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | Seções 3.1–3.4, pp. 11–16; Figuras 3–5; Tabelas 2–5 | Arquitetura RAG e tecnologias são concretas: Wazuh, Qdrant, embeddings BAAI/bge-large-en-v1.5, extração com Pixtral, GPT-4o/Pixtral 12B e coleções MITRE/NIST/guias de IR. Há recuperação de conhecimento e interface conversacional, mas não se evidenciam orquestração multiagente, guardrails, observabilidade de agentes ou execução autônoma de ferramentas. |
| P83 | SERC / Wazuh RAG Copilot | RQ3 — Evidence Benefits | Respondida Plenamente | T (1,0) | Seções 4.1–4.3, pp. 16–21; Figuras 6–12 | Relata benefícios funcionais qualitativos, apresenta avaliação quantitativa por similaridade de cosseno e BERTScore (precisão, recall e F1), e identifica a natureza da evidência como simulação de ataques com comparação a um ground truth. A cobertura da RQ é plena **quanto às três subdimensões**, não significando comprovação de redução de tempo operacional ou carga cognitiva. |
| P83 | SERC / Wazuh RAG Copilot | RQ4 — Challenges & Ethics | Parcialmente Respondida | P (0,5) | Seção 2.8, pp. 9–10; seção 5, p. 21 | Discute limitações de adaptação e atualização do conhecimento, variação de desempenho entre modelos e necessidade de melhorar robustez. Não apresenta tratamento substantivo de accountability, privacidade dos logs, autorização de ações, riscos de prompt injection ou mecanismos específicos de governança do copilot. |
| P83 | SERC / Wazuh RAG Copilot | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | Seção 5, p. 21 | Propõe explicitamente fine-tuning com dados do domínio, treinamento específico por cenário (phishing e ransomware), treinamento adversarial, aprendizagem ativa com especialistas e integração futura com SOAR para automação ponta a ponta. A ausência de proposta de benchmark operacional e governança é uma lacuna adicional identificada pelo revisor, não uma contribuição alegada pelos autores. |
| **P83** | **TOTAL** | **SCORE_RQ** | | **3,5 / 5,0** | | **P + P + T + P + T** |

**Detalhamento de RQ3:** na Figura 9 e no texto da seção 4.3 (p. 19), o artigo relata pico de similaridade de cosseno de 75,81% para OpenAI no cenário 8 e 71,69% para Pixtral no cenário 9. Nas Figuras 10–12 (pp. 20–21), Pixtral apresenta precisão de 84,5%–87,0%, recall de 85,6%–87,5% e F1 de 85,4%–87,2%. Esses indicadores avaliam concordância das respostas geradas com a referência textual; não constituem métricas de tempo de resposta nem validam a correção operacional de todas as recomendações. O texto menciona seis tipos de ataque e doze cenários; a descrição enumera cinco categorias, inconsistência que prejudica a transparência experimental (seção 4.2, pp. 18–19).

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---:|---|
| P83 | Protótipo aplicado com avaliação experimental por simulação | Y (1,0) | P (0,5) | Y (1,0) | P (0,5) | **3,0 / 4,0** | **Alta** |

### Justificativas por critério

**QA1 — Objetivos claros: Y (1,0).** O resumo e a introdução (pp. 1–2) delimitam a dificuldade de responder a eventos de segurança, a carga de análise manual e a proposta de um copilot RAG integrado ao Wazuh. Ressalva conceitual: o artigo não apresenta uma solução agêntica autônoma no sentido estrito.

**QA2 — Metodologia replicável: P (0,5).** As seções 3.1–3.4 (pp. 11–16) descrevem modelos, Qdrant, estratégia de chunking, três coleções, prompts e configuração de geração (Tabela 3: temperatura 0,1; top-k 50; top-p 0,9; máximo 4096 tokens). A seção 4.2 (pp. 17–19) descreve Wazuh e Atomic Red Team. Contudo, falta uma especificação integral verificável do conjunto de cenários e de detalhes operacionais suficientes para repetição rigorosa da experiência; também há divergência entre o número de tipos de ataque e as categorias enumeradas.

**QA3 — Base de evidências sólidas: Y (1,0).** Há implementação integrada (Figura 6, p. 17) e experimento com simulações de ataques (Figuras 7–8, pp. 17–18), comparando respostas a um ground truth por métricas quantitativas (Figuras 9–12, pp. 19–21). Este Y reconhece a existência de validação empírica, sem transformar métricas semânticas em prova de eficácia operacional de um SOC real.

**QA4 — Conclusões coerentes: P (0,5).** A discussão (seção 5, p. 21) reconhece desempenho variável do modelo OpenAI, estabilidade relativa de Pixtral e espaço para melhorias. As observações refletem os resultados apresentados. Entretanto, a fundamentação não permite extrapolar a redução efetiva de carga do analista, MTTR ou automação integral, e a discussão de limitações metodológicas e riscos operacionais é restrita.

## Parecer final do revisor

**Síntese.** O P83 é altamente pertinente à dimensão de *copilot* com RAG para resposta a incidentes em SOC, pois demonstra integração ao Wazuh e contextualização de recomendações por MITRE ATT&CK, NIST CSF e guias de resposta. A arquitetura e a simulação oferecem evidências úteis para RQ2 e RQ3. Seu enquadramento em Agentic AI é, porém, parcial: há assistência conversacional, sem demonstração de autonomia de execução, ciclo de planejamento ou mecanismos agênticos robustos de governança. As métricas de similaridade não permitem inferir ganhos de MTTD, MTTR, qualidade da decisão humana ou redução da carga cognitiva.

**Recomendação: INCLUIR COM RESSALVAS**, condicionada à confirmação dos critérios bibliométricos obrigatórios. Incluir como evidência de **copilot RAG de apoio à decisão na resposta a incidentes**, distinguindo-o explicitamente de sistemas agênticos autônomos. Não extrapolar resultados de correspondência textual para efetividade operacional.

**Pendências de verificação externa:** (1) pelo menos uma citação em base indexadora; (2) quartil do periódico em **SCImago Journal Rank**; (3) estrato e enquadramento temporal do periódico na **Plataforma Sucupira / Qualis CAPES**. Os valores Q1 e A1 constantes no prompt são metadados fornecidos, **não confirmados pelo PDF**.

---

*Fonte única utilizada: artigo PDF P83, 26 páginas. Os metadados externos fornecidos no protocolo foram explicitamente sinalizados como não verificados.*
