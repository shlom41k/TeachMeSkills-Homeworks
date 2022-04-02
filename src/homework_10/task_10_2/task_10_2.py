# Task 10.2
# shlom41k

"""
Создать csv файл с данными о ежедневной погоде. Структура: Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду (скорость ветра и градусы) для Минска за последние 7 дней.

# Use https://openweathermap.org/ to get temperature history for cities
"""

import requests
import datetime
import csv


# my_fun for write 1 line into a CSV file
def write_list(filename, data, method='w', delimiter=','):
    with open(filename, method, newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerow(data)


# my_fun for read data from CSV file
def read_list(filename):
    with open(filename, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)


# my_fun for get data from OpenWeatherMap API
# and write in into a file
def get_weather(file):

    # Create API
    api_url = 'https://api.openweathermap.org/data/2.5/forecast'
    cities = ["Minsk", "Moscow", "London", "Paris", "Kyiv", "Oslo", "Surgut", "Noril'sk", "Beijing"]

    # Write weather to fie
    header = ["Date", "Place", "Temp", "Wind"]
    write_list(file, header, "w", delimiter=";")

    for city in cities:
        params = {
            'q': city,
            'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
            'units': 'metric',
            'cnt': '50'
        }

        # Get data
        res = requests.get(api_url, params=params)
        data = res.json()

        for i in data['list']:
            d_date = datetime.datetime.fromtimestamp(int(i['dt']))
            t = i['main']['temp']
            v = i['wind']['speed']

            write_list(file, [d_date, city, t, v], 'a', delimiter=";")

            print(f"{d_date}, {city}: t = {t} \N{DEGREE SIGN}C, "
                  f"wind speed = {v} m/s, weather - {i['weather'][0]['description']}")


if __name__ == "__main__":

    # file with weather data
    file = "weather.csv"

    """
    get weather data (need Network connection):
    use the function below for update weather data
    """
    get_weather(file)     # Comment/uncomment

    # Read data from file
    temp = read_list(file)

    tmp, speed, cnt = 0, 0, 0

    for line in temp[1:]:

        d, c, tm, vv = line[0].split(";")

        if c != "Minsk":
            continue

        if (datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S") < datetime.datetime.now() - datetime.timedelta(days=5)):
            continue

        tmp += float(tm)
        speed += float(vv)
        cnt += 1

    print(f"\nMean temperature in Minsk: {round(tmp / (cnt), 2) if cnt else 0}.")
    print(f"Mean wind speed in Minsk: {round(speed / (cnt), 2) if cnt else 0}.")
