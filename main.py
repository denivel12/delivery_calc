import csv


class Product:
    def __init__(self, price, weight=1, volume=0.01, category=1, package=2):
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


tablets_lenovo = Product(1500)
gpus_msi = Product(3500, 3)

list_parameters_default = [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def print_info(sum_list, info_list):
    print(f"Общая сумма: {info_list[0]} x {info_list[1]}¥ = {info_list[-1]}₽")
    print(f"Общий вес: {info_list[0]*info_list[2]} | Общий объем: {info_list[0]*(info_list[-2]/info_list[2])}")
    print(f"Вес|Объем|Плотность: {info_list[2]}кг|{info_list[-2]}м3|{info_list[2]/info_list[-2]}кг/м3")
    print("1. Покупка. Магазин -> склад Китай: ", sum_list[0] + sum_list[1])
    print("1.1 Выкуп посредником: ", sum_list[0])
    print("1.2 Доставка до склада: ", sum_list[1], "\n")

    print("2. Обработка. Склад Китай", sum(sum_list[2:6]))
    print("2.1 Упаковка", sum_list[2])
    print("2.2 Консолидация", sum_list[3])
    print("2.3 Фото", sum_list[4])
    print("2.4 Проверка", sum_list[5], "\n")

    print("3. Доставка. Склад Китай - Склад РФ", sum(sum_list[6:8]))
    print("3.1 Доставка", sum_list[6])
    print("3.2 Страховка", sum_list[7], "\n")

    print("4. Обработка. Склад РФ", sum(sum_list[8:10]))
    print("4.1 Разгрузка", sum_list[8])
    print("4.2 Хранение", sum_list[9], "\n")

    print("5. Доставка. Склад РФ - Покупатель", sum_list[10:12])
    print("5.1 Доставка в другой город через ТК", sum_list[10])
    print("5.2 Курьерская доставка", sum_list[11], "\n")





def calculate_delivery(product, quantity, dict, carrier, show_info=False):
    cny_rub = carrier.cny_rub
    usd_rub = carrier.usd_rub
    order_sum = product.price * quantity * cny_rub
    A1_cost, A2_cost, B1_cost, B2_cost, B3_cost, B4_cost, C1_cost, C2_cost, D1_cost, D2_cost, K1_cost, K2_cost = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if list_parameters_default[0] == 0:
        A1_cost = 0
    else:
        A1_cost = order_sum * dict["A1"]

    if list_parameters_default[1] == 0:
        A2_cost = 0
    else:
        A2_cost = 30 * cny_rub

    if list_parameters_default[2] == 0:
        B1_cost = 0
    else:
        B1_cost = dict["B1"] * usd_rub

    if list_parameters_default[3] == 0:
        B2_cost = 0
    else:
        B2_cost = dict["B2"] * usd_rub

    if list_parameters_default[4] == 0:
        B3_cost = 0
    else:
        B3_cost = dict["B3"] * usd_rub

    if list_parameters_default[5] == 0:
        B4_cost = 0
    else:
        B4_cost = dict["B4"] * usd_rub

    if list_parameters_default[6] == 0:
        C1_cost = 0
    else:
        C1_cost = dict["C1"] * product.weight * quantity * usd_rub

    if list_parameters_default[7] == 0:
        C2_cost = 0
    else:
        C2_cost = dict["C2"] * order_sum

    if list_parameters_default[8] == 0:
        D1_cost = 0
    else:
        D1_cost = dict["D1"]

    if list_parameters_default[9] == 0:
        D2_cost = 0
    else:
        D2_cost = dict["D2"]

    if list_parameters_default[10] == 0:
        K1_cost = 0
    else:
        K1_cost = dict["K1"]

    if list_parameters_default[11] == 0:
        K2_cost = 0
    else:
        K2_cost = dict["K2"]

    order_info_list = [quantity, product.price, product.weight, product.volume, order_sum]

    sum_list = [A1_cost, A2_cost, B1_cost, B2_cost, B3_cost, B4_cost, C1_cost, C2_cost, D1_cost, D2_cost, K1_cost, K2_cost]

    print_info(sum_list, order_info_list)

    return sum_list, sum(sum_list)



print(calculate_delivery(gpus_msi, 10, dict_tariff, default_carrier, show_info=True))

