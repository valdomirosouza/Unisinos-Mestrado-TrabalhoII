# Extração PICOC dos Estudos sobre Agentic AI Copilot e Resposta a Incidentes

**Protocolo aplicado:** `picoc-extraction.md` v1.0.0  
**Corpus analisado:** 39 artigos em PDF  
**Cobertura documental:** P01–P35 e P37–P40. O estudo P36 não foi fornecido e, portanto, não integra esta extração.  
**Unidade de referência:** as páginas indicadas correspondem à numeração física do PDF. Quando disponível, a seção do artigo também é informada.  
**Regra de extração:** somente informações declaradas nos artigos foram utilizadas. Elementos sem suporte explícito foram registrados como `NÃO DECLARADO` ou `N/A`.

## 1. Raciocínio auditável por artigo

### P01 — *Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment*

- **Population:** o artigo trata de sistemas de Agentic AI com memória, raciocínio, planejamento e uso de ferramentas, implantados em ambientes dinâmicos e de alto risco, como saúde, infraestrutura crítica e cibersegurança (Seção 1, pp. 1–3).
- **Intervention:** a solução analisada é uma abordagem transversal de confiabilidade que combina arquiteturas agênticas, taxonomia de ameaças, defesa em camadas, zero trust, governança, supervisão humana e avaliação orientada à observabilidade (Seções 4, 6 e 9, pp. 10–24 e 44–45).
- **Comparison:** há comparação explícita entre arquiteturas monoagente, multiagente, federadas/descentralizadas e híbridas, além do contraste com políticas estáticas e modelos convencionais de segurança (Seção 4.5, p. 13; resumo, p. 1).
- **Outcomes e Context:** os resultados esperados ou reportados incluem segurança, resiliência, transparência, accountability, detecção mais rápida e menor carga humana. O caso ReliaQuest é citado como melhoria na velocidade de detecção e redução do trabalho humano, mas como evidência secundária da revisão (Seção 7.2, p. 27). O contexto inclui operações de cibersegurança, automação industrial, governo, defesa e políticas públicas.

### P02 — *The role of agentic AI in shaping a smart future: A systematic review*

- **Population:** organizações e processos de negócio que adotam Agentic AI em diferentes setores, incluindo atendimento, saúde, cibersegurança, operações e automação empresarial (Resumo e Seções 1–4, pp. 1–6).
- **Intervention:** agentes baseados em ferramentas como LangChain, CrewAI, AutoGen e AutoGPT, com estruturas hierárquicas e evolução do modelo assistivo **Copilot** para o modelo autônomo **Autopilot** (Resumo, p. 1; Seção 5, pp. 6–8).
- **Comparison:** o artigo compara Copilot com Autopilot e também diferencia Agentic AI, Generative AI e Autonomous AI (Tabela 3 e Seção 5, pp. 6–7).
- **Outcomes e Context:** são reportados ganhos de produtividade, redução de custos, inovação, rapidez na prestação de serviços e menor necessidade de supervisão. Não são declaradas métricas de MTTD, MTTR ou carga cognitiva aplicadas especificamente à resposta a incidentes. O contexto é estratégico e organizacional, com adoção multissetorial (Resumo, p. 1; Conclusão, p. 13).

### P03 — *A Research Landscape of Agentic AI and Large Language Models: Applications, Challenges and Future Directions*

- **Population:** aplicações de LLMs e Agentic AI em educação, saúde, cibersegurança, veículos autônomos, comércio eletrônico e atendimento ao cliente (Resumo, p. 1).
- **Intervention:** arquiteturas agênticas baseadas em LLMs que utilizam ferramentas, APIs, memória, coordenação multiagente e supervisão humana para executar fluxos autônomos (Seções 2–5, pp. 3–23).
- **Comparison:** a revisão não possui baseline central. Há apenas demonstrações exploratórias comparando GPT-4o e DeepSeek-R1 em questões de viés e inclusão cultural; os autores esclarecem que não constituem avaliação rigorosa ou totalmente reproduzível (Seção 4, pp. 12–18).
- **Outcomes e Context:** no cenário de cibersegurança, os agentes podem avaliar incidentes, priorizar riscos e executar contenção e remediação com rapidez. O artigo também identifica riscos de desalinhamento, decisões opacas, baixa supervisão, privacidade, segurança e coordenação multiagente. Não apresenta MTTD/MTTR quantitativos (Seção 3, pp. 9–10; Conclusão, p. 25).

### P04 — *LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead*

- **Population:** tarefas de Engenharia de Software ao longo do SDLC, incluindo requisitos, geração de código, qualidade, manutenção, depuração, localização de falhas e análise de causa raiz em ambientes de nuvem (Seção 3, pp. 6–10).
- **Intervention:** sistemas multiagentes baseados em LLMs, compostos por agentes especializados que planejam, colaboram, revisam e executam tarefas. O RCAgent, por exemplo, coleta dados do sistema, analisa logs e diagnostica falhas (Seção 3.3, p. 8).
- **Comparison:** `N/A (revisão de mapeamento)`. Os dois estudos de caso avaliam capacidades e limitações do ChatDev, mas não utilizam um baseline humano ou uma técnica tradicional controlada (Seção 4, pp. 10–12).
- **Outcomes e Context:** no jogo Snake, a segunda tentativa gerou uma solução funcional, com média de 76 segundos e custo de US$ 0,019 por tentativa. No Tetris, a solução surgiu apenas na décima tentativa e permaneceu incompleta, apesar de média de 70 segundos e US$ 0,020 por execução. O contexto principal é desenvolvimento e manutenção de software, não operação de incidentes em produção (Seção 4, pp. 11–12; Conclusão, p. 22).

### P05 — *A Survey of AIOps in the Era of Large Language Models*

- **Population:** sistemas de software e equipes de operação que trabalham com logs, métricas, séries temporais, traces, relatórios de incidentes e outros dados de falha em atividades de AIOps (Resumo e Seções 1–3, pp. 1–10).
- **Intervention:** LLM4AIOps aplicado ao ciclo de percepção de falhas, análise de causa raiz e remediação assistida, por meio de prompting, fine-tuning, RAG, agentes com ferramentas e geração ou execução de scripts (Seções 4–5, pp. 11–21).
- **Comparison:** o estudo contrasta AIOps tradicional, baseado em ML/DL e alta intervenção manual, com abordagens baseadas em LLMs. Também discute a alternativa de modelos menores combinados com especialistas humanos quando custo e eficiência tornam LLMs pouco práticos (Seções 1.1 e 7.1, pp. 3 e 24).
- **Outcomes e Context:** os outcomes abrangem detecção, classificação, RCA, geração de relatórios, recomendação de solução, execução de remediação e novas métricas de classificação, geração, execução e avaliação humana. A automação de remediação ainda se concentra em triagem ou recomendação, e a integração ponta a ponta permanece uma lacuna. O contexto é AIOps e resposta operacional a incidentes em software, inclusive microsserviços e clusters (Seções 4–7, pp. 11–26).

### P06 — *Agentic AI: A Comprehensive Survey of Technologies, Applications, and Societal Implications*

- **Population:** sistemas agênticos aplicados a robótica, saúde, veículos autônomos, automação do trabalho, cadeias de suprimentos e outras áreas dinâmicas (Resumo, p. 1).
- **Intervention:** Agentic AI com autonomia, memória, comportamento orientado a objetivos, raciocínio adaptativo, reinforcement learning e orquestração de múltiplos agentes (Seções 1–5, pp. 1–9).
- **Comparison:** o artigo compara Agentic AI com IA tradicional, caracterizada por regras predefinidas, baixa adaptabilidade e tarefas estreitas (Tabela 1, p. 2).
- **Outcomes e Context:** como evidência secundária, o artigo cita dados de aproximadamente 500 organizações com redução de 34,2% no tempo de conclusão de tarefas, aumento de 7,7% na acurácia e melhoria de 13,6% no uso de recursos. Também menciona automação de resposta a ameaças cibernéticas, sem detalhar MTTD/MTTR ou um experimento próprio nesse domínio (pp. 2 e 9; Conclusão, p. 11 do corpo do artigo, PDF p. 11).

### P07 — *Artificial Empathy: A New Perspective for Analyzing and Designing Multi-Agent Systems*

- **Population:** agentes autônomos em sistemas multiagentes envolvidos em cooperação e competição, avaliados em jogos simulados (Resumo, p. 1; Seções 2–5, pp. 2–15).
- **Intervention:** modelo de empatia formulado como problema de otimização e algoritmo **Empathy-based Interactive Learner (EIL)** para avaliação afetiva de utilidade e aprendizagem adaptativa (Resumo, p. 1).
- **Comparison:** EIL é comparado com agentes Q-learning e estratégia multi-step; o artigo também controla diferentes modos e temperaturas do mecanismo de empatia (Seção 5, p. 11).
- **Outcomes e Context:** EIL aumenta cooperação, altruísmo e percepção de justiça no modo de igualdade, enquanto outros modos aumentam o comportamento de interesse próprio. O contexto é experimental e simulado, com dilema do prisioneiro, ultimatum game, variante multiusuário e survival game. Não há relação declarada com incidentes de TI (Resumo, p. 1; Conclusão, p. 15).

