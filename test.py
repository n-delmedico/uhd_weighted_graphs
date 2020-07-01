# This is a test area for code development for this project
# Code in this area will not be documented further

import networkx as nx
from functions.drawings import draw_subtree

def prims_algorithm(G, starting_node, draw = False, attr = False):
    T = nx.Graph()
    T.add_node(starting_node)
    
    if draw == True:
        draw_subtree(G,T)
    
    while set(T.nodes()) != set(G.nodes()):
        e = low_edge(G,T)
        T.add_edge(e[0],e[1], weight = cost(G,e))
        if draw == True:
            draw_subtree(G,T)
            
    if attr == True:
        total_cost = sum(cost(G,e) for e in T.edges())
        print('')
        print('T Nodes = ',list(T.nodes()))
        print('T Edges = ',list(T.edges()))
        print('Cost = ',total_cost)
        
    return T        
    

def cost(G,e):
    return G.edges()[e]['weight']


def find_edges(G,T):
    possible_edge_list = []
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                possible_edge_list.append(e)
                
    good_edge_list = []
    for e in possible_edge_list:
        if e[0] in T.nodes() and e[1] in T.nodes():
            continue 
        else:
            good_edge_list.append(e)
    
    return good_edge_list

def low_edge(G,T):
    edge_list = find_edges(G,T)
    lowest_edge = edge_list[0]
    for e in edge_list:
        if cost(G,e) <= cost(G,lowest_edge):
            lowest_edge = e
        
    return lowest_edge
        

G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)
# G = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)
# G = nx.read_weighted_edgelist('data/G3.txt', nodetype = int)

T = prims_algorithm(G,0,draw=True,attr=True)
