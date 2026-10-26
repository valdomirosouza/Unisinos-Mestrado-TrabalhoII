# Avaliação RSL: Ciclo 2 — Estudo P63

**Artigo:** The Chatbot Usability Scale: the Design and Pilot of a Usability Scale for Interaction with AI-Based Conversational Agents  
**Autores:** Simone Borsci, Alessio Malizia, Martin Schmettow, Frank van der Velde, Gunay Tariverdiyeva, Divyaa Balaji, Alan Chamberlain  
**Periódico:** *Personal and Ubiquitous Computing* (Springer), Vol. 26, pp. 95–119, 2022  
**DOI:** `10.1007/s00779-021-01582-9`  
**RSL Alvo:** "Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura" (PPGCA Unisinos)

---

## 1. Contexto e Parâmetros de Entrada (Prompt)

- **Papel:** Pesquisador em Computação Aplicada do PPGCA da Unisinos, orientado por Doutor em Ciência da Computação, especialista em RSL em Engenharia de Software segundo Kitchenham (2009) e critérios DARE (QA1–QA4).
- **ID atribuído:** P63
- **Qualis declarado:** A1 (derivado do percentil Scopus 92.0%, regra CAPES 2025–2028)
- **SJR Quartil declarado:** Q2
- **Ressalvas de triagem prévia:** Aprovado na triagem; instrumento HCI de avaliação de conversational agents, não sistema; domínio geral.

---

## 2. Extração Bibliométrica e Triagem

### 2.1 Extração Bibliométrica
- **ID:** P63
- **Periódico/Conferência:** Personal and Ubiquitous Computing (Springer)
- **Ano:** 2022 (Online em 2021)
- **Tipo de Estudo:** Empírico / Validação Psicométrica de Instrumento de Medição
- **DOI:** `10.1007/s00779-021-01582-9`
- **Citações:** `[VERIFICAR]` (Bases indexadoras: Scopus / Google Scholar / Web of Science)
- **SJR (Quartil):** Q2 `[VERIFICAR]` (Fonte: SCImago Journal & Country Rank)
- **Qualis (Estrato):** A1 `[VERIFICAR]` (Fonte: Plataforma Sucupira / Qualis CAPES)

### 2.2 Triagem de Elegibilidade
- **Ano ≥ 2020:** Sim (2022 / 2021 online).
- **Publicação ≠ NULL:** Sim (*Personal and Ubiquitous Computing*).
- **Citações ≥ 1:** `[VERIFICAR]` (Pendente de consulta externa).
- **SJR Q1–Q2:** Sim (Q2 declarado; pendente de validação externa no SCImago).
- **Qualis A1–A2:** Sim (A1 declarado; pendente de conferência no Qualis Sucupira).
- **Veredito da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (Citações, confirmação externa de SJR e Qualis). Prossegue-se para a extração analítica das RQs e QA.

---

## 3. Extração e Classificação das Questões de Pesquisa (RQs)

### RQ1 — Context Definitions
- **Veredito:** Não tem conteúdo suficiente (N = 0.0)
- **Evidência:** Seção 1 (pp. 95–96)
- **Análise:** O foco do estudo reside estritamente em interfaces conversacionais voltadas a CRM e recuperação de informações gerais. Não discute níveis de autonomia agêntica, planejamento dinâmico, raciocínio deliberativo, memória de trabalho ou arquitetura de tomada de decisão para sistemas complexos ou incident response.

### RQ2 — Engineering Architecture
- **Veredito:** Não tem conteúdo suficiente (N = 0.0)
- **Evidência:** Seções 4.1.2 e 5.1.2 (pp. 106–107)
- **Análise:** O trabalho não aborda a arquitetura de software interna, mecanismos de orquestração multiagente, integração com ferramentas externas via APIs/plugins, guardrails técnicos ou observabilidade de logs/telemetria. Os chatbots analisados são tratados puramente como caixas-pretas de interação externa.

### RQ3 — Evidence Benefits
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Seções 5.2.2 e 5.2.3, Fig. 2 e Tabela 7 (pp. 100, 108–109)
- **Análise:** Fornece evidências empíricas quantitativas robustas (n = 385 avaliações completas, análise bayesiana de fatores, correlações estatísticas com UMUX-LITE, confiabilidade com alfa de Cronbach de 0.74 a 0.87) em dimensões como eficiência conversacional e tempo de resposta percebido. No entanto, não avalia benefícios específicos para incident response (ex.: MTTR, MTTD, redução de fadiga de alertas).

### RQ4 — Challenges & Ethics
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Tabela 4, Seção 5.2.2, Apêndices 6 e 8 (pp. 103, 108, 114, 116)
- **Análise:** Trata explicitamente de dimensões como "Resilience to failure" (comportamento diante de falhas de comunicação), "Perceived privacy and security" (segurança e conformidade de dados) e "Conversational credibility/trust". Contudo, as discussões são centradas no usuário final de CRM e não cobrem supervisão HITL/HOTL crítica ou threat models cibernéticos.

### RQ5 — Research Gaps
- **Veredito:** Parcialmente Respondida (P = 0.5)
- **Evidência:** Seção 5.3 e Seção 6 (p. 109)
- **Análise:** O artigo destaca a carência metodológica de ferramentas de avaliação padronizadas para interfaces conversacionais de IA, aponta a necessidade de escalas psicométricas validadas e relata desafios como a volatilidade de mercado de bots e inclusão de acessibilidade neurodiversa. Não cobre lacunas específicas de engenharia de software para automação de incidentes.

