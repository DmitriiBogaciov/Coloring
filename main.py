import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = 50
edges = 3
steps = 1000

Gb = nx.barabasi_albert_graph(nodes, edges)
colormus = list(range(1, nodes + 1))
rng = np.random.default_rng(12345)  # seed


def iscoloring(G, col):
    for u, v in G.edges():
        if col[u] == col[v]:
            return False
    return True


def color(G, k, steps):
    col = [0] * G.number_of_nodes()
    bestcol = col[:]
    bestscore = 0

    # Random initialization
    for i in range(G.number_of_nodes()):
        col[i] = rng.integers(k)
    score = sum([iscoloring(G, col)])
    if score > bestscore:
        bestcol = col[:]
        bestscore = score

    for i in range(steps):
        # Random walk
        rnode = rng.integers(G.number_of_nodes())
        rcolor = rng.integers(k)
        colnew = col[:]
        colnew[rnode] = rcolor
        score = sum([iscoloring(G, colnew)])
        if score > bestscore:
            bestcol = colnew[:]
            bestscore = score
        # Hill climbing
        for j in range(10):
            rnode = rng.integers(G.number_of_nodes())
            rcolor = rng.integers(k)
            colnew = col[:]
            colnew[rnode] = rcolor
            score = sum([iscoloring(G, colnew)])
            if score > bestscore:
                bestcol = colnew[:]
                bestscore = score
            if score >= sum([iscoloring(G, col)]):
                col = colnew[:]
                break
    return bestcol, bestscore == G.number_of_nodes()


def plot(G, cols):
    k = np.max(cols)
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    colmap = ["#" + ''.join(rng.choice(symbols, 6)) for _ in range(k + 1)]

    colors = [colmap[c] for c in cols]

    exam = iscoloring(Gb, colors)
    print(exam)
    nx.draw(G, node_color=colors, with_labels=True)
    plt.show()


plot(Gb, colormus)
plt.pause(0.001)
