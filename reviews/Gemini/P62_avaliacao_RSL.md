# PROTOCOLO DE AVALIAÇÃO DE ESTUDO CANDIDATO (CICLO 2) — RSL AGENTIC AI COPILOT

---

## 1. INSUMOS DO ESTUDO

- **ID**: P62
- **Título**: *A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance*
- **Autores**: Frédéric Dehais, Alex Lafont, Raphaëlle Roy, Stephen Fairclough
- **Ano**: 2020 (Publicado em 07 de abril de 2020)
- **Periódico**: *Frontiers in Neuroscience* (Seção *Neural Technology*), Vol. 14, Artigo 268
- **DOI**: `10.3389/fnins.2020.00268`
- **Qualis Informado**: A3 (percentil Scopus 74.0%, regra CAPES 2025-2028)
- **SJR Quartile Informado**: Q2
- **Ressalvas de Triagem**: Ressalva de estrato (Qualis A3, emenda de protocolo 2026-09-09); cluster carga cognitiva; fora do domínio TI estrito.

---

## 2. ETAPA 0 — EXTRAÇÃO BIBLIOMÉTRICA

| Campo | Dado Extraído do Documento / Insumo | Observação / Ação |
| :--- | :--- | :--- |
| **ID** | P62 | Sequencial Ciclo 2 |
| **Título** | A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance | Verificado no PDF (p. 1) |
| **Periódico/Evento** | *Frontiers in Neuroscience* | Verificado no PDF (p. 1) |
| **Ano** | 2020 | Verificado no PDF (p. 1) |
| **Citações** | `[VERIFICAR]` | Fonte: Google Scholar / Scopus / Web of Science |
| **SJR (Quartil)** | Q2 `[VERIFICAR]` | Fonte: SCImago Journal Rank |
| **Qualis (Estrato)** | A3 `[VERIFICAR]` | Fonte: Plataforma Sucupira / CAPES (Área Computação) |
| **Tipo de Estudo** | Artigo de Revisão Teórica / Conceitual (*Review*) | Verificado no PDF (p. 1) |
| **DOI** | `10.3389/fnins.2020.00268` | Verificado no PDF (p. 1) |

---

## 3. ETAPA 1 — TRIAGEM DE ELEGIBILIDADE (PRISMA / CRITÉRIOS RSL)

- **Critério 1: Ano $\ge$ 2020?**
  - **Sim** (2020). Atende ao critério temporal.
- **Critério 2: Publicação $\ne$ NULL (Veículo Identificável)?**
  - **Sim** (*Frontiers in Neuroscience*, periódico indexado internacional com revisão por pares).
- **Critério 3: Citações $\ge$ 1?**
  - `[VERIFICAR]` (Requer checagem em base bibliográfica externa).
- **Critério 4: SJR Q1–Q2?**
  - **Sim** (Informado como Q2; pendente de confirmação externa de rotina `[VERIFICAR]`).
- **Critério 5: Qualis A1–A2?**
  - **RESSALVA DE ESTRATO**: O insumo classifica o artigo como A3. Sob a regra estrita inicial seria limítrofe/inelegível, porém é admitido para análise detalhada com base na **emenda de protocolo de 2026-09-09** (admissão de estudos A3 para sustentação teórica do cluster transversal de carga cognitiva).
- **Veredito da Triagem**: **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações, confirmação SJR e validação da ressalva de estrato). Procede-se à extração completa.

---

## 4. ETAPA 2 — EXTRAÇÃO E CLASSIFICAÇÃO DAS RQs

### RQ1 — Context Definitions
*Quais capacidades e níveis de autonomia (planejamento, memória, uso de ferramentas e supervisão humana) caracterizam Agentic AI e como afetam a tomada de decisão em ambientes complexos?*
- **Subdimensões**: a) Definição de autonomia; b) Características essenciais; c) Modelo de tomada de decisão.
- **Análise do Texto**: O estudo não discute *Agentic AI* no sentido estrito de engenharia de software ou modelos baseados em LLM. Contudo, examina profundamente a autonomia sob a ótica de sistemas adaptativos de tomada de decisão em ambientes críticos (aviação, medicina e tráfego aéreo). Descreve como o estresse extremo e a sobrecarga cognitiva alteram o modelo de decisão humano, desativando funções executivas pré-frontais e ativando esquemas automatizados subcorticais (gânglios da base), gerando perseveração irracional (pp. 3–4). Propõe a divisão dinâmica de autoridade e supervisão compartilhada (*authority sharing*, pp. 9–10).
- **Classificação**: **Parcialmente Respondida (P = 0.5)**