### P08 — *Applications, Challenges, and Future Directions of Human-in-the-Loop Learning*

- **Population:** sistemas de automação baseados em ML em saúde, finanças, educação, manufatura, robótica, visão computacional e outros domínios da Indústria 4.0 (Resumo e Seções 1–4, pp. 1–16).
- **Intervention:** Human-in-the-Loop Learning, integrando conhecimento humano a modelos de ML por active learning, iterative ML, reinforcement learning e diferentes formas de feedback (Resumo, p. 1).
- **Comparison:** `N/A (revisão)`. O texto contrapõe conceitualmente automação puramente algorítmica e automação com conhecimento humano, mas não apresenta um único experimento ou baseline consolidado.
- **Outcomes e Context:** os benefícios declarados incluem maior acurácia, accountability, transparência, melhor decisão, automação de tarefas repetitivas e melhoria de desempenho. O contexto é colaboração humano-máquina em múltiplos setores; resposta a incidentes não é declarada como objeto do estudo (Resumo, p. 1; Conclusão, p. 20).

### P09 — *AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges*

- **Population:** AI Agents e sistemas de Agentic AI aplicados a tarefas digitais, pesquisa, robótica, saúde e ambientes corporativos de TI e cibersegurança (Resumo e Seções 1–4, pp. 1–16).
- **Intervention:** ecossistemas multiagentes com decomposição dinâmica de tarefas, memória persistente, coordenação, ferramentas externas e orquestração central ou distribuída (Resumo, pp. 1–2).
- **Comparison:** o estudo compara AI Agents modulares e específicos com Agentic AI multiagente. No caso de cibersegurança, também contrasta o fluxo agêntico com sistemas tradicionais baseados em regras (pp. 1–3 e 16).
- **Outcomes e Context:** no exemplo de resposta a incidentes corporativos, agentes classificam ameaças, correlacionam logs, analisam compliance e simulam mitigação. O artigo reporta menor latência decisória, redução de falsos positivos, contenção proativa e respostas futuras mais rápidas e precisas, sem valores quantitativos. O contexto é uma taxonomia conceitual com um cenário explícito de incident response empresarial (Seção 4, pp. 16–17; Conclusão, p. 25).

### P10 — *Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey*

- **Population:** sistemas autônomos que perseguem objetivos complexos em ambientes mutáveis, com aplicações em saúde, finanças, manufatura, software adaptativo, cibersegurança e outros setores (Resumo e Introdução, pp. 1–3).
- **Intervention:** Agentic AI baseada em goal-oriented architectures, reinforcement learning, adaptive control, planejamento, aprendizagem, uso de ferramentas e colaboração humano-IA (Seções 2–6, pp. 3–10).
- **Comparison:** IA agêntica é contrastada com IA tradicional, que depende de instruções estruturadas, supervisão próxima e limites rígidos (Resumo e Seção 2, pp. 1–3).
- **Outcomes e Context:** os efeitos discutidos incluem produtividade, eficiência, adaptabilidade, escalabilidade, decisão contextual, redução de atrasos por manutenção preditiva e melhor colaboração humano-IA. Não há avaliação específica de MTTD, MTTR ou operação de incidentes; o contexto é multissetorial e conceitual (Seções 5–8, pp. 8–17; Conclusão, p. 22).

### P11 — *Co-Evolving Multi-Agent Transfer Reinforcement Learning via Scenario Independent Representation*

- **Population:** políticas e agentes MARL em sistemas multiagentes com cenários cooperativos e competitivos no SMAC e MP-SMAC, baseados em StarCraft II (Resumo e Metodologia, pp. 1–8).
- **Intervention:** framework **Co-MACTRL**, que combina coevolução, curriculum transfer learning e representação independente de cenário para reutilizar conhecimento entre tarefas e oponentes (Resumo, pp. 1–3).
- **Comparison:** comparação com MARL baseline, agentes aprendendo do zero, oponentes estáticos do SMAC e o framework Co-MARL sem curriculum transfer learning (pp. 2–4 e Seção de resultados, pp. 8–11).
- **Outcomes e Context:** são reportadas melhorias no desempenho de aprendizagem, taxa média de vitória, eficiência amostral, robustez e generalização entre cenários. O contexto é simulação de jogos multiagentes; o artigo apenas sugere aplicações futuras em aeronaves e veículos autônomos, sem vínculo declarado com incidentes de TI (Resumo, pp. 1–3; resultados, pp. 8–11; conclusão, p. 12).

### P12 — *Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey*

- **Population:** sistemas autônomos e ciberfísicos, incluindo UAVs, veículos autônomos, braços robóticos, edge robots e frotas ou enxames cooperativos (Resumo e Seção 1, pp. 1–3).
- **Intervention:** GenAI baseada em GANs, VAEs, Transformers e LLMs para arquiteturas seguras, manutenção preditiva, detecção de anomalias, gestão de falhas e resposta adaptativa a ameaças (Resumo e Seções 2–5, pp. 1–20).
- **Comparison:** o artigo contrasta GenAI com abordagens tradicionais de AI/ML, destacando criação dinâmica de conteúdo e decisão contextual em tempo real como diferenciais (Seção 1, p. 2).
- **Outcomes e Context:** os outcomes incluem maior segurança, resiliência, autoconsciência, autonomia, eficiência, detecção de intrusão, risk assessment, fault management e robustez de comunicação. O contexto é segurança de sistemas autônomos, edge robotics, operações de drones e ameaças ciberfísicas; há human-machine teaming, mas não MTTD/MTTR de operações de TI (Resumo, pp. 1–2; Seção 4, p. 13; Conclusão, p. 20).

### P13 — *Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach*

- **Population:** sistemas de varejo e decisões relacionadas a inventário, previsão de demanda, feedback de clientes, resiliência e desenvolvimento de software orientado a testes (Resumo e Seções 1–3, pp. 1–4).
- **Intervention:** **Retail Resilience Engine (RRE)**, que integra TDD, LLM, arquitetura Agentic AI, camadas modulares, gerenciamento de features e filtragem de entradas (Seção 3, pp. 4–9).
- **Comparison:** especialistas humanos com mais de dez anos de experiência em desenvolvimento de sistemas de varejo são usados como baseline (Seção 4, p. 10).
- **Outcomes e Context:** o RRE alcança 97,5% de similaridade com decisões de especialistas, acurácia superior a 90% nos cenários testados, métricas de accuracy, precision, recall e F1 estáveis e bloqueio de 98,2% das entradas irrelevantes. O contexto é experimental no domínio de varejo e TDD, não resposta a incidentes de TI (Resumo, p. 1; resultados e conclusão, pp. 10–16).

### P14 — *Transforming cybersecurity with agentic AI to combat emerging cyber threats*

- **Population:** Security Operations Centers, analistas de segurança, ambientes corporativos, ativos digitais e fluxos de detecção, triagem, contenção, remediação e resposta a incidentes (Resumo e Seções 1–3, pp. 1–4).
- **Intervention:** Agentic AI e redes de agentes especializados para análise de threat intelligence, triagem, detecção, decisão, execução de ações, remediação e automação de tarefas Tier 1 e Tier 2 (pp. 1–4).
- **Comparison:** abordagens humanas ou tradicionais e reativas de cibersegurança são contrastadas com defesa autônoma, adaptativa e em tempo real. A tabela de casos também compara diferentes produtos e resultados operacionais (pp. 3–4 e Seção 6, p. 7).
- **Outcomes e Context:** o artigo reporta, a partir de casos industriais, redução de 90% no tempo de triagem, 30% de redução no MTTR com Microsoft Security Copilot, contenção em menos de cinco minutos em um caso e ganhos de velocidade e acurácia para profissionais iniciantes e experientes. Também destaca redução de falsos positivos, carga operacional e tempo de resposta. O contexto é diretamente SOC e cybersecurity incident response, com necessidade de governança e supervisão humana (pp. 3–4, 7 e 10).

### P15 — *The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges*

- **Population:** sistemas de Agentic AI baseados ou não em LLMs, aplicados a múltiplos domínios e formados por componentes de percepção, planejamento, execução, memória, reflexão, orquestração e interação (Resumo e Seções 1–3, pp. 1–20).
- **Intervention:** frameworks como LangChain, AutoGPT, BabyAGI, AutoGen e OpenAgents, combinando LLMs, reinforcement learning, memória explícita, feedback, uso de ferramentas e colaboração multiagente (Resumo, p. 1; Conclusão, p. 40).
- **Comparison:** comparação conceitual com IA tradicional, IA generativa, sistemas autônomos e diferentes estilos arquiteturais e de orquestração; não há baseline experimental único (Seções 1–3, pp. 3–21).
- **Outcomes e Context:** o artigo classifica métricas qualitativas e quantitativas de desempenho, confiabilidade, segurança e satisfação, além de métodos como HITL verification e UAT. Observabilidade, tolerância a falhas, throughput e rastreabilidade são requisitos arquiteturais. Incident response aparece como aplicação de entradas acionadas por alertas, porém sem MTTD/MTTR próprio (pp. 15, 19–20, 32, 35 e 40).

