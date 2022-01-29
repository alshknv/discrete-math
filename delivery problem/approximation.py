import networkx as nx


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    length = 0
    for i in range(1, len(cycle)+1):
        length += g[cycle[i-1]][cycle[i % len(cycle)]]['weight']
    return length

# The function should return a 2-approximation of an optimal Hamiltonian cycle.


def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    mst = nx.minimum_spanning_tree(g)
    preord = list(nx.dfs_preorder_nodes(mst, 0))
    return cycle_length(g, preord)


g = nx.Graph()
g.add_edge(0, 1, weight=1)
g.add_edge(1, 2, weight=5)
g.add_edge(0, 2, weight=1)
g.add_edge(0, 3, weight=10)
g.add_edge(1, 3, weight=2)
g.add_edge(2, 3, weight=3)

assert(approximation(g) == 7)
