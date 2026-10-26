# Avaliação Sistemática de Estudo Primário — RSL (Kitchenham et al., 2009 / DARE)

## Identificação do Estudo
- **ID do Artigo:** P39
- **Arquivo PDF Avaliado:** [P39-A3-Agentic_AI_and_the_Cyber_Arms_Race.pdf](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/P39-A3-Agentic_AI_and_the_Cyber_Arms_Race.pdf)
- **Prompt de Referência:** [prompt-P39.md](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/prompt-P39.md)
- **Título:** *Agentic AI and the Cyber Arms Race*
- **Autores:** Sean Oesch; Jack Hutchins; Phillipe Austria; Amul Chaulagain (Oak Ridge National Laboratory — ORNL, Oak Ridge, TN 37830, USA)
- **Periódico / Fonte:** *Computer* (IEEE Computer Society, coluna *Cybertrust*), Vol. 58, No. 5, pp. 82–85, Maio de 2025
- **DOI:** `10.1109/MC.2025.3544116`

---

## Etapa 0 — Extração Bibliométrica e Escopo

- **Metadados verificados no PDF:** Artigo curto de coluna técnica/científica (*Cybertrust*, editada por James Bret Michael) publicado na revista *Computer* (IEEE Computer Society), Maio de 2025, pp. 82–85 (versão de 28 de abril de 2025, p. 82/p. 1 do PDF).
- **Métricas externas (`[VERIFICAR]`):**
  - **Citações:** `[VERIFICAR]` (não consta no PDF; verificar no *Scopus*, *IEEE Xplore* ou *Google Scholar*).
  - **SJR / Quartil:** Informado como `Q1` no input do protocolo (`[VERIFICAR]` no *Scimago Journal Rank* para *Computer*, ISSN 0018-9162).
  - **Qualis CAPES:** Informado como `A3` no input do protocolo (`[VERIFICAR]` na *Plataforma Sucupira / Qualis Periódicos* na área de Ciência da Computação).
- **Adequação ao Escopo Temático da RSL:** **Tematicamente aderente, porém em formato de artigo curto de opinião/perspectiva (4 páginas)**. Discute o impacto da IA Agêntica ofensiva e defensiva no equilíbrio de poder da guerra cibernética (*cyberwarfare*), coevolução entre agentes *Red* e *Blue* e implicações geopolíticas.

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério PRISMA | Status | Evidência no Texto / Justificativa |
| :--- | :---: | :--- |
| **1. Publicação entre 2020 e 2026** | **Atende** | Publicado em maio de 2025 (*Computer*, pp. 82–85). |
| **2. Qualis A1–A2** | **`[VERIFICAR]` (Alerta: `A3` no input)** | O metadado do protocolo indica `Qualis: A3`, abaixo do limiar estrito `A1–A2` (requer verificação externa na Plataforma Sucupira). |
| **3. Escopo: IA Agêntica em redes, segurança ou operações de TI** | **Atende** | Aborda diretamente IA Agêntica aplicada a operações cibernéticas ofensivas e defensivas (pp. 82–85). |
| **4. Texto completo disponível e acessível** | **Atende** | Texto integral de 4 páginas (pp. 82–85) disponível e analisado via PDF. |
| **5. Sem critérios de exclusão (não é apenas ML clássico, IoT puro, resumo ou duplicata)** | **Atende Parcialmente (Coluna de 4 páginas)** | Trata-se de um artigo curto de coluna (*Cybertrust*, 4 páginas e 9 referências) de caráter predominantemente ensaístico/conceitual e geopolítico, sem metodologia experimental detalhada. |

**Status da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (COM ALERTA DE EXCLUSÃO POR QUALIS A3 E RIGOR METODOLÓGICO DARE)** — Em cumprimento à instrução de gerar o parecer completo para todos os arquivos do lote, realiza-se abaixo a extração integral das Tabelas A, B e C, recomendando-se a exclusão fundamentada no parecer final.

---

## Tabela A — Extração Bibliométrica (Tabela 3 do Protocolo)

| ID | Autores | Título | Ano | Fonte | Qualis | SJR | Citações | Escopo_Resumo |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **P39** | Oesch, S.; Hutchins, J.; Austria, P.; Chaulagain, A. | *Agentic AI and the Cyber Arms Race* | 2025 | *Computer* (IEEE Computer Society, Vol. 58, No. 5, pp. 82–85) | A3 `[VERIFICAR]` | Q1 `[VERIFICAR]` | `[VERIFICAR]` | Artigo de perspectiva na coluna *Cybertrust* que analisa como arquiteturas hierárquicas de IA agêntica (combinando RL e LLMs especializados) alteram o equilíbrio ofensivo-defensivo na guerra cibernética, ilustrando a coevolução entre agentes *Red* e *Blue* no ambiente *Cyberwheel* do ORNL e discutindo riscos de IA adversarial e proliferação geopolítica. |

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5 do Protocolo)

