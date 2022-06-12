# -*- coding: utf-8 -*-

import networkx
import matplotlib.pyplot as plt
from itertools import combinations

#Biblioteka - przypisuje z kim ma połaczenie konkretne domostwo
vector = {}

#wprowadzamy liczbe domostw (mozna przerobic na while'a z warunem wyjscia)
liczba_domow = int(input(("Podaj liczbę domów do połączenia: ")))

#tablica z nazwami domostw
tab_domostwa = []

#Dodawanie kolejnych domostw-węzłów do tablicy inputem
for i in range (liczba_domow):
    tab_domostwa.append(input(('Podaj adres domu: '))) 
    
#oznaczenia wagi połączenia
edge_labels = {}

#tworzenie grafu pod Kruskala 
G = networkx.Graph()

#Ustawianie w bibliotece domow, do których będziemy przypisywać połączone z nim inne
for dom in tab_domostwa:
    vector[dom] = []
    vector[dom] = []

#przeszukujemy wszystkie kombinacje połączeń domów
#combinations tworzy wszystkie kombinacje tablic dwóch elementów z tab_domostwa
for pary_domow in combinations(tab_domostwa, 2): 
    dom1, dom2 = pary_domow 
    print("Ile wynosi odleglosc między "+ str(dom1) + ", a " + str(dom2) + " ? (wpisz 0 jesli są niepołączone: ")
    odleglosc = float(input()) #przypisujemy odleglosc miedzy konkretnymi domami w grafie

    
    if odleglosc == 0: #pomin jesli brak poloczenia
        continue
    else:
        G.add_edge(dom1,dom2,weight=odleglosc) #dodaj krawedz o danej wadze   
        vector[dom1].append(dom2) #przypisz somsiada
        edge_labels[(dom1, dom2)] = odleglosc #dodaj oznaczenie wagi do krawedzi

#przjrzenie jak wygladaja biblioteki
#print (edge_labels)
#print(vector,"wektor")


graph = networkx.Graph(vector)  #tworzenie grafu (z wszystkimi połaczeniami) 
#print(graph, "graph")

pos = networkx.spring_layout(graph)  #Wspolrzedne na grafie dla wezłów
#print(pos, "pos")


#Tworzenie grafu
networkx.draw_networkx_nodes(graph, pos, node_size=15, node_color="r")
networkx.draw_networkx_edges(graph, pos, width=1)
networkx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
networkx.draw_networkx_labels(graph, pos, font_size=16, font_color="b")
plt.title('Sieć elektryczna we wsi')

#nałożenie na rysunek minimalnej sieci rozpinającej wdg Kruskala

T = networkx.minimum_spanning_tree(G)

#nałożenie czerwonych krawedzi na graf
networkx.draw_networkx_edges(T, pos, width=1, edge_color="r")

#wypisuje posortowane najkrótsze krawędzie
print(sorted(T.edges(data=True)))

plt.savefig("graf_poloczenie_we_wsi.png")
plt.show()
