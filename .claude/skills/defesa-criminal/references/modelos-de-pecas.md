# Modelos das três peças

Os modelos fixam a estrutura e as frases de ligação. O conteúdo de cada tese vem de `teses-defensivas.md` (campo "Texto-base para a peça"). O que depende dos autos fica entre colchetes, em maiúsculas, para o usuário preencher.

Regras comuns:

- Numere as seções (1, 2, 3) e as subseções (3.1, 3.2). Título de seção em maiúsculas.
- Na primeira citação de cada norma, use o nome completo com a data; nas seguintes, a forma curta (ver `redacao-oficial.md`).
- Em cada tese, siga a ordem: norma, fato do processo, aplicação, precedentes, prejuízo.
- Os pedidos repetem a ordem dos argumentos, um por alínea.
- Feche com "Nesses termos, pede deferimento.", local, data por extenso, nome e inscrição na OAB (ou "Defensor Público").
- Endereçamento: a praxe forense usa "Excelentíssimo Senhor Juiz de Direito"; o Manual de Redação indica "Senhor Juiz". Pergunte ao usuário se ele não tiver dito qual prefere e use a praxe forense como padrão.

## 1. Resposta à acusação, com pedido de rejeição da denúncia e de absolvição sumária

**Base legal:** CPP, arts. 396, 396-A e 397; art. 395 para a rejeição.
**Prazo:** dez dias depois da citação (em dobro para a Defensoria Pública). Calcule com `scripts/calculos.py prazo`.
**Endereçamento:** juízo da ação penal.
**Atenção:** o rol de testemunhas deve vir nesta peça. Limite de oito por fato no rito ordinário e de cinco no sumário (CPP, arts. 401 e 532).

```
EXCELENTÍSSIMO SENHOR JUIZ DE DIREITO DA [VARA] DA COMARCA DE [COMARCA] – [UF]

Processo nº [NÚMERO]

[NOME DO ACUSADO], já qualificado nos autos, por seu defensor, [NOME], advogado inscrito na
[OAB/UF Nº], apresenta

RESPOSTA À ACUSAÇÃO

com fundamento nos arts. 396 e 396-A do Código de Processo Penal – CPP (Decreto-Lei nº 3.689,
de 3 de outubro de 1941), pelas razões a seguir.

1 SÍNTESE DA ACUSAÇÃO
O Ministério Público imputa ao acusado a prática do crime previsto no [TIPO PENAL].
[RESUMO DA NARRATIVA DA DENÚNCIA, EM UM PARÁGRAFO.]

2 TEMPESTIVIDADE
O acusado foi citado em [DATA]. A resposta é apresentada no prazo de dez dias do art. 396 do CPP.

3 QUESTÕES PRELIMINARES
3.1 [Título da tese]
[Norma] [Fato do processo, com documento e folhas ou ID] [Aplicação]
[Precedentes, em alíneas] [Prejuízo concreto]
3.2 [...]

4 EXTINÇÃO DA PUNIBILIDADE            (se houver)

5 ABSOLVIÇÃO SUMÁRIA                  (CPP, art. 397, I a III)
5.1 [Título da tese]

6 PEDIDOS SUBSIDIÁRIOS                (se houver)

7 LIBERDADE DO ACUSADO                (se houver réu preso e tese de prisão)

8 PROVAS
A defesa requer a produção das provas admitidas em direito, em especial [PERÍCIAS, DOCUMENTOS
E DILIGÊNCIAS], e a inquirição das testemunhas abaixo, que deverão ser intimadas (art. 396-A
do CPP):
1. [NOME], [QUALIFICAÇÃO E ENDEREÇO];
2. [...].

9 PEDIDOS
Ante o exposto, a defesa requer as seguintes providências, em ordem sucessiva:
a) [pedido da primeira preliminar];
b) [...];
c) [absolver sumariamente o acusado, com fundamento no art. 397, inciso ..., do CPP];
d) subsidiariamente, [...];
e) caso a ação penal prossiga, deferir a produção das provas requeridas e a intimação das
   testemunhas arroladas.

Nesses termos, pede deferimento.

[LOCAL], [DATA POR EXTENSO].

[NOME DO DEFENSOR]
[OAB/UF Nº]
```

Observações:

