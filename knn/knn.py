import math
from builtins import len

from sklearn.neighbors import KNeighborsClassifier


entradas = [[3,2,1],[3,3,1],[2,4,3],[2,1,4],[8,9,3],[6,8,3],[7,4,2],[6,7,8],[4,2,3],[9,6,8]]
saidas =  [1,1,1,1,0,0,0,0,1,0]




class KNN(object):
    """Classe que resposvel pelas operações do KNN"""

    def __init__(self, k):
        self.k = k

    def euclidean_dist(self, p, q):
        size = len(p)
        sum = 0
        for i in range(size):
        	sum += math.pow(p[i]-q[i],2)
        return math.sqrt(sum)


if __name__ == '__main__':

    p = 0.6
    limite = int(p * len(entradas))
    knn = KNeighborsClassifier(n_neighbors=3,p=1)
    knn.fit(entradas[:limite], saidas[:limite])
    labels = knn.predict(entradas[limite:])

    acertos, indice_label = 0, 0

    for i in range(limite, len(entradas)):
        if labels[indice_label] == saidas[i]:
            acertos += 1
        indice_label += 1

    print("Total de treinamento %d" % limite)
    print("Total de teste %d" % (len(entradas) - limite))
    print("Total de acertos %d" % acertos)
    print("Porcentagem de acertos %2.f" % (100*acertos/(len(entradas)-limite)))

    # print(labels)
    # print(len(saidas))