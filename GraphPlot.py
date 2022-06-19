import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from PIL import Image
import os
os.environ["PATH"] += 'gev\\bin\\'

img = mpimg.imread('assets\\domek_small.png')  


def update_graph(G, pos, T):
    labels = nx.get_edge_attributes(G, 'weight')

    plt.close()
    fig = plt.figure(figsize=(8, 8), facecolor='w')
    ax = plt.subplot()
    plt.title('Sieć elektryczna')
    ax.set_aspect('equal')
    nx.draw_networkx_edges(G, pos, ax=ax)
    # koloruje krawędzie minimalnego drzewa rozpinającego
    nx.draw_networkx_edges(T, pos, width=5, edge_color="r")
    #Moduł analizujący

    plt.xlim(-1.15, 1.15)
    plt.ylim(-1.15, 1.15)
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform

    piesize = 0.1
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


def get_minimum_spanning_tree(G):
    T = nx.minimum_spanning_tree(G)

    if not nx.is_empty(T):
        plt.close()
        sum_weights = T.size(weight='weight')
        title = "Minimalne drzewo rozpinające"
        if not nx.is_connected(T):
            title = "Minimalne drzewa rozpinające"
        plt.title(f"{title}\n(suma wag krawędzi: {sum_weights})")
        Tpos = graphviz_layout(T, prog="dot")
        nx.draw(T, Tpos, with_labels=True)
        labels = nx.get_edge_attributes(T, 'weight')
        nx.draw_networkx_edge_labels(T, Tpos, edge_labels=labels)

        plt.savefig("MST.png")
        MST = Image.open('MST.png')
        MST.show()
    return T


def add_edge(G, u, v, weight_of_edge):
    if G.has_edge(u, v):
        remove_edge(G, u, v)
    G.add_edge(u, v, weight=weight_of_edge)


def add_node(G, n, nodes_array):
    name = f'Dom{n}'
    G.add_node(name)
    nodes_array.append(name)


def remove_node(G, node, nodes_array):
    name = node
    G.remove_node(name)
    nodes_array.remove(name)


def remove_edge(G, u, v):
    G.remove_edge(u, v)
