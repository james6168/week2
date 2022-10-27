

# number_factorial = int(input("Введите число, которое нужно возвратить в факториал: "))
# counter = 1
# for i in range(1, number_factorial + 1):
#     counter *= i
#
# print(counter)

# counter = 0
# for i in range(21):
#     counter += i
# print(counter)

# for i in range(1, 10):
#     if i  % 2 == 0:
#         continue
#     print(i)

# for i in range(1, 10):
#     if i == 2:
#         break
# else:
#     print("end")

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
# else:
#     print("end")

# list_divided_on_3 = []
#
# for i in range(1, 100):
#     if i % 3 != 0:
#         continue
#
#     list_divided_on_3.append(i)
# else:
#     print(list_divided_on_3)

# while

# i = 0
#
# while i <= 100:
#     if i % 2 == 0 and i != 0:
#         print(i)
#     i += 1

# i = 0
#
# while i <= 100:
#     if i == 50:
#         break
#     print(i)
#     i += 1
#
# while True:
#     print("Fuck you")

# while True:
#     number1 = int(input("Введите первый аргумент: "))
#     number2 = int(input("Введите второй аргумент: "))
#     operation = input("Выберите операцию: +, -, *, / ")
#
#     if operation == "+":
#         print(number1 + number2)
#     elif operation == "-":
#         print(number1 - number2)
#     elif operation == "*":
#         print(number1 * number2)
#     elif operation == "/":
#         print(number1 / number2)
#
#     input_interrupt_or_continue = input("Хочется дальше?: Да, Нет? ")
#
#     if input_interrupt_or_continue.lower() == "Да".lower():
#         pass
#     elif input_interrupt_or_continue.lower() == "Нет".lower():
#         print("Пока, включи меня потом, если буду нужен.")
#         break

#Задача 1

# list_of_correct_credentials = ["Chyngyz", "616"]
#
# count_of_attempts = 0
# while True:
#     input_username_of_user = input("Введите логин: ")
#     input_password_of_user = input("Введите пароль: ")
#     if input_username_of_user == list_of_correct_credentials[0] and input_password_of_user == list_of_correct_credentials[1]:
#         print("Вы вошли в систему")
#         break
#     elif count_of_attempts == 2:
#         print("Вы забанены за большое кол-во попыток")
#         list_of_correct_credentials.clear()
#         break
#     else:
#         print("Повторите попытку")
#         count_of_attempts += 1

# Задача 2:

# res = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1]

# res = [1]
# counter = 0

# Первый вариант решения:
# while True:
#     for i in range (0, counter):
#         res.append(0)
#     res.append(1)
#     counter += 1
#     if counter > 10:
#         break
# print(res)

# Второй вариант решения без двойного цикла:
# while True:
#     if counter <= 10:
#         res.extend([0 for x in range(counter)])
#         res.append(1)
#     elif counter > 10:
#         break
#     counter += 1
# print(res)
# Вариант решения от ментора:

res = [1]
for i in range(11):
    res = res + i * [0] + [1]
print(res)








