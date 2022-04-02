# Task 4.3
# shlom41k

"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
"""


my_dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}
my_dict2 = my_dict.copy()

print("Dictionary:\n", my_dict)


# 1) Use while
# Get all keys
keys = list(my_dict.keys())

i = 0   # Loops counter

while i < len(keys):
    my_dict[keys[i] + str(len(keys[i]))] = my_dict.pop(keys[i])
    i += 1


# 2) Use for
# Get all keys
keys2 = list(my_dict2.keys())

for k in keys2:
    my_dict2[k + str(len(k))] = my_dict2.pop(k)

print("Changed (using while):\n", my_dict)
print("Changed (using for):\n", my_dict2)