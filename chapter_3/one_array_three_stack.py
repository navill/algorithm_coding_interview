"""
스택에 값을 push 또는 pop 할 때 마다 stack 내 최소값을 구하는 알고리즘
li.append(6)  # [6] 6
li.append(3)  # [3,6] 3
li.append(2)  # [2,3,6] 2
li.append(5)  # [5,2,3,6] 2
li.pop()  # [2,3,6] 2
li.pop()  # [3,6] 3
li.pop()  # [6] 6

"""

min_li = list()  # 최소값이 저장될 stack


def min_push(li, value):
    if li:
        min_li.append(min(value, min_li[-1]))
    else:
        min_li.append(value)
    li.append(value)
    return min_li[-1]


def min_pop(li):
    if li:
        min_li.pop()
        if min_li:
            return li.pop(), min_li[-1]
        else:
            return li.pop(), None
    return None, None


l = list()
print(l, min_push(l, 5))
print(l, min_push(l, 2))
print(l, min_push(l, 3))
print(l, min_push(l, 4))
print(min_pop(l))
print(min_pop(l))
print(min_pop(l))
print(min_pop(l))
print(l, min_push(l, 4))
print(l, min_push(l, 2))
print(min_pop(l))
print(min_pop(l))
print(min_pop(l))
