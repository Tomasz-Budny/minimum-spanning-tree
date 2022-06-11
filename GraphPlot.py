import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('assets\\domek_small.png')


def update_graph(G, pos):
    labels = nx.get_edge_attributes(G, 'weight')

    plt.close()
    fig = plt.figure(figsize=(8, 8), facecolor='w')
    ax = plt.subplot()
    plt.title('Sieć elektryczna')
    ax.set_aspect('equal')
    nx.draw_networkx_edges(G, pos, ax=ax)

    plt.xlim(-1.15, 1.15)
    plt.ylim(-1.15, 1.15)

    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform

    piesize = 0.1  # this is the image size
    p2 = piesize / 2.0
    for n in G:
        xx, yy = trans(pos[n])  # figure coordinates
        xa, ya = trans2((xx, yy))  # axes coordinates
        a = plt.axes([xa - p2, ya - p2, piesize, piesize])
        a.set_aspect('equal')
        a.imshow(img)
        a.axis('off')
    ax.axis('off')

    # nx.draw_networkx_edges(G, pos, [('Domek', 'C')], ax=ax, width=5, alpha=0.9, edge_color="tab:red")
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=labels)
    label_pos = {}
    for key, value in pos.items():
        label_pos.update({key: [value[0], value[1] - 0.11]})
    nx.draw_networkx_labels(G, label_pos, ax=ax, font_size=10, font_family='serif')
    plt.savefig("graph.png", bbox_inches='tight')


def add_edge(G, u, v):
    G.add_edge(u, v)


def add_node(G, n, nodes_array):
    name = 'Dom ' + str(n)
    G.add_node(name)
    nodes_array.append(name)
