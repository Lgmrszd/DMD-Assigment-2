import random

__plate_formats = [(("L", 4), ("-",), ("d", 3)), (("L", 3), ("-",), ("d", 4))]
__colors = ["Red", "Green", "Blue", "Magenta", "Yellow", "Silver", "Gray", "White", "Black"]
__models = [("Toyota Prius", "Type 1"), ("Tesla Model S", "Tesla Supercharger"),
            ("Tesla Model 3", "Tesla Supercharger"), ("KAMAZ", "GOST 23784"), ("Waymo", "Type 2"), ("ICar", "Lighting"),
            ("Ford Japan", "CHAdeMO")]


def car_types():
    return __models


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
