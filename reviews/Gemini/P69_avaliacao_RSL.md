# Avaliação RSL: Ciclo 2 — Estudo P69

**Artigo:** WAUC: A Multi-Modal Database for Mental Workload Assessment Under Physical Activity  
**Autores:** Isabela Albuquerque, Abhishek Tiwari, Mark Parent, Raymundo Cassani, Jean-François Gagnon, Daniel Lafond, Sébastien Tremblay, Tiago H. Falk  
**Periódico:** *Frontiers in Neuroscience* (Seção Neural Technology), Vol. 14, Artigo 549524, 2020  
**DOI:** `10.3389/fnins.2020.549524`  
**RSL Alvo:** "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura" (PPGCA Unisinos)

---

## 1. Contexto e Parâmetros de Entrada (Prompt)

- **Papel:** Pesquisador em Computação Aplicada do PPGCA da Unisinos, orientado por Doutor em Ciência da Computação, especialista em RSL em Engenharia de Software segundo Kitchenham (2009) e critérios DARE (QA1–QA4).
- **ID atribuído:** P69
- **Qualis declarado:** A3 (derivado do percentil Scopus 74.0%, regra CAPES 2025–2028)
- **SJR Quartil declarado:** Q2
- **Ressalvas de triagem prévia:** RESSALVA DE ESTRATO (Qualis A3, emenda de protocolo 2026-09-09); cluster carga cognitiva; fora do domínio TI.

---

## 2. Extração Bibliométrica e Triagem

### 2.1 Extração Bibliométrica
- **ID:** P69
- **Periódico/Conferência:** Frontiers in Neuroscience (Seção Neural Technology)
- **Ano:** 2020 (Publicado em 01 de dezembro de 2020)
- **Tipo de Estudo:** Artigo de Pesquisa Original / Apresentação de Dataset Multimodal e Estudo Experimental de Benchmark (Neurociência / Ergonomia Cognitiva)
- **DOI:** `10.3389/fnins.2020.549524`
- **Citações:** `[VERIFICAR]` (Bases indexadoras: Scopus / Web of Science / Google Scholar)
- **SJR (Quartil):** Q2 `[VERIFICAR]` (Fonte: SCImago Journal Rank)
- **Qualis (Estrato):** A3 `[VERIFICAR]` (Fonte: Plataforma Sucupira / Qualis CAPES)

### 2.2 Triagem de Elegibilidade
- **Ano ≥ 2020:** Sim (2020).
- **Publicação ≠ NULL:** Sim (*Frontiers in Neuroscience*).
- **Citações ≥ 1:** `[VERIFICAR]` (Pendente de checagem em base indexadora).
- **SJR Q1–Q2:** Sim (Q2 declarado no insumo).
- **Qualis A1–A2:** **Ressalva de Estrato** — Qualis A3 (percentil Scopus 74.0%). Pela regra geral seria excluído, mas atende à exceção do protocolo de emenda de 2026-09-09 para estudos do *cluster* de carga cognitiva.
- **Veredito da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações, validação do estrato Qualis/SJR e aplicação formal da emenda de protocolo). Prossegue-se para a extração analítica.

---

## 3. Extração e Classificação das Questões de Pesquisa (RQs)

### RQ1 — Context Definitions
- **Veredito:** Não tem conteúdo suficiente (N = 0.0)
- **Evidência:** Seção 1 (pp. 1–2)
- **Análise:** O trabalho fundamenta-se no conceito de *Operator Functional State* (OFS) e na avaliação da carga de trabalho mental (*Mental Workload* - MW) sob estresse físico. Não define níveis de autonomia agêntica, modelos de tomada de decisão baseados em LLMs/agentes de software ou processos de supervisão humana (HITL/HOTL) voltados à Engenharia de Software ou resposta a incidentes.

### RQ2 — Engineering Architecture
- **Veredito:** Não tem conteúdo suficiente (N = 0.0)
- **Evidência:** Seção 3.5, Tabela 1 (pp. 5–7)
- **Análise:** Descreve uma arquitetura de sensoriamento fisiológico corporal (eletrodos de EEG Enobio, cinta BioHarness 3 e pulseira Empatica E4) sincronizada por meio do software de streaming MuLES. Não apresenta componentes de arquitetura de software agêntico, orquestração multiagente, uso de ferramentas/APIs em produção ou observabilidade de telemetria de infraestrutura.

### RQ3 — Evidence Benefits
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Seções 4.2, 5.1 e 5.2, Tabelas 2, 3 e 4 (pp. 8–12)
- **Análise:** Traz farta evidência empírica quantitativa sobre monitoramento e predição de carga cognitiva e fadiga humana (NASA-TLX, Borg, modelos Random Forest com métricas de AUC para espectro EEG, HRV/ECG, respiração e GSR). Embora seja relevante para o *cluster* de carga mental/fadiga do operador em sistemas críticos, não aborda métricas de incident response de TI (ex.: MTTD, MTTR, fadiga de alertas operacionais de software).

### RQ4 — Challenges & Ethics
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Seções 3.1, 4.2 e 5.2 (pp. 4, 8, 9–11)
- **Análise:** Trata de desafios técnicos cruciais como variabilidade inter-sujeito (*cross-subject variability*), drástica queda de desempenho em validação *leave-one-subject-out* (AUC ~0.50), contaminação por ruídos/artefatos de movimento e conformidade com comitês de ética em pesquisa com humanos. Não abrange vulnerabilidades de segurança de IA, *jailbreaks* ou governança de agentes autônomos em produção.

