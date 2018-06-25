from random import randint


class MontyHall:
    def __init__(self):
        self.portes = self.init_porte()
        self.myIndexChoice = randint(0, 2)
        self.MCIndexChoice = self.MCChoose()
        self.resultat = self.portes[self.myIndexChoice]

    def init_porte(self):
        listedeporte = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        return listedeporte[randint(0,2)]

    def MCChoose(self):
        indexesofzero = self.__getIndexOfZero()
        selectIndexZero = randint(0,1)
        if self.myIndexChoice in indexesofzero and indexesofzero[selectIndexZero] == self.myIndexChoice:
            if selectIndexZero == 0:
                return indexesofzero[1]
            else:
                return indexesofzero[0]
        else:
            return indexesofzero[selectIndexZero]

    def changePorte(self):
        self.resultat = not self.resultat

    def __getIndexOfZero(self):
        indexesofzero = []
        for porteindex in range(0, self.portes.__len__()):
            if self.portes[porteindex] == 0:
                indexesofzero.append(porteindex)
        return indexesofzero


class Simulator:
    def __init__(self, number):
        self.simulationNumber = number
        self.victoireSurChangement = 0
        self.victoireSurIdle = 0
        self.main()

    def main(self):

        for i in range(1,self.simulationNumber):
            game = MontyHall()
            if randint(0,1):
                game.changePorte()

                if game.resultat:
                    self.victoireSurChangement += 1
            else:

                if game.resultat:
                    self.victoireSurIdle +=1

    def results(self):
        print("Nombres de tours : %s" % self.simulationNumber)
        print("Nombre de victoire au changement de portes : %s" % self.victoireSurChangement)
        print("Nombre de victoire quand on change pas : %s " % self.victoireSurIdle)


Simulator(10000).results()








