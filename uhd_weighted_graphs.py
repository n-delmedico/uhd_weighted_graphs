from algorithms.prims import prims_algorithm
import networkx as nx

# Three sample graphs are included in this project. Ensure that only 1 is
# active while keeping the others commented out.

G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)
# G = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)
# G = nx.read_weighted_edgelist('data/G3.txt', nodetype = int)

T = prims_algorithm(G,0,draw=True,attr=True)
# draw and attr are optional args which may be omitted