### P16 — *A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey*

- **Population:** projetos de ciência de dados, sistemas de TI, infraestruturas de telecomunicações, ambientes industriais e organizações que adotam MLOps ou AIOps (Resumo e Seções 1–5, pp. 1–21).
- **Intervention:** metodologias, arquiteturas e práticas de MLOps/AIOps para monitoramento, detecção de anomalias, predição de falhas, RCA, remediação, resource management e automação operacional (Seções 4–5, pp. 11–21).
- **Comparison:** o estudo compara MLOps e AIOps quanto à adoção, domínios, frameworks e cobertura do ciclo de vida. Não existe baseline experimental controlado (Resumo e discussão, pp. 1 e 19–21).
- **Outcomes e Context:** AIOps é associado à prevenção, predição, detecção, análise de causa raiz e remediação. O artigo cita uso de logs na remediação e potencial para prever e resolver incidentes de ITSM no menor tempo, mas observa que a automação permanece limitada e concentrada em detecção e RCA. O contexto inclui indústria, academia, DevOps, ITSM, 5G e 6G (pp. 19–22; Conclusão, p. 22).

### P17 — *A Review of Trustworthy and Explainable Artificial Intelligence (XAI)*

- **Population:** sistemas de IA em bancos, saúde, IoT, sistemas autônomos e veículos autônomos, especialmente onde decisões opacas podem causar risco humano ou operacional (Resumo, p. 1).
- **Intervention:** Trustworthy AI e Explainable AI, incluindo transparência, explicações post hoc, robustez, segurança, privacidade, fairness, accountability e governança com HITL, HOTL ou HIC (Seções 2–4, pp. 3–14).
- **Comparison:** sistemas confiáveis e explicáveis são contrastados com modelos black box, vulneráveis, enviesados ou não interpretáveis (Resumo e Seções 2–3, pp. 1–10).
- **Outcomes e Context:** os outcomes são confiabilidade, interpretabilidade, rastreabilidade, precisão consistente, segurança, responsabilização e capacidade de revisão humana. O contexto é multissetorial e de alto risco, com ênfase em veículos autônomos. Não há resultados específicos de resposta a incidentes ou métricas MTTD/MTTR (Resumo, p. 1; supervisão humana, p. 4; Conclusão, p. 19).

### P18 — *An architecture for model-based and intelligent automation in DevOps*

- **Population:** sistemas complexos e software-intensive, pipelines DevOps e dez estudos de caso industriais do projeto AIDOaRt (Resumo e Seção 1, pp. 1–2).
- **Intervention:** arquitetura AIDOaRt, que integra AI/ML, Model-Driven Engineering e AIOps para coleta e tratamento de dados, monitoramento, análise, RCA, predição, remediação, response automation e atividades de Engenharia de Software (Seções 2–4, pp. 2–7).
- **Comparison:** `N/A (avaliação arquitetural sem baseline controlado)`. A arquitetura foi avaliada por sua implementação e aplicação em estudos de caso, não contra uma arquitetura concorrente única.
- **Outcomes e Context:** com dez casos industriais e 54 soluções tecnológicas, os autores reportam viabilidade, aplicabilidade, utilidade, integração, satisfação de requisitos e apoio ao desenvolvimento. A arquitetura contempla automação de incident handling e threat mitigation, mas o artigo não mede MTTD/MTTR. O contexto é DevOps industrial, continuous engineering e validação (pp. 6–7, 17–19).

### P19 — *Agent System Mining: Vision, Benefits, and Challenges*

- **Population:** organizações vistas como sistemas multiagentes, seus processos de negócio, agentes autônomos e event logs de operações reais (Resumo e Seções 1–3, pp. 1–6).
- **Intervention:** **Agent System Mining (ASM)**, que combina Process Mining e Agent-Based Modeling para inferir modelos MAS a partir de dados de eventos e relacionar atividades ao ciclo de modelagem (Resumo e Seção 4, pp. 1 e 6–10).
- **Comparison:** ASM é contrastado com Process Mining tradicional e seus modelos de controle macro do tipo “spaghetti”, que dificultam visualização e compreensão de processos complexos (Seção 2, pp. 2–4).
- **Outcomes e Context:** os benefícios são modelos mais compreensíveis, análise de comportamentos locais, descoberta de oportunidades de melhoria e suporte à simulação e evolução de processos. Não são apresentadas métricas quantitativas nem relação explícita com resposta a incidentes. O contexto é BPM e um exemplo de order fulfillment baseado em event logs (pp. 2–10; Conclusão, p. 13).

### P20 — *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code*

- **Population:** templates AWS CloudFormation e fluxos de Infrastructure-as-Code usados para provisionar infraestrutura em nuvem, especialmente em pipelines CI/CD (Resumo e Introdução, p. 1).
- **Intervention:** workflow multiagente baseado em LLM, RAG e base de conhecimento continuamente atualizada, com agentes para detecção de vulnerabilidades e geração de relatórios e correções contextuais (Seções III–IV, pp. 3–4).
- **Comparison:** a proposta é contrastada com ferramentas estáticas ou baseadas em regras, como CDK-Nag, e com auditorias manuais, que podem não identificar vulnerabilidades compostas ou dependentes do contexto (Introdução, p. 1; Resultados, pp. 4–6).
- **Outcomes e Context:** o sistema alcançou taxa de detecção de 85%, com 15% de falsos positivos e 5% de casos de correção excessiva. A latência ficou entre 80 e 100 segundos por template. O contexto é segurança preventiva de IaC antes da implantação, não resposta a incidentes já ocorridos (Resumo, p. 1; Seção V, pp. 4–6; Conclusão, p. 7).

### P21 — *Small Language Model Agent for the Operations of Continuously Updating ICT Systems*

- **Population:** operações de sistemas ICT e redes cujos procedimentos, manuais e políticas são continuamente atualizados; a avaliação utiliza ALFWorld e o ambiente real WideEnet (Resumo e Introdução, pp. 1–2; Seção V, pp. 7–10).
- **Intervention:** agente baseado em Small Language Model com *nested thoughts*, reconfiguração de prompts, recuperação por blocos e seleção de exemplos para evitar *shortcut reasoning* e incorporar procedimentos mais recentes (Seções III–IV, pp. 3–7).
- **Comparison:** são utilizados Act, ReAct e RAP como baselines, com SLMs e resultados reportados para GPT-3.5 e GPT-4 (Seção V-B, p. 7).
- **Outcomes e Context:** no ALFWorld, LLaMA2 atingiu 96,3%, acima do ReAct com GPT-4, 85,8%, e do RAP com GPT-4, 94,8%. No WideEnet, Mistral e LLaMA2 alcançaram 88,9% e 87,0%; após uma terceira atualização, o desempenho passou de 29,4% para 78,8%. Há sobrecarga computacional de aproximadamente 2,1 vezes mais chamadas ao modelo que o ReAct. O foco experimental é operação e configuração de redes, com aplicação potencial em troubleshooting e RCA (Resultados, pp. 8–10).

### P22 — *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control*

- **Population:** infraestruturas Kubernetes distribuídas entre nuvem, borda e IoT, submetidas a violações de SLA, falhas de recursos e problemas de configuração (Resumo e Introdução, pp. 1–2).
- **Intervention:** framework fechado de monitoramento, RCA e mitigação, no qual agentes LLM selecionam ações corretivas, como escalonamento, reagendamento de pods e atualização de configuração, por ferramentas expostas via MCP, seguidas de validação pós-ação (Seções III–IV, pp. 3–6).
- **Comparison:** GPT-5 é comparado ao GPT-5-mini em topologias, falhas e ferramentas equivalentes, funcionando o modelo menor como baseline de menor custo (Protocolo experimental, pp. 6–7).
- **Outcomes e Context:** o resumo reporta 52,9% de identificação de violações e 70,7% de mitigação bem-sucedida no agregado. Na análise específica do GPT-5, o artigo informa aproximadamente 78% de identificação de causa e 80% de restauração do SLA. O contexto é um benchmark reproduzível com workloads IoT sintéticos e falhas injetadas, portanto não representa operação produtiva contínua (Resumo, p. 1; Resultados, pp. 7–9; Conclusão, p. 9).

### P23 — *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems*