- Depois da resposta, o juiz pode absolver sumariamente (art. 397) ou manter o recebimento e designar audiência (art. 399). Peça a rejeição da denúncia nas preliminares e a absolvição sumária no mérito; os pedidos não se excluem.
- Teses de insuficiência de prova (palavra isolada de policiais, depoimentos só do inquérito) pertencem às alegações finais. Na resposta, só entram se servirem à falta de justa causa.
- A decisão que rejeita a absolvição sumária com fórmula genérica ("as matérias se confundem com o mérito") abre duas vias: arguição de nulidade por falta de fundamentação (tese `fundamentacao`) e habeas corpus.

## 2. Arguição de nulidade e pedido de desentranhamento de prova ilícita

**Base legal:** CPP, arts. 563 a 573 (nulidades) e art. 157 (provas ilícitas).
**Quando:** na primeira oportunidade depois do ato, por petição nos autos; ou como preliminar da resposta à acusação e das alegações finais.
**Endereçamento:** juízo da ação penal.

```
EXCELENTÍSSIMO SENHOR JUIZ DE DIREITO DA [VARA] DA COMARCA DE [COMARCA] – [UF]

Processo nº [NÚMERO]

[NOME DO ACUSADO], já qualificado nos autos, por seu defensor, [NOME], advogado inscrito na
[OAB/UF Nº], apresenta

ARGUIÇÃO DE NULIDADE

com fundamento nos arts. 157 e 563 a 573 do Código de Processo Penal – CPP (Decreto-Lei
nº 3.689, de 3 de outubro de 1941), pelas razões a seguir.

1 SÍNTESE DO PROCESSO
[ANDAMENTO E ATO IMPUGNADO, COM DATA E ID.]

2 OPORTUNIDADE DA ARGUIÇÃO
A arguição é apresentada na primeira oportunidade em que a defesa se manifesta nos autos
depois do ato impugnado, como exige o art. 571 do CPP. As nulidades absolutas e a ilicitude
da prova não se sujeitam a preclusão.

3 FUNDAMENTOS
3.1 [Título da tese]
[Norma] [Fato] [Aplicação] [Precedentes] [Prejuízo concreto]

4 EXTENSÃO DA NULIDADE
A nulidade de um ato, uma vez declarada, causa a dos atos que dele diretamente dependam ou
sejam consequência (art. 573, § 1º, do CPP). O juiz que pronunciar a nulidade declarará os
atos a que ela se estende (art. 573, § 2º). No caso, a nulidade alcança [ATOS DEPENDENTES].

5 PEDIDOS
Ante o exposto, a defesa requer as seguintes providências:
a) suspender a audiência de instrução e julgamento designada para [DATA] até a decisão desta
   arguição;                                           (se houver audiência designada)
b) [pedido de cada tese: declarar a nulidade de ..., desentranhar ...];
c) declarar os atos a que a nulidade se estende (art. 573, § 2º, do CPP) e determinar sua
   renovação.

Nesses termos, pede deferimento.
[LOCAL], [DATA]. [NOME]. [OAB/UF Nº].
```

Observações:

- Distinga na peça nulidade (ato do processo praticado em desacordo com a lei) e ilicitude (prova obtida com violação de direito). Para a prova ilícita, o pedido é declarar a inadmissibilidade e desentranhar (art. 157, caput e § 3º).
- Se a nulidade é relativa, a seção 2 é decisiva. Indique a data do ato e a da primeira manifestação da defesa, e mostre que o protesto constou da ata.
- Não confunda com exceção de suspeição ou de incompetência, que têm rito próprio (CPP, arts. 95 a 111).

## 3. Habeas corpus para trancamento da ação penal, com liminar para suspender a audiência

**Base legal:** Constituição, art. 5º, LXVIII; CPP, arts. 647, 648 e 654.
**Quem pode impetrar:** qualquer pessoa, em favor próprio ou de outrem (CPP, art. 654).
**Endereçamento:** tribunal a que o juiz está vinculado (Tribunal de Justiça ou Tribunal Regional Federal). Contra ato de tribunal, o STJ; contra ato do STJ, o STF.
**Prova:** documental e pré-constituída. Junte denúncia, decisão impugnada, peças do inquérito citadas e, se houver, o despacho que designou a audiência.