### RQ2 — Engineering Architecture
*Quais arquiteturas e mecanismos (orquestração, memória, ferramentas, guardrails, observabilidade) sustentam Agentic AI em produção?*
- **Subdimensões**: a) Tipo de arquitetura; b) Ferramentas/frameworks; c) Capacidades avançadas.
- **Análise do Texto**: Não descreve pipelines de microsserviços, chamadas de ferramentas (*tool-use*) ou memória de longo prazo para agentes de IA de software. Em contrapartida, formaliza a arquitetura conceitual e técnica de sistemas neuroadaptativos em malha fechada (*biocybernetic loop* / BCI passivo): (1) aquisição de sinal neurofisiológico; (2) pré-processamento de ruído; (3) extração de características em tempo/frequência; (4) classificação do estado mental; e (5) unidade de decisão estocástica para adaptação da interface ou do nível de automação (p. 7).
- **Classificação**: **Parcialmente Respondida (P = 0.5)**

### RQ3 — Evidence Benefits
*Quais evidências (quanti/quali) reportam benefícios e quais métricas são usadas (tempo de resposta, qualidade de decisão, carga operacional), especialmente em IR?*
- **Subdimensões**: a) Benefícios qualitativos; b) Métricas e benefícios quantitativos; c) Nível de evidência.
- **Análise do Texto**: Cobertura extensa das métricas que quantificam a carga mental e o desempenho em cenários de emergência/incidentes críticos. Mapeia detalhadamente o desengajamento cognitivo (*effort withdrawal*), surdez e cegueira desatencionais, correlacionando-os com métricas hemodinâmicas no córtex pré-frontal dorsolateral (fNIRS / DLPFC), sincronia de fase e bandas espectrais EEG (teta e alfa frontal/parietal), índices autonômicos (HRV/ECG) e oculometria (fixações, sacadas, dilatação pupilar) (Tabela 1, Figuras 1, 2 e 3, pp. 5–8). Nível de evidência fundamentado em extensa literatura experimental prévia de fatores humanos e neurociência aplicada.
- **Classificação**: **Respondida Plenamente (T = 1.0)**

### RQ4 — Challenges & Ethics
*Quais riscos e desafios (segurança, robustez, governança, accountability) limitam o uso responsável em sistemas críticos?*
- **Subdimensões**: a) Desafios técnicos; b) Desafios éticos/governança; c) Mecanismos de governança.
- **Análise do Texto**: Analisa os riscos associados à intervenção inadequada da automação adaptativa: a tomada de controle não transparente ou no momento errado induz quebra de confiança do operador (*reduced trust in technology*), perda de consciência situacional (*out-of-the-loop phenomenon*) e degradação adicional de desempenho (pp. 9–10). Defende um modelo de governança operacional escalonado (*gradient of solutions*): biofeedback $\rightarrow$ alertas sugestivos $\rightarrow$ adaptação visual da interface $\rightarrow$ intervenção ativa/assunção de controle apenas em último caso (p. 10). Não abrange governança algorítmica ou regulação formal de IA.
- **Classificação**: **Parcialmente Respondida (P = 0.5)**

### RQ5 — Research Gaps
*Quais lacunas e direções futuras (avaliação/benchmarking, threat models, governança, observabilidade, alinhamento) são apontadas?*
- **Subdimensões**: Identificação de lacunas e direções futuras de pesquisa.
- **Análise do Texto**: O artigo pontua lacunas estruturais claras: (1) escassez de estudos sobre equipes complexas, com forte necessidade de migrar da díade humano-máquina simples para cooperação humano-humano e humano-múltiplas máquinas (*teaming* via hiperscanning e BCIs colaborativas); (2) ausência de contramedidas adaptativas para falhas de atenção auditiva (surdez desatencional a alarmes críticos); e (3) carência de estudos sobre a eficácia de longo prazo e segurança de técnicas de neuromodulação ativa (tDCS, estimulação luminosa) (pp. 10–11).
- **Classificação**: **Respondida Plenamente (T = 1.0)**

---

## 5. ETAPA 3 — AVALIAÇÃO DE QUALIDADE (DARE / QA1–QA4)

- **QA1 (Objetivos Claros)**: **P (0.5)**
  - *Justificativa*: A contextualização do problema (falhas dos modelos clássicos de recursos cognitivos limitados e breakdown em situações extremas) e a proposta do modelo bi-dimensional (engajamento $\times$ *arousal*) são muito claras. Todavia, o foco não é um problema ou solução de software agêntico corporativo, mas um framework de neuroergonomia e automação adaptativa.
- **QA2 (Metodologia Replicável)**: **P (0.5)**
  - *Justificativa*: Trata-se de uma revisão teórica/narrativa com síntese conceitual. Não apresenta protocolo de busca estruturado com strings explícitas de busca, critérios de inclusão/exclusão sistematizados ou parâmetros detalhados para replicação direta como em uma RSL ou experimento empírico.
- **QA3 (Base de Evidências Sólidas)**: **P (0.5)**
  - *Justificativa*: Apresenta compilação e triangulação densa de evidências experimentais publicadas (Tabela 1, Figuras 1 e 3), mas o artigo em si não conduz uma validação empírica primária nem estudo de caso industrial inédito dentro do corpo do texto.
