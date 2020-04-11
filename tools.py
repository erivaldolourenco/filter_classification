import os


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


if __name__ == '__main__':

	n_line = 0

	files = os.listdir('data/amador')
	for file in files:
		with open('data/amador/'+file, 'r') as f:
			
			n_line += sum(1 for line in f)
			print(str(file)+": "+str(n_line))

	media = n_line/len(files)

	print(media)