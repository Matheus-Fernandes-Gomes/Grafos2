import itertools
#força bruta
def forca_bruta(grafo):

    i = 1
    menorPeso = float('inf')
    melhorCaminho = []
    caminhoAtual = []
    vertices = []
    total = 1 # Total de permutações que devem ser feitas
    soma = 0


    while i <= len(grafo) -1:
        total *= i
        vertices.append(i)
        i += 1

    i = 0
    j = 0

    for permutation in itertools.permutations(vertices):
        soma = 0
        j = 0
        for vertice in permutation:
            soma += grafo[j][vertice]
            caminhoAtual.append((j, vertice))
            j = vertice
        soma += grafo[j][0]
        caminhoAtual.append((j, 0))
        if soma < menorPeso:
            menorPeso = soma
            melhorCaminho.clear()
            melhorCaminho = caminhoAtual.copy()
        caminhoAtual.clear()
        i += 1

    return melhorCaminho, menorPeso