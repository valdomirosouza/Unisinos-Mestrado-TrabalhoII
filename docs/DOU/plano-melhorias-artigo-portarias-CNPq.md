# Plano de melhorias do artigo — conformidade com as Portarias CNPq nº 2.664/2026 e nº 3.004/2026

**Data:** 2026-11-23 · **Alvo:** `artigo/main.tex` — _"Agentic AI Copilots for Incident Response: A Systematic Literature Review"_ (draft IEEE Access)
**Fontes normativas (DOU, em `docs/DOU/CNPq/`):**

- **Portaria CNPq nº 2.664, de 6 de março de 2026** (DOU 11/03/2026) — institui a **Política de Integridade na Atividade Científica** do CNPq: código de boas práticas, diretrizes de integridade (incl. IAG), CIAC, infrações e sanções.
- **Portaria CNPq nº 3.004, de 16 de novembro de 2026** (DOU 18/11/2026) — institui **diretrizes para uso de IAG (Inteligência Artificial Generativa) e IAP (Inteligência Artificial Preditiva)** na pesquisa apoiada pelo CNPq; LGPD, confidencialidade, responsabilidade e declaração obrigatória de uso.

---

## 1. Aplicabilidade ao artigo

As portarias alcançam, além de bolsistas e proponentes, **usuários das plataformas do CNPq (Lattes, Carlos Chagas)** e agentes vinculados ao fomento (2.664, art. 4º; 3.004, art. 2º). Ambos os autores mantêm Currículo Lattes e atuam em programa avaliado pela CAPES; o orientador participa do ecossistema de fomento. Ainda que o artigo declare _"no specific grant"_, a conformidade é (i) juridicamente prudente, (ii) exigência provável de editais e avaliações futuras (dissertação, chamadas), e (iii) **argumento metodológico a favor do artigo**: o protocolo _LLM-assisted, human-decided_ pode ser apresentado como _compliant-by-design_ com a primeira regulação federal brasileira sobre IAG em pesquisa — publicada **depois** do desenho do protocolo.

## 2. Diagnóstico — o que o artigo já atende

| Exigência                                     | Dispositivo                               | Situação no artigo                                                                                                                    |
| --------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Declarar ferramenta **e versão**              | 3.004, art. 4º-I                          | ✅ Table `llmversions` (Seção III): Claude/ChatGPT/Gemini por ciclo, com versões exatas                                               |
| Declarar **fase** de uso                      | 3.004, art. 4º-II                         | ✅ Parcial — Seção III descreve uso na avaliação full-text; identificação assistida (ciclo 1) descrita em _Search and identification_ |
| Declarar **finalidade específica**            | 3.004, art. 4º-III                        | ✅ Parcial — metodologia descreve o papel dos assistentes (draft de pareceres, extração PICOC)                                        |
| Responsabilidade integral dos autores         | 3.004, art. 6º; 2.664, art. 9º-I-d/f      | ✅ Framing _"inputs to, not substitutes for, the authors' judgment"_; Threats: _"no screening… was delegated to an LLM"_              |
| Verificação não delegada à IAG                | 3.004, art. 6º §1º                        | ✅ Em substância: _hallucination screen_ é gatilho de verificação humana; âncoras de evidência por claim; decisão sempre dos autores  |
| Proveniência de versão no momento da geração  | 3.004, art. 4º-I                          | ✅ Rodapé obrigatório de versão/timestamp ratificado após o ciclo 3 (melhoria de protocolo já registrada no artigo)                   |
| Citações fiéis, fonte primária vs. secundária | 2.664, art. 9º-II-i/j/l                   | ✅ Prática da RSL (ex.: ganhos "dramáticos mas não reproduzidos" relatados como fonte secundária)                                     |
| Dados por fonte, sem somar                    | Convenção própria + 2.664, art. 9º-II-m/n | ✅ Citações por fonte; _audit trail_ documentado                                                                                      |

