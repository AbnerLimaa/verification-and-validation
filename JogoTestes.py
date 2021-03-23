from Jogo import *
from Monstro import *
from Ataque import *
from Jogador import *
import unittest

#Equipe: Abner Lima, Daniel Queiroz e Tibet Teixeira

class JogoTestes(unittest.TestCase):
    def setUp(self):
        self.monstro = MonstroDummy()
        self.jogador = JogadorDummy()
        self.sut = Jogo(self.monstro, self.jogador)
    
    def tearDown(self):
        del self.sut
        del self.monstro
        del self.jogador
    
    def teste_atacar_givenMonstroSemDefasa_whenAtacar_thenMonstroGerouDefesa(self):
        #given
        self.monstro = MonstroSpy()
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        self.monstro.defesa = []
        ataque = AtaqueDummy([])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertEqual(self.monstro.gerarDefesaCount, 1)

    def teste_atacar_givenRespostaQuaseCorreta_whenAtacar_thenDeveTerRespostasCorretas_andRespostasQuaseCorretas(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = Ataque([1, 2, 5, 4])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertEqual(ataque.armasCorretasNaPosicaoCorreta, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoErrada, 2)

    # Teste unitário da questão 1 quando deve retornar True
    def teste_acertouAtaque_givenRespostaCerta_whenAtacar_thenAcertouAlgumAtaqueRetornaTrue(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = AtaqueSpy([1, 5, 2, 4])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertTrue(ataque.acertouAlgumAtaque)

    # Teste unitário da questão 1 quando deve retornar False
    def teste_acertouAtaque_givenRespostaCerta_whenAtacar_thenAcertouAlgumAtaqueRetornaFalse(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = AtaqueSpy([3, 6, 7, 8])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertFalse(ataque.acertouAlgumAtaque)

    # Teste unitário da questão 2 quando deve retornar True
    def teste_acertouAtaque_givenRespostaQuaseCerta_whenAtacar_thenAcertouAlgumaArmaRetornaTrue(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = AtaqueSpy([1, 2, 5, 4])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertTrue(ataque.acertouAlgumaArma)

    # Teste unitário da questão 2 quando deve retornar False
    def teste_acertouAtaque_givenRespostaQuaseCerta_whenAtacar_thenAcertouAlgumaArmaRetornaFalse(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = AtaqueSpy([3, 6, 7, 8])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertFalse(ataque.acertouAlgumaArma)

    # Teste unitário da questão 3 quando deve retornar True
    def teste_atacar_givenRespostaCorreta_whenAtacar_thenConferirGanhouRetornaTrue(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = AtaqueStub() # valor do ataque = [1, 5, 2, 4]

        #when
        self.sut.atacar(ataque)

        #then
        self.assertTrue(ataque.conferirSeGanhou())

    # Teste unitário da questão 3 quando deve retornar False
    def teste_atacar_givenRespostaErrada_whenAtacar_thenConferirGanhouRetornaFalse(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorDummy()
        self.sut = JogoDummy(self.monstro, self.jogador)
        ataque = Ataque([1, 2, 3, 4]) # valor do ataque

        #when
        self.sut.atacar(ataque)

        #then
        self.assertFalse(ataque.conferirSeGanhou())

    # Teste unitário da questão desafio para mostrar que o método atacar da classe Jogo está errado
    def teste_atacar_givenRespostaErrada_whenAtacar_thenJogadorPerdeVida(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.jogador = JogadorSpy(3)
        self.sut = Jogo(self.monstro, self.jogador)
        ataque = Ataque([3, 6, 7, 8])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertTrue(self.jogador.perdeuAlgumaVida)

if __name__ == '__main__':
    unittest.main(verbosity=2)
