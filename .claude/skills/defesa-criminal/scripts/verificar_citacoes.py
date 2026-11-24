#!/usr/bin/env python3
"""Confere as citações de um texto jurídico contra a base de precedentes conferidos.

Uso:
    python3 scripts/verificar_citacoes.py minuta.txt
    python3 scripts/verificar_citacoes.py - < minuta.txt
    python3 scripts/verificar_citacoes.py minuta.md --json

Três resultados possíveis para cada citação localizada:
    NA BASE      o julgado, a súmula ou o tema consta da base conferida;
    DIVERGENTE   consta da base, mas o texto indica relator ou órgão julgador diferente;
    FORA DA BASE não consta. Pode existir: localize o inteiro teor no site do tribunal
                 ou retire a citação.

O código de saída é 1 quando há citação DIVERGENTE ou FORA DA BASE. Isso permite usar
o script como trava antes de entregar uma peça.

Limite: "NA BASE" prova que o precedente existe e está registrado. Não prova que ele
se aplica ao caso nem que continua em vigor na data do protocolo.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base as B  # noqa: E402

RX_PROC = re.compile(r"\b(HC|RHC|REsp|AREsp|EREsp|EAREsp|RE|ARE|ADI|ADC|ADPF|Rcl|Inq|AP|RMS|SL|Pet)s?\s*"
                     r"(?:n\.?\s*[ºo°]?\s*)?(\d{1,3}(?:\.\d{3})+|\d{3,7})")
RX_SUM = re.compile(r"S[úu]mulas?\s+(Vinculante\s+)?(?:n\.?\s*[ºo°]?\s*)?(\d{1,3})"
                    r"(?:[\s,]*(?:do|da)\s+(STF|STJ|Supremo|Superior))?", re.I)
RX_TEMA = re.compile(r"Tema\s+(Repetitivo\s+)?(?:n\.?\s*[ºo°]?\s*)?(\d{1,2}\.?\d{1,3}|\d{1,4})"
                     r"(?:[\s,]*(?:do|da|de|dos)\s+(STF|STJ|repercuss[ãa]o geral|recursos repetitivos|Supremo|Superior))?", re.I)
RX_REL = re.compile(r"Rel(?:ator|atora)?\.?(?:\s+(?:p/|para)\s+(?:o\s+)?ac[óo]rd[ãa]o)?\s*:?\s*(?:o\s+|a\s+)?"
                    r"Min(?:istr[oa])?\.?\s+([A-ZÀ-Ú][\wÀ-ú.]+(?:\s+(?:de\s+|da\s+|do\s+|dos\s+)?[A-ZÀ-Ú][\wÀ-ú.]+){0,3})")
RX_ORG = re.compile(r"(PLENARIO|TRIBUNAL PLENO|\bPLENO\b)|(CORTE ESPECIAL)|"
                    r"(PRIMEIRA|SEGUNDA|TERCEIRA|QUARTA|QUINTA|SEXTA|[1-6]A)\s+(TURMA|SECAO)")
ORD = {"PRIMEIRA": "1", "SEGUNDA": "2", "TERCEIRA": "3", "QUARTA": "4", "QUINTA": "5", "SEXTA": "6",
       "1A": "1", "2A": "2", "3A": "3", "4A": "4", "5A": "5", "6A": "6"}
JANELA = 260


def normaliza(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").upper()


def orgao_chave(s: str) -> str:
    """Primeiro órgão julgador mencionado no trecho, em forma normalizada."""
    m = RX_ORG.search(normaliza(s).replace("ª", "A"))
    if not m:
        return ""
    if m.group(1):
        return "PLENO"
    if m.group(2):
        return "CE"
    return ORD[m.group(3)] + ("T" if m.group(4) == "TURMA" else "S")


def verificar(texto: str, precedentes: list[dict]) -> list[dict]:
    idx = {k: p for p in precedentes for k in p.get("chaves", [])}
    achados: dict[tuple, dict] = {}
    inicios = sorted(m.start() for rx in (RX_PROC, RX_SUM, RX_TEMA) for m in rx.finditer(texto))

    def janela(m) -> str:
        """Trecho que pertence a esta citação: até a próxima citação, o fim da frase ou JANELA caracteres."""
        fim = m.start() + JANELA
        fim = min([fim] + [i for i in inicios if i >= m.end()])
        for sep in (";", "\n"):
            k = texto.find(sep, m.end())
            if k != -1:
                fim = min(fim, k)
        return texto[m.start():fim]

    def registra(pos, bruto, chaves, p, divergencias=(), obs=""):
        achados.setdefault((pos, "/".join(chaves)), {
            "posicao": pos, "citacao_no_texto": bruto,
            "resultado": "FORA DA BASE" if not p else "DIVERGENTE" if divergencias else "NA BASE",
            "registro": p["citacao"] if p else "", "id": p["id"] if p else "",
            "divergencias": list(divergencias), "observacao": obs,
            "fonte": p["fonte"] if p else "", "ressalva": (p.get("nota") or "") if p else ""})

    for m in RX_PROC.finditer(texto):
        chave = m.group(1).upper() + m.group(2).replace(".", "")
        p = idx.get(chave)
        div = []
        if p:
            jan = janela(m)
            r = RX_REL.search(jan)
            nomes = [normaliza(n) for n in (p.get("relator"), p.get("redator")) if n]
            if r and nomes:
                dito = normaliza(r.group(1))
                if not any(w in dito for n in nomes for w in n.split() if len(w) > 2):
                    div.append(f"relator indicado no texto (“{r.group(1)}”) difere do registrado na base "
                               f"({'; redator para o acórdão: '.join(n for n in (p.get('relator'), p.get('redator')) if n)})")
            o, ob = orgao_chave(jan), orgao_chave(p.get("orgao", ""))
            if o and ob and o != ob:
                div.append(f"órgão julgador indicado no texto difere do registrado na base ({p['orgao']})")
        registra(m.start(), m.group(0), [chave], p, div)

    for m in RX_SUM.finditer(texto):
        num = m.group(2)
        if m.group(1):
            chaves = [f"SV{num}"]
        elif m.group(3):
            chaves = ["SUM" + ("STF" if re.search(r"STF|Supremo", m.group(3), re.I) else "STJ") + num]
        else:
            chaves = [f"SUMSTF{num}", f"SUMSTJ{num}"]
        ps = [idx[k] for k in chaves if k in idx]
        obs = ("O texto não indica o tribunal. Na base: " + " e ".join(x["citacao"] for x in ps) + "."
               if len(chaves) > 1 and ps else "")
        registra(m.start(), m.group(0), chaves, ps[0] if ps else None, obs=obs)

    for m in RX_TEMA.finditer(texto):
        num = m.group(2).replace(".", "")
        antes = texto[max(0, m.start() - 8):m.start()]
        trib = ""
        if m.group(3):
            trib = "STJ" if re.search(r"STJ|Superior|repetitivos", m.group(3), re.I) else "STF"
        elif m.group(1):
            trib = "STJ"
        elif "STJ" in antes:
            trib = "STJ"
        elif "STF" in antes:
            trib = "STF"
        chaves = [f"TEMA{trib}{num}"] if trib else [f"TEMASTF{num}", f"TEMASTJ{num}"]
        ps = [idx[k] for k in chaves if k in idx]
        obs = ("O texto não indica o tribunal. Na base: " + " e ".join(x["citacao"] for x in ps) + "."
               if len(chaves) > 1 and ps else "")
        registra(m.start(), m.group(0), chaves, ps[0] if ps else None, obs=obs)

    return sorted(achados.values(), key=lambda a: a["posicao"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", help="arquivo de texto ou '-' para a entrada padrão")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    a = ap.parse_args()
    texto = sys.stdin.read() if a.arquivo == "-" else Path(a.arquivo).read_text(encoding="utf-8")
    res = verificar(texto, B.carregar()["precedentes"])
    ruins = [r for r in res if r["resultado"] != "NA BASE"]
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 1 if ruins else 0
    if not res:
        print("Nenhuma citação de julgado, súmula ou tema foi reconhecida no texto.")
        return 0
    cont = {k: sum(1 for r in res if r["resultado"] == k) for k in ("NA BASE", "DIVERGENTE", "FORA DA BASE")}
    print(f"{len(res)} citações: {cont['NA BASE']} na base, {cont['DIVERGENTE']} divergentes, {cont['FORA DA BASE']} fora da base.\n")
    for r in res:
        print(f"[{r['resultado']}] {r['citacao_no_texto']}")
        if r["registro"]:
            print(f"    registro: {r['registro']}")
        for d in r["divergencias"]:
            print(f"    atenção: {d}")
        if r["observacao"]:
            print(f"    {r['observacao']}")
        if r["ressalva"]:
            print(f"    ressalva: {r['ressalva']}")
        if r["resultado"] == "FORA DA BASE":
            print("    Localize o inteiro teor no site do tribunal. Se não encontrar, retire a citação.")
    return 1 if ruins else 0


if __name__ == "__main__":
    raise SystemExit(main())
