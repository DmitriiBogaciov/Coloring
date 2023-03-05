import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = 7
edges = 1
all_steps = 10000
file = 'dsjc250.txt'

Gb = nx.Graph()
color_mus = list(range(1, nodes + 1))
rng = np.random.default_rng(12345)  # seed


def is_coloring(G, col):
    for u, v in G.edges():
        if col[u] == col[v]:
            return False
    return True


def greedy_color(G):
    colors = {}
    for v in G.nodes:
        used_colors = set(colors.get(n, -1) for n in G.neighbors(v))
        for g_color in range(len(G.nodes)):
            if g_color not in used_colors:
                colors[v] = g_color
                break
    return list(colors.values())


def color(G, colors, k, steps):
    best_col = colors[:]
    best_num_colors = len(set(colors))
    current_col = []

    for i in range(steps):
        # Random walk
        r_node = rng.integers(G.number_of_nodes())  # выбираем случайную вершину
        r_color = colors[rng.integers(k)]  # выбираем случайный цвет
        col_new = best_col[:]  # копируем текущую раскраску новую раскраску
        col_new[r_node] = r_color  # меняем цвет вершины
        if is_coloring(G, col_new):  # проверяем если раскраска правильная
            if len(set(col_new)) <= best_num_colors:
                current_col = col_new[:]
                # Hill climbing
                for j in range(steps):
                    r_node = rng.integers(G.number_of_nodes())
                    r_color = colors[rng.integers(k)]
                    col_new = best_col[:]
                    col_new[r_node] = r_color
                    if is_coloring(G, col_new):
                        if len(set(col_new)) <= len(set(current_col)):
                            current_col = col_new[:]
                            best_num_colors = len(set(current_col))
                best_col = current_col[:]
    print(best_col)
    print(is_coloring(G, best_col))
    print(len(set(best_col)))
    nx.draw(G, node_color=best_col, with_labels=True)
    plt.show()
    return best_col, is_coloring(G, best_col), len(set(best_col))


def read_dimacs(filename):
    d_file = open(filename, 'r')
    lines = d_file.readlines()

    Gd = nx.Graph()

    for line in lines:
        if line[0] == "e":
            vs = [int(s) for s in line.split() if s.isdigit()]
            Gd.add_edge(vs[0] - 1, vs[1] - 1)
    return Gd


def plot(G, cols):
    # symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # col_map = ["#" + ''.join(rng.choice(symbols, 6)) for _ in range(k + 1)]
    #
    # colors = [col_map[c] for c in cols]

    # exam = is_coloring(Gb, colors)
    # print(exam)

    plt.pause(0.001)
    G = read_dimacs(file)
    initial_colors = greedy_color(G)
    print(is_coloring(G, initial_colors))
    color(G, initial_colors, len(set(initial_colors)), all_steps)

    # nx.draw(G, node_color=colors, with_labels=True)
    # plt.show()


plot(Gb, color_mus)
