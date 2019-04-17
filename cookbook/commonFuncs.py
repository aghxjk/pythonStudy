##############################################
# zip()函数创建的是一个只能访问一次的迭代器
##############################################

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

res = a.keys() & b.keys()
res1 = a.items() & b.items()
print(res)
print(res1)
