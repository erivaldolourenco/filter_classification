
ct = 0.5  # constante de tempo
dt = 1  # varição de tempo
angle = [0, 0, 0]

class ComplementaryFilter(object):

    def __init__(self):
        self.alpha = ct / (ct + dt)
        print(self.alpha)

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
        acc_new_x = (1 - self.alpha) * float(acc_collect[0]) + self.alpha * float(acc_previous[0])
        acc_new_y = (1 - self.alpha) * float(acc_collect[1]) + self.alpha * float(acc_previous[1])
        acc_new_z = (1 - self.alpha) * float(acc_collect[2]) + self.alpha * float(acc_previous[2])
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

