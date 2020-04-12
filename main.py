import matplotlib.pyplot as plt
import numpy as np

from tools import *
from cf.cf import ComplementaryFilter

if __name__ == '__main__':

    file_name = 'data/spin_amador_eri.data'

    cf = ComplementaryFilter()

    fc_list = cf.get_cfilter(file_name, 5)
    acc_antigo = cf.get_cfilter(file_name, 2)
    gyr_antigo = cf.get_cfilter(file_name, 4)

    


    '''
    PLOTAGEM DE GRAFICOS
    '''
    gyr_x_plot = get_coordenada(gyr_antigo, 0)
    acc_x_plot = get_coordenada(acc_antigo, 0)
    fc_x_list = get_coordenada(fc_list, 0)
    
    fig, ax = plt.subplots()

    ax.plot(range(len(acc_x_plot)), acc_x_plot, label='Acelerômetro')
    ax.plot(range(len(gyr_x_plot)), gyr_x_plot, label='Giroscópio')
    ax.plot(range(len(fc_x_list)), fc_x_list,label='Filtro Complementar')
    ax.set_xlabel('Variação de tempo')  
    ax.set_ylabel('Valores coletados')  
    ax.set_title("Acelerômetro X Giroscópio X Filtro Complementar ")

    ax.legend()
    plt.show()