- **Population:** sistemas cloud-native baseados em microsserviços, observados por métricas, logs, traces e grafos de dependência dinâmicos (Resumo e Introdução, pp. 1–2).
- **Intervention:** agente LLM assistido por três ferramentas especializadas para alinhamento multimodal, localização da causa raiz e classificação do tipo de falha, seguido da geração de estratégias de reparo contextualizadas (Seções III–IV, pp. 3–7).
- **Comparison:** TAMO é comparado a Eadro, HolisticRCA, baselines unimodais de séries temporais, LightGBM e variantes de ablação, inclusive uso direto de dados brutos pelo LLM (Seção V, pp. 7–11).
- **Outcomes e Context:** no conjunto An, atingiu microprecisão de 0,8718 e micro-F1 de 0,8831, com ganhos de 24,99% e 19,85% sobre HolisticRCA. Em As e Ap, a microprecisão foi 0,7164 e 0,7182. A inferência levou cerca de 0,17 segundo por amostra. As estratégias de reparo são avaliadas como saída textual, sem execução controlada da correção (Resultados, pp. 8–11).

### P24 — *AgentAI: A Comprehensive Survey on Autonomous Agents in Distributed AI for Industry 4.0*

- **Population:** agentes autônomos e não autônomos em IA distribuída, cobrindo múltiplos domínios da Indústria 4.0 e sua evolução para Indústria 5.0 e 6.0 (Resumo, p. 1; Seções 2–5, pp. 2–13).
- **Intervention:** AgentAI integrado a foundation models, LLMs, VLMs, memória, percepção, raciocínio, comunicação e tomada de decisão autônoma ou colaborativa (Introdução, pp. 1–2; Taxonomia, pp. 4–8).
- **Comparison:** `N/A (estudo de mapeamento)`. O artigo realiza contrastes conceituais entre agentes não autônomos e plenamente autônomos e compara sua cobertura com surveys anteriores, sem baseline experimental único.
- **Outcomes e Context:** os benefícios sintetizados incluem eficiência, escalabilidade, robustez, flexibilidade, produtividade, segurança e adaptabilidade. Não são reportadas medidas próprias de MTTD, MTTR ou carga cognitiva. O contexto é industrial e multissetorial, não exclusivamente resposta a incidentes (Discussão, pp. 14–15).

### P25 — *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments*

- **Population:** ambientes de cyber range, agentes ofensivos e defensivos e profissionais treinados em cenários de ataque e resposta, utilizando CICIDS2017 e UNSW-NB15 (Resumo e Introdução, pp. 1–3).
- **Intervention:** MAS orientado por IA integrado ao CyDER 2.0, com agentes atacantes baseados em reinforcement learning, agentes defensivos de detecção de anomalias e coordenação automatizada de ações de resposta (Arquitetura e implementação, pp. 6–12).
- **Comparison:** o framework é comparado a simuladores estáticos ou baseados em regras e a abordagens anteriores com menor adaptação e escala (Introdução, pp. 1–3; Tabela comparativa, p. 18).
- **Outcomes e Context:** o artigo reporta cerca de 91% de F1 ou acurácia de detecção, latência de resposta de 5,3 segundos e suporte a mais de 25 agentes, enquanto o baseline apresentado registra aproximadamente 65%, mais de 15 segundos e menos de cinco agentes. Os resultados são obtidos em cyber range controlado, e não em SOC de produção (Resultados, pp. 13–18).

### P26 — *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications*

- **Population:** aplicações multisserviço em nuvem, microsserviços e sistemas industriais, analisadas por logs, traces, métricas e relatórios (Resumo, p. 1; Seções II–III, pp. 2–6).
- **Intervention:** famílias de técnicas de RCA estatísticas, baseadas em ML/DL, grafos, causalidade, modelos híbridos e abordagens recentes com LLMs, além de datasets e ferramentas (Seções III–VI, pp. 3–15).
- **Comparison:** `N/A (estudo de mapeamento)`. A revisão organiza e contrasta métodos por cenário, tipo de dado e família algorítmica, sem executar um benchmark unificado.
- **Outcomes e Context:** o estudo consolida métricas como acurácia, precisão, recall, F1, Top-k e tempo de diagnóstico, mas não produz um resultado operacional próprio. O contexto é diagnóstico de falhas no dia a dia de operação e manutenção de serviços complexos (Resumo, p. 1; Seções VI–VII, pp. 13–16).

### P27 — *Leveraging Multi-Agent Framework for Root Cause Analysis*

- **Population:** plataformas cloud-native e infraestruturas distribuídas de medição de energia, nas quais SREs analisam logs, métricas e traces para diagnosticar falhas (Resumo e Introdução, pp. 1–2).
- **Intervention:** MA-RCA, com agentes especializados em análise, recuperação de conhecimento, validação dinâmica e geração de relatório; RAG ancora hipóteses em documentação histórica e testes sobre dados de runtime verificam as causas propostas (Seções 3–4, pp. 3–7).
- **Comparison:** CoT, RAG, RCACOPILOT, RCAgent, mABC, arquiteturas monoagente e variantes multiagentes por votação são usados como baselines (Seção 5, pp. 7–10).
- **Outcomes e Context:** MA-RCA atingiu acurácia de 0,958 e F1 de 0,952 no Nezha e acurácia de 0,843 e F1 de 0,828 no domínio de energia. As ablações mostram queda importante sem colaboração multiagente, RAG e validação. O contexto é RCA automatizada em datasets de telemetria e cenários reais ou representativos, não medição longitudinal de MTTR em produção (Resultados, pp. 8–11).

### P28 — *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models*

- **Population:** dados de e-mail, logs e varreduras de IP ou rede, analisados por equipes de segurança diante de phishing, APTs e ataques multietapas (Resumo e Introdução, pp. 1–3).
- **Intervention:** arquitetura modular com agentes de verificação de e-mail, análise de logs e varredura de IP, coordenados por um recomendador contextual que correlaciona evidências e produz explicações estruturadas com LLMs (Seções III–IV, pp. 4–11).
- **Comparison:** a solução é comparada a SIEMs e mecanismos tradicionais baseados em regras, além de pipelines isolados ou monoagentes (Introdução, pp. 2–3; Resultados, pp. 11–14).
- **Outcomes e Context:** alcançou 93,6% de acurácia de detecção, 87% de acurácia na correlação multiagente, F1 de 0,94, redução de 41,3% nos falsos positivos e de 38,5% no tempo de triagem. A avaliação usa datasets públicos e ambientes de rede simulados, aproximando um cenário SOC, mas sem operação produtiva longitudinal (Resumo, p. 1; Resultados, pp. 11–14).

### P29 — *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review*

- **Population:** sistemas modernos de TI que produzem grandes volumes de logs e equipes de AIOps responsáveis por detectar anomalias e preservar disponibilidade (Resumo e Introdução, pp. 1–2).
- **Intervention:** métodos de detecção de anomalias em logs baseados em LLMs, especialmente prompt engineering, RAG e fine-tuning (Seções 3–5, pp. 3–12).
- **Comparison:** a revisão contrasta métodos tradicionais de ML/DL e frameworks do estado da arte com abordagens orientadas por LLMs (Resumo, p. 1; Síntese, pp. 6–12).
- **Outcomes e Context:** os estudos revisados indicam ganhos em F1, precisão, recall, interpretabilidade e adaptação a mudanças, mas a revisão não executa experimento próprio nem consolida MTTD ou MTTR. O contexto é AIOps para log anomaly detection, com extensão discutida para defesa e operações militares (Conclusão, p. 14).

### P30 — *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports*

- **Population:** defeitos reportados em mecanismos de inferência LLM, principalmente vLLM e TensorRT-LLM, representados por issues e discussões de desenvolvedores (Resumo e Introdução, pp. 1–3).
- **Intervention:** classificação estática de causa raiz a partir de texto, localização de módulo por similaridade e geração de sugestões de reparo com padrões estruturados e LLMs, sem executar o código afetado (Seções 3–4, pp. 5–10).
- **Comparison:** classificadores como SVM linear e Random Forest, baselines aleatórios ou de classe mais frequente e avaliação cross-engine são usados para comparação (Seção 5, pp. 11–15).
- **Outcomes e Context:** a classificação de RCA alcançou acurácia de 0,688 e macro-F1 de 0,421; a localização obteve Top-1 de 0,705 e Top-2 de 0,841. No TensorRT-LLM, a acurácia foi 0,640. Avaliadores humanos atribuíram ao GPT notas médias de 3,7 para correção, 3,6 para utilidade e 4,3 para clareza. O contexto é triagem estática de bugs, não resposta operacional em runtime (Resultados, pp. 12–15; Conclusão, p. 16).

### P31 — *LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services*

