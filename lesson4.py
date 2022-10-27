# lists_names = ["Nazgul", "Zamira", "Aliza"]
# i = len(lists_names) - 1
# while i < len(lists_names):
#     print(lists_names[i])
#     if i == 0:
#         break
#     i -= 1

# tuples

# tuples = ("Nazgul", [1, 2, 3], 6)
# tuples[1][0] = 0
# print(tuples)

# a = 8
# b = 10
# a, b = b, a
# print(a)
# print(b)

# tuples = ([1, 2, 3], 4, 5)
#
# lists, number, number2 = tuples
#
# print(id(lists))
# print(id(number))
# print(id(number2))
# print(id(tuples))

# tuples = (5, ["a"], "b", 8)
# (number1, *number, number2) = tuples
# print(number1)
# print(number)
# print(number2)

# from math import *
# print(sqrt(4))

# names = ("Nurlan", "Smanaly", "Aman", ["Nurlan"])
# # print(names[::2])
#
# print(names.count("Nurlan"))
# print(names.index("Nurlan"))

# Задача
# some_tuple = ((), (), ('',), ('a', 'b'), 4, 5, ('a', 'b', 'c'), ('d'))
# some_list = list(some_tuple)
#
# for i in range(0, len(some_list)):
#     if type(some_list[i]) == tuple:
#         if len(some_list[i]) == 0:
#             some_list.remove(some_list[i])
#
# print(len(some_list))
# Решение
# some_tuple = ((), (), ('',), ('a', 'b'), 4, 5, ('a', 'b', 'c'), ('d'))
# some_tuple = list(some_tuple)
# new_list = []
#
# for i in some_tuple:
#     if type(i) != tuple or len(i) != 0:
#         new_list.append(i)
# print(new_list)


# some_tuple = ((), (), ('',), ('a', 'b'), 4, 5, ('a', 'b', 'c'), ('d'))
# some_tuple = list(some_tuple)
# some_list = []
#
# for i in some_tuple:
#     if type(i) == tuple and len(i) == 0:
#         continue
#     some_list.append(i)
# print(some_list)

#Задача 2

# some_tuple = ((), ('a', 'b'), 'd', 5, (5, 8, ()))
# new_list =[]
#
# for i in some_tuple:
#     if type(i) != tuple:
#         continue
#     elif type(i) == tuple and len(i) % 2 != 0 or len(i) == 0:
#         continue
#     new_list.append(i)
#
# print(new_list)

# Решение:

some_tuple = ((), (), ('',), ('a', 'b'), 4, 5, ('a', 'b', 'c'), ('d', 'e', 'v', 'i', 'l', 'l'))
lists = []
for i in some_tuple:
    if type(i) == tuple and len(i) % 2 == 0 and len(i) != 0:
        lists.append(i)
lists = tuple(lists)
print(lists)









