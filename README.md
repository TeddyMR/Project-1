# Defesa criminal: skill e oficina interativa

Este repositório traz uma skill para o Claude e um aplicativo de página única que apoiam a defesa em processo criminal brasileiro.

O que faz:

- analisa o processo por fases e indica o documento a consultar em cada ponto;
- liga cada vício à garantia do art. 5º da Constituição e o classifica (nulidade absoluta, nulidade relativa, prova ilícita);
- refuta as bases da acusação, com a réplica previsível do Ministério Público e a resposta;
- ordena os argumentos e os pedidos;
- monta minuta de resposta à acusação com absolvição sumária, de arguição de nulidade e de habeas corpus para trancamento da ação penal com liminar para suspender a audiência de instrução e julgamento;
- cita somente precedentes de uma base conferida, com fonte e data, e confere as citações de qualquer texto.

O que não faz: não substitui advogado nem defensor público, não promete resultado e não dispensa a leitura do inteiro teor dos precedentes antes do protocolo.

## Onde está cada coisa

```
.claude/skills/defesa-criminal/
├── SKILL.md                      instruções da skill
├── references/                   material de consulta (parte é gerada a partir dos dados)
├── assets/
│   ├── dados/                    base: teses, precedentes, roteiro, estrutura
│   └── app/
│       ├── oficina-defesa-penal.html   aplicativo pronto (abrir no navegador)
│       ├── oficina.src.html            fonte do aplicativo
│       └── capa.jpg                    imagem de capa
├── scripts/
│   ├── montar.py                 valida a base e gera aplicativo e referências
│   ├── verificar_citacoes.py     confere as citações de um texto
│   ├── calculos.py               prazo da resposta e prescrição, com a conta
│   └── testes.py                 testes dos scripts
└── evals/                        casos de teste da skill
```

## Como usar

**Com o Claude Code.** Abra o repositório. A skill `defesa-criminal` é carregada do diretório `.claude/skills/`. Descreva o caso ou envie as peças do processo.

**Sem o Claude.** Abra `.claude/skills/defesa-criminal/assets/app/oficina-defesa-penal.html` no navegador, com `capa.jpg` na mesma pasta. Os dados do caso ficam no navegador e não são enviados a servidor.

**Linha de comando.**

```bash
cd .claude/skills/defesa-criminal
python3 scripts/calculos.py prazo --citacao 2026-11-16
python3 scripts/calculos.py prescricao --fato 2015-03-10 --pena-max-anos 4 --recebimento 2020-01-15
python3 scripts/verificar_citacoes.py minuta.txt
python3 scripts/montar.py          # depois de alterar assets/dados/
python3 scripts/testes.py
```

## Como a base é mantida

Cada precedente em `assets/dados/precedentes.json` traz a URL consultada e a data da conferência. `scripts/montar.py` recusa registro sem fonte e tese que cite precedente fora da base. A jurisprudência muda: reconfira os registros antes de usar, em especial os que têm ressalva de julgamento pendente.

## Aviso

Material de apoio e de estudo. A responsabilidade técnica pela peça é do advogado ou do defensor público que a assina.
