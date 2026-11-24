"""Carga, validação e formatação da base da skill defesa-criminal.

A base é a única fonte das teses e dos precedentes. O aplicativo, as referências
em Markdown e o verificador de citações são gerados a partir dela. Um precedente
só entra se tiver fonte consultada e data de conferência: é isso que impede a
citação "de memória".
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "assets" / "dados"

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]
MINISTRAS = {"Laurita Vaz", "Rosa Weber", "Cármen Lúcia", "Ellen Gracie",
             "Maria Thereza de Assis Moura", "Daniela Teixeira", "Regina Helena Costa",
             "Assusete Magalhães", "Nancy Andrighi", "Isabel Gallotti", "Eliana Calmon"}
TIPOS = {"acordao", "tema", "sumula", "sv", "corteidh"}
PESQUISA = {"STF": "https://jurisprudencia.stf.jus.br/pages/search",
            "STJ": "https://scon.stj.jus.br/SCON/",
            "Corte IDH": "https://www.corteidh.or.cr/"}
RX_PROC = re.compile(r"\b(HC|RHC|REsp|AREsp|EREsp|EAREsp|RE|ARE|ADI|ADC|ADPF|Rcl|Inq|AP|RMS|SL|Pet)s?\s*"
                     r"(?:n\.?\s*[ºo°]?\s*)?(\d{1,3}(?:\.\d{3})+|\d{3,7})")
SECOES = ("preliminar", "punibilidade", "merito", "subsidiario", "prisao")
PECAS = ("resposta", "nulidade", "hc")


def data_extenso(iso: str) -> str:
    if not iso:
        return ""
    a, m, d = (int(x) for x in iso.split("-"))
    return f"{'1º' if d == 1 else d} de {MESES[m - 1]} de {a}"


def data_br(iso: str) -> str:
    if not iso:
        return ""
    a, m, d = iso.split("-")
    return f"{d}/{m}/{a}"


def _ministro(nome: str, papel: str) -> str:
    fem = nome in MINISTRAS
    papeis = {"relator": ("relator Ministro", "relatora Ministra"),
              "redator": ("redator para o acórdão Ministro", "redatora para o acórdão Ministra")}
    return f"{papeis[papel][1 if fem else 0]} {nome}"


def citar(p: dict) -> str:
    """Forma padronizada de citação, usada no aplicativo e nas referências."""
    t = p["tipo"]
    if t == "sumula":
        return f"Súmula nº {p['numero']} do {p['tribunal']}"
    if t == "sv":
        return f"Súmula Vinculante nº {p['numero']} do STF"
    if t == "corteidh":
        s = f"Corte Interamericana de Direitos Humanos, {p['rotulo']}"
        if p.get("data"):
            s += f", sentença de {data_extenso(p['data'])}"
        if p.get("numero"):
            s += f", Série C nº {p['numero']}"
        return s
    det = []
    if t == "tema":
        base = f"{p['tribunal']}, Tema nº {p['numero']} " + (
            "da repercussão geral" if p["tribunal"] == "STF" else "dos recursos repetitivos")
        if p.get("paradigma"):
            det.append(p["paradigma"])
    else:
        base = f"{p['tribunal']}, {p['rotulo']}"
    if p.get("orgao"):
        det.append(p["orgao"])
    if p.get("relator"):
        det.append(_ministro(p["relator"], "relator"))
    if p.get("redator"):
        det.append(_ministro(p["redator"], "redator"))
    if p.get("data"):
        det.append(f"julgado em {data_extenso(p['data'])}")
    if t == "tema":
        return base + (f" ({', '.join(det)})" if det else "")
    return ", ".join([base] + det)


def chaves_de(p: dict) -> list[str]:
    """Chaves normalizadas para localizar a citação em um texto."""
    ch = {re.sub(r"[^A-Z0-9]", "", str(c).upper()) for c in p.get("chaves", [])}
    num = re.sub(r"\D", "", str(p.get("numero", "")))
    trib = {"STF": "STF", "STJ": "STJ"}.get(p["tribunal"], "")
    if p["tipo"] == "sumula" and num:
        ch.add(f"SUM{trib}{num}")
    elif p["tipo"] == "sv" and num:
        ch.add(f"SV{num}")
    elif p["tipo"] == "tema" and num:
        ch.add(f"TEMA{trib}{num}")
    for campo in ("rotulo", "paradigma"):
        for m in RX_PROC.finditer(p.get(campo, "") or ""):
            ch.add(m.group(1).upper() + m.group(2).replace(".", ""))
    # julgamentos conjuntos: "ADIs nº 6.298, 6.299, 6.300 e 6.305"
    m = re.match(r"\s*(ADI|ADC|ADPF|HC|RE|REsp)s\b(.*)", p.get("rotulo", "") or "")
    if m:
        for n in re.findall(r"\d{1,3}(?:\.\d{3})+|\d{2,7}", m.group(2)):
            ch.add(m.group(1).upper() + n.replace(".", ""))
    ch.discard("")
    return sorted(ch)


def carregar() -> dict:
    """Lê todos os arquivos de dados e devolve a base consolidada."""
    teses = []
    for f in sorted(DADOS.glob("teses-*.json")):
        grupo = json.loads(f.read_text(encoding="utf-8"))
        for t in grupo:
            t["arquivo"] = f.stem
        teses += grupo
    precs = []
    for nome in ("precedentes.json", "precedentes-corteidh.json"):
        f = DADOS / nome
        if f.exists():
            precs += json.loads(f.read_text(encoding="utf-8"))
    est = json.loads((DADOS / "estrutura.json").read_text(encoding="utf-8"))
    chk = json.loads((DADOS / "checklist.json").read_text(encoding="utf-8"))
    dout_f = DADOS / "doutrina.json"
    dout = json.loads(dout_f.read_text(encoding="utf-8")) if dout_f.exists() else []
    for p in precs:
        p["chaves"] = chaves_de(p)
        p["citacao"] = citar(p)
        p["conferir"] = PESQUISA.get(p["tribunal"], "")
    teses.sort(key=lambda t: t["ordem"])
    return {"teses": teses, "precedentes": precs, "checklist": chk, "doutrina": dout, **est}


def validar(b: dict) -> list[str]:
    """Devolve a lista de erros. Lista vazia significa base íntegra."""
    erros: list[str] = []
    ids_p = [p["id"] for p in b["precedentes"]]
    for i in {x for x in ids_p if ids_p.count(x) > 1}:
        erros.append(f"precedente repetido: {i}")
    P = {p["id"]: p for p in b["precedentes"]}
    for p in b["precedentes"]:
        pid = p.get("id", "?")
        for campo in ("tribunal", "tipo", "sintese", "fonte", "verificado_em"):
            if not str(p.get(campo, "")).strip():
                erros.append(f"{pid}: campo obrigatório vazio: {campo}")
        if p.get("tipo") not in TIPOS:
            erros.append(f"{pid}: tipo inválido: {p.get('tipo')}")
        if not str(p.get("fonte", "")).startswith("https://"):
            erros.append(f"{pid}: fonte sem URL https")
        if p.get("tipo") in ("sumula", "sv", "tema") and not re.sub(r"\D", "", str(p.get("numero", ""))):
            erros.append(f"{pid}: súmula ou tema sem número")
        if p.get("tipo") in ("sumula", "sv") and not (p.get("literal") or p.get("integra")):
            erros.append(f"{pid}: súmula sem texto literal")
        if p.get("tipo") == "acordao" and not (p.get("rotulo") and p.get("orgao") and p.get("data")):
            erros.append(f"{pid}: acórdão sem rótulo, órgão julgador ou data")
        if p.get("tipo") != "corteidh" and not p["chaves"]:
            erros.append(f"{pid}: sem chave de localização")
        if p.get("data") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["data"]):
            erros.append(f"{pid}: data fora do formato AAAA-MM-DD")
    ids_t = [t["id"] for t in b["teses"]]
    for i in {x for x in ids_t if ids_t.count(x) > 1}:
        erros.append(f"tese repetida: {i}")
    T = set(ids_t)
    bases = {x["id"] for x in b["bases"]}
    obrig = ("id", "titulo", "secao", "ordem", "natureza", "art5", "lei", "detectar",
             "nucleo", "replicas", "pedido", "pecas", "texto", "precedentes")
    for t in b["teses"]:
        tid = t.get("id", "?")
        for campo in obrig:
            if campo not in t:
                erros.append(f"{tid}: falta o campo {campo}")
        if t.get("secao") not in SECOES:
            erros.append(f"{tid}: seção inválida: {t.get('secao')}")
        for pc in t.get("pecas", []):
            if pc not in PECAS:
                erros.append(f"{tid}: peça inválida: {pc}")
        for lista in ("precedentes", "opcionais", "limites"):
            for ref in t.get(lista, []):
                if ref not in P:
                    erros.append(f"{tid}: {lista} cita precedente fora da base: {ref}")
        if t.get("base") and t["base"] not in bases:
            erros.append(f"{tid}: base de acusação inexistente: {t['base']}")
        textos = [t.get("nucleo", ""), t.get("prejuizo", ""), t.get("pedido", "")] + t.get("texto", []) + \
            t.get("detectar", []) + [r["a"] + r["r"] for r in t.get("replicas", [])]
        for tok in set(re.findall(r"\{([A-Z0-9]+)\}", " ".join(textos))) - {"FATO"}:
            if tok not in b["normas"]:
                erros.append(f"{tid}: marcador de norma desconhecido: {{{tok}}}")
        if "{FATO}" not in t.get("texto", []):
            erros.append(f"{tid}: o texto não reserva o parágrafo do fato")
    com_pergunta = set()
    for f in b["checklist"]:
        for q in f["perguntas"]:
            if q["tese"] not in T:
                erros.append(f"pergunta {q['id']}: tese inexistente: {q['tese']}")
            com_pergunta.add(q["tese"])
    for t in sorted(T - com_pergunta):
        erros.append(f"{t}: nenhuma pergunta do roteiro leva a esta tese")
    return erros
