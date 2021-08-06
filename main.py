import gera_grafo
import algoritimo_guloso 
import forca_bruta
import timeit




#gerando grafo
grafo = gera_grafo.gera_grafo(12, 1, 500)
grafo1 = [[None, 2.7, 3.1, 8.8, 6.1, 5.5], [2.7, None, 7.0, 7.6, 3.4, 3.5], [3.1, 7.0, None, 2.8, 7.4, 3.0],[8.8, 7.6, 2.8, None, 2.5, 4.2], [6.1, 3.4, 7.4, 3.5, None, 1.7], [5.5, 3.5, 3.0, 4.2, 1.7, None]]
grafo2 = [[None, 0, -4, -1], [0, None, -5, 10], [-4, -5, None, 0], [-1, 10, 0, None]]




print('Escolha a opção númerica para selecionar o algoritmo desejado')
selecao = input('1 - Algoritimo Guloso \n2 - algoritimo Força-Bruta :')
   

if selecao == '1':
    inicio = timeit.default_timer()
    caminho, peso = algoritimo_guloso.algoritimo_guloso(grafo)
    fim = timeit.default_timer()
   

elif selecao == '2':
    inicio = timeit.default_timer()
    caminho, peso = forca_bruta.forca_bruta(grafo)
    fim = timeit.default_timer()
   

else:
    print('Por favor, insira um valor correspondente a um dos algoritmos. \n\n')

if len(grafo[1]) < 20:
        for item in grafo:
            print('\t', item)
else:
    print('Grafo muito grande para ser impreso')
#print('Grafo: ', grafo)

print('Melhor Rota:', caminho)
print('Custo ', peso)
print('Tempo: %.5f s' % (fim - inicio))





