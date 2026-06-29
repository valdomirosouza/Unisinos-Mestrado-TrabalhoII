# Avaliação RSL — Estudo P23

**Artigo:** _TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems_ — X. Zhang, Q. Wang, M. Li, Y. Yuan, M. Xiao, F. Zhuang, D. Yu (Shandong University et al.)
**Arquivo:** P23-A1-TAMO...pdf (13 páginas)

## Tabela A — Bibliométrica (Tabela 3)

| ID  | Periódico/Conf.                                          | Ano  | Cit.                          | SJR                               | Qualis                                          | Tipo                                                                                        | DOI                      |
| --- | -------------------------------------------------------- | ---- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------ |
| P23 | IEEE Transactions on Services Computing (Vol. 18, No. 6) | 2025 | [VERIFICAR] (base indexadora) | [VERIFICAR] (Scimago; insumo: Q1) | [VERIFICAR] (Qualis CAPES/Sucupira; insumo: A1) | Artigo de pesquisa c/ avaliação experimental (DL/LLM, 2 datasets, ablações, estudo de caso) | 10.1109/TSC.2025.3629066 |

_Evidências: cabeçalho p.1 (DOI; recebido 10/06/2025, aceito 27/10/2025, publicado 05/11/2025); rótulo "IEEE Transactions on Services Computing, Vol. 18, No. 6, Nov/Dec 2025". Citações/SJR/Qualis não constam no PDF. Carimbo de download IEEE Xplore identifica "UNIVERSIDADE DO VALE DO RIO DOS SINOS"._

## Tabela B — Classificação das RQs (Tabela 5)

| ID  | Artigo                   | RQ                           | Veredito                | Símbolo       | Evidência (seção/pág.)                    | Parecer do revisor                                                                                                                                                                                                                                                                                                                                                                                                       |
| --- | ------------------------ | ---------------------------- | ----------------------- | ------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P23 | TAMO (Tool-Assisted RCA) | RQ1 Context Definitions      | Parcialmente Respondida | **P**         | §III, §III.D (p.3-7), Fig.2               | Uso de ferramentas presente — agente A invoca tools T1-T3 como ferramentas de percepção (b parcial). Porém **autonomia não é definida** (a ausente), não há memória nem planejamento dinâmico (pipeline fixo), e a "decisão" agêntica resume-se a síntese de relatório pelo GPT-4 — modelo decisório agêntico não caracterizado (c tangencial). O cerne é um método DL multimodal, não autonomia agêntica.               |
| P23 | "                        | RQ2 Engineering Architecture | Respondida Plenamente   | **T**         | §III.A-D (p.3-7), Fig.2, Tab. IV          | Arquitetura explícita — 3 tools + 1 expert agent em pipeline (a); stack rico e detalhado: difusão dual-branch, Drain+TF-IDF, FFT, GAT, Transformer, GPT-4, PyTorch/CUDA (b); capacidades avançadas — alinhamento multimodal por difusão, análise causal em domínio de frequência, prompts estruturados (c). Ressalva: guardrails/observabilidade/memória ausentes e avaliação é offline (não "em produção").             |
| P23 | "                        | RQ3 Evidence Benefits        | Respondida Plenamente   | **T**         | §IV.C-G, Tabs. II-III, Figs. 4-7 (p.7-11) | Quantitativo robusto: Acc@1 +4,8% (localização) e MiPr +10,8% (classificação) vs SOTA; ablações (Tab. III); eficiência (inferência 0,17s/amostra; treino 0,81-5,7s/época); confianças do estudo de caso (97,96%/82,39%) (b); benefícios qualitativos — comparação TAMO-LLM vs LLM-com-dados-brutos (Fig. 7) (a); evidência forte — 2 datasets públicos, múltiplos baselines, ablação, sensibilidade, estudo de caso (c). |
| P23 | "                        | RQ4 Challenges & Ethics      | Parcialmente Respondida | **P**         | §I (3 desafios), §IV.F (p.1-2, 10)        | Desafios técnicos bem articulados (multimodalidade, janela de contexto, grafo de dependência dinâmico) e sensibilidade a hiperparâmetro β como questão de robustez (a). Porém **nenhuma discussão ética/governança/accountability** (b, c ausentes).                                                                                                                                                                     |
| P23 | "                        | RQ5 Research Gaps            | Parcialmente Respondida | **P**         | §I, §II, §V (p.1-3, 11)                   | Lacunas do estado da arte bem identificadas (limitações de métodos existentes). Mas **sem seção de trabalhos futuros**; a conclusão não aponta direções futuras, threat models, governança, observabilidade ou alinhamento.                                                                                                                                                                                              |
|     |                          | **SCORE_RQ**                 |                         | **3.5 / 5.0** |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Tabela C — Avaliação de Qualidade (Tabela 7)

