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
        return nodeA in self.bridges[nodeB] and nodeB in self.bridges[nodeA]

    def node_count(self):
        return len(self.nodes)

    def bridge_count(self):
        return NotImplemented

class TestGraph(unittest.TestCase):

    def test_add_node(self):
        g = Graph()
        g.addNode("n1")
        g.addNode("n2")
        self.assertEqual(g.node_count(),2)

    def test_addBridge(self):
        g=graph()
        g.addNode("n1")
        g.addNode("n2")
        g.addBridge("n1","n2")
        self.assertEqual(g.isNodesConnected("n1","n2"),True)



keymap = {"A" : ["B","C"],
          "B" : ["A"],
          "C" : ["A"]}
nodes = ["A", "B", "C"]

graph = Graph(nodes,keymap)

print( "A et B connecté ? : %s" % graph.isNodesConnected("A","B"))

print("C et B connecté ? %s" % graph.isNodesConnected("C","B"))

graph.addBridge("C","B")

print("C et B connecté ? %s" % graph.isNodesConnected("C","B"))

