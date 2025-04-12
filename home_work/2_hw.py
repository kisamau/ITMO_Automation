def task_1(a,b,c,d,e) -> str:
    return str(a,b,c,d,e)
a = 3
b = 4.12
c = 'mind'
d = [1,2,3]
e = 2>1
print(type(a),type(b),type(c),type(d),type(e))


def task_2(a=[1,2,3,5,8,13,21]) -> int:
    return a[0:3]
print(task_2())
# последовательность называется списком (если я правильно поняла)

def task_3(numero) -> int:
    return numero*numero
print(task_3(6))