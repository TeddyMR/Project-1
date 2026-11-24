# Roteiro de análise do processo

> Arquivo gerado por `scripts/montar.py` a partir de `assets/dados/`. Não edite à mão: altere os dados e rode o script.

Percorra os autos na ordem dos atos. Para cada pergunta, consulte o documento indicado.
Resposta “sim” indica a tese a examinar em `teses-defensivas.md`. Sem o documento em mãos, registre
a pergunta como pendência e não presuma a resposta.

## Abordagem, buscas e investigação

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| A revista pessoal foi justificada só por “atitude suspeita”, nervosismo, local ou denúncia anônima não verificada? | auto de prisão em flagrante e depoimentos dos condutores | Busca pessoal sem fundada suspeita (`busca-pessoal`) |
| Houve entrada em residência sem mandado judicial? | auto de prisão em flagrante, auto de apreensão e depoimentos | Ingresso em domicílio sem mandado e sem fundadas razões (`busca-domiciliar`) |
| O conteúdo do celular foi acessado antes de decisão judicial? | relatório policial, auto de apreensão e decisão de quebra de sigilo (compare as datas) | Acesso a dados de aparelho celular sem autorização judicial (`celular`) |
| Há capturas de tela ou extração de dados sem perícia, sem código hash ou sem acesso da defesa à íntegra? | laudo ou relatório de extração e mídias juntadas | Prova digital sem preservação da cadeia de custódia (`prova-digital`) |
| Há divergência de lacre, peso ou descrição entre o auto de apreensão e o laudo, ou intervalo de guarda sem registro? | auto de apreensão, guia de remessa e laudo pericial | Quebra da cadeia de custódia do vestígio (`cadeia-custodia`) |
| Há interceptação telefônica com decisão genérica, prorrogações padronizadas ou período sem cobertura judicial? | autos da medida cautelar: decisões e relatórios, com as datas | Interceptação telefônica em desacordo com a lei (`interceptacao`) |
| O acusado foi reconhecido por fotografia isolada, sozinho, ou sem descrição prévia e auto formal? | termo ou auto de reconhecimento e depoimento da vítima | Reconhecimento de pessoa em desacordo com o art. 226 do CPP (`reconhecimento`) |
| A acusação menciona confissão informal, feita aos policiais, sem advertência do direito ao silêncio e sem registro? | depoimentos dos condutores e termo de interrogatório policial | Confissão informal ou extrajudicial sem garantias (`confissao`) |
| Há lesões ou relato de agressão, ameaça ou coação no momento da prisão? | laudo de exame de corpo de delito do preso e ata da audiência de custódia | Prova obtida mediante tortura, violência ou ameaça (`tortura`) |
| O crime deixa vestígios e não há laudo pericial definitivo nos autos? | laudos e auto de apreensão | Ausência de exame de corpo de delito (`corpo-delito`) |
| As demais provas foram obtidas a partir de alguma das medidas acima? | relatório final do inquérito, na ordem cronológica das diligências | Provas derivadas das ilícitas (`derivadas`) |
| A defesa teve negado o acesso a mídias, autos apartados ou à íntegra de dados já documentados? | pedidos da defesa, respostas e certidões | Negativa de acesso da defesa aos elementos de prova já documentados (`acesso-autos`) |
| A conduta foi provocada por policial ou por pessoa a serviço da polícia? | depoimentos dos agentes e relatório da operação | Flagrante preparado e crime impossível (`flagrante-preparado`) |

## Prisão e custódia

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| A prisão preventiva foi decretada sem pedido do Ministério Público e sem representação da autoridade policial? | decisão que decretou a prisão e ata da audiência de custódia | Prisão preventiva decretada sem requerimento (`preventiva-oficio`) |
| O preso deixou de ser apresentado ao juiz em audiência de custódia? | ata da audiência de custódia ou certidão de sua não realização | Ausência de audiência de custódia (`custodia`) |
| A decisão de prisão se apoia na gravidade abstrata do crime, sem fato concreto e atual? | decisão que decretou ou manteve a prisão | Prisão preventiva sem fundamentos concretos e atuais (`preventiva-fundamentacao`) |
| O acusado está preso há tempo excessivo por atrasos atribuíveis ao Estado? | andamento processual, com as datas dos adiamentos e seus motivos | Excesso de prazo da prisão ou do processo (`excesso-prazo`) |
| O acusado ficou algemado em audiência ou julgamento sem decisão escrita que justificasse? | ata e gravação da audiência | Uso injustificado de algemas (`algemas`) |

