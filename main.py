from tools import *
from config import *
from cf.cf import ComplementaryFilter
from knn.knn import KNN

if __name__ == '__main__':
    file_name = BASE_DIR+'/data/spin_amador_eri.data'
    print("################## INICIO ##################")
    print("==================== 1 ====================")
    cf = ComplementaryFilter()
    acc_antigo = cf.get_cfilter(file_name, 2)
    print("VALORES CAPTURADOS ACELEROMETRO:")
    print(acc_antigo)
    gyr_antigo = cf.get_cfilter(file_name, 4)
    print("VALORES CAPTURADOS GIROSCOPIO:")
    print(gyr_antigo)
    gyr_high_pass = cf.get_cfilter(file_name, 3)
    print("VALORES FILTRO PASSA_ALTA:")
    print(gyr_high_pass)
    acc_low_pass = cf.get_cfilter(file_name, 1)
    print("VALORES FILTRO PASSA-BAIXA:")
    print(acc_low_pass)
    fc_list = cf.get_cfilter(file_name, 5)
    print("VALORES FILTRO COMPLEMENTAR:")
    print(fc_list)
    print("===========================================")
    '''
    KNN CLASSIFICADOR
    '''
    print("==================== 2 ====================")
    knn = KNN(3, (len(fc_list) - 2))
    result = knn.classify(fc_list, 'backhand')
    print("CLASSIFICACAO DE CADA PONTO (1 = PROFISSIONAL, 0 = AMADOR):")
    print("QUANTIDADE DE LINHAS ANALIZADAS: "+str(len(result)))
    print(result)
    porcent = (result.count(1) * 100) / knn.n_lines
    print("PROFISSIONA: "+str(result.count(1))+" AMADOR: "+str(result.count(0))+" QUANTO DE PROFISSIONAL: "+str(porcent)+"%")
    print("===========================================")

    '''
    PLOTAGEM DE GRAFICOS
    '''
    gyr_x_plot = get_coordenada(gyr_antigo, 0)
    acc_x_plot = get_coordenada(acc_antigo, 0)
    fc_x_list = get_coordenada(fc_list, 0)
    gyr_high_pass_plot = get_coordenada(gyr_high_pass, 0)
    acc_low_pass_plot = get_coordenada(acc_low_pass, 0)

    plot_cf_graph(gyr_x_plot, acc_x_plot, fc_x_list)
    plot_high_pass_graph(gyr_x_plot, gyr_high_pass_plot)
    plot_low_pass_graph(acc_x_plot, acc_low_pass_plot)

    val_in_out = knn.get_in_out('backhand')
    plot_knn_graph(val_in_out)

    plt.show()