- **Population:** serviços cloud-native de uma infraestrutura elétrica crítica, com 1.289 combinações de serviços e dados reais da State Grid Corporation of China (Resumo, p. 1; Seção 4, pp. 10–12).
- **Intervention:** MAS hierárquico no qual agentes inferiores analisam logs e métricas, enquanto um agente coordenador realiza fusão multimodal, decisão global de anomalia e raciocínio causal apoiado por LLM (Seções 3–4, pp. 4–10).
- **Comparison:** cinco métodos tradicionais ou de aprendizado são utilizados como baselines para detecção de anomalias e análise de desempenho (Seção 4, pp. 10–12).
- **Outcomes e Context:** o framework alcançou F1 máximo de 88,78%, precisão de 92,16% e recall de 85,63%, com melhoria de até 10,3% no F1 em quatro plataformas. O estudo também reporta melhor desempenho em anomalias compostas e RCA. O contexto é AIOps industrial de rede elétrica, embora a avaliação seja experimental sobre dados coletados (Resultados, pp. 12–16).

### P32 — *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems*

- **Population:** plataformas de negócio baseadas em microsserviços, com sinais multimodais de métricas, logs e traces conectados por dependências dinâmicas (Resumo e Introdução, pp. 1–3).
- **Intervention:** grafo multimodal de chamadas, GAT com atenção temporal, enriquecimento semântico de nós por LLM e agente RAG que recupera casos históricos e gera estratégias de recuperação verificadas contra playbooks (Seções 3–4, pp. 5–11).
- **Comparison:** GCN, GraphSAGE, DiagFusion, MicroRank, MicroEGRCL, PDiagnose e configurações zero-shot, few-shot e RAG são usados como baselines (Seção 5, pp. 12–16).
- **Outcomes e Context:** o MRR médio foi 0,931, contra 0,902 do baseline mais forte. A acurácia dos planos de recuperação com LLM e RAG foi 79,2% no SockShop, 75,8% no PowerGrid e 70,1% no CustomerService. A correção não foi executada em produção; o indicador mede aderência das estratégias aos playbooks de referência (Resultados, pp. 14–16; Conclusão, pp. 16–17).

### P33 — *A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense*

- **Population:** sistemas autônomos de defesa cibernética, infraestruturas críticas, desenvolvedores, profissionais e formuladores de políticas (Resumo, pp. 1–2; Introdução, pp. 3–4).
- **Intervention:** Agentic AI com arquiteturas cognitivas, reinforcement learning, agentes autônomos ou multiagentes, governança incorporada e mecanismos de defesa resilientes à computação quântica (Seções 3–6, pp. 7–17).
- **Comparison:** `N/A (revisão narrativa)`. O artigo contrapõe defesa reativa e estática a abordagens proativas, adaptativas e autônomas, sem um baseline experimental consolidado.
- **Outcomes e Context:** são sintetizados detecção de anomalias em tempo real, resposta preditiva, resiliência, autonomia e accountability, junto a riscos de uso dual, interoperabilidade de governança e segurança pós-quântica. Não há medição própria de MTTD ou MTTR. O contexto abrange cibersegurança convencional e pós-quântica (Discussão e conclusão, pp. 17–21).

### P34 — *Analysing the Role of LLMs in Cybersecurity Incident Management*

- **Population:** equipes e processos de resposta a incidentes cibernéticos, avaliados por dez cenários realistas que cobrem diferentes fases do gerenciamento de incidentes (Resumo e Introdução, pp. 1–2; Metodologia, pp. 4–7).
- **Intervention:** uso de GPT-3.5, GPT-4, GPT-4o e o1-preview com zero-shot, one-shot, few-shot e diferentes níveis de contexto, incluindo runbooks, para apoiar atividades do ciclo de resposta (Seções 3–4, pp. 4–7).
- **Comparison:** os modelos e configurações de contexto são comparados entre si; não há baseline humano nem processo não assistido por IA (Metodologia, pp. 5–7).
- **Outcomes e Context:** em 1.200 execuções, GPT-4o e GPT-3.5 apresentaram maior clareza, consistência e coerência para contenção, erradicação e recuperação, enquanto o1 e GPT-4 se destacaram em raciocínio e concisão para preparação, análise pós-incidente, vulnerabilidades e treinamento. O estudo não mede MTTD ou MTTR; avalia qualidade textual por métricas automáticas em ambiente controlado (Resultados, pp. 8–10; Conclusão, pp. 10–11).

### P35 — *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps*

- **Population:** sistemas complexos de microsserviços e fluxos de trabalho de SRE baseados em logs, métricas e traces (Resumo e Introdução, pp. 1–3).
- **Intervention:** grafo de fusão de anomalias, LLM como árbitro semântico e equipe formada por Navigator, Diagnoser e Verifier, que aplica validação adversarial e raciocínio contrafactual para reduzir alucinações (Seções 3–4, pp. 5–12).
- **Comparison:** métodos SOTA de RCA, abordagens unimodais, variantes apenas com LLM e estudos de ablação são utilizados como baselines (Seção 5, pp. 13–18).
- **Outcomes e Context:** o framework obteve F1 médio de 88,4% em cinco datasets, superando o melhor baseline em 4,6%. Os resultados mostram maior robustez multimodal e confiabilidade diagnóstica, mas não medem diretamente redução de MTTR em operação real. O contexto é AIOps e localização de falhas em microsserviços (Resumo, p. 1; Resultados e conclusão, pp. 13–18).

### P37 — *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response*

- **Population:** 194 profissionais de cibersegurança dos Estados Unidos e as práticas organizacionais baseadas em frameworks como NIST e SANS (Resumo, pp. 1–2; Metodologia, pp. 5–10).
- **Intervention:** adoção percebida de automação inteligente e Agentic AI na resposta a incidentes, acompanhada da modernização de frameworks para incorporar riscos, auditabilidade e decisões autônomas (Introdução, pp. 1–3).
- **Comparison:** ferramentas e playbooks estáticos atuais são contrastados com frameworks modulares e adaptativos; também são comparados diferentes níveis de delegação humana e autonomia (Questionário e resultados, pp. 8–21).
- **Outcomes e Context:** 84% declararam integração de Agentic AI, 92% perceberam redução significativa de MTTD e MTTR, 37% apoiaram triagem autônoma sem supervisão e apenas 13% confiaram em decisões totalmente autônomas. Além disso, 96% apoiaram revisão dos frameworks. Esses números são percepções autorrelatadas, não medições de telemetria operacional (Resultados, pp. 10–21; Discussão, pp. 22–26).

### P38 — *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation*

- **Population:** modelos open source locais, Mistral 7B, Llama 3.1 8B e Granite 3.2 8B, avaliados em 100 pares de perguntas e respostas do domínio agrícola (Resumo e Metodologia, pp. 1 e 5–14).
- **Intervention:** quatro estratégias de coordenação multiagente: colaborativa, sequencial, competitiva e hierárquica (Seções 2–3, pp. 3–10).
- **Comparison:** cada configuração multiagente é comparada diretamente a um baseline monoagente com RAG (Resumo, p. 1; Resultados, pp. 15–23).
- **Outcomes e Context:** todas as 28 configurações multiagentes degradaram entre 4,4% e 35,3% frente aos baselines. Llama 3.1 apresentou as menores perdas nas estratégias sequencial e hierárquica, 4,9% a 5,3%, enquanto Granite perdeu de 14% a 35%. O contexto é question answering local e restrito à agricultura, não resposta a incidentes, mas o estudo fornece evidência crítica sobre custo de coordenação (Discussão e conclusão, pp. 23–26).

### P39 — *Agentic AI and the Cyber Arms Race*

- **Population:** atacantes, defensores, Estados, atores não estatais e equipes de cibersegurança inseridos na dinâmica do ciberconflito (pp. 1–2).
- **Intervention:** arquitetura hierárquica com orquestrador baseado em reinforcement learning e agentes especializados em engenharia reversa, análise de logs e redes e descoberta de vulnerabilidades, com coevolução ofensiva e defensiva (pp. 2–3).
- **Comparison:** o texto contrapõe operações tradicionais dependentes de especialistas humanos e ML a operações agênticas escaláveis e adaptativas; não há avaliação experimental controlada (pp. 1–3).
- **Outcomes e Context:** são projetadas maior velocidade, autonomia, adaptação e democratização de capacidades ofensivas e defensivas, acompanhadas de riscos de robustez, ataques adversariais e instabilidade geopolítica. O artigo cita resultados externos, como 75% em benchmarks web, mas não mede MTTD ou MTTR. Trata-se de uma coluna conceitual sobre cyberwarfare (pp. 2–4).

### P40 — *A Comprehensive Survey on LLM-Based Network Management and Operations*

- **Population:** redes modernas heterogêneas, incluindo 5G/6G, NFV, SDN e nuvem, e seus operadores e administradores (Resumo e Introdução, pp. 1–3).
- **Intervention:** métodos baseados em LLMs para projeto, configuração, monitoramento, fault management, segurança e orquestração de redes, com linguagem natural, agentes, prompting, RAG e fine-tuning (Seções 2–5, pp. 4–45).
- **Comparison:** `N/A (survey)`. O artigo compara conceitualmente abordagens LLM com métodos manuais, baseados em regras e ML/DL, mas não executa benchmark próprio unificado.
- **Outcomes e Context:** a literatura revisada aponta interpretação de intenções, automação, redução de erros manuais, eficiência operacional, troubleshooting, RCA e recomendações de mitigação. Permanecem limitações de alucinação, latência, adaptação de domínio, segurança e privacidade. O contexto é gerenciamento e operação de redes, inclusive fault management e self-healing, sem MTTD/MTTR consolidados pelos autores (Seções de análise, pp. 15–45; Conclusão, p. 46).

