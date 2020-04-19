import os
from builtins import len
from sklearn.neighbors import KNeighborsClassifier
from cf.cf import ComplementaryFilter


class KNN(object):
    """Classe que resposvel pelas operações do KNN"""

    def __init__(self, k, n_lines):
        self.k = k
        self.n_lines = n_lines

    def get_in_out(self, move_name):

        inputs = {}
        outputs = {}

        for i in range(self.n_lines):
            inputs[i] = []
            outputs[i] = []

        cf = ComplementaryFilter()
        categories = ['amateur', 'professional']

        for category in categories:
            files = os.listdir('data/' + str(category) + '/' + str(move_name))

            for file in files:
                filter_list = cf.get_cfilter('data/' + str(category) + '/' + str(move_name) + '/' + str(file))

                for i in range(self.n_lines):
                    inputs[i].append(filter_list[i])

                    if category == 'amateur':
                        outputs[i].append(0)

                    elif category == 'professional':
                        outputs[i].append(1)

        return [inputs, outputs]

    """
    value: uma lista de cordenadas filtradas
    move_name: nome da jogada de tenis (backhand, spin)
    """

    def classify(self, value, move_name):
        class_list = []
        inputs = self.get_in_out(move_name)[0]
        outputs = self.get_in_out(move_name)[1]

        for i in range(self.n_lines):
            knn = KNeighborsClassifier(n_neighbors=self.k, p=1)
            knn.fit(inputs[i], outputs[i])
            class_list.append(knn.predict([value[i]])[0])

        return class_list


if __name__ == '__main__':
    entradas = [[3, 2, 1], [3, 3, 1], [2, 4, 3], [2, 1, 4], [8, 9, 3], [6, 8, 3], [7, 4, 2], [6, 7, 8], [4, 2, 3],
                [9, 6, 8]]
    saidas = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    p = 0.6
    limite = int(p * len(entradas))
    knn = KNeighborsClassifier(n_neighbors=3, p=2)
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
    print("Porcentagem de acertos %2.f" % (100 * acertos / (len(entradas) - limite)))
