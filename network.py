import networkx as nx
import subprocess
from networkx.drawing.nx_pydot import write_dot

G = nx.Graph()

G.add_node("n1")
G.add_node("n2")
G.add_node("n3")
G.add_node("toto")

G.add_edge("n1", "n3")
G.add_edge("n1", "n2")

pos = nx.nx_agraph.to_agraph(G)
nx.draw(G, pos=pos)
write_dot(G, 'file.dot')

subprocess.call(["xdot", "file.dot"])