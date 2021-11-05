# ===========создаем функции==============
import time

# import names, randomtimestamp as rd


# def yolochka_1 (item_1,....):
#     print('--Hello yolocka_1')
#
#
# yolochka_1(10,.....)

# def yolochka_1(item_1, item_2):
#     result = item_1 + 100
#     result_2 = item_2 + 1000
#
#     print('--Hello yolocka_1')
#     print('item_1 = ', item_1)
#     print('result = ', result)


def yolochka_2(y_1):
    result = y_1 + 300


    print('--Hello yolocka_2')
    print('item_1 = ', y_1)
    print('result = ', result)


# yolochka_1(10, 20)

print('=============')

yolochka_2(5)

# for i in range(0, 10):      делаем счетчик от 0 до 10
#     yolochka_2(i)
#     time.sleep(.400)
#     print('***********')
#
#     yolochka_1(i, i*2)
#     time.sleep(.400)
#     print('==========')



# python generate names взять генерацию
# python generate dates взять генерацию

def yolochka_2(u_name, b_date):

    result = 'Hello' + u_name + 'you was born in' + str(b_date)

    print(result)


for i in range(0, 10):
    user_name = names.get_full_name()
    gen_date = rd.random_date()
