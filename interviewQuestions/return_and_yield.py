'''
    yield 生成器(generator)
'''

def func_1():
    for i in range(1, 5):
        return i


def func_2():
    for i in range(1, 5):
        yield i

print(func_1())
print(func_2())

yi = func_2()
for y in yi:
    print(y)
