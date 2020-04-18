import math
import os
from builtins import len
import linecache
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from cf.cf import ComplementaryFilter


entradas = [[3,2,1],[3,3,1],[2,4,3],[2,1,4],[8,9,3],[6,8,3],[7,4,2],[6,7,8],[4,2,3],[9,6,8]]
saidas =  [1,1,1,1,0,0,0,0,1,0]

# entradas = [[3,2,1,1],[3,3,1,1],[2,4,3,1],[2,1,4,1],[8,9,3,0],[6,8,3,0],[7,4,2,0],[6,7,8,0],[4,2,3,1],[9,6,8,0]]





class KNN(object):
    """Classe que resposvel pelas operações do KNN"""

    def __init__(self, k):
        self.k = k


    """
    value: uma lista de cordenadas filtradas
    move_name: nome da jogada de tenis (backhand, spin)
    """
    def classify(self, value,move_name):
        n_lines = 5
        cf = ComplementaryFilter()
        categories = ['amateur','professional']

        for category in categories:
            files = os.listdir('../data/'+str(category)+'/'+str(move_name))
            print("========"+category+"===========")
            for file in files:
                print("FILE:"+str(file))
                filter_list = cf.get_cfilter('../data/'+str(category)+'/'+str(move_name)+'/'+str(file))
                print(filter_list)
        return 50



if __name__ == '__main__':

    # p = 0.6
    # limite = int(p * len(entradas))
    # knn = KNeighborsClassifier(n_neighbors=3,p=1)
    # knn.fit(entradas[:limite], saidas[:limite])
    # labels = knn.predict(entradas[limite:])
    #
    # acertos, indice_label = 0, 0
    #
    # for i in range(limite, len(entradas)):
    #     if labels[indice_label] == saidas[i]:
    #         acertos += 1
    #     indice_label += 1
    #
    #
    # print("Total de treinamento %d" % limite)
    # print("Total de teste %d" % (len(entradas) - limite))
    # print("Total de acertos %d" % acertos)
    # print("Porcentagem de acertos %2.f" % (100*acertos/(len(entradas)-limite)))

    knn = KNN(3)
    print(knn.classify([3,4,3,4,3,4,3],'backhand'))