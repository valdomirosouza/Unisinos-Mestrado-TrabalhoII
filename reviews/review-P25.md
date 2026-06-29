# Avaliação RSL — Estudo P25

**Artigo:** _Artificial intelligence driven multi-agent framework for adaptive cyber attack simulation and automated incident response in cyber range environments_ — A. Agrawal, M. Nadeem, A. Al Nuaim, A. Al Nuaim
**Arquivo:** P25-A1-s41598-026-45937-9.pdf (20 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                        | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                                   | DOI                        |
| --- | -------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------- |
| P25 | Scientific Reports (Nature) (16:11673) | 2026 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa empírico (MAS/RL, cyber range, datasets reais, testes estatísticos) | 10.1038/s41598-026-45937-9 |

_Evidências: cabeçalho/rodapé (DOI; "Scientific Reports (2026) 16:11673"; recebido 09/01/2026, aceito 23/03/2026); "Data availability: supplementary information files". Citações/SJR/Qualis não constam no PDF._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                           | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                                                   | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --- | -------------------------------- | ---------------------------- | ----------------------- | ------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P25 | AI-Driven MAS (cyber range / IR) | RQ1 Context Definitions      | Respondida Plenamente   | **T**         | "Model development", "MAS architecture", "Attacker agent model" (p.8-13) | Autonomia operacional explícita (agentes atacante RL/DQN e defensor ML auto-aprendizes) (a); características — planejamento multi-estágio via RL, aprendizado, comunicação FIPA/ACL, supervisão humana (alertas, teste de aceitação por especialistas) (b); modelo decisório **formal** — MDP (S,A,P,R,γ) + DQN + função de recompensa (c). Ressalva: autonomia em sentido **MAS/RL**, não LLM-agêntica.                                                                    |
| P25 | "                                | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | "Research methodology", "Model implementation" (p.7-12), Figs. 5-7       | Arquitetura MAS atacante/defensor integrada ao cyber range, distribuída/assíncrona (a); stack muito detalhado — DQN/Policy Gradient, Random Forest/Autoencoder/ensemble, Python, TF/PyTorch, ZeroMQ+JSON, Docker, FIPA-ACL, APIs CyDER 2.0 (b); capacidades avançadas — ataque adaptativo multi-estágio, detecção de anomalia, IR automatizada (lib. NIST SP 800-61), coordenação multiagente (c).                                                                          |
| P25 | "                                | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | "Experimental results", Tabs. 6-15 (p.14-18)                             | Quantitativo robusto e **IR-específico**: F1 detecção 94,5%/89,9%/87,9% por porte de rede; latência de resposta 4,2-6,1s (vs 6,5-9,5 rule-based, 12,1-18,4 estático); +25% F1 e −35% latência vs estático; complexity score; uso de recursos; significância estatística (t-tests, ANOVA, p<0,05) (b); benefícios qualitativos (realismo, escalabilidade) (a); evidência forte — datasets reais, baselines, validação cruzada, aceitação por especialistas, stress test (c). |
| P25 | "                                | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | "Literature review", "Conclusion" (p.2-3, 18)                            | Desafios técnicos cobertos — escassez de dados rotulados, tuning de RL, escalabilidade, restrições de borda (computação/armazenamento) (a). Governança parcial via alinhamento a NIST SP 800-61 e alertas humano-no-loop (c). Porém **sem discussão ética** — notável dado o caráter **dual-use ofensivo** (agente atacante RL) (b ausente).                                                                                                                                |
| P25 | "                                | RQ5 Research Gaps            | Respondida Plenamente   | **T**         | "Literature review", "Conclusion" (p.2-3, 18)                            | Lacunas do estado da arte bem articuladas (falta de integração a cyber range, validação com dados reais, escalabilidade) e direções concretas: compressão de modelos, inferência leve, arquiteturas híbridas edge-cloud.                                                                                                                                                                                                                                                    |
|     |                                  | **SCORE_RQ**                 |                         | **4.5 / 5.0** |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                    | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P25 | Artigo de pesquisa empírico (MAS/RL, cyber range) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **4.0 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — problema (cyber ranges rule-based sem adaptatividade; lacuna de MAS-IA validada com dados reais) e solução (AI-driven MAS p/ simulação adaptativa + IR automatizada) explícitos, com **hipóteses formais**.
- **QA2 = Y** — formulação MDP, hiperparâmetros DQN completos (camadas 128/64/32, lr 0,001, γ 0,95, ε-decay, replay 100k, batch 64), datasets públicos (CICIDS2017, UNSW-NB15), pré-processamento (SMOTE, split 80/20), ferramentas (ZeroMQ, Docker, FIPA, CyDER 2.0). Alta replicabilidade.
- **QA3 = Y** — validação empírica rigorosa: datasets reais, baselines (estático, rule-based MAS), 3 portes de rede, validação cruzada 10-fold, aceitação por especialistas, stress/scaling tests e **significância estatística**.
- **QA4 = Y** — conclusões decorrem dos resultados; limitações discutidas (implantação em borda, restrição de recursos) com direções de mitigação.

## Parecer final do revisor

**Síntese.** Artigo empírico **forte e diretamente no escopo de Resposta a Incidentes**: um Sistema Multi-Agente dirigido por IA que simula ciberataques adaptativos (atacante RL/DQN) e executa **incident response automatizado** (defensor ML + biblioteca de ações alinhada a NIST SP 800-61) em um cyber range (CyDER 2.0), validado com datasets reais (CICIDS2017, UNSW-NB15) e testes estatísticos. Aderência alta a **RQ1-RQ3 e RQ5**; **RQ4 parcial** (desafios técnicos e alinhamento a NIST presentes, mas **sem discussão ética**, o que é relevante dado o componente ofensivo dual-use).

**Recomendação: INCLUIR.** SCORE_RQ 4,5/5,0 e QA 4,0/4,0 (Banda Alta). É o estudo **mais alinhado ao domínio de IR/cibersegurança** do lote até agora, com IR automatizado explícito e evidência empírica robusta.

> ⚠️ **Ressalva de escopo conceitual (importante para a síntese):** diferentemente de P20-P23, os "agentes" aqui são **RL/ML (DQN, Random Forest, Autoencoder)** e o IR é **baseado em regras** — não há LLM nem agente de modelo-fundacional. Trata-se de "agêntico" no sentido **MAS/autonomia RL**, não no sentido **LLM-agêntico/copilot** que caracteriza a maioria dos demais estudos. Recomendo registrar essa distinção de paradigma no mapeamento (eixo "tipo de agente"), pois afeta a comparabilidade com os estudos de copilot LLM.

_Observações menores de qualidade:_ redação com diversos problemas gramaticais (não compromete o conteúdo); a referência [1] citada (deep learning para "polar ring galaxies") aparenta ser citação espúria/desalinhada — sinalizar na extração bibliométrica.

**Pendências de verificação externa:**

- **Citações** ≥ 1 → Scopus / Google Scholar (artigo muito recente, 2026 — possível baixa contagem).
- **SJR (quartil)** → Scimago, _Scientific Reports_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios verificáveis no PDF atendidos (Ano 2026 ✓; veículo Scientific Reports ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
