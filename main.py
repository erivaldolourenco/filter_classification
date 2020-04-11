import matplotlib.pyplot as plt
import numpy as np
import linecache

from tools import *
from cf.cf import ComplementaryFilter

if __name__ == '__main__':

    file_name = 'data/spin_amador_eri.data'

    acc_previous = [0, 0, 0]
    gyr_previous = [0, 0, 0]
    gyr_previous_filtred = [0, 0, 0]

    angle_list = []
    acc_list = []
    gyr_list = []

    acc_antigo = []
    gyr_antigo = []


    gyr_high_pass_list = []
    gyr_collect_list = []


    acc_low_pass_list = []
    acc_collect_list = []


    lista_coordenadas = list()
    fc = ComplementaryFilter()

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for i in range(1, int(len(lines))):

            line = linecache.getline(file_name, i)
            next_line = str(linecache.getline(file_name, i + 1))

            if line[0] == 'A':
                acc_collect = get_value(line)
                acc_collect_list.append(float(acc_collect[0]))
                acc_antigo.append(acc_collect)
                acc_new = fc.low_pass_f(acc_collect, acc_previous)
                acc_previous = acc_collect
                #angle_new = fc.complementary_f(acc_new,angle)
                #angle = angle_new
                acc_list.append(acc_new)
                acc_low_pass_list.append(float(acc_new[0]))

            elif line[0] == 'G':
                gyr_collect = get_value(line)
                gyr_collect_list.append(float(gyr_collect[0]))
                gyr_antigo.append(gyr_collect)

                gyr_new = fc.high_pass_f(yr_collect, gyr_previous, gyr_previous_filtred)
                gyr_previous = gyr_collect
                gyr_previous_filtred = gyr_new
                #angle_new = fc.complementary_f(angle, gyr_new)
                #angle = angle_new
                gyr_list.append(gyr_new)
                gyr_high_pass_list.append(float(gyr_new[0]))


    for i in range(len(gyr_list)):
        angle_new = fc.complementary_f(acc_list[i], gyr_list[i])
        angle = angle_new
        angle_list.append(angle_new)

    # print(gyr_collect_list)
    # print(gyr_high_pass_list)

    gyr_x_plot = get_coordenada(gyr_antigo, 0)
    acc_x_plot = get_coordenada(acc_antigo, 0)
    angle_x_plot = get_coordenada(angle_list, 0)

    # print(angle_x_plot)
    
    fig, ax = plt.subplots()

    # ax.plot(range(len(gyr_collect_list)), gyr_collect_list, label='Coletado')
    # ax.plot(range(len(gyr_high_pass_list)), gyr_high_pass_list, label='Passa Alta')
    # ax.set_xlabel('Variação de tempo')  
    # ax.set_ylabel('Valores coletados')  
    # ax.set_title("Filtro Passa-Alta")

    # ax.plot(range(len(acc_collect_list)), acc_collect_list, label='Coletado')
    # ax.plot(range(len(acc_low_pass_list)), acc_low_pass_list, label='Passa-Baixa')
    # ax.set_xlabel('Variação de tempo')  
    # ax.set_ylabel('Valores coletados')  
    # ax.set_title("Filtro Passa-Baixa")

    ax.plot(range(len(acc_x_plot)), acc_x_plot, label='Acelerômetro')
    ax.plot(range(len(gyr_x_plot)), gyr_x_plot, label='Giroscópio')
    ax.plot(range(len(angle_x_plot)), angle_x_plot,label='Filtro Complementar')
    ax.set_xlabel('Variação de tempo')  
    ax.set_ylabel('Valores coletados')  
    ax.set_title("Acelerômetro X Giroscópio X Filtro Complementar ")


    ax.legend()
    plt.show()
