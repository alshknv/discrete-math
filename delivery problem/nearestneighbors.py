import networkx as nx


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
            if v in path:
                continue
            edge = g[current_node][v]['weight']
            if (edge < min_edge):
                min_edge = edge
                next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight']
                 for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
g.add_edge(0, 2, weight=3)
g.add_edge(0, 3, weight=7)
g.add_edge(1, 2, weight=4)
g.add_edge(1, 3, weight=6)
g.add_edge(2, 3, weight=3)

assert(nearest_neighbors(g) == 16)
