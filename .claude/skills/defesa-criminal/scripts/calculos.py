#!/usr/bin/env python3
"""Cálculos por regra fixa: prazo da resposta à acusação e prescrição pela pena máxima.

Prazo e prescrição não se estimam "de cabeça" nem por texto gerado: um dia de erro
perde o prazo. Este script aplica a regra legal e mostra cada passo da conta.

Uso:
    python3 scripts/calculos.py prazo --citacao 2026-11-16 [--defensoria] [--hoje 2026-11-24]
    python3 scripts/calculos.py prescricao --fato 2015-03-10 --pena-max-anos 4
            [--pena-max-meses 0] [--recebimento 2020-01-15] [--menor21] [--maior70] [--hoje 2026-11-24]

As duas contas são estimativas conservadoras e trazem, na saída, o que não consideram.
"""
from __future__ import annotations

import argparse
import calendar
from datetime import date, timedelta

DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
LEI_12234 = date(2010, 5, 6)  # publicação da Lei nº 12.234, de 5 de maio de 2010


def br(d: date) -> str:
    return d.strftime("%d/%m/%Y")


def soma_meses(d: date, meses: int) -> date:
    total = d.year * 12 + (d.month - 1) + meses
    ano, mes = divmod(total, 12)
    return date(ano, mes + 1, min(d.day, calendar.monthrange(ano, mes + 1)[1]))


def prazo_resposta(citacao: date, defensoria: bool = False, hoje: date | None = None) -> dict:
    """Prazo do art. 396 do CPP: dez dias corridos, sem contar o dia do começo.

    Regra aplicada: CPP, art. 396 (dez dias); art. 798, § 1º (exclui o dia do começo,
    inclui o do vencimento); art. 798, § 3º (vencimento em dia não útil prorroga-se ao
    dia útil seguinte). Defensoria Pública: prazo em dobro.
    Não considera feriados, suspensões locais nem o recesso do art. 798-A, que só
    adiam o vencimento. Por isso a data nunca é posterior à real.
    """
    dias = 20 if defensoria else 10
    bruto = citacao + timedelta(days=dias)
    fim = bruto
    while fim.weekday() >= 5:
        fim += timedelta(days=1)
    recesso = any((d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20)
                  for d in (citacao + timedelta(days=i) for i in range(1, (fim - citacao).days + 1)))
    hoje = hoje or date.today()
    return {"citacao": citacao, "dias": dias, "termo_bruto": bruto, "vencimento": fim,
            "prorrogado": fim != bruto, "toca_recesso": recesso, "dias_restantes": (fim - hoje).days}


def prazo_prescricional(pena_max_meses: int, fato: date) -> tuple[int, str]:
    """Prazo em anos e inciso do art. 109 do Código Penal, pela pena máxima em abstrato."""
    m = pena_max_meses
    if m > 144:
        return 20, "I"
    if m > 96:
        return 16, "II"
    if m > 48:
        return 12, "III"
    if m > 24:
        return 8, "IV"
    if m >= 12:
        return 4, "V"
    return (2 if fato < LEI_12234 else 3), "VI"


