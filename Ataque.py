class Ataque:
    def __init__(self, armas):
        self.armas = armas
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

    def __del__(self):
        self.armas = []

    #Esse método está retornando True mesmo quando está errado
    def conferirAtaque(self, defesaDoMonstro):
        count = 0

        for armaDefensiva in defesaDoMonstro:
            if armaDefensiva == self.armas[count]:
                self.acertouAtaque()

            elif armaDefensiva in self.armas:
                self.acertouArma()

            count += 1

        #print("armas corretas na posição correta: " + str(self.armasCorretasNaPosicaoCorreta))
        return self.conferirSeGanhou()

    def acertouAtaque(self):
        self.armasCorretasNaPosicaoCorreta += 1

    def acertouArma(self):
        self.armasCorretasNaPosicaoErrada += 1

    def conferirSeGanhou(self):
        return self.armasCorretasNaPosicaoCorreta == 4


class AtaqueDummy(Ataque):
    pass

class AtaqueSpy(Ataque):
    def __init__(self, armas):
        self.armas = armas
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0
        self.acertouAlgumAtaque = False
        self.acertouAlgumaArma = False

    def __del__(self):
        self.armas = []

    def acertouAtaque(self):
        self.armasCorretasNaPosicaoCorreta += 1
        self.acertouAlgumAtaque = True

    def acertouArma(self):
        self.armasCorretasNaPosicaoErrada += 1
        self.acertouAlgumaArma = True

class AtaqueStub(Ataque):
    def __init__(self):
        self.armas = [1, 5, 2, 4]
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

    def __del__(self):
        self.armas = []