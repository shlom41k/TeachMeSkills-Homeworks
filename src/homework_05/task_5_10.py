# Task 5.10
# shlom41k

"""
Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
"""


from datetime import datetime, timedelta


trains = {
    "№ 367": {
        "From": "Брест",
        "T_start": datetime(2021, 11, 12, 8, 4),
        "To": "Москва",
        "T_finish": datetime(2021, 11, 13, 12, 15)
    },
    "№ 210": {
        "From": "Минск",
        "T_start": datetime(2021, 10, 22, 13, 10),
        "To": "Прага",
        "T_finish": datetime(2021, 10, 23, 0, 56)
    },
    "№ 666": {
        "From": "Адлер",
        "T_start": datetime(2021, 9, 1, 12, 5),
        "To": "Калининград",
        "T_finish": datetime(2021, 9, 11, 7, 14)
    },
    "№ 777": {
        "From": "Москва",
        "T_start": datetime(2021, 11, 1, 10, 10),
        "To": "Владивосток",
        "T_finish": datetime(2021, 11, 8, 15, 30)
    },
    "№ 284": {
        "From": "Минск",
        "T_start": datetime(2021, 11, 11, 10, 45),
        "To": "Гомель",
        "T_finish": datetime(2021, 11, 11, 13, 57)
    },
    "№ 111": {
        "From": "Минск",
        "T_start": datetime(2021, 10, 11, 10, 45),
        "To": "Заславль",
        "T_finish": datetime(2021, 10, 11, 11, 5)
    },
}

for key in trains.keys():
    travel_time = trains[key]["T_finish"] - trains[key]["T_start"]

    if travel_time > timedelta(hours=7, minutes=20):
        print(f"Поезд {key} {trains[key]['From']} - {trains[key]['To']} был в пути {travel_time}")