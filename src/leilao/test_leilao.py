from unittest import TestCase, main

from dominio import Lance, Leilao, Usuario
from excecoes import LanceInvalido

class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500)
        self.yuri = Usuario('Yuri', 500)

        self.lance_do_gui = Lance(self.gui, 150)
        self.lance_do_yuri = Lance(self.yuri, 100)

        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)


        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 150
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        self.vini = Usuario('Vini', 500)
        self.lance_do_vini = Lance(self.vini, 200.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual([self.lance_do_yuri], self.leilao.lances)


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual([self.lance_do_yuri, self.lance_do_gui], self.leilao.lances)


    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_yury300 = Lance(self.yuri, 300)
        
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_yuri)
            self.leilao.propoe(lance_do_yury300)


if __name__ == '__main__':
    main()