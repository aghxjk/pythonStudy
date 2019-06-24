# encoding: utf-8
__author__ = 'zhaoyimeng'

'''
    1. Python对象拥有三个特性: 身份、类型、值
       a) 身份
              每一个对象都有一个唯一的身份标识自己，任何对象的身份可以使用内建函数id()来得到。

       b) 类型
              对象的类型决定了该对象可以保存什么类型的值，可以进行什么样的操作，以及遵循什么样的规则。
              可以用内建函数type()查看Python 对象的类型。因为在Python中类型也是对象,所以type()返回的是对象而不是简单的字符串。

       c) 值
          对象表示的数据项，除了值之外，其它两个特性都是只读的。
'''

###############################
# 第1个例子
###############################
print('>>>>>>>> 第一个Class示例:')


class FirstClass:

    def setData(self, value):
        self.data = value

    def display(self):
        print(self.__class__, self.data)


x = FirstClass()
y = FirstClass()

x.setData('xxxx')
y.setData('yyyy')

x.display()
y.display()

##########################
# 第2个例子 :  inherit and override
###############################
print('\n')
print('>>>>>>>> 第二个Class示例(继承+重载):')


class SecondClass(FirstClass):
    def display(self):  # 覆盖FirstClass的display方法
        print(self.__class__, self.data)


z = SecondClass()
z.setData('zzz')  # 没有构造函数的时候,必须显示调用设置对象的data
z.display()

###############################
# 第3个例子 :
# 1.构造函数
# 2.运算符重载
###############################
print('\n')
print('>>>>>>>> 第三个Class示例(构造函数 + 运算符重载):')


class ThirdClass(SecondClass):
    def __init__(self, value='null'):
        self.data = value

    def __add__(self, other):  # 对于+运算符, Python把+左侧的实例对象传递给__add__中的self, 把+右侧的值传递给other
        return ThirdClass(self.data + other)

    def __str__(self):  # 对于print, Python把要打印的对象传递给__str__中的self
        return '[ThirdClass: {0}]'.format(self.data)

    def __mul__(self, other):
        self.data *= other


k = ThirdClass('abc')
k.display()
print(k)  # 打印一个对象时,会调用类内的自定义方法__str__()

kk = k + 'xyz'  # + 运算符重载,当两个对象相加时会调用__add__()方法
kk.display()

k * 3  # * 运算符重载,当对象示例调用 * 运算符时,会调用__mul__()方法
print(k)

###############################
# 世界上最简单的Python类
###############################
print('\n')
print('>>>>>>>> 第四个Class示例(The Simplest Class):')


class Simple: pass


Simple.name = 'Bob'  # 类对象的属性可以不用实例化就能够使用
Simple.age = 40

print('name: {0}, \nage: {1}'.format(Simple.name, Simple.age))

s1 = Simple()  # 实例对象s1
s2 = Simple()
print('(Simple.name, s1.name, s2.name) => ({0}, {1}, {2})'.format(Simple.name, s1.name, s2.name))
s1.name = 'Tom'
print("执行实例对象赋值操作: s1.name = 'Tom'")
print('(Simple.name, s1.name, s2.name) => ({0}, {1}, {2})'.format(Simple.name, s1.name, s2.name))

print('\n')
print('>>>>>>>> 命名空间初探: ')
print('命名空间初探: ', s1.__dict__.keys(), ' : ', s1.__class__)  # s1实例对象空间有自己的Name
print('命名空间初探: ', s2.__dict__.keys(), ' : ', s2.__class__)  # s2依然没有是空的, s2实例对象空间是没有name的
print('命名空间初探: ', s2.__class__.__dict__.keys())  # Simple类对象空间有name和age

# 一个空类创建了一个命名空间，可以用来代替字典
print('\n')
print('>>>>>>>> 可以用空类代替字典来创建命名空间:')
person = {}
person['name'] = 'Apple'
person['age'] = 50
person['sex'] = 'Man'

print('dict: ', person['name'], person.__class__)


class ClassSpace: pass


ClassSpace.name = 'Apple'
ClassSpace.age = 50
ClassSpace.sex = 'male'
print('class:', ClassSpace.name)
