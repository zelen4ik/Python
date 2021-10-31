import math
# a = 5
# b = 2
#
# c = 5**2
#
# print(True * False)
# print(int(False))

# d = as

a = True
b = False

# c = a / b
#
# print(c)


#               === присвоение ===
# x = 10
# y = 12
# z = x == y        равно
# z = x != y        не равно
# z = x > y
# z = x < y
# z = x <= y
# z = x >= y
# print('z_result is:', z)

age = 35
weight = 73
salary = 1000
# result = age == 35 and weight == 73
# print('Result', result) =====TRUE
#                   ====== Сравнение ======
# result = age == 32 and weight == 73
# print('Result', result) =====False age is not 32 expected 35

# result = age == 35 or weight == 73 or salary == 1000  ===TRUE
# result = age == 35 or (weight == 73 and salary == 10)  ===TRUE все что дальше идет он считает TRUE для всех
# result = age == 35 or weight == 73 and salary == 1000 === FALSE
# result = age == 34 and weight == 73 or salary == 1000  ===TRUE
# print('Result', result)
#                     ===== конвертация =====
not_result = not age == 35
print('Not Result', not_result)

not_result1 = not age == 34
print('Not Result1', not_result1)

not_result2 = not age == 34 and weight == 73
print('Not Result2', not_result2)

not_result3 = not age == 30 or not weight == 100
print('Not Result3', not_result3)

not_result4 = not age == 30 or (not weight == 100 and salary == 1000)
print('Not Result4', not_result4)

#         ======= if , else, elif ========

a = True
b = False

if a:
    print('True --', True)
else:
    print('ELSE !!!!')

# if age == 32:
#     print('True --', True)
# else:
#     print('ELSE !!!!')
#
# if age == 34:
#     print('True --', True)
# elif weight == 75:
#     print('weight == 75 ---', True)
# else:
#     print('ELSE !!!!')

# if salary ==1000:
#     print('salary == 1000 --', True)
#
if age == 34:
    print('True --', True)
elif weight == 75:
    print('weight == 75 ---', True)
elif weight >= 75:
    print('weight == 75 ---', True)
    if salary == 1000:
        print('salary == 1000 --', True)

else:
    print('ELSE !!!!')
