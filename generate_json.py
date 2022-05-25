import json
import os
from dotenv import load_dotenv

load_dotenv()

PATH_RAW = os.getenv("PATH_RAW")
PATH_JSON = os.getenv("PATH_JSON")

def dict_data_bus(name_json="data", raw="bus_9"):
    arq = open(PATH_RAW + raw + ".txt")
    linhas = arq.readlines()

    list_data = []
    len_cols = len(linhas[0])
    for linha in linhas:
        # Separa a linha em colunas
        linha = linha.split("\t")
        if "\n" in linha:
            linha.remove("\n")

        # Normaliza linha em relação as colunas
        for j in range(len(linha), len_cols):
            linha.append("")

        list_data.append(linha)

    # Montar dicionário
    dict_data = {}
    for i, col in enumerate(list_data[0]):
        list_aux = []
        for linha in list_data[1:]:
            list_aux.append(linha[i])

        dict_data[col] = [list_aux]

    # Salva os dados em um json
    with open(PATH_JSON + name_json + ".json", "w") as j_file:
        json.dump(dict_data, j_file)

if __name__ == "__main__":
    dict_data_bus()