## Denúncia e admissibilidade

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| O juízo é incompetente em razão da matéria ou da pessoa? | denúncia e decisão de recebimento | Incompetência absoluta do juízo (`incompetencia`) |
| A denúncia deixa de descrever a conduta individual do acusado, ou o tempo, o lugar e o modo do fato? | denúncia | Inépcia da denúncia (`inepcia`) |
| Falta representação da vítima, legitimidade da parte, lançamento definitivo do tributo ou prova nova após arquivamento? | denúncia, termo de representação e certidões | Falta de pressuposto processual ou de condição da ação penal (`condicao-acao`) |
| A denúncia se apoia apenas na palavra de colaborador? | denúncia, termos de colaboração e documentos que a acompanham | Declarações de colaborador sem corroboração (`colaboracao`) |
| Excluídas as provas inválidas, a denúncia fica sem lastro mínimo de autoria ou de materialidade? | denúncia e peças do inquérito que a instruem | Falta de justa causa para a ação penal (`justa-causa`) |
| Pelas datas e pela pena máxima, pode ter ocorrido prescrição ou decadência? | data do fato, data do recebimento da denúncia e pena cominada (use o verificador abaixo) | Extinção da punibilidade (`punibilidade`) |
| Mesmo admitidos como verdadeiros, os fatos narrados deixam de preencher algum elemento do tipo penal? | denúncia e texto do tipo penal | O fato narrado não constitui crime (`atipicidade`) |
| O bem tem valor ínfimo e o fato ocorreu sem violência ou grave ameaça? | auto de avaliação, termo de restituição e folha de antecedentes | Atipicidade material (princípio da insignificância) (`insignificancia`) |
| A imputação é de tráfico por pequena quantidade de maconha, sem sinais de comércio? | laudo de constatação, auto de apreensão e auto de prisão | Porte de maconha para consumo pessoal (`porte-maconha`) |
| Os autos já mostram, de forma clara, legítima defesa, estado de necessidade ou outra excludente da ilicitude? | laudos, imagens e depoimentos do inquérito | Causa excludente da ilicitude (`excludente-ilicitude`) |
| Os autos já mostram, de forma clara, coação irresistível, obediência hierárquica ou erro inevitável sobre a ilicitude? | depoimentos, mensagens e registros de ameaça | Causa excludente da culpabilidade (`excludente-culpabilidade`) |

## Citação e defesa

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| A citação foi feita por edital sem esgotamento dos meios de localização, ou com o acusado preso? | mandado, certidão do oficial de justiça e edital | Citação inexistente ou inválida (`citacao`) |
| Algum ato ocorreu sem defensor, ou a defesa anterior foi inerte? | atas de audiência e peças da defesa anterior | Ausência de defesa técnica ou defesa meramente formal (`defesa-tecnica`) |
| A defesa deixou de ser intimada de audiência, de carta precatória ou de decisão? | certidões de intimação e publicações | Falta de intimação da defesa para ato do processo (`intimacao`) |

## Audiência e instrução

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| O acusado foi interrogado antes de ouvidas todas as testemunhas? | ata e gravação da audiência | Interrogatório realizado antes do fim da prova oral (`interrogatorio`) |
| O juiz conduziu a inquirição das testemunhas ou produziu, de ofício, prova da acusação? | gravação da audiência e ata, com o registro do protesto | Atuação do juiz em substituição à acusação (`sistema-acusatorio`) |
| O juiz indeferiu prova da defesa sem explicar por que seria irrelevante ou protelatória? | requerimento da defesa e decisão que o indeferiu | Indeferimento imotivado de prova requerida pela defesa (`prova-indeferida`) |
| O delatado apresentou alegações finais antes do colaborador ou no mesmo prazo? | despacho que abriu o prazo e datas das alegações finais | Alegações finais do delatado antes ou junto com as do delator (`delator-delatado`) |
| A prova de autoria se resume a depoimentos do inquérito não repetidos em juízo ou a testemunhas de “ouvir dizer”? | termos de depoimento da fase policial e da fase judicial | Acusação apoiada só em elementos do inquérito ou em testemunho indireto (`inquerito-exclusivo`) |
| A acusação se apoia só na palavra dos policiais que fizeram a prisão, sem imagem, perícia ou testemunha civil? | depoimentos judiciais e rol de provas da acusação | Acusação apoiada apenas na palavra dos agentes que efetuaram a prisão (`policial-exclusivo`) |

## Decisões e sentença

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| A decisão que analisou a resposta à acusação, a prova ou a prisão usou fundamentação genérica? | a própria decisão, comparada com a peça da defesa | Decisão sem fundamentação (`fundamentacao`) |
| Há causa de impedimento ou de suspeição do juiz, ou sinais de perda de imparcialidade? | decisões, despachos e atas de audiência | Impedimento, suspeição ou quebra da imparcialidade do julgador (`parcialidade`) |
| A sentença condenou por fato ou circunstância que a denúncia não descreve? | denúncia, eventual aditamento e sentença | Sentença em desacordo com a acusação (`correlacao`) |

## Saídas alternativas

| Pergunta | Onde conferir | Se sim, tese |
|---|---|---|
| O crime é sem violência ou grave ameaça, com pena mínima inferior a quatro anos, e o acordo de não persecução penal não foi oferecido? | denúncia e manifestação do Ministério Público sobre o acordo | Acordo de não persecução penal (`anpp`) |
| A pena mínima é de até um ano e a suspensão condicional do processo não foi proposta? | denúncia e folha de antecedentes | Suspensão condicional do processo (`sursis-processual`) |
| Os fatos correspondem a crime menos grave do que o indicado na denúncia? | denúncia e texto dos tipos penais | Desclassificação para infração menos grave (`desclassificacao`) |
