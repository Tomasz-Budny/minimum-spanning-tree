import numpy as np
import PySimpleGUI as sg
import networkx as nx
from GraphPlot import update_graph, add_node, add_edge, remove_node, remove_edge

G = nx.Graph()
pos = nx.shell_layout(G)
n = 1
nodes_array = []

layout = [
          [sg.Image('graph.png', key='graph_img', size=(630, 650))],
          [sg.Button('Dodaj węzeł'), sg.Button('Usuń węzeł'), sg.Button('update'), sg.Button('clear')],
          [sg.Button('Dodaj krawędź'), sg.Button('Usuń krawędź'), sg.OptionMenu(values=['-'], key='ddl1'), sg.OptionMenu(values=['-'], key='ddl2'), sg.Text('Waga krawędzi'), sg.Input(size=(5,5), key='ddl3')]]


def update_app():
    update_graph(G, pos)
    window['graph_img'].update('graph.png', size=(630, 650))
    window['ddl1'].update(values=nodes_array)
    window['ddl2'].update(values=nodes_array)
    window['ddl3'].update('')


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
            remove_node(G, n-1, nodes_array)
            n = n - 1
            pos = update_pos()
            update_app()

        if event == 'clear':
            G.clear()
            pos = update_pos()
            nodes_array.clear()
            n = 1
            update_app()

        if event == 'update':
            pos = update_pos()
            update_app()

        if event == 'Dodaj krawędź':
            selected_data1 = window['ddl1'].TKStringVar.get()
            selected_data2 = window['ddl2'].TKStringVar.get()
            selected_data3 = window['ddl3'].TKStringVar.get()
            if selected_data1 == "" or selected_data1 == "-":
                continue
            if selected_data2 == "" or selected_data2 == "-":
                continue
            add_edge(G, selected_data1, selected_data2, selected_data3)
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

    window.close()