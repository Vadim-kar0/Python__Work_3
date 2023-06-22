#list,set,dct - изменяемые
# import time
#
# a = [i for i in range(15000000)]
# start = time.perf_counter()
# if 130000 in a:
#     print("нашел в списке")
# end = time.perf_counter()
# print(end-start)
#
# dct = {i:1 for i in range(15000000)}
# start = time.perf_counter()
# if 130000 in dct:
#     print("нашел в словаре")
# end = time.perf_counter()
# print(end-start)


# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6



# a = [1, 1, 2, 0, -1, 3, 4, 4, 4, 4]
# #print(len(set(a)))


# for i in a:
#     if a.count(i) > 1 :
#         for j in range(a.count(i)-1):
#             a.remove(i)
# print(len(a))
# print(a)

# my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]
# unique = []
# for i in my_list:
#     if i not in unique:
#         unique.append(i)
# print(my_list)
# print(len(unique))



# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# k = 2
# a = [1, 2, 3, 4, 5]
# memory = 0
# for _ in range(k):
#     memory = a[-1]   # a.insert(0,a.pop())
#     a.pop()
#     a.insert(0, memory)
# print(a)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 2
# new_list = []
# for i in my_list:
#     if i - k > 0:
#         new_list.append(i - k)
#     else:
#         new_list.append(i - k + len(my_list))
# print(new_list)

# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0,lst.pop())
# print(lst)

# lst = [1, 2, 3, 4, 5]
# a1 = lst[-k:]
# a2 = lst[:-k]
# print(a1+a2)

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

# a = set()

# for i in dic:a.add(str(*i.values()).strip())

# print(a)


# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# set_n = set()

# for dct in list_1:
#    set_n.add(str(*dct.values()).strip())
   
# print(set_n)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


#Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# list_1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1,len(list_1)):
#     if list_1[i]>list_1[i-1]:
#         count+=1
#
# print(count)













