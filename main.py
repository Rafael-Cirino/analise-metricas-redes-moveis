from generate_json import dict_data_bus
from function_plot import plot_data



if __name__ == "__main__":
    dict_data = dict_data_bus()

    #plot_data(dict_data, "t_norm", "Speed", points="NetworkTech", y2="Level")
    plot_data(dict_data, "t_norm", "Level", points="NetworkTech")

    # https://pythonguides.com/python-plot-multiple-lines/ Para criar com duas linhass
