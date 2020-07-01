import networkx as nx
from functions.drawings import draw_subtree
from functions.prims_funcs import cost, low_edge

"""The following descibes the prims_algorithm function

The function prims_algorithm takes 4 agruments: a graph 'G', an integer 
indicating a node called 'starting_node', and two booleans called 'draw' and 
'attr' which are set to False by default. 
This function will then build an MST using the imported functions: cost(G,e) 
and low_edge(G,e) from the directory functions/prims_funcs
T is initilized as graph using the imported network library.
A 'starting_node' is arbitarilly chosen and added to T. While the set of nodes
in T is not equal to the set of nodes in G the loop will continue. For each
iteration of the loop, e is initialized to the return value of low_edge(G,T).
This means that e is the lowest cost edge from some node in T to some node in G
An edge (a tuple of u,v,d format where d is weight) is then added to T
This loop continues until all nodes (vertices) have been added to T and a 
lowest cost edge connects the nodes of T into a tree.
The function then returns the updated tree T

When draw == True, a graph will be drawn in the 'Plots' window using the
draw_subtree function imported from functions/drawings. 
When attr == True, additional text will be outputted to the console. 
The outputted text will print lists of the nodes and edges in T 
After summing the cost of the edges in T using the cost function imported from
functions/prims_funcs, the output text will also include the total cost of 
the MST.
"""

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
    

