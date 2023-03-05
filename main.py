import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = 7
edges = 2
all_steps = 100

Gb = nx.barabasi_albert_graph(nodes, edges)
color_mus = list(range(1, nodes + 1))
rng = np.random.default_rng(12345)  # seed


def is_coloring(G, col):
    for u, v in G.edges():
        if col[u] == col[v]:
            return False
    return True


def color(G, colors, k, steps):
    best_col = colors[:]
    best_num_colors = len(set(colors))

    for i in range(steps):
        # Random walk
        r_node = rng.integers(G.number_of_nodes())  # выбираем случайную вершину
        r_color = colors[rng.integers(k)]  # выбираем случайный цвет
        col_new = best_col[:]  # копируем текущую раскраску новую раскраску
        col_new[r_node] = r_color  # меняем цыет верщины
        if is_coloring(G, col_new):  # проверяем если раскраска правильная
            if len(set(col_new)) <= best_num_colors:
                best_col = col_new[:]
                best_num_colors = len(set(col_new))
        # Hill climbing
        for j in range(steps):
            r_node = rng.integers(G.number_of_nodes())
            r_color = colors[rng.integers(k)]
            col_new = best_col[:]
            col_new[r_node] = r_color
            if is_coloring(G, col_new):
                if len(set(col_new)) <= best_num_colors:
                    best_col = col_new[:]
                    best_num_colors = len(set(col_new))

    print(best_col)
    print(is_coloring(G, best_col))
    print(len(set(best_col)))
    nx.draw(G, node_color=best_col, with_labels=True)
    plt.show()
    return best_col, is_coloring(G, best_col), len(set(best_col))


def plot(G, cols):
    k = np.max(cols)
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    col_map = ["#" + ''.join(rng.choice(symbols, 6)) for _ in range(k + 1)]

    colors = [col_map[c] for c in cols]

    exam = is_coloring(Gb, colors)
    print(exam)

    color(Gb, colors, k, all_steps)

    # nx.draw(G, node_color=colors, with_labels=True)
    # plt.show()


plot(Gb, color_mus)
plt.pause(0.001)
