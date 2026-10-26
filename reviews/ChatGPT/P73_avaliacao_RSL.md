# Avaliação do estudo P73 — Ciclo 2 da RSL

**RSL:** Agentic AI Copilot para Resposta a Incidentes: Uma Revisão da Literatura  
**Artigo:** Ban, T.; Takahashi, T.; Ndichu, S.; Inoue, D. *Breaking Alert Fatigue: AI-Assisted SIEM Framework for Effective Incident Response*.  
**Fonte avaliada:** PDF fornecido, 29 páginas.  
**Método:** protocolo de avaliação fornecido em `prompt-P73.md`; análise exclusivamente documental.

## Etapa 0 — Tabela A: Bibliometria (Tabela 3)

| ID | Periódico/Conf. | Ano | Cit. | SJR | Qualis | Tipo | DOI |
|---|---|---:|---|---|---|---|---|
| P73 | *Applied Sciences*, 13(11), artigo 6610 | 2023 | [VERIFICAR] | [VERIFICAR] (Q2 informado no prompt) | [VERIFICAR] (A2 informado no prompt) | Proposição de framework com protótipo e avaliação experimental quantitativa em dados de SOC empresarial | https://doi.org/10.3390/app13116610 |

**Rastreabilidade:** capa e referência bibliográfica na p. 1; introdução e contribuições nas pp. 2–3; experimentos na Seção 5, pp. 16–22. Os valores Q2 e A2 constituem *metadados informados no prompt*, não uma verificação independente no PDF. Não são confirmados nesta avaliação.

## Etapa 1 — Elegibilidade

| Critério | Evidência / situação | Resultado |
|---|---|---|
| Ano ≥ 2020 | Publicado em 29 de maio de 2023; p. 1 | Atende |
| Veículo identificável | *Applied Sciences*, volume 13, artigo 6610; p. 1 | Atende |
| Pelo menos uma citação | O PDF não fornece contagem de citações recebidas | [VERIFICAR] |
| SJR Q1–Q2 | Q2 fornecido no prompt, não demonstrado no PDF | [VERIFICAR] |
| Qualis A1–A2 | A2 fornecido no prompt, não demonstrado no PDF | [VERIFICAR] |

**Resultado:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA (citações recebidas, quartil SJR e estrato Qualis).** De acordo com o protocolo, a condição pendente permite prosseguir à extração completa. A aprovação prévia na triagem, declarada no prompt, não substitui a conferência bibliométrica.

## Etapa 2 — Tabela B: Classificação das RQs (Tabela 5)