## 2. Tabela PICOC consolidada

| ID | Artigo | Population | Intervention | Comparison | Outcomes | Context | Evidência (seção/pág.) |
|---|---|---|---|---|---|---|---|
| P01 | *Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment* | Sistemas de Agentic AI em ambientes dinâmicos e de alto risco; arquiteturas monoagente, multiagente, federadas e híbridas | Arquiteturas confiáveis, memória, raciocínio, planejamento, tool use, zero trust, governança, supervisão humana e observabilidade | Políticas estáticas e segurança convencional; comparação entre quatro tipos arquiteturais | Segurança, resiliência, accountability, transparência; detecção mais rápida e menor carga humana em caso reportado | Cibersegurança, infraestrutura crítica, indústria, governo, defesa e políticas públicas | Resumo, p. 1; Seção 1, pp. 3–4; Seção 4.5, p. 13; Seção 7.2, p. 27; Seção 9.8, p. 44; Conclusão, p. 45 |
| P02 | *The role of agentic AI in shaping a smart future: A systematic review* | Organizações e processos de negócio em múltiplos setores | Ferramentas agênticas, estruturas hierárquicas e transição Copilot → Autopilot | Copilot vs. Autopilot; Agentic AI vs. Generative AI vs. Autonomous AI | Produtividade, redução de custos, inovação, rapidez e menor supervisão; sem métricas de incident response | Adoção organizacional e estratégia GenAI em vários setores | Resumo, p. 1; Seção 5, pp. 6–8; Conclusão, p. 13 |
| P03 | *A Research Landscape of Agentic AI and Large Language Models: Applications, Challenges and Future Directions* | Aplicações de LLM e Agentic AI em seis domínios | Agentes com LLM, ferramentas, APIs, memória, coordenação e supervisão humana | GPT-4o vs. DeepSeek-R1 em demonstrações exploratórias; sem baseline central | Automação e decisão; em segurança, avaliação, priorização, contenção e remediação; riscos de opacidade e desalinhamento | Scoping review multissetorial, incluindo cibersegurança | Resumo, p. 1; cibersegurança, pp. 9–10; demonstrações, pp. 12–18; Conclusão, p. 25 |
| P04 | *LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead* | Tarefas do SDLC, QA, manutenção, debugging, fault localization e RCA | Sistemas multiagentes baseados em LLMs e agentes especializados; ChatDev | N/A (revisão de mapeamento e estudos de caso sem baseline controlado) | RCA e automação de SE; Snake funcional em 76 s/US$ 0,019; Tetris incompleto após dez tentativas | Engenharia e manutenção de software | Seção 3.3, p. 8; Seção 4, pp. 10–12; Conclusão, p. 22 |
| P05 | *A Survey of AIOps in the Era of Large Language Models* | Sistemas de software, operadores e dados de falha: logs, métricas, traces, séries e incident reports | LLM4AIOps para failure perception, RCA e assisted/auto remediation; prompting, RAG, fine-tuning e agentes | AIOps tradicional ML/DL vs. LLM4AIOps; modelos menores + especialistas como alternativa | Detecção, diagnóstico, RCA, relatórios, triagem, recomendação e execução; automação ponta a ponta ainda limitada | AIOps, on-call engineering, microsserviços, clusters e incident lifecycle | Resumo, p. 1; Seção 1.1, p. 3; Seções 3–6, pp. 8–23; Seção 7, pp. 24–26 |
| P06 | *Agentic AI: A Comprehensive Survey of Technologies, Applications, and Societal Implications* | Sistemas agênticos em robótica, saúde, veículos, trabalho, supply chain e segurança | Autonomia, memória, goals, adaptive reasoning, RL e multiagentes | Agentic AI vs. IA tradicional | Evidência secundária: -34,2% no tempo de tarefa, +7,7% na acurácia e +13,6% em recursos; menção a cyber threat response | Survey multissetorial e conceitual | Resumo, p. 1; Tabela 1 e resultados citados, p. 2; aplicações, p. 9; Conclusão, p. 11 |
| P07 | *Artificial Empathy: A New Perspective for Analyzing and Designing Multi-Agent Systems* | Agentes em MAS cooperativos/competitivos e jogos simulados | Modelo de empatia e Empathy-based Interactive Learner | EIL vs. Q-learning e multi-step; diferentes modos/temperaturas | Maior cooperação, altruísmo e justiça; variação de interesse próprio | Simulações de jogos; psicologia e economia comportamental | Resumo, p. 1; comparação, p. 11; Conclusão, p. 15 |
| P08 | *Applications, Challenges, and Future Directions of Human-in-the-Loop Learning* | Sistemas ML em saúde, finanças, educação, manufatura, robótica e Indústria 4.0 | HITL com active learning, iterative ML, RL e feedback humano | N/A (revisão); contraste conceitual com automação sem expertise humana | Acurácia, accountability, transparência, decisão e desempenho | Colaboração humano-máquina multissetorial | Resumo, p. 1; aplicações, pp. 4–16; Conclusão, p. 20 |
| P09 | *AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges* | AI Agents e Agentic AI em tarefas digitais e domínios complexos; inclui TI corporativa | Multiagentes, decomposição dinâmica, memória, ferramentas e orquestração | AI Agents vs. Agentic AI; fluxo agêntico vs. segurança baseada em regras | Menor latência decisória, menos falsos positivos, contenção proativa e respostas mais rápidas/precisas, sem valores | Taxonomia conceitual e cybersecurity incident response empresarial | Resumo, pp. 1–2; cenário de segurança, pp. 16–17; Conclusão, p. 25 |
| P10 | *Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey* | Sistemas autônomos orientados a objetivos complexos em ambientes variáveis | RL, goal-oriented architectures, adaptive control, planejamento, tool use e colaboração | Agentic AI vs. IA tradicional supervisionada e rígida | Produtividade, eficiência, adaptabilidade, escalabilidade, decisão e colaboração; sem MTTD/MTTR | Saúde, finanças, manufatura, software adaptativo e outros | Resumo, p. 1; Seções 2–6, pp. 3–10; métricas/casos, pp. 11–17; Conclusão, p. 22 |
| P11 | *Co-Evolving Multi-Agent Transfer Reinforcement Learning via Scenario Independent Representation* | Agentes MARL em SMAC/MP-SMAC | Co-MACTRL: coevolução, curriculum transfer learning e representação independente | MARL baseline, aprendizado do zero, oponentes estáticos e Co-MARL | Taxas de vitória, desempenho de aprendizagem, eficiência amostral, robustez e generalização | Simulação StarCraft II; não incidente de TI | Resumo, pp. 1–3; metodologia/resultados, pp. 8–11; conclusão, p. 12 |
| P12 | *Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey* | UAVs, veículos autônomos, robôs, edge devices e frotas | GANs, VAEs, Transformers e LLMs para segurança, anomalias, manutenção e resposta adaptativa | GenAI vs. AI/ML tradicional | Segurança, resiliência, autoconsciência, anomaly detection, predictive maintenance, fault management e eficiência | Sistemas autônomos, edge robotics e ameaças ciberfísicas | Resumo e contribuições, pp. 1–2; HMT, p. 13; Conclusão, p. 20 |
| P13 | *Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach* | Sistemas e decisões de varejo | RRE integrando TDD, LLM e Agentic AI | Especialistas humanos com mais de dez anos | 97,5% de similaridade; >90% de acurácia; accuracy/precision/recall/F1; 98,2% de filtragem | Experimento em desenvolvimento de sistemas de varejo | Resumo, p. 1; baseline, p. 10; resultados/conclusão, pp. 10–16 |
| P14 | *Transforming cybersecurity with agentic AI to combat emerging cyber threats* | SOCs, analistas, ativos e fluxos de incident response | Agentes especializados para detecção, triagem, decisão, contenção e remediação | Abordagens humanas/tradicionais e reativas vs. defesa autônoma/adaptativa | -90% no tempo de triagem; -30% no MTTR; contenção <5 min; velocidade, acurácia e menor carga | Cibersegurança e resposta a incidentes em SOC | Resumo, p. 1; tabela/casos, pp. 3–4; discussão, p. 7; Conclusão, p. 10 |
| P15 | *The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges* | Sistemas Agentic AI LLM e não LLM em vários domínios | Frameworks, LLM+RL, memória, reflexão, ferramentas e multiagentes | IA tradicional, generativa, autônoma e diferentes arquiteturas | Métricas qualitativas/quantitativas de performance e reliability; HITL, UAT, observabilidade e fault tolerance | Revisão de 143 estudos; incident response aparece como aplicação | Resumo, p. 1; arquiteturas, pp. 15–20; incident response, p. 32; testes, p. 35; Conclusão, p. 40 |
| P16 | *A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey* | Projetos de dados, sistemas de TI, telecom e ambientes industriais | MLOps/AIOps para monitoramento, anomalias, falhas, RCA, remediação e automação | MLOps vs. AIOps quanto a adoção, domínios e lifecycle | Predição/resolução de incidentes, RCA e remediação; automação ainda limitada | Indústria, academia, DevOps, ITSM, 5G e 6G | Resumo, p. 1; aplicações, pp. 19–21; Conclusão, p. 22 |
| P17 | *A Review of Trustworthy and Explainable Artificial Intelligence (XAI)* | IA em bancos, saúde, IoT e sistemas/veículos autônomos | TAI/XAI, transparência, explicações, robustez, privacidade, fairness e HITL/HOTL/HIC | IA confiável/explicável vs. black-box, enviesada e vulnerável | Confiabilidade, precisão consistente, interpretabilidade, segurança e accountability | Domínios de alto risco, com ênfase em veículos autônomos | Resumo, p. 1; princípios, pp. 3–4; XAI, pp. 9–14; Conclusão, p. 19 |
| P18 | *An architecture for model-based and intelligent automation in DevOps* | Sistemas complexos, pipelines DevOps e dez casos industriais | AIDOaRt: AI/ML + MDE + AIOps para monitoramento, RCA, predição e response/remediation automation | N/A (avaliação arquitetural sem baseline único) | Viabilidade, aplicabilidade, utilidade, integração e satisfação de requisitos; sem MTTD/MTTR | DevOps industrial, continuous engineering e 54 soluções | Resumo, pp. 1–2; arquitetura, pp. 4–7; avaliação, pp. 17–19; Conclusão, p. 19 |
| P19 | *Agent System Mining: Vision, Benefits, and Challenges* | Organizações como MAS, agentes e event logs de processos | ASM combinando Process Mining e Agent-Based Modeling | ASM vs. Process Mining tradicional e modelos “spaghetti” | Modelos compreensíveis, análise micro/macro e oportunidades de melhoria; sem métricas | BPM e order fulfillment com dados de eventos | Resumo, p. 1; exemplo, pp. 2–4; framework, pp. 6–10; Conclusão, p. 13 |
| P20 | *LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code* | Templates AWS CloudFormation e pipelines IaC/CI/CD | Workflow multiagente com LLM, RAG e base de conhecimento para detecção e remediação | Ferramentas estáticas como CDK-Nag e auditoria manual | 85% de detecção; 15% de falsos positivos; 5% de sobrecorreção; 80–100 s por template | Segurança preventiva de infraestrutura em nuvem antes do deploy | Resumo, p. 1; arquitetura, pp. 3–4; resultados, pp. 4–6; Conclusão, p. 7 |
| P21 | *Small Language Model Agent for the Operations of Continuously Updating ICT Systems* | Operações ICT e redes com procedimentos continuamente atualizados | SLM agent com nested thoughts, recuperação por blocos, reconfiguração de prompt e seleção de exemplos | Act, ReAct, RAP e resultados com GPT-3.5/GPT-4 | Até 96,3% no ALFWorld; 88,9% e 87,0% no WideEnet; adaptação de 29,4% para 78,8%; overhead computacional | Operação e configuração de redes, com dados sintéticos e reais | Resumo, p. 1; método, pp. 3–7; resultados, pp. 8–10 |
| P22 | *ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control* | Kubernetes cloud-edge/IoT com violações de SLA | Loop fechado LLM para RCA, mitigação via MCP e validação pós-ação | GPT-5 vs. GPT-5-mini | Agregado: 52,9% de identificação e 70,7% de mitigação; GPT-5: cerca de 78% e 80% | Benchmark com workloads IoT sintéticos e falhas injetadas | Resumo, p. 1; framework, pp. 3–6; resultados, pp. 7–9 |
| P23 | *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems* | Microsserviços cloud-native com métricas, logs, traces e dependências | Agente LLM com ferramentas de alinhamento multimodal, localização e classificação de falha | Eadro, HolisticRCA, baselines unimodais, LightGBM, ablações e LLM direto | Micro-F1 0,8831 no An; ganhos de até 19,85% em F1; inferência de 0,17 s/amostra | RCA fina em datasets de falhas cloud-native | Resumo, p. 1; método, pp. 3–7; avaliação, pp. 7–11 |
| P24 | *AgentAI: A Comprehensive Survey on Autonomous Agents in Distributed AI for Industry 4.0* | Agentes distribuídos na Indústria 4.0–6.0 | AgentAI com foundation models, memória, percepção, raciocínio e colaboração | N/A (estudo de mapeamento) | Eficiência, escalabilidade, robustez, produtividade e adaptabilidade; sem MTTD/MTTR próprios | Ambientes industriais multissetoriais | Resumo, p. 1; taxonomia, pp. 4–13; discussão, pp. 14–15 |
| P25 | *Artificial Intelligence Driven Multi-Agent Framework for Adaptive Cyber Attack Simulation and Automated Incident Response in Cyber Range Environments* | Cyber ranges, agentes atacantes/defensivos e datasets CICIDS2017 e UNSW-NB15 | MAS com RL, detecção de anomalias e resposta automatizada no CyDER 2.0 | Simulação estática ou baseada em regras | Cerca de 91% de desempenho de detecção; 5,3 s de resposta; mais de 25 agentes | Cyber range controlado para treinamento e validação de IR | Resumo, p. 1; implementação, pp. 8–12; resultados, pp. 13–18 |
| P26 | *Surveying Root Cause Analysis Techniques: A Comprehensive Review of Aspects for Multi-Service Applications* | Cloud, microsserviços e sistemas industriais; logs, traces, métricas e relatórios | Taxonomia de RCA estatística, ML/DL, grafos, causalidade, híbridos e LLMs | N/A (estudo de mapeamento) | Consolida acurácia, precisão, recall, F1, Top-k e tempo de diagnóstico; sem resultado próprio | Operação e manutenção de aplicações multisserviço | Resumo, p. 1; técnicas, pp. 3–12; métricas, pp. 13–16 |
| P27 | *Leveraging Multi-Agent Framework for Root Cause Analysis* | Plataformas cloud-native e medição distribuída de energia | MA-RCA com agentes de análise, RAG, validação dinâmica e relatório | CoT, RAG, RCACOPILOT, RCAgent, mABC e variantes mono/multiagente | F1 0,952 no Nezha e 0,828 em energia; menor alucinação e erro propagado | RCA automatizada em dados operacionais de dois domínios | Resumo, pp. 1–2; método, pp. 3–7; resultados, pp. 8–11 |
| P28 | *A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models* | E-mails, logs, IPs e analistas diante de ataques multivetor | Agentes especializados e recomendador contextual com LLM | SIEM/regra e pipelines isolados ou monoagentes | 93,6% de detecção; 87% de correlação; F1 0,94; −41,3% falsos positivos; −38,5% triagem | Datasets públicos e ambiente SOC simulado | Resumo, p. 1; arquitetura, pp. 4–11; resultados, pp. 11–14 |
| P29 | *AIOps for Log Anomaly Detection in the Era of LLMs: A Systematic Literature Review* | Sistemas de TI e equipes AIOps que analisam logs | LLMs com prompting, RAG e fine-tuning para detecção de anomalias | ML/DL e métodos tradicionais vs. LLMs | Evidência revisada de ganhos em F1, precisão, recall, interpretabilidade e adaptação; sem MTTD/MTTR próprio | AIOps e log anomaly detection | Resumo, pp. 1–2; método, pp. 3–5; síntese, pp. 6–14 |
| P30 | *Reliability of LLM Inference Engines from a Static Perspective: Root Cause Analysis and Repair Suggestion via Natural Language Reports* | Issues de defeitos em vLLM e TensorRT-LLM | RCA textual estática, localização de módulo e sugestões de reparo por LLM | SVM, Random Forest, baselines aleatório/frequente e cross-engine | Acurácia 0,688; macro-F1 0,421; Top-1 0,705; Top-2 0,841; avaliação humana positiva | Debugging estático de infraestrutura de inferência LLM | Resumo, pp. 1–2; método, pp. 5–10; resultados, pp. 11–16 |
| P31 | *LEMAD: LLM-Empowered Multi-Agent System for Anomaly Detection in Power Grid Services* | Serviços cloud-native da rede elétrica e 1.289 combinações de serviços | MAS hierárquico para logs, métricas, fusão multimodal e RCA | Cinco métodos baseline | F1 até 88,78%; precisão 92,16%; recall 85,63%; ganho de até 10,3% | AIOps industrial em infraestrutura elétrica crítica | Resumo, p. 1; framework, pp. 4–10; resultados, pp. 10–16 |
| P32 | *GALR: Graph-Based Root Cause Localization and LLM-Assisted Recovery for Microservice Systems* | Microsserviços com métricas, logs, traces e dependências | Grafo multimodal, GAT, enriquecimento LLM e agente RAG de recuperação | GCN, GraphSAGE, DiagFusion, MicroRank, MicroEGRCL, PDiagnose e variantes de prompting | MRR médio 0,931; planos de recuperação com 70,1%–79,2% de acurácia | Datasets e falhas injetadas; recuperação avaliada offline | Resumo, pp. 1–2; método, pp. 5–11; resultados, pp. 12–17 |
| P33 | *A Review of Agentic AI in Cybersecurity: Cognitive Autonomy, Ethical Governance, and Quantum-Resilient Defense* | Defesa cibernética, infraestrutura crítica e stakeholders de governança | Agentic AI cognitiva, RL, MAS, governança incorporada e defesa pós-quântica | N/A (revisão narrativa) | Detecção em tempo real, resposta preditiva, resiliência e accountability; sem métricas próprias | Cibersegurança convencional e pós-quântica | Resumo, pp. 1–2; método, pp. 7–9; síntese, pp. 12–21 |
| P34 | *Analysing the Role of LLMs in Cybersecurity Incident Management* | Equipes e processos de IR em dez cenários | GPT-3.5, GPT-4, GPT-4o e o1 com diferentes estratégias e contextos | Comparação entre modelos e níveis de contexto; sem baseline humano | 1.200 execuções; diferenças de clareza, coerência, relevância e raciocínio por fase; sem MTTD/MTTR | Experimento controlado de gerenciamento de incidentes | Resumo, p. 1; metodologia, pp. 4–7; resultados, pp. 8–11 |
| P35 | *Graph-Augmented Multi-Agent Robust Root Cause Analysis in AIOps* | Microsserviços e workflows SRE com observabilidade multimodal | Grafo de anomalias e agentes Navigator, Diagnoser e Verifier com validação adversarial | Métodos SOTA, abordagens unimodais, LLM-only e ablações | F1 médio 88,4%, 4,6% acima do melhor baseline; maior robustez | AIOps/SRE em cinco datasets | Resumo, p. 1; método, pp. 5–12; avaliação, pp. 13–18 |
| P37 | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | 194 profissionais de cibersegurança dos EUA | Automação e Agentic AI em IR; modernização de NIST/SANS | Frameworks/playbooks estáticos vs. modelos adaptativos; níveis de autonomia | 84% adotam; 92% percebem redução de MTTD/MTTR; 13% confiam em autonomia plena; 96% pedem revisão | Survey de percepções profissionais, não telemetria operacional | Resumo, pp. 1–2; método, pp. 5–10; resultados, pp. 10–26 |
| P38 | *Multi-Agent Coordination Strategies vs. Retrieval-Augmented Generation in LLMs: A Comparative Evaluation* | Três LLMs locais e 100 perguntas agrícolas | Coordenação colaborativa, sequencial, competitiva e hierárquica | Baseline monoagente com RAG | Todas as 28 configurações degradaram de 4,4% a 35,3%; overhead de coordenação | QA agrícola local, fora de incident response | Resumo, p. 1; método, pp. 5–14; resultados, pp. 15–26 |
| P39 | *Agentic AI and the Cyber Arms Race* | Atacantes, defensores, Estados e equipes de segurança | Orquestrador RL e agentes especializados ofensivos/defensivos | Operações humanas/ML tradicionais vs. automação agêntica | Velocidade, escala e adaptação projetadas; riscos adversariais e geopolíticos; sem métricas próprias | Cyberwarfare e análise conceitual | pp. 1–4 |
| P40 | *A Comprehensive Survey on LLM-Based Network Management and Operations* | Redes 5G/6G, NFV, SDN, nuvem e seus operadores | LLMs/agentes para configuração, monitoramento, fault management, segurança e orquestração | N/A (survey); contraste com manual, regras e ML/DL | Automação, menos erros, troubleshooting, RCA e mitigação; desafios de alucinação, latência e privacidade | Gerenciamento e operação de redes, inclusive self-healing | Resumo, pp. 1–3; taxonomia e análise, pp. 4–45; Conclusão, p. 46 |