- **QA4 (Conclusões Coerentes)**: **Y (1.0)**
  - *Justificativa*: As conclusões são estritamente sustentadas pela literatura neurocientífica revisada. Os autores discutem com equilíbrio os limites do modelo, riscos de aceitação pelo usuário, necessidade de transparência nas contramedidas e limitações ecológicas dos métodos avaliados.
- **SCORE_QA TOTAL**: **2.5 / 4.0**
- **Banda de Qualidade**: **Média** (1.5 – 2.5)

---

## 6. TABELAS DE SÍNTESE PARA A RSL

### Tabela A — Extração Bibliométrica (Alimenta a Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **P62** | *Frontiers in Neuroscience* | 2020 | `[VERIFICAR]` | Q2 `[VERIFICAR]` | A3 `[VERIFICAR]` | Review | `10.3389/fnins.2020.00268` |

### Tabela B — Classificação das RQs (Alimenta a Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (Seção/Pág.) | Parecer do Revisor |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| P62 | Dehais et al. (2020) | RQ1 | Parcialmente Respondida | P | Seções *Brain and Inhibitory Mechanisms*, *Non-linear Effects*, *Task & Auto.* (pp. 3–4, 9) | Analisa tomada de decisão sob sobrecarga cognitiva e persistência de erros (perseveração), propondo divisão dinâmica de autoridade. |
| P62 | Dehais et al. (2020) | RQ2 | Parcialmente Respondida | P | Seção *Solutions to Mitigate...* (p. 7) | Detalha a arquitetura em malha fechada de sistemas neuroadaptativos (aquisição, processamento, classificação e atuador de adaptação). |
| P62 | Dehais et al. (2020) | RQ3 | Respondida Plenamente | T | Seções *Understanding Performance...*, Tabela 1, Figuras 1–3 (pp. 5–8) | Fornece catálogo robusto de métricas neurofisiológicas e psicofisiológicas para quantificação de estresse, fadiga e abandono de esforço em incidentes críticos. |
| P62 | Dehais et al. (2020) | RQ4 | Parcialmente Respondida | P | Seção *Synthesis of Neuro-Adaptive Solutions* (pp. 9–10) | Aborda o impacto da perda de transparência e quebra de confiança pelo operador quando sistemas automatizados interferem sem feedback. |
| P62 | Dehais et al. (2020) | RQ5 | Respondida Plenamente | T | Seção *Conclusion*, Legenda da Fig. 4 (pp. 10–11) | Mapeia lacunas em sistemas de múltiplos agentes/equipes (*teaming* humano-máquina), mitigação de surdez desatencional e efeitos em longo prazo. |
| **SCORE_RQ** | | | | | | **3.5 / 5.0** |

### Tabela C — Avaliação de Qualidade Metodológica DARE (Alimenta a Tabela 7 da RSL)

| ID | Tipo de Estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda de Qualidade |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P62** | Review | P (0.5) | P (0.5) | P (0.5) | Y (1.0) | **2.5** | **Média** |

---

## 7. PARECER FINAL DO REVISOR

- **Síntese da Avaliação**:
  O estudo P62 propõe uma mudança de paradigma em relação à teoria clássica de recursos atencionais finitos, estruturando a performance humana e a carga mental em um espaço bidimensional composto por engajamento na tarefa e *arousal* fisiológico. Apresenta uma taxonomia rigorosa de estados degradados (desengajamento por esforço, divagação mental, perseveração e bloqueios perceptuais de alarme) e catálogo de métricas psicofisiológicas e neurofuncionais correspondentes. Embora provenha da área de Neuroergonomia / Fatores Humanos e não trate de arquiteturas de software agêntico baseadas em LLM, serve como pilar teórico fundamental para a modelagem da carga cognitiva e desenho de interação adaptativa humano-agente em resposta a incidentes críticos.

- **Recomendação**:
  **INCLUIR COM RESSALVAS**.
  *Justificativa*: A inclusão é justificada pela relevância teórica direta ao cluster de carga cognitiva e interação homem-máquina em cenários de alta pressão (RQ3 e RQ5 respondidas plenamente, SCORE_RQ = 3.5). A ressalva é mandatória devido ao estrato Qualis A3 (admitido sob emenda de protocolo 2026-09-09) e ao fato de o artigo situar-se fora do escopo estrito de TI/Computação Aplicada.

- **Pendências de Verificação Externa**:
  1. *Citações*: Levantar contagem oficial no Google Scholar / Scopus.
  2. *SJR*: Checar quartil oficial no SCImago Journal Rank no ano base.
  3. *Qualis CAPES*: Confirmar classificação definitiva no quadriênio vigente na Plataforma Sucupira para a área de Ciência da Computação.