**SCORE_RQ TOTAL:** **1.5 / 5.0**

---

## 4. Avaliação de Qualidade (Critérios DARE / Kitchenham)

- **QA1 (Objetivos Claros): Y = 1.0**  
  O problema de pesquisa (ausência de escalas padronizadas de satisfação para agentes conversacionais) e os artefatos propostos (escala psicométrica BUS-15 e checklist de diagnóstico BOT-Check) são definidos de maneira explícita e estruturada.
- **QA2 (Metodologia Replicável): Y = 1.0**  
  Apresenta um processo em quatro fases sequenciais com riqueza de detalhes metodológicos: protocolo PRISMA para revisão, cálculo de consenso via IQR e alfa de Krippendorff, condução de grupos focais e análise fatorial exploratória bayesiana (BEFA com pacote R `BayesFM`).
- **QA3 (Base de Evidências Sólidas): Y = 1.0**  
  Há validação empírica expressiva, totalizando 141 participantes em diferentes etapas e 385 coletas completas em 10 chatbots comerciais reais de grande porte (ex.: Amtrak, Toshiba, ATO, HSBC UK, Booking.com).
- **QA4 (Conclusões Coerentes): Y = 1.0**  
  As conclusões derivam com rigor dos dados coletados, com discussão transparente sobre a necessidade de validações confirmatórias adicionais e limitações do perfil etário e de acessibilidade da amostra.

**SCORE_QA TOTAL:** **4.0 / 4.0**  
**Banda de Qualidade:** **Alta** ($\ge 3.0$)

---

## 5. Tabelas Consolidadas da RSL

### Tabela A — Bibliométrica (Tabela 3 da RSL)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P63 | Personal and Ubiquitous Computing | 2022 | [VERIFICAR] | Q2 [VERIFICAR] | A1 [VERIFICAR] | Empírico / Validação Psicométrica | 10.1007/s00779-021-01582-9 |

### Tabela B — Classificação das RQs (Tabela 5 da RSL)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| P63 | Borsci et al. (2022) | RQ1 | Não tem conteúdo suficiente | N | Seção 1 (pp. 95–96) | Ausência de definição de níveis de autonomia agêntica, planejamento ou suporte a incidentes críticos. |
| P63 | Borsci et al. (2022) | RQ2 | Não tem conteúdo suficiente | N | Seções 4.1.2 e 5.1.2 (pp. 106–107) | Não aborda arquitetura de software, orquestração multiagente, ferramentas ou observabilidade em produção. |
| P63 | Borsci et al. (2022) | RQ3 | Parcialmente Respondida | P | Seções 5.2.2 e 5.2.3, Fig. 2 (pp. 100, 108–109) | Traz métricas quantitativas robustas de usabilidade, eficiência de resposta e correlação com UMUX-LITE, mas fora do contexto de IR. |
| P63 | Borsci et al. (2022) | RQ4 | Parcialmente Respondida | P | Tabela 4, Seção 5.2.2, Apêndices 6 e 8 (pp. 103, 108, 114, 116) | Avalia segurança percebida, privacidade, credibilidade conversacional e resiliência a falhas de diálogo. |
| P63 | Borsci et al. (2022) | RQ5 | Parcialmente Respondida | P | Seção 5.3 e Seção 6 (p. 109) | Destaca a carência de benchmarks padronizados e a necessidade de escalas validadas para agentes com IA. |
| **P63** | **SCORE_RQ TOTAL** | — | — | — | — | **1.5 / 5.0** |

### Tabela C — Avaliação de Qualidade (Tabela 7 da RSL)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| P63 | Empírico / Validação Psicométrica | 1.0 | 1.0 | 1.0 | 1.0 | 4.0 | Alta |

---

## 6. Parecer Final do Revisor

- **Síntese:** O estudo destaca-se pelo rigor metodológico no campo de Interação Humano-Computador (IHC), desenvolvendo e validando psicometricamente a *Bot Usability Scale* (BUS-15) e a checklist de diagnóstico *BOT-Check*. Não obstante o alto rigor empírico ($QA = 4.0$), o artigo limita-se à percepção de usabilidade e satisfação do usuário em chatbots de CRM e consulta de informações em cenários gerais, sem tangenciar a arquitetura técnica agêntica, a autonomia de decisão operacional ou pipelines de resposta a incidentes de software e cibersegurança ($SCORE\_RQ = 1.5$).
- **Recomendação:** **INCLUIR COM RESSALVAS** (Estudo de fronteira / metodológico).  
  *Justificativa:* Sua inclusão só se sustenta caso a RSL contemple uma seção dedicada a metodologias e instrumentos padronizados de avaliação de usabilidade/interação humana (HCI/UX) para assistentes e copilotos baseados em IA. Caso a RSL adote um filtro restrito a arquiteturas de software e tarefas operacionais de Resposta a Incidentes (SRE/DevOps/SOC), o estudo deve ser **EXCLUÍDO** por desvio de escopo de domínio.
- **Pendências de verificação externa:**
  1. Extrair a contagem atualizada de citações nas bases indexadoras (Scopus / Google Scholar / Web of Science).
  2. Confirmar a classificação de quartil SJR (Q2) do periódico *Personal and Ubiquitous Computing* no SCImago Journal Rank.
  3. Confirmar a classificação Qualis CAPES (A1) na Plataforma Sucupira para o quadriênio de referência.