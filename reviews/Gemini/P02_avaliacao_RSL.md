# Avaliação Individual de Estudo Primário — RSL

## Identificação do Estudo
- **ID:** P02
- **Arquivo PDF avaliado:** `P02-A1-The role of agentic AI in shaping a smart future A systematic review.pdf`
- **Status no Corpus:** Estudo **FUNDACIONAL** do Trabalho I (já incluído na RSL — avaliação retroativa de padronização para as Tabelas 3, 5 e 7; não se rediscute a inclusão).
- **Qualis (pré-verificado no protocolo):** A1
- **Quartil SJR (pré-verificado no protocolo):** Q1

---

## Etapa 0 — Elegibilidade (Check Retroativo de Padronização)

- **E1 (Aderência ao escopo semântico):** **Atendido.** O artigo investiga de forma abrangente o paradigma de *Agentic AI* (IA Agêntica), definindo seus atributos estruturais (autonomia, comportamento orientado a metas, interação ambiental, aprendizado contínuo, otimização de fluxos de trabalho e sistemas multiagentes), a transição organizacional do modelo **Copilot** (assistente *human-in-the-loop*) para **Autopilot** (execução autônoma ponta a ponta), arquiteturas hierárquicas de coordenação (*Master agent* $\to$ *Orchestrator agent* $\to$ *Micro-agents*) e frameworks de implementação (*LangGraph*, *CrewAI*, *AutoGen*, *AutoGPT*).
- **E2 (Recorte temporal 2023–2026):** **Atendido.** Publicado em 2025 no periódico *Array* (Elsevier), Volume 26, Artigo 100399 (Recebido em 29 de dezembro de 2024; Revisado em 4 de abril de 2025; Aceito em 15 de abril de 2025; Disponível online em 8 de maio de 2025).
- **E3 (Padrão de qualidade e revisão por pares):** **Atendido.** Artigo de revisão publicado em periódico científico com revisão por pares (*Array*, Elsevier), classificado como **Qualis A1** e **SJR Q1** nos metadados pré-verificados do protocolo.
- **E4 (Critérios de exclusão):** **Nenhum aplicável.** Texto integral de 15 páginas em inglês com análise conceitual, arquitetural e de ferramentas de IA agêntica.
- **Status:** **INCLUÍDO (Corpus Fundacional — Trabalho I)**.

---

## Etapa 1 — Avaliação Detalhada das Questões de Pesquisa (RQ1–RQ5)

### RQ1 — Fundamentos Conceituais e Paradigmas de Transição (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Definição e seis pilares de *Agentic AI* (Seção 1.2, Fig. 1, p. 2; Tabela 1, p. 3):** O estudo conceitua a IA Agêntica em torno de seis dimensões centrais: (1) *Autonomy* (execução independente sem supervisão humana constante); (2) *Goal-oriented behavior* (planejamento e decomposição de objetivos complexos); (3) *Environmental interaction* (percepção e atuação dinâmica sobre o ambiente); (4) *Learning capability* (adaptação via *reinforcement learning* e *self-supervised learning*); (5) *Workflow optimization* (automação e coordenação de processos complexos); e (6) *Multi-agent systems* (colaboração distribuída entre múltiplos agentes).
  - **Evolução histórica em cinco estágios (Seção 2, Fig. 2, p. 3; Tabela 2, p. 5):** Traça a progressão desde sistemas baseados em regras (pré-anos 2000), aprendizado de máquina (anos 2000), *deep learning* e RL (anos 2010), IA generativa e autônoma (início dos anos 2020) até IA agêntica multimodal e autonomia avançada (anos 2020+), distinguindo agentes de resposta rápida (*fast thinking*, ex.: *ChatGPT-4*) de agentes de raciocínio deliberativo lento (*slow thinking*, ex.: *ChatGPT-o1* / *ChatGPT-1* na grafia do texto, Seção 2.3, p. 4).
  - **Diferenciação taxonômica (Seção 3.2, Tabela 3, pp. 5–6):** Compara sistematicamente **Agentic AI**, **Generative AI** e **Autonomous AI** ao longo de 14 critérios (definição, objetivo primário, escopo funcional, autonomia, tomada de decisão, adaptabilidade, tratamento de tarefas, interação ambiental, orientação a objetivos, aprendizado, intervenção humana, gerenciamento de complexidade, exemplos e casos de uso).
  - **Transição *Copilot* $\to$ *Autopilot* (Seção 5, Fig. 4, pp. 6–8):** Formaliza a evolução operacional desde o **Copilot model** (IA como assistente colaborativo com *human-in-the-loop*, exemplificado pela plataforma *Sierra* que resolve chamados rotineiros e escala casos complexos para especialistas humanos, Seção 5.1, p. 6) até o **Autopilot model** (IA executando fluxos de trabalho completos de forma autônoma, Seção 5.2, pp. 6–8).
