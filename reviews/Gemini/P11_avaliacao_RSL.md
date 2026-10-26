# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P11
- **Arquivo PDF avaliado:** `P11-A1-Co-Evolving_Multi-Agent_Transfer_Reinforcement_Learning_via_Scenario_Independent_Representation.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo investiga um problema estrutural de sistemas multiagentes autônomos (*Multi-Agent Systems — MAS*): como escalar a coordenação cooperativa e competitiva entre múltiplos agentes heterogêneos sem sofrer explosão combinatória do espaço de estados/ações nem estagnação de políticas, propondo os frameworks **MACTRL (*Multi-Agent Curriculum Transfer Reinforcement Learning*)** e **Co-MACTRL (*Co-Evolving Multi-Agent Curriculum Transfer Reinforcement Learning*)** baseados em **representações espaciais independentes de cenário (*Agent Influence Maps — AIM* e *Multi-Agent Influence Maps — MAIM*)** sob o paradigma de **Treinamento Centralizado com Execução Semicentralizada (*CTSCE*)**.
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado no periódico *IEEE Access*, Volume 12, pp. 99439–99451, 2024 (Recebido em 19 de maio de 2024; Aceito em 11 de julho de 2024; Data de publicação em 17 de julho de 2024; Data da versão atual em 26 de julho de 2024).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo experimental completo publicado em periódico científico com revisão por pares (*IEEE Access*, IEEE), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 13 páginas em inglês com 42 referências, formulação matemática completa, pseudocódigos (Algoritmos 1 e 2) e avaliação experimental rigorosa.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Superação do Acoplamento Topológico em Sistemas Multiagentes (Seções I–II, pp. 1–4):** O artigo analisa a limitação fundamental dos algoritmos clássicos de *Multi-Agent Reinforcement Learning (MARL)*: como as dimensões dos vetores de estado e de ação dependem diretamente do número e do tipo de agentes no ambiente, redes neurais treinadas em um cenário não podem transferir conhecimento diretamente para cenários com cardinalidade ou heterogeneidade distintas sem redesenho arquitetural ou *padding* artificial dependente do cenário máximo.
  - **Paradigma *Centralized Training with Semi-Centralized Execution (CTSCE)* e Co-Evolução Competitiva (Seção I, p. 2; Seção III.B, pp. 4–5):** Adapta o paradigma *CTDE* para **CTSCE**, no qual o crítico utiliza o estado global completo durante o treinamento, enquanto os atores executam políticas descentralizadas apoiadas por uma abstração espacial compacta do estado global (*MAIM*), e substitui o treinamento contra oponentes estáticos (*built-in scripted AI*) por um processo de **co-evolução competitiva cíclica** aliado a **aprendizado por transferência curricular (*Curriculum Transfer Learning — CTL*)**.
  - **Limitação:** O estudo fundamenta-se exclusivamente em *Multi-Agent Reinforcement Learning (MARL)* e jogos de Markov (Eq. 1, p. 4), não abordando agentes baseados em *Large Language Models (LLMs)* ou *Generative AI*.
- **Justificativa:** Contribui com fundamentos sólidos sobre generalização inter-cenários, transferência curricular e co-evolução em sistemas multiagentes (*MARL*), mas sem abordar a transição para agentes baseados em LLMs (`P = 0.5`).

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Representação de Estado Independente de Cenário via *Influence Maps (AIM / MAIM)* (Seção III.B.1, Fig. 1b, pp. 4–6):**
    - Cada agente $i$ é modelado espacialmente por um **Agent Influence Map (AIM)** parametrizado pelo valor máximo de influência proporcional à saúde relativa da unidade ($I_0$), taxa de decaimento espacial ($\lambda_I$) e alcance de influência ($d_I$), atribuindo pesos positivos a aliados e negativos a inimigos;
    - A soma algébrica dos *AIMs* de todos os agentes produz um **Multi-Agent Influence Map (MAIM)** global de dimensão fixa $64 \times 64$ (`4.096` parâmetros), combinado a um mapa de influência local de alcance visual de dimensão $37 \times 37$ (`1.369` parâmetros), resultando em um vetor de entrada de tamanho invariante de **`5.465` parâmetros** independentemente do número ou tipo de agentes no cenário.
  - **Representação Compacta de Ações e Arquitetura *A3C* com Compartilhamento de Parâmetros (Seção III.B.2, Fig. 1c–e, Tabela 1, pp. 5–6):**
    - Reduz o espaço de ações variável do *SMAC* (onde atacar exige selecionar entre $M$ inimigos) para um vetor de saída fixo de **`7` ações discretas** (`no-op`, `stop`, `move north`, `move south`, `move east`, `move west` e `attack closest enemy` dentro do alcance de tiro, Fig. 1e, p. 6);
    - Emprega **Asynchronous Advantage Actor-Critic (A3C)** com compartilhamento de parâmetros (*parameter sharing*) entre agentes aliados: rede **Actor** MLP (`5465 -> 64 -> 64 -> 7`, Fig. 1c) e rede **Critic** centralizada (`365 -> 64 -> 64 -> 1`, Fig. 1d).
  - **Algoritmos *MACTRL* e *Co-MACTRL* e Ambiente *Multi-Player SMAC (MP-SMAC)* (Seção III.C–D, Algoritmos 1 e 2, Figs. 2 e 3, pp. 6–8):**
    - **MACTRL (Algoritmo 1, p. 7):** Transfere sequencialmente os pesos da política compartilhada ao longo de um currículo progressivo de complexidade ($3m \to 8m \to 2s3z \to 3s5z$);
    - **MP-SMAC (Fig. 3, p. 8):** Estende o *StarCraft Multi-Agent Challenge (SMAC)* para suportar partidas simétricas entre duas equipes controladas por redes de aprendizado independentes (gerando *MAIMs* duplos com inversão de perspectiva na linha $x = 32$);
    - **Co-MACTRL (Algoritmo 2, Fig. 2, pp. 6–8):** Orquestra uma arena co-evolutiva com **3 *learners* concorrentes** ao longo de múltiplos ciclos curriculares, intercalando fases de transferência contra a IA nativa nos mapas simples ($3m, 8m, 2s3z$) e confrontos diretos multiagente (*self-play* competitivo entre *learners*) no cenário heterogêneo mais complexo ($3s5z\_mp$).
- **Justificativa:** Especifica com total transparência matemática e algorítmica uma arquitetura multiagente escalável, invariante à topologia da equipe e capaz de transferir políticas entre ambientes heterogêneos (`T = 1.0`).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Protocolo Experimental Rigoroso (Seção IV, pp. 8–11):** Todos os experimentos foram executados em **7 sementes aleatórias independentes (*7 random seeds*)**, com até **`80 milhões de timesteps`** de treinamento no *Co-MACTRL*, avaliando a taxa média de vitórias (*average win rate*) a cada `25 episódios` por meio de `32 episódios de teste` em todos os quatro cenários ($3m$, $8m$, $2s3z$ e $3s5z$).
  - **Ablação da Resolução do Mapa de Influência Local (Seção IV, p. 8):** Comparou cinco resoluções de janela local ($19 \times 19$, $25 \times 25$, $37 \times 37$, $45 \times 45$ e $55 \times 55$), comprovando que a resolução intermediária de **$37 \times 37$** maximiza a taxa de vitória ao equilibrar campo de visão e granularidade espacial.
  - **Desempenho do *MACTRL* vs. *Regular MARL* em `8M steps` (Seção IV.A, Tabela 2, Fig. 4, p. 9):**
    - O **MACTRL** atingiu uma **taxa média global de vitórias de `80%`** nos quatro cenários, contra **`40%`** do *Regular MARL* treinado diretamente em $3s5z$ (**ganho absoluto de `+40 pontos percentuais`**, dobrando a eficácia global);
    - Por cenário (Tabela 2, p. 9): em **$3m$**, `87%` (*MACTRL*) vs. `38%` (*Regular MARL*, com média de apenas `15%` na fase inicial); em **$8m$**, `68%` vs. `41%` (`20%` na fase inicial); em **$2s3z$**, `84%` (citado como `85%` no texto) vs. `50%` (`30%` na fase inicial); e em **$3s5z$**, `85%` vs. `72%`.
  - **Desempenho do *Co-MACTRL* vs. *Co-MARL* ao longo de 4 Ciclos / `72M steps` (Seção IV.B, Tabela 3, Fig. 5, pp. 10–11):**
    - No **Co-MACTRL**, a taxa média global de vitórias do *Learner 1* evoluiu de **`75%` no Ciclo 1 para `84%` no Ciclo 4** (progredindo de `80% -> 90%` em $3m$, `60% -> 73%` em $8m$, `89% -> 90%` em $2s3z$ e `83% -> 90%` em $3s5z$), com o *Learner 2* alcançando **`79%`** e o *Learner 3* alcançando **`83%`** no Ciclo 4;
    - O *Co-MACTRL* superou os valores de pico do próprio *MACTRL* em quase **`7%`** e superou o baseline **Co-MARL** (co-evolução sem currículo, que obteve médias de apenas `39%` para o *Learner 1*, `38%` para o *Learner 2* e `54%` para o *Learner 3* no Ciclo 4) em **quase `50 pontos percentuais` em mapas não vistos**.
  - **Emergência de Coordenação Tática Multiagente (Seção IV.C, Fig. 6, p. 11):** A inspeção visual dos episódios (Fig. 6a–d) demonstra a emergência autônoma da tática de **"focus fire"** (concentração coordenada de fogo no mesmo alvo inimigo para reduzir rapidamente o poder de dano adversário) e posicionamento tático diferenciado por tipo de unidade (separando *Stalkers* de longo alcance e *Zealots* corpo a corpo para eliminar primeiro os *Zealots* inimigos).
- **Justificativa:** Fornece validação empírica quantitativa exemplar (Tabelas 2 e 3, Figs. 4–6, 7 sementes, 80M *steps*) demonstrando ganhos expressivos de generalização, transferência e robustez co-evolutiva (`T = 1.0`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Degradação de Desempenho / Esquecimento Catastrófico em Transferência Sequencial (Seção IV.A, Fig. 4, pp. 9–10):** O artigo identifica e demonstra empiricamente um risco crítico em sistemas multiagentes com aprendizado contínuo: no *MACTRL*, após atingir o estágio final do currículo ($3s5z$, a partir de `7M steps`), a política sofre **degradação gradual de desempenho nas tarefas aprendidas anteriormente** ($3m$, $8m$ e $2s3z$) devido à sobreposição de pesos (*catastrophic forgetting*), problema mitigado pelo retreinamento cíclico introduzido no *Co-MACTRL* (Seção IV.B, p. 10).
  - **Fragilidade e *Overfitting* contra Adversários Estáticos (Seções I e IV.B, pp. 2, 10–11):** Demonstra que agentes treinados apenas contra heurísticas fixas exploram falhas previsíveis da IA nativa e falham quando expostos a políticas adversariais adaptativas, justificando a necessidade de treinamento co-evolutivo competitivo.
  - **Custo Computacional da Simulação Multi-Player (Seção III.D, p. 8):** Aponta o elevado custo computacional de executar múltiplos aprendizes simultâneos no *MP-SMAC*, o que restringiu as partidas diretas entre *learners* ao cenário mais complexo ($3s5z\_mp$).
  - **Limitação:** Não aborda riscos de segurança cibernética, ataques adversariais de *prompt* ou governança ética/regulatória.
- **Justificativa:** Analisa e resolve empiricamente riscos operacionais importantes de sistemas multiagentes adaptativos (*catastrophic forgetting* entre tarefas e *overfitting* a oponentes estáticos), embora sem foco em cibersegurança ou governança (`P = 0.5`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Direções Futuras para *MARL* Escalável (Seção V, p. 12):** Os autores apontam três frentes prioritárias de investigação futura:
    1. Avaliar a escalabilidade do *Co-MACTRL* em um espectro mais amplo de cenários heterogêneos de larga escala e domínios de aplicação além de *StarCraft II*;
    2. Investigar estratégias avançadas de sequenciamento curricular automático e mecanismos mais eficientes de transferência de conhecimento durante a co-evolução;
    3. Integrar **Redes Neurais Recorrentes (*RNNs* / *LSTMs* / *GRUs*)** à arquitetura profunda de RL para capturar dependências temporais de longo prazo sob observabilidade parcial.
- **Justificativa:** Delimita extensões técnicas claras e coerentes para arquiteturas *MARL* co-evolutivas na Seção V (p. 12), ainda que circunscritas ao escopo de aprendizado por reforço (`P = 0.5`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 0.5 + 1.0 + 1.0 + 0.5 + 0.5 = 3.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P11 |
| **Autores** | Ayesha Siddiqua; Siming Liu; Ayesha Siddika Nipu; Anthony Harris; Yan Liu |
| **Ano** | 2024 |
| **Título** | *Co-Evolving Multi-Agent Transfer Reinforcement Learning via Scenario Independent Representation* |
| **Periódico / Fonte** | *IEEE Access*, Vol. 12, pp. 99439–99451 |
| **DOI** | `10.1109/ACCESS.2024.3430037` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Estudo Primário Experimental / Proposta Arquitetural e Algorítmica em *MARL* (42 referências) |
| **Domínio Principal** | Aprendizado por Reforço Multiagente (*MARL*) com Transferência Curricular (*CTL*), Co-Evolução Competitiva e Representação Espacial Independente de Cenário |
| **Tecnologias / Frameworks Analisados** | **MACTRL**, **Co-MACTRL**, *Agent Influence Map (AIM)*, *Multi-Agent Influence Map (MAIM)*, *Asynchronous Advantage Actor-Critic (A3C)*, *Centralized Training with Semi-Centralized Execution (CTSCE)*, *StarCraft Multi-Agent Challenge (SMAC)* e extensão **Multi-Player SMAC (MP-SMAC)** |
| **Escopo de Aplicação** | Coordenação tática cooperativa e competitiva de sistemas multiagentes heterogêneos em ambientes dinâmicos de tempo real (micromanagement em *StarCraft II*: cenários $3m, 8m, 2s3z, 3s5z$) |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `P` | `0.5` | Formulação do problema de acoplamento dimensional em *MARL* e introdução do paradigma **CTSCE (*Centralized Training with Semi-Centralized Execution*)** combinado com transferência curricular (*CTL*) e co-evolução competitiva (Seções I–II, pp. 1–4). Não aborda agentes LLM. |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Representação espacial invariante de estado via *AIM/MAIM* (`5.465` entradas fixas: global $64 \times 64$ + local $37 \times 37$) e de ação (`7` ações discretas) acoplada a redes *A3C* compartilhadas (Fig. 1, Tabela 1, pp. 5–6); algoritmos **MACTRL** (Alg. 1) e **Co-MACTRL** (Alg. 2, Fig. 2) e ambiente **MP-SMAC** (Fig. 3, pp. 6–8). |
| **RQ3** (Evidências Empíricas e Métricas) | `T` | `1.0` | Avaliação em 7 sementes e até 80M *steps* (Tabelas 2 e 3, Figs. 4–6, pp. 8–11): **MACTRL atingiu `80%` de taxa média de vitória vs. `40%` do *Regular MARL***; **Co-MACTRL atingiu `84%` no Ciclo 4**, superando *MACTRL* em ~`7%` e *Co-MARL* (`39%`) em quase `50%` em mapas não vistos, com emergência de *focus fire*. |
| **RQ4** (Riscos, Segurança e Governança) | `P` | `0.5` | Demonstração empírica e mitigação do **esquecimento catastrófico (*catastrophic forgetting*)** na transferência sequencial (Fig. 4, pp. 9–10) e do *overfitting* a oponentes estáticos via ciclos co-evolutivos, além da análise do custo computacional do *MP-SMAC* (p. 8). |
| **RQ5** (Lacunas e Direções Futuras) | `P` | `0.5` | Direções futuras (Seção V, p. 12): expansão para cenários heterogêneos mais amplos, otimização de currículos co-evolutivos e integração de redes recorrentes (*RNNs*) para memória temporal. |
| **Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Boa Aderência (70,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | Como estudo experimental primário, delimita com precisão o problema de pesquisa (transferência de políticas entre cenários multiagentes com dimensões de estado/ação variáveis), o conjunto de cenários avaliados ($3m, 8m, 2s3z, 3s5z$) e as hipóteses testadas (Seções I e III, pp. 1–6). |
| **QA2 — Busca e transparência metodológica** | `Y` | `1.0` | Elevada transparência metodológica e reprodutibilidade: apresenta formulação matemática completa do jogo de Markov e dos mapas de influência (Eq. 1, Seção III.B), pseudocódigos detalhados (Algoritmos 1 e 2), hiperparâmetros de rede (`5465 -> 64 -> 64 -> 7` e `365 -> 64 -> 64 -> 1`), ablação de resolução ($19 \times 19$ a $55 \times 55$) e protocolo de avaliação com 7 sementes aleatórias e 80M *steps* (pp. 4–8). |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `Y` | `1.0` | Compara sistematicamente os métodos propostos contra múltiplos *baselines* controlados (*MACTRL vs. Regular MARL* na Tabela 2 e Fig. 4; *Co-MACTRL vs. Co-MARL* ao longo de 4 ciclos na Tabela 3 e Fig. 5), reportando médias e curvas de aprendizado com intervalos de confiança e análise comportamental qualitativa (Fig. 6). |
| **QA4 — Coerência entre evidências e conclusões** | `Y` | `1.0` | Todas as conclusões da Seção V (p. 12) são diretamente sustentadas pelas evidências quantitativas das Tabelas 2 e 3 e pelas curvas das Figuras 4 e 5, sem extrapolações indevidas. |
| **Total (`SCORE_QA`)** | **Banda: Alta** | **4.0 / 4.0** | **Qualidade Metodológica Máxima (100,0%)** |

---

## Parecer Final do Revisor

O artigo **P11** (Siddiqua et al., 2024), publicado no *IEEE Access* e integrante do **Corpus Fundacional** do Trabalho I, atinge a pontuação máxima de qualidade metodológica (`SCORE_QA = 4.0 / 4.0`, banda **Alta**) e boa aderência às questões da RSL (`SCORE_RQ = 3.5 / 5.0`). Assim como **P07** (Chen et al., 2020), **P11** representa a vertente de **Aprendizado por Reforço Multiagente (*MARL*)** do corpus fundacional, fornecendo evidências quantitativas rigorosas para a **RQ2** e a **RQ3**: sua representação espacial independente de cenário via *Multi-Agent Influence Maps (MAIM)* permite transferir políticas diretamente entre equipes de tamanhos e composições distintas, elevando a taxa média de vitórias de **`40%` (*Regular MARL*) para `80%` (*MACTRL*)** e alcançando **`84%` com co-evolução cíclica (*Co-MACTRL*)**, ao mesmo tempo em que documenta e resolve empiricamente o fenômeno de **esquecimento catastrófico (*catastrophic forgetting*)** em sistemas multiagentes contínuos (**RQ4**).
