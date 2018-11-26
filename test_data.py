import random

__plate_formats = [(("L", 4), ("-",), ("d", 3)), (("L", 3), ("-",), ("d", 4))]
__colors = ["Red", "Green", "Blue", "Magenta", "Yellow", "Silver", "Gray", "White", "Black"]
__models = [("Toyota Prius", "Type 1"), ("Tesla Model S", "Tesla Supercharger"),
            ("Tesla Model 3", "Tesla Supercharger"), ("KAMAZ", "GOST 23784"), ("Waymo", "Type 2"), ("ICar", "Lighting"),
            ("Ford Japan", "CHAdeMO")]
__parts_for = [("Tesla Supercharger Connector", "Tesla Model 3"), ("Tesla Supercharger Connector", "Tesla Model S"),
               ("ICar Engine", "ICar"),
               ("Lidar T1", "KAMAZ"), ("Lidar T1", "Toyota Prius"),
               ("Lidar T2", "Tesla Model S"), ("Lidar T2", "Tesla Model 3"), ("Lidar T2", "Ford Japan")]

__parts_providers = [(1, "Chicago", "IParts", "123456"), (2, "Petrovich Store", "Str. Pushkina", "+79801234567"),
                     (3, "Auto Parts Co.", "City 17", "+10000000")]
__can_provide = [(1, "ICar Engine"),
                 (2, "Lidar 1"), (2, "Lidar 2"),
                 (3, "Tesla Supercharger Connector"), (3, "Lidar 2")]


def car_types():
    return __models


def parts():
    return [(j,) for j in set([i[0] for i in __parts_for])]


def parts_for():
    return __parts_for


def parts_providers():
    return __parts_providers


def can_provide():
    return __can_provide

def random_car_plate_number():
    plate_format = random.choice(__plate_formats)
    plate_num = ""
    for seq in plate_format:
        if seq[0] == "L":
            seq_len = seq[1]
            plate_num += "".join(map(chr, random.choices(range(ord("A"), ord("Z")), k=seq_len)))
        elif seq[0] == "d":
            seq_len = seq[1]
            plate_num += "".join(map(str, random.choices(range(10), k=seq_len)))
        else:
            plate_num += seq[0]
    return plate_num


def random_car():
    plate_num = random_car_plate_number()
    color = random.choice(__colors)
    model = random.choice(__models)[0]
    return plate_num, color, model


def specific_cars():
    cars = []
    for _ in range(3):
        plate_num = random_car_plate_number()
        plate_num = "AN" + plate_num[2:]
        color = random.choice(__colors)
        model = random.choice(__models)[0]
        while color == "Red":
            color = random.choice(__colors)
        cars.append((plate_num, color, model))
    for _ in range(3):
        plate_num = random_car_plate_number()
        color = "Red"
        model = random.choice(__models)[0]
        while plate_num.startswith("AN"):
            plate_num = random_car_plate_number()
        cars.append((plate_num, color, model))
    for _ in range(2):
        plate_num = random_car_plate_number()
        plate_num = "AN" + plate_num[2:]
        color = "Red"
        model = random.choice(__models)[0]
        cars.append((plate_num, color, model))
    return cars


