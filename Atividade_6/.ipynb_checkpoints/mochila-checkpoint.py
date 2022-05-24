import numpy as np

class Mochila:
    def __init__(self,capacidade):
        self.capacidade = capacidade
    
    def getMax (pesos, valores, capacidade):
        arraySort = []
        for i in range(len(pesos)):
            arraySort.append (ObjetoDaMochila(pesos[i], valores[i], i))

        # Classifica os elementos da sacola pela razão
        arraySort.sort(reverse = True)

        conta_valor = 0
        itens = []
        for objeto in arraySort:
            peso_atual = int (objeto.peso)
            valor_atual = int (objeto.valor)
            if (capacidade - peso_atual) >= 0:
                # adicionamos o objeto no saco
                # Nós subtraímos a capacidade
                capacidade -= peso_atual
                conta_valor += valor_atual
                # Nós adicionamos o valor no saco
                itens.append(objeto.indice + 1)
        return itens, conta_valor
    
    def getMaxDinamico(pesos, valores,capacidade,n):
        g = np.zeros(shape=(capacidade+1,n+1))
        x = np.zeros(shape=(capacidade+1,n+1))
        g[:][n] = 0
        for i in range(n-1,-1,-1):
            for y in range(capacidade+1):
                if pesos[i] <= y:
                    g[y][i] = np.max([valores[i] + g[y-pesos[i]][i+1],g[y][i+1]])
                    x[y][i] = np.max([valores[i] + g[y-pesos[i]][i+1],g[y][i+1]]) == valores[i] + g[y-pesos[i]][i+1]
                else:
                    g[y][i] = g[y][i+1]
        return g,x
        
    def ler_instancia(nome_arquivo):
        pesos = []
        valores = []
        with open(nome_arquivo,'r') as f:
            for i,linha in enumerate(f):
                if(i == 0):
                    n,M = linha.strip().split(' ')
                    n = int(n)
                    capacidade = int(M)
                else:
                    p,v = linha.strip().split(' ')
                    pesos.append(int(p))
                    valores.append(int(v))
        return pesos,valores,capacidade,n
    
    def get_items(g,x,pesos):
        l_bin = []
        l_itens = []
        i,j = np.where(g == g.max())
        new_i = i[0] 
        _x = x[new_i,j[0]]
        l_bin.append(_x)
        for i in range(1,len(pesos)):
            if(_x!= 0):
                peso = pesos[i-1]
                new_i = new_i - peso
                _x = x[new_i,i]
                l_bin.append(_x)
            else:
                _x = x[new_i,i]
                l_bin.append(_x)
        for i,v in enumerate(l_bin):
            if(v == 1):
                l_itens.append(i+1)
        return l_bin,l_itens

class ObjetoDaMochila:
    def __init__(self,peso, valor,indice):
        self.indice = indice
        self.peso = peso
        self.valor = valor
        self.razao = valor / peso
    ## Sobrescreve comparacao entre objetos
    def __lt__(self, obj2):
        return self.razao <= obj2.razao
