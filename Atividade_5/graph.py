
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
                        pesos = re.split("\t| ",linha.strip())
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
    
    def prim(self):
        """Usa o algoritmo Prim para solucionar o problema da árvore mínima espalhada. 
        Retorna um set de tuplas (no_inicio, no_fim), representando as arestas.
        """
        self.arvore = set()
        nao_visitados = self.nodes.copy()  # Todos os nós são inicialmente não visitados
        
        distancia_inicio = {
            node: (0 if node == '1' else INFINITY) for node in self.nodes
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
                if((vizinho in nao_visitados) & (distancia_inicio[vizinho] > distancia)):
                    distancia_inicio[vizinho] = distancia
                    no_previo[vizinho] = no_atual
            
        for node in self.nodes:
            self.arvore.add((no_previo[node],node))
        self.arvore.discard((None,'1'))
        return self.arvore
        

    def quicksort(self,vetor,inicio,fim):
        if(inicio < fim):
            q = self.pQSort(vetor,inicio,fim) #q[0] = pivo; q[1] = inicio; q[2] = fim
            self.quicksort(vetor, q[1],q[0]-1) #(vetor, inicio, pivo-1)
            self.quicksort(vetor, q[0]+1,q[2]) #(vetor, pivo+1, fim)

    def pQSort(self,vetor,inicio,fim):
        pivo = vetor[fim]
        i = inicio-1

        for j in range(inicio,fim):
            if(self.peso(vetor[j]) <= self.peso(pivo)):
                i += 1
                vetor[i],vetor[j] = vetor[j],vetor[i]

        vetor[i+1],vetor[fim] = vetor[fim],vetor[i+1]
        return i+1,inicio,fim

    def peso(self, aresta):
        for v,p in self.adjacency_list[aresta[0]]:
            if(v == aresta[1]):
                return p

    def ordena_arestas(self):
        arestas_ordenadas = []
        for u in self.nodes:
            for v,peso in self.adjacency_list[u]:
                arestas_ordenadas.append(tuple([u, v]))
        self.quicksort(arestas_ordenadas,0,len(arestas_ordenadas)-1)
        return arestas_ordenadas

    def makeSet(self,x,sets):
        sets[x] = set([x])
        return sets
        
    def find(self,x):
        for representative,subset in self.sets.items():
            if x in subset:
                return representative
        return None

    def union(self,x, y):
        xRepresentative = self.find(x)
        yRepresentative = self.find(y)
        self.sets[yRepresentative] = self.sets[yRepresentative].union(self.sets[xRepresentative])
        del self.sets[xRepresentative]

    def kruskal(self):
        """Usa o algoritmo Kruskal para solucionar o problema da árvore mínima espalhada. 
        Retorna uma lista de tuplas (no_inicio, no_fim), representando as arestas.
        """
        arestas_ordenadas = self.ordena_arestas()
        arvore_geradora_minima = []
        self.sets = {}
        for v in self.nodes:
            self.sets = self.makeSet(v,self.sets)
        for aresta in arestas_ordenadas:
            if self.find(aresta[0]) != self.find(aresta[1]):
                arvore_geradora_minima.append(aresta)
                self.union(aresta[0], aresta[1])

        return arvore_geradora_minima