```
EXCELENTÍSSIMO SENHOR DESEMBARGADOR PRESIDENTE DO [TRIBUNAL]

[NOME DO IMPETRANTE], advogado inscrito na [OAB/UF Nº], impetra

HABEAS CORPUS, COM PEDIDO DE LIMINAR,

em favor de [NOME DO PACIENTE], [QUALIFICAÇÃO], contra ato do Juízo da [VARA] da Comarca de
[COMARCA], praticado na Ação Penal nº [NÚMERO], com fundamento no art. 5º, caput, inciso
LXVIII, da Constituição e nos arts. 647 e 648 do Código de Processo Penal – CPP (Decreto-Lei
nº 3.689, de 3 de outubro de 1941), pelas razões a seguir.

1 SÍNTESE DOS FATOS E DO ATO COATOR
[IMPUTAÇÃO E RESUMO DA DENÚNCIA.]
A autoridade coatora [ATO: RECEBEU A DENÚNCIA / REJEITOU A ABSOLVIÇÃO SUMÁRIA / INDEFERIU A
ARGUIÇÃO DE NULIDADE, COM DATA E ID] e designou audiência de instrução e julgamento para [DATA].

2 CABIMENTO
Dar-se-á habeas corpus sempre que alguém sofrer ou se achar na iminência de sofrer violência
ou coação ilegal na sua liberdade de ir e vir (art. 647 do CPP). A coação é ilegal, entre
outras hipóteses, quando não houver justa causa, quando o processo for manifestamente nulo e
quando extinta a punibilidade (art. 648, caput, incisos I, VI e VII, do CPP).
O trancamento da ação penal por habeas corpus é medida excepcional. Os tribunais superiores o
admitem quando a ilegalidade se verifica de plano, sem exame aprofundado de provas. É o que
ocorre neste caso: as questões a seguir são de direito e se demonstram com os documentos que
instruem esta impetração.

3 CONSTRANGIMENTO ILEGAL
3.1 [Título da tese]
[Norma] [Fato] [Aplicação] [Precedentes] [Prejuízo]

4 LIMINAR
A plausibilidade do direito resulta dos fundamentos expostos, demonstrados por prova
documental. O perigo da demora decorre da audiência de instrução e julgamento designada para
[DATA]. A realização do ato antes do julgamento desta impetração tornaria ineficaz a ordem que
vier a ser concedida.

5 PEDIDOS
Ante o exposto, o impetrante requer as seguintes providências, em ordem sucessiva:
a) conceder a liminar para suspender o curso da Ação Penal nº [NÚMERO] e a audiência designada
   para [DATA], até o julgamento deste habeas corpus;
b) requisitar informações à autoridade coatora e ouvir o Ministério Público;
c) no mérito, conceder a ordem para trancar a Ação Penal nº [NÚMERO];
d) subsidiariamente, conceder a ordem para [pedido de cada tese].

Instruem esta impetração cópias da denúncia, da decisão impugnada e das peças mencionadas.

Nesses termos, pede deferimento.
[LOCAL], [DATA]. [NOME]. [OAB/UF Nº].
```

Observações:

- **"Trancar a AIJ".** O que se tranca é a ação penal. A audiência se suspende por liminar. Explique isso ao usuário e peça as duas coisas.
- **Momento.** Impetre antes da sentença. A sentença condenatória prejudica o pedido de trancamento por falta de justa causa (Súmula 648 do STJ). Em regra, espere a decisão do juiz sobre a resposta à acusação: sem ela, o tribunal pode apontar supressão de instância.
- **O que serve ao trancamento.** Atipicidade evidente, extinção da punibilidade, inépcia da denúncia, falta de justa causa e ilicitude da prova que seja a única base da acusação. Teses que dependem de valorar depoimentos não servem.
- **Prova pré-constituída.** O habeas corpus não admite produção de prova. Cada afirmação de fato deve remeter a documento juntado.
- **Liminar negada por relator de tribunal superior.** Em regra, não cabe novo habeas corpus ao STF contra essa decisão (Súmula 691 do STF). Avise o usuário antes de sugerir essa via.
- **Réu preso.** Se houver tese de ilegalidade da prisão, acrescente o pedido de liberdade na liminar e no mérito.
- No habeas corpus, a pessoa defendida é o **paciente**. Troque "acusado" por "paciente" no texto das teses.