**Conclusão do diagnóstico:** o _corpo metodológico_ já é conforme. As lacunas estão no **fecho do artigo** (back matter) — exatamente o bloco removido em 2026-11-01 aguardando a revisão do orientador — e em **declarações formais** que as portarias agora tornam obrigatórias, não opcionais.

## 3. Melhorias propostas

### Prioridade ALTA (exigências diretas)

**A1. Seção própria "Declaration of Generative AI Use" (back matter).**
_Base:_ 3.004, art. 4º caput e **§1º** ("na ausência de campos estruturados… incluir a declaração em seção específica no próprio documento"); 2.664, art. 9º-I-c. _Omissão injustificada é apurável_ (3.004, art. 4º §2º).
_Ação:_ criar seção não numerada antes das referências declarando, por fase da pesquisa: (i) ferramenta + versão (remeter à Table `llmversions`); (ii) fase (identificação assistida no ciclo 1; extração PICOC; draft dos pareceres full-text; apoio à redação/revisão do manuscrito, se houve — **declarar também o uso de IAG na escrita do próprio artigo**, incluindo o apoio de Claude Code na preparação do LaTeX); (iii) finalidade específica de cada uso. Fechar com: conteúdo final validado pelos autores; nenhuma decisão de inclusão/exclusão delegada à IAG.
_Nota:_ isto resolve, com base normativa, a pendência "divulgação do uso de LLMs" do bloco Acknowledgment removido (commit `620bbdb`); submeter o texto ao orientador junto com esta justificativa.

**A2. Declaração de confidencialidade e dados pessoais.**
_Base:_ 3.004, arts. 5º (LGPD), 6º §2º (planos gratuitos/treinamento), 7º (vedação de conteúdo sigiloso em IAG) e 8º §1º (vedação ao parecerista); 2.664, art. 9º-I-e.
_Ação:_ acrescentar à seção A1 um parágrafo afirmando que: (i) apenas **textos integrais publicados e legitimamente acessados** foram fornecidos às ferramentas — nenhum manuscrito inédito, projeto de terceiros sob avaliação, dado sigiloso ou dado pessoal (LGPD não incidente); (ii) o uso de IAG aqui **não constitui parecer/avaliação por pares** no sentido do art. 8º — os assistentes avaliaram literatura publicada sob um protocolo de RSL, com decisão humana; (iii) registrar o **modo de acesso** de cada ferramenta (Claude Code; ChatGPT e Gemini via aplicação web) e o plano/condição de tratamento de dados dos serviços. ➜ **Insumo do condutor necessário:** confirmar se os planos eram pagos e se havia _opt-out_ de treinamento.

**A3. Responsabilização explícita no texto.**
_Base:_ 3.004, art. 6º caput e §1º; 2.664, art. 9º-I-d/f.
_Ação:_ uma frase na seção A1 (não apenas na metodologia): _"The authors take full responsibility for all content, including factual claims, citations, and references; final verification was performed by the authors and was not delegated to any generative AI tool."_ A metodologia já diz isso em espírito; a declaração formal precisa dizê-lo com as palavras da norma.

### Prioridade MÉDIA (boas práticas exigíveis no fecho/submissão)

**A4. Data Availability + depósito do audit trail com DOI.**
_Base:_ 2.664, art. 9º-I-g (conservação de dados, metadados, protocolos, código; depósito em repositório confiável "sempre que possível").
_Ação:_ depositar o pacote de replicação (protocolo, prompts canônicos, pareceres, CSVs de extração, scripts de κ, PRISMA, rede de citações) em repositório confiável (Zenodo/OSF) com DOI e citar na seção _Data Availability_. Já era a pendência C7.4 do parecer PPGCA — agora com base normativa. Atenção: o pacote público **não** pode conter os PDFs com direitos autorais (separar dados derivados dos textos-fonte).

