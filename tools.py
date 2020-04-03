
def get_value(line):
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