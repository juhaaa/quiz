import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataus(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_ota_rahaa(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
        
    def test_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


