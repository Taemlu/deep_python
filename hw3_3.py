# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак,
# передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
import random

a = {"Спальник": 55,
     "Вода": 40,
     "Фонарик": 10,
     "Хлоргексидин": 20,
     "Сменка": 60,
     "Хлеб": 20,
     "Термос": 45,
     }

max_weight = 200
counter = 0
List_artibute = []
while counter < max_weight:
    key, value = random.choice(list(a.items()))
    if key in List_artibute:
        continue
    if counter + value > max_weight:
        break
    counter += value
    List_artibute += (str(key), str(value))

print(List_artibute, "=", counter)