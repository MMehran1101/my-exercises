def sum_numbers(*num):
    if num == 0:
        return 0
    res = 0
    for i in num:
        res += i
    return res


def pick_evens(*args):
    l = []
    if args == 0:
        return l
    for i in args:
        if i % 2 == 0:
            l.append(i)
    return l


print(sum_numbers(1,2,3))
print(pick_evens(1,2,3,4,5))
