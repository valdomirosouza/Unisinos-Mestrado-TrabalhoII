# Parecer de avaliação integral — P94

**RSL:** Agentic AI como copiloto no processo de resposta a incidentes  
**Protocolo:** `prompt-P94.md`, diretrizes de Kitchenham (2009)  
**Decisão:** **Incluir c/ ressalvas (evidência restrita à segurança de middleware MCP sob ataques controlados; sem demonstração de redução de MTTD/MTTR ou carga cognitiva)**.

> **Nota de rastreabilidade:** o arquivo `templates/review.md` e as definições operacionais originais de QA1–QA4 não acompanham os dois arquivos disponibilizados. A estrutura abaixo preserva as três tabelas e a recomendação exigidas no prompt; a Tabela C declara explicitamente a interpretação adotada para cada QA. A classificação bibliométrica foi fornecida no prompt, não revalidada neste parecer.

## Tabela A — Identificação e PICOC

| Dimensão | Extração e julgamento | Evidência |
|---|---|---|
| ID | P94 | Prompt da avaliação |
| Título | *Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments* | p. 1 |
| Autores | Rodrigo Tavares de Pina Simões; Xavier Larriva-Novo; Carmen Sánchez-Zas; Victor A. Villagrá; Andrés I. Marín López | p. 1 |
| Ano / periódico | 2026; *Applied Sciences*, 16, artigo 7915; publicado em 8 de agosto de 2026 | p. 1 |
| DOI | 10.3390/app16167915 | p. 1 |
| Tipo / método | Proposta e implementação de framework; modelo de ameaças; avaliação experimental controlada com seis suítes; demonstração da pipeline completa e microbenchmarks | §§3.1–3.5, 4.1–4.5, pp. 5–26 |
| Bibliometria informada | OpenAlex 0; Crossref 0; Scopus 0, consultados em 27/10/2026; percentil Scopus 85%; estrato derivado A2; SJR N/D. **Não somar contagens.** | Prompt P94 |
| Elegibilidade de estrato | A2 segundo os insumos: sem ressalva obrigatória de estrato na PDR-0007. PDR-0006 trata especificamente de conference papers e não altera a condição deste artigo de periódico. | Prompt P94 |
| **Population** | Agentes LLM especializados e sistemas multiagentes vinculados a SIEM/SOC, em uma pipeline de triagem, enriquecimento e proposta de resposta. **Aderente.** | §§1, 3.1, pp. 2–6 |
| **Intervention** | Middleware de segurança sobre MCP: validação de registro de ferramentas, RBAC, rate limiting, validação de entrada/saída e auditoria; controles de sessão e integridade. **Aderente.** | §§3.2.1–3.2.8, pp. 7–14 |
| **Comparison** | **Sim, com escopo restrito:** §4.2 executa uma demonstração com baseline **sem framework** (acesso direto aos servidores MCP) e condição **protegida**, tanto para alerta real quanto sintético. Não há ensaio comparativo de MTTD, MTTR ou carga cognitiva. As seis suítes de bloqueio não são, por si, comparação com baseline desprotegido. | §4.2, pp. 23–24 |
| **Outcome** | Resultado primário: segurança e confiabilidade de chamadas e superfícies MCP. 29/35 vetores com controles; 25 instâncias distintas testadas, 600 decisões de bloqueio corretas, nenhum bypass nesse conjunto. Overhead local medido, mas sem indicadores operacionais de incident response. **Aderência indireta aos benefícios pretendidos pela RSL.** | §§3.2.8, 3.4, 4.1–4.5, pp. 12–14, 18, 23–26 |
| **Context** | SOC com Wazuh SIEM real, servidor MCP dedicado, três agentes em execução sequencial e servidor MCP malicioso de laboratório. **Aderente ao contexto de resposta a incidentes**, mas não a uma operação de produção validada em escala. | §§3.1, 3.3, 5, pp. 5–6, 16–18, 26–28 |
| Síntese de elegibilidade | **Elegível.** Estudo primário diretamente relevante para engenharia, arquitetura e limites de segurança de Agentic AI em SOC. Evidências de desempenho operacional e carga cognitiva são ausentes. | Conjunto do artigo |

## Tabela B — Aderência a RQ1–RQ5

Escala: **T=1,0** (trata diretamente), **P=0,5** (trata parcialmente), **N=0** (não trata).

