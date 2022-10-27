# a = [[1, 3],
#      [2, 9]]
#
# for i in a:
#     for j in i:
#         print(i, j)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}", end="\t")
#     print()

# str_n = "Nazgul"
# print(str_n)

# a = [[3, 2, 1],
#      [2, 3, 4],
#      [0, 2, 5]]


next_index = 0
# for i in a:
#     for j in i:
#         if i.index(j) == next_index:
#             print(j * 2, end="\t")
#     next_index += 1
#     print()

# Решение

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i].index(a[i][j]) == next_index:
#             a[i][j] *=2
#     next_index += 1
# print(a)

# Решение от ментора:

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i == j:
#             a[i][j] *= 2
#     print(a[i])

# Задача 2

# [0, 2, 2]
# [1, 0, 2]
# [1, 1, 0]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i != j and i < j:
#             a[i][j] = 2
#         elif i != j and i > j:
#             a[i][j] = 1
#         elif i == j:
#             a[i][j] = 0
#     print(a[i])

# Задача 3
# some_string = "Бишкек"
# for i in "Бишкек":
#     some_string[] = "-"
# while True:
#     input_character = input("Введите букву: ")
#
#     for symbol in "бишкек":
#         if input_character in "бишкек":
#             i

# s = "weo aslkd aslfkj aslfk safaf"
# list_of_words = s.split()
#
# string_again = "".join(list_of_words)
# print(string_again)


import random
cities = ['Moscow', 'Bishkek', 'New York', 'Los Angeles', 'Muenchen', 'Koeln', 'Copenhagen', 'Seattle']
some_city = list(random.choice(cities).lower())
list_of_word = []
for each_char in some_city:
    list_of_word.append("-")
attempts_count = len(some_city)

print(f"Привет дружочек, добро пожаловать в игру отгадай город! \nПравила тут очень просты: \nЗагаданы следующие города: {cities} \nТебе нужно будет вводить буквы латинского алфавита в нижнем регистре и постепенно отгадывать определённый городок посимвольно. У тебя {len(some_city)} попыток. Смотри не истрать всё. \nУдачки!")

while True:

    if attempts_count == 0:
        print("К сожалению вы проиграли, ибо не осталось у вас попыток.")
        input_again = input("Ну что? Ещё разок? \nДа/Нет: ")
        if input_again.lower() == "нет":
            print("Приходите опять. \nИгра окончена.")
            break
        elif input_again.lower() == "да":
            attempts_count = len(list_of_word)
            continue
        else:
            attempts_count = 0
            print("Пожайлуста ответье либо да либо нет!")
            continue

    input_symbol = input("Введите символ по латинскому алфавиту: ")

    if input_symbol.lower() in some_city:
        if some_city.count(input_symbol) > 1:
            
        list_of_word[some_city.index(input_symbol)] = input_symbol
        print(f"Угадали! {list_of_word} \nОсталось попыток: {attempts_count}")

    else:
        attempts_count -= 1
        print(f"Не попали, увы, {list_of_word} \nОсталось попыток: {attempts_count}")







