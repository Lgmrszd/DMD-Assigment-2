import random

__plate_formats = [(("L", 4), ("-",), ("d", 3)), (("L", 3), ("-",), ("d", 4))]
__colors = ["Red", "Green", "Blue", "Magenta", "Yellow", "Silver", "Gray", "White", "Black"]
__models = [("Toyota Prius", "Type 1"), ("Tesla Model S", "Tesla Supercharger"),
            ("Tesla Model 3", "Tesla Supercharger"), ("KAMAZ", "GOST 23784"), ("Waymo", "Type 2"), ("ICar", "Lighting"),
            ("Ford Japan", "CHAdeMO")]
__parts_for = [("Tesla Supercharger Connector", "Tesla Model 3"), ("Tesla Supercharger Connector", "Tesla Model S"),
               ("ICar Engine", "ICar"), ("Lidar T1", "KAMAZ"), ("Lidar T1", "Toyota Prius"),
               ("Lidar T2", "Tesla Model S"), ("Lidar T2", "Tesla Model 3"), ("Lidar T2", "Ford Japan")]


def car_types():
    return __models


def parts():
    return [(j,) for j in set([i[0] for i in __parts_for])]


def parts_for():
    return __parts_for


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
