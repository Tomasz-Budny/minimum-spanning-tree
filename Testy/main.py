import heapq
from Testy.Edge import Edge

e1 = Edge(0, 1, 1)
e2 = Edge(0, 2, 8)
e3 = Edge(1, 2, 1)
et = Edge(1, 5, 1)
e4 = Edge(1, 3, 5)
e5 = Edge(2, 4, 2)
e6 = Edge(2, 5, 3)
e7 = Edge(3, 4, 4)
e8 = Edge(3, 5, 6)

wn = 6

le = [e1, e2, e3, e4, e5, e6, e7, e8]
heapq.heapify(le)


def find(u, Z):
    if Z[u] != u:
        Z[u] = find(Z[u], Z)
    return Z[u]


def union(u, v, Z):
    Z[v] = find(u, Z)


def serce_aplikacji(le, wn):
    Z = list(range(0, wn))
    T = []
    i = 0
    while i < wn - 1:
        e = heapq.heappop(le)
        if find(e.u, Z) != find(e.v, Z):
            T.append(e)
            union(e.u, e.v, Z)
            i = i + 1
    return T


T = serce_aplikacji(le, wn)
print(T)