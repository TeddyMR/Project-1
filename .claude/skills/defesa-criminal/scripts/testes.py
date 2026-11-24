#!/usr/bin/env python3
"""Testes dos scripts da skill. Rode com: python3 scripts/testes.py"""
from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base as B  # noqa: E402
import calculos as C  # noqa: E402
import verificar_citacoes as V  # noqa: E402

PRECS = [
    {"id": "stj-hc-598886", "tribunal": "STJ", "tipo": "acordao", "classe": "HC", "numero": "598886",
     "rotulo": "HC nº 598.886/SC", "orgao": "Sexta Turma", "relator": "Rogerio Schietti Cruz", "redator": "",
     "data": "2020-10-27", "fonte": "https://scon.stj.jus.br/SCON/", "chaves": []},
    {"id": "stj-hc-653515", "tribunal": "STJ", "tipo": "acordao", "classe": "HC", "numero": "653515",
     "rotulo": "HC nº 653.515/RJ", "orgao": "Sexta Turma", "relator": "Laurita Vaz", "redator": "Rogerio Schietti Cruz",
     "data": "2021-11-23", "fonte": "https://scon.stj.jus.br/SCON/", "chaves": []},
    {"id": "stf-tema-280", "tribunal": "STF", "tipo": "tema", "numero": "280", "paradigma": "RE nº 603.616",
     "orgao": "Plenário", "relator": "Gilmar Mendes", "redator": "", "data": "2015-11-05",
     "fonte": "https://portal.stf.jus.br/", "chaves": []},
    {"id": "stj-tema-1258", "tribunal": "STJ", "tipo": "tema", "numero": "1258", "paradigma": "REsp nº 1.953.602/SP",
     "orgao": "Terceira Seção", "relator": "Reynaldo Soares da Fonseca", "redator": "", "data": "2025-06-11",
     "fonte": "https://processo.stj.jus.br/", "chaves": []},
    {"id": "stf-sum-523", "tribunal": "STF", "tipo": "sumula", "numero": "523", "fonte": "https://portal.stf.jus.br/", "chaves": []},
    {"id": "stj-sum-648", "tribunal": "STJ", "tipo": "sumula", "numero": "648", "fonte": "https://scon.stj.jus.br/", "chaves": []},
    {"id": "stf-sv-14", "tribunal": "STF", "tipo": "sv", "numero": "14", "fonte": "https://portal.stf.jus.br/", "chaves": []},
    {"id": "stf-adi-6298", "tribunal": "STF", "tipo": "acordao", "classe": "ADI", "numero": "6298",
     "rotulo": "ADIs nº 6.298, 6.299, 6.300 e 6.305", "orgao": "Plenário", "relator": "Luiz Fux", "redator": "",
     "data": "2023-08-24", "fonte": "https://portal.stf.jus.br/", "chaves": []},
]
for _p in PRECS:
    _p["chaves"] = B.chaves_de(_p)
    _p["citacao"] = B.citar(_p)


class Citacao(unittest.TestCase):
    def test_formas(self):
        c = {p["id"]: p["citacao"] for p in PRECS}
        self.assertEqual(c["stj-hc-598886"], "STJ, HC nº 598.886/SC, Sexta Turma, relator Ministro Rogerio Schietti Cruz, julgado em 27 de outubro de 2020")
        self.assertIn("relatora Ministra Laurita Vaz, redator para o acórdão Ministro Rogerio Schietti Cruz", c["stj-hc-653515"])
        self.assertEqual(c["stf-tema-280"], "STF, Tema nº 280 da repercussão geral (RE nº 603.616, Plenário, relator Ministro Gilmar Mendes, julgado em 5 de novembro de 2015)")
        self.assertTrue(c["stj-tema-1258"].startswith("STJ, Tema nº 1258 dos recursos repetitivos"))
        self.assertEqual(c["stf-sum-523"], "Súmula nº 523 do STF")
        self.assertEqual(c["stf-sv-14"], "Súmula Vinculante nº 14 do STF")

    def test_chaves(self):
        k = {p["id"]: p["chaves"] for p in PRECS}
        self.assertEqual(k["stj-hc-598886"], ["HC598886"])
        self.assertEqual(k["stf-tema-280"], ["RE603616", "TEMASTF280"])
        self.assertEqual(k["stf-adi-6298"], ["ADI6298", "ADI6299", "ADI6300", "ADI6305"])
        self.assertEqual(k["stj-sum-648"], ["SUMSTJ648"])

    def test_primeiro_dia_do_mes(self):
        self.assertEqual(B.data_extenso("2016-03-01"), "1º de março de 2016")


