# a: int = 5
# b: str = 'stroka'
# c: list = [1,2]
# def indent(s: str, width: int) -> str:
#     return " " * (max(0,width - len(s))) + s
# print(indent('1289', 45))

# def st_length(s: str = '') -> int:
#     return len(s)
# def min_list(a: list, b: list) -> int:
#     return max(len(a),len(b))

def append_list(l: list):
    l.append('test')
    return l
print(append_list([1,'two',3]))

def sum_list(a: list) -> int:
    result = 0
    for elem in a:
        result = result +elem
    return result
print(sum_list([1,2,3]))
