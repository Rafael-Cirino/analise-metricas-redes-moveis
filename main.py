from numpy import NaN

import os
from dotenv import load_dotenv

load_dotenv()

PATH_RAW = os.getenv("PATH_RAW")
PATH_JSON = os.getenv("PATH_JSON")

arq = open(PATH_RAW + "bus_9.txt")
linhas = arq.readlines()

list_data = []
len_cols = len(linhas[0])
for linha in linhas:
    # linha = linha.replace("\t", "\t;")
    linha = linha.split("\t")
    if "\n" in linha:
        linha.remove("\n")

    for j in range(len(linha), len_cols):
        linha.append("")

    list_data.append(linha)

# print(list_data[0], list_data[1])
print(len(list_data[0]), len(list_data[1]))

# Montar dicionário
dict_data = {}

for i, col in enumerate(list_data[0]):
    list_aux = []
    for linha in list_data[1:]:
        # if (len(linha)-1) > i:
        list_aux.append(linha[i])
        # print(i, len(linha))

    dict_data[col] = [list_aux]

print(dict_data["Timestamp"])
print(dict_data["NTech2"])

import json

with open(PATH_JSON + "data.json", "w") as j_file:
    json.dump(dict_data, j_file)