class Verificador(unittest.TestCase):
    def res(self, txt):
        return {r["citacao_no_texto"]: r for r in V.verificar(txt, PRECS)}

    def test_na_base(self):
        r = self.res("Conforme o HC 598.886/SC, Rel. Min. Rogerio Schietti Cruz, Sexta Turma, e a Súmula 523 do STF.")
        self.assertEqual(r["HC 598.886"]["resultado"], "NA BASE")
        self.assertEqual(r["Súmula 523 do STF"]["resultado"], "NA BASE")

    def test_relator_trocado(self):
        r = self.res("HC nº 598.886/SC, Rel. Min. Nefi Cordeiro, Sexta Turma")
        self.assertEqual(list(r.values())[0]["resultado"], "DIVERGENTE")

    def test_orgao_trocado(self):
        r = self.res("HC 598.886/SC, relator Ministro Rogerio Schietti Cruz, Quinta Turma")
        self.assertEqual(list(r.values())[0]["resultado"], "DIVERGENTE")

    def test_redator_aceito(self):
        r = self.res("HC 653.515/RJ, Rel. p/ acórdão Min. Rogerio Schietti Cruz, 6ª Turma")
        self.assertEqual(list(r.values())[0]["resultado"], "NA BASE")

    def test_fora_da_base(self):
        r = self.res("o REsp 1.234.567/SP decidiu que")
        self.assertEqual(list(r.values())[0]["resultado"], "FORA DA BASE")

    def test_temas_e_sumulas(self):
        r = V.verificar("Tema 280 da repercussão geral; STJ, Tema nº 1258 dos recursos repetitivos; Tema Repetitivo 1258; "
                        "Súmula Vinculante 14; Súmula 648 do STJ; Súmula 999 do STJ; ADI 6.300.", PRECS)
        self.assertEqual([x["resultado"] for x in r], ["NA BASE"] * 5 + ["FORA DA BASE", "NA BASE"])

    def test_citacao_padrao_volta_como_na_base(self):
        txt = "; ".join(p["citacao"] for p in PRECS)
        self.assertTrue(all(x["resultado"] == "NA BASE" for x in V.verificar(txt, PRECS)), V.verificar(txt, PRECS))


class Prazo(unittest.TestCase):
    def test_dez_dias(self):
        r = C.prazo_resposta(date(2026, 11, 16), hoje=date(2026, 11, 24))
        self.assertEqual(r["vencimento"], date(2026, 11, 26))
        self.assertEqual(r["dias_restantes"], 2)
        self.assertFalse(r["prorrogado"])

    def test_vence_no_sabado(self):
        r = C.prazo_resposta(date(2026, 11, 11), hoje=date(2026, 11, 12))  # 21/11/2026 é sábado
        self.assertEqual(r["termo_bruto"], date(2026, 11, 21))
        self.assertEqual(r["vencimento"], date(2026, 11, 23))
        self.assertTrue(r["prorrogado"])

    def test_defensoria_e_recesso(self):
        r = C.prazo_resposta(date(2026, 12, 7), defensoria=True, hoje=date(2026, 12, 8))
        self.assertEqual(r["dias"], 20)
        self.assertEqual(r["vencimento"], date(2026, 12, 28))
        self.assertTrue(r["toca_recesso"])


class Prescricao(unittest.TestCase):
    def test_faixas_do_art_109(self):
        f = date(2020, 1, 1)
        casos = [(145, 20, "I"), (144, 16, "II"), (97, 16, "II"), (96, 12, "III"), (49, 12, "III"), (48, 8, "IV"),
                 (25, 8, "IV"), (24, 4, "V"), (12, 4, "V"), (11, 3, "VI")]
        for meses, anos, inc in casos:
            self.assertEqual(C.prazo_prescricional(meses, f), (anos, inc), meses)

    def test_lei_12234(self):
        self.assertEqual(C.prazo_prescricional(6, date(2010, 5, 5))[0], 2)
        self.assertEqual(C.prazo_prescricional(6, date(2010, 5, 6))[0], 3)

    def test_limite_exato(self):
        r = C.prescricao(date(2015, 3, 10), 4, recebimento=date(2023, 3, 10), hoje=date(2026, 11, 24))
        self.assertTrue(r["trechos"][0]["prescrito"])
        self.assertEqual(r["trechos"][0]["ultimo_dia"], date(2023, 3, 9))
        r = C.prescricao(date(2015, 3, 10), 4, recebimento=date(2023, 3, 9), hoje=date(2026, 11, 24))
        self.assertFalse(r["trechos"][0]["prescrito"])

    def test_metade(self):
        r = C.prescricao(date(2020, 1, 31), 1, menor21=True, hoje=date(2022, 1, 31))
        self.assertEqual(r["prazo_meses"], 24)
        self.assertTrue(r["trechos"][0]["prescrito"])


class BaseReal(unittest.TestCase):
    def test_base_integra(self):
        if not (B.DADOS / "precedentes.json").exists():
            self.skipTest("precedentes.json ainda não existe")
        erros = B.validar(B.carregar())
        self.assertEqual(erros, [], "\n".join(erros))


if __name__ == "__main__":
    unittest.main(verbosity=1)
