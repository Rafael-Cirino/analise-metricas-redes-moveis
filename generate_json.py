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
    len_cols = len(linhas[0].split("\t")) - 1
    for linha in linhas:
        # Separa a linha em colunas
        linha = linha.split("\t")
        if "\n" in linha:
            linha.remove("\n")

        # Converter as str para float
        for i, x in enumerate(linha):
            if x.replace(".", "", 1).replace("-", "", 1).isdigit():
                    linha[i] = float(x)

        # Normaliza linha em relação as colunas
        for j in range(len(linha), len_cols):
            linha.append("")

        list_data.append(linha)

    # Montar dicionário
    dict_data = {}
    dict_data["keys"] = list_data[0]
    for i, col in enumerate(list_data[0]):
        list_aux = []
        for linha in list_data[1:]:
            list_aux.append(linha[i])

        dict_data[col] = list_aux

    list_aux = []
    t0 = time_to_sec(dict_data[dict_data["keys"][0]][0])
    for t in dict_data[dict_data["keys"][0]]:
        list_aux.append(time_to_sec(t) - t0)

    dict_data["t_norm"] = list_aux

    # Salva os dados em um json
    with open(PATH_JSON + name_json + ".json", "w") as j_file:
        json.dump(dict_data, j_file)

    return dict_data


def time_to_sec(list_timestamp):
    list_time = list_timestamp.split("_")[1].split(".")

    time_sec = int(list_time[0]) * 3600
    time_sec += int(list_time[1]) * 60
    time_sec += int(list_time[2])

    return time_sec


if __name__ == "__main__":
    dict_data_bus()