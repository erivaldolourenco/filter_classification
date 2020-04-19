import linecache
from tools import get_value


ct = 1 # constante de tempo
dt = 1  # varição de tempo
angle = [0, 0, 0]

class ComplementaryFilter(object):

    def __init__(self):
        self.alpha = ct / (ct + dt)
        # print(self.alpha)


    def complementary_f(self, acc, gyr):
        angle_x = (1 - self.alpha) * float(gyr[0]) * dt + (self.alpha) * (float(acc[0]))
        angle_y = (1 - self.alpha) * float(gyr[1]) * dt + (self.alpha) * (float(acc[1]))
        angle_z = (1 - self.alpha) * float(gyr[2]) * dt + (self.alpha) * (float(acc[2]))
        angle_new = []
        angle_new.append(angle_x)
        angle_new.append(angle_y)
        angle_new.append(angle_z)

        return angle_new


    def low_pass_f(self, acc_collect, acc_previous):
        # acc_new_x = (1 - self.alpha) * float(acc_collect[0]) + self.alpha * float(acc_previous[0])
        # acc_new_y = (1 - self.alpha) * float(acc_collect[1]) + self.alpha * float(acc_previous[1])
        # acc_new_z = (1 - self.alpha) * float(acc_collect[2]) + self.alpha * float(acc_previous[2])
        acc_new_x = (float(acc_collect[0]) + float(acc_previous[0]))/2
        acc_new_y = (float(acc_collect[0]) + float(acc_previous[0]))/2
        acc_new_z = (float(acc_collect[0]) + float(acc_previous[0]))/2
        acc_new = []
        acc_new.append(acc_new_x)
        acc_new.append(acc_new_y)
        acc_new.append(acc_new_z)

        return acc_new


    def high_pass_f(self, gyr_collect, gyr_previous, gyr_previous_filtred):
        gyr_new_x = (1 - self.alpha) * float(gyr_previous_filtred[0]) + (1 - self.alpha) * (float(gyr_collect[0]) - float(gyr_previous[0]))
        gyr_new_y = (1 - self.alpha) * float(gyr_previous_filtred[1]) + (1 - self.alpha) * (float(gyr_collect[1]) - float(gyr_previous[1]))
        gyr_new_z = (1 - self.alpha) * float(gyr_previous_filtred[2]) + (1 - self.alpha) * (float(gyr_collect[2]) - float(gyr_previous[2]))
        gyr_new = []
        gyr_new.append(gyr_new_x)
        gyr_new.append(gyr_new_y)
        gyr_new.append(gyr_new_z)

        return gyr_new

    def get_cfilter(self, file_name, filter_type=5):
        acc_previous = [0, 0, 0]
        gyr_previous = [0, 0, 0]
        gyr_previous_filtred = [0, 0, 0]
        angle_filter_list = []
        gyr_high_pass_list = []
        gyr_collect_list = []
        acc_low_pass_list = []
        acc_collect_list = []

        with open(file_name, 'r') as file:
            lines = file.readlines()

            for i in range(1, int(len(lines))):
                line = linecache.getline(file_name, i)

                if line[0] == 'A':
                    acc_collect = get_value(line)
                    acc_collect_list.append(acc_collect)
                    acc_new = self.low_pass_f(acc_collect, acc_previous)
                    acc_previous = acc_collect
                    acc_low_pass_list.append(acc_new)

                elif line[0] == 'G':
                    gyr_collect = get_value(line)
                    gyr_collect_list.append(gyr_collect)
                    gyr_new = self.high_pass_f(gyr_collect, gyr_previous, gyr_previous_filtred)
                    gyr_previous = gyr_collect
                    gyr_previous_filtred = gyr_new
                    gyr_high_pass_list.append(gyr_new)

        if len(gyr_high_pass_list) < len(acc_low_pass_list):
            value_limit = len(gyr_high_pass_list)
        else:
            value_limit = len(acc_low_pass_list)

        for i in range(value_limit):
            angle_new = self.complementary_f(acc_low_pass_list[i], gyr_high_pass_list[i])
            angle = angle_new
            angle_filter_list.append(angle_new)

        if filter_type == 1:
            return acc_low_pass_list
        elif filter_type == 2:
            return acc_collect_list
        elif filter_type == 3:
            return gyr_high_pass_list
        elif filter_type == 4:
            return gyr_collect_list
        else:
            return angle_filter_list