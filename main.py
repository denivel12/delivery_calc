import csv


class Product:
    def __init__(self, price, weight=2, volume=0.2, category=1, package=2):
        self.price = price
        self.weight = weight
        self.category = category
        self.package = package
        self.volume = volume

class Carrier:
    def __init__(self, usd_rub, cny_rub):
        self.usd_rub = usd_rub
        self.cny_rub = cny_rub
        pass

with open('default_tariff.csv', ) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    dict_tariff = {rows[0]: float(rows[1]) for rows in reader}

print(dict_tariff["A1"])

default_carrier = Carrier(70, 10)

def get_values(product):
    density = round(product.volume/product.weight, 2)
    weight_coefficient = 0


tablets_lenovo = Product(1500, 2)

list_parameters_default = [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def print_info(sum_list):
    print("Покупка. Магазин -> склад Китай: ", sum_list[0] + sum_list[1])
    print("Обработка. Склад Китай", sum(sum_list[2:5]))
    print("Доставка. Склад Китай - Склад РФ", )


def calculate_delivery(product, quantity, dict, carrier):
    cny_rub = carrier.cny_rub
    usd_rub = carrier.usd_rub
    order_sum = product.price * quantity * cny_rub
    A1_cost, A2_cost, B1_cost, B2_cost, B3_cost, B4_cost, C1_cost, C2_cost, D1_cost, D2_cost, K1_cost, K2_cost = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if list_parameters_default[0] == "0":
        A1_cost = 0
    else:
        A1_cost = order_sum * dict["A1"]

    if list_parameters_default[1] == "0":
        A2_cost = 0
    else:
        A2_cost = 30 * cny_rub

    if list_parameters_default[2] == "0":
        B1_cost = 0
    else:
        B1_cost = dict["B1"] * usd_rub

    if list_parameters_default[3] == "0":
        B2_cost = 0
    else:
        B2_cost = dict["B2"] * usd_rub

    if list_parameters_default[4] == "0":
        B3_cost = 0
    else:
        B3_cost = dict["B3"] * usd_rub

    if list_parameters_default[5] == "0":
        B4_cost = 0
    else:
        B4_cost = dict["B4"] * usd_rub

    if list_parameters_default[6] == "0":
        C1_cost = 0
    else:
        C1_cost = dict["C1"] * product.weight * quantity * usd_rub

    if list_parameters_default[7] == "0":
        C2_cost = 0
    else:
        C2_cost = dict["C2"] * order_sum

    if list_parameters_default[8] == "0":
        D1_cost = 0
    else:
        D1_cost = dict["D1"]

    if list_parameters_default[9] == "0":
        D2_cost = 0
    else:
        D2_cost = dict["D2"]

    if list_parameters_default[10] == "0":
        K1_cost = 0
    else:
        K1_cost = dict["K1"]

    if list_parameters_default[11] == "0":
        K2_cost = 0
    else:
        K2_cost = dict["K2"]

    sum_list = [A1_cost, A2_cost, B1_cost, B2_cost, B3_cost, B4_cost, C1_cost, C2_cost, D1_cost, D2_cost, K1_cost, K2_cost]
    return sum_list, sum(sum_list)


print(calculate_delivery(tablets_lenovo, 10, dict_tariff, default_carrier))

