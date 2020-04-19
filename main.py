from tools import *
from cf.cf import ComplementaryFilter
from knn.knn import KNN

if __name__ == '__main__':


    file_name = 'data/spin_amador_eri.data'

    cf = ComplementaryFilter()

    fc_list = cf.get_cfilter(file_name, 5)
    acc_antigo = cf.get_cfilter(file_name, 2)
    gyr_antigo = cf.get_cfilter(file_name, 4)
    gyr_high_pass = cf.get_cfilter(file_name, 3)

    print(len(fc_list))
    # print(type(fc_list[0][0]))

    '''
    KNN CLASSIFICADOR
    '''
    knn = KNN(3,(len(fc_list)-2))

    result = knn.classify(fc_list,'backhand')
    # print(result)
    # print(result.count(1))

    porcent = (result.count(1)*100)/knn.n_lines

    print("valor ="+str(porcent))

    '''
    PLOTAGEM DE GRAFICOS
    '''
    gyr_x_plot = get_coordenada(gyr_antigo, 0)
    acc_x_plot = get_coordenada(acc_antigo, 0)
    fc_x_list = get_coordenada(fc_list, 0)
    gyr_high_pass_plot = get_coordenada(gyr_high_pass, 0)


    plot_cf_graph(gyr_x_plot,acc_x_plot,fc_x_list)
    plot_high_pass_graph(gyr_x_plot,gyr_high_pass_plot)

    val_in_out = knn.get_in_out('backhand')
    plot_knn_graph(val_in_out)
