import numpy as np
import PySimpleGUI as sg
import networkx as nx
from GraphPlot import update_graph, add_node, add_edge

G = nx.Graph()
pos = nx.shell_layout(G)
n = 1
nodes_array = []

layout = [
          [sg.Image('graph.png', key='graph_img', size=(630, 650))],
          [sg.Button('Dodaj węzeł'), sg.Button('update'), sg.Button('clear')],
          [sg.Button('Dodaj krawędź'), sg.OptionMenu(values=['-'], key='ddl1'), sg.OptionMenu(values=['-'], key='ddl2')]]


def update_app():
    update_graph(G, pos)
    window['graph_img'].update('graph.png', size=(630, 650))
    window['ddl1'].update(values=nodes_array)
    window['ddl2'].update(values=nodes_array)


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
            if selected_data1 == "" or selected_data1 == "-":
                continue
            if selected_data2 == "" or selected_data2 == "-":
                continue
            add_edge(G, selected_data1, selected_data2)
            update_app()

    window.close()