#!/usr/bin/env python3
"""Valida a base e gera o aplicativo e as referências da skill.

Uso:
    python3 scripts/montar.py                 # valida e gera tudo
    python3 scripts/montar.py --so-validar    # só valida
    python3 scripts/montar.py --fragmento CAMINHO.html   # também grava a página sem <html>/<head>

Rode sempre depois de alterar qualquer arquivo em assets/dados/.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base as B  # noqa: E402

RAIZ = B.RAIZ
REF = RAIZ / "references"
APP = RAIZ / "assets" / "app"
AVISO = ("> Arquivo gerado por `scripts/montar.py` a partir de `assets/dados/`. "
         "Não edite à mão: altere os dados e rode o script.\n")


def curto(txt: str, normas: dict) -> str:
    for k, v in normas.items():
        txt = txt.replace("{" + k + "}", v["depois"])
    return txt


def md_precedente(p: dict) -> str:
    linhas = [f"### {p['citacao']}", ""]
    if p.get("literal"):
        linhas.append(f"- Texto: “{p['literal']}”")
    linhas.append(f"- O que decidiu: {p['sintese']}")
    if p.get("integra"):
        linhas.append(f"- Íntegra da tese: “{p['integra']}”")
    if p.get("situacao"):
        linhas.append(f"- Situação: {p['situacao']}")
    if p.get("nota"):
        linhas.append(f"- Ressalva: {p['nota']}")
    linhas.append(f"- Fonte consultada ({p.get('fonte_tipo', 'não classificada')}) em {B.data_br(p['verificado_em'])}: {p['fonte']}")
    linhas.append(f"- Identificador na base: `{p['id']}`")
    return "\n".join(linhas) + "\n"


def gerar_referencias(b: dict) -> None:
    N = b["normas"]
    P = {p["id"]: p for p in b["precedentes"]}
    REF.mkdir(exist_ok=True)

    # 1. precedentes
    grupos = [("STF: súmulas vinculantes", lambda p: p["tipo"] == "sv"),
              ("STF: temas de repercussão geral", lambda p: p["tribunal"] == "STF" and p["tipo"] == "tema"),
              ("STF: acórdãos e ações de controle", lambda p: p["tribunal"] == "STF" and p["tipo"] == "acordao"),
              ("STF: súmulas", lambda p: p["tribunal"] == "STF" and p["tipo"] == "sumula"),
              ("STJ: temas repetitivos", lambda p: p["tribunal"] == "STJ" and p["tipo"] == "tema"),
              ("STJ: acórdãos", lambda p: p["tribunal"] == "STJ" and p["tipo"] == "acordao"),
              ("STJ: súmulas", lambda p: p["tribunal"] == "STJ" and p["tipo"] == "sumula"),
              ("Corte Interamericana de Direitos Humanos", lambda p: p["tipo"] == "corteidh")]
    out = ["# Precedentes conferidos", "", AVISO,
           f"Total: {len(b['precedentes'])} registros. Cada um traz a fonte consultada e a data da conferência.",
           "", "Regra de uso: cite somente o que está neste arquivo. Se o precedente de que você precisa não está aqui,",
           "pesquise no site do tribunal, confira o inteiro teor e só então cite. Nunca complete número, relator,",
           "data ou ementa de memória.", "", "## Sumário", ""]
    for titulo, _ in grupos:
        out.append(f"- {titulo}")
    out.append("")
    for titulo, filtro in grupos:
        itens = [p for p in b["precedentes"] if filtro(p)]
        if not itens:
            continue
        out += [f"## {titulo}", ""]
        for p in sorted(itens, key=lambda p: (len(str(p.get("numero", ""))), str(p.get("numero", "")), p["id"])):
            out.append(md_precedente(p))
    (REF / "precedentes-verificados.md").write_text("\n".join(out), encoding="utf-8")

    # 2. teses: um índice e um arquivo por grupo, para carregar só o necessário
    GRUPOS = {"teses-1-juizo-processo": "Juízo, relação processual e denúncia",
              "teses-2-provas": "Provas ilícitas, inválidas e insuficientes",
              "teses-3-procedimento-prisao": "Procedimento, instrução e prisão",
              "teses-4-merito": "Punibilidade, mérito e pedidos subsidiários"}

    def md_tese(t: dict) -> list[str]:
        o = [f"## {t['titulo']}", "",
             f"- Identificador: `{t['id']}` · Natureza: {t['natureza']} · Seção da peça: {t['secao']}",
             f"- Peças em que cabe: {', '.join(t['pecas'])}", ""]
        if t.get("acusacao"):
            o += [f"**O que a acusação afirma:** {t['acusacao']}", ""]
        o += [f"**Núcleo:** {curto(t['nucleo'], N)}", "", "**O que conferir nos autos**", ""]
        o += [f"- {curto(d, N)}" for d in t["detectar"]]
        o += ["", "**Fundamento**", "",
              "- Constituição: " + "; ".join([f"art. 5º, {i}" for i in t["art5"]] + t.get("cf_outros", [])),
              "- Tratados: " + ("; ".join(t.get("tratados", [])) or "sem dispositivo específico"),
              "- Lei: " + "; ".join(t["lei"]), ""]
        for rot, chave in (("Precedentes para citar", "precedentes"),
                           ("Precedentes para citar só se a hipótese ocorrer", "opcionais"),
                           ("Precedentes que limitam a tese (conhecer e enfrentar; não citar como apoio)", "limites")):
            refs = [P[i] for i in t.get(chave, []) if i in P]
            if refs:
                o += [f"**{rot}**", ""]
                for q in refs:
                    txt = "“" + q["literal"] + "”" if q.get("literal") else q["sintese"]
                    o.append(f"- {q['citacao']}: {txt}" + (f" Ressalva: {q['nota']}" if q.get("nota") else ""))
                o.append("")
        if not (t.get("precedentes") or t.get("opcionais")):
            o += ["**Precedentes:** nenhum vinculado nesta base. A tese se apoia no texto da Constituição e da lei.", ""]
        if t.get("prejuizo"):
            o += [f"**Como demonstrar o prejuízo:** {curto(t['prejuizo'], N)}", ""]
        o += ["**Réplicas previsíveis da acusação e resposta**", ""]
        for r in t["replicas"]:
            o += [f"- Acusação: {curto(r['a'], N)}", f"  Resposta: {curto(r['r'], N)}"]
        o += ["", f"**Pedido:** {t['pedido']}.", "", "**Texto-base para a peça**", ""]
        for par in t["texto"]:
            o.append("> [DESCREVER O FATO DO PROCESSO, COM O DOCUMENTO E AS FOLHAS OU O ID]" if par == "{FATO}" else "> " + curto(par, N))
            o.append(">")
        o[-1] = ""
        return o

    indice = ["# Teses defensivas: índice", "", AVISO,
              f"São {len(b['teses'])} teses, na ordem em que devem aparecer na peça. Abra só o arquivo do grupo de que precisar.",
              "Cada ficha traz: o que conferir nos autos, fundamento, precedentes, como demonstrar o prejuízo,",
              "réplicas previsíveis da acusação com a resposta, pedido e texto-base para a peça.", "",
              "| Tese | Identificador | Natureza | Peças | Arquivo |", "|---|---|---|---|---|"]
    for t in b["teses"]:
        indice.append(f"| {t['titulo']} | `{t['id']}` | {t['natureza']} | {', '.join(t['pecas'])} | `{t['arquivo']}.md` |")
    (REF / "teses-defensivas.md").write_text("\n".join(indice) + "\n", encoding="utf-8")
    for stem, titulo in GRUPOS.items():
        ts = [t for t in b["teses"] if t["arquivo"] == stem]
        out = [f"# Teses defensivas: {titulo.lower()}", "", AVISO, "## Sumário", ""]
        out += [f"- {t['titulo']} (`{t['id']}`)" for t in ts] + [""]
        for t in ts:
            out += md_tese(t)
        (REF / f"{stem}.md").write_text("\n".join(out), encoding="utf-8")
    sobras = {t["arquivo"] for t in b["teses"]} - set(GRUPOS)
    if sobras:
        raise SystemExit(f"grupo de teses sem título em montar.py: {sorted(sobras)}")

    # 3. matriz do art. 5º
    out = ["# Matriz: garantias do art. 5º e vícios correspondentes", "", AVISO,
           "| Dispositivo da Constituição | Garantia | Vícios relacionados |", "|---|---|---|"]
    for i in b["incisos"]:
        ts = [t for t in b["teses"] if i["inc"] in t["art5"] or i["inc"] in t.get("cf_outros", [])]
        out.append(f"| {i['rot']} | {i['garantia']} | " + "; ".join(f"{t['titulo']} ({t['natureza']})" for t in ts) + " |")
    out += ["", "## Três categorias, três regimes", "",
            "- **Nulidade absoluta**: atinge interesse público, não preclui e pode ser reconhecida a qualquer tempo.",
            "- **Nulidade relativa**: deve ser arguida no momento do art. 571 do CPP, sob pena de preclusão (art. 572).",
            "- **Prova ilícita**: não é nula, é inadmissível. Deve ser desentranhada com as que dela derivam",
            "  (Constituição, art. 5º, LVI; CPP, art. 157).",
            "", "Os tribunais superiores exigem demonstração de prejuízo também nas nulidades absolutas (CPP, art. 563).",
            "Por isso, toda arguição deve indicar o prejuízo concreto.", ""]
    (REF / "matriz-art5.md").write_text("\n".join(out), encoding="utf-8")

    # 4. roteiro de análise
    T = {t["id"]: t for t in b["teses"]}
    out = ["# Roteiro de análise do processo", "", AVISO,
           "Percorra os autos na ordem dos atos. Para cada pergunta, consulte o documento indicado.",
           "Resposta “sim” indica a tese a examinar em `teses-defensivas.md`. Sem o documento em mãos, registre",
           "a pergunta como pendência e não presuma a resposta.", ""]
    for f in b["checklist"]:
        out += [f"## {f['titulo']}", "", "| Pergunta | Onde conferir | Se sim, tese |", "|---|---|---|"]
        for q in f["perguntas"]:
            out.append(f"| {q['texto']} | {q['onde']} | {T[q['tese']]['titulo']} (`{q['tese']}`) |")
        out.append("")
    (REF / "roteiro-de-analise.md").write_text("\n".join(out), encoding="utf-8")


def gerar_app(b: dict, fragmento: Path | None) -> Path:
    b = dict(b)
    b["meta"] = {"verificado_em": max(p["verificado_em"] for p in b["precedentes"]),
                 "teses": len(b["teses"]), "precedentes": len(b["precedentes"]),
                 "gerado_em": date.today().isoformat()}
    dados = json.dumps(b, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    fonte = (APP / "oficina.src.html").read_text(encoding="utf-8")
    if "/*__DADOS__*/" not in fonte:
        raise SystemExit("marcador /*__DADOS__*/ não encontrado em oficina.src.html")
    pagina = fonte.replace("/*__DADOS__*/", dados)
    corte = pagina.index("<header")
    cabeca, corpo = pagina[:corte], pagina[corte:]
    completo = ('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                '<style>:root{color-scheme:light;padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}'
                'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
                + cabeca + "</head><body>\n" + corpo + "</body></html>\n")
    saida = APP / "oficina-defesa-penal.html"
    saida.write_text(completo, encoding="utf-8")
    if fragmento:
        fragmento.parent.mkdir(parents=True, exist_ok=True)
        fragmento.write_text(pagina, encoding="utf-8")
    return saida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so-validar", action="store_true")
    ap.add_argument("--fragmento", type=Path)
    a = ap.parse_args()
    b = B.carregar()
    erros = B.validar(b)
    if erros:
        print(f"Base com {len(erros)} erro(s):")
        for e in erros:
            print("  -", e)
        return 1
    print(f"Base íntegra: {len(b['teses'])} teses, {len(b['precedentes'])} precedentes.")
    if a.so_validar:
        return 0
    gerar_referencias(b)
    saida = gerar_app(b, a.fragmento)
    print(f"Referências geradas em {REF.relative_to(RAIZ)}/ e aplicativo em {saida.relative_to(RAIZ)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
