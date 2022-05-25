from generate_json import dict_data_bus

def test_plot(data):
    import matplotlib.pyplot as plt

    int_speed = data_to_int(data["Speed"])

    plt.plot(data["t_norm"], int_speed)
    plt.show()

def data_to_int(list_data):
    list_return = []
    for value in list_data:
        if value:
            list_return.append(int(value))
        else:
            list_return.append(0)
    
    return list_return

if __name__ == '__main__':
    dict_data = dict_data_bus()

    print(dict_data["t_norm"])

    test_plot(dict_data)
