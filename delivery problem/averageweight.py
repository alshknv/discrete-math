import networkx as nx

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the average weight of a Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)


# average length of hamiltonian cycle

def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    # In case of undirected graph the probability of some edge to be in cycle
    # is (#edges_in_cycle) / (#edges_total) = n / (n*(n-1)/2) = 2 / (n-1)
    return (sum_of_weights * 2) / (n-1)
