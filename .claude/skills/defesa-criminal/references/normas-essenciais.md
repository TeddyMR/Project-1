# Normas essenciais: texto conferido

> Texto extraído de fontes oficiais em 24 de novembro de 2026. Confira a redação vigente no Planalto antes de transcrever.

Conferência feita em 24 de novembro de 2026. Todo texto entre aspas foi copiado por script do arquivo indicado, linha a linha. Nada foi completado de memória.

## 1. Origem das fontes

Convenções deste arquivo:

- `cpp.txt:608` significa a linha 608 do arquivo de texto correspondente. Os caminhos completos estão na tabela abaixo.
- As notas entre parênteses, como "(Redação dada pela Lei nº 11.690, de 2008)", fazem parte da página do Planalto. Quando ocupavam linha própria, foram unidas à linha anterior.
- A grafia é a da fonte (por exemplo, "§ 1o", "conseqüência", "Il" no lugar de "II").
- Texto riscado na página do Planalto (redação revogada) não foi copiado, salvo quando indicado.
- No Manual de Redação, extraído de PDF, as quebras de linha foram unidas onde indicado por intervalo de linhas.

Arquivos que já estavam em disco, em `/tmp/claude-0/-home-user-Project-1/9b4f7fbb-f7ad-5d3e-a371-7597fde0d42f/scratchpad/research/_normas/txt/`:

| Arquivo | Norma | Site de origem | Como a origem foi confirmada |
|---|---|---|---|
| `cpp.txt` | Decreto-Lei nº 3.689, de 3 de outubro de 1941 (Código de Processo Penal), texto compilado | Planalto: https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm | O HTML em `_normas/dl/cpp.html` tem título "Del3689Compilado" e cabeçalho da Presidência da República. Baixei a mesma URL hoje: o conteúdo é idêntico, descontado o script do balanceador de carga. |
| `cf.txt` | Constituição de 1988, texto compilado | Planalto: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `d678.txt` | Decreto nº 678, de 6 de novembro de 1992 (Convenção Americana sobre Direitos Humanos) | Planalto: https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `d592.txt` | Decreto nº 592, de 6 de julho de 1992 (Pacto Internacional sobre Direitos Civis e Políticos) | Planalto: https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0592.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `d40.txt` | Decreto nº 40, de 15 de fevereiro de 1991 (Convenção contra a Tortura) | Planalto: https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0040.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `d4463.txt` | Decreto nº 4.463, de 8 de novembro de 2002 (competência da Corte Interamericana) | Planalto: https://www.planalto.gov.br/ccivil_03/decreto/2002/d4463.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `lcp95.txt` | Lei Complementar nº 95, de 26 de fevereiro de 1998 | Planalto: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `d12002.txt` | Decreto nº 12.002, de 22 de abril de 2024 (não estava na lista da tarefa; usado como complemento) | Planalto: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12002.htm | Mesmo método. Conteúdo idêntico ao baixado hoje. |
| `manual.txt` | Manual de Redação da Presidência da República, 3ª edição (2018) | **Não veio do Planalto.** Cópia hospedada pela Universidade Federal da Grande Dourados: https://files.ufgd.edu.br/arquivos/arquivos/78/PROTOCOLO/Normas%20Internas/Manual%20de%20Reda%C3%A7%C3%A3o%20da%20Presid%C3%AAncia%20da%20Rep%C3%BAblica%20-%203%C2%AA%20edi%C3%A7%C3%A3o,%20revista,%20atualizada%20e%20ampliada.pdf | `manual.txt` é idêntico ao resultado de `pdftotext -layout` sobre `_normas/dl/manual_ufgd.pdf`. Esse PDF é idêntico, byte a byte (md5 d34714c3f5f55b034b847f333395b142), ao que baixei hoje da URL da UFGD. Metadados do PDF: autor "Centro de Estudos Jurídicos", 189 páginas, criado em 17.1.2019. O endereço oficial (www4.planalto.gov.br/centrodeestudos/.../manual-de-redacao.pdf) respondeu com erro 503 nesta sessão; `_normas/dl/manual.pdf` é uma página de bloqueio, não o PDF. A Portaria nº 1.369, de 27 de dezembro de 2018, que aprova a 3ª edição, está em `_normas/dl/prt1369.html`. |

Normas que busquei hoje no Planalto, no Senado e no CNJ (HTML e texto em `/tmp/claude-0/-home-user-Project-1/9b4f7fbb-f7ad-5d3e-a371-7597fde0d42f/scratchpad/normas_audit/`, pastas `dl/` e `txt/`):

| Arquivo | Norma | URL aberta (resposta 200) |
|---|---|---|
| `cp.txt` | Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (Código Penal), texto compilado | https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| `cpfull.txt` | Código Penal, texto com as redações anteriores riscadas | https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm |
| `l9296.txt` | Lei nº 9.296, de 24 de julho de 1996 | https://www.planalto.gov.br/ccivil_03/leis/l9296.htm |
| `l12850.txt` | Lei nº 12.850, de 2 de agosto de 2013 | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm |
| `l11343.txt` | Lei nº 11.343, de 23 de agosto de 2006 | https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm |
| `l9099.txt` | Lei nº 9.099, de 26 de setembro de 1995 | https://www.planalto.gov.br/ccivil_03/leis/l9099.htm |
| `l12965.txt` | Lei nº 12.965, de 23 de abril de 2014 | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm |
| `l8906.txt` | Lei nº 8.906, de 4 de julho de 1994 | https://www.planalto.gov.br/ccivil_03/leis/l8906.htm |
| `l12234.txt` | Lei nº 12.234, de 5 de maio de 2010 | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12234.htm |
| `l14365.txt` | Lei nº 14.365, de 2 de junho de 2022 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm |
| `l13964.txt` | Lei nº 13.964, de 24 de dezembro de 2019 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13964.htm |
| `lcp80.txt` | Lei Complementar nº 80, de 12 de janeiro de 1994 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp80.htm |
| `l15160.txt` | Lei nº 15.160, de 3 de julho de 2025 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15160.htm |
| `l15272.txt` | Lei nº 15.272, de 26 de novembro de 2025 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15272.htm |
| `l15358.txt` | Lei nº 15.358, de 24 de março de 2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15358.htm |
| `l15438.txt` | Lei nº 15.438, de 18 de junho de 2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15438.htm |
| `l15487.txt` | Lei nº 15.487, de 6 de agosto de 2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15487.htm |
| `cnj213.txt` | Resolução CNJ nº 213, de 15 de dezembro de 2015 | https://atos.cnj.jus.br/atos/detalhar/2234 |
| `cnj484.txt` | Resolução CNJ nº 484, de 19 de dezembro de 2022 | https://atos.cnj.jus.br/atos/detalhar/4883 |
| `adi6298.txt` | Decisão do STF nas ADIs 6298, 6299, 6300 e 6305 (publicação oficial) | https://legis.senado.leg.br/norma/37567157/publicacao/37567563 |
| `adi6581.txt` | Decisão do STF na ADI 6581 | Texto extraído de `research/_normas/dl/adi6581.html`, que já estava em disco. A URL de origem não consta do arquivo: não confirmada. |

Aviso sobre leis recentes. O texto compilado do Planalto traz alterações de 2025 e 2026 que atingem dispositivos usados nas teses: Lei nº 15.160, de 2025 (CP, art. 115); Lei nº 15.272, de 2025 (CPP, arts. 310 e 312); Lei nº 15.358, de 2026 (CPP, arts. 3º-B, 78, 310 e 313); Lei nº 15.438, de 2026 (CPP, art. 38; CP, art. 103); Lei nº 15.487, de 2026 (CPP, art. 313). Todas entraram em vigor na data da publicação (ver seção 6).

## 2. Código de Processo Penal

Fonte de todos os itens desta seção: `cpp.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm).

### Art. 3º-A

- `cpp.txt:26` — "Art. 3º-A. O processo penal terá estrutura acusatória, vedadas a iniciativa do juiz na fase de investigação e a substituição da atuação probatória do órgão de acusação. (Incluído pela Lei nº 13.964, de 2019) (Vigência) (Vide ADI 6.298) (Vide ADI 6.300) (Vide ADI 6.305)"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019. O STF deu interpretação conforme ao artigo "para assentar que o juiz, pontualmente, nos limites legalmente autorizados, pode determinar a realização de diligências suplementares, para o fim de dirimir dúvida sobre questão relevante para o julgamento do mérito" (item 1 da decisão; ADIs 6298, 6299, 6300 e 6305, Plenário, 24.8.2023, `adi6298.txt:23`, https://legis.senado.leg.br/norma/37567157/publicacao/37567563).

### Art. 41

- `cpp.txt:298` — "Art. 41. A denúncia ou queixa conterá a exposição do fato criminoso, com todas as suas circunstâncias, a qualificação do acusado ou esclarecimentos pelos quais se possa identificá-lo, a classificação do crime e, quando necessário, o rol das testemunhas."

Situação: vigente. Redação original.

### Art. 155

- `cpp.txt:601` — "Art. 155. O juiz formará sua convicção pela livre apreciação da prova produzida em contraditório judicial, não podendo fundamentar sua decisão exclusivamente nos elementos informativos colhidos na investigação, ressalvadas as provas cautelares, não repetíveis e antecipadas. (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:602` — "Parágrafo único. Somente quanto ao estado das pessoas serão observadas as restrições estabelecidas na lei civil. (Incluído pela Lei nº 11.690, de 2008)"

Situação: vigente. Redação da Lei nº 11.690, de 2008.

### Art. 156

