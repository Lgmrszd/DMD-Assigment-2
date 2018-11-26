import random
import datetime

__ch_count = 12
__plate_formats = [(("L", 4), ("-",), ("d", 3)), (("L", 3), ("-",), ("d", 4))]
__locations = ["shops", "west square", "east square", "north square", "tavern", "medical center"]
__colors = ["Red", "Green", "Blue", "Magenta", "Yellow", "Silver", "Gray", "White", "Black"]
__models = [("Toyota Prius", "Type 1"), ("Tesla Model S", "Tesla Supercharger"),
            ("Tesla Model 3", "Tesla Supercharger"), ("KAMAZ", "GOST 23784"), ("Waymo", "Type 2"), ("ICar", "Lighting"),
            ("Ford Japan", "CHAdeMO")]
__plug_types = ["Type 1", "Type 2", "Tesla Supercharger", "GOST 23784", "CHAdeMO", "Lighting"]
__parts_for = [("Tesla Supercharger Connector", "Tesla Model 3"), ("Tesla Supercharger Connector", "Tesla Model S"),
               ("ICar Engine", "ICar"),
               ("Lidar T1", "KAMAZ"), ("Lidar T1", "Toyota Prius"),
               ("Lidar T2", "Tesla Model S"), ("Lidar T2", "Tesla Model 3"), ("Lidar T2", "Ford Japan")]

__parts_providers = [(1, "Chicago", "IParts", "123456"), (2, "Str. Pushkina", "Petrovich Store", "+79801234567"),
                     (3, "City 17", "Auto Parts Co.", "+10000000")]
__can_provide = [(1, "ICar Engine"),
                 (2, "Lidar 1"), (2, "Lidar 2"),
                 (3, "Tesla Supercharger Connector"), (3, "Lidar 2")]
__workshops = [(1, "GPS[WS_1])", "Never available"), (2, "GPS[WS_2])", "Sometimes available"),
               (3, "GPS[WS_3])", "Always available")]

__available_parts = [("Tesla Supercharger Connector", 1), ("Tesla Supercharger Connector", 3),
                    ("Lidar T1", 1), ("Lidar T1", 2), ("Lidar T1", 3),
                    ("Lidar T2", 2), ("Lidar T2", 3)]

__customers = [('xX_CoolName_Xx', 'CoolMail@cool-email.com', '+79805551122',
                'Vasya Pupkin', 'Russia', 'Moscow', '123131'),
               ('Petr_Dude', 'Petrov123@yandex.ru', '+79042744315',
                'Petr Vasilyev', 'Russia', 'Kazan', '948173'),
               ('m.petrova_1989', 'm.petrova_1970@inbox.ru', '+79021849184',
                'Maria Petrova', 'Russia', 'Kaliningrad', '948173'),
               ('n.prutko_1983', 'n.prutko_1983@yandex.ru', '+79028201834',
                'Nadezhda Prutko', 'Russia', 'Samara', '861243'),
               ('a.smirnow_1994', 'a.smirnow_1994@gmail.com', '+79048591295',
                'Aleksey Smirnov', 'Russia', 'Kaliningrad', '948173'),
               ('l.petrova_1958', ';.petrova_1958@inbox.ru', '+79051738245',
                'Lena Petrova', 'Russia', 'Novokuznetsk', '858914'),
               ('f.petrov_1996', 'f.petrov_1996@inbox.ru', '+79409281853',
                'Fedor Petrov', 'Russia', 'Omsk', '819472')]
__cities = ["Kazan", "Moscow", "Kaliningrad", "Skolkovo", "Omsk", "Petrozavodsk", "Novokuznetsk", "Uzhgorod",
            "Novokuznetsk", "Oktyabrskiy", "Belebey", "Samara"]


def car_types():
    return __models


def charging_stations():
    stations_list = []
    for i in range(1, __ch_count+1):
        station = (i, "GPS[{}]".format(random.choice(__cities)),
                   random.randint(10, 20)/10 + 1,
                   random.randint(1, 5))
        stations_list.append(station)
    return stations_list


def sockets():
    sockets_list = []
    for uid in range(1, __ch_count+1):
        for plug in __plug_types:
            socket = (uid, plug, random.randint(1, 10))
            sockets_list.append(socket)
    return sockets_list


def repairs():
    today = datetime.datetime.today()
    repairs_list = []
    for i in range(5):
        wid = random.randint(1, 3)
        car_id = random.randint(1, 18)
        date_time = today - datetime.timedelta(days=random.randint(1, 10),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59))
        repair = (wid, car_id, date_time.strftime("%Y-%m-%d %H:%M"), "Done", (2+random.randint(1, 4))*10000)
        repairs_list.append(repair)
    return repairs_list


