from cProfile import label
from generate_json import dict_data_bus
import matplotlib.pyplot as plt
import numpy as np



COLOR = ["r", "y", "c", "g", "m", "b"]

def generate_color():
    import matplotlib.cm as cm 

    for i in np.arange(0, 1, 0.15):
        COLOR.append([cm.rainbow(i)])

def test_plot(data, name_save="plot2"):
    int_speed = data_to_int(data["Speed"])

    #plt.subplots()
    plt.plot(data["t_norm"], int_speed, label="Speed", c="k")
    #plot_points(data["t_norm"], int_speed, data["NCell1"])
    plot_points(data["t_norm"], int_speed, data["NetworkTech"])
    plt.legend(loc=1)
    plt.title("network x speed")
    plt.savefig("Data/charts/" + name_save + ".png")
    plt.show()

    plt.close()

def plot_points(x, y1, y2):
    list_info = []
    for i in range(len(x) - 1):
        value_name = y2[i]

        marker_size = 80
        if (value_name != ""):
            if value_name not in list_info:
                list_info.append(value_name)
                set_color = COLOR[len(list_info) - 1]
                plt.scatter(
                        x[i],
                        y1[i],
                        marker=".",
                        label=value_name,
                        s=marker_size,
                        c=set_color
                    )
            else:
                set_color = COLOR[list_info.index(value_name)]
                plt.scatter(
                        x[i],
                        y1[i],
                        marker=".",
                        s=marker_size,
                        c=set_color
                    )   

def data_to_int(list_data):
    list_return = []
    for value in list_data:
        if value:
            list_return.append(int(value))
        else:
            list_return.append(0)

    return list_return


if __name__ == "__main__":
    dict_data = dict_data_bus()

    generate_color()

    test_plot(dict_data)