| ID  | Tipo de estudo                                        | QA1         | QA2         | QA3         | QA4         | SCORE_QA      | Banda    |
| --- | ----------------------------------------------------- | ----------- | ----------- | ----------- | ----------- | ------------- | -------- |
| P23 | Artigo de pesquisa c/ avaliação experimental (DL/LLM) | **Y** (1.0) | **Y** (1.0) | **Y** (1.0) | **P** (0.5) | **3.5 / 4.0** | **Alta** |

_Âncoras:_

- **QA1 = Y** — três desafios de RCA fina e a solução (tool-assisted LLM agent) explícitos (§I).
- **QA2 = Y** — formulação matemática completa, hiperparâmetros (batch 32, μ=0,5, β=0,001, 200 épocas, lr=0,001), hardware (RTX 3090), datasets públicos, estratégia de treino em estágios e baselines com código aberto. Alta replicabilidade.
- **QA3 = Y** — validação empírica robusta: 2 datasets públicos, múltiplos baselines, ablação, sensibilidade de hiperparâmetros e estudo de caso real (HipsterShop).
- **QA4 = P** — conclusões coerentes com as evidências, **porém limitações não são discutidas** (sem seção de limitações; apenas a sensibilidade a β é mencionada de passagem). A ausência de discussão crítica de limitações rebaixa o critério.

## Parecer final do revisor

**Síntese.** Trabalho técnico forte de **RCA fina** em sistemas cloud-native, combinando alinhamento multimodal por difusão, localização causal em domínio de frequência (FFT+GAT) e classificação de tipos de falha, com um **agente especialista LLM (GPT-4)** sintetizando os resultados em relatório e recomendações. Alta aderência a **RQ2** (arquitetura/ferramentas) e **RQ3** (evidências quantitativas robustas). Contudo, do ponto de vista de **Agentic AI** o componente agêntico é **limitado**: o "agente" é majoritariamente uma camada de síntese sobre um pipeline DL fixo — sem autonomia definida, planejamento dinâmico, memória ou execução de remediação (apenas sugestões). Por isso **RQ1, RQ4 e RQ5 ficam parciais**.

**Recomendação: INCLUIR COM RESSALVAS.** SCORE_RQ 3,5/5,0 e QA 3,5/4,0 (Banda Alta). Estudo metodologicamente sólido e altamente relevante para a etapa de **diagnóstico/RCA** da Resposta a Incidentes, mas com baixa contribuição às questões de **autonomia agêntica** (RQ1) e **desafios/ética** (RQ4), e sem direções futuras (RQ5). Ressalva central a registrar no mapeamento: enquadra-se melhor como **RCA assistida por ferramentas com LLM** do que como sistema agêntico autônomo — útil para contrastar com estudos de remediação autônoma (ex.: P22).

**Pendências de verificação externa:**

- **Citações** ≥ 1 → IEEE Xplore / Scopus / Google Scholar.
- **SJR (quartil)** → Scimago, _IEEE Transactions on Services Computing_ (insumo: Q1).
- **Qualis (estrato)** → Plataforma Sucupira / Qualis CAPES (insumo: A1).

Critérios verificáveis no PDF atendidos (Ano 2025 ✓; veículo IEEE TSC ✓); os três acima ficam **PENDENTES DE VERIFICAÇÃO EXTERNA**.
