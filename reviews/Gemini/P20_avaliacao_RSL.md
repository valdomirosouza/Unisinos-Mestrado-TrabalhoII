# Avaliação Sistemática de Literatura — Estudo P20

**Artigo avaliado:** *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code*  
**Autores:** Dheer Toprani; Vijay K. Madisetti  
**Arquivo fonte:** `P20-A1-LLM_Agentic_Workflow_for_Automated_Vulnerability_Detection_and_Remediation_in_Infrastructure-as-Code.pdf`

---

## Etapa 0 e Etapa 1 — Extração Bibliométrica e Triagem de Elegibilidade (PRISMA)

### Verificação dos Critérios de Inclusão
- **Ano ≥ 2020:** Sim — 2025 (p. 1 / p. 69175).
- **Publicação ≠ NULL (veículo identificável):** Sim — *IEEE Access*, Volume 13, pp. 69175–69181.
- **Citações ≥ 1:** `[VERIFICAR]` — dado não constante no PDF (verificar em base indexadora: Scopus, Web of Science, IEEE Xplore ou Google Scholar).
- **SJR Q1–Q2:** Informado nos insumos como `Q1` — `[VERIFICAR]` no *Scimago Journal Rank (SJR)* para o periódico *IEEE Access*.
- **Qualis A1–A2:** Informado nos insumos como `A1` — `[VERIFICAR]` na *Plataforma Sucupira / Qualis CAPES* (área Ciência da Computação).

**Resultado da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (confirmação de contagem de citações ≥ 1 em base indexadora e validação formal do SJR Q1 e Qualis A1 nas respectivas bases oficiais). Prossegue-se à extração completa conforme protocolo da RSL.

---

## Tabela A — Bibliométrica (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| P20 | IEEE Access (Vol. 13, pp. 69175–69181) | 2025 | `[VERIFICAR]` (base indexadora: Scopus / IEEE Xplore / Scholar) | Q1 `[VERIFICAR]` (Scimago Journal Rank) | A1 `[VERIFICAR]` (Plataforma Sucupira / Qualis CAPES) | Artigo de pesquisa empírica / Proposta de arquitetura com avaliação experimental (*Research Article*) | `10.1109/ACCESS.2025.3560911` |

---

## Tabela B — Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| P20 | LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code | RQ1 | Parcialmente Respondida | P (0.5) | Seção I (p. 69175–69176); Seção III-A (pp. 69176–69177); Seção IV-A e IV-E (pp. 69177–69178) | **(a) Autonomy definition:** Não formaliza níveis ou taxonomia de autonomia agêntica; propõe automação com *"diminished manual intervention"* em pipelines CI/CD. **(b) Core characteristics:** Apresenta interpretação semântica, uso de base de conhecimento via RAG e geração de relatórios, sem memória episódica ou planejamento dinâmico multi-etapas. **(c) Decision-making model:** Fluxo sequencial determinístico de 3 agentes em pipeline que produz recomendações em Markdown para revisão humana (*developer issue trackers/dashboards*). |
| P20 | LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code | RQ2 | Respondida Plenamente | T (1.0) | Seção III-A e Figura 1 (pp. 69176–69177); Seção IV-A a IV-E (pp. 69177–69178); Seção V-B (pp. 69178–69179) | **(a) Architecture type:** Pipeline multiagente em três estágios (*Retrieval System*, *Vulnerability Detection Agent* e *Report Generation Agent*). **(b) Tools/frameworks:** Especifica *Anthropic Claude Sonnet 3.5 V2* via *Amazon Bedrock Agents*, *Titan Text Embeddings V2*, *Amazon OpenSearch* e parsers YAML/JSON para *AWS CloudFormation*, ancorados em *AWS Well-Architected Framework* e *CIS Benchmarks*. **(c) Advanced capabilities:** Integração RAG com atualização contínua de políticas (mitigando alucinações), normalização estruturada de templates e engenharia de prompt especializada. |
| P20 | LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code | RQ3 | Respondida Plenamente | T (1.0) | Seção V-A a V-F (pp. 69178–69180); Tabela 1 (p. 69179); Tabela 2 (p. 69180) | **(a) Qualitative benefits:** Detecção de vulnerabilidades contextuais compostas (ex.: combinação de políticas IAM), redução de alucinações via RAG e justificativas claras que ampliam a confiança do desenvolvedor. **(b) Quantitative benefits / metrics:** Avaliação em 10 templates CloudFormation (20 vulnerabilidades conhecidas): *Precision* = 85%, *Recall* = 85% (17/20), *F1 Score* = 85%, falsos positivos = ~15% (3 alertas), *over-remediation* = ~5%, e latência média total de 85,1 s por template (2,07 s *Retrieval*, 70,0 s *LLM Analysis*, 13,0 s *Report Gen*). **(c) Evidence level:** Experimento controlado em pequena escala (10 templates anotados por 1 especialista AWS certificado), voltado à prevenção em CI/CD (pré-incidente). |
| P20 | LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code | RQ4 | Parcialmente Respondida | P (0.5) | Seção V-A, V-C, V-D, V-E (pp. 69178–69179); Seção VI-A a VI-C (p. 69180); Seção VII (p. 69181) | **(a) Technical challenges:** Dependência de atualização constante da base RAG (risco de falsos negativos por dados obsoletos), falhas de interpretação em templates com lógica condicional/parametrizada aninhada, taxa de 15% de falsos positivos, 5% de sobre-remediação e latência elevada (80–100 s vs. <5 s de análise estática). **(b) Ethical/governance challenges:** Ausência de discussão sobre ética, *accountability* ou riscos de execução autônoma; trata apenas de aderência a políticas internas e padrões de conformidade. **(c) Governance mechanisms:** Propõe apenas como direção futura o uso de escores de confiança/estimativa de incerteza, *feedback loop* humano e módulos de contexto organizacional. |
| P20 | LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code | RQ5 | Respondida Plenamente | T (1.0) | Seção V-A (p. 69178); Seção VI-A a VI-C (p. 69180); Seção VII (p. 69181) | Mapeia lacunas e trabalhos futuros claros: (1) pipeline de atualização automática da base RAG e estimativa de incerteza/confiança; (2) *parsers* contextuais para lógica condicional e análise híbrida (pré-triagem estática baseada em regras antes do LLM para reduzir latência e custo); (3) estudos de ablação e *feedback loop* de desenvolvedores; (4) ampliação do *benchmark* com repositórios públicos e rotulagem semiautomatizada; e (5) generalização multi-cloud (Azure, GCP, Kubernetes) e outros frameworks IaC (Terraform). |
| **P20** | **TOTAL (SCORE_RQ)** | — | **4.0 / 5.0** | **2P, 3T** | — | Cobertura forte em arquitetura de engenharia (RQ2), métricas empíricas (RQ3) e lacunas de pesquisa (RQ5); cobertura parcial em modelos de autonomia (RQ1) e governança/ética (RQ4). |

