# условные операторы
#=========================================================
# age = int(input("Sag mir über dein Alt: "))
# if age > 18:
#     print("Willkommen")
# elif age == 18:
#     print("Du kannst hierkommen")
# else:
#     print("Du bist aber sehr Jung für dieses Gebäude")
#=========================================================
# num1 = int(input("Ведите первое число: "))
# num2 = int(input("Ведите второе число: "))
# math_operator = input("Выберите математическую операцию: + - * /")
# if math_operator == "+":
#     print(num1 + num2)
# elif math_operator == "-":
#     print(num1 - num2)
# elif math_operator == "*":
#     print(num1 * num2)
# elif math_operator == "/":
#     print(num1 / num2)
# else:
#     print("Вы выбрали некорректный математический оператор")
#========================================================== Fahrenheit#

gradus = int(input("Введите градус: "))
fahrenheit = input("По Фаренгейту?: ")

if fahrenheit.lower() == "Да".lower() or "ДА, СУКА!".lower():
    output_temperature = (gradus - 32)* 5 / 9
    if gradus > 0:
        print(f"Температура выше нуля по Цельсию и равна {output_temperature} по Фаренгейту")
    elif gradus < 0:
        print(f"Температура нижу нуля по Цельсию и равна {output_temperature} по Фаренгейту")
    else:
        print("Fuck you")
else:
    output_temperature = (gradus * 9 / 5) + 32
    if gradus > 0:
        print(f"Температура выше нуля по Фаренгейту и равна {output_temperature} по Цельсию")
    elif gradus < 0:
        print(f"Температура нижу нуля по Фаренгейту и равна {output_temperature} по Цельсию")
    else:
        print("Fuck you")
#========================================================== Високосный год#

# year = int(input("Введите год: "))
#
# if year % 4 == 0 and year % 100 != 0:
#     print(f"Год {year} - високосный")
# elif year % 400 == 0 and 100 == 0:
#     print(f"Год {year} - високосный")
# elif year % 100 == 0:
#     print(f"Год {year} - невисокосный")
# else:
#     print(f"Год {year} - невисокосный")
#========================================================== Високосный год - решение от ментора#

# year = int(input("Введите год: "))
#
# if (year % 4 == 0) and year % 400 == 0 and year % 100 == 0:
#     print("Yes")
# else:
#     print("No")
#========================================================== List - списки#

# some_list = [1, 2, 3, 4, 5, "Hallo", [1, 2, 3]]
# list1 = list()
# # # Methods
# list1.append("Hello")
# list1.append("hi")
# print(list1)
# list1[0] = "bootcamp"
# # print(len(list1))
# # print(dir(list1))
#
# list1.insert(1, "world")


# fruits = ["banana", "banana", "apple", "orange"]
# vegetables = ["potato", "cabbage", "tomato"]
# fruits.extend(vegetables)
# # print(fruits)
# # print(fruits.count("banana"))
# print(fruits.index("banana", 1))

# phone_numbers = ["996555090807", "996700765849"]
# black_list = phone_numbers.pop(1)
# print(phone_numbers)
# print(black_list)
#========================================================== Phone operators#

phone_numbers_list = ["555905651", "700657898", "777098767", "554909878", "777125409", "506897809", "702789878"]
megacom_list = []
beeline_list = []
o_list = []

for each_number in phone_numbers_list:
    if each_number.startswith("5"):
        megacom_list.append(each_number)
    elif each_number.startswith("77"):
        beeline_list.append(each_number)
    elif each_number.startswith("70"):
        o_list.append(each_number)
    else:
        pass
print(megacom_list)
print(beeline_list)
print(o_list)





