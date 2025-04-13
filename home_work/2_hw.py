def task_1(a: int,b: float,c: str,d: list,e: bool):
    return type(a),type(b),type(c),type(d),type(e)
print(task_1(2, 45.1, 'sukuna',[5,6,7], 4>1))


def task_2(a=[1,2,3,5,8,13,21]) -> int:
    return a[0:3]
print(task_2())
# последовательность называется списком (если я правильно поняла)

def task_3(numero) -> int:
    return numero*numero
print(task_3(6))