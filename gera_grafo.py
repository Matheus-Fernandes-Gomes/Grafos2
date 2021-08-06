from random import randint

def gera_grafo(vertice, menorPeso, maiorPeso):

    grafo = []
    i = 0
    j = 0


    while i < vertice:
        j = 0
        grafo.append([])
        while j < vertice:
            #diagonal principal = 0
            if i == j:
                grafo[i].append(0)
            else:
                grafo[i].append(0)
            j += 1
        i += 1

    i = 0
    j = 0

    while i < vertice:
        j = 0
        while j < vertice:
            if i != j:
                peso = randint(menorPeso, maiorPeso)
                grafo[i][j] = peso
                grafo[j][i] = peso
            j += 1
        i += 1

    return grafo