**A5. Declaração de contribuições de autoria (CRediT).**
_Base:_ 2.664, art. 9º-II-p/r/s (critérios de autoria desde o início, responsabilização, capacidade de descrever a contribuição individual; remete a diretrizes tipo ICMJE).
_Ação:_ seção/nota com taxonomia CRediT: condutor (conceptualization, methodology, investigation, data curation, writing — original draft); orientador (supervision, validation, writing — review & editing).

**A6. Conflito de interesses.**
_Base:_ 2.664, arts. 3º-III e 5º-VII.
_Ação:_ declarar o vínculo industrial do primeiro autor (Head of IT, Zenvia) e afirmar ausência de conflito com os fornecedores citados — coerente com o próprio artigo, que sinaliza evidência _vendor-affiliated_ nos estudos primários. Nenhum dos estudos incluídos tem vínculo com os autores.

**A7. Declaração de divulgação prévia na submissão.**
_Base:_ 2.664, art. 9º-II-e/u (informar divulgação prévia e versões anteriores no ato da submissão); art. 9º-II-g (citar trabalhos anteriores dos autores, prevenindo autoplágio).
_Ação:_ item de _cover letter_ (não necessariamente do texto): declarar o relatório de síntese do Trabalho I e o repositório GitHub como divulgação prévia parcial; garantir que o artigo cite o relatório anterior onde reutiliza material.

### Prioridade BAIXA (robustez e posicionamento)

**A8. Nota de que não há IAP a declarar.**
_Base:_ 3.004, art. 9º (declaração formal de IAP **quando há treinamento de modelos**).
_Ação:_ uma linha na seção A1: a revisão usa estatística clássica (Cohen's κ, Fleiss' κ) e **não treina** modelos de ML; logo não há uso de IAP a declarar. Antecipada a pergunta de um revisor brasileiro.

**A9. Ancorar o protocolo no arcabouço normativo.**
_Base:_ posicionamento, não obrigação.
_Ação:_ em _Methodological lessons for LLM-assisted SLRs_ (Discussion), 1–2 frases observando que o desenho _LLM-assisted, human-decided_ satisfaz as exigências das Portarias CNPq 2.664/2026 e 3.004/2026 (declaração de ferramenta/versão/fase/finalidade; verificação humana não delegada; vedação de conteúdo não publicado), citando-as como referências normativas — transforma conformidade em contribuição.

**A10. Reforço pontual em Threats to Validity.**
_Ação:_ frase curta em _Assistant validity_ remetendo à seção de declaração (A1), fechando o circuito norma → método → ameaças.

## 4. O que **não** requer mudança

- **Art. 8º §1º da 3.004 (vedação ao parecerista)** — não incide: os assistentes processaram **literatura publicada** para fins de RSL, não projetos/propostas de terceiros sob avaliação. A2 deixa isso explícito para evitar leitura apressada.
- **Tabela de versões e rodapé de proveniência** — já conformes ao art. 4º-I; nenhuma alteração além da referência cruzada pela seção A1.
- **Competência apuratória (2.664, arts. 17–25; CIAC)** — institucional; sem reflexo no texto.

## 5. Sequência sugerida de aplicação

1. **A1 + A2 + A3 + A8** — redigir a seção _Declaration of Generative AI Use_ completa (um bloco LaTeX único, antes de `\bibliographystyle`), já com a nota de confidencialidade/LGPD e responsabilização. ⚠️ Depende de: insumo do condutor sobre planos/opt-out (A2) e aprovação do orientador (pendência do Acknowledgment).
2. **A5 + A6** — CRediT e COI no mesmo bloco de fecho.
3. **A4** — montar e depositar o pacote de replicação (Zenodo), obter DOI, escrever _Data Availability_.
4. **A9 + A10** — ajustes na Discussion e em Threats, com as portarias adicionadas a `referencias.bib`.
5. **A7** — checklist de submissão (cover letter).

---

_Este plano não altera artefatos históricos; toda aplicação gera commits próprios e registro no MEMORY.md, conforme as convenções do repositório._
