import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myyty_nolla(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_liian_vahan_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
 
    def test_liian_vahan_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_edullinen_korttiosto(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_korttiosto(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kortilla_ei_rahaa(self):
        self.kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kortilla_ei_rahaa(self):
        self.kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_summa_ei_muutu_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_ladataan_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    
