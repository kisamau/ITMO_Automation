# программа проверяет является ли число положительным
#или отриц и выводит соответ сообщение

# num = 3
# num = -5
num = 0

if num >=0:
    print('число больше либо равно 0')
else:
    print('число отрицательное')


# str_2 содержит в себе str_1?


def task_yes_no(str_1,str_2):
    if str_1 in str_2:
        print('yes')
    else:
        print('no')
task_yes_no(str_1='test',str_2='test1')


num_float = 3.4
# num_float = 0
# num_float = -4.5
if num_float > 0:
    print('plus number')
elif num_float == 0:
    print('null')
else:
    print('minus number')


permit_print = True
num = 7
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')


def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('вы - бакалавр')
    elif year_of_study in range(5,7):
        print('вы - магистр')
    elif 7 <= year_of_study <= 9:
        print('вы - аспирант')
    else:
        print('введите корректный год обучения')
student_rank(6)


n = 7
if -100 > n > 100:
    print('-')
else:
    print('+')

