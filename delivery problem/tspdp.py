import networkx as nx
from itertools import chain, combinations

# This function returns all the subsets of the given set s in the increasing order of their sizes.


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# This function finds an optimal Hamiltonian cycle using the dynamic programming approach.
def dynamic_programming(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # The variable power now contains a tuple for each subset of the set {1, ..., n-1}.
    power = powerset(range(1, n))
    # The variable T is a dictionary, where the element T[s, i] for a set s and an integer i
    T = {}
    # For every non-zero vertex i, we say that T[ tuple with the element i only, i]
    # equals the weight of the edge from 0 to i.
    for i in range(1, n):
        T[(i,), i] = g[0][i]['weight']

    # For every subset s of [1,...,n-1]
    for s in power:
        # We have already initialized the elements of T indexed by sets of size 1, so we skip them.
        if len(s) > 1:
            # For every vertex i from s which we consider as the ending vertex of a path going through vertices from s.
            for i in s:
                # Define the tuple which contains all elements from s without *the last vertex* i.
                t = tuple([x for x in s if x != i])
                # Now we compute the optimal value of a cycle which visits all vertices from s and ends at the vertex i.
                for j in t:
                    if (s, i) not in T.keys():
                        T[s, i] = float("inf")
                    T[s, i] = min(T[s, i], T[t, j] + g[j][i]['weight'])

    # Return the weight of on optimal cycle - this is the minimum of the following sum:
    # weight of a path + the last edge to the vertex 0.
    return min(T[tuple(range(1, n)), i] + g[i][0]['weight'] for i in range(1, n))


g = nx.Graph()
g.add_edge(0, 1, weight=1)
g.add_edge(1, 2, weight=5)
g.add_edge(0, 2, weight=1)
g.add_edge(0, 3, weight=10)
g.add_edge(1, 3, weight=2)
g.add_edge(2, 3, weight=3)

assert(dynamic_programming(g) == 7)
