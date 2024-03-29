import numpy as np
import PySimpleGUI as sg
import networkx as nx
from GraphPlot import update_graph, add_node, add_edge, remove_node, remove_edge, get_minimum_spanning_tree

G = nx.Graph()
T = nx.Graph()
pos = nx.shell_layout(G)
n = 1
nodes_array = []

# ddl - Drop Down List
# wi - weight input

layout = [
    [sg.Image('graph.png', key='graph_img', size=(630, 650))],
    [sg.Button('Dodaj węzeł'), sg.Button('Wyczyść')],
    [sg.Button('Usuń węzeł'), sg.OptionMenu(values=['-'], key='ddl0')],
    [sg.Button('Dodaj krawędź'), sg.Button('Usuń krawędź'), sg.OptionMenu(values=['-'], key='ddl1'),
     sg.OptionMenu(values=['-'], key='ddl2'), sg.Text('Waga krawędzi'), sg.Input(size=(5, 5), key='wi')],
    [sg.Button('Analizuj')]
]


def update_app():
    update_graph(G, pos, T)
    window['graph_img'].update('graph.png', size=(630, 650))
    window['ddl0'].update(values=nodes_array)
    window['ddl1'].update(values=nodes_array)
    window['ddl2'].update(values=nodes_array)
    window['wi'].update('1')


def update_pos():
    return nx.shell_layout(G)


if __name__ == "__main__":
    sg.theme('DarkTeal')
    window = sg.Window('Grafy - Projekt', layout, finalize=True)
    update_app()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Dodaj węzeł':
            add_node(G, n, nodes_array)
            n = n + 1
            pos = update_pos()
            update_app()

        if event == 'Usuń węzeł':
            selected_node = window['ddl0'].TKStringVar.get()
            if selected_node != "":
                remove_node(G, selected_node, nodes_array)
                pos = update_pos()
                update_app()

        if event == 'Wyczyść':
            G.clear()
            pos = update_pos()
            nodes_array.clear()
            n = 1
            update_app()

        if event == 'Dodaj krawędź':
            try:
                selected_data1 = window['ddl1'].TKStringVar.get()
                selected_data2 = window['ddl2'].TKStringVar.get()
                selected_data3 = float(window['wi'].TKStringVar.get())
                if selected_data1 == "" or selected_data1 == "-":
                    continue
                if selected_data2 == "" or selected_data2 == "-":
                    continue
                add_edge(G, selected_data1, selected_data2, selected_data3)
            except ValueError:
                sg.Popup('Błąd', "Waga musi być liczbą!")
            finally:
                update_app()

        if event == 'Usuń krawędź':
            selected_data1 = window['ddl1'].TKStringVar.get()
            selected_data2 = window['ddl2'].TKStringVar.get()
            if selected_data1 == "" or selected_data1 == "-":
                continue
            if selected_data2 == "" or selected_data2 == "-":
                continue
            try:
                remove_edge(G, selected_data1, selected_data2)
                update_app()
            except nx.exception.NetworkXError:
                sg.Popup('Błąd', "Brak krawędzi między wybranymi wierzchołkami")

        if event == 'Analizuj':
            T = get_minimum_spanning_tree(G)
            update_app()
            T = nx.Graph()

    window.close()