- **Justificativa:** O artigo oferece uma cobertura completa e estruturada da definição de IA agêntica, sua distinção frente à IA generativa tradicional e a transição operacional entre os modelos *Copilot* e *Autopilot*.

### RQ2 — Arquiteturas, Protocolos e Orquestração Multiagente (`T = 1.0`)
- **Evidências concretas no artigo:**
  - **Arquitetura hierárquica de três camadas (Seção 4, Fig. 3, p. 6; Tabela 4, p. 7):** Especifica uma topologia de orquestração composta por: (1) **Master agent** (interface primária com o usuário/sistema e definição de diretrizes estratégicas); (2) **Orchestrator agent** (decomposição de tarefas, roteamento dinâmico e sincronização de fluxos); e (3) **Micro-agents** especializados (*User Experience Agent*, *FAQ Agent*, *Issue Resolution Agent*, *Status Update Agent*, *Feedback Collection Agent* e *Nth Agent*), detalhando entradas, saídas e responsabilidades na Tabela 4 (p. 7).
  - **Paradigma *AI-as-a-Service (AIaaS)* e *Service-as-Software* (Seção 4, p. 5):** Descreve a transição de *Software-as-a-Service (SaaS)* para *Service-as-Software*, onde agentes autônomos entregam resultados operacionais completos (incluindo *AI-driven penetration testers* para identificação e mitigação contínua de vulnerabilidades cibernéticas e agentes de suporte técnico).
  - **Análise comparativa de frameworks e plataformas (Seção 7, Fig. 5, pp. 10–12; Seção 8.3, p. 13):** Avalia e contrasta ferramentas comerciais e de código aberto para construção de sistemas agênticos: **LangGraph** (gerenciamento de estado explícito, *streaming*, ciclos de monitoramento e recuperação de falhas), **CrewAI** (templates *no-code/low-code* para orquestração multiagente corporativa), **AutoGen** (coordenação multiagente aberta com suporte nativo a *human-in-the-loop*), **AutoGPT** (decomposição autônoma de metas com acesso à internet e execução de código), além de plataformas de infraestrutura como *IBM Watson*, *Amazon SageMaker*, *TensorFlow* e *Llama 3.1*. Na Seção 8.3 (p. 13), propõe uma arquitetura de implantação em dois estágios: prototipação (*PoC*) com *AutoGPT*/*AutoGen* seguida de produção escalável com *LangGraph*/*CrewAI* integrada a sistemas corporativos (ERP/CRM).
- **Justificativa:** Apresenta arquitetura hierárquica multiagente explícita e avaliação comparativa detalhada dos principais frameworks de orquestração agêntica (*LangGraph*, *CrewAI*, *AutoGen*, *AutoGPT*).

