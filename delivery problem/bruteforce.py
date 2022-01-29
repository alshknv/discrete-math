from xmlrpc.client import MAXINT
import networkx as nx
from itertools import permutations
import cycleweight


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    minweight = MAXINT
    for p in permutations(range(n)):
        weight = cycleweight.cycle_length(g, p)
        if weight < minweight:
            minweight = weight
    return minweight


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)

assert(all_permutations(g) == 6)