| Questão de Pesquisa (RQ) | Classificação | Pontuação | Evidências e Justificativa Detalhada (com páginas, seções, tabelas e figuras) |
| :--- | :---: | :---: | :--- |
| **RQ1 (Adaptação e autonomia de modelos fundacionais como agentes para gestão de redes/TI)** | **P** | **0.5** | **Conceitualização de agentes hierárquicos em cibersegurança, sem detalhamento técnico.** Propõe o conceito de um *Centralized Reinforcement Learning Agent (CARL)* (p. 83/p. 2 do PDF) coordenando quatro agentes especializados: (1) modelo de engenharia reversa para manipulação de código binário; (2) agente de análise e inferência sobre logs; (3) agente de rede para mapeamento e travessia de topologias; e (4) agente descobridor de vulnerabilidades e identificação de TTPs. Cita agentes comerciais existentes (*Microsoft Security Copilot*, *CrewAI*, *XBOW* — capaz de explorar `75%` de benchmarks de segurança web e descobrir bypass de autenticação no Scoold —, *RunSybil* e *Dropzone AI* para triagem de alertas Tier 1 em SOC, pp. 82–83) e ilustra a coevolução de agentes *Red/Blue* baseados em RL no ambiente *Cyberwheel* (Figura 1, p. 84). |
| **RQ2 (Arquiteturas, padrões de design e integração com infraestrutura de TI)** | **P** | **0.5** | **Menção superficial a padrões de orquestração.** Descreve em nível conceitual o padrão hierárquico *manager-worker* (*CARL* delegando subtarefas a subagentes que interagem com bibliotecas e ferramentas existentes, p. 83) e menciona a plataforma *CrewAI* e o ambiente de simulação *Cyberwheel* no GitHub do ORNL (Figura 1, p. 84), mas não apresenta diagramas de arquitetura, protocolos de comunicação ou especificações de integração. |
| **RQ3 (Cenários de avaliação, métricas de desempenho e eficácia)** | **P** | **0.5** | **Evidência empírica mínima e apenas ilustrativa.** Apresenta um único gráfico (Figura 1, p. 84) de retorno episódico (*Episodic Return*, de `0` a `2.000`) ao longo de `17.500` episódios de treinamento no ambiente *Cyberwheel*, mostrando cinco rodadas alternadas de retreinamento coevolutivo entre um *Red Agent* e um *Blue Agent*, além de citar o número externo da ferramenta *XBOW* (`75%` em benchmarks web, p. 83). Não descreve a configuração experimental, espaço de estados/ações, hiperparâmetros ou baselines comparativos. |
| **RQ4 (Desafios de segurança, confiabilidade, alucinação, guarda-corpos e limitações)** | **P** | **0.5** | **Foco em riscos estratégicos, IA adversarial e geopolítica.** Destaca: (1) vulnerabilidade de agentes de IA a ataques de *Adversarial AI* e *prompt injection* defensivo (citando Pasquini et al. [7], *"Hacking back the AI-hacker"*, onde defensores detectam que o invasor é um agente LLM e alteram a resposta do sistema para fazê-lo falhar, p. 83); (2) assimetria de custos entre defesa e ataques automatizados gerados em horas, minutos ou segundos, expondo organizações com poucos recursos (p. 83); e (3) proliferação horizontal/vertical de capacidades cibernéticas autônomas para atores estatais menores e não estatais, opacidade de atribuição e ausência de mecanismos de verificação ou tratados análogos aos da Guerra Fria (pp. 84–85). Não avalia tecnicamente mecanismos de *guardrails* ou alucinação. |
| **RQ5 (Tendências futuras e direções de pesquisa abertas)** | **P** | **0.5** | **Aponta desafios abertos em alto nível.** Indica a necessidade futura de garantir a robustez dos agentes contra IA adversarial (p. 83), desenvolver defesas adaptativas coevolutivas e lidar com a imprevisibilidade geopolítica, falta de transparência e ausência de *accountability* em operações cibernéticas autônomas (pp. 84–85), sem estruturar uma agenda técnica de pesquisa. |
| **Pontuação Total (`SCORE_RQ`)** | — | **2.5 / 5.0** | **Média de aderência às RQs: 50,0% (0 T, 5 Ps, 0 N).** |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 do Protocolo)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências do Artigo |
| :--- | :---: | :---: | :--- |
| **QA1 (Clareza e explicitação dos objetivos e questões da pesquisa)** | **P** | **0.5** | O sumário inicial (p. 82) explicita o propósito de examinar as implicações da IA agêntica para a guerra cibernética e a política global, mas não formula questões de pesquisa estruturadas nem objetivos técnicos verificáveis. |
| **QA2 (Descrição adequada do método, arquitetura e reprodutibilidade)** | **N** | **0.0** | Por ser um artigo curto de coluna (*Cybertrust*, 4 páginas), não possui seção de metodologia. A arquitetura *CARL* é apresentada apenas como exercício imaginativo (*"Imagine a centralized reinforcement learning agent..."*, p. 83), e o experimento da Figura 1 (p. 84) não detalha algoritmos de RL, funções de recompensa, topologia de rede simulada ou parâmetros de treinamento (remetendo apenas aos artigos anteriores [5, 6] dos autores). |
| **QA3 (Suficiência da validação empírica, cenários e métricas)** | **N** | **0.0** | Não há validação empírica sistemática: o único resultado próprio é o gráfico ilustrativo de retorno episódico na Figura 1 (p. 84), sem tabelas quantitativas, métricas de eficácia operacional, análise estatística ou comparação com baselines. |
| **QA4 (Consistência entre resultados obtidos e conclusões reportadas)** | **P** | **0.5** | As reflexões estratégicas e geopolíticas (pp. 83–85) são bem argumentadas e apoiadas em paralelos históricos da corrida nuclear [1, 2, 8], mas extrapolam amplamente a evidência empírica contida no próprio texto. |
| **Pontuação Total (`SCORE_QA`)** | **Banda Baixa** | **1.0 / 4.0** | **Qualidade metodológica Baixa (`SCORE_QA = 1.0`, faixa $< 2.0$).** |

