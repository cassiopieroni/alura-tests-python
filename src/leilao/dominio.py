from excecoes import LanceInvalido


class Usuario:
    def __init__(self, nome, carteira=500):
        self.__nome = nome
        self.__carteira = carteira


    def propoe_lance(self, leilao, valor):
        if self._nao_possui_o_valor_na_carteira(valor):
            raise LanceInvalido(f'{self.__nome} não possui este valor na carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor
    
    def _nao_possui_o_valor_na_carteira(self, valor):
        return not self.__carteira >= valor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def carteira(self):
        return self.__carteira


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0


    def propoe(self, lance: Lance):
        if self._lance_invalido(lance):
            raise LanceInvalido('Lance inválido')

        if self._nao_tem_laces():
            self.menor_lance = lance.valor
        
        self.maior_lance = lance.valor
        self.__lances.append(lance)


    def _lance_invalido(self, lance: Lance):
        return (self._o_usuario_eh_o_mesmo_do_ultimo_lance(lance)
                or self._o_lance_eh_menor_ou_igual_ao_ultimo_lance(lance))


    def _o_usuario_eh_o_mesmo_do_ultimo_lance(self, lance: Lance):
        if self.lances:
            ultimo_lance = self.lances[-1]
            return ultimo_lance.usuario is lance.usuario
        return False


    def _o_lance_eh_menor_ou_igual_ao_ultimo_lance(self, lance_atual: Lance):
        if self.lances:
            ultimo_lance = self.lances[-1]
            return lance_atual.valor <= ultimo_lance.valor
        return False


    def _nao_tem_laces(self):
        return not self.__lances


    @property
    def lances(self):
        return self.__lances[:]
