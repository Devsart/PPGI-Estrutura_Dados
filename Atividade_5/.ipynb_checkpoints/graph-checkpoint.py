
from collections import deque
import os
import re
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
                        pesos = linha.strip()
                        pesos = re.split("\t| ",pesos)
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
    
    def Prim(grafo_adj, ini):
        vertices = list()
        arestas = dict()
        ArvMin = list()
        visitados = list()

        while True:  
            visitados.append(ini) # Armazena os vertices ja visitados
            for i in grafo_adj[ini]: # Adiciona as arestas conhecidas com excecao das que ligam a vertices ja visitados e substituindo por arestas de menor valor
                if (i not in vertices) and (i not in visitados): 
                    vertices.append(i)
                if i in arestas:
                    if arestas[i][0] > grafo_adj[ini][i]:
                        arestas[i] = grafo_adj[ini][i], ini
                else:
                    arestas[i] = grafo_adj[ini][i], ini

            menor = (MAX, '-')
            for i in vertices: # Encontra a menor aresta entre as arestas conhecidas
                if arestas[i][0] < menor[0]:
                    menor = (arestas[i][0], i)

            ArvMin.append([menor[0], arestas[menor[1]][1], menor[1]]) # Adiciona a aresta a ArvMin
            arestas.pop(menor[1]) # Remove das arestas conhecidas
            vertices.remove(menor[1]) # Remove da lista de vertices existentes
            ini = menor[1] # Armazena o vertice encontrado para adicionar as novas arestas conhecidas

            if not vertices: # Caso nao existam mais vertices, ou seja, todos ja tenham sido 'visitados' para o algoritmo
                break

        return ArvMin
    
    def kruskal()
