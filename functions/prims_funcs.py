def cost(G,e):
    return G.edges()[e]['weight']
# returns the value of weight attribute of the edge 'e' in the graph G

    
"""The following descibes the find_edges function

The function find_edges(G,T) takes two arguments G and T and determines which 
edges, if any, may be added from the graph G to the tree T. The function then
returns a list of these edges.
To accomplish this, an empty list named possible_edge_list is initiallized.
This list will contain all the possible edges from the nodes in T to the nodes
in G.
Two nested for-loops iterate through the vertices in T.nodes() and the edges
in G.edges(). For every vertex in T.nodes() if the vertex 'v' is an endpoint
of the edge 'e' in G.edges(), it is appended to possible_edge_list.
Once the nested for-loop is completed another empty list named 
good_edge_list is initialized.
Like possible_edge_list, good_edge_list will contain all valid edges from 
nodes in T to the nodes in  with the exception of the edges already in T.
This is achieved by ignoring any edge where both of the endpoints (vertices) 
are already present in T.
Finally, the function returns good_edge_list which is used by the 
function low_edge(G,T).
"""

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

"""The following descibes the low_edge function

The function low_edge(G,T) takes two arguments G and T, determines which of
the available edges has the lowest cost (weight), then returns that edge.
edge_list is intialized to the return value of the function find_edges(G,T)
lowest_edge is initialized to the first item in edge_list
edge_list is then iterated through using a for-loop to compare whether any of
the costs of edges in edge_list are less than the the cost of lowest_edge. This
is accomplished using the function cost(G,e).
The function will then update lowest_edge to the current edge 'e'.
Once the loop is complete, the function will return lowest_edge, which is
the edge with the lowest weight in the list edge_list.
"""

def low_edge(G,T):
    edge_list = find_edges(G,T)
    lowest_edge = edge_list[0]
    for e in edge_list:
        if cost(G,e) < cost(G,lowest_edge):
            lowest_edge = e
        
    return lowest_edge