### RQ3 — Evidências Empíricas e Métricas Operacionais (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Síntese de indicadores secundários de indústria e literatura (Seções 3, 4.1, 6.1–6.2, pp. 4–6, 9):** O estudo compila estimativas quantitativas reportadas na literatura secundária e em relatórios de mercado:
    - Ganhos de produtividade de até `40%` em fluxos corporativos segundo relatórios da McKinsey (Seção 3, p. 4);
    - Economia de `360.000 horas` anuais de trabalho jurídico/analítico pelo sistema *COiN* do JPMorgan (Seção 3, p. 4);
    - Redução de `20–50%` no tempo de inatividade de equipamentos (*downtime*) via manutenção preditiva e redução de `60%` no tempo de resposta em atendimento ao cliente com aumento de `25%` na satisfação (Seção 3, p. 4);
    - Redução de custos operacionais em até `30%` e aumento de `40–50%` na eficiência de resposta com *AIaaS* (Seção 4, p. 5), com custos iniciais de implantação estimados entre `US$ 50.000 e US$ 500.000`, redução de custos de `20–35%` em dois anos e retorno sobre investimento (*ROI*) de `3x–5x` em cinco anos (Seção 4.1, p. 5);
    - Redução de `40%` em transações fraudulentas (Seção 4.2, p. 6) e redução de `25%` em perdas por fraude no setor financeiro (Seção 6.1, p. 9).
  - **Limitação empírica:** Trata-se de uma revisão narrativa que reporta estatísticas secundárias agregadas, sem conduzir experimentos próprios, *benchmarks* controlados de resposta a incidentes ou medições primárias de *MTTR*, latência ou precisão.
- **Justificativa:** Fornece métricas secundárias de eficiência, custo e *ROI* úteis para contextualização econômica, mas carece de avaliação experimental primária ou *benchmarks* técnicos verificáveis (`P = 0.5`).

### RQ4 — Riscos, Superfícies de Ataque, Governança e Limitações (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Desafios técnicos e éticos gerais (Seção 3.1, p. 5):** Discute alto custo computacional e energético, opacidade de modelos *black-box* (falta de explicabilidade), vieses algorítmicos e riscos de privacidade.
  - **Riscos de terceirização e conformidade regulatória (Seção 6.3, pp. 9–10; Seção 7.3, p. 11):** Analisa riscos de perda de controle sobre dados sensíveis (*GDPR*, *HIPAA*), aprisionamento tecnológico (*vendor lock-in*), custos ocultos e desalinhamento cultural na adoção de agentes terceirizados, além de contrastar o modelo regulatório estrito do *EU AI Act* com a abordagem de autorregulação nos EUA (Seção 7.3, p. 11).
  - **Diretrizes de segurança e privacidade (Seção 8.5, p. 13):** Recomenda criptografia, autenticação forte, conformidade com *PCI-DSS* e *HIPAA*, defesa contra ataques adversariais e testes de penetração regulares.
  - **Limitação:** Não aprofunda ameaças específicas de arquiteturas agênticas baseadas em LLMs (como *indirect prompt injection*, *tool misuse*, *memory poisoning* ou alucinações em cascata entre micro-agentes) nem especifica *guardrails* arquiteturais em nível de protocolo.
- **Justificativa:** Aborda governança, conformidade regulatória (*GDPR*, *HIPAA*, *EU AI Act*) e riscos organizacionais de forma relevante, mas superficial quanto a vetores de ataque técnico-agênticos específicos (`P = 0.5`).

### RQ5 — Lacunas, Tendências e Direções Futuras (`P = 0.5`)
- **Evidências concretas no artigo:**
  - **Agenda de evolução tecnológica (Seção 5.4, p. 8; Seção 9.2, p. 14):** Identifica cinco direções principais para pesquisas futuras: (1) **Explainable Agentic AI (XAI)** para tornar rastreáveis as decisões autônomas em domínios críticos; (2) **People-to-AI Collaboration**, evoluindo de comandos estáticos para compartilhamento dinâmico de metas e negociação em tempo real entre humanos e agentes; (3) **Federated Agentic AI**, combinando aprendizado federado com sistemas multiagentes para preservar privacidade entre organizações; (4) integração com **computação quântica e Edge AI** rumo a um *Cognitive Autopilot*; e (5) necessidade de estudos de caso empíricos específicos por indústria.
- **Justificativa:** Aponta tendências futuras claras (*XAI agêntico*, *Federated Agentic AI*, colaboração humano-agente dinâmica), embora formuladas em nível macro e sem um roteiro formal específico para operações de segurança/TI (`P = 0.5`).

---

## Síntese Quantitativa de Aderência às Questões de Pesquisa

$$\text{SCORE\_RQ} = 1.0 + 1.0 + 0.5 + 0.5 + 0.5 = 3.5 \text{ / } 5.0$$

---