def orders_payments(cars_tuples):
    today = datetime.datetime.today()
    orders_list = []
    payments_list = []

    for i in range(5):
        username = random.choice(__customers)[0]
        car_id = cars_tuples[random.randint(1, 18) - 1][0]
        date_time = today - datetime.timedelta(days=random.randint(1, 10),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59))
        _from = random.choice(__locations)
        _to = random.choice(__locations)
        while _from == _to:
            _to = random.choice(__locations)
        price = 100*random.randint(1, 7)
        tr2c = random.randint(500, 2000)
        duration = "{:02}:{:02}".format(random.randint(0, 1), random.randint(0, 59))

        order = (username, car_id, date_time.strftime("%Y-%m-%d %H:%M"), _from, _to, "Done", price, tr2c, duration)
        orders_list.append(order)

        p_dt = date_time + datetime.timedelta(minutes=random.randint(0, 10))
        payment = (username, car_id, date_time.strftime("%Y-%m-%d %H:%M"), p_dt.strftime("%Y-%m-%d %H:%M"), price)
        payments_list.append(payment)

    false_order = list(orders_list[-1])
    false_payment = list(payments_list[-1])
    false_order[6] = 25000
    false_payment[4] = 500000
    orders_list[-1] = tuple(false_order)
    payments_list[-1] = tuple(false_payment)

    for i in range(5):
        username = random.choice(__customers)[0]
        car_id = cars_tuples[random.randint(1, 18) - 1][0]
        date_time = today - datetime.timedelta(weeks=15,
                                               days=random.randint(1, 10),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59))
        _from = random.choice(__locations)
        _to = random.choice(__locations)
        while _from == _to:
            _to = random.choice(__locations)
        price = 100*random.randint(1, 7)
        tr2c = random.randint(500, 2000)
        duration = "{:02}:{:02}".format(random.randint(0, 1), random.randint(0, 59))

        order = (username, car_id, date_time.strftime("%Y-%m-%d %H:%M"), _from, _to, "Done", price, tr2c, duration)
        orders_list.append(order)

        p_dt = date_time + datetime.timedelta(minutes=random.randint(0, 10))
        payment = (username, car_id, date_time.strftime("%Y-%m-%d %H:%M"), p_dt.strftime("%Y-%m-%d %H:%M"), price)
        payments_list.append(payment)

    return orders_list, payments_list


def charges(cars_tuples):
    today = datetime.datetime.today()
    charges_list = []
    for i in range(10):
        uid = random.randint(1, __ch_count)
        car_id = cars_tuples[random.randint(1, 18) - 1][0]
        date_time = today - datetime.timedelta(days=random.randint(1, 10),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59))
        charging_time = "{:02}:{:02}".format(random.randint(0, 1), random.randint(0, 59))
        cost = 100*random.randint(1, 5)
        charge = (uid, car_id, date_time, "Done", charging_time, cost)
        charges_list.append(charge)

    # greedy car
    car_id = cars_tuples[random.randint(1, 18) - 1][0]
    for i in range(5):
        uid = random.randint(1, __ch_count)
        date_time = today - datetime.timedelta(days=random.randint(1, 4),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59))
        charging_time = "{:02}:{:02}".format(random.randint(0, 1), random.randint(0, 59))
        cost = 100*random.randint(1, 5)
        charge = (uid, car_id, date_time, "Done", charging_time, cost)
        charges_list.append(charge)

    return charges_list


def parts():
    return [(j,) for j in set([i[0] for i in __parts_for])]


def parts_for():
    return __parts_for


def parts_providers():
    return __parts_providers


def can_provide():
    return __can_provide


def workshops():
    return __workshops


def customers():
    return __customers


def available_parts():
    return __available_parts


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
    cars_list = []
    for _ in range(3):
        plate_num = random_car_plate_number()
        plate_num = "AN" + plate_num[2:]
        color = random.choice(__colors)
        model = random.choice(__models)[0]
        while color == "Red":
            color = random.choice(__colors)
        cars_list.append((plate_num, color, model))
    for _ in range(3):
        plate_num = random_car_plate_number()
        color = "Red"
        model = random.choice(__models)[0]
        while plate_num.startswith("AN"):
            plate_num = random_car_plate_number()
        cars_list.append((plate_num, color, model))
    for _ in range(2):
        plate_num = random_car_plate_number()
        plate_num = "AN" + plate_num[2:]
        color = "Red"
        model = random.choice(__models)[0]
        cars_list.append((plate_num, color, model))
    return cars_list


def cars():
    cars_list = [random_car() for _ in range(10)]
    cars_list.extend(specific_cars())
    return cars_list
