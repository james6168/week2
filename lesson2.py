# number = 10
#
# if number == 10:
#     number = number / 2
#     if number == 5:
#         print(number /2)

# my_list = [1, 2, 3]
# my_list2 = list()
# print(bool(my_list))

# print(sum(my_list))

# if my_list:
#     result = sum(my_list)/len(my_list)
# print(round(result))
#
# print(round(2.6))

# my_list = [1, 8, 4]
# if 2 in my_list:
#     print("ksdakjd")

# print(dir(my_list))
# my_list.clear()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)
# my_list.sort()
# my_list.reverse()
# print(my_list)

# Задача

# input_palindrom_value = input("Введите слово: ")
# input_palindrom_value_list = list(input_palindrom_value)
# input_palindrom_value_list.reverse()
# if input_palindrom_value_list == list(input_palindrom_value):
#     print(f"Да это слово {input_palindrom_value} палиндром")
# else:
#     print(f"Fuck you")

# Решение менторов

# input_palindrom_value = input("Введите слово: ")
# if input_palindrom_value == input_palindrom_value[::-1]:
#     print("Palindrom")
# else:
#     print("Not palindrom")

# my_list1 = [1, 2, 5]
# my_list2 = list(my_list1)
# # my_list2 = my_list1.copy()
# my_list2.append(3)
#
# print(id(my_list1))
# print(id(my_list2))

# my_list1 = [1, 2, 5]
# my_list1.remove(8)
# my_list1.pop(3)
# print(my_list1)


# for

# lists = [1, 4,  2, "Syimyk", 2.3]

# list_of_digits = []
# list_of_alphas = []
#
# for i in "Ab35CD":
#     if i.isalpha():
#         list_of_alphas.append(i)
#     else:
#         list_of_digits.append(i)
#         print(f"Fuck you, digit {i}")
# print(list_of_digits)
# print(list_of_alphas)

# Задача 3

# list_of_numbers = [3, 8, 7, 20, 142, 45, 78, 97, 99, 24, 4, 8, 10, 6, 66, 616, 100, 45, 65]
# numbers = []
#
# for i in list_of_numbers:
#     if i % 3 == 0 and i % 2 == 0:
#         numbers.append(i)
#     else:
#         pass
#
# print(numbers)

# Range

# number = list(range(0, 100))
# print(number)

numbers_list = []

for i in range(1, 1000):
    if i % 2 == 0:
        numbers_list.append(i)
print(numbers_list)