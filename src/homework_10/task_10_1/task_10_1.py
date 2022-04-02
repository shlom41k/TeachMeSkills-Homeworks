# Task 10.1
# shlom41k

"""
Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+
"""

import csv


# my_fun for writing dicts to CSV
def write_dict(filename, data, method='w', delimiter=','):
    with open(filename, method, newline='') as csv_file:
        # Create header
        header = [key for key in data[0].keys()]

        # Create writer
        writer = csv.DictWriter(csv_file, fieldnames=header, delimiter=delimiter)

        # Write header
        writer.writeheader()

        # Write data
        writer.writerows(data)
    print("Data wrote to file successfully")


# my_fun for reading dicts from CSV
def read_dict(filename):
    with open(filename, "r", newline="") as readfile:
        reader = csv.DictReader(readfile)
        print("Data from file load successfully\n")
        return list(reader)


if __name__ == "__main__":

    # Create some data structure
    k_name, k_sec_name, k_age = ["first_name", "second_name", "age"]

    peoples = [
        {k_name: "Sam", k_sec_name: "Gamji", k_age: "34"},
        {k_name: "Ann", k_sec_name: "Toper", k_age: "22"},
        {k_name: "Ted", k_sec_name: "Groud", k_age: "6"},
        {k_name: "Ann", k_sec_name: "Toper", k_age: "24"},
        {k_name: "Ron", k_sec_name: "Uizli", k_age: "16"},
        {k_name: "Menerva", k_sec_name: "Makgonagoll", k_age: "75"},
        {k_name: "Harry", k_sec_name: "Potter", k_age: "27"},
        {k_name: "Peter", k_sec_name: "Parker", k_age: "23"},
        {k_name: "John", k_sec_name: "Trever", k_age: "41"},
        {k_name: "Uill", k_sec_name: "Smitt", k_age: "55"},
        {k_name: "Uane", k_sec_name: "Rooney", k_age: "46"},
        {k_name: "Tim", k_sec_name: "Koks", k_age: "17"}
    ]

    # Write data into a file
    write_dict('peoples.csv', peoples, method='w', delimiter=',')

    # Create statistic structure
    stat_keys = ["age 1...12", "age 13...18", "age 19...25", "age 26...40", "age 40+"]
    stat = {key: 0 for key in stat_keys}

    # Read data from  file
    pipl = read_dict('peoples.csv')

    # Calculate some statistic
    for p in pipl:
        if 1 <= int(p[k_age]) <= 12:
            stat[stat_keys[0]] = stat.get(stat_keys[0], 0) + 1
        elif 13 < int(p[k_age]) <= 18:
            stat[stat_keys[1]] = stat.get(stat_keys[1], 0) + 1
        elif 19 < int(p[k_age]) <= 25:
            stat[stat_keys[2]] = stat.get(stat_keys[2], 0) + 1
        elif 16 < int(p[k_age]) <= 40:
            stat[stat_keys[3]] = stat.get(stat_keys[3], 0) + 1
        else:
            stat[stat_keys[4]] = stat.get(stat_keys[4], 0) + 1

    [print(f"In group '{key}' now {value} people") for key, value in stat.items()]

    # Write statistic to file
    write_dict('statistic.csv', [stat], method='w', delimiter=';')
