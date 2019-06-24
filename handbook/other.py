y = 0


def add():
    global y
    y += 1
    print("add() = {0}".format(y))
    return y


for ite in iter(add, 5):
    print(ite)


# 定义类迭代器


class mytest:
    def __iter__(self):
        print('__iter__ is called!')
        self.result = [1, 2, 3]
        return iter(self.result)


print('*' * 20)
t = mytest()

for i in t:
    print(i, ',')


