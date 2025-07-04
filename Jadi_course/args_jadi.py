# Project 1
def sum_numbers(*num):
    if num == 0:
        return 0
    res = 0
    for i in num:
        res += i
    return res

# Project 2
def pick_evens(*args):
    l = []
    if args == 0:
        return l
    for i in args:
        if i % 2 == 0:
            l.append(i)
    return l

# Project 3
def skyline(*args):
    return 0 if not args else max(args)


print(skyline())
print(sum_numbers(1, 2, 3))
print(pick_evens(1, 2, 3, 4, 5))
