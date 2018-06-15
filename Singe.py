import time
import unittest



class Monkey :
    def __init__(self, name):
        self.name = name

    def eat(self, banana):
        print(self.name + " mange une banane de couleur " + banana.color)

    def reproduceWith(self, monkey, childrenName):
        print("wow c'est chaud entre " + self.name + " et " + monkey.name + "!")
        robert = Monkey(childrenName)
        time.sleep(5)
        print(robert.name + " est né !")
        return robert


class Banana :
    def __init__(self, color):
        self.color = color







pierre = Monkey("Pierre")
bananeVerte = Banana("verte")
marie = Monkey("Marie")
bananeJaune = Banana("Jaune")

marie.eat(bananeJaune)
pierre.eat(bananeVerte)

robert = pierre.reproduceWith(marie, "Robert")