| RQ | Nota | Evidência âncora (seção/página) | Justificativa crítica |
|---|---:|---|---|
| **RQ1 — capacidades e níveis de autonomia** | **P (0,5)** | §1, p. 2; §3.1, pp. 5–6 | Discute planejamento e invocação de ferramentas, memória compartilhada, especialização de papéis e supervisão humana. A resposta produz propostas que exigem revisão humana, sem executar alterações no SIEM. Não formula taxonomia de níveis de autonomia, nem avalia mudanças na qualidade da decisão por grau de autonomia. |
| **RQ2 — engenharia, arquitetura, guardrails e observabilidade** | **T (1,0)** | §§3.1–3.3, pp. 5–18; Figuras 1–7, pp. 6–11 | Implementa pipeline triagem→enriquecimento→resposta, memória compartilhada, conectores MCP, gateway de segurança e controles de sessão. Detalha auditoria e permissões por papel. Fornece arquitetura e experimento de laboratório, mas não comprova robustez de operação em produção em escala. |
| **RQ3 — evidências de benefícios e métricas** | **P (0,5)** | §3.4, p. 18; §§4.1–4.5, pp. 23–26, Tabelas 12–15 | Apresenta evidência quantitativa de bloqueios e latência local; no teste isolado, 600/600 decisões corretas, porém falhas sob ofuscação (0/4 bloqueadas por técnica no scanner L3) e 7/8 falsos positivos em casos benignos com conteúdo semelhante a ataques. **Não mede MTTD, MTTR, tempo total da triagem, precisão da decisão de incidentes ou carga cognitiva.** |
| **RQ4 — riscos, segurança e governança** | **T (1,0)** | §§1–2, pp. 2–4; §§3.2.1–3.2.8, pp. 7–14; §5, pp. 26–28 | Analisa prompt injection, tool poisoning, confused deputy, envenenamento de memória, abuso de privilégios, saturação de aprovações e trilhas de auditoria. Expõe limitações do matching lexical e dependências da segmentação de rede. Forte contribuição para segurança e accountability técnica; ética mais ampla não é eixo empírico. |
| **RQ5 — lacunas e direções futuras** | **T (1,0)** | §§4.4–4.5, pp. 25–26; §§5–6, pp. 26–29 | Evidencia lacunas em ataques adaptativos, conteúdo multilíngue/ofuscado, falsos positivos, topologias não sequenciais, modelos adicionais, backend de memória escalável, integração de auditoria com SIEM e mecanismos antifraude de logs. Aponta futuras avaliações sem afirmar que foram realizadas. |
| **TOTAL** | **4,0/5,0 — ALTA** | | Evidência mais pertinente a RQ2/RQ4/RQ5. A nota alta de aderência não implica validação de benefícios de produtividade/MTTR. |

## Tabela C — Avaliação de qualidade QA1–QA4

**Limitação do protocolo recebido:** o prompt determina pontuação QA1–QA4, mas não define a redação de cada pergunta. Para evitar atribuir definições inexistentes ao protocolo, são usadas **dimensões analíticas provisórias**, que devem ser substituídas se houver rubrica QA oficial. Escala: Y=1,0; P=0,5; N=0.

| Critério operacionalizado | Nota | Evidência e justificativa |
|---|---:|---|
| **QA1 — objetivos e contribuição claramente formulados** | **Y (1,0)** | §1, p. 3 explicita quatro contribuições: modelo de ameaças, pipeline com Wazuh, controles do framework e validação experimental. |
| **QA2 — método de implementação e avaliação suficientemente descrito** | **Y (1,0)** | §§3.1–3.5, pp. 5–22 detalham camadas, arquitetura, critérios de seleção de vetores, suíte de testes, instâncias repetidas e métricas. Código e dados são indicados como disponibilizados em repositório. |
| **QA3 — resultados sustentados por dados verificáveis no artigo** | **Y (1,0)** | §§4.1–4.5, pp. 23–26 apresentam tabelas com bloqueios, latência local, evasões e falsos positivos. A repetição de testes determinísticos não equivale a 600 amostras independentes; os autores explicitam isso em §3.4. |
| **QA4 — validade externa, robustez e limitações adequadamente demonstradas** | **P (0,5)** | §5, pp. 26–28 reconhece single-model (GPT-4o mini), servidor adversarial construído para o experimento, topologia sequencial, backend de memória baseado em arquivos e DNS-rebinding check inativo no ambiente testado. Os testes adicionais de ofuscação e falso positivo revelam fragilidade real; falta validação longitudinal e adversarial em produção. |
| **TOTAL PROVISÓRIO** | **3,5/4,0** | Qualidade metodológica satisfatória dentro do escopo de laboratório; reavaliar sob a rubrica QA oficial, se disponível. |

## Achados quantitativos para a síntese