| ID | Artigo | RQ | Veredito | Símbolo (T/P/N) | Evidência (seção/pág.) | Parecer do revisor |
|---|---|---|---|---|---|---|
| P73 | Breaking Alert Fatigue | RQ1 — Context Definitions | Não tem conteúdo suficiente | N (0,0) | Seções 2.1.3, 3.3 e 4.1; pp. 4, 7–11 | O texto descreve automação SOAR e classificação supervisionada, mas não define autonomia agêntica nem especifica planejamento, memória, seleção autônoma de ferramentas ou modelo deliberativo de decisão. A triagem executada por ML não equivale a um agente autônomo. As dimensões (a), (b) e (c), na acepção de Agentic AI, não são explicitamente atendidas. |
| P73 | Breaking Alert Fatigue | RQ2 — Engineering Architecture | Parcialmente Respondida | P (0,5) | Figura 1 e Seção 3, pp. 6–9; Seções 4.1–4.2, pp. 10–14 | Há arquitetura de SIEM em quatro módulos (geração, processamento, ML e investigação), com normalização JSON, one-hot encoding, IWSVM, segmentação temporal/espacial e visualização ATG. A integração SOAR é contextualizada. Não são implementados ou detalhados mecanismos típicos de agentes, como memória operacional, planos, ciclo agente–ferramenta e guardrails de execução. Cobertura explícita das dimensões arquitetura e ferramentas, apenas parcial das capacidades avançadas agênticas. |
| P73 | Breaking Alert Fatigue | RQ3 — Evidence Benefits | Respondida Plenamente | T (1,0) | Seções 5.1–5.5, pp. 16–22; Tabelas 3, 5, 6 e 7, pp. 19–22 | Evidência experimental quantitativa e discussão qualitativa sobre redução de falsos alertas e esforço de investigação. Em NSOC2017, IWSVM obteve recall de 99,643%, precisão de 99,687% e FPR de 0,001% (Tabela 3). Em NSOC2022, a redução generalizada de alertas (GARR) variou de 74,070% a 83,980% (Tabela 7). A evidência se refere a filtragem/correlação no SOC, **não** a desempenho de agente autônomo; não há medida direta de MTTR, MTTD ou carga cognitiva. As dimensões benefício qualitativo, métricas quantitativas e nível de evidência são explicitamente contempladas no âmbito do estudo. |
| P73 | Breaking Alert Fatigue | RQ4 — Challenges & Ethics | Respondida Plenamente | T (1,0) | Seções 6.2–6.3.4, pp. 23–24 | Discute privacidade, segurança de dados, falsos positivos, conformidade legal, auditorias, políticas de retenção, viés associado aos analistas e às políticas do SOC, erros de detecção, ameaças emergentes, ataques adversariais e necessidade de atualização do modelo. Propõe controles organizacionais e feedback humano. Esses mecanismos são apresentados para SIEM/ML, não como política formal de governança de agentes autônomos. |
| P73 | Breaking Alert Fatigue | RQ5 — Research Gaps | Respondida Plenamente | T (1,0) | Seções 6.1, 6.3.1–6.4, pp. 22–24 | Aponta necessidade de piloto em SOC real, validação de integração e escalabilidade, estudos com redes e ataques mais diversos, mitigação de erros e viés, adaptação a ameaças novas, avaliação contínua e retreinamento. Não formula agenda específica de benchmarking ou alinhamento de sistemas multiagentes, mas apresenta explicitamente lacunas e direções futuras aplicáveis à automação de resposta a incidentes. |
| **P73** | **TOTAL** | **SCORE_RQ** | **3,5 / 5,0** | **N + P + T + T + T** | **Seções 2–6** | **Boa evidência complementar sobre automação assistida por ML; aderência limitada à autonomia agêntica.** |

### Justificativa da classificação por subdimensão

**RQ1:** (a) definição de autonomia agêntica: ausente; (b) capacidades centrais agênticas: ausentes; (c) decisão agêntica: ausente. Existe classificação automática de alertas e supervisão humana, mas sem caracterização de um agente que planeja e age autonomamente.

**RQ2:** (a) tipo de arquitetura: presente, como framework SIEM modular; (b) ferramentas/tecnologias: presentes (IDS, SOAR em nível de integração proposta, IWSVM/LIBSVM, JSON, ATG e algoritmo de segmentação); (c) recursos avançados: parciais, sem memória, planejamento ou guardrails agênticos detalhados.

**RQ3:** (a) benefícios qualitativos: presentes; (b) métricas quantitativas: presentes (precision, recall, FPR, F1, ARR e GARR); (c) nível de evidência: avaliação empírica com dados de rede corporativa, mas sem demonstração de ganhos reais de tempo de resposta ou de redução mensurada da carga cognitiva.

**RQ4:** (a) desafios técnicos: presentes; (b) ética e governança: presentes; (c) mecanismos de governança: recomendações explícitas de políticas de coleta e retenção, privacidade, auditoria, revisão de alertas por operadores e atualização dos modelos, sem validação operacional específica desses controles.

**RQ5:** lacunas e trabalhos futuros explicitamente articulados na Seção 6.4 e em limitações técnicas anteriores; foco em SIEM e ML, não em governança de agentes autônomos.

## Etapa 3 — Tabela C: Avaliação de qualidade (Tabela 7)

| ID | Tipo de estudo | QA1 | QA2 | QA3 | QA4 | SCORE_QA | Banda |
|---|---|---|---|---|---|---|---|
| P73 | Framework proposto e avaliação experimental quantitativa com dados reais de SOC | P (0,5) | P (0,5) | Y (1,0) | Y (1,0) | **3,0 / 4,0** | **Alta** |

### Fundamentação dos critérios QA

**QA1 — P (0,5).** Objetivo e problema são explícitos: combater *alert fatigue* causada por falsos alertas e redundância mediante filtragem ML e correlação (Resumo e Introdução, pp. 1–3; Seção 4, pp. 10–14). A rubrica exige também solução **agêntica** explícita, que não é demonstrada. A pontuação parcial evita equiparar automaticamente IA assistida a Agentic AI.

