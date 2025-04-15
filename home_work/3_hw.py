def mark_func(q = 4, w = 127):
    return max(q,w)
print(mark_func())

def condition_func(a,b):
    if a - b == 135:
        print('yes')
    else:
        print('no')
condition_func(201,66)


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


def mark_2_func(x,y,z):
    if x > 10 and y > 10 and z > 10:
        print('yes')
    else:
        print('no')
mark_2_func(9,15,13)


def amorfeus_func(kremnos = [8,-100,19,0,-2]):
    positive_numb = 0
    for num in kremnos:
        if num > 0:
            positive_numb +=1
    print(positive_numb)


# задание под номером 7 так и не удалось решить
# хочется понять, как будет правильно
def calculate_days(months,years):
    d_in_months = months * 29
    d_in_years = years * 348
    d_total = d_in_months + d_in_years
    return d_total
days = calculate_days(8,2)
print(days)