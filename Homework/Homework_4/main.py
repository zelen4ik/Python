# Python HW 4 Cycles
import time
# =========================Цилы While=====================
# Создать переменную count со значением 0
count = 0
# Создать переменную range_count со значением 10
range_count = 10
# Создать переменную for_count со значением 0
for_count = 0
# Создать переменную run  со значением True
run = True
# Сделать цикл while который будет работать пока run
    # Тело цикла:
# 	5.1 Выводить в консоль “Hello Cycle”
while run:
    print('Hello Cycle', count)
# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	6.1 Выводить в консоль (“Step =”, count)
# 	6.2 Переменной count прибавлять 1 с присвоением.
    count += 1
    time.sleep(.500)
    print('Step =', count)
# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	7.1 Выводить в консоль (“Step =”, count)
# 	7.2 Переменной count прибавлять 1 с присвоением.
    if count < range_count:
        print('Step =123', count)

# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	9.1 Выводить в консоль (“Step =”, count)
# 	9.2 Переменной count прибавлять 1 с присвоением.
# 	9.2 Сделать if с условием, если count равен range_count то цикл остановится.
# 	9.3 В теле if вывести в консоль (“STOP”, count)
    elif count <= range_count:
        print('Step 123=', count)
        break
    else:
        print('ELSE !!!!')
#
# Цилы For
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)
#
for item in range(for_count, range_count):
    item += 1
    time.sleep(.400)
    print('Step 456=', item)
#
#
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).
for item in range(0, 30):
    item += 1
    # time.sleep(.600)
    # print('Step 789=', item)
    if item == 5:
        print('Item =', item)
    elif item == 10:
        print('Item =', item)
    elif item <= 4:
        print('Item =', item)
    elif item >= 27:
        print('Item =', item)
#
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item равен  7.
# 	 - В теле if создать переменную inner_count равную 0
# 	 - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
# 	 - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
# 	Тело внутреннего цикла For:
# 		-- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
# 		-- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
# 	- За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)
for item in range(0, +1):
    item += 1
    time.sleep(.600)
    print('Step =', item)
    if item == 7:
        inner_count = 0
        print('-- inner_count =', inner_count)
    for inner_item in range(0, 7):
        print('-------- Inner_Step =', inner_item)




# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
# Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
# 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
# 	- В теле if вывести (‘If_item =’, item)
# 	- В теле if поставить continue
#
# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)
for item in range(0, 20):
    print('Step =', item)
    if item >= 7:
        print('If_item =', item)
    elif item <= 12:
        continue
print('End_iteration =', item)