## 3. Síntese transversal

A **Population** do corpus consolidado desloca-se de uma base ampla de sistemas autônomos, multiagentes e aplicações industriais para um núcleo mais específico de microsserviços, plataformas cloud-native, redes, SOCs e equipes de SRE ou AIOps. A **Intervention** predominante combina LLMs, RAG, uso de ferramentas, agentes especializados e orquestração multiagente. Nos estudos P20–P40, cresce o uso de logs, métricas e traces em pipelines que conectam detecção, RCA, recomendação de correção e, em poucos casos, execução e validação da remediação.

A dimensão **Comparison** torna-se mais robusta na segunda leva. P20, P21, P22, P23, P25, P27, P28, P30, P31, P32, P35 e P38 usam baselines técnicos ou ablações. As revisões e surveys continuam apresentando comparação conceitual ou `N/A`, o que impede uma síntese quantitativa única. P38 oferece ainda uma evidência negativa importante: coordenação multiagente pode degradar o desempenho quando o problema não exige decomposição e o custo de coordenação supera seus benefícios.

Os **Outcomes** mais frequentes passam a incluir acurácia, F1, Top-k, MRR, falsos positivos, latência de diagnóstico, tempo de triagem e sucesso de mitigação. Mesmo assim, MTTD e MTTR permanecem pouco medidos diretamente: P14 reúne valores industriais secundários, enquanto P37 registra a percepção de profissionais, não telemetria real. Observabilidade aparece principalmente como fonte de dados para RCA, e não como variável de resultado. Carga cognitiva ou esforço mental da equipe quase nunca é operacionalizado por instrumento validado.