def prescricao(fato: date, pena_max_anos: int, pena_max_meses: int = 0, recebimento: date | None = None,
               menor21: bool = False, maior70: bool = False, hoje: date | None = None) -> dict:
    """Prescrição da pretensão punitiva pela pena máxima em abstrato.

    Regra aplicada: CP, art. 109 (prazos); art. 115 (redução à metade); art. 117, I
    (o recebimento da denúncia interrompe o prazo); art. 10 (o dia do começo se inclui).
    Não considera causas de aumento ou de diminuição, a exceção do art. 115 para violência sexual contra a mulher, o termo inicial especial do art. 111, V, outras causas interruptivas
    (pronúncia, sentença), causas suspensivas (CP, art. 116; CPP, art. 366) nem a
    prescrição pela pena aplicada.
    """
    hoje = hoje or date.today()
    anos, inciso = prazo_prescricional(pena_max_anos * 12 + pena_max_meses, fato)
    metade = menor21 or maior70
    meses = anos * 6 if metade else anos * 12
    trechos = []
    marcos = [("fato", fato)] + ([("recebimento da denúncia", recebimento)] if recebimento else []) + [("hoje", hoje)]
    for (n1, d1), (n2, d2) in zip(marcos, marcos[1:]):
        limite = soma_meses(d1, meses)
        # prazo penal: o dia do começo se inclui (CP, art. 10); o último dia é a véspera do aniversário
        trechos.append({"de": n1, "ate": n2, "inicio": d1, "fim": d2, "ultimo_dia": limite - timedelta(days=1),
                        "prescrito": limite <= d2})
    return {"prazo_anos": anos, "inciso": inciso, "reduzido": metade, "prazo_meses": meses, "trechos": trechos}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("prazo", help="prazo da resposta à acusação")
    p1.add_argument("--citacao", required=True, type=date.fromisoformat)
    p1.add_argument("--defensoria", action="store_true")
    p1.add_argument("--hoje", type=date.fromisoformat)
    p2 = sub.add_parser("prescricao", help="prescrição pela pena máxima em abstrato")
    p2.add_argument("--fato", required=True, type=date.fromisoformat)
    p2.add_argument("--pena-max-anos", required=True, type=int)
    p2.add_argument("--pena-max-meses", type=int, default=0)
    p2.add_argument("--recebimento", type=date.fromisoformat)
    p2.add_argument("--menor21", action="store_true")
    p2.add_argument("--maior70", action="store_true")
    p2.add_argument("--hoje", type=date.fromisoformat)
    a = ap.parse_args()
    if a.cmd == "prazo":
        r = prazo_resposta(a.citacao, a.defensoria, a.hoje)
        print(f"Citação em {br(r['citacao'])} ({DIAS[r['citacao'].weekday()]}). O dia do começo não se computa (CPP, art. 798, § 1º).")
        print(f"{r['dias']} dias corridos" + (" (prazo em dobro da Defensoria Pública)" if a.defensoria else " (CPP, art. 396)")
              + f" terminam em {br(r['termo_bruto'])} ({DIAS[r['termo_bruto'].weekday()]}).")
        if r["prorrogado"]:
            print(f"O dia não é útil: o prazo se prorroga até {br(r['vencimento'])} (CPP, art. 798, § 3º).")
        print(f"Vencimento estimado: {br(r['vencimento'])}. Dias restantes: {r['dias_restantes']}.")
        if r["toca_recesso"]:
            print("O período inclui dias entre 20 de dezembro e 20 de janeiro. Com réu solto, o prazo fica suspenso "
                  "nesse intervalo (CPP, art. 798-A), e a data real pode ser posterior.")
        print("Estimativa conservadora: não considera feriados nem suspensões locais. Confira no sistema do tribunal.")
    else:
        r = prescricao(a.fato, a.pena_max_anos, a.pena_max_meses, a.recebimento, a.menor21, a.maior70, a.hoje)
        print(f"Pena máxima: {a.pena_max_anos} ano(s) e {a.pena_max_meses} mês(es). Prazo: {r['prazo_anos']} anos (CP, art. 109, {r['inciso']})"
              + (f", reduzido à metade (CP, art. 115): {r['prazo_meses']} meses." if r["reduzido"] else "."))
        for t in r["trechos"]:
            print(f"Do {t['de']} ({br(t['inicio'])}) até {t['ate']} ({br(t['fim'])}): o último dia do prazo é {br(t['ultimo_dia'])}. "
                  + ("Em tese, PRESCRITO." if t["prescrito"] else "Não alcança o prazo."))
        print("Cálculo pela pena máxima em abstrato. Não considera causas de aumento ou de diminuição, a exceção do art. 115 para violência sexual contra a mulher, o termo inicial especial do art. 111, V, outras causas "
              "interruptivas nem causas suspensivas. Confira antes de alegar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
