q = 19
w = 3
print(max(q,w))

a = 257
b = 122
if a - b == 135:
    print('yes')
else:
    print('no')


def task_month(my_month):
    if my_month == 12 or my_month == 1 or my_month == 2:
        print('winter')
    elif my_month in range(3,6):
        print('spring')
    elif my_month in range(6,9):
        print('summer')
    elif my_month in range(9,12):
        print('autumn')
    else:
        print('')
task_month(6)


x = 9
y = 15
z = 13
if x > 10 and y > 10 and z > 10:
    print('yes')
else:
    print('no')


kremnos = [8,-100,19,0,-2]
positive_numb = 0
for num in kremnos:
    if num > 0:
        positive_numb +=1
print(positive_numb)


# задание под номером 7 так и не удалось решить
# хочется понять, как будет правильно