## Tabelas Consolidadas para o Artigo da RSL

### Tabela A — Metadados e Caracterização (Dados para Tabelas 3 e 5 da RSL)

| Campo | Conteúdo Extraído |
|---|---|
| **ID** | P02 |
| **Autores** | Soodeh Hosseini; Hossein Seilani |
| **Ano** | 2025 |
| **Título** | *The role of agentic AI in shaping a smart future: A systematic review* |
| **Periódico / Fonte** | *Array* (Elsevier), Vol. 26, Art. 100399, pp. 1–15 |
| **DOI** | `10.1016/j.array.2025.100399` |
| **Qualis** | A1 *(pré-verificado no protocolo)* |
| **Quartil SJR** | Q1 *(pré-verificado no protocolo)* |
| **Fator de Impacto / SJR** | `[VERIFICAR]` *(não consta no PDF)* |
| **Citações** | `[VERIFICAR]` *(métrica externa dinâmica)* |
| **Tipo de Estudo** | Revisão de Literatura (intitulada *Systematic Review*, porém autodeclarada no resumo como *Narrative Review*) |
| **Domínio Principal** | Sistemas de IA Agêntica (*Agentic AI*), Automação Corporativa, *AI-as-a-Service (AIaaS)* e Transformação Digital |
| **Tecnologias / Frameworks Analisados** | *LangGraph*, *CrewAI*, *AutoGen*, *AutoGPT*, *ChatGPT-4*, *ChatGPT-o1* (*ChatGPT-1*), *Llama 3.1*, *Sierra*, *IBM Watson*, *Amazon SageMaker*, *TensorFlow* |
| **Escopo de Aplicação** | Atendimento ao cliente, finanças e detecção de fraudes, cibersegurança (*AI-driven penetration testers*), saúde, manufatura e cadeia de suprimentos |

---

### Tabela B — Mapeamento de Cobertura das Questões de Pesquisa (Dados para Tabela 7 da RSL)