O **Context** combina benchmarks, fault injection, cyber ranges, datasets públicos, dados industriais históricos e estudos conceituais. P22 aproxima-se de um loop fechado com validação após a ação, mas em ambiente experimental. P32 avalia planos de recuperação contra playbooks sem executá-los em produção. Portanto, o corpus sustenta com mais força a eficácia diagnóstica de agentes do que a redução comprovada de tempo de recuperação e risco operacional em ambientes produtivos.

## 4. Observações metodológicas

1. **Cobertura do corpus:** foram analisados 39 estudos, P01–P35 e P37–P40. O P36 não foi fornecido e não deve ser considerado excluído por critério metodológico; ele está apenas ausente do material recebido.
2. **Heterogeneidade dos desenhos:** o corpus reúne surveys, revisões sistemáticas ou narrativas, estudos arquiteturais, benchmarks, experimentos com fault injection, cyber ranges e pesquisa de percepção. Resultados desses desenhos não devem ser agregados como se possuíssem o mesmo nível de evidência.
3. **Predomínio de métricas substitutas:** F1, acurácia, Top-k, MRR, latência de inferência e aderência a playbooks são úteis, mas não equivalem automaticamente a MTTD, MTTR, disponibilidade ou impacto no negócio.
4. **MTTD e MTTR:** P37 informa percepção de redução entre profissionais; P14 consolida números de casos industriais citados. A maior parte dos estudos primários não mede esses indicadores em uma janela operacional real.
5. **Remediação recomendada versus executada:** P20, P23, P30, P32 e P34 geram correções, estratégias ou respostas, mas não demonstram necessariamente execução segura. P22 executa ações e valida estabilidade em benchmark, sendo uma evidência mais próxima de *closed-loop remediation*.
6. **Observabilidade:** logs, métricas e traces são centrais em P05, P23, P26, P27, P31, P32, P35 e P40. Contudo, a observabilidade é tratada como entrada do diagnóstico, não como outcome mensurado por cobertura, qualidade do sinal ou redução de pontos cegos.
7. **Carga cognitiva:** reduções de trabalho, triagem ou intervenção humana aparecem em P01, P02, P08, P09, P14 e P28, mas faltam escalas validadas, desenho longitudinal e comparação com equipes sem copiloto. Assim, não é seguro concluir redução de carga cognitiva para o conjunto.
8. **Produção versus simulação:** vários resultados derivam de datasets públicos, falhas injetadas, ambientes sintéticos ou cyber ranges. A validade externa para produção deve ser discutida separadamente, sobretudo quando agentes executam mudanças em infraestrutura.
9. **Autonomia e confiança:** P37 evidencia um contraste relevante: ampla percepção de benefício, mas baixa confiança em autonomia total. Esse achado reforça a necessidade de HITL/HOTL, auditabilidade e controles de autorização para ações irreversíveis.
10. **Coordenação multiagente não é benefício automático:** P38 mostra degradação de 4,4% a 35,3% em todas as configurações avaliadas. A escolha entre monoagente, RAG e MAS deve depender da decomposição real da tarefa, diversidade de papéis e custo de coordenação.
11. **Maturidade editorial:** o status de revisão por pares varia entre os artigos. O P01 declara aguardar peer review na versão analisada; essa condição deve integrar uma avaliação separada de qualidade metodológica.
