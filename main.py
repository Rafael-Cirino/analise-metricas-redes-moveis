arq = open("Data/bus_9.txt")
linhas = arq.readlines()

list_data = []
for linha in linhas:
    #linha = linha.replace("\t", "\t;")
    linha = linha.split("\t")
    if "\n" in linha:
        linha.remove("\n")
    list_data.append(linha)

print(list_data[0], list_data[1])
print(len(list_data[0]), len(list_data[1]))

#Montar dicionário
dict_data = {}

for i, col in enumerate(list_data[0]):
    list_aux = []
    for linha in list_data[1:]:
        if (len(linha)-1) > i:
            list_aux.append(linha[i])
            #print(i, len(linha))
    
    dict_data[col] = [list_aux]
    print(col)

print(dict_data["Timestamp"])
print(dict_data["NTech2"])

import csv

with open('Data/bus_9.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = '\t')

    for row in plots:
        print(row, len(row))

