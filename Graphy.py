import unittest
from abc import ABC


class GraphInterface(ABC):

    def addNode(self, node):
        return NotImplemented

    def nodeCount(self):
        return NotImplemented

    def addBridge(self, nd1, nd2):
        return NotImplemented

    def bridgeCount(self):
        return NotImplemented

    def isNodesConnected(self, nd1, nd2):
        return NotImplemented


class Graph(GraphInterface):
    def __init__(self, noeud=[], pont = {}):
        self.nodes = noeud
        self.bridges = pont

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.bridges[node] = []

    def addBridge(self, nodeA, nodeB):
        self.bridges[nodeA].append(nodeB)
        self.bridges[nodeB].append(nodeA)

    def isNodesConnected(self, nodeA, nodeB):
        return nodeA in self.bridges[nodeB] and nodeB in self.bridges[nodeA]

    def nodeCount(self):
        return len(self.nodes)


class TestGraph(unittest.TestCase):

    def test_add_node(self):
        g = Graph()
        g.addNode("n1")
        g.addNode("n2")
        self.assertEqual(2, g.nodeCount())

    def test_addBridge(self):
        g = Graph()
        g.addNode("n1")
        g.addNode("n2")
        g.addBridge("n1", "n2")
        self.assertTrue(g.isNodesConnected("n1", "n2"))


if __name__ == '__main__':
    unittest.main()