**QA2 — P (0,5).** Arquitetura, funções dos módulos, representação de atributos, definição formal do IWSVM, algoritmo de segmentação, parâmetros, datasets, estratégias SCV/ROV e métricas estão documentados (Seções 3–5, pp. 6–22; Figura 1; Algoritmo 1; Tabela 1). Entretanto, os datasets empresariais não estão disponíveis publicamente e o código é disponibilizado apenas mediante solicitação (*Data Availability Statement*, p. 25). Essas restrições comprometem a replicação independente integral. O estudo também não valida um agente autônomo completo.

**QA3 — Y (1,0).** Experimentos com dados de rede empresarial, incluindo NSOC2017 e NSOC2022, coletados a partir de múltiplos IDS e de operação de SOC, e comparação por métricas quantitativas (Seção 5, pp. 16–22; Tabelas 2–7). A evidência é empírica e não apenas um exemplo hipotético. A ressalva é que avaliação sobre dados reais não equivale a implantação integral do framework em produção.

**QA4 — Y (1,0).** As conclusões da Seção 7 (pp. 24–25) correspondem à filtragem e correlação examinadas na Seção 5; o texto reconhece limitações de escopo, viés, erro de detecção, ataques adversariais, degradação temporal e generalização (Seção 6, pp. 22–24). A promessa de eficiência operacional deve ser compreendida como potencial inferido pela redução de alertas, não como ganho temporal de resposta diretamente medido.

## Parecer final do revisor

### Síntese

O P73 apresenta um framework SIEM de assistência à resposta a incidentes, com filtragem supervisionada sensível a custos, correlação de alertas e visualização ATG. A avaliação utiliza dados operacionais de SOC e oferece métricas sólidas de qualidade de classificação e redução de volume de alertas, com GARR entre 74,070% e 83,980% na Tabela 7. O trabalho contribui de forma direta para o *Outcome* de fadiga de alertas e para o suporte à triagem humana. Contudo, sua capacidade de agência é limitada: não demonstra agente LLM, planejamento autônomo, memória ou execução deliberativa de ferramentas. A extrapolação dos resultados para redução de MTTR/MTTD ou de carga cognitiva de operadores não é empiricamente sustentada.

### Recomendação

**INCLUIR COM RESSALVAS**, condicionado à confirmação dos requisitos bibliométricos externos.

**Fundamentação:** a contribuição é relevante como antecedente técnico e evidência empírica complementar de *AI-assisted incident response*, em particular à redução do volume de alertas e ao suporte à decisão em SOCs. O artigo **não** deve ser apresentado como evidência direta de arquitetura Agentic AI ou de autonomia na resposta a incidentes. Sugere-se identificá-lo na síntese da RSL como **IA/ML assistiva, não agêntica, com controle e investigação humanos**. A continuidade da inclusão depende da compatibilidade dessa categoria limítrofe com o critério de escopo do protocolo completo da revisão.

### Pendências de verificação externa

1. **Citações recebidas ≥ 1 [VERIFICAR]:** consultar Scopus, Web of Science ou Google Scholar e registrar a contagem e a data da consulta.
2. **Quartil SJR Q2 [VERIFICAR]:** confrontar o metadado fornecido no prompt com o *SCImago Journal Rank*, registrando ano de referência e categoria temática.
3. **Qualis A2 [VERIFICAR]:** consultar Plataforma Sucupira / Qualis CAPES, conferindo área, período de avaliação e correspondência do periódico. O percentil Scopus informado no prompt não constitui por si só comprovação documental do estrato.

### Notas de cautela na síntese da RSL

- **ARR ≠ GARR:** a Tabela 6 relata ARR de 45,010% a 50,490% para filtragem nos conjuntos preliminares, enquanto a Tabela 7 relata GARR de 74,070% a 83,980% para filtragem combinada com correlação. Não intercambiar as métricas.
- **Desempenho de detecção ≠ desempenho operacional humano:** precisão, recall, F1 e volume de alertas são medidas da solução analítica; não são medidas diretas de tempo de resolução, fadiga psicológica ou esforço cognitivo.
- **Dados de produção ≠ framework integral implantado:** os datasets provêm de SOC empresarial, mas a Seção 6.4 propõe implementar e avaliar o framework em ambiente real como trabalho futuro.
- **Limitação de reprodutibilidade:** datasets não públicos e código mediante solicitação (p. 25).

---

*Avaliação restrita ao PDF disponibilizado, sem consultas a fontes externas. A classificação bibliométrica permanece provisória nos campos identificados com [VERIFICAR].*
