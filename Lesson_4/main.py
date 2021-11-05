# циклы в питоне
import time


# count = 0  с 0 начнет
# while True:
#
#     print(count, '~ Hello')
#     time.sleep(.500) делаем как быстро время отражения
#     count += 1 делаем шаг

# count = 0
# while count < 10:
#     print(count, '~ Hello')
#     time.sleep(.500)
#     count += 1

# for i in range(1, 10):
#     print(i)
#     time.sleep(.500)
# arr = [1,2,3,4,5]

# for i in arr:
#
#
#     print('Hello', i)
#     time.sleep(.300)

# for i in arr:
#     multiply_i = i * 10
#
#     print('Hello', multiply_i)
#     time.sleep(.300)
# count = 0
# arr = [1,2,3,4,5]
# for i in arr:
    # dev_i = i % 10
    # if dev_i == 0:
    #     print('i = ', i, 'dev_i =', dev_i)

    # print('i = ', i)
    # if i == 3:
    #     break   прекращает работу

# count = 0
# arr = [1, 2, 3, 4, 5]
# for i in arr:
#     print('i = ', i)
#     if i = 4
#         continue
#
#     print('Hello', i*10)
#     print('========')
#
#     time.sleep(.300)

# count = 0
#
# while True:
#     name = input("Enter your name: ")
#     print('Hello,', name, count)
#     count += 1

curr = 'USD'
curr_rate = 26.46

while True:
    usd_input = input("Enter your USD: ")
    usd_ukr = int(usd_input) * curr_rate

    print('Your enter USD: "', usd_input)
    print('Your UAH,', usd_ukr)


# usd_input = input("Enter your USD: ")
#     usd_ukr = float(usd_input) * curr_rate  FLOAT
#
#     print('Your enter USD: "', usd_input)
#     print('Your UAH,', usd_ukr)