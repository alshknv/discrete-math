import networkx as nx


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    length = 0
    for i in range(1, len(cycle)+1):
        length += g[cycle[i-1]][cycle[i % len(cycle)]]['weight']
    return length


# Here is a test case:
# Create an empty graph.
g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]

assert(cycle_length(g, cycle1) == 8)
assert(cycle_length(g, cycle2) == 6)
