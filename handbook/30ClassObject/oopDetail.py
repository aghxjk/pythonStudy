# encoding: utf-8
__author__ = 'zhaoyimeng'

###############################
# class语句
# 1.与其它面向对象语言不同,class像def一样,是对象的创建者并隐含着一个赋值运算
# 2.执行时，class会产生类对象并将其引用值存储给变量
# 3.像def一样,class语句也是真正的可执行语句
###############################

# 一般形式
print('一般形式(构造函数&继承):')


class First:
    def __init__(self, val=10):
        self.fVal = val

    def display(self):
        print('fVal = {0}'.format(self.fVal))


class Second:
    def __init__(self, val=20):
        self.sVal = val

    def display(self):
        print('sVal = {0}'.format(self.sVal))


class Third(First, Second):  # 多重继承
    def __init__(self, v1=100, v2=200):
        First.__init__(self, v1)  # 调用超类构造函数
        Second.__init__(self, v2)

    def display(self):  # 方法
        print('fVal = {0}, sVal = {1}'.format(self.fVal, self.sVal))


for cl in (First, Second, Third):
    print('\n' + cl.__name__ + ' class...')
    cl().display()

###############################
#  命名空间: 禅--涅槃重生
###############################
print('\n')
print('>>>>>>>> 命名空间:')
X = 11


def f():
    """# f() Access global X(11)"""
    print(X)


def g():
    """# g() Local(function) variable (X, hides module X)"""
    X = 22
    print(X)


class C:
    """# Class attribute (C.X)"""
    X = 33

    def __init__(self):
        pass

    def m(self):
        """# Local variable in method"""
        X = 44

        """# Instance attribute (instance.X)"""
        self.X = 55


print(f.__doc__)
print(g.__doc__)
print(C().__doc__)
print(C().m.__doc__)

###############################
#       模块 VS 类
# 模块:
#      1.是数据/逻辑包
#      2.通过编写Python文件或C扩展来创建
#      3.通过导入来使用
# 类
#      1.实现新的对象
#      2.由class语句来创建
#      3.通过调用来使用
#      2.总是位于一个模块中
###############################


###############################
#  类的设计:
#  1.Python没有类型声明,基于参数类型标记的重载函数行不通;
###############################


###############################
#  类的伪私有属性:
###############################
print('\n')
print('>>>>>>>> 私有属性示例:')


class C1:
    X = None

    def method_1(self):
        self.X = 88

    def method_2(self):
        print(self.X)


class C2:
    X = None

    def method_a(self):
        self.X = 99

    def method_b(self):
        print(self.X)


class C3(C1, C2):
    pass


tmp1 = C3()
tmp1.method_1()
tmp1.method_2()

tmp1.method_a()
tmp1.method_b()

tmp1.method_2()
print(tmp1.__dict__)

# 伪私有示例
print('\n')
print('>>>>>>>> 伪私有属性示例:')


class C11:
    __X = None

    def method_1(self):
        self.__X = 88

    def method_2(self):
        print(self.__X)


class C22:
    __X = None

    def method_a(self):
        self.__X = 99

    def method_b(self):
        print(self.__X)


class C33(C11, C22):
    pass


tmp2 = C33()
tmp2.method_1()
tmp2.method_2()

tmp2.method_a()
tmp2.method_b()

tmp2.method_2()
print(tmp2.__dict__)

###############################
#  方法是对象,可分为两种:
#  1.无绑定方法
#  2.绑定方法
###############################
print('\n')
print('>>>>>>>> 绑定&无绑定方法: ')


# 1.方法是对象示例


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2


x = Number(2)
y = Number(3)
z = Number(4)
# act = x.double
acts = [x.double, y.double, z.double]
for act in acts:
    print('方法是对象: ', act())


# 2.无绑定方法示例
class Spam:

    def doit(self, toprint):
        print(toprint)


obj = Spam()
unbind = Spam.doit  # 得到未绑定方法
unbind(obj, 'unbind: Hello World')
# unbind('unbind: Hello World')  unbound method doit() must be called with Spam instance as first argument


# 3.绑定方法示例
objbind = obj.doit  # 得到绑定方法
objbind(' bind : Hello World')

print(isinstance(objbind, object))
print(isinstance(Spam, object))

###############################
#  属性限制(__slots__)
#  1.使用slots可以限制类的属性;
#  2.slots属性可以节省空间,提高执行效率;
#  3.slots顺序存储属性,不会为实例分配字典属性
###############################
print('\n')
print('>>>>>>>> 类的属性限制:')


class Limiter(object):
    def __init__(self):
        self.name = ''
        self.age = 10
    # 把下面的代码注释掉后再次执行，可以查看出错日志信息
    # __slots__ = ['age', 'name', 'job']


x = Limiter()
x.name = 'Tom'
x.age = 28
x.score = 100
print('属性限制:', x.name)
print('属性限制:', x.age)
print('属性限制:', x.score)
print(x.__dict__)

###############################
#  装饰器:
# 1.静态函数装饰器:staticmethod
###############################
print('\n')
print('>>>>>>>> 静态函数装饰器:')


class StaticClass:
    numInstances = 0
    numInstance = 0

    def __init__(self):
        StaticClass.numInstances += 1  # 类空间属性,所有的实例对象共享。相当于类的静态属性
        self.numInstance += 1  # 对象空间属性,属于每个对象实例自己的属性
        # 注意:
        #     如果使用下面被注释的代码，是无法统计该类被实例化的次数的
        # self.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances created: ', StaticClass.numInstances)


a = StaticClass()
print('numInstance = {0}'.format(a.numInstance))
StaticClass.printNumInstances()

b = StaticClass()
print('numInstance = {0}'.format(b.numInstance))
StaticClass.printNumInstances()

c = StaticClass()
print('numInstance = {0}'.format(c.numInstance))
StaticClass.printNumInstances()

print('\n')
print('>>>>>>>> bool表达式的支持(__nonzero__)')


class C:

    c_date = ''

    def __init__(self, c_date):
        self.c_date = c_date

    def __bool__(self):
        if self.c_date == '':
            return False
        else:
            return True


c = C('abc')
print(c.c_date)
#
print(bool(C))
print(bool(c))
#
print(type(C))
print(type(c))

print('*' * 50)
