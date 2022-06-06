import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('..\\assets\\domek_small.png')

G = nx.DiGraph()
G.add_node('Domek', image=img)
G.add_node('B', image=img)
G.add_node('C', image=img)
G.add_node('D', image=img)
G.add_node('Tomek', image=img)
G.add_node('Dodatkowy #1', image=img)
G.add_node('Dodatkowy #2', image=img)
G.remove_node('D')
G.remove_node('Domek')

G.add_edge('Domek', 'B', weight=5)
G.add_edge('Domek', 'C', weight=1000)
G.add_edge('Domek', 'Tomek', weight=10)
G.add_edge('Dodatkowy #1', 'Tomek', weight=2)

pos = nx.shell_layout(G)
# nx.draw(G, pos,  with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')

# rysowanie podpisów na krawędziach i kolorowanie ich na inny odcień

fig = plt.figure(figsize=(7, 7))
ax = plt.subplot()
ax.set_aspect('equal')
nx.draw_networkx_edges(G, pos, ax=ax)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform

piesize = 0.1  # this is the image size
p2 = piesize/2.0
for n in G:
    xx, yy = trans(pos[n])  # figure coordinates
    xa, ya = trans2((xx, yy))  # axes coordinates
    a = plt.axes([xa-p2, ya-p2, piesize, piesize])
    a.set_aspect('equal')
    a.imshow(img)
    a.axis('off')
ax.axis('off')

# nx.draw_networkx_edges(G, pos, [('Domek', 'C')], ax=ax, width=5, alpha=0.9, edge_color="tab:red")
nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=labels)
label_pos = {}
for key, value in pos.items():
    label_pos.update({key: [value[0], value[1] - 0.15]})
nx.draw_networkx_labels(G, label_pos, ax=ax, font_size=10, font_family='serif')

# zwraca tupla zawierającego wezel u i v oraz wage krawedzi
edges = [(u, v, G.get_edge_data(u, v).get('weight')) for u, v in G.edges()]
print(edges)
plt.savefig("..\\simple_path.png")
plt.show()