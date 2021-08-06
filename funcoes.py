def busca_menor(lista, visitados):
    menor = float('inf')
    posicao = 0
    i = 0


    while i <  len(lista) :

        if lista[i] == None or i in visitados:
            i += 1
            continue

        if lista[i] < menor:
            posicao = i
            menor = lista[i]
        i += 1


    return menor, posicao