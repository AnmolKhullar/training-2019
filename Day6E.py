def add_five(x):
    temp = x + 5
    return temp


num = [11, 22, 33, 44, 55]
result = list(map(add_five, num))
print(num)
print(result)