### RQ5 — Research Gaps
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Seção 5.5 e Seção 6 (pp. 12–13)
- **Análise:** Enumera lacunas claras para aprimoramento da avaliação do estado funcional do operador: desenvolvimento de algoritmos de remoção de artefatos em sensores de baixa densidade, uso de *deep learning* para representações invariantes ao usuário, modelagem contínua da intensidade de carga mental e fusão sensorial resiliente a variações de SNR. Não aborda lacunas específicas de DevOps/SRE ou copilotos de TI.

**SCORE_RQ TOTAL:** **1.5 / 5.0**

---

## 4. Avaliação de Qualidade (Critérios DARE / Kitchenham)

- **QA1 (Objetivos Claros): Y = 1.0**  
  O objetivo de suprir a carência de bases de dados abertas para avaliação multimodal de carga mental sob estresse físico e fornecer um benchmark de validação é explicitado com clareza exemplar.
- **QA2 (Metodologia Replicável): Y = 1.0**  
  Metodologia experimental descrita minuciosamente: especificação completa dos equipamentos e frequências de amostragem, alocação de canais no sistema 10-20, parâmetros operacionais da bateria MATB-II, métodos de filtragem (wICA, Chebyshev, detecção QRS de Pan-Tompkins), janelamento temporal e disponibilização pública de scripts e dados brutos.
- **QA3 (Base de Evidências Sólidas): Y = 1.0**  
  Validação empírica de grande porte com 48 voluntários submetidos a desenho fatorial balanceado ($2\text{ níveis de MW} \times 3\text{ níveis de esforço físico} \times 2\text{ tipos de aparelho}$), apoiada por ANOVA mista de medidas repetidas e algoritmos supervisionados (*Random Forest*).
- **QA4 (Conclusões Coerentes): Y = 1.0**  
  As conclusões decorrem com consistência dos experimentos, detalhando de forma transparente o desafio de generalização cruzada entre indivíduos e os efeitos de acoplamento entre esforço físico e cognitivo.

**SCORE_QA TOTAL:** **4.0 / 4.0**  
**Banda de Qualidade:** **Alta** ($\ge 3.0$)

---

## 5. Tabelas Consolidadas da RSL

### Tabela A — Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P69 | Frontiers in Neuroscience | 2020 | [VERIFICAR] | Q2 [VERIFICAR] | A3 [VERIFICAR] | Estudo Experimental / Base Multimodal | 10.3389/fnins.2020.549524 |

### Tabela B — Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| P69 | Albuquerque et al. (2020) | RQ1 | Não tem conteúdo suficiente | N | Seção 1 (pp. 1–2) | Foca no estado funcional humano e carga mental; não conceitua agentes de IA, autonomia ou tomada de decisão em TI. |
| P69 | Albuquerque et al. (2020) | RQ2 | Não tem conteúdo suficiente | N | Seção 3.5, Tabela 1 (pp. 5–7) | Detalha infraestrutura de biossensores e MuLES; sem orquestração de software agêntico ou observabilidade de logs. |
| P69 | Albuquerque et al. (2020) | RQ3 | Parcialmente Respondida | P | Seções 4.2, 5.1 e 5.2, Tabelas 2–4 (pp. 8–12) | Apresenta métricas empíricas rigorosas de carga cognitiva (NASA-TLX, Borg, AUC), mas fora do contexto de resposta a incidentes. |
| P69 | Albuquerque et al. (2020) | RQ4 | Parcialmente Respondida | P | Seções 3.1, 4.2 e 5.2 (pp. 4, 8, 9–11) | Aborda ruído de sensores, robustez a artefatos e variabilidade inter-sujeito; não aborda riscos de governança ou segurança de IA. |
| P69 | Albuquerque et al. (2020) | RQ5 | Parcialmente Respondida | P | Seção 5.5 e Seção 6 (pp. 12–13) | Aponta lacunas em modelos generalizáveis de carga mental e fusão sensorial robusta sob perturbações físicas. |
| **P69** | **SCORE_RQ TOTAL** | — | — | — | — | **1.5 / 5.0** |

### Tabela C — Avaliação de Qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P69 | Estudo Experimental / Base Multimodal | 1.0 | 1.0 | 1.0 | 1.0 | 4.0 | Alta |

---

## 6. Parecer Final do Revisor

- **Síntese:** O artigo possui padrão metodológico de alta qualidade ($SCORE\_QA = 4.0$), documentando a criação e validação do banco de dados multimodal WAUC com 48 participantes em tarefas de atenção dividida (*MATB-II*) sob esforço físico concorrente. Contudo, seu foco pertence à neuroengenharia e à ergonomia cognitiva humana, não investigando soluções agênticas de software, automação de processos de TI ou mitigação direta de incidentes de software ($SCORE\_RQ = 1.5$).
- **Recomendação:** **INCLUIR COM RESSALVAS** exclusivamente como referência empírica de suporte ao *cluster* de **carga cognitiva do operador humano** (fundamentando como a sobrecarga mental e a fadiga afetam a performance em sistemas críticos), amparado pela emenda de protocolo de 2026-09-09 para admissão excepcional do estrato Qualis A3. Caso o critério de inclusão do Ciclo 2 seja estritamente restrito a ferramentas de software para DevOps/SRE/IR, o artigo deve ser **EXCLUÍDO** por desvio de escopo de domínio.
- **Pendências de verificação externa:**
  1. Coletar o número atualizado de citações nas bases Scopus, Web of Science ou Google Scholar.
  2. Confirmar o quartil SJR (Q2) do periódico *Frontiers in Neuroscience* no SCImago.
  3. Confirmar a classificação Qualis A3 na Plataforma Sucupira/CAPES para a área de Ciência da Computação.