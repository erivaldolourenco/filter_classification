import matplotlib.pyplot as plt
import numpy as np
import linecache

linha = 0
ct = 1  # constante de tempo
dt = 1  # varição de tempo
angle = [0, 0, 0]


class ComplementaryFilter(object):

    def __init__(self):
        self.alpha = ct / (ct + dt)
        print(self.alpha)

    def complementary_f(self, acc, gyr):
        angle_x = (1 - self.alpha) * \
            (angle[0] + float(gyr[0]) * dt) + (self.alpha) * (float(acc[0]))
        angle_y = (1 - self.alpha) * \
            (angle[1] + float(gyr[1]) * dt) + (self.alpha) * (float(acc[1]))
        angle_z = (1 - self.alpha) * \
            (angle[2] + float(gyr[2]) * dt) + (self.alpha) * (float(acc[2]))
        angle_new = []
        angle_new.append(angle_x)
        angle_new.append(angle_y)
        angle_new.append(angle_z)

        return angle_new

    def low_pass_f(self, acc_collect, acc_previous):
        acc_new_x = (1 - self.alpha) * \
            float(acc_collect[0]) + self.alpha * float(acc_previous[0])
        acc_new_y = (1 - self.alpha) * \
            float(acc_collect[1]) + self.alpha * float(acc_previous[1])
        acc_new_z = (1 - self.alpha) * \
            float(acc_collect[2]) + self.alpha * float(acc_previous[2])
        acc_new = []
        acc_new.append(acc_new_x)
        acc_new.append(acc_new_y)
        acc_new.append(acc_new_z)
        return acc_new

    def high_pass_f(self, gyr_collect, gyr_previous, gyr_previous_filtred):
        gyr_new_x = (1 - self.alpha) * float(gyr_previous_filtred[0]) + (
            1 - self.alpha) * (float(gyr_collect[0]) - float(gyr_previous[0]))
        gyr_new_y = (1 - self.alpha) * float(gyr_previous_filtred[1]) + (
            1 - self.alpha) * (float(gyr_collect[1]) - float(gyr_previous[1]))
        gyr_new_z = (1 - self.alpha) * float(gyr_previous_filtred[2]) + (
            1 - self.alpha) * (float(gyr_collect[2]) - float(gyr_previous[2]))
        gyr_new = []
        gyr_new.append(gyr_new_x)
        gyr_new.append(gyr_new_y)
        gyr_new.append(gyr_new_z)
        return gyr_new

    def get_value(self, line):
        clean_line = "AG[]\n"
        for i in range(0, len(clean_line)):
            line = line.replace(clean_line[i], "")
        line = line.split(',')
        return line


def get_coordenada(values, n):
    v = []
    for value in values:
        v.append(float(value[n]))
    return v


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

    lista_coordenadas = list()
    fc = ComplementaryFilter()

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for i in range(1, int(len(lines))):

            line = linecache.getline(file_name, i)
            next_line = str(linecache.getline(file_name, i + 1))

            if line[0] == 'A':
                acc_collect = fc.get_value(line)
                acc_antigo.append(acc_collect)
                acc_new = fc.low_pass_f(acc_collect, acc_previous)
                acc_previous = acc_collect
                #angle_new = fc.complementary_f(acc_new,angle)
                #angle = angle_new
                acc_list.append(acc_new)

                #a = []
                #x = 0.70*angle_new[0]
                #y = 0.98*angle_new[1]
                #z = 0.98*angle_new[2]
                # a.append(x)
                # a.append(y)
                # a.append(z)

                # gyr_list.append(a)
                # print("COLLECT:"+str(acc_collect)+" PREVIOUS:"+str(acc_previous) + " LOW_PASS:"+ str(acc_new) )
                # print("=====================================================")
            elif line[0] == 'G':
                gyr_collect = fc.get_value(line)

                gyr_antigo.append(gyr_collect)

                gyr_new = fc.high_pass_f(
                    gyr_collect, gyr_previous, gyr_previous_filtred)
                gyr_previous = gyr_collect
                gyr_previous_filtred = gyr_new
                #angle_new = fc.complementary_f(angle, gyr_new)
                #angle = angle_new
                gyr_list.append(gyr_new)

                #a = []
                #x = 0.30*angle_new[0]
                #y = 0.02*angle_new[1]
                #z = 0.02*angle_new[2]
                # a.append(x)
                # a.append(y)
                # a.append(z)

                # acc_list.append(a)

                # print("=====================================================")
                # print("COLLECT:"+str(gyr_collect)+" HIGHPASS:"+str(gyr_new))
            # angle_list.append(angle_new)

    for i in range(len(gyr_list)):
        angle_new = fc.complementary_f(acc_list[i], gyr_list[i])
        angle = angle_new
        angle_list.append(angle_new)

    gyr_x_plot = get_coordenada(gyr_antigo, 0)
    acc_x_plot = get_coordenada(acc_antigo, 0)
    angle_x_plot = get_coordenada(angle_list, 0)

    print(angle_x_plot)

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(range(len(acc_x_plot)), acc_x_plot, label='Acelerômetro')
    ax.plot(range(len(gyr_x_plot)), gyr_x_plot, label='Giroscópio')
    ax.plot(range(len(angle_x_plot)), angle_x_plot,
            label='Filtro Complementar')
    ax.set_xlabel('dt')  # Add an x-label to the axes.
    ax.set_ylabel('Valores coletados')  # Add a y-label to the axes.
    # Add a title to the axes.
    ax.set_title("Acelerômetro X Giroscópio X Filtro Complementar ")
    ax.legend()
    plt.show()