1. **Cobertura arquitetural:** 29 de 35 vetores foram mapeados a controles do middleware. Os seis não cobertos incluem RAG/knowledge-base poisoning, embeddings adversariais, package hallucination, manipulação de consenso, coordenação encoberta e replay (§3.2.8, pp. 12–14). **Cobertura nominal não significa prova experimental completa de 29 trajetórias end-to-end.** Quatro vetores são transportados pelo servidor MCP malicioso real; os demais são exercitados por injeções no harness (§3.2.8, pp. 13–14).
2. **Experimentos de bloqueio:** seis suítes T00–T05; 25 instâncias distintas repetidas 20 vezes; alguns casos produzem mais de uma decisão por repetição, totalizando **600 decisões**. Resultado **600/600 bloqueadas, 0 bypasses e 0 falsos bloqueios nos casos benignos do harness** (§§3.4 e 4.1, pp. 18, 23). Os ensaios repetem cargas determinísticas; não demonstram robustez estatística frente a novos ataques.
3. **Comparador operacional real:** a demonstração da pipeline confronta diretamente execução **sem middleware** e **com middleware**, usando um alerta real Wazuh e um cenário sintético. Campos decisórios do plano permaneceram iguais para alertas benignos; a comparação não inclui ganho de tempo ou de qualidade decisória (§4.2, pp. 23–24).
4. **Overhead de controles:** benchmark local de 10.000 iterações temporizadas por controle, após 200 de aquecimento. Validação de JSON Schema média de 546,6 µs (11,4 µs após pré-compilação); processamento local agregado informado abaixo de 0,6 ms e abaixo de 30 µs com otimização. **Não é latência end-to-end da resposta a incidentes** (§4.3, pp. 24–25).
5. **Evasão adversarial:** quatro payloads originalmente bloqueados por L3 foram ofuscados por base64, homoglifos, tradução ao espanhol e paráfrase; em cada modalidade, **0/4 permaneceu bloqueado**. Restringe a inferência de sucesso aos padrões literais não adaptativos (§4.4, p. 25).
6. **Falsos positivos:** sete de oito entradas legítimas com substrings semelhantes a ataques foram bloqueadas pelo scanner de argumentos L3, em análise separada. Portanto, **0 falsos positivos na Tabela 12 não é uma taxa generalizável para tráfego real de SOC** (§4.5, pp. 25–26).

## Interpretação e aplicação à dissertação

O P94 oferece evidência primária para **guardrails e arquiteturas de Agentic AI aplicadas à resposta a incidentes**, particularmente fronteiras de confiança entre agentes, ferramentas MCP, memória e fontes externas. Seu padrão de gateway independente do modelo, privilégio mínimo e aprovação humana para ações consequenciais oferece subsídios de engenharia para um copiloto SRE/SOC. Logs por sessão com sanitização de dados também ajudam a fundamentar observabilidade, auditabilidade e responsabilização.

A contribuição **não deve ser extrapolada** como prova de melhoria em MTTD/MTTR, diminuição de fadiga, redução da sobrecarga cognitiva ou eficácia de resolução. A demonstração não implementa remediação automática: o agente de resposta formula propostas para apreciação do analista (§3.1, p. 6). Além disso, os testes revelam que detecção lexical isolada não é suficientemente confiável diante de ataques adaptativos ou de logs benignos que contêm sequências suspeitas.

Para a síntese da RSL, classificar os resultados de **600/600 bloqueios** como eficácia **interna dos controles sob os ataques definidos**, e o benchmark de tempo como **overhead de middleware**, não como tempo operacional de recuperação. A separação entre mecanismo de proteção e outcome de incident response é essencial para não confundir segurança do copiloto com efetividade do copiloto.

## Limitações do parecer e controle de viés

- O estrato A2 e as contagens de citação decorrem **exclusivamente dos metadados fornecidos pelo prompt**. Não houve uma nova auditoria bibliométrica independente.
- A rubrica QA1–QA4 foi operacionalizada provisoriamente porque suas definições e o arquivo `templates/review.md` não foram anexados.
- O estudo informa implementação em repositório público, mas o presente parecer **não realizou auditoria do código nem reprodução dos testes**.
- As conclusões empíricas respeitam o recorte de laboratório, a topologia sequencial e os payloads definidos pelos autores.

## Recomendação final

**Incluir c/ ressalvas (evidência experimental forte e tematicamente relevante sobre segurança de sistemas multiagentes MCP em SOC, especialmente RQ2, RQ4 e RQ5; validade circunscrita a cenários controlados e não adaptativos, com evasão por ofuscação e falsos positivos em tráfego legítimo; ausência de evidência direta de redução de MTTD, MTTR ou carga cognitiva).**

**Estrato:** A2 conforme informado, sem ressalva obrigatória de estrato sob PDR-0007.
