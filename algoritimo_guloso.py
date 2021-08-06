from funcoes import busca_menor


# algoritmo Dijkstra
#Recebe como entrada um grafo ponderado
def algoritimo_guloso(grafo):

    #criando visitados
    visitados = []    
    # Primeiro vértice
    u = 0
    #criando caminho
    caminho = []
    #atribuindo peso=0
    peso = 0
    i = 0
    visitados.append(i)

    while True:
        menor, posicao = busca_menor(grafo[u], visitados)
        peso += menor
        visitados.append(posicao)
        caminho.append((u, posicao))
        u = posicao

        if len(visitados) == len(grafo):
            caminho.append((u, 0))
            peso += grafo[u][0]
            return caminho, peso
