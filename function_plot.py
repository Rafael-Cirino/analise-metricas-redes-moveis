import matplotlib.pyplot as plt
import numpy as np

COLOR = ["r", "y", "c", "g", "m", "b"]


def generate_color():
    import matplotlib.cm as cm

    for i in np.arange(0, 1, 0.15):
        COLOR.append([cm.rainbow(i)])


def plot_data(data, x, y1, points=False, y2=False, title_text="", name_save=False):
    generate_color()

    fig, ax = plt.subplots()

    if not (y2):
        plt.plot(data[x], data[y1], label=y1, c="k")
        if points:
            plot_points(data[x], data[y1], data[points], plt)
        
        plt.xlabel(x, color="k", fontsize=12)
        plt.ylabel(y1, color="k", fontsize=12)

        plt.legend(loc=1)
    elif y2:
        fig, ax = plt.subplots()

        ax.plot(data[x], data[y1], c="k")
        ax.set_ylabel(y1, color="k", fontsize=12)
        ax.set_xlabel(x, color="k", fontsize=12)

        ax2 = ax.twinx()
        ax2.plot(data[x], data[y2], c="b")
        ax2.set_ylabel(y2, color="b", fontsize=12)

        if points:
            plot_points(data[x], data[y1], data[points], ax)

        ax.legend(loc=1)
    
    if not (title_text):
        title_text = f"{x} x {(y1 + ' x ' + y2) if y2 else y1}"
    plt.title(title_text)

    if not (name_save):
        name_save = f"{x} x {(y1 + ' x ' + y2) if y2 else y1}"

    plt.figure(figsize=(8, 6))
    plt.savefig("Data/charts/" + name_save + ".png")

    plt.show()
    plt.close()


def test_plot(data, name_save="plot2"):
    # int_speed = data_to_int(data["Speed"])
    # int_down = data_to_int(data["Level"])

    # Speed
    # plt.subplots()
    # plt.plot(data["t_norm"], int_speed, label="Speed", c="k")
    # plot_points(data["t_norm"], int_speed, data["NCell1"])
    # plot_points(data["t_norm"], int_speed, data["NetworkTech"])

    plt.plot(data["t_norm"], data["Speed"], label="Download", c="k")
    plot_points(data["t_norm"], data["Speed"], data["NetworkTech"])

    plt.legend(loc=1)
    plt.title("network x speed")
    plt.savefig("Data/charts/" + name_save + ".png")
    plt.show()

    plt.close()


def plot_points(x, y1, y2, obj_plt):
    list_info = []
    for i in range(len(x) - 1):
        value_name = y2[i]

        marker_size = 80
        if value_name != "":
            if value_name not in list_info:
                list_info.append(value_name)
                set_color = COLOR[len(list_info) - 1]
                obj_plt.scatter(
                    x[i],
                    y1[i],
                    marker=".",
                    label=value_name,
                    s=marker_size,
                    c=set_color,
                )
            else:
                set_color = COLOR[list_info.index(value_name)]
                obj_plt.scatter(x[i], y1[i], marker=".", s=marker_size, c=set_color)


def data_to_int(list_data):
    list_return = []
    for value in list_data:
        if value:
            list_return.append(int(value))
        else:
            list_return.append(0)

    return list_return