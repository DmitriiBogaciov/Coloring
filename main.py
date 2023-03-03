import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

Gb = nx.barabasi_albert_graph(20, 5)
colormus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rng = np.random.default_rng(12345)  # seed


# bere na vstupu pole barev vrcholu poporade, cislum priradi nahodne barvy a vykresli graf
def plot(G, cols):
    k = np.max(cols)
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    colmap = ["#" + ''.join(rng.choice(symbols, 6)) for i in range(k + 1)]

    colors = [colmap[c] for c in cols]

    nx.draw(G, node_color=colors, with_labels=True)
    plt.show()


plot(Gb, colormus)
