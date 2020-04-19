import os
import matplotlib.pyplot as plt
# from knn.knn import KNN
from matplotlib.colors import ListedColormap

'''
Ler uma linha do arquivo de dados e retorna a linha já sem caracteres indesejados
ex: [1,3,4]
'''


def get_value(line):
    clean_line = "AG[]\n"
    for i in range(0, len(clean_line)):
        line = line.replace(clean_line[i], "")
    line = line.split(',')
    return line


'''
Entrada: Lista com itens de coordenadas ex: [[0,0,0],[1,2,3]]
Saida: Lista com todas as coordenada do index n
'''


def get_coordenada(values, n):
    v = []
    for value in values:
        v.append(float(value[n]))
    return v


def plot_cf_graph(gyr_x_plot, acc_x_plot, fc_x_list):

    fig, ax = plt.subplots()

    ax.plot(range(len(acc_x_plot)), acc_x_plot, label='Acelerômetro')
    ax.plot(range(len(gyr_x_plot)), gyr_x_plot, label='Giroscópio')
    ax.plot(range(len(fc_x_list)), fc_x_list, label='Filtro Complementar')
    ax.set_xlabel('Variação de tempo')
    ax.set_ylabel('Valores coletados')
    ax.set_title("Acelerômetro X Giroscópio X Filtro Complementar ")
    ax.legend()
    plt.figure(1)
    # plt.show()
    return True


def plot_high_pass_graph(gyr_x_plot, low_pass_plot):
    fig, ax = plt.subplots()
    ax.plot(range(len(gyr_x_plot)), gyr_x_plot, label='Giroscópio')
    ax.plot(range(len(low_pass_plot)), low_pass_plot, label='Filtro Passa-Alta')
    ax.set_xlabel('Variação de tempo')
    ax.set_ylabel('Valores coletados')
    ax.set_title("Giroscópio X Filtro Passa Alta ")
    ax.legend()
    plt.figure(2)
    # plt.show()
    return True

def plot_low_pass_graph(acc_x_plot, high_pass_plot):
    fig, ax = plt.subplots()
    ax.plot(range(len(acc_x_plot)), acc_x_plot, label='Acelerômetro')
    ax.plot(range(len(high_pass_plot)), high_pass_plot, label='Filtro Passa-Baixa')
    ax.set_xlabel('Variação de tempo')
    ax.set_ylabel('Valores coletados')
    ax.set_title("Acelerômetro X Filtro Passa-Baixa ")
    ax.legend()
    plt.figure(3)
    # plt.show()
    return True


def plot_knn_graph(values):

    out = values[1][1]
    x = get_coordenada(values[0][1], 0)
    y = get_coordenada(values[0][1], 1)

    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    fig, ax = plt.subplots()
    color =["prof","amad"]
    scatter = ax.scatter(x, y, c=out, s=200, cmap=cm_bright, edgecolors='k', alpha=0.3 ,label='Teste')
    ax.set_title("Distribuição Profissional X Amador")
    ax.legend()
    legenda = ax.legend(*scatter.legend_elements(),
                        loc="upper left", title="Classe")
    ax.add_artist(legenda)
    # ax.set_xticks(())
    # ax.set_yticks(())
    # plt.tight_layout()
    # ax.grid(True)
    plt.figure(4)


    return True


if __name__ == '__main__':

    n_line = 0
    value = 20000

    files = os.listdir('data/amateur/backhand')
    for file in files:
        with open('data/amateur/backhand/' + file, 'r') as f:

            n_line = sum(1 for line in f)
            if value > n_line:
                value = n_line
            print(str(file) + ": " + str(n_line))

    # media = n_line/len(files)

    print(value)