- `cpp.txt:604` — "Art. 156. A prova da alegação incumbirá a quem a fizer, sendo, porém, facultado ao juiz de ofício: (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:605` — "I – ordenar, mesmo antes de iniciada a ação penal, a produção antecipada de provas consideradas urgentes e relevantes, observando a necessidade, adequação e proporcionalidade da medida; (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:606` — "II – determinar, no curso da instrução, ou antes de proferir sentença, a realização de diligências para dirimir dúvida sobre ponto relevante. (Incluído pela Lei nº 11.690, de 2008)"

Situação: vigente. Redação da Lei nº 11.690, de 2008.

### Art. 157 (caput, §§ 1º a 3º; situação do § 5º)

- `cpp.txt:608` — "Art. 157. São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas, assim entendidas as obtidas em violação a normas constitucionais ou legais. (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:609` — "§ 1o São também inadmissíveis as provas derivadas das ilícitas, salvo quando não evidenciado o nexo de causalidade entre umas e outras, ou quando as derivadas puderem ser obtidas por uma fonte independente das primeiras. (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:610` — "§ 2o Considera-se fonte independente aquela que por si só, seguindo os trâmites típicos e de praxe, próprios da investigação ou instrução criminal, seria capaz de conduzir ao fato objeto da prova. (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:612` — "§ 3o Preclusa a decisão de desentranhamento da prova declarada inadmissível, esta será inutilizada por decisão judicial, facultado às partes acompanhar o incidente. (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:614` — "§ 4o (VETADO) (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:615` — "§ 5º O juiz que conhecer do conteúdo da prova declarada inadmissível não poderá proferir a sentença ou acórdão. (Incluído pela Lei nº 13.964, de 2019) (Vide ADI 6.298) (Vide ADI 6.299) (Vide ADI 6.300) (Vide ADI 6.305)"

Situação: caput e §§ 1º a 3º vigentes (Lei nº 11.690, de 2008). § 4º vetado. § 5º: incluído pela Lei nº 13.964, de 2019, e declarado inconstitucional pelo STF. Texto da decisão, item 23: "Por maioria, declarar a inconstitucionalidade do § 5º do art. 157 do CPP, incluído pela Lei nº 13.964/2019" (ADIs 6298, 6299, 6300 e 6305, Plenário, 24.8.2023, `adi6298.txt:23`, https://legis.senado.leg.br/norma/37567157/publicacao/37567563). A página do Planalto ainda exibe o § 5º, só com a nota "Vide ADI".

### Art. 158

- `cpp.txt:624` — "Art. 158. Quando a infração deixar vestígios, será indispensável o exame de corpo de delito, direto ou indireto, não podendo supri-lo a confissão do acusado."
- `cpp.txt:625` — "Parágrafo único. Dar-se-á prioridade à realização do exame de corpo de delito quando se tratar de crime que envolva: (Incluído dada pela Lei nº 13.721, de 2018)"
- `cpp.txt:626` — "I - violência doméstica e familiar contra mulher; (Incluído dada pela Lei nº 13.721, de 2018)"
- `cpp.txt:627` — "II - violência contra criança, adolescente, idoso ou pessoa com deficiência. (Incluído dada pela Lei nº 13.721, de 2018)"

Situação: vigente. Caput na redação original. Parágrafo único incluído pela Lei nº 13.721, de 2018.

### Art. 158-A (caput)

- `cpp.txt:628` — "Art. 158-A. Considera-se cadeia de custódia o conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio coletado em locais ou em vítimas de crimes, para rastrear sua posse e manuseio a partir de seu reconhecimento até o descarte. (Incluído pela Lei nº 13.964, de 2019)"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019.

### Art. 158-B (nomes das etapas)

- `cpp.txt:636` — "Art. 158-B. A cadeia de custódia compreende o rastreamento do vestígio nas seguintes etapas: (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:638` — "I - reconhecimento"
- `cpp.txt:640` — "II - isolamento"
- `cpp.txt:642` — "III - fixação"
- `cpp.txt:644` — "IV - coleta"
- `cpp.txt:646` — "V - acondicionamento"
- `cpp.txt:648` — "VI - transporte"
- `cpp.txt:650` — "VII - recebimento"
- `cpp.txt:652` — "VIII - processamento"
- `cpp.txt:654` — "IX - armazenamento"
- `cpp.txt:656` — "X - descarte"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019. Dez etapas, nos incisos I a X. Só o nome de cada etapa foi copiado; a definição completa está nas linhas indicadas. Os arts. 158-C a 158-F começam nas linhas 658, 664, 676 e 686.

### Art. 167

- `cpp.txt:712` — "Art. 167. Não sendo possível o exame de corpo de delito, por haverem desaparecido os vestígios, a prova testemunhal poderá suprir-lhe a falta."

Situação: vigente. Redação original.

### Art. 186

- `cpp.txt:761` — "Art. 186. Depois de devidamente qualificado e cientificado do inteiro teor da acusação, o acusado será informado pelo juiz, antes de iniciar o interrogatório, do seu direito de permanecer calado e de não responder perguntas que lhe forem formuladas. (Redação dada pela Lei nº 10.792, de 1º.12.2003)"
- `cpp.txt:762` — "Parágrafo único. O silêncio, que não importará em confissão, não poderá ser interpretado em prejuízo da defesa. (Incluído pela Lei nº 10.792, de 1º.12.2003)"

Situação: vigente. Redação da Lei nº 10.792, de 2003.

### Art. 197

- `cpp.txt:788` — "Art. 197. O valor da confissão se aferirá pelos critérios adotados para os outros elementos de prova, e para a sua apreciação o juiz deverá confrontá-la com as demais provas do processo, verificando se entre ela e estas existe compatibilidade ou concordância."

Situação: vigente. Redação original.

### Art. 212

- `cpp.txt:822` — "Art. 212. As perguntas serão formuladas pelas partes diretamente à testemunha, não admitindo o juiz aquelas que puderem induzir a resposta, não tiverem relação com a causa ou importarem na repetição de outra já respondida. (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:824` — "Parágrafo único. Sobre os pontos não esclarecidos, o juiz poderá complementar a inquirição. (Incluído pela Lei nº 11.690, de 2008)"

Situação: vigente. Redação da Lei nº 11.690, de 2008.

### Art. 226

- `cpp.txt:853` — "Art. 226. Quando houver necessidade de fazer-se o reconhecimento de pessoa, proceder-se-á pela seguinte forma:"
- `cpp.txt:854` — "I - a pessoa que tiver de fazer o reconhecimento será convidada a descrever a pessoa que deva ser reconhecida;"
- `cpp.txt:855` — "Il - a pessoa, cujo reconhecimento se pretender, será colocada, se possível, ao lado de outras que com ela tiverem qualquer semelhança, convidando-se quem tiver de fazer o reconhecimento a apontá-la;"
- `cpp.txt:856` — "III - se houver razão para recear que a pessoa chamada para o reconhecimento, por efeito de intimidação ou outra influência, não diga a verdade em face da pessoa que deve ser reconhecida, a autoridade providenciará para que esta não veja aquela;"
- `cpp.txt:857` — "IV - do ato de reconhecimento lavrar-se-á auto pormenorizado, subscrito pela autoridade, pela pessoa chamada para proceder ao reconhecimento e por duas testemunhas presenciais."
- `cpp.txt:858` — "Parágrafo único. O disposto no no III deste artigo não terá aplicação na fase da instrução criminal ou em plenário de julgamento."

Situação: vigente. Redação original.

### Art. 244

- `cpp.txt:902` — "Art. 244. A busca pessoal independerá de mandado, no caso de prisão ou quando houver fundada suspeita de que a pessoa esteja na posse de arma proibida ou de objetos ou papéis que constituam corpo de delito, ou quando a medida for determinada no curso de busca domiciliar."

Situação: vigente. Redação original. O art. 240, § 2º, está em `cpp.txt:893`.

### Art. 261

- `cpp.txt:955` — "Art. 261. Nenhum acusado, ainda que ausente ou foragido, será processado ou julgado sem defensor."
- `cpp.txt:956` — "Parágrafo único. A defesa técnica, quando realizada por defensor público ou dativo, será sempre exercida através de manifestação fundamentada. (Incluído pela Lei nº 10.792, de 1º.12.2003)"

Situação: vigente. Caput na redação original. Parágrafo único incluído pela Lei nº 10.792, de 2003.

### Art. 282, §§ 2º e 6º

- `cpp.txt:1005` — "§ 2º As medidas cautelares serão decretadas pelo juiz a requerimento das partes ou, quando no curso da investigação criminal, por representação da autoridade policial ou mediante requerimento do Ministério Público. (Redação dada pela Lei nº 13.964, de 2019)"
- `cpp.txt:1013` — "§ 6º A prisão preventiva somente será determinada quando não for cabível a sua substituição por outra medida cautelar, observado o art. 319 deste Código, e o não cabimento da substituição por outra medida cautelar deverá ser justificado de forma fundamentada nos elementos presentes do caso concreto, de forma individualizada. (Redação dada pela Lei nº 13.964, de 2019)"

Situação: vigentes. Redação da Lei nº 13.964, de 2019.

### Art. 310 (caput e § 4º; parágrafos novos)

- `cpp.txt:1111` — "Art. 310. Após receber o auto de prisão em flagrante, no prazo máximo de até 24 (vinte e quatro) horas após a realização da prisão, o juiz deverá promover, por meio de videoconferência em tempo real, audiência de custódia com a presença do acusado, seu advogado constituído ou membro da Defensoria Pública e o membro do Ministério Público, e, nessa audiência, o juiz deverá, fundamentadamente: (Redação dada pela Lei nº 15.358, de 2026)"
- `cpp.txt:1112` — "I - relaxar a prisão ilegal; ou (Incluído pela Lei nº 12.403, de 2011)."
- `cpp.txt:1113` — "II - converter a prisão em flagrante em preventiva, quando presentes os requisitos constantes do art. 312 deste Código, e se revelarem inadequadas ou insuficientes as medidas cautelares diversas da prisão; ou (Incluído pela Lei nº 12.403, de 2011)."
- `cpp.txt:1114` — "III - conceder liberdade provisória, com ou sem fiança. (Incluído pela Lei nº 12.403, de 2011)."
- `cpp.txt:1121` — "§ 4º Transcorridas 24 (vinte e quatro) horas após o decurso do prazo estabelecido no caput deste artigo, a não realização de audiência de custódia sem motivação idônea ensejará também a ilegalidade da prisão, a ser relaxada pela autoridade competente, sem prejuízo da possibilidade de imediata decretação de prisão preventiva. (Incluído pela Lei nº 13.964, de 2019) (Vigência) (Vide ADI 6.298) (Vide ADI 6.300) (Vide ADI 6.305)"
- `cpp.txt:1132` — "§ 6º A decisão de que trata o caput deste artigo deve ser motivada e fundamentada, sendo obrigatório o exame, pelo juiz, das circunstâncias previstas nos §§ 2º e 5º deste artigo e dos critérios de periculosidade previstos no § 3º do art. 312. (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1133` — "§ 7º Antes do início da audiência de custódia, deverá a serventia judicial conferir os processos criminais a que responde o acusado e, constatada pendência de citação em qualquer deles, informar ao juiz, que certificará a ocorrência e procederá a citação pessoal do acusado, comunicando de imediato o juízo competente. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1134` — "§ 8º Na audiência de custódia por videoconferência, serão facultados todos os mecanismos para intervenção da defesa técnica e do Ministério Público, que poderão suscitar questões de ordem. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1135` — "§ 9º Será garantido o direito de entrevista prévia, reservada e inviolável entre o preso e o seu defensor, presencialmente, por videoconferência ou por qualquer outro meio de comunicação. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1136` — "§ 10. Deverá ser assegurada privacidade ao preso na sala em que se realizar a videoconferência, devendo permanecer sozinho durante a realização de sua oitiva, ressalvada a possibilidade de presença física de seu defensor no ambiente. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1137` — "§ 11. No caso de qualquer falha no sistema de comunicações cuja causa seja atribuível ao tribunal, por questões internas ou decorrente dos provedores de serviço que o tribunal tenha contratado, é obrigatória a repetição completa da audiência, sem convalescer qualquer ato incompleto. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1138` — "§ 12. Todos os estabelecimentos prisionais terão salas próprias, com disponibilização de mecanismos de videoconferência estáveis, para a realização das audiências de custódia. (Incluído pela Lei nº 15.358, de 2026)"
- `cpp.txt:1139` — "§ 13. Em situações excepcionais decorrentes de força maior, poderá a audiência de custódia ser realizada presencialmente, mediante decisão justificada do juiz competente, vedada a hipótese se o ato se revelar demasiadamente custoso ou trouxer excessivo risco à segurança social ou à segurança física do detido. (Incluído pela Lei nº 15.358, de 2026)"

Situação: caput **alterado pela Lei nº 15.358, de 24 de março de 2026** (DOU de 25.3.2026; vigência na publicação): a audiência de custódia passou a ser promovida "por meio de videoconferência em tempo real". Incisos I a III: Lei nº 12.403, de 2011. § 4º: incluído pela Lei nº 13.964, de 2019; o STF deu interpretação conforme "para assentar que a autoridade judiciária deverá avaliar se estão presentes os requisitos para a prorrogação excepcional do prazo ou para sua realização por videoconferência, sem prejuízo da possibilidade de imediata decretação de prisão preventiva" (item 25 da decisão; ADIs 6298, 6299, 6300 e 6305, Plenário, 24.8.2023, `adi6298.txt:23`, https://legis.senado.leg.br/norma/37567157/publicacao/37567563). §§ 5º e 6º: incluídos pela Lei nº 15.272, de 26 de novembro de 2025 (o § 5º está em `cpp.txt:1125-1131`). §§ 7º a 13: incluídos pela Lei nº 15.358, de 2026. O art. 3º-B, § 1º, também foi alterado pela Lei nº 15.358, de 2026 (`cpp.txt:76-77`).

### Art. 311

- `cpp.txt:1146` — "Art. 311. Em qualquer fase da investigação policial ou do processo penal, caberá a prisão preventiva decretada pelo juiz, a requerimento do Ministério Público, do querelante ou do assistente, ou por representação da autoridade policial. (Redação dada pela Lei nº 13.964, de 2019)"

Situação: vigente. Redação da Lei nº 13.964, de 2019.

### Art. 312 (caput e § 2º; §§ 3º e 4º novos)

- `cpp.txt:1148` — "Art. 312. A prisão preventiva poderá ser decretada como garantia da ordem pública, da ordem econômica, por conveniência da instrução criminal ou para assegurar a aplicação da lei penal, quando houver prova da existência do crime e indício suficiente de autoria e de perigo gerado pelo estado de liberdade do imputado. (Redação dada pela Lei nº 13.964, de 2019)"
- `cpp.txt:1151` — "§ 2º A decisão que decretar a prisão preventiva deve ser motivada e fundamentada em receio de perigo e existência concreta de fatos novos ou contemporâneos que justifiquem a aplicação da medida adotada. (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1153` — "§ 3º Devem ser considerados na aferição da periculosidade do agente, geradora de riscos à ordem pública: (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1154` — "I – o modus operandi, inclusive quanto ao uso reiterado de violência ou grave ameaça à pessoa ou quanto à premeditação do agente para a prática delituosa; (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1155` — "II – a participação em organização criminosa; (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1156` — "III – a natureza, a quantidade e a variedade de drogas, armas ou munições apreendidas; ou (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1157` — "IV – o fundado receio de reiteração delitiva, inclusive à vista da existência de outros inquéritos e ações penais em curso. (Incluído pela Leinº 15.272, de 2025)"
- `cpp.txt:1158` — "§ 4º É incabível a decretação da prisão preventiva com base em alegações de gravidade abstrata do delito, devendo ser concretamente demonstrados a periculosidade do agente e seu risco à ordem pública, à ordem econômica, à regularidade da instrução criminal e à aplicação da lei penal, conforme o caso. (Incluído pela Leinº 15.272, de 2025)"

Situação: caput e § 2º vigentes (Lei nº 13.964, de 2019). §§ 3º e 4º **incluídos pela Lei nº 15.272, de 26 de novembro de 2025** (DOU de 27.11.2025; vigência na publicação).

### Art. 313, § 2º

- `cpp.txt:1169` — "§ 2º Não será admitida a decretação da prisão preventiva com a finalidade de antecipação de cumprimento de pena ou como decorrência imediata de investigação criminal ou da apresentação ou recebimento de denúncia. (Incluído pela Lei nº 13.964, de 2019)"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019. O caput do art. 313 ganhou o inciso V (Lei nº 15.358, de 2026, `cpp.txt:1164-1165`) e o inciso VI (Lei nº 15.487, de 2026, `cpp.txt:1166-1167`).

### Art. 315, § 2º

- `cpp.txt:1176` — "§ 2º Não se considera fundamentada qualquer decisão judicial, seja ela interlocutória, sentença ou acórdão, que: (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1178` — "I - limitar-se à indicação, à reprodução ou à paráfrase de ato normativo, sem explicar sua relação com a causa ou a questão decidida; (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1180` — "II - empregar conceitos jurídicos indeterminados, sem explicar o motivo concreto de sua incidência no caso; (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1182` — "III - invocar motivos que se prestariam a justificar qualquer outra decisão; (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1184` — "IV - não enfrentar todos os argumentos deduzidos no processo capazes de, em tese, infirmar a conclusão adotada pelo julgador; (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1186` — "V - limitar-se a invocar precedente ou enunciado de súmula, sem identificar seus fundamentos determinantes nem demonstrar que o caso sob julgamento se ajusta àqueles fundamentos; (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:1188` — "VI - deixar de seguir enunciado de súmula, jurisprudência ou precedente invocado pela parte, sem demonstrar a existência de distinção no caso em julgamento ou a superação do entendimento. (Incluído pela Lei nº 13.964, de 2019)"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019.

### Art. 316, parágrafo único

- `cpp.txt:1192` — "Parágrafo único. Decretada a prisão preventiva, deverá o órgão emissor da decisão revisar a necessidade de sua manutenção a cada 90 (noventa) dias, mediante decisão fundamentada, de ofício, sob pena de tornar a prisão ilegal. (Incluído pela Lei nº 13.964, de 2019) (Vigência) (Vide ADI 6581) (Vide ADI 6582)"

Situação: vigente. Incluído pela Lei nº 13.964, de 2019. O STF deu interpretação conforme na ADI 6581 (Plenário, sessão virtual de 25.2.2022 a 8.3.2022): "a inobservância da reavaliação prevista no parágrafo único do artigo 316 do Código de Processo Penal (CPP), com a redação dada pela Lei 13.964/2019, após o prazo legal de 90 (noventa) dias, não implica a revogação automática da prisão preventiva, devendo o juízo competente ser instado a reavaliar a legalidade e a atualidade de seus fundamentos" (`adi6581.txt:24`; URL de origem do arquivo não confirmada).

### Art. 363

- `cpp.txt:1392` — "Art. 363. O processo terá completada a sua formação quando realizada a citação do acusado. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1394` — "I - (revogado); (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1396` — "II - (revogado). (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1398` — "§ 1o Não sendo encontrado o acusado, será procedida a citação por edital. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1399` — "§ 2o (VETADO) (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1401` — "§ 3o (VETADO) (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1403` — "§ 4o Comparecendo o acusado citado por edital, em qualquer tempo, o processo observará o disposto nos arts. 394 e seguintes deste Código. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008. Incisos I e II revogados. §§ 2º e 3º vetados.

### Art. 366

- `cpp.txt:1412` — "Art. 366. Se o acusado, citado por edital, não comparecer, nem constituir advogado, ficarão suspensos o processo e o curso do prazo prescricional, podendo o juiz determinar a produção antecipada das provas consideradas urgentes e, se for o caso, decretar prisão preventiva, nos termos do disposto no art. 312. (Redação dada pela Lei nº 9.271, de 17.4.1996)"
- `cpp.txt:1413` — "§ 1o (Revogado pela Lei nº 11.719, de 2008)."
- `cpp.txt:1414` — "§ 2o (Revogado pela Lei nº 11.719, de 2008)."

Situação: vigente. Caput na redação da Lei nº 9.271, de 1996. §§ 1º e 2º revogados pela Lei nº 11.719, de 2008.

### Art. 370

- `cpp.txt:1420` — "Art. 370. Nas intimações dos acusados, das testemunhas e demais pessoas que devam tomar conhecimento de qualquer ato, será observado, no que for aplicável, o disposto no Capítulo anterior. (Redação dada pela Lei nº 9.271, de 17.4.1996)"
- `cpp.txt:1421` — "§ 1o A intimação do defensor constituído, do advogado do querelante e do assistente far-se-á por publicação no órgão incumbido da publicidade dos atos judiciais da comarca, incluindo, sob pena de nulidade, o nome do acusado. (Incluído Lei nº 9.271, de 17.4.1996)"
- `cpp.txt:1422` — "§ 2o Caso não haja órgão de publicação dos atos judiciais na comarca, a intimação far-se-á diretamente pelo escrivão, por mandado, ou via postal com comprovante de recebimento, ou por qualquer outro meio idôneo. (Redação dada pela Lei nº 9.271, de 17.4.1996)"
- `cpp.txt:1423` — "§ 3o A intimação pessoal, feita pelo escrivão, dispensará a aplicação a que alude o"
- `cpp.txt:1424` — "§ 1o. (Incluído pela Lei nº 9.271, de 17.4.1996)"
- `cpp.txt:1425` — "§ 4o A intimação do Ministério Público e do defensor nomeado será pessoal. (Incluído pela Lei nº 9.271, de 17.4.1996)"

Situação: vigente. Redação da Lei nº 9.271, de 1996. Na fonte, o § 3º está partido em duas linhas (1423 e 1424).

### Art. 383

- `cpp.txt:1462` — "Art. 383. O juiz, sem modificar a descrição do fato contida na denúncia ou queixa, poderá atribuir-lhe definição jurídica diversa, ainda que, em conseqüência, tenha de aplicar pena mais grave. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1464` — "§ 1o Se, em conseqüência de definição jurídica diversa, houver possibilidade de proposta de suspensão condicional do processo, o juiz procederá de acordo com o disposto na lei. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1466` — "§ 2o Tratando-se de infração da competência de outro juízo, a este serão encaminhados os autos. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 384 (caput; § 2º como complemento)

- `cpp.txt:1467` — "Art. 384. Encerrada a instrução probatória, se entender cabível nova definição jurídica do fato, em conseqüência de prova existente nos autos de elemento ou circunstância da infração penal não contida na acusação, o Ministério Público deverá aditar a denúncia ou queixa, no prazo de 5 (cinco) dias, se em virtude desta houver sido instaurado o processo em crime de ação pública, reduzindo-se a termo o aditamento, quando feito oralmente. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1471` — "§ 2o Ouvido o defensor do acusado no prazo de 5 (cinco) dias e admitido o aditamento, o juiz, a requerimento de qualquer das partes, designará dia e hora para continuação da audiência, com inquirição de testemunhas, novo interrogatório do acusado, realização de debates e julgamento. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008. No caput, o sujeito de "se entender cabível" é o Ministério Público.

### Art. 386

- `cpp.txt:1481` — "Art. 386. O juiz absolverá o réu, mencionando a causa na parte dispositiva, desde que reconheça:"
- `cpp.txt:1482` — "I - estar provada a inexistência do fato;"
- `cpp.txt:1483` — "II - não haver prova da existência do fato;"
- `cpp.txt:1484` — "III - não constituir o fato infração penal;"
- `cpp.txt:1485` — "IV – estar provado que o réu não concorreu para a infração penal; (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:1486` — "V – não existir prova de ter o réu concorrido para a infração penal; (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:1487` — "VI – existirem circunstâncias que excluam o crime ou isentem o réu de pena (arts. 20, 21, 22, 23, 26 e § 1º do art. 28, todos do Código Penal), ou mesmo se houver fundada dúvida sobre sua existência; (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:1488` — "VII – não existir prova suficiente para a condenação. (Incluído pela Lei nº 11.690, de 2008)"
- `cpp.txt:1489` — "Parágrafo único. Na sentença absolutória, o juiz:"
- `cpp.txt:1490` — "I - mandará, se for o caso, pôr o réu em liberdade;"
- `cpp.txt:1491` — "II – ordenará a cessação das medidas cautelares e provisoriamente aplicadas; (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:1493` — "III - aplicará medida de segurança, se cabível."

Situação: vigente. Incisos IV a VII e inciso II do parágrafo único na redação da Lei nº 11.690, de 2008.

### Art. 395

- `cpp.txt:1545` — "Art. 395. A denúncia ou queixa será rejeitada quando: (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1547` — "I - for manifestamente inepta; (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1548` — "II - faltar pressuposto processual ou condição para o exercício da ação penal; ou (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1549` — "III - faltar justa causa para o exercício da ação penal. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1550` — "Parágrafo único. (Revogado). (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008. Parágrafo único revogado.

### Art. 396

- `cpp.txt:1552` — "Art. 396. Nos procedimentos ordinário e sumário, oferecida a denúncia ou queixa, o juiz, se não a rejeitar liminarmente, recebê-la-á e ordenará a citação do acusado para responder à acusação, por escrito, no prazo de 10 (dez) dias. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1554` — "Parágrafo único. No caso de citação por edital, o prazo para a defesa começará a fluir a partir do comparecimento pessoal do acusado ou do defensor constituído. (Redação dada pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 396-A

- `cpp.txt:1556` — "Art. 396-A. Na resposta, o acusado poderá argüir preliminares e alegar tudo o que interesse à sua defesa, oferecer documentos e justificações, especificar as provas pretendidas e arrolar testemunhas, qualificando-as e requerendo sua intimação, quando necessário. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1558` — "§ 1o A exceção será processada em apartado, nos termos dos arts. 95 a 112 deste Código. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1560` — "§ 2o Não apresentada a resposta no prazo legal, ou se o acusado, citado, não constituir defensor, o juiz nomeará defensor para oferecê-la, concedendo-lhe vista dos autos por 10 (dez) dias. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Incluído pela Lei nº 11.719, de 2008.

### Art. 397

- `cpp.txt:1562` — "Art. 397. Após o cumprimento do disposto no art. 396-A, e parágrafos, deste Código, o juiz deverá absolver sumariamente o acusado quando verificar: (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1564` — "I - a existência manifesta de causa excludente da ilicitude do fato; (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1565` — "II - a existência manifesta de causa excludente da culpabilidade do agente, salvo inimputabilidade; (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1566` — "III - que o fato narrado evidentemente não constitui crime; ou (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1567` — "IV - extinta a punibilidade do agente. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 400 (caput e § 1º)

- `cpp.txt:1573` — "Art. 400. Na audiência de instrução e julgamento, a ser realizada no prazo máximo de 60 (sessenta) dias, proceder-se-á à tomada de declarações do ofendido, à inquirição das testemunhas arroladas pela acusação e pela defesa, nesta ordem, ressalvado o disposto no art. 222 deste Código, bem como aos esclarecimentos dos peritos, às acareações e ao reconhecimento de pessoas e coisas, interrogando-se, em seguida, o acusado. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1575` — "§ 1o As provas serão produzidas numa só audiência, podendo o juiz indeferir as consideradas irrelevantes, impertinentes ou protelatórias. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 401

- `cpp.txt:1585` — "Art. 401. Na instrução poderão ser inquiridas até 8 (oito) testemunhas arroladas pela acusação e 8 (oito) pela defesa. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1587` — "§ 1o Nesse número não se compreendem as que não prestem compromisso e as referidas. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1588` — "§ 2o A parte poderá desistir da inquirição de qualquer das testemunhas arroladas, ressalvado o disposto no art. 209 deste Código. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 402

- `cpp.txt:1590` — "Art. 402. Produzidas as provas, ao final da audiência, o Ministério Público, o querelante e o assistente e, a seguir, o acusado poderão requerer diligências cuja necessidade se origine de circunstâncias ou fatos apurados na instrução. (Redação dada pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 403

- `cpp.txt:1592` — "Art. 403. Não havendo requerimento de diligências, ou sendo indeferido, serão oferecidas alegações finais orais por 20 (vinte) minutos, respectivamente, pela acusação e pela defesa, prorrogáveis por mais 10 (dez), proferindo o juiz, a seguir, sentença. (Redação dada pela Lei nº 11.719, de 2008)."
- `cpp.txt:1594` — "§ 1o Havendo mais de um acusado, o tempo previsto para a defesa de cada um será individual. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1595` — "§ 2o Ao assistente do Ministério Público, após a manifestação desse, serão concedidos 10 (dez) minutos, prorrogando-se por igual período o tempo de manifestação da defesa. (Incluído pela Lei nº 11.719, de 2008)."
- `cpp.txt:1596` — "§ 3o O juiz poderá, considerada a complexidade do caso ou o número de acusados, conceder às partes o prazo de 5 (cinco) dias sucessivamente para a apresentação de memoriais. Nesse caso, terá o prazo de 10 (dez) dias para proferir a sentença. (Incluído pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 532

- `cpp.txt:2156` — "Art. 532. Na instrução, poderão ser inquiridas até 5 (cinco) testemunhas arroladas pela acusação e 5 (cinco) pela defesa. (Redação dada pela Lei nº 11.719, de 2008)."

Situação: vigente. Redação da Lei nº 11.719, de 2008.

### Art. 563

- `cpp.txt:2244` — "Art. 563. Nenhum ato será declarado nulo, se da nulidade não resultar prejuízo para a acusação ou para a defesa."

Situação: vigente. Redação original.

### Art. 564 (inteiro)

- `cpp.txt:2245` — "Art. 564. A nulidade ocorrerá nos seguintes casos:"
- `cpp.txt:2246` — "I - por incompetência, suspeição ou suborno do juiz;"
- `cpp.txt:2247` — "II - por ilegitimidade de parte;"
- `cpp.txt:2248` — "III - por falta das fórmulas ou dos termos seguintes:"
- `cpp.txt:2249` — "a) a denúncia ou a queixa e a representação e, nos processos de contravenções penais, a portaria ou o auto de prisão em flagrante;"
- `cpp.txt:2250` — "b) o exame do corpo de delito nos crimes que deixam vestígios, ressalvado o disposto no Art. 167;"
- `cpp.txt:2251` — "c) a nomeação de defensor ao réu presente, que o não tiver, ou ao ausente, e de curador ao menor de 21 anos;"
- `cpp.txt:2252` — "d) a intervenção do Ministério Público em todos os termos da ação por ele intentada e nos da intentada pela parte ofendida, quando se tratar de crime de ação pública;"
- `cpp.txt:2253` — "e) a citação do réu para ver-se processar, o seu interrogatório, quando presente, e os prazos concedidos à acusação e à defesa;"
- `cpp.txt:2254` — "f) a sentença de pronúncia, o libelo e a entrega da respectiva cópia, com o rol de testemunhas, nos processos perante o Tribunal do Júri;"
- `cpp.txt:2255` — "g) a intimação do réu para a sessão de julgamento, pelo Tribunal do Júri, quando a lei não permitir o julgamento à revelia;"
- `cpp.txt:2256` — "h) a intimação das testemunhas arroladas no libelo e na contrariedade, nos termos estabelecidos pela lei;"
- `cpp.txt:2257` — "i) a presença pelo menos de 15 jurados para a constituição do júri;"
- `cpp.txt:2258` — "j) o sorteio dos jurados do conselho de sentença em número legal e sua incomunicabilidade;"
- `cpp.txt:2259` — "k) os quesitos e as respectivas respostas;"
- `cpp.txt:2260` — "l) a acusação e a defesa, na sessão de julgamento;"
- `cpp.txt:2261` — "m) a sentença;"
- `cpp.txt:2262` — "n) o recurso de oficio, nos casos em que a lei o tenha estabelecido;"
- `cpp.txt:2263` — "o) a intimação, nas condições estabelecidas pela lei, para ciência de sentenças e despachos de que caiba recurso;"
- `cpp.txt:2264` — "p) no Supremo Tribunal Federal e nos Tribunais de Apelação, o quorum legal para o julgamento;"
- `cpp.txt:2265` — "IV - por omissão de formalidade que constitua elemento essencial do ato."
- `cpp.txt:2266` — "V - em decorrência de decisão carente de fundamentação. (Incluído pela Lei nº 13.964, de 2019)"
- `cpp.txt:2268` — "Parágrafo único. Ocorrerá ainda a nulidade, por deficiência dos quesitos ou das suas respostas, e contradição entre estas. (Incluído pela Lei nº 263, de 23.2.1948)"

Situação: vigente. Inciso V incluído pela Lei nº 13.964, de 2019. Parágrafo único incluído pela Lei nº 263, de 1948. O inciso I menciona incompetência, suspeição e suborno; não menciona impedimento.

### Art. 565

- `cpp.txt:2269` — "Art. 565. Nenhuma das partes poderá argüir nulidade a que haja dado causa, ou para que tenha concorrido, ou referente a formalidade cuja observância só à parte contrária interesse."

Situação: vigente. Redação original.

### Art. 566

- `cpp.txt:2270` — "Art. 566. Não será declarada a nulidade de ato processual que não houver influído na apuração da verdade substancial ou na decisão da causa."

Situação: vigente. Redação original.

### Art. 567

- `cpp.txt:2271` — "Art. 567. A incompetência do juízo anula somente os atos decisórios, devendo o processo, quando for declarada a nulidade, ser remetido ao juiz competente."

Situação: vigente. Redação original.

### Art. 569

- `cpp.txt:2273` — "Art. 569. As omissões da denúncia ou da queixa, da representação, ou, nos processos das contravenções penais, da portaria ou do auto de prisão em flagrante, poderão ser supridas a todo o tempo, antes da sentença final."

Situação: vigente. Redação original.

### Art. 570

- `cpp.txt:2274` — "Art. 570. A falta ou a nulidade da citação, da intimação ou notificação estará sanada, desde que o interessado compareça, antes de o ato consumar-se, embora declare que o faz para o único fim de argüi-la. O juiz ordenará, todavia, a suspensão ou o adiamento do ato, quando reconhecer que a irregularidade poderá prejudicar direito da parte."

Situação: vigente. Redação original.

### Art. 571

- `cpp.txt:2275` — "Art. 571. As nulidades deverão ser argüidas:"
- `cpp.txt:2276` — "I - as da instrução criminal dos processos da competência do júri, nos prazos a que se refere o art. 406;"
- `cpp.txt:2277` — "II - as da instrução criminal dos processos de competência do juiz singular e dos processos especiais, salvo os dos Capítulos V e Vll do Título II do Livro II, nos prazos a que se refere o art. 500;"
- `cpp.txt:2278` — "III - as do processo sumário, no prazo a que se refere o art. 537, ou, se verificadas depois desse prazo, logo depois de aberta a audiência e apregoadas as partes;"
- `cpp.txt:2279` — "IV - as do processo regulado no Capítulo VII do Título II do Livro II, logo depois de aberta a audiência;"
- `cpp.txt:2280` — "V - as ocorridas posteriormente à pronúncia, logo depois de anunciado o julgamento e apregoadas as partes (art. 447);"
- `cpp.txt:2281` — "VI - as de instrução criminal dos processos de competência do Supremo Tribunal Federal e dos Tribunais de Apelação, nos prazos a que se refere o art. 500;"
- `cpp.txt:2282` — "VII - se verificadas após a decisão da primeira instância, nas razões de recurso ou logo depois de anunciado o julgamento do recurso e apregoadas as partes;"
- `cpp.txt:2283` — "VIII - as do julgamento em plenário, em audiência ou em sessão do tribunal, logo depois de ocorrerem."

Situação: vigente na redação original. Os incisos II, III e VI remetem aos arts. 500 e 537, que a página registra como revogados pela Lei nº 11.719, de 2008 (`cpp.txt:2091` e `cpp.txt:2178`). O inciso I remete ao art. 406, cuja redação atual é da Lei nº 11.689, de 2008 (`cpp.txt:1609`).

### Art. 572

- `cpp.txt:2284` — "Art. 572. As nulidades previstas no art. 564, Ill, d e e, segunda parte, g e h, e IV, considerar-se-ão sanadas:"
- `cpp.txt:2285` — "I - se não forem argüidas, em tempo oportuno, de acordo com o disposto no artigo anterior;"
- `cpp.txt:2286` — "II - se, praticado por outra forma, o ato tiver atingido o seu fim;"
- `cpp.txt:2287` — "III - se a parte, ainda que tacitamente, tiver aceito os seus efeitos."

Situação: vigente. Redação original.

### Art. 573

- `cpp.txt:2288` — "Art. 573. Os atos, cuja nulidade não tiver sido sanada, na forma dos artigos anteriores, serão renovados ou retificados."
- `cpp.txt:2289` — "§ 1o A nulidade de um ato, uma vez declarada, causará a dos atos que dele diretamente dependam ou sejam conseqüência."
- `cpp.txt:2290` — "§ 2o O juiz que pronunciar a nulidade declarará os atos a que ela se estende."

Situação: vigente. Redação original.

### Art. 647

- `cpp.txt:2490` — "Art. 647. Dar-se-á habeas corpus sempre que alguém sofrer ou se achar na iminência de sofrer violência ou coação ilegal na sua liberdade de ir e vir, salvo nos casos de punição disciplinar."

Situação: vigente. Redação original. O art. 647-A foi incluído pela Lei nº 14.836, de 2024 (`cpp.txt:2491-2492`).

### Art. 648

- `cpp.txt:2493` — "Art. 648. A coação considerar-se-á ilegal:"
- `cpp.txt:2494` — "I - quando não houver justa causa;"
- `cpp.txt:2495` — "II - quando alguém estiver preso por mais tempo do que determina a lei;"
- `cpp.txt:2496` — "III - quando quem ordenar a coação não tiver competência para fazê-lo;"
- `cpp.txt:2497` — "IV - quando houver cessado o motivo que autorizou a coação;"
- `cpp.txt:2498` — "V - quando não for alguém admitido a prestar fiança, nos casos em que a lei a autoriza;"
- `cpp.txt:2499` — "VI - quando o processo for manifestamente nulo;"
- `cpp.txt:2500` — "VII - quando extinta a punibilidade."

Situação: vigente. Redação original.

### Art. 654 (caput, §§ 1º e 2º)

- `cpp.txt:2512` — "Art. 654. O habeas corpus poderá ser impetrado por qualquer pessoa, em seu favor ou de outrem, bem como pelo Ministério Público."
- `cpp.txt:2513` — "§ 1o A petição de habeas corpus conterá:"
- `cpp.txt:2514` — "a) o nome da pessoa que sofre ou está ameaçada de sofrer violência ou coação e o de quem exercer a violência, coação ou ameaça;"
- `cpp.txt:2515` — "b) a declaração da espécie de constrangimento ou, em caso de simples ameaça de coação, as razões em que funda o seu temor;"
- `cpp.txt:2516` — "c) a assinatura do impetrante, ou de alguém a seu rogo, quando não souber ou não puder escrever, e a designação das respectivas residências."
- `cpp.txt:2517` — "§ 2o Os juízes e os tribunais têm competência para expedir de ofício ordem de habeas corpus, quando no curso de processo verificarem que alguém sofre ou está na iminência de sofrer coação ilegal."

Situação: vigente. Redação original.

### Art. 798 (caput, §§ 1º e 3º)

- `cpp.txt:2871` — "Art. 798. Todos os prazos correrão em cartório e serão contínuos e peremptórios, não se interrompendo por férias, domingo ou dia feriado."
- `cpp.txt:2872` — "§ 1o Não se computará no prazo o dia do começo, incluindo-se, porém, o do vencimento."
- `cpp.txt:2874` — "§ 3o O prazo que terminar em domingo ou dia feriado considerar-se-á prorrogado até o dia útil imediato."

Situação: vigente. Redação original.

### Art. 798-A (inteiro)

- `cpp.txt:2880` — "Art. 798-A. Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive, salvo nos seguintes casos: (Incluído pela Lei nº 14.365, de 2022)"
- `cpp.txt:2882` — "I - que envolvam réus presos, nos processos vinculados a essas prisões; (Incluído pela Lei nº 14.365, de 2022)"
- `cpp.txt:2884` — "II - nos procedimentos regidos pela Lei nº 11.340, de 7 de agosto de 2006 (Lei Maria da Penha); (Incluído pela Lei nº 14.365, de 2022)"
- `cpp.txt:2886` — "III - nas medidas consideradas urgentes, mediante despacho fundamentado do juízo competente. (Incluído pela Lei nº 14.365, de 2022)"
- `cpp.txt:2888` — "Parágrafo único. Durante o período a que se refere o caput deste artigo, fica vedada a realização de audiências e de sessões de julgamento, salvo nas hipóteses dos incisos I, II e III do caput deste artigo. (Incluído pela Lei nº 14.365, de 2022)"

Situação: vigente. O artigo existe. Incluído pela Lei nº 14.365, de 2 de junho de 2022 (art. 4º; DOU de 3.6.2022; vigência na publicação: `l14365.txt:162-168` e `l14365.txt:175`).

### Outros dispositivos do CPP usados na auditoria

- `cpp.txt:76` — "§ 1º O preso em flagrante ou por força de mandado de prisão provisória será encaminhado à presença do juiz competente para celebração da audiência de custódia no prazo de 24 (vinte e quatro) horas, momento em que se realizará, por videoconferência, audiência com a presença do Ministério Público e da Defensoria Pública ou de advogado constituído, na forma estabelecida no art. 310 deste Código. (Redação dada pela Lei nº 15.358, de 2026)"
- `cpp.txt:286` — "Art. 38. Salvo disposição em contrário, o ofendido, ou seu representante legal, decairá no direito de queixa ou de representação, se não o exercer dentro do prazo de seis meses, contado do dia em que vier a saber quem é o autor do crime, ou, no caso do art. 29, do dia em que se esgotar o prazo para o oferecimento da denúncia."
- `cpp.txt:287` — "§ 1º Verificar-se-á a decadência do direito de queixa ou representação, dentro do mesmo prazo, nos casos dos arts. 24, parágrafo único, e 31. (Redação dada pela Lei nº 15.438, de 2026)"
- `cpp.txt:289` — "§ 2º Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decairá do direito de queixa ou de representação se não o exercer no prazo de 12 (doze) meses, contado do dia em que vier a saber quem é o autor do crime, ou, no caso do art. 29 deste Código, do dia em que se esgotar o prazo para o oferecimento de denúncia. (Incluído pela Lei nº 15.438, de 2026)"
- `cpp.txt:326` — "Art. 61. Em qualquer fase do processo, o juiz, se reconhecer extinta a punibilidade, deverá declará-lo de ofício."
- `cpp.txt:387` — "Art. 78. Na determinação da competência por conexão ou continência, serão observadas as seguintes regras: (Redação dada pela Lei nº 263, de 23.2.1948)"
- `cpp.txt:388` — "I - no concurso entre a competência do júri e a de outro órgão da jurisdição comum, prevalecerá a competência do júri, salvo os casos de homicídios cometidos por membros de organizações criminosas ultraviolentas, grupo paramilitar ou milícia privada, ou sua tentativa, na forma do art. 2º da lei que institui o marco legal do combate ao crime organizado no Brasil; (Redação dada pela Lei nº 15.358, de 2026)"
- `cpp.txt:446` — "Art. 96. A argüição de suspeição precederá a qualquer outra, salvo quando fundada em motivo superveniente."
- `cpp.txt:453` — "Art. 101. Julgada procedente a suspeição, ficarão nulos os atos do processo principal, pagando o juiz as custas, no caso de erro inescusável; rejeitada, evidenciando-se a malícia do excipiente, a este será imposta a multa de duzentos mil-réis a dois contos de réis."
- `cpp.txt:465` — "Art. 108. A exceção de incompetência do juízo poderá ser oposta, verbalmente ou por escrito, no prazo de defesa."
- `cpp.txt:475` — "Art. 112. O juiz, o órgão do Ministério Público, os serventuários ou funcionários de justiça e os peritos ou intérpretes abster-se-ão de servir no processo, quando houver incompatibilidade ou impedimento legal, que declararão nos autos. Se não se der a abstenção, a incompatibilidade ou impedimento poderá ser argüido pelas partes, seguindo-se o processo estabelecido para a exceção de suspeição."
- `cpp.txt:690` — "Art. 159. O exame de corpo de delito e outras perícias serão realizados por perito oficial, portador de diploma de curso superior. (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:691` — "§ 1o Na falta de perito oficial, o exame será realizado por 2 (duas) pessoas idôneas, portadoras de diploma de curso superior preferencialmente na área específica, dentre as que tiverem habilitação técnica relacionada com a natureza do exame. (Redação dada pela Lei nº 11.690, de 2008)"
- `cpp.txt:893` — "§ 2o Proceder-se-á à busca pessoal quando houver fundada suspeita de que alguém oculte consigo arma proibida ou objetos mencionados nas letras b a f e letra h do parágrafo anterior."
- `cpp.txt:926` — "Art. 252. O juiz não poderá exercer jurisdição no processo em que:"
- `cpp.txt:927` — "I - tiver funcionado seu cônjuge ou parente, consangüíneo ou afim, em linha reta ou colateral até o terceiro grau, inclusive, como defensor ou advogado, órgão do Ministério Público, autoridade policial, auxiliar da justiça ou perito;"
- `cpp.txt:928` — "II - ele próprio houver desempenhado qualquer dessas funções ou servido como testemunha;"
- `cpp.txt:929` — "III - tiver funcionado como juiz de outra instância, pronunciando-se, de fato ou de direito, sobre a questão;"
- `cpp.txt:930` — "IV - ele próprio ou seu cônjuge ou parente, consangüíneo ou afim em linha reta ou colateral até o terceiro grau, inclusive, for parte ou diretamente interessado no feito."
- `cpp.txt:932` — "Art. 254. O juiz dar-se-á por suspeito, e, se não o fizer, poderá ser recusado por qualquer das partes:"
- `cpp.txt:933` — "I - se for amigo íntimo ou inimigo capital de qualquer deles;"
- `cpp.txt:934` — "II - se ele, seu cônjuge, ascendente ou descendente, estiver respondendo a processo por fato análogo, sobre cujo caráter criminoso haja controvérsia;"
- `cpp.txt:935` — "III - se ele, seu cônjuge, ou parente, consangüíneo, ou afim, até o terceiro grau, inclusive, sustentar demanda ou responder a processo que tenha de ser julgado por qualquer das partes;"
- `cpp.txt:936` — "IV - se tiver aconselhado qualquer das partes;"
- `cpp.txt:937` — "V - se for credor ou devedor, tutor ou curador, de qualquer das partes;"
- `cpp.txt:938` — "Vl - se for sócio, acionista ou administrador de sociedade interessada no processo."
- `cpp.txt:221` — "Art. 28-A. Não sendo caso de arquivamento e tendo o investigado confessado formal e circunstancialmente a prática de infração penal sem violência ou grave ameaça e com pena mínima inferior a 4 (quatro) anos, o Ministério Público poderá propor acordo de não persecução penal, desde que necessário e suficiente para reprovação e prevenção do crime, mediante as seguintes condições ajustadas cumulativa e alternativamente: (Incluído pela Lei nº 13.964, de 2019) (Vigência) (Vide ADI 6.298)"
- `cpp.txt:236` — "§ 1º Para aferição da pena mínima cominada ao delito a que se refere o caput deste artigo, serão consideradas as causas de aumento e diminuição aplicáveis ao caso concreto."
- `cpp.txt:238` — "§ 2º O disposto no caput deste artigo não se aplica nas seguintes hipóteses: (Incluído pela Lei nº 13.964, de 2019) (Vigência)"
- `cpp.txt:240` — "I - se for cabível transação penal de competência dos Juizados Especiais Criminais, nos termos da lei; (Incluído pela Lei nº 13.964, de 2019) (Vigência)"
- `cpp.txt:242` — "II - se o investigado for reincidente ou se houver elementos probatórios que indiquem conduta criminal habitual, reiterada ou profissional, exceto se insignificantes as infrações penais pretéritas; (Incluído pela Lei nº 13.964, de 2019) (Vigência)"
- `cpp.txt:244` — "III - ter sido o agente beneficiado nos 5 (cinco) anos anteriores ao cometimento da infração, em acordo de não persecução penal, transação penal ou suspensão condicional do processo; e (Incluído pela Lei nº 13.964, de 2019) (Vigência)"
- `cpp.txt:246` — "IV - nos crimes praticados no âmbito de violência doméstica ou familiar, ou praticados contra a mulher por razões da condição de sexo feminino, em favor do agressor. (Incluído pela Lei nº 13.964, de 2019) (Vigência)"
- `cpp.txt:273` — "§ 14. No caso de recusa, por parte do Ministério Público, em propor o acordo de não persecução penal, o investigado poderá requerer a remessa dos autos a órgão superior, na forma do art. 28 deste Código. (Incluído pela Lei nº 13.964, de 2019) (Vigência)"

Situação: o art. 38 teve o § 2º incluído e o parágrafo único renumerado pela Lei nº 15.438, de 18 de junho de 2026 (DOU de 19.6.2026). O art. 78, I, e o art. 3º-B, § 1º, têm a redação da Lei nº 15.358, de 24 de março de 2026 (DOU de 25.3.2026). Os demais estão na redação indicada em cada linha.

## 3. Constituição

Fonte: `cf.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm). Todos os dispositivos abaixo estão vigentes. Salvo indicação, a redação é a original de 1988.

Art. 5º, caput e incisos pedidos:

- `cf.txt:51` — "Art. 5º Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos seguintes:"
- `cf.txt:54` — "III - ninguém será submetido a tortura nem a tratamento desumano ou degradante;"
- `cf.txt:61` — "X - são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de sua violação;"
- `cf.txt:62` — "XI - a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial;"
- `cf.txt:65` — "XII - é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal;"
- `cf.txt:97` — "XXXVII - não haverá juízo ou tribunal de exceção;"
- `cf.txt:98` — "XXXVIII - é reconhecida a instituição do júri, com a organização que lhe der a lei, assegurados:"
- `cf.txt:99` — "a) a plenitude de defesa;"
- `cf.txt:100` — "b) o sigilo das votações;"
- `cf.txt:101` — "c) a soberania dos veredictos;"
- `cf.txt:102` — "d) a competência para o julgamento dos crimes dolosos contra a vida;"
- `cf.txt:103` — "XXXIX - não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal;"
- `cf.txt:104` — "XL - a lei penal não retroagirá, salvo para beneficiar o réu;"
- `cf.txt:124` — "XLIX - é assegurado aos presos o respeito à integridade física e moral;"
- `cf.txt:128` — "LIII - ninguém será processado nem sentenciado senão pela autoridade competente;"
- `cf.txt:129` — "LIV - ninguém será privado da liberdade ou de seus bens sem o devido processo legal;"
- `cf.txt:130` — "LV - aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e ampla defesa, com os meios e recursos a ela inerentes;"
- `cf.txt:131` — "LVI - são inadmissíveis, no processo, as provas obtidas por meios ilícitos;"
- `cf.txt:132` — "LVII - ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória;"
- `cf.txt:137` — "LXI - ninguém será preso senão em flagrante delito ou por ordem escrita e fundamentada de autoridade judiciária competente, salvo nos casos de transgressão militar ou crime propriamente militar, definidos em lei;"
- `cf.txt:138` — "LXII - a prisão de qualquer pessoa e o local onde se encontre serão comunicados imediatamente ao juiz competente e à família do preso ou à pessoa por ele indicada;"
- `cf.txt:139` — "LXIII - o preso será informado de seus direitos, entre os quais o de permanecer calado, sendo-lhe assegurada a assistência da família e de advogado;"
- `cf.txt:140` — "LXIV - o preso tem direito à identificação dos responsáveis por sua prisão ou por seu interrogatório policial;"
- `cf.txt:141` — "LXV - a prisão ilegal será imediatamente relaxada pela autoridade judiciária;"
- `cf.txt:142` — "LXVI - ninguém será levado à prisão ou nela mantido, quando a lei admitir a liberdade provisória, com ou sem fiança;"
- `cf.txt:144-146` — "LXVIII - conceder-se-á "habeas-corpus" sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder;"
- `cf.txt:160` — "LXXIV - o Estado prestará assistência jurídica integral e gratuita aos que comprovarem insuficiência de recursos;"
- `cf.txt:172` — "LXXVIII - a todos, no âmbito judicial e administrativo, são assegurados a razoável duração do processo e os meios que garantam a celeridade de sua tramitação. (Incluído pela Emenda Constitucional nº 45, de 2004) (Vide ADIN 3392)"
- `cf.txt:179` — "§ 2º Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte."
- `cf.txt:180` — "§ 3º Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais. (Incluído pela Emenda Constitucional nº 45, de 2004) (Vide ADIN 3392) (Vide Atos decorrentes do disposto no § 3º do art. 5º da Constituição)"

Observações: o inciso LXVIII ocupa três linhas na fonte (144 a 146), unidas acima. O inciso LXXVIII e o § 3º foram incluídos pela Emenda Constitucional nº 45, de 2004. O inciso XV, usado na auditoria, é:

- `cf.txt:69` — "XV - é livre a locomoção no território nacional em tempo de paz, podendo qualquer pessoa, nos termos da lei, nele entrar, permanecer ou dele sair com seus bens;"

Art. 93, IX:

- `cf.txt:1991` — "Art. 93. Lei complementar, de iniciativa do Supremo Tribunal Federal, disporá sobre o Estatuto da Magistratura, observados os seguintes princípios:"
- `cf.txt:2049` — "IX todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e fundamentadas todas as decisões, sob pena de nulidade, podendo a lei limitar a presença, em determinados atos, às próprias partes e a seus advogados, ou somente a estes, em casos nos quais a preservação do direito à intimidade do interessado no sigilo não prejudique o interesse público à informação; (Redação dada pela Emenda Constitucional nº 45, de 2004)"

Situação: redação da Emenda Constitucional nº 45, de 2004. A redação original está riscada na página (`cf.txt:2031`).

Art. 129, I:

- `cf.txt:2899` — "Art. 129. São funções institucionais do Ministério Público:"
- `cf.txt:2900` — "I - promover, privativamente, a ação penal pública, na forma da lei;"

Art. 133:

- `cf.txt:2989` — "Art. 133. O advogado é indispensável à administração da justiça, sendo inviolável por seus atos e manifestações no exercício da profissão, nos limites da lei."

Art. 134 (citado na tese "defesa-tecnica"):

- `cf.txt:2995-2996` — "Art. 134. A Defensoria Pública é instituição permanente, essencial à função jurisdicional do Estado, incumbindo-lhe, como expressão e instrumento do regime democrático, fundamentalmente, a orientação jurídica, a promoção dos direitos humanos e a defesa, em todos os graus, judicial e extrajudicial, dos direitos individuais e coletivos, de forma integral e gratuita, aos necessitados, na forma do inciso LXXIV do art. 5º desta Constituição Federal"

## 4. Tratados

### Convenção Americana sobre Direitos Humanos (Decreto nº 678, de 6 de novembro de 1992)

Fonte: `d678.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm). Em vigor para o Brasil desde 25 de setembro de 1992 (`d678.txt:10`). Decreto publicado no DOU de 9.11.1992 (`d678.txt:18`).

- `d678.txt:5` — "DECRETO No 678, DE 6 DE NOVEMBRO DE 1992"
- `d678.txt:6` — "Promulga a Convenção Americana sobre Direitos Humanos (Pacto de São José da Costa Rica), de 22 de novembro de 1969."
- `d678.txt:10` — "Considerando que a Convenção Americana sobre Direitos Humanos (Pacto de São José da Costa Rica) entrou em vigor, para o Brasil, em 25 de setembro de 1992, de conformidade com o disposto no segundo parágrafo de seu artigo 74;"

Art. 5, itens 1 e 2:

- `d678.txt:54` — "ARTIGO 5"
- `d678.txt:55` — "Direito à Integridade Pessoal"
- `d678.txt:56` — "1. Toda pessoa tem o direito de que se respeite sua integridade física, psíquica e moral."
- `d678.txt:57` — "2. Ninguém deve ser submetido a torturas, nem a penas ou tratos cruéis, desumanos ou degradantes. Toda pessoa privada da liberdade deve ser tratada com o respeito devido à dignidade inerente ao ser humano."

Art. 7, itens 1 a 6:

- `d678.txt:71` — "ARTIGO 7"
- `d678.txt:72` — "Direito à Liberdade Pessoal"
- `d678.txt:73` — "1. Toda pessoa tem direito à liberdade e à segurança pessoais."
- `d678.txt:74` — "2. Ninguém pode ser privado de sua liberdade física, salvo pelas causas e nas condições previamente fixadas pelas constituições políticas dos Estados-Partes ou pelas leis de acordo com elas promulgadas."
- `d678.txt:75` — "3. Ninguém pode ser submetido a detenção ou encarceramento arbitrários."
- `d678.txt:76` — "4. Toda pessoa detida ou retida deve ser informada das razões da sua detenção e notificada, sem demora, da acusação ou acusações formuladas contra ela."
- `d678.txt:77` — "5. Toda pessoa detida ou retida deve ser conduzida, sem demora, à presença de um juiz ou outra autoridade autorizada pela lei a exercer funções judiciais e tem direito a ser julgada dentro de um prazo razoável ou a ser posta em liberdade, sem prejuízo de que prossiga o processo. Sua liberdade pode ser condicionada a garantias que assegurem o seu comparecimento em juízo."
- `d678.txt:78` — "6. Toda pessoa privada da liberdade tem direito a recorrer a um juiz ou tribunal competente, a fim de que este decida, sem demora, sobre a legalidade de sua prisão ou detenção e ordene sua soltura se a prisão ou a detenção forem ilegais. Nos Estados-Partes cujas leis prevêem que toda pessoa que se vir ameaçada de ser privada de sua liberdade tem direito a recorrer a um juiz ou tribunal competente a fim de que este decida sobre a legalidade de tal ameaça, tal recurso não pode ser restringido nem abolido. O recurso pode ser interposto pela própria pessoa ou por outra pessoa."

Art. 8, itens 1 a 5:

- `d678.txt:80` — "ARTIGO 8"
- `d678.txt:81` — "Garantias Judiciais"
- `d678.txt:82` — "1. Toda pessoa tem direito a ser ouvida, com as devidas garantias e dentro de um prazo razoável, por um juiz ou tribunal competente, independente e imparcial, estabelecido anteriormente por lei, na apuração de qualquer acusação penal formulada contra ela, ou para que se determinem seus direitos ou obrigações de natureza civil, trabalhista, fiscal ou de qualquer outra natureza."
- `d678.txt:83` — "2. Toda pessoa acusada de delito tem direito a que se presuma sua inocência enquanto não se comprove legalmente sua culpa. Durante o processo, toda pessoa tem direito, em plena igualdade, às seguintes garantias mínimas:"
- `d678.txt:84` — "a) direito do acusado de ser assistido gratuitamente por tradutor ou intérprete, se não compreender ou não falar o idioma do juízo ou tribunal;"
- `d678.txt:85` — "b) comunicação prévia e pormenorizada ao acusado da acusação formulada;"
- `d678.txt:86` — "c) concessão ao acusado do tempo e dos meios adequados para a preparação de sua defesa;"
- `d678.txt:87` — "d) direito do acusado de defender-se pessoalmente ou de ser assistido por um defensor de sua escolha e de comunicar-se, livremente e em particular, com seu defensor;"
- `d678.txt:88` — "e) direito irrenunciável de ser assistido por um defensor proporcionado pelo Estado, remunerado ou não, segundo a legislação interna, se o acusado não se defender ele próprio nem nomear defensor dentro do prazo estabelecido pela lei;"
- `d678.txt:89` — "f) direito da defesa de inquirir as testemunhas presentes no tribunal e de obter o comparecimento, como testemunhas ou peritos, de outras pessoas que possam lançar luz sobre os fatos."
- `d678.txt:90` — "g) direito de não ser obrigado a depor contra si mesma, nem a declarar-se culpada; e"
- `d678.txt:91` — "h) direito de recorrer da sentença para juiz ou tribunal superior."
- `d678.txt:92` — "3. A confissão do acusado só é válida se feita sem coação de nenhuma natureza."
- `d678.txt:93` — "4. O acusado absolvido por sentença passada em julgado não poderá se submetido a novo processo pelos mesmos fatos."
- `d678.txt:94` — "5. O processo penal deve ser público, salvo no que for necessário para preservar os interesses da justiça."

Art. 9:

- `d678.txt:95` — "ARTIGO 9"
- `d678.txt:96` — "Princípio da Legalidade e da Retroatividade"
- `d678.txt:97` — "Ninguém pode ser condenado por ações ou omissões que, no memento em que forem cometidas, não sejam delituosas, de acordo com o direito aplicável. Tampouco se pode impor pena mais grave que a aplicável no momento da perpetração do delito. Se depois da perpetração do delito a lei dispuser a imposição de pena mais leve, o delinqüente será por isso beneficiado."

Art. 11:

- `d678.txt:101` — "ARTIGO 11"
- `d678.txt:102` — "Proteção da Honra e da Dignidade"
- `d678.txt:103` — "1. Toda pessoa tem direito ao respeito de sua honra e ao reconhecimento de sua dignidade."
- `d678.txt:104` — "2. Ninguém pode ser objeto de ingerências arbitrárias ou abusivas em sua vida privada, na de sua família, em seu domicílio ou em sua correspondência, nem de ofensas ilegais à sua honra ou reputação."
- `d678.txt:105` — "3. Toda pessoa tem direito à proteção da lei contra tais ingerências ou tais ofensas."

Art. 25:

- `d678.txt:178` — "ARTIGO 25"
- `d678.txt:179` — "Proteção Judicial"
- `d678.txt:180` — "1. Toda pessoa tem direito a um recurso simples e rápido ou a qualquer outro recurso efetivo, perante os juízes ou tribunais competentes, que a proteja contra atos que violem seus direitos fundamentais reconhecidos pela constituição, pela lei ou pela presente Convenção, mesmo quando tal violação seja cometida por pessoas que estejam atuando no exercício de suas funções oficiais."
- `d678.txt:181` — "2. Os Estados-Partes comprometem-se:"
- `d678.txt:182` — "a) a assegurar que a autoridade competente prevista pelo sistema legal do Estado decida sobre os direitos de toda pessoa que interpuser tal recurso;"
- `d678.txt:183` — "b) a desenvolver as possibilidades de recurso judicial; e"
- `d678.txt:184` — "c) a assegurar o cumprimento, pelas autoridades competentes, de toda decisão em que se tenha considerado procedente o recurso."

Observação: a grafia é a da fonte ("no memento", "não poderá se submetido").

### Reconhecimento da competência contenciosa da Corte Interamericana (Decreto nº 4.463, de 8 de novembro de 2002)

Fonte: `d4463.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto/2002/d4463.htm).

- `d4463.txt:5` — "DECRETO Nº 4.463, DE 8 DE NOVEMBRO DE 2002."
- `d4463.txt:6` — "Promulga a Declaração de Reconhecimento da Competência Obrigatória da Corte Interamericana de Direitos Humanos, sob reserva de reciprocidade, em consonância com o art. 62 da Convenção Americana sobre Direitos Humanos (Pacto de São José), de 22 de novembro de 1969."
- `d4463.txt:9` — "Considerando que o Congresso Nacional aprovou, pelo Decreto Legislativo no 89, de 3 de dezembro de 1998, solicitação de reconhecimento da competência obrigatória da Corte Interamericana de Direitos Humanos, em todos os casos relativos à interpretação ou aplicação da Convenção, de acordo com o previsto no art. 62 daquele instrumento;"
- `d4463.txt:10` — "Considerando que a Declaração de aceitação da competência obrigatória da Corte Interamericana de Direitos Humanos foi depositada junto à Secretaria-Geral da Organização dos Estados Americanos em 10 de dezembro de 1998,"
- `d4463.txt:12` — "Art. 1o É reconhecida como obrigatória, de pleno direito e por prazo indeterminado, a competência da Corte Interamericana de Direitos Humanos em todos os casos relativos à interpretação ou aplicação da Convenção Americana de Direitos Humanos (Pacto de São José), de 22 de novembro de 1969, de acordo com art. 62 da citada Convenção, sob reserva de reciprocidade e para fatos posteriores a 10 de dezembro de 1998."
- `d4463.txt:17` — "Este texto não substitui o publicado no D.O.U. de 11.11.2002"

Datas: a declaração de aceitação foi depositada em 10 de dezembro de 1998. A competência vale "para fatos posteriores a 10 de dezembro de 1998". O Congresso aprovou o reconhecimento pelo Decreto Legislativo nº 89, de 3 de dezembro de 1998. O decreto de promulgação é de 8 de novembro de 2002 (DOU de 11.11.2002).

### Pacto Internacional sobre Direitos Civis e Políticos (Decreto nº 592, de 6 de julho de 1992)

Fonte: `d592.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0592.htm). DOU de 7.7.1992 (`d592.txt:18`).

- `d592.txt:5` — "DECRETO No 592, DE 6 DE JULHO DE 1992."
- `d592.txt:6` — "Atos Internacionais. Pacto Internacional sobre Direitos Civis e Políticos. Promulgação."

Art. 7:

- `d592.txt:59` — "ARTIGO 7"
- `d592.txt:60` — "Ninguém poderá ser submetido à tortura, nem a penas ou tratamento cruéis, desumanos ou degradantes. Será proibido, sobretudo, submeter uma pessoa, sem seu livre consentimento, a experiências médicas ou científicas."

Art. 9:

- `d592.txt:71` — "ARTIGO 9"
- `d592.txt:72` — "1. Toda pessoa tem direito à liberdade e à segurança pessoais. Ninguém poderá ser preso ou encarcerado arbitrariamente. Ninguém poderá ser privado de sua liberdade, salvo pelos motivos previstos em lei e em conformidade com os procedimentos nela estabelecidos."
- `d592.txt:73` — "2. Qualquer pessoa, ao ser presa, deverá ser informada das razões da prisão e notificada, sem demora, das acusações formuladas contra ela."
- `d592.txt:74` — "3. Qualquer pessoa presa ou encarcerada em virtude de infração penal deverá ser conduzida, sem demora, à presença do juiz ou de outra autoridade habilitada por lei a exercer funções judiciais e terá o direito de ser julgada em prazo razoável ou de ser posta em liberdade. A prisão preventiva de pessoas que aguardam julgamento não deverá constituir a regra geral, mas a soltura poderá estar condicionada a garantias que assegurem o comparecimento da pessoa em questão à audiência, a todos os atos do processo e, se necessário for, para a execução da sentença."
- `d592.txt:75` — "4. Qualquer pessoa que seja privada de sua liberdade por prisão ou encarceramento terá o direito de recorrer a um tribunal para que este decida sobre a legalidade de seu encarceramento e ordene sua soltura, caso a prisão tenha sido ilegal."
- `d592.txt:76` — "5. Qualquer pessoa vítima de prisão ou encarceramento ilegais terá direito à reparação."

Art. 14:

- `d592.txt:91` — "ARTIGO 14"
- `d592.txt:92` — "1. Todas as pessoas são iguais perante os tribunais e as cortes de justiça. Toda pessoa terá o direito de ser ouvida publicamente e com as devidas garantias por um tribunal competente, independente e imparcial, estabelecido por lei, na apuração de qualquer acusação de caráter penal formulada contra ela ou na determinação de seus direitos e obrigações de caráter civil. A imprensa e o público poderão ser excluídos de parte ou da totalidade de um julgamento, quer por motivo de moral pública, de ordem pública ou de segurança nacional em uma sociedade democrática, quer quando o interesse da vida privada das Partes o exija, que na medida em que isso seja estritamente necessário na opinião da justiça, em circunstâncias específicas, nas quais a publicidade venha a prejudicar os interesses da justiça; entretanto, qualquer sentença proferida em matéria penal ou civil deverá tornar-se pública, a menos que o interesse de menores exija procedimento oposto, ou o processo diga respeito à controvérsias matrimoniais ou à tutela de menores."
- `d592.txt:93` — "2. Toda pessoa acusada de um delito terá direito a que se presuma sua inocência enquanto não for legalmente comprovada sua culpa."
- `d592.txt:94` — "3. Toda pessoa acusada de um delito terá direito, em plena igualdade, a, pelo menos, as seguintes garantias:"
- `d592.txt:95` — "a) De ser informado, sem demora, numa língua que compreenda e de forma minuciosa, da natureza e dos motivos da acusão contra ela formulada;"
- `d592.txt:96` — "b) De dispor do tempo e dos meios necessários à preparação de sua defesa e a comunicar-se com defensor de sua escolha;"
- `d592.txt:97` — "c) De ser julgado sem dilações indevidas;"
- `d592.txt:98` — "d) De estar presente no julgamento e de defender-se pessoalmente ou por intermédio de defensor de sua escolha; de ser informado, caso não tenha defensor, do direito que lhe assiste de tê-lo e, sempre que o interesse da justiça assim exija, de ter um defensor designado ex-offício gratuitamente, se não tiver meios para remunerá-lo;"
- `d592.txt:99` — "e) De interrogar ou fazer interrogar as testemunhas de acusão e de obter o comparecimento e o interrogatório das testemunhas de defesa nas mesmas condições de que dispõem as de acusação;"
- `d592.txt:100` — "f) De ser assistida gratuitamente por um intérprete, caso não compreenda ou não fale a língua empregada durante o julgamento;"
- `d592.txt:101` — "g) De não ser obrigada a depor contra si mesma, nem a confessar-se culpada."
- `d592.txt:102` — "4. O processo aplicável a jovens que não sejam maiores nos termos da legislação penal levará em conta a idade dos mesmos e a importância de promover sua reintegração social."
- `d592.txt:103` — "5. Toda pessoa declarada culpada por um delito terá o direito de recorrer da sentença condenatória e da pena a uma instância superior, em conformidade com a lei."
- `d592.txt:104` — "6. Se uma sentença condenatória passada em julgado for posteriormente anulada ou se um indulto for concedido, pela ocorrência ou descoberta de fatos novos que provem cabalmente a existência de erro judicial, a pessoa que sofreu a pena decorrente dessa condenação deverá ser indenizada, de acordo com a lei, a menos que fique provado que se lhe pode imputar, total ou parcialmente, a não-revelação dos fatos desconhecidos em tempo útil."
- `d592.txt:105` — "7. Ninguém poderá ser processado ou punido por um delito pelo qual já foi absolvido ou condenado por sentença passada em julgado, em conformidade com a lei e os procedimentos penais de cada país."

Art. 15:

- `d592.txt:106` — "ARTIGO 15"
- `d592.txt:107` — "1. Ninguém poderá ser condenado por atos ou omissões que não constituam delito de acordo com o direito nacional ou internacional, no momento em que foram cometidos. Tampouco poder-se-a impor pena mais grave do que a aplicável no momento da ocorrência do delito. Se, depois de perpetrado o delito, a lei estipular a imposição de pena mais leve, o delinqüente deverá dela beneficiar-se."
- `d592.txt:108` — "2. Nenhuma disposição do presente Pacto impedirá o julgamento ou a condenação de qualquer indivíduo por atos ou omissões que, no momento em que foram cometidos, eram considerados delituosos de acordo com os princípios gerais de direito reconhecidos pela comunidade das nações."

Art. 17:

- `d592.txt:111` — "ARTIGO 17"
- `d592.txt:112` — "1. Ninguém poderá ser objeto de ingerências arbitrárias ou ilegais em sua vida privada, em sua família, em seu domicílio ou em sua correspondência, nem de ofensas ilegais às suas honra e reputação."
- `d592.txt:113` — "2. Toda pessoa terá direito à proteção da lei contra essas ingerências ou ofensas."

Observação: a grafia é a da fonte ("acusão", "ex-offício", "poder-se-a").

### Convenção contra a Tortura (Decreto nº 40, de 15 de fevereiro de 1991)

Fonte: `d40.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0040.htm). DOU de 18.2.1991 (`d40.txt:18`).

- `d40.txt:5` — "DECRETO No 40, DE 15 DE FEVEREIRO DE 1991."
- `d40.txt:6` — "Promulga a Convenção Contra a Tortura e Outros Tratamentos ou Penas Cruéis, Desumanos ou Degradantes."
- `d40.txt:79` — "ARTIGO 15"
- `d40.txt:80` — "Cada Estado Parte assegurará que nenhuma declaração que se demonstre ter sido prestada como resultado de tortura possa ser invocada como prova em qualquer processo, salvo contra uma pessoa acusada de tortura como prova de que a declaração foi prestada."

Observação: o art. 15 tem ressalva. A declaração pode ser usada "contra uma pessoa acusada de tortura como prova de que a declaração foi prestada".

## 5. Manual de Redação da Presidência da República, Lei Complementar nº 95 e Decreto nº 12.002

Fonte do Manual: `manual.txt` (3ª edição, 2018; cópia da UFGD, ver seção 1). Os números de seção são os do próprio Manual.

### Seção 3 — Atributos da redação oficial

- `manual.txt:498` — "3 Atributos da redação oficial"
- `manual.txt:499` — "A redação oficial deve caracterizar-se por:"
- `manual.txt:500` — "clareza e precisão;"
- `manual.txt:501` — "objetividade;"
- `manual.txt:502` — "concisão;"
- `manual.txt:503` — "coesão e coerência;"
- `manual.txt:504` — "impessoalidade;"
- `manual.txt:505` — "formalidade e padronização; e"
- `manual.txt:506` — "uso da norma padrão da língua portuguesa."

### Siglas na primeira citação

Seção 3.1 (clareza), alínea f:

- `manual.txt:533` — "f) explicitar o significado da sigla na primeira referência a ela; e"

Seção 10.6 (uso de siglas e acrônimos):

- `manual.txt:2242-2244` — "Na primeira citação, a expressão designada deve vir escrita por extenso, de forma completa e correta, sempre antes de sua sigla ou acrônimo respectivo, separados por travessão."
- `manual.txt:2246` — "Exemplo:"
- `manual.txt:2247` — "Imposto Predial e Territorial Urbano – IPTU"

Seção 10.6.1 (siglas em atos normativos), com remissão ao Decreto nº 9.191, de 2017:

- `manual.txt:2307-2308` — "Nos textos de atos normativos, o uso de siglas e acrônimos deve respeitar o disposto na alínea “e” do inciso II, do art. 14 do Decreto nº 9.191, de 2017:"
- `manual.txt:2309` — "1 não utilizar para designar órgãos da administração pública direta;"
- `manual.txt:2310` — "2 para entidades da administração pública indireta, utilizar apenas se previsto em lei;"
- `manual.txt:2311` — "3 não utilizar para designar ato normativo;"
- `manual.txt:2312` — "4 usar apenas se consagrado pelo uso geral e não apenas no âmbito de setor da"
- `manual.txt:2313` — "administração pública ou de grupo social específico; e"
- `manual.txt:2314` — "5 na primeira menção, utilizar acompanhado da explicitação de seu significado."

Lei Complementar nº 95, de 1998, art. 11, II, e:

- `lcp95.txt:69` — "e) usar apenas siglas consagradas pelo uso, observado o princípio de que a primeira referência no texto seja acompanhada de explicitação de seu significado;"

### Seção 4.4 — Vocativo

- `manual.txt:924-925` — "O vocativo é uma invocação ao destinatário. Nas comunicações oficiais, o vocativo será sempre seguido de vírgula."
- `manual.txt:926-927` — "Em comunicações dirigidas aos Chefes de Poder, utiliza-se a expressão Excelentíssimo Senhor ou Excelentíssima Senhora e o cargo respectivo, seguidos de vírgula."
- `manual.txt:929` — "Exemplos:"
- `manual.txt:930` — "Excelentíssimo Senhor Presidente da República,"
- `manual.txt:931` — "Excelentíssimo Senhor Presidente do Congresso Nacional,"
- `manual.txt:932` — "Excelentíssimo Senhor Presidente do Supremo Tribunal Federal,"
- `manual.txt:934-935` — "As demais autoridades, mesmo aquelas tratadas por Vossa Excelência, receberão o vocativo Senhor ou Senhora seguido do cargo respectivo."
- `manual.txt:937` — "Exemplos:"
- `manual.txt:938` — "Senhora Senadora,"
- `manual.txt:939` — "Senhor Juiz,"
- `manual.txt:940` — "Senhora Ministra,"
- `manual.txt:942-944` — "Na hipótese de comunicação com particular, pode-se utilizar o vocativo Senhor ou Senhora e a forma utilizada pela instituição para referir-se ao interlocutor: beneficiário, usuário, contribuinte, eleitor etc."
- `manual.txt:946` — "Exemplos:"
- `manual.txt:947` — "Senhora Beneficiária,"
- `manual.txt:948` — "Senhor Contribuinte,"
- `manual.txt:952-954` — "Ainda, quando o destinatário for um particular, no vocativo, pode-se utilizar Senhor ou Senhora seguido do nome do particular ou pode-se utilizar o vocativo “Prezado Senhor” ou “Prezada Senhora”."
- `manual.txt:956` — "Exemplos:"
- `manual.txt:957` — "Senhora [Nome],"
- `manual.txt:958` — "Prezado Senhor,"
- `manual.txt:960` — "Em comunicações oficiais, está abolido o uso de Digníssimo (DD) e de Ilustríssimo (Ilmo.)."
- `manual.txt:961-962` — "Evite-se o uso de “doutor” indiscriminadamente. O tratamento por meio de Senhor confere a formalidade desejada."

### Seção 5.1.6 — Texto do documento (padrão ofício)

- `manual.txt:1093` — "O texto do documento oficial deve seguir a seguinte padronização de estrutura:"
- `manual.txt:1094-1095` — "I – nos casos em que não seja usado para encaminhamento de documentos, o expediente deve conter a seguinte estrutura:"
- `manual.txt:1096-1098` — "a) introdução: em que é apresentado o objetivo da comunicação. Evite o uso das formas: Tenho a honra de, Tenho o prazer de, Cumpre-me informar que. Prefira empregar a forma direta: Informo, Solicito, Comunico;"
- `manual.txt:1099-1101` — "b) desenvolvimento: em que o assunto é detalhado; se o texto contiver mais de uma ideia sobre o assunto, elas devem ser tratadas em parágrafos distintos, o que confere maior clareza à exposição; e"
- `manual.txt:1102` — "c) conclusão: em que é afirmada a posição sobre o assunto."
- `manual.txt:1104` — "II – quando forem usados para encaminhamento de documentos, a estrutura é modificada:"
- `manual.txt:1105-1109` — "a) introdução: deve iniciar com referência ao expediente que solicitou o encaminhamento. Se a remessa do documento não tiver sido solicitada, deve iniciar com a informação do motivo da comunicação, que é encaminhar, indicando a seguir os dados completos do documento encaminhado (tipo, data, origem ou signatário e assunto de que se trata) e a razão pela qual está sendo encaminhado; e"
- `manual.txt:1120-1123` — "b) desenvolvimento: se o autor da comunicação desejar fazer algum comentário a respeito do documento que encaminha, poderá acrescentar parágrafos de desenvolvimento. Caso contrário, não há parágrafos de desenvolvimento em expediente usado para encaminhamento de documentos."
- `manual.txt:1125-1126` — "III – tanto na estrutura I quanto na estrutura II, o texto do documento deve ser formatado da seguinte maneira:"
- `manual.txt:1127` — "a) alinhamento: justificado;"
- `manual.txt:1128` — "b) espaçamento entre linhas: simples;"
- `manual.txt:1129` — "c) parágrafos:"
- `manual.txt:1130` — "i espaçamento entre parágrafos: de 6 pontos após cada parágrafo;"
- `manual.txt:1131` — "ii recuo de parágrafo: 2,5 cm de distância da margem esquerda;"
- `manual.txt:1132-1133` — "iii numeração dos parágrafos: apenas quando o documento tiver três ou mais parágrafos, desde o primeiro parágrafo. Não se numeram o vocativo e o fecho;"
- `manual.txt:1134` — "d) fonte: Calibri ou Carlito;"
- `manual.txt:1137` — "i corpo do texto: tamanho 12 pontos;"
- `manual.txt:1138` — "ii citações recuadas: tamanho 11 pontos; e"
- `manual.txt:1139` — "iii notas de Rodapé: tamanho 10 pontos;"
- `manual.txt:1140-1141` — "e) símbolos: para símbolos não existentes nas fontes indicadas, pode-se utilizar as fontes Symbol e Wingdings;"

### Seção 5.2 — Formatação e apresentação

- `manual.txt:1195` — "Os documentos do padrão ofício devem obedecer à seguinte formatação:"
- `manual.txt:1196` — "a) tamanho do papel: A4 (29,7 cm x 21 cm);"
- `manual.txt:1197` — "b) margem lateral esquerda: no mínimo, 3 cm de largura;"
- `manual.txt:1198` — "c) margem lateral direita: 1,5 cm;"
- `manual.txt:1199` — "d) margens superior e inferior: 2 cm;"
- `manual.txt:1200` — "e) área de cabeçalho: na primeira página, 5 cm a partir da margem superior do papel;"
- `manual.txt:1201` — "f) área de rodapé: nos 2 cm da margem inferior do documento;"
- `manual.txt:1202-1204` — "g) impressão: na correspondência oficial, a impressão pode ocorrer em ambas as faces do papel. Nesse caso, as margens esquerda e direita terão as distâncias invertidas nas páginas pares (margem espelho);"
- `manual.txt:1205-1206` — "h) cores: os textos devem ser impressos na cor preta em papel branco, reservando-se, se necessário, a impressão colorida para gráficos e ilustrações;"
- `manual.txt:1207-1209` — "i) destaques: para destaques deve-se utilizar, sem abuso, o negrito. Deve-se evitar destaques com uso de itálico, sublinhado, letras maiúsculas, sombreado, sombra, relevo, bordas ou qualquer outra forma de formatação que afete a sobriedade e a padronização do documento;"
- `manual.txt:1210` — "j) palavras estrangeiras: palavras estrangeiras devem ser grafadas em itálico;"
- `manual.txt:1211-1215` — "k) arquivamento: dentro do possível, todos os documentos elaborados devem ter o arquivo de texto preservado para consulta posterior ou aproveitamento de trechos para casos análogos. Deve ser utilizado, preferencialmente, formato de arquivo que possa ser lido e editado pela maioria dos editores de texto utilizados no serviço público, tais como DOCX, ODT ou RTF."
- `manual.txt:1216-1219` — "l) nome do arquivo: para facilitar a localização, os nomes dos arquivos devem ser formados da seguinte maneira: tipo do documento + número do documento + ano do documento (com 4 dígitos) + palavras-chaves do conteúdo"
- `manual.txt:1220` — "Exemplo:"
- `manual.txt:1221` — "Ofício 123_2018_relatório produtividade anual"

### Como citar atos normativos e seus dispositivos

**Primeira referência completa e referências seguintes.** O Manual não tem regra expressa sobre isso: procurei por "primeira remissão", "nos demais casos", "data completa" e termos próximos e não encontrei. O Manual aplica a prática no próprio texto: primeira menção com a data completa, menções seguintes só com o ano.

- `manual.txt:1453-1455` — "As Exposições de Motivos que encaminham proposições normativas devem seguir o prescrito no Decreto nº 9.191, de 1º de novembro de 2017. Em síntese, elas devem ser instruídas com parecer jurídico e parecer de mérito que permitam a adequada avaliação da proposta."
- `manual.txt:1456-1457` — "O atendimento dos requisitos do Decreto nº 9.191, de 2017, nas exposições de motivos que proponham a edição de ato normativo, tem como propósito:"

A regra expressa estava no Decreto nº 9.191, de 2017, art. 14, II, k, hoje revogado. A página do Planalto exibe o texto riscado (`d9191.txt:235-239`):

- `d9191.txt:235` — (riscado na fonte) "k) grafar a remissão aos atos normativos das seguintes formas:"
- `d9191.txt:237` — (riscado na fonte) "1. “Lei nº 8.112, de 11 de dezembro de 1990”, na ementa, no preâmbulo e na primeira remissão no corpo da norma; e"
- `d9191.txt:239` — (riscado na fonte) "2. “Lei nº 8.112, de 1990”, nos demais casos;"

O Decreto nº 9.191, de 2017, foi revogado pelo Decreto nº 12.002, de 22 de abril de 2024 (art. 77; em vigor desde 1º de junho de 2024):

- `d12002.txt:662-664` — "Art. 77. Ficam revogados: I - o Decreto nº 9.191, de 1º de novembro de 2017;"
- `d12002.txt:692` — "Art. 78. Este Decreto entra em vigor em 1º de junho de 2024."

Regra atual para atos normativos do Poder Executivo federal (Decreto nº 12.002, de 2024, art. 11, II, k e l). A forma abreviada "Lei nº 8.112, de 1990" não consta mais:

- `d12002.txt:89` — "Art. 11. As disposições normativas serão redigidas com clareza, precisão e ordem lógica, e observarão o seguinte:"
- `d12002.txt:129` — "k) grafar a remissão aos atos normativos das seguintes formas:"
- `d12002.txt:130` — "1. “Lei nº 10.406, de 10 de janeiro de 2002 – Código Civil”, no caso de códigos; e"
- `d12002.txt:131` — "2. “Lei nº 8.112, de 11 de dezembro de 1990”, nos demais casos;"
- `d12002.txt:132` — "l) quanto às remissões:"
- `d12002.txt:133` — "1. não fazer remissões desnecessárias a outros atos normativos;"
- `d12002.txt:134` — "2. não fazer remissões encadeadas;"
- `d12002.txt:135` — "3. não fazer remissões a atos normativos hierarquicamente inferiores;"
- `d12002.txt:136` — "4. indicar, expressamente, o dispositivo objeto de remissão, por meio do emprego da abreviatura “art.”, seguida do número correspondente, ordinal ou cardinal;"
- `d12002.txt:137` — "5. grafar as remissões aos dispositivos de outros artigos da seguinte forma: “art. 1º, caput, inciso I, alínea ‘a’”;"
- `d12002.txt:138` — "6. grafar as remissões ao próprio artigo da seguinte forma:"
- `d12002.txt:139` — "6.1. “inciso I, alínea ‘a’, do caput”; ou"
- `d12002.txt:140` — "6.2. “inciso I, alínea ‘a’, item 1, do § 1º”;"
- `d12002.txt:141` — "7. com exceção dos códigos, não usar nomes próprios ou apelidos para se referir a atos normativos; e"

Conclusão para as peças: o Manual, 3ª edição, não obriga uma forma. A prática do Manual é data completa na primeira menção e ano nas seguintes. O decreto em vigor, que vale para a redação de atos normativos, usa sempre a data completa.

**Artigo: grafia e numeração (seção 16.2.1).**

- `manual.txt:5174-5182` — "Artigo é a unidade básica para apresentação, divisão ou agrupamento de assuntos em um texto normativo. A Lei Complementar no 95, de 26 de fevereiro de 1998, apresenta as regras para a numeração dos artigos, de maneira que, até o artigo nono (art. 9o), deve-se adotar a numeração ordinal. A partir do artigo dez, emprega-se a numeração cardinal correspondente, seguida de ponto-final (art. 10.). Os artigos serão designados pela abreviatura “Art.”, com inicial maiúscula, sem traço antes do início do texto e, ao longo do texto, designados pela abreviatura – art. –, com inicial minúscula. Os textos dos artigos serão iniciados com letra maiúscula e encerrados com ponto-final, exceto quando tiverem incisos, hipótese em que serão encerrados por dois-pontos."

**Parágrafo e "parágrafo único" (seção 16.2.2).**

- `manual.txt:5222-5223` — "O parágrafo é representado pelo sinal gráfico § (signum sectionis, em português, sinal de seção ou sinal de corte)."
- `manual.txt:5226-5230` — "Também em relação ao parágrafo, existe a prática da numeração ordinal até o nono (§ 9o) e cardinal a partir do parágrafo dez (§ 10.). Na hipótese de haver apenas um parágrafo, adota-se a grafia “Parágrafo único.” (e não “§ único”), com a primeira letra em maiúsculo quando inicia o texto e minúscula quando citada ao longo do texto. Os textos dos parágrafos serão iniciados com letra maiúscula e encerrados com ponto-final."

**Incisos, alíneas e itens (seção 16.2.3).**

- `manual.txt:5268-5274` — "Os incisos são utilizados como elementos discriminativos de artigo ou parágrafo se o assunto nele tratado não puder ser condensado no próprio artigo ou não se mostrar adequado a constituir parágrafo. Os incisos são indicados por algarismos romanos seguidos de travessão ou meia-risca, que é separado do algarismo e do texto por um espaço em branco: I – ; II – ; III – etc."
- `manual.txt:5282-5285` — "As alíneas são representadas por letras e constituem desdobramentos dos incisos e dos parágrafos. A alínea ou a letra será grafada em minúsculo, seguida de parêntese e separada do texto por um espaço em branco: a) ; b) ; c) etc. Quando iniciar o texto e, quando citada ao longo do texto, será grafada em minúsculo, entre aspas e sem o parêntese."
- `manual.txt:5296-5297` — "Os itens são desdobramentos de alíneas e são representados por números cardinais, seguidos de ponto-final e separados do texto por um espaço em branco: 1. ; 2. ; 3 etc."

**Desdobramento dos dispositivos (seção 16.2.1).**

- `manual.txt:5203-5204` — "Os artigos podem desdobrar-se, por sua vez, em parágrafos e incisos; os parágrafos em incisos; estes, em alíneas; e estas, em itens."

**Uso de "caput".** Não encontrei no Manual seção própria com regra sobre o uso de "caput". Nos exemplos abaixo, o Manual escreve "caput" ao citar inciso ligado diretamente ao artigo:

- `manual.txt:1586` — "(Constituição, art. 64, caput)."
- `manual.txt:4239` — "omissão legislativa – como o mandado de injunção (Constituição, art. 5o, caput, inciso LXXI) e a"
- `manual.txt:4374-4375` — "Tal como a Constituição de 1967/1969 (art. 119, caput, inciso I, alínea “p”), a Constituição de 1988 (art. 102, caput, inciso I, alínea “p”) outorgou ao Supremo Tribunal Federal"
- `manual.txt:4454-4456` — "A Constituição consagra, no art. 5o, caput, inciso XXXIX, exigência expressa de previsão legal para a definição de crime e a cominação de pena, e proíbe a retroatividade da lei penal (Constituição, art. 5o, caput, inciso XL). Exige que o crime seja previsto em lei escrita e veda a"
- `manual.txt:5848` — "III – o inciso II do caput do art. 41; e"
- `manual.txt:5859` — "III – os incisos II e III do caput e o parágrafo único do art. 28;"

O Manual também explica a função do caput em relação aos incisos e parágrafos:

- `manual.txt:5188-5189` — "Quando o assunto requerer discriminações, o enunciado comporá o caput do artigo, e os elementos de discriminação serão apresentados sob a forma de incisos;"

**Remissões (seção 14.2.6).**

- `manual.txt:4520-4521` — "Por fim, deve-se indicar expressamente o dispositivo objeto de remissão interna, em vez de usar as expressões “anterior”, “seguinte” ou equivalentes."

**Lei Complementar nº 95, de 1998, art. 10, I a IV, e art. 11, II, g** (`lcp95.txt`, Planalto, https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95.htm):

- `lcp95.txt:48` — "Art. 10. Os textos legais serão articulados com observância dos seguintes princípios:"
- `lcp95.txt:49` — "I - a unidade básica de articulação será o artigo, indicado pela abreviatura "Art.", seguida de numeração ordinal até o nono e cardinal a partir deste;"
- `lcp95.txt:50` — "II - os artigos desdobrar-se-ão em parágrafos ou em incisos; os parágrafos em incisos, os incisos em alíneas e as alíneas em itens;"
- `lcp95.txt:51` — "III - os parágrafos serão representados pelo sinal gráfico "§", seguido de numeração ordinal até o nono e cardinal a partir deste, utilizando-se, quando existente apenas um, a expressão "parágrafo único" por extenso;"
- `lcp95.txt:52` — "IV - os incisos serão representados por algarismos romanos, as alíneas por letras minúsculas e os itens por algarismos arábicos;"
- `lcp95.txt:72` — "g) indicar, expressamente o dispositivo objeto de remissão, em vez de usar as expressões ‘anterior’, ‘seguinte’ ou equivalentes; (Incluída pela Lei Complementar nº 107, de 26.4.2001)"

Resumo das regras conferidas: "Art." no início do dispositivo e "art." no meio do texto; numeração ordinal até o nono (art. 9º, § 9º) e cardinal a partir do dez (art. 10, § 10); "parágrafo único" por extenso, nunca "§ único"; incisos em algarismos romanos; alíneas em letras minúsculas; itens em algarismos arábicos; alínea citada no texto vem entre aspas e sem parêntese; forma de remissão do Manual e do Decreto nº 12.002, de 2024: "art. 1º, caput, inciso I, alínea 'a'".

## 6. Demais normas buscadas hoje

### Código Penal (Decreto-Lei nº 2.848, de 7 de dezembro de 1940)

Fonte: `cp.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm).

- `cp.txt:5` — "DECRETO-LEI No 2.848, DE 7 DE DEZEMBRO DE 1940"

Arts. 1º e 2º:

- `cp.txt:24` — "Art. 1º - Não há crime sem lei anterior que o defina. Não há pena sem prévia cominação legal. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:26` — "Art. 2º - Ninguém pode ser punido por fato que lei posterior deixa de considerar crime, cessando em virtude dela a execução e os efeitos penais da sentença condenatória. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:27` — "Parágrafo único - A lei posterior, que de qualquer modo favorecer o agente, aplica-se aos fatos anteriores, ainda que decididos por sentença condenatória transitada em julgado. (Redação dada pela Lei nº 7.209, de 11.7.1984)"

Art. 10:

- `cp.txt:69` — "Art. 10 - O dia do começo inclui-se no cômputo do prazo. Contam-se os dias, os meses e os anos pelo calendário comum. (Redação dada pela Lei nº 7.209, de 11.7.1984)"

Art. 13:

- `cp.txt:77` — "Art. 13 - O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa. Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:79` — "§ 1º - A superveniência de causa relativamente independente exclui a imputação quando, por si só, produziu o resultado; os fatos anteriores, entretanto, imputam-se a quem os praticou. (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:81` — "§ 2º - A omissão é penalmente relevante quando o omitente devia e podia agir para evitar o resultado. O dever de agir incumbe a quem:(Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:82` — "a) tenha por lei obrigação de cuidado, proteção ou vigilância; (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:83` — "b) de outra forma, assumiu a responsabilidade de impedir o resultado; (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:84` — "c) com seu comportamento anterior, criou o risco da ocorrência do resultado. (Incluído pela Lei nº 7.209, de 11.7.1984)"

Arts. 17 e 18:

- `cp.txt:97` — "Art. 17 - Não se pune a tentativa quando, por ineficácia absoluta do meio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.(Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:98` — "Art. 18 - Diz-se o crime: (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:100` — "I - doloso, quando o agente quis o resultado ou assumiu o risco de produzi-lo;(Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:102` — "II - culposo, quando o agente deu causa ao resultado por imprudência, negligência ou imperícia. (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:103` — "Parágrafo único - Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime, senão quando o pratica dolosamente. (Incluído pela Lei nº 7.209, de 11.7.1984)"

Arts. 20 a 25:

- `cp.txt:107` — "Art. 20 - O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo, mas permite a punição por crime culposo, se previsto em lei. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:109` — "§ 1º - É isento de pena quem, por erro plenamente justificado pelas circunstâncias, supõe situação de fato que, se existisse, tornaria a ação legítima. Não há isenção de pena quando o erro deriva de culpa e o fato é punível como crime culposo.(Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:111` — "§ 2º - Responde pelo crime o terceiro que determina o erro. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:113` — "§ 3º - O erro quanto à pessoa contra a qual o crime é praticado não isenta de pena. Não se consideram, neste caso, as condições ou qualidades da vítima, senão as da pessoa contra quem o agente queria praticar o crime. (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:115` — "Art. 21 - O desconhecimento da lei é inescusável. O erro sobre a ilicitude do fato, se inevitável, isenta de pena; se evitável, poderá diminuí-la de um sexto a um terço. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:116` — "Parágrafo único - Considera-se evitável o erro se o agente atua ou se omite sem a consciência da ilicitude do fato, quando lhe era possível, nas circunstâncias, ter ou atingir essa consciência. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:118` — "Art. 22 - Se o fato é cometido sob coação irresistível ou em estrita obediência a ordem, não manifestamente ilegal, de superior hierárquico, só é punível o autor da coação ou da ordem. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:120` — "Art. 23 - Não há crime quando o agente pratica o fato: (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:121` — "I - em estado de necessidade; (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:122` — "II - em legítima defesa; (Incluído pela Lei nº 7.209, de 11.7.1984) (Vide ADPF 779)"
- `cp.txt:123` — "III - em estrito cumprimento de dever legal ou no exercício regular de direito. (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:125` — "Parágrafo único - O agente, em qualquer das hipóteses deste artigo, responderá pelo excesso doloso ou culposo. (Incluído pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:127` — "Art. 24 - Considera-se em estado de necessidade quem pratica o fato para salvar de perigo atual, que não provocou por sua vontade, nem podia de outro modo evitar, direito próprio ou alheio, cujo sacrifício, nas circunstâncias, não era razoável exigir-se. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:128` — "§ 1º - Não pode alegar estado de necessidade quem tinha o dever legal de enfrentar o perigo. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:129` — "§ 2º - Embora seja razoável exigir-se o sacrifício do direito ameaçado, a pena poderá ser reduzida de um a dois terços. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:131` — "Art. 25 - Entende-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão, atual ou iminente, a direito seu ou de outrem. (Redação dada pela Lei nº 7.209, de 11.7.1984) (Vide ADPF 779)"
- `cp.txt:132` — "Parágrafo único. Observados os requisitos previstos no caput deste artigo, considera-se também em legítima defesa o agente de segurança pública que repele agressão ou risco de agressão a vítima mantida refém durante a prática de crimes. (Incluído pela Lei nº 13.964, de 2019) (Vide ADPF 779)"

Art. 103 (decadência):

- `cp.txt:505` — "Art. 103 - Salvo disposição expressa em contrário, o ofendido decai do direito de queixa ou de representação se não o exerce dentro do prazo de 6 (seis) meses, contado do dia em que veio a saber quem é o autor do crime, ou, no caso do § 3º do art. 100 deste Código, do dia em que se esgota o prazo para oferecimento da denúncia. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:506` — "Parágrafo único. Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decai do direito de queixa ou de representação se não o exerce no prazo de 12 (doze) meses, contado do dia em que veio a saber quem é o autor do crime, ou, no caso do § 3º do art. 100 deste Código, do dia em que se esgota o prazo para oferecimento da denúncia. (Incluído pela Lei nº 15.438, de 2026)"

Art. 107:

- `cp.txt:521` — "Art. 107 - Extingue-se a punibilidade: (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:522` — "I - pela morte do agente;"
- `cp.txt:523` — "II - pela anistia, graça ou indulto;"
- `cp.txt:524` — "III - pela retroatividade de lei que não mais considera o fato como criminoso;"
- `cp.txt:525` — "IV - pela prescrição, decadência ou perempção;"
- `cp.txt:526` — "V - pela renúncia do direito de queixa ou pelo perdão aceito, nos crimes de ação privada;"
- `cp.txt:527` — "VI - pela retratação do agente, nos casos em que a lei a admite;"
- `cp.txt:528` — "VII - (Revogado pela Lei nº 11.106, de 2005)"
- `cp.txt:529` — "VIII - (Revogado pela Lei nº 11.106, de 2005)"
- `cp.txt:530` — "IX - pelo perdão judicial, nos casos previstos em lei."

Art. 109:

- `cp.txt:533` — "Art. 109. A prescrição, antes de transitar em julgado a sentença final, salvo o disposto no § 1o do art. 110 deste Código, regula-se pelo máximo da pena privativa de liberdade cominada ao crime, verificando-se: (Redação dada pela Lei nº 12.234, de 2010)."
- `cp.txt:534` — "I - em vinte anos, se o máximo da pena é superior a doze;"
- `cp.txt:535` — "II - em dezesseis anos, se o máximo da pena é superior a oito anos e não excede a doze;"
- `cp.txt:536` — "III - em doze anos, se o máximo da pena é superior a quatro anos e não excede a oito;"
- `cp.txt:537` — "IV - em oito anos, se o máximo da pena é superior a dois anos e não excede a quatro;"
- `cp.txt:538` — "V - em quatro anos, se o máximo da pena é igual a um ano ou, sendo superior, não excede a dois;"
- `cp.txt:539` — "VI - em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano. (Redação dada pela Lei nº 12.234, de 2010)."
- `cp.txt:541` — "Parágrafo único - Aplicam-se às penas restritivas de direito os mesmos prazos previstos para as privativas de liberdade. (Redação dada pela Lei nº 7.209, de 11.7.1984)"

Art. 115:

- `cp.txt:567` — "Art. 115. São reduzidos de metade os prazos de prescrição quando o criminoso era, ao tempo do crime, menor de 21 (vinte e um) anos ou, na data da sentença, maior de 70 (setenta) anos, salvo se o crime envolver violência sexual contra a mulher. (Redação dada pela Lei nº 15.160, de 2025)"

Arts. 116 e 117:

- `cp.txt:569` — "Art. 116 - Antes de passar em julgado a sentença final, a prescrição não corre: (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:570` — "I - enquanto não resolvida, em outro processo, questão de que dependa o reconhecimento da existência do crime; (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:571` — "II - enquanto o agente cumpre pena no exterior; (Redação dada pela Lei nº 13.964, de 2019)"
- `cp.txt:573` — "III - na pendência de embargos de declaração ou de recursos aos Tribunais Superiores, quando inadmissíveis; e (Incluído pela Lei nº 13.964, de 2019)"
- `cp.txt:574` — "IV - enquanto não cumprido ou não rescindido o acordo de não persecução penal. (Incluído pela Lei nº 13.964, de 2019)"
- `cp.txt:575` — "Parágrafo único - Depois de passada em julgado a sentença condenatória, a prescrição não corre durante o tempo em que o condenado está preso por outro motivo. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:577` — "Art. 117 - O curso da prescrição interrompe-se: (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:578` — "I - pelo recebimento da denúncia ou da queixa; (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:579` — "II - pela pronúncia; (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:580` — "III - pela decisão confirmatória da pronúncia; (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:581` — "IV - pela publicação da sentença ou acórdão condenatórios recorríveis; (Redação dada pela Lei nº 11.596, de 2007)."
- `cp.txt:582` — "V - pelo início ou continuação do cumprimento da pena; (Redação dada pela Lei nº 9.268, de 1º.4.1996)"
- `cp.txt:583` — "VI - pela reincidência. (Redação dada pela Lei nº 9.268, de 1º.4.1996)"
- `cp.txt:584` — "§ 1º - Excetuados os casos dos incisos V e VI deste artigo, a interrupção da prescrição produz efeitos relativamente a todos os autores do crime. Nos crimes conexos, que sejam objeto do mesmo processo, estende-se aos demais a interrupção relativa a qualquer deles. (Redação dada pela Lei nº 7.209, de 11.7.1984)"
- `cp.txt:585` — "§ 2º - Interrompida a prescrição, salvo a hipótese do inciso V deste artigo, todo o prazo começa a correr, novamente, do dia da interrupção. (Redação dada pela Lei nº 7.209, de 11.7.1984)"

Situação: arts. 1º, 2º, 10, 13, 17, 18, 20 a 24 e 107 na redação da Lei nº 7.209, de 1984 (art. 107, VII e VIII, revogados pela Lei nº 11.106, de 2005). Art. 25: parágrafo único incluído pela Lei nº 13.964, de 2019. Art. 103: parágrafo único **incluído pela Lei nº 15.438, de 18 de junho de 2026**. Art. 109: caput e inciso VI na redação da Lei nº 12.234, de 2010. Art. 115: **redação da Lei nº 15.160, de 3 de julho de 2025**, que acrescentou a ressalva "salvo se o crime envolver violência sexual contra a mulher". Art. 116: incisos II a IV na redação da Lei nº 13.964, de 2019. Art. 117: inciso IV na redação da Lei nº 11.596, de 2007; incisos V e VI na redação da Lei nº 9.268, de 1996.

### Lei nº 12.234, de 5 de maio de 2010

Fonte: `l12234.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12234.htm).

- `l12234.txt:5` — "LEI Nº 12.234, DE 5 DE MAIO DE 2010."
- `l12234.txt:6` — "Altera os arts. 109 e 110 do Decreto-Lei no 2.848, de 7 de dezembro de 1940 - Código Penal."
- `l12234.txt:10` — "“Art. 109. A prescrição, antes de transitar em julgado a sentença final, salvo o disposto no § 1o do art. 110 deste Código, regula-se pelo máximo da pena privativa de liberdade cominada ao crime, verificando-se:"
- `l12234.txt:12` — "VI - em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano."
- `l12234.txt:17` — "Art. 3o Esta Lei entra em vigor na data de sua publicação."
- `l12234.txt:18` — "Art. 4o Revoga-se o § 2o do art. 110 do Código Penal."
- `l12234.txt:22` — "Este texto não substitui o publicado no DOU de 6.5.2010"

Data de publicação: DOU de 6.5.2010. Vigência: na data da publicação (art. 3º). O que mudou no art. 109, VI, do CP: o prazo passou de dois para três anos. Redação anterior, riscada na página não compilada do Código Penal (`cpfull.txt`, Planalto, https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm):

- `cpfull.txt:1383` — (riscado na fonte) "VI - em dois anos, se o máximo da pena é inferior a um ano."
- `cpfull.txt:1384` — "VI - em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano. (Redação dada pela Lei nº 12.234, de 2010)."

A mesma lei alterou o caput do art. 109 e o § 1º do art. 110 e revogou o § 2º do art. 110.

### Lei nº 15.160, de 3 de julho de 2025 (CP, arts. 65 e 115)

Fonte: `l15160.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15160.htm).

- `l15160.txt:5` — "LEI Nº 15.160, DE 3 DE JULHO DE 2025"
- `l15160.txt:14` — "“Art. 115. São reduzidos de metade os prazos de prescrição quando o criminoso era, ao tempo do crime, menor de 21 (vinte e um) anos ou, na data da sentença, maior de 70 (setenta) anos, salvo se o crime envolver violência sexual contra a mulher.” (NR)"
- `l15160.txt:15` — "Art. 3º Esta Lei entra em vigor na data de sua publicação."
- `l15160.txt:20` — "Este texto não substitui o publicado no DOU de 4.7.2025."

### Lei nº 15.438, de 18 de junho de 2026 (decadência em violência doméstica)

Fonte: `l15438.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15438.htm).

- `l15438.txt:5` — "LEI Nº 15.438, DE 18 DE JUNHO DE 2026"
- `l15438.txt:11` — "Parágrafo único. Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decai do direito de queixa ou de representação se não o exerce no prazo de 12 (doze) meses, contado do dia em que veio a saber quem é o autor do crime, ou, no caso do § 3º do art. 100 deste Código, do dia em que se esgota o prazo para oferecimento da denúncia.” (NR)"
- `l15438.txt:17` — "§ 2º Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decairá do direito de queixa ou de representação se não o exercer no prazo de 12 (doze) meses, contado do dia em que vier a saber quem é o autor do crime, ou, no caso do art. 29 deste Código, do dia em que se esgotar o prazo para o oferecimento de denúncia.” (NR)"
- `l15438.txt:18` — "Art. 5º Esta Lei entra em vigor na data de sua publicação."
- `l15438.txt:23` — "Este texto não substitui o publicado no DOU de 19.6.2026"

### Lei nº 15.272, de 26 de novembro de 2025 (CPP, arts. 310, 310-A e 312)

Fonte: `l15272.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15272.htm).

- `l15272.txt:5` — "LEI Nº 15.272, DE 26 DE NOVEMBRO DE 2025"
- `l15272.txt:30` — "Art. 2º Esta Lei entra em vigor na data de sua publicação."
- `l15272.txt:34` — "Este texto não substitui o publicado no DOU de 27.11.2025"

### Lei nº 15.358, de 24 de março de 2026 (Marco Legal do Combate ao Crime Organizado)

Fonte: `l15358.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15358.htm).

- `l15358.txt:5` — "LEI Nº 15.358, DE 24 DE MARÇO DE 2026"
- `l15358.txt:54` — "§ 8º Os homicídios cometidos por membros de organizações criminosas ultraviolentas, grupo paramilitar ou milícia privada, ou sua tentativa, quando conexos aos crimes a que se refere este artigo, serão julgados pelas Varas Criminais Colegiadas a que se refere o art. 1º-A da Lei nº 12.694, de 24 de julho de 2012."
- `l15358.txt:55` — "§ 9º A prática dos crimes previstos neste artigo é causa suficiente para decretação de prisão preventiva."
- `l15358.txt:333` — "I - no concurso entre a competência do júri e a de outro órgão da jurisdição comum, prevalecerá a competência do júri, salvo os casos de homicídios cometidos por membros de organizações criminosas ultraviolentas, grupo paramilitar ou milícia privada, ou sua tentativa, na forma do art. 2º da lei que institui o marco legal do combate ao crime organizado no Brasil;"
- `l15358.txt:336` — "Após receber o auto de prisão em flagrante, no prazo máximo de até 24 (vinte e quatro) horas após a realização da prisão, o juiz deverá promover, por meio de videoconferência em tempo real, audiência de custódia com a presença do acusado, seu advogado constituído ou membro da Defensoria Pública e o membro do Ministério Público, e, nessa audiência, o juiz deverá, fundamentadamente:"
- `l15358.txt:466` — "Art. 44. Esta Lei entra em vigor na data de sua publicação."
- `l15358.txt:474` — "Este texto não substitui o publicado no DOU de 25.3.2026."

Observação: o art. 2º, §§ 8º e 9º, e a nova redação do art. 78, I, do CPP criam exceção legal à competência do júri e regra própria de prisão preventiva para os crimes dessa lei.

### Lei nº 15.487, de 6 de agosto de 2026 (CPP, art. 313, VI)

Fonte: `l15487.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15487.htm).

- `l15487.txt:5` — "LEI Nº 15.487, DE 6 DE AGOSTO DE 2026"
- `l15487.txt:85` — "Art. 3º O caput do art. 313 do Decreto-Lei nº 3.689, de 3 de outubro de 1941 (Código de Processo Penal), passa a vigorar acrescido do seguinte inciso VI:"
- `l15487.txt:109` — "Art. 7º Esta Lei entra em vigor na data de sua publicação."
- `l15487.txt:117` — "Este texto não substitui o publicado no DOU de 7.8.2026"

### Lei nº 9.296, de 24 de julho de 1996 (arts. 2º, 4º e 5º)

Fonte: `l9296.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/leis/l9296.htm). Vigentes, na redação original.

- `l9296.txt:5` — "LEI Nº 9.296, DE 24 DE JULHO DE 1996."
- `l9296.txt:11` — "Art. 2° Não será admitida a interceptação de comunicações telefônicas quando ocorrer qualquer das seguintes hipóteses:"
- `l9296.txt:12` — "I - não houver indícios razoáveis da autoria ou participação em infração penal;"
- `l9296.txt:13` — "II - a prova puder ser feita por outros meios disponíveis;"
- `l9296.txt:14` — "III - o fato investigado constituir infração penal punida, no máximo, com pena de detenção."
- `l9296.txt:15` — "Parágrafo único. Em qualquer hipótese deve ser descrita com clareza a situação objeto da investigação, inclusive com a indicação e qualificação dos investigados, salvo impossibilidade manifesta, devidamente justificada."
- `l9296.txt:19` — "Art. 4° O pedido de interceptação de comunicação telefônica conterá a demonstração de que a sua realização é necessária à apuração de infração penal, com indicação dos meios a serem empregados."
- `l9296.txt:20` — "§ 1° Excepcionalmente, o juiz poderá admitir que o pedido seja formulado verbalmente, desde que estejam presentes os pressupostos que autorizem a interceptação, caso em que a concessão será condicionada à sua redução a termo."
- `l9296.txt:21` — "§ 2° O juiz, no prazo máximo de vinte e quatro horas, decidirá sobre o pedido."
- `l9296.txt:22` — "Art. 5° A decisão será fundamentada, sob pena de nulidade, indicando também a forma de execução da diligência, que não poderá exceder o prazo de quinze dias, renovável por igual tempo uma vez comprovada a indispensabilidade do meio de prova."
- `l9296.txt:69` — "Este texto não substitui o publicado no D.O.U. de 25.7.1996"

### Lei nº 12.850, de 2 de agosto de 2013 (art. 4º, §§ 10-A e 16)

Fonte: `l12850.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm).

- `l12850.txt:5` — "LEI Nº 12.850, DE 2 DE AGOSTO DE 2013"
- `l12850.txt:73` — "Art. 3º-A. O acordo de colaboração premiada é negócio jurídico processual e meio de obtenção de prova, que pressupõe utilidade e interesse públicos."
- `l12850.txt:144` — "§ 10-A Em todas as fases do processo, deve-se garantir ao réu delatado a oportunidade de manifestar-se após o decurso do prazo concedido ao réu que o delatou. (Incluído pela Lei nº 13.964, de 2019)"
- `l12850.txt:157` — "§ 16. Nenhuma das seguintes medidas será decretada ou proferida com fundamento apenas nas declarações do colaborador: (Redação dada pela Lei nº 13.964, de 2019)"
- `l12850.txt:159` — "I - medidas cautelares reais ou pessoais; (Incluído pela Lei nº 13.964, de 2019)"
- `l12850.txt:161` — "II - recebimento de denúncia ou queixa-crime; (Incluído pela Lei nº 13.964, de 2019)"
- `l12850.txt:163` — "III - sentença condenatória. (Incluído pela Lei nº 13.964, de 2019)"

Situação: § 10-A incluído e § 16 com redação da Lei nº 13.964, de 2019. A redação anterior do § 16 ("Nenhuma sentença condenatória será proferida com fundamento apenas nas declarações de agente colaborador") está riscada em `l12850.txt:156`. As alterações de 2025 e 2026 (Leis nº 15.245 e nº 15.487) não atingem esses parágrafos.

### Lei nº 11.343, de 23 de agosto de 2006 (art. 28, § 2º; art. 33, § 1º, IV; art. 57)

Fonte: `l11343.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm).

- `l11343.txt:5` — "LEI Nº 11.343, DE 23 DE AGOSTO DE 2006"
- `l11343.txt:409` — "§ 2º Para determinar se a droga destinava-se a consumo pessoal, o juiz atenderá à natureza e à quantidade da substância apreendida, ao local e às condições em que se desenvolveu a ação, às circunstâncias sociais e pessoais, bem como à conduta e aos antecedentes do agente."
- `l11343.txt:453` — "§ 1º Nas mesmas penas incorre quem:"
- `l11343.txt:457` — "IV - vende ou entrega drogas ou matéria-prima, insumo ou produto químico destinado à preparação de drogas, sem autorização ou em desacordo com a determinação legal ou regulamentar, a agente policial disfarçado, quando presentes elementos probatórios razoáveis de conduta criminal preexistente. (Incluído pela Lei nº 13.964, de 2019)"
- `l11343.txt:565` — "Art. 57. Na audiência de instrução e julgamento, após o interrogatório do acusado e a inquirição das testemunhas, será dada a palavra, sucessivamente, ao representante do Ministério Público e ao defensor do acusado, para sustentação oral, pelo prazo de 20 (vinte) minutos para cada um, prorrogável por mais 10 (dez), a critério do juiz."

Situação: art. 28, § 2º, na redação original. Art. 33, § 1º, IV, incluído pela Lei nº 13.964, de 2019. A Lei nº 15.358, de 2026, incluiu o art. 40-A (`l11343.txt:490-493`); não alterou os dispositivos acima. DOU de 24.8.2006 (`l11343.txt:1013`).

### Lei nº 9.099, de 26 de setembro de 1995 (art. 89)

Fonte: `l9099.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/leis/l9099.htm). Vigente, redação original. DOU de 27.9.1995.

- `l9099.txt:5` — "LEI Nº 9.099, DE 26 DE SETEMBRO DE 1995."
- `l9099.txt:302` — "Art. 89. Nos crimes em que a pena mínima cominada for igual ou inferior a um ano, abrangidas ou não por esta Lei, o Ministério Público, ao oferecer a denúncia, poderá propor a suspensão do processo, por dois a quatro anos, desde que o acusado não esteja sendo processado ou não tenha sido condenado por outro crime, presentes os demais requisitos que autorizariam a suspensão condicional da pena (art. 77 do Código Penal)."

### Lei nº 12.965, de 23 de abril de 2014 (art. 7º, II e III)

Fonte: `l12965.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm). Vigentes, redação original. DOU de 24.4.2014.

- `l12965.txt:5` — "LEI Nº 12.965, DE 23 DE ABRIL DE 2014"
- `l12965.txt:76` — "Art. 7º O acesso à internet é essencial ao exercício da cidadania, e ao usuário são assegurados os seguintes direitos:"
- `l12965.txt:78` — "II - inviolabilidade e sigilo do fluxo de suas comunicações pela internet, salvo por ordem judicial, na forma da lei;"
- `l12965.txt:79` — "III - inviolabilidade e sigilo de suas comunicações privadas armazenadas, salvo por ordem judicial;"

### Lei nº 8.906, de 4 de julho de 1994 (art. 7º, XIV)

Fonte: `l8906.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/leis/l8906.htm). DOU de 5.7.1994.

- `l8906.txt:5` — "LEI Nº 8.906, DE 4 DE JULHO DE 1994."
- `l8906.txt:49` — "Art. 7º São direitos do advogado:"
- `l8906.txt:73` — "XIV - examinar, em qualquer instituição responsável por conduzir investigação, mesmo sem procuração, autos de flagrante e de investigações de qualquer natureza, findos ou em andamento, ainda que conclusos à autoridade, podendo copiar peças e tomar apontamentos, em meio físico ou digital; (Redação dada pela Lei nº 13.245, de 2016)"
- `l8906.txt:148` — "§ 10. Nos autos sujeitos a sigilo, deve o advogado apresentar procuração para o exercício dos direitos de que trata o inciso XIV. (Incluído pela Lei nº 13.245, de 2016)"
- `l8906.txt:149` — "§ 11. No caso previsto no inciso XIV, a autoridade competente poderá delimitar o acesso do advogado aos elementos de prova relacionados a diligências em andamento e ainda não documentados nos autos, quando houver risco de comprometimento da eficiência, da eficácia ou da finalidade das diligências. (Incluído pela Lei nº 13.245, de 2016)"

Situação: inciso XIV na redação da Lei nº 13.245, de 2016. §§ 10 e 11 incluídos pela mesma lei.

### Lei nº 14.365, de 2 de junho de 2022 (inclui o art. 798-A no CPP)

Fonte: `l14365.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm).

- `l14365.txt:5` — "LEI Nº 14.365, DE 2 DE JUNHO DE 2022"
- `l14365.txt:162` — "Art. 4º O Decreto-Lei nº 3.689, de 3 de outubro de 1941 (Código de Processo Penal), passa a vigorar acrescido do seguinte art. 798-A:"
- `l14365.txt:163` — "“Art. 798-A. Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive, salvo nos seguintes casos:"
- `l14365.txt:164` — "I - que envolvam réus presos, nos processos vinculados a essas prisões;"
- `l14365.txt:165` — "II - nos procedimentos regidos pela Lei nº 11.340, de 7 de agosto de 2006 (Lei Maria da Penha);"
- `l14365.txt:166` — "III - nas medidas consideradas urgentes, mediante despacho fundamentado do juízo competente."
- `l14365.txt:167` — "Parágrafo único. Durante o período a que se refere o caput deste artigo, fica vedada a realização de audiências e de sessões de julgamento, salvo nas hipóteses dos incisos I, II e III do caput deste artigo.”"
- `l14365.txt:168` — "Art. 5º Esta Lei entra em vigor na data de sua publicação."
- `l14365.txt:175` — "Este texto não substitui o publicado no DOU de 3.6.2022"

### Lei nº 13.964, de 24 de dezembro de 2019

Fonte: `l13964.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13964.htm).

- `l13964.txt:5` — "LEI Nº 13.964, DE 24 DE DEZEMBRO DE 2019"
- `l13964.txt:557` — "Art. 20. Esta Lei entra em vigor após decorridos 30 (trinta) dias de sua publicação oficial."
- `l13964.txt:563` — "Este texto não substitui o publicado no DOU de 24.12.2019 - Edição extra"

### Lei Complementar nº 80, de 12 de janeiro de 1994 (intimação pessoal e prazo em dobro)

Fonte: `lcp80.txt` (Planalto, https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp80.htm). DOU de 13.1.1994. O mesmo texto aparece nos arts. 44, I (União), 89, I (Distrito Federal e Territórios) e 128, I (Estados), na redação da Lei Complementar nº 132, de 2009.

- `lcp80.txt:5` — "LEI COMPLEMENTAR Nº 80, DE 12 DE JANEIRO DE 1994"
- `lcp80.txt:315` — "Art. 44. São prerrogativas dos membros da Defensoria Pública da União:"
- `lcp80.txt:317` — "I – receber, inclusive quando necessário, mediante entrega dos autos com vista, intimação pessoal em qualquer processo e grau de jurisdição ou instância administrativa, contando-se-lhes em dobro todos os prazos; (Redação dada pela Lei Complementar nº 132, de 2009)."
- `lcp80.txt:591` — "Art. 89. São prerrogativas dos membros da Defensoria Pública do Distrito Federal e dos Territórios:"
- `lcp80.txt:593` — "I – receber, inclusive quando necessário, mediante entrega dos autos com vista, intimação pessoal em qualquer processo e grau de jurisdição ou instância administrativa, contando-se-lhes em dobro todos os prazos; (Redação dada pela Lei Complementar nº 132, de 2009)."
- `lcp80.txt:860` — "Art. 128. São prerrogativas dos membros da Defensoria Pública do Estado, dentre outras que a lei local estabelecer:"
- `lcp80.txt:862` — "I – receber, inclusive quando necessário, mediante entrega dos autos com vista, intimação pessoal em qualquer processo e grau de jurisdição ou instância administrativa, contando-se-lhes em dobro todos os prazos; (Redação dada pela Lei Complementar nº 132, de 2009)."

### Resolução CNJ nº 213, de 15 de dezembro de 2015

Fonte: `cnj213.txt` (CNJ, https://atos.cnj.jus.br/atos/detalhar/2234).

- `cnj213.txt:2` — "Resolução Nº 213 de 15/12/2015"
- `cnj213.txt:8` — "Dispõe sobre a apresentação de toda pessoa presa à autoridade judicial no prazo de 24 horas."
- `cnj213.txt:10` — "Alterado"
- `cnj213.txt:16` — "DJe/CNJ nº 1/2016, de 8 de janeiro de 2016, p. 2-13."
- `cnj213.txt:18` — "Resolução n. 254, de 4 de setembro de 2018"
- `cnj213.txt:19` — "Resolução n. 268, de 21 de novembro de 2018"
- `cnj213.txt:20` — "Resolução n. 414, de 2 de setembro de 2021"
- `cnj213.txt:21` — "Resolução n. 417, de 20 de setembro de 2021"
- `cnj213.txt:22` — "Resolução n. 562, de 3 de junho de 2024"

Data exata: 15 de dezembro de 2015. Publicação: DJe/CNJ nº 1/2016, de 8 de janeiro de 2016. Situação no portal do CNJ: "Alterado".

### Resolução CNJ nº 484, de 19 de dezembro de 2022

Fonte: `cnj484.txt` (CNJ, https://atos.cnj.jus.br/atos/detalhar/4883).

- `cnj484.txt:2` — "Resolução Nº 484 de 19/12/2022"
- `cnj484.txt:8` — "Estabelece diretrizes para a realização do reconhecimento de pessoas em procedimentos e processos criminais e sua avaliação no âmbito do Poder Judiciário."
- `cnj484.txt:10` — "Vigente"
- `cnj484.txt:16` — "DJe/CNJ nº 317/2022, de 21 de dezembro de 2022, p. 4-6."

Data exata: 19 de dezembro de 2022. Publicação: DJe/CNJ nº 317/2022, de 21 de dezembro de 2022. Situação no portal do CNJ: "Vigente".

## 7. Afirmações usadas em cálculos e textos do aplicativo

Cada afirmação foi tratada como hipótese e conferida contra o texto oficial. Nas fontes, os nomes de arquivo seguem a tabela da seção 1.

| Afirmação | Resultado | Correção ou nota | Fonte |
|---|---|---|---|
| 1. CPP, art. 396: prazo de dez dias para a resposta à acusação. | confirmada | Nenhuma. Nota para o cálculo: na citação por edital, o prazo começa a fluir do comparecimento pessoal do acusado ou do defensor constituído (art. 396, parágrafo único). Se a resposta não for apresentada, o juiz nomeia defensor, com vista dos autos por dez dias (art. 396-A, § 2º). | cpp.txt:1552-1555 (art. 396) e :1560 (art. 396-A, § 2º); https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 2a. CPP, art. 798, § 1º: não se computa o dia do começo e inclui-se o do vencimento. | confirmada | Nenhuma. | cpp.txt:2872; https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 2b. CPP, art. 798, § 3º: prazo que termina em domingo ou feriado prorroga-se até o dia útil imediato. | confirmada | Nenhuma. Nota: o texto fala em "domingo ou dia feriado". Não menciona o sábado. | cpp.txt:2874; https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 3. CPP, art. 798-A: suspensão dos prazos de 20 de dezembro a 20 de janeiro, com exceções. | confirmada | Nenhuma. O período é "entre 20 de dezembro e 20 de janeiro, inclusive". Exceções: I - casos que envolvam réus presos, nos processos vinculados a essas prisões; II - procedimentos regidos pela Lei nº 11.340, de 2006 (Lei Maria da Penha); III - medidas consideradas urgentes, mediante despacho fundamentado do juízo competente. No período também ficam vedadas audiências e sessões de julgamento, salvo nessas três hipóteses (parágrafo único). Artigo incluído pela Lei nº 14.365, de 2 de junho de 2022. | cpp.txt:2880-2889; l14365.txt:162-168; https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 4. CPP, arts. 401 e 532: até oito testemunhas no rito ordinário e cinco no sumário. | confirmada | Nenhuma. O limite é por parte: oito (ou cinco) arroladas pela acusação e oito (ou cinco) pela defesa. No rito ordinário, não entram na conta as que não prestam compromisso e as referidas (art. 401, § 1º). | cpp.txt:1585-1587 (art. 401) e :2156 (art. 532); https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 5a. CP, art. 109: prazos de 20, 16, 12, 8, 4 e 3 anos conforme a pena máxima. | confirmada | Nenhuma. Faixas: I - 20 anos, se o máximo da pena é superior a 12; II - 16 anos, se superior a 8 e não excede 12; III - 12 anos, se superior a 4 e não excede 8; IV - 8 anos, se superior a 2 e não excede 4; V - 4 anos, se igual a 1 ano ou, sendo superior, não excede 2; VI - 3 anos, se inferior a 1 ano. | cp.txt:533-539; https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| 5b. Antes da Lei nº 12.234/2010, o prazo do inciso VI do art. 109 do CP era de 2 anos. | confirmada | Nenhuma. Redação anterior: "VI - em dois anos, se o máximo da pena é inferior a um ano." Início de vigência da Lei nº 12.234, de 5 de maio de 2010: data da publicação (art. 3º), DOU de 6.5.2010. | cpfull.txt:1383-1384 (https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm); l12234.txt:12, :17 e :22; https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12234.htm |
| 6. CP, art. 115: redução dos prazos pela metade (menor de 21 anos ao tempo do crime; maior de 70 na data da sentença). | incompleta: dispositivo alterado | CP, art. 115: os prazos de prescrição são reduzidos de metade quando o agente era, ao tempo do crime, menor de 21 anos ou, na data da sentença, maior de 70 anos, salvo se o crime envolver violência sexual contra a mulher (redação da Lei nº 15.160, de 3 de julho de 2025, DOU de 4.7.2025, em vigor na publicação). O cálculo deve perguntar se o crime envolve violência sexual contra a mulher antes de aplicar a redução. Para fatos anteriores a 4.7.2025, considere o art. 5º, XL, da Constituição ("a lei penal não retroagirá, salvo para beneficiar o réu"); a aplicação da ressalva a esses fatos não foi conferida em jurisprudência. | cp.txt:567; l15160.txt:14, :15 e :20; cf.txt:104; https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15160.htm |
| 7. CP, art. 117, I: o recebimento da denúncia interrompe a prescrição. | confirmada | Nenhuma. Texto: "pelo recebimento da denúncia ou da queixa". | cp.txt:577-578; https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| 8. CP, art. 10: o dia do começo inclui-se no cômputo do prazo penal. | confirmada | Nenhuma. Texto: "O dia do começo inclui-se no cômputo do prazo. Contam-se os dias, os meses e os anos pelo calendário comum." | cp.txt:69; https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| 9. Data da norma: Decreto-Lei nº 3.689, de 3 de outubro de 1941. | confirmada | Nenhuma. | cpp.txt:5; https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| 9. Data da norma: Decreto-Lei nº 2.848, de 7 de dezembro de 1940. | confirmada | Nenhuma. | cp.txt:5; https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| 9. Data da norma: Lei nº 9.296, de 24 de julho de 1996. | confirmada | Nenhuma. | l9296.txt:5; https://www.planalto.gov.br/ccivil_03/leis/l9296.htm |
| 9. Data da norma: Lei nº 11.343, de 23 de agosto de 2006. | confirmada | Nenhuma. | l11343.txt:5; https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm |
| 9. Data da norma: Lei nº 12.850, de 2 de agosto de 2013. | confirmada | Nenhuma. | l12850.txt:5; https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm |
| 9. Data da norma: Lei nº 13.964, de 24 de dezembro de 2019. | confirmada | Nenhuma. | l13964.txt:5; https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13964.htm |
| 9. Data da norma: Lei nº 9.099, de 26 de setembro de 1995. | confirmada | Nenhuma. | l9099.txt:5; https://www.planalto.gov.br/ccivil_03/leis/l9099.htm |
| 9. Data da norma: Lei nº 8.906, de 4 de julho de 1994. | confirmada | Nenhuma. | l8906.txt:5; https://www.planalto.gov.br/ccivil_03/leis/l8906.htm |
| 9. Data da norma: Lei Complementar nº 80, de 12 de janeiro de 1994. | confirmada | Nenhuma. | lcp80.txt:5; https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp80.htm |
| 9. Data da norma: Lei nº 12.965, de 23 de abril de 2014. | confirmada | Nenhuma. | l12965.txt:5; https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm |
| 9. Data da norma: Lei nº 14.365, de 2 de junho de 2022. | confirmada | Nenhuma. | l14365.txt:5; https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm |
| 9. Data da norma: Decreto nº 678, de 6 de novembro de 1992. | confirmada | Nenhuma. | d678.txt:5; https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm |
| 9. Data da norma: Decreto nº 592, de 6 de julho de 1992. | confirmada | Nenhuma. | d592.txt:5; https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0592.htm |
| 9. Data da norma: Decreto nº 40, de 15 de fevereiro de 1991. | confirmada | Nenhuma. | d40.txt:5; https://www.planalto.gov.br/ccivil_03/decreto/1990-1994/d0040.htm |
| 9. Data da norma: Resolução CNJ nº 213, de 15 de dezembro de 2015. | confirmada | Nenhuma. | cnj213.txt:2; https://atos.cnj.jus.br/atos/detalhar/2234 |
| 9. Data da norma: Resolução CNJ nº 484, de 19 de dezembro de 2022. | confirmada | Nenhuma. | cnj484.txt:2; https://atos.cnj.jus.br/atos/detalhar/4883 |