---

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P20 | Artigo de pesquisa empírica / Proposta de solução com avaliação experimental | Y (1.0) | P (0.5) | P (0.5) | Y (1.0) | **3.0 / 4.0** | **Alta** |

### Justificativa Analítica de Qualidade (Critérios DARE QA1–QA4)
- **QA1 — Objetivos Claros (Y = 1.0):** A Seção I (pp. 69175–69176) explicita claramente o problema (incapacidade de ferramentas estáticas baseadas em regras de detectar erros de configuração sutis e dependentes de contexto em templates IaC) e o objetivo de propor um fluxo multiagente baseado em LLM e RAG para detecção e remediação proativa em pipelines CI/CD.
- **QA2 — Metodologia Replicável (P = 0.5):** A arquitetura de três agentes e o *stack* tecnológico são especificados (Amazon Bedrock Agents, Anthropic Claude Sonnet 3.5 V2, Titan Text Embeddings V2, Amazon OpenSearch, Seção IV, pp. 69177–69178). Contudo, os 10 templates utilizados no experimento não são disponibilizados, faltam hiperparâmetros exatos (temperatura, *chunking*, *top-k* de recuperação) e os *prompts* completos não são transcritos literalmente. Ademais, a comparação com *CDK-Nag* mencionada na Seção I (p. 69175) não é reportada em tabela comparativa nos resultados.
- **QA3 — Base de Evidências Sólidas (P = 0.5):** Apresenta validação empírica com métricas claras de *Precision*, *Recall*, *F1 Score* e latência por etapa (Tabelas 1 e 2, pp. 69179–69180). Entretanto, o corpus experimental é restrito a 10 templates CloudFormation (contendo de 1 a 12 recursos cada, sendo apenas 5 com vulnerabilidades presentes) e o *ground-truth* foi anotado por um único engenheiro, caracterizando validação empírica preliminar de pequena escala.
- **QA4 — Conclusões Coerentes (Y = 1.0):** As conclusões (Seção VIII, p. 69181) derivam diretamente dos dados experimentais apresentados e o artigo dedica seção específica e rigorosa às limitações técnicas e estratégias de mitigação (Seção VI, p. 69180).

---

## Parecer Final do Revisor

- **Síntese de aderência (RQs e escopo da RSL):** O estudo P20 apresenta uma arquitetura multiagente prática baseada em LLM (*Claude Sonnet 3.5 V2* via *Amazon Bedrock Agents*) e RAG para detecção e recomendação de remediação de vulnerabilidades em *Infrastructure-as-Code* (*AWS CloudFormation*). Embora seu foco recaia sobre segurança preventiva/proativa no ciclo CI/CD (pré-incidente) em vez de resposta a incidentes em tempo de execução (*runtime IR*), o artigo contribui diretamente para as questões de engenharia arquitetural (RQ2), métricas quantitativas de eficácia/latência (RQ3) e desafios práticos como manutenção de conhecimento RAG e sobre-remediação (RQ4 e RQ5), alcançando `SCORE_RQ = 4.0/5.0` e qualidade metodológica `SCORE_QA = 3.0/4.0` (Banda Alta).
- **Recomendação:** **INCLUIR COM RESSALVAS** — O estudo atende aos critérios de qualidade (Banda Alta, 3.0/4.0) e fornece evidências empíricas e arquiteturais valiosas sobre fluxos agênticos para remediação automatizada de configurações em nuvem; a ressalva deve-se ao escopo focado em análise preventiva estática/semântica de IaC em CI/CD (e não em triagem de incidentes operacionais em *runtime*) e ao tamanho reduzido da amostra experimental (10 templates).
- **Pendências de verificação externa:**
  1. **Citações (≥ 1):** Verificar contagem atual de citações nas bases indexadoras (Scopus, Web of Science, IEEE Xplore ou Google Scholar).
  2. **SJR (Q1–Q2):** Confirmar formalmente o quartil Q1 do periódico *IEEE Access* no *Scimago Journal Rank*.
  3. **Qualis (A1–A2):** Confirmar formalmente o estrato A1 na *Plataforma Sucupira / Qualis CAPES*.
