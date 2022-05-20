
from collections import deque
import os
INFINITY = float("inf")

class Graph:
    def __init__(self, arquivo):
        """Lê os grafos através da instancia e a transforma para uma forma mais
        facil de se utilizar nos algoritmos
        """

        graph_edges = []
        with open(arquivo) as f:
            with open('temp','w') as f2:
                for i,linha in enumerate(f):
                    if i == 0:
                        n = int(linha)
                    else:
                        pesos = linha.strip().split(" ")
                        for j in range(i,n):
                             f2.write(f'{i} {j+1} {pesos[j-i]}\n')
            with open('temp','r') as f2:
                for line in f2:
                    edge_from, edge_to, cost, *_ = line.strip().split(" ")
                    graph_edges.append((edge_from, edge_to, float(cost)))
            os.remove('temp')

        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])

        self.adjacency_list = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.adjacency_list[edge[0]].add((edge[1], edge[2]))

    def dijkstra(self, start_node, no_final):
        """Usa o algoritmo Djikstra para retornar a menor distancia entre dois nós. 
        Retorna uma tupla (caminho, distância).
        """

        nao_visitados = self.nodes.copy()  # Todos os nós são inicialmente não visitados

        distancia_inicio = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        no_previo = {node: None for node in self.nodes}

        while nao_visitados:
            no_atual = min(
                nao_visitados, key=lambda node: distancia_inicio[node]
            )
            nao_visitados.remove(no_atual)

            if distancia_inicio[no_atual] == INFINITY:
                break

            for vizinho, distancia in self.adjacency_list[no_atual]:
                novo_caminho = distancia_inicio[no_atual] + distancia
                if novo_caminho < distancia_inicio[vizinho]:
                    distancia_inicio[vizinho] = novo_caminho
                    no_previo[vizinho] = no_atual

            if no_atual == no_final:
                break

        path = deque()
        no_atual = no_final
        while no_previo[no_atual] is not None:
            path.appendleft(no_atual)
            no_atual = no_previo[no_atual]
        path.appendleft(start_node)

        return path, distancia_inicio[no_final]
