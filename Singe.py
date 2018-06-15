import time


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


class Graph :
    def __init__(self,nodes=[],bridges={}):
        self.nodes = nodes
        self.bridges = bridges


    def addNode(self,node):
        self.nodes.append(node)

    def addBridge(self,nodeA,nodeB):
        self.bridges[nodeA].append(nodeB)
        self.bridges[nodeB].append(nodeA)



    def isNodesConnected(self,nodeA,nodeB):
        if nodeA in self.bridges[nodeB] and nodeB in self.bridges[nodeA]:
            return "true"
        else:
            return "false"




pierre = Monkey("Pierre")
bananeVerte = Banana("verte")
marie = Monkey("Marie")
bananeJaune = Banana("Jaune")

marie.eat(bananeJaune)
pierre.eat(bananeVerte)

robert = pierre.reproduceWith(marie, "Robert")



keymap = {"A" : ["B","C"],
          "B" : ["A"],
          "C" : ["A"]}
nodes = ["A", "B", "C"]

graph = Graph(nodes,keymap)

print( "A et B connecté ? : " + graph.isNodesConnected("A","B"))

print("C et B connecté ? " + graph.isNodesConnected("C","B"))

graph.addBridge("C","B")

print("C et B connecté ? " + graph.isNodesConnected("C","B"))