| Questão de Pesquisa | Classificação | Pontuação | Evidências-Chave no Artigo |
|---|:---:|:---:|---|
| **RQ1** (Fundamentos e Transição) | `T` | `1.0` | Seis pilares de *Agentic AI* (Fig. 1, Tabela 1, pp. 2–3); evolução em 5 estágios (Fig. 2, Tabela 2, pp. 3–5); comparação de 14 dimensões entre *Agentic*, *Generative* e *Autonomous AI* (Tabela 3, pp. 5–6); transição *Copilot* $\to$ *Autopilot* (Seção 5, Fig. 4, pp. 6–8). |
| **RQ2** (Arquiteturas e Orquestração) | `T` | `1.0` | Arquitetura hierárquica em 3 níveis: *Master agent* $\to$ *Orchestrator agent* $\to$ *Micro-agents* (Seção 4, Fig. 3, p. 6; Tabela 4, p. 7); *Service-as-Software* / *AIaaS* (p. 5); comparação técnica e estratégica entre *LangGraph*, *CrewAI*, *AutoGen* e *AutoGPT* (Seção 7, Fig. 5, pp. 10–12; Seção 8.3, p. 13). |
| **RQ3** (Evidências Empíricas e Métricas) | `P` | `0.5` | Compilação de métricas secundárias: até `40%` ganho de produtividade (p. 4), `360.000 h/ano` poupadas no *JPMorgan COiN* (p. 4), `-20–50%` *downtime* (p. 4), `-60%` tempo de resposta em suporte (p. 4), `-30%` custos operacionais e `ROI 3x–5x` em 5 anos com *AIaaS* (p. 5), `-40%` transações fraudulentas (p. 6). Sem experimentos primários. |
| **RQ4** (Riscos, Segurança e Governança) | `P` | `0.5` | Opacidade *black-box*, custo computacional e viés (Seção 3.1, p. 5); riscos de *outsourcing*, *vendor lock-in* e conformidade *GDPR*/*HIPAA*/*PCI-DSS* (Seções 6.3 e 8.5, pp. 9–10, 13); comparação regulatória *EU AI Act* vs. EUA (Seção 7.3, p. 11). Sem modelagem profunda de ameaças agênticas. |
| **RQ5** (Lacunas e Direções Futuras) | `P` | `0.5` | Agenda futura destacando *Explainable Agentic AI (XAI)*, colaboração dinâmica humano-IA, *Federated Agentic AI*, *Cognitive Autopilot* com computação quântica/*Edge AI* e estudos de caso setoriais (Seções 5.4 e 9.2, pp. 8, 14). |
| **Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Aderência Forte (70,0%)** |

---

### Tabela C — Avaliação de Qualidade Metodológica DARE (QA1–QA4)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências |
|---|:---:|:---:|---|
| **QA1 — Critérios de inclusão/exclusão e escopo** | `Y` | `1.0` | O artigo delimita claramente na Seção 1.1–1.2 (pp. 1–3) o escopo temático da revisão: evolução histórica, arquitetura hierárquica, transição *Copilot* para *Autopilot*, frameworks tecnológicos (*LangGraph*, *CrewAI*, *AutoGen*, *AutoGPT*), aplicações industriais e desafios ético-regulatórios da IA agêntica. |
| **QA2 — Busca e transparência metodológica** | `N` | `0.0` | Embora o título contenha a expressão *"A systematic review"*, o próprio *Abstract* (p. 1) declara tratar-se de uma revisão narrativa (*"This narrative review explores the role of Agentic AI..."*). O artigo não possui seção de metodologia de busca: não informa bases consultadas, *strings* de busca, janela temporal de coleta, critérios de triagem nem diagrama PRISMA. |
| **QA3 — Avaliação de qualidade e síntese das fontes** | `P` | `0.5` | Sintetiza 48 referências cobrindo artigos acadêmicos e relatórios industriais em tabelas comparativas estruturadas (Tabelas 1–4, pp. 3–7). Contudo, não realiza avaliação crítica da qualidade dos estudos primários e apresenta inconsistências pontuais de citação na lista de referências (ex.: referências [3] e [4] na p. 14 tratam de tópicos médicos desconectados das afirmações sobre *COiN* e atendimento ao cliente na p. 4). |
| **QA4 — Coerência entre evidências e conclusões** | `P` | `0.5` | As conclusões e recomendações estratégicas de adoção em duas fases (*PoC* com *AutoGen/AutoGPT* $\to$ produção com *LangGraph/CrewAI*, Seções 8.3 e 9, pp. 13–14) são coerentes com a síntese arquitetural apresentada, e a Seção 9.1 (p. 14) reconhece explicitamente as limitações do trabalho (ausência de validação empírica primária), mas as afirmações quantitativas apoiam-se em estatísticas secundárias de mercado não auditadas. |
| **Total (`SCORE_QA`)** | **Banda: Média** | **2.0 / 4.0** | **Qualidade Metodológica Moderada (50,0%)** |

---

## Parecer Final do Revisor

O estudo **P02** (Hosseini & Seilani, 2025), integrante do **Corpus Fundacional** herdado do Trabalho I, constitui uma referência conceitual e arquitetural importante para a RSL (`SCORE_RQ = 3.5 / 5.0`), destacando-se especialmente nas questões **RQ1** (`T = 1.0`) e **RQ2** (`T = 1.0`). Suas principais contribuições para a síntese da revisão incluem: (i) a sistematização clara da transição operacional do modelo **Copilot** (assistência supervisionada com escalonamento humano) para o modelo **Autopilot** (autonomia ponta a ponta); (ii) a formalização da arquitetura hierárquica em três camadas (*Master agent*, *Orchestrator agent* e *Micro-agents* funcionais); e (iii) o mapeamento prático de adoção combinando frameworks de prototipação rápida (*AutoGPT*, *AutoGen*) com frameworks orientados a produção e controle de estado (*LangGraph*, *CrewAI*). Sob a ótica metodológica DARE (`SCORE_QA = 2.0 / 4.0`, banda **Média**), deve-se registrar no texto da RSL que, a despeito do subtítulo *"A systematic review"*, o trabalho configura metodologicamente uma revisão narrativa sem protocolo de busca reprodutível, devendo suas métricas quantitativas de eficiência e *ROI* ser citadas como estimativas secundárias de mercado.