---

## Parecer Final do Revisor

### Síntese Crítica (3–5 linhas)
O artigo **P39** é um texto curto de coluna (*Cybertrust*, 4 páginas) publicado na *IEEE Computer* por pesquisadores do *Oak Ridge National Laboratory* (ORNL), dedicado a discutir as implicações estratégicas e geopolíticas da IA Agêntica na corrida armamentista cibernética. Embora apresente ideias relevantes — como a arquitetura conceitual hierárquica *CARL*, o gráfico ilustrativo de coevolução *Red vs. Blue* em Aprendizado por Reforço no ambiente *Cyberwheel* (Figura 1, p. 84) e o alerta sobre vulnerabilidades de agentes LLM a *prompt injection* defensivo (*"Hacking back the AI-hacker"*) —, o trabalho carece de metodologia científica, detalhamento arquitetural e validação experimental rigorosa. Como consequência, atinge pontuação metodológica insuficiente (`SCORE_QA = 1.0/4.0`, Banda Baixa), somada à indicação de `Qualis A3` nos metadados do protocolo.

### Recomendação Final
- **Decisão:** **EXCLUIR**
- **Justificativa:** O artigo enquadra-se na **Banda Baixa** de qualidade metodológica DARE (`SCORE_QA = 1.0/4.0 < 2.0`), tratando-se de um ensaio curto de coluna (4 páginas) sem descrição metodológica (`QA2 = 0.0`) ou validação empírica suficiente (`QA3 = 0.0`), além de apresentar indicativo de `Qualis A3` (abaixo do critério `A1–A2` da Etapa 1). Pode ser citado apenas na Introdução/Motivação da RSL para contextualizar a corrida armamentista entre agentes ofensivos e defensivos, mas não deve compor a amostra de estudos primários sintetizados.

### Pendências de Verificação Externa (`[VERIFICAR]`)
1. **Qualis CAPES:** Verificar na *Plataforma Sucupira (Qualis Periódicos)* a classificação vigente da revista *Computer* (IEEE Computer Society, ISSN 0018-9162), indicada como `A3` no prompt.
2. **SJR / Quartil:** Confirmar o quartil `Q1` e o índice SJR no portal *Scimago Journal Rank*.
3. **Citações:** Verificar o número atual de citações (`DOI: 10.1109/MC.2025.3544116`) no *Scopus* ou *Google Scholar*.
