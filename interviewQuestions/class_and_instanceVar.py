class Person:    # 类对象
    x = 5  # 类变量
    y = 6  # 类变量

    def __init__(self, x, y):
        self.x = x  # 实例变量
        self.y = y  # 实例变量
        print(x)
        print(y)

    def add(self):
        return self.x + self.y


# 实例对象
p1 = Person(1, 2)
p2 = Person(3, 4)
print(p2.add())
print(Person.add(p2))


