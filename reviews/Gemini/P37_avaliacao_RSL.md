# Avaliação Sistemática de Estudo Primário — RSL (Kitchenham et al., 2009 / DARE)

## Identificação do Estudo
- **ID do Artigo:** P37
- **Arquivo PDF Avaliado:** [P37-A2-algorithms-19-00062-v2.pdf](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/P37-A2-algorithms-19-00062-v2.pdf)
- **Prompt de Referência:** [prompt-P37.md](file:///Users/valdomirosouza/Projects/Gemini-ArtigoII/prompt-P37.md)
- **Título:** *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response*
- **Autores:** Olufunsho I. Falowo; Jacques Bou Abdo (School of Information Technology, University of Cincinnati, Cincinnati, OH 45221, USA)
- **Periódico / Fonte:** *Algorithms* (MDPI), Vol. 19, No. 1, Art. 62, pp. 1–32, 2026
- **DOI:** `10.3390/a19010062`

---

## Etapa 0 — Extração Bibliométrica e Escopo

- **Metadados verificados no PDF:** Artigo de pesquisa empírica (*Article*) publicado no periódico *Algorithms* (MDPI), Vol. 19, Art. 62, pp. 1–32, 2026 (Recebido em 2 de dezembro de 2025; Revisado em 29 de dezembro de 2025; Aceito em 7 de janeiro de 2026; Publicado em 11 de janeiro de 2026, p. 1).
- **Métricas externas (`[VERIFICAR]`):**
  - **Citações:** `[VERIFICAR]` (não consta no PDF; verificar no *Scopus* ou *Google Scholar*).
  - **SJR / Quartil:** Informado como `Q2` no input do protocolo (`[VERIFICAR]` no *Scimago Journal Rank* para *Algorithms*, ISSN 1999-4893).
  - **Qualis CAPES:** Informado como `A2` no input do protocolo (`[VERIFICAR]` na *Plataforma Sucupira / Qualis Periódicos* na área de Ciência da Computação).
- **Adequação ao Escopo Temático da RSL:** **Aderente (Foco em Governança, Confiança e Adoção Operacional em Resposta a Incidentes)**. O artigo apresenta um levantamento quantitativo estruturado (*survey*) com 194 profissionais e líderes de cibersegurança nos EUA sobre a adoção de automação inteligente e IA agêntica em fluxos de Resposta a Incidentes (*Incident Response* — IR), confiança na delegação autônoma de decisões e prontidão de frameworks legados (*NIST*, *SANS*, *SOAR*) frente a ameaças impulsionadas por IA.

---

## Etapa 1 — Triagem de Elegibilidade (PRISMA)

| Critério PRISMA | Status | Evidência no Texto / Justificativa |
| :--- | :---: | :--- |
| **1. Publicação entre 2020 e 2026** | **Atende** | Publicado em janeiro de 2026 (*Algorithms*, Vol. 19, Art. 62, p. 1). |
| **2. Qualis A1–A2** | **`[VERIFICAR]`** | Informado no metadado do protocolo como `A2` (requer confirmação externa na Plataforma Sucupira). |
| **3. Escopo: IA Agêntica em redes, segurança ou operações de TI** | **Atende** | Investiga empiricamente a adoção de IA agêntica, automação SOAR, confiança humana e governança em Resposta a Incidentes de Cibersegurança (Seções 1–6, pp. 1–30). |
| **4. Texto completo disponível e acessível** | **Atende** | Texto integral de 32 páginas disponível e analisado via PDF. |
| **5. Sem critérios de exclusão (não é apenas ML clássico, IoT puro, resumo ou duplicata)** | **Atende** | Artigo empírico original (*survey* quantitativo com validação psicométrica KR-20/Alfa de Cronbach) focado especificamente em IA agêntica e automação em IR. |

**Status da Triagem:** **ELEGIBILIDADE PENDENTE DE VERIFICAÇÃO EXTERNA** (aprovado nos critérios de escopo, recorte temporal e texto completo; pendente apenas de verificação externa de Qualis/SJR).

---

## Tabela A — Extração Bibliométrica (Tabela 3 do Protocolo)

| ID | Autores | Título | Ano | Fonte | Qualis | SJR | Citações | Escopo_Resumo |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **P37** | Falowo, O. I.; Abdo, J. B. | *Empirical Study on Automation, AI Trust, and Framework Readiness in Cybersecurity Incident Response* | 2026 | *Algorithms* (MDPI, Vol. 19, Art. 62, pp. 1–32) | A2 `[VERIFICAR]` | Q2 `[VERIFICAR]` | `[VERIFICAR]` | Estudo empírico quantitativo (*survey* com $n = 194$ profissionais de cibersegurança nos EUA) que mensura a adoção operacional de IA agêntica em resposta a incidentes (IR), a redução percebida de MTTD/MTTR, os limiares de confiança na tomada de decisão autônoma e a adequação de frameworks tradicionais (NIST, SANS e SOAR) às ameaças da era da IA. |

---

## Tabela B — Classificação das Questões de Pesquisa (Tabela 5 do Protocolo)

| Questão de Pesquisa (RQ) | Classificação | Pontuação | Evidências e Justificativa Detalhada (com páginas, seções, tabelas e figuras) |
| :--- | :---: | :---: | :--- |
| **RQ1 (Adaptação e autonomia de modelos fundacionais como agentes para gestão de redes/TI)** | **P** | **0.5** | **Abordagem empírica de adoção e níveis de autonomia, sem implementação técnica de modelo fundacional.** Define explicitamente IA agêntica para os respondentes (Seção 4.1.2, p. 12) como sistemas autônomos ou semiautônomos capazes de perceber o ambiente, raciocinar sobre objetivos complexos e executar ações independentes (ex.: atualizar dinamicamente regras de firewall ou isolar nós comprometidos sem *prompts* humanos passo a passo). Quantifica a integração operacional de agentes no ciclo de IR (`84%` já integram IA agêntica, Q2, Tabela 3, p. 11) e os limiares de delegação de autonomia (`13%` confiam em decisão autônoma sem intervenção humana em cenários críticos, Q4; `37%` apoiam triagem e contenção autônomas sem supervisão de analista, Q5; `79%` defendem uma nova taxonomia de ferramentas baseada em níveis de IA agêntica, Q10, p. 11). Não desenvolve nem treina algoritmos ou agentes de software. |
| **RQ2 (Arquiteturas, padrões de design e integração com infraestrutura de TI)** | **P** | **0.5** | **Avalia a integração com plataformas SOAR e frameworks de processos (NIST/SANS), mas não propõe arquitetura de software.** Discute a lacuna de integração fragmentada de *Security Orchestration, Automation, and Response* (SOAR) (Seção 2.6, p. 4) e avalia empiricamente a prontidão estrutural de frameworks de IR na Parte 2 do *survey* (Tabelas 2 e 4, pp. 8, 16–22): identifica que `40%` consideram o ciclo linear clássico (*Preparation $\to$ Detection $\to$ Containment $\to$ Eradication $\to$ Recovery*) rígido demais (Q3 Parte 2), apenas `20%` customizaram o NIST/SANS para ameaças de IA (Q2 Parte 2), `73%` preferem frameworks modulares e simplificados (Q6 Parte 2) e `96%` apoiam revisão ampla dos padrões da indústria para incluir dimensões de ameaças agênticas (Q10 Parte 2, Figura 20, p. 22). |
| **RQ3 (Cenários de avaliação, métricas de desempenho e eficácia)** | **P** | **0.5** | **Avaliação estatística e psicométrica rigorosa de percepções de profissionais, sem bancada experimental de sistemas.** Coleta dados de $n = 194$ profissionais nos EUA via Qualtrics (superando a amostra mínima calculada de $n = 140$ sobre a população de 613.500 gestores de TI do *U.S. Bureau of Labor Statistics*, reduzindo a margem de erro máxima de `8,28%` para `7,04%`, ganho de precisão de `15%`, Seções 3.2 e 5.1, pp. 5–6, 22–23). Valida a consistência interna via Kuder-Richardson 20 (KR-20 / Alfa de Cronbach, Eq. 1, p. 24), obtendo $\alpha = 0,82$ na Parte 1 (*Operational Trust*) e $\alpha = 0,78$ na Parte 2 (*Framework Readiness*). Reporta que `92%` (IC 95%: `[88,2%, 95,8%]`, Q3 Parte 1, pp. 11, 23) confirmam redução significativa de *Mean Time to Detect* (MTTD) e *Mean Time to Respond* (MTTR) e `74%` reportam retreinamento de equipes (Q8 Parte 1). Formula o *"Paradoxo da Automação Eficaz porém Insuficiente"* (Seção 5.5, p. 26): `92%` atestam redução de MTTD/MTTR, mas `70%` afirmam que as ferramentas atuais não conseguem acompanhar a evolução dos ataques impulsionados por IA (Q1 Parte 1). |
| **RQ4 (Desafios de segurança, confiabilidade, alucinação, guarda-corpos e limitações)** | **T** | **1.0** | **Foco central e contribuição primária do artigo.** Quantifica empiricamente as barreiras de confiança, falsos positivos/negativos, governança ética e lacunas de modelagem de ameaças: (1) `87%` desconfiam de decisões autônomas sem supervisão humana em cenários de alto risco (Q4 Parte 1, Figura 4, p. 13); (2) `83%` consideram que os benefícios da automação por IA *não* superam os riscos de falsos positivos ou falsos negativos (Q6 Parte 1, Figura 6, pp. 13–14); (3) `41%` apontam atraso dos marcos regulatórios (Q9 Parte 1, p. 15) e `51%` apontam falta de diretrizes de supervisão ética sobre decisões de agentes de IA nos frameworks atuais (Q5 Parte 2, Figura 15, p. 19); (4) `55%` relatam dificuldade para mapear indicadores de ameaças de IA/ML (como *model drift* ou *data poisoning*) nas categorias tradicionais de IR (Q8 Parte 2, pp. 20–21); e (5) `79%` das organizações não possuem processo separado de modelagem de ameaças para IA (*The AI Threat Modeling Maturity Gap*, Q9 Parte 2 e Seção 5.6, pp. 21, 26–27), criando pontos cegos contra *prompt injection*, *data poisoning* e comportamento não determinístico de sistemas agênticos. Adicionalmente, reflete com transparência exemplar sobre vieses metodológicos (dicotomização binária Sim/Não, amostragem por conveniência/intencional via LinkedIn/ISC2/ISACA restrita aos EUA, viés de autorrelato e *framing effects*, Seções 5.1, 6, 6.2 e 6.3, pp. 23, 27–29). |
| **RQ5 (Tendências futuras e direções de pesquisa abertas)** | **T** | **1.0** | **Agenda de pesquisa futura bem estruturada.** Nas Seções 5.6, 6, 6.1, 6.3 e 6.4 (pp. 26–29), propõe direções claras: (1) estudos longitudinais sobre a evolução de modelos dedicados de ameaças de IA (*adversarial ML*, *prompt injection*, *model drift*) e sua correlação com a confiança institucional em respostas autônomas (Seção 5.6, p. 27); (2) triangulação qualitativa e quantitativa usando entrevistas semiestruturadas, estudos de caso e escalas Likert para capturar nuances da lacuna entre adoção e confiança (Seção 6.3, pp. 28–29); (3) modernização de exercícios *tabletop* com ambientes de simulação dinâmica que incorporem comportamentos adaptativos de agentes de IA (Seções 4.1.18 e 6.1, pp. 20, 27); e (4) um roteiro de validação (*validation roadmap* com estudos-piloto e ajustes iterativos) para construir um framework de IR modular, escalável e orientado à governança ética e *human-in-the-loop* (Seções 6, 6.4 e Tabela 5, pp. 27, 29–30). |
| **Pontuação Total (`SCORE_RQ`)** | — | **3.5 / 5.0** | **Média de aderência às RQs: 70,0% (2 Ts, 3 Ps, 0 N).** |

---

## Tabela C — Avaliação de Qualidade Metodológica DARE (Tabela 7 do Protocolo)

| Critério DARE | Classificação | Pontuação | Justificativa Baseada em Evidências do Artigo |
| :--- | :---: | :---: | :--- |
| **QA1 (Clareza e explicitação dos objetivos e questões da pesquisa)** | **Y** | **1.0** | A Seção 2.7 (p. 4) formula explicitamente duas questões de pesquisa (RQ1 sobre prioridades operacionais, adoção de IA agêntica, MTTD/MTTR e confiança; RQ2 sobre adequação e modernização de frameworks de IR como NIST e SANS), mapeadas diretamente nos 20 itens das Tabelas 1 e 2 (pp. 4–5, 8). |
| **QA2 (Descrição adequada do método, arquitetura e reprodutibilidade)** | **P** | **0.5** | Descreve com transparência os 20 itens binários do instrumento (Tabelas 1 e 2), o protocolo de ética aprovado pelo IRB da University of Cincinnati (`Protocol ID: 2025-0022-UC`, pp. 9, 30), o cálculo amostral (Seção 3.2, p. 6) e a derivação matemática do KR-20 / Alfa de Cronbach (Seção 5.2.3, Eq. 1, p. 24). Contudo, há duas limitações metodológicas: (1) utiliza fórmula de amostragem aleatória simples para população finita (Seção 3.2, p. 6), embora a coleta real tenha ocorrido por amostragem intencional/conveniência em redes profissionais (LinkedIn, ISC2, ISACA), o que os próprios autores ressalvam na Seção 5.1 (p. 23); e (2) menciona na Seção 3.4.2 (p. 9) a inclusão de declarações psicométricas adicionais para checagem de consistência, mas não lista o texto exato dessas perguntas extras nem disponibiliza os microdados brutos em repositório público (disponíveis apenas mediante solicitação, p. 31). |
| **QA3 (Suficiência da validação empírica, cenários e métricas)** | **P** | **0.5** | A amostra de $n = 194$ profissionais atuantes em cibersegurança supera o mínimo planejado ($n = 140$), inclui intervalos de confiança de 95% (Seção 5.1, p. 23) e validação de confiabilidade interna KR-20 ($\alpha = 0,82$ e $\alpha = 0,78$, Seção 5.2.2, p. 24). Entretanto, por se tratar exclusivamente de um *survey* de percepção com variáveis dicotômicas (*Yes/No*), não realiza medições diretas de telemetria de sistemas nem testes estatísticos inferenciais multivariados (restrito a frequências relativas, intervalos de confiança e KR-20). |
| **QA4 (Consistência entre resultados obtidos e conclusões reportadas)** | **Y** | **1.0** | As discussões e conclusões (Seções 5 e 6, pp. 22–30) são altamente coerentes com os dados coletados nas Tabelas 3, 4 e 5, destacando com maturidade crítica as limitações de viés de construto, efeito de enquadramento (*framing effects*), restrição geográfica aos EUA e perda de granularidade das respostas binárias (Seções 6.1–6.3, pp. 27–29). |
| **Pontuação Total (`SCORE_QA`)** | **Banda Alta** | **3.0 / 4.0** | **Qualidade metodológica Alta (`SCORE_QA = 3.0`, no limiar da faixa $\ge 3.0$).** |

---

## Parecer Final do Revisor

### Síntese Crítica (3–5 linhas)
O artigo **P37** oferece uma contribuição empírica valiosa e diferenciada para a RSL sob a ótica de **operações de segurança (SecOps/IR), confiança humana e governança de IA agêntica**, baseada em um *survey* quantitativo com 194 profissionais de cibersegurança nos EUA. O estudo evidencia o *"paradoxo da eficácia versus capacidade"* (`92%` relatam redução de MTTD/MTTR com automação e `84%` já integram IA agêntica, mas `70%` julgam as ferramentas atuais incapazes de acompanhar ataques movidos a IA) e quantifica a forte resistência à autonomia irrestrita (`87%` desconfiam de decisões sem humano no circuito e `83%` temem falsos positivos/negativos). Embora não proponha arquiteturas algorítmicas de agentes (limitando sua pontuação técnica em RQ1–RQ3), é uma fonte primária de alta relevância para fundamentar **RQ4 e RQ5** quanto às lacunas dos frameworks legados (*NIST*, *SANS*, *SOAR*), modelagem de ameaças de IA (`79%` carecem de processo dedicado) e necessidade de supervisão ética (*human-in-the-loop*).

### Recomendação Final
- **Decisão:** **INCLUIR COM RESSALVAS**
- **Justificativa:** Estudo primário elegível e metodologicamente sólido (`SCORE_QA = 3.0/4.0`, Banda Alta; `SCORE_RQ = 3.5/5.0`), essencial para sustentar a discussão empírica sobre adoção industrial, confiança humana, governança e limitações de frameworks de Resposta a Incidentes (**RQ4 e RQ5**). A ressalva deve-se ao caráter exclusivamente perceptual (*survey* binário de opinião profissional, sem implementação ou benchmark técnico de arquitetura agêntica).

### Pendências de Verificação Externa (`[VERIFICAR]`)
1. **Qualis CAPES:** Confirmar a classificação `A2` do periódico *Algorithms* (MDPI, ISSN 1999-4893) na *Plataforma Sucupira (Qualis Periódicos)* na área de Ciência da Computação.
2. **SJR / Quartil:** Confirmar o quartil `Q2` e o índice SJR vigente no portal *Scimago Journal Rank*.
3. **Citações:** Levantar o número atual de citações do artigo (`DOI: 10.3390/a19010062`) no *Scopus* ou *Google Scholar*.
