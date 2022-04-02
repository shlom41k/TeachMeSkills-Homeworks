# Task 7.1
# shlom41k


# f1
def in_to_cm(l):
    return l * 2.54


# f2
def cm_to_in(l):
    return l / 2.54


# f3
def mi_to_km(l):
    return l * 1.609344


# f4
def km_to_mi(l):
    return l / 1.609344


# f5
def ft_to_kg(m):
    return m * 0.4535923745


# f6
def kg_to_ft(m):
    return m / 0.4535923745


# f7
def unc_to_gr(m):
    return m * 28.349523125


# f8
def gr_to_unc(m):
    return m / 28.349523125


# f9
def ga_to_l(v):
    return v * 4.546


# f10
def l_to_ga(v):
    return v / 4.546


# f11
def pt_to_l(v):
    return v * 0.568


# f12
def l_to_pt(v):
    return v / 0.568


ans = {
    "1": lambda: print(f"{n} [дюйм] = {in_to_cm(n)} [см]"),
    "2": lambda: print(f"{n} [см] = {cm_to_in(n)} [дюйм]"),
    "3": lambda: print(f"{n} [миля] = {mi_to_km(n)} [км]"),
    "4": lambda: print(f"{n} [км] = {km_to_mi(n)} [миля]"),
    "5": lambda: print(f"{n} [фунт] = {ft_to_kg(n)} [кг]"),
    "6": lambda: print(f"{n} [кг] = {kg_to_ft(n)} [фунт]"),
    "7": lambda: print(f"{n} [унц] = {unc_to_gr(n)} [гр]"),
    "8": lambda: print(f"{n} [гр] = {gr_to_unc(n)} [унц]"),
    "9": lambda: print(f"{n} [гал] = {ga_to_l(n)} [л]"),
    "10": lambda: print(f"{n} [л] = {l_to_ga(n)} [гал]"),
    "11": lambda: print(f"{n} [пт] = {pt_to_l(n)} [л]"),
    "12": lambda: print(f"{n} [л] = {l_to_pt(n)} [пт]"),
    "err_op": lambda: print("Неизвестная операция"),
}


if __name__ == "__main__":

    print("Программа конвертации единиц измерения запущена.")

    while True:
        print("\nВыребите желаемую операцию перевода: "
              "\n[1] Дюймы --> сантиметры"
              "\n[2] Сантиметры --> дюймы"
              "\n[3] Мили --> километры"
              "\n[4] Километры --> мили"
              "\n[5] Фунты --> килограммы"
              "\n[6] Килограммы --> фунты"
              "\n[7] Унции --> граммы"
              "\n[8] Граммы --> унции"
              "\n[9] Галлоны --> литры"
              "\n[10] Литры --> галлоны"
              "\n[11] Пинты --> литры"
              "\n[12] Литры --> пинты"
              "\n[0] Выход")

        act = input("Хочу перевести: ")

        if act == "0":
            print("\nВыход из программы.")
            break

        n = int(input("Введите значение конвертируемой величины: "))

        ans.get(act, ans["err_op"])()
