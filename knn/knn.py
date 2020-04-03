import math


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