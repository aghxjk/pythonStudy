#encoding: utf-8
from functools import reduce
import sys

__author__ = 'zhaoyimeng'


###############################
#   变量层次结构：
#   函数内的变量，全局变量，内建变量
###############################

print('''
变量作用域LEGB原则:
    1. 变量名引用分三个作用域: 本地 > 函数内 > 全局 > 内置
    2. 默认情况, 变量名赋值会创建或者改变本地变量
    3. 全局声明和非本地声明将赋值的变量映射到模块文件内部的作用域
    
    L: 本地作用域
    E: 上一层结构中def或lambda的本地作用域
    G: 全局作用域
    B: 内置作用域
    |———————————————————————————————————————————————|
    |  Build-in(Python)                             |
    |   |—————————————————————————————————————————| |
    |   | Global(module)                          | |
    |   |   |———————————————————————————————————| | |
    |   |   | Enclosing function locals         | | |
    |   |   |   |—————————————————————————————| | | |
    |   |   |   | Local(function)             | | | |
    |   |   |   |_____________________________| | | |
    |   |   |___________________________________| | |
    |   |_________________________________________| |
    |_______________________________________________|
''')
print('\n')
print('>>>>>>>> 全局变量')
g_var = 90


def gfunc(v):
    global g_var
    g_var = v


def lfunc(v):
    g_var = v


print('g_var = {0}'.format(g_var))
print('>>>>>>>> 操作全局变量')
gfunc(80)
print('gfunc(80) => g_var = {0}'.format(g_var))

print('\n')
print('>>>>>>>> 操作局部变量')
lfunc(90)
print('lfunc(90) => g_var = {0}'.format(g_var))

# 函数可以作为对象复制给其它变量进行函数调用
print('\n')
print('>>>>>>>> 函数也是对象:')
tf = gfunc
tf(100)
print('tf = gfunc\ntf(100) => g_var = {0}'.format(g_var))


print('\n')
print('>>>>>>>> 函数可以嵌套:')


def outFunc():
    out_x = 10

    def inFunc():
        print('inFunc call: ', out_x)           # outFunc 使用的是变量是Enclosing function locals
    inFunc()


outFunc()

X = 99

print('>>>>>>>> 嵌套作用域举例')


def fun1():
    X = 88

    def fun2():
        print('fun1->fun2 =>', X)
    return fun2


action1 = fun1()
action1()


def fun11():
    fx = 4
    return lambda n: fx * n


action2 = fun11()
print('fun11() => {0}'.format(action2(4)))

print('\n')
print('>>>>>>>> 工厂函数:')


def maker(n):
    def action3(m):
        return m * n
    return action3


fct = maker(9)
rs1 = fct(9)
rs2 = fct(10)
print('Factory maker: rs1={0}  rs2={1}'.format(rs1, rs2))


def makerAction():
    acts = []
    for i in range(5):
        acts.append(lambda x, n=i: x ** n)    # i必须赋值给lambda表达式
    return acts


action3 = makerAction()
print('makerAction: action3[0](2) = {0}'.format(action3[0](2)))
print('makerAction: action3[1](2) = {0}'.format(action3[1](2)))
print('makerAction: action3[2](2) = {0}'.format(action3[2](2)))
print('makerAction: action3[3](2) = {0}'.format(action3[3](2)))
print('makerAction: action3[4](2) = {0}'.format(action3[4](2)))


print('\n')
print('>>>>>>>> nonlocal作用域')


def tester(start):
    state = start

    def nested(lable):
        nonlocal state                 # 如果不使用nonlocal,会导致调用时state不可写
        state += 1
        print('nonlocal test: {0} count={1}'.format(lable, state))
    return nested


test = tester(0)
test('apple ')
test('eggs  ')
test('babies')


###############################
# 函数传递参数的总结
# 1. 对于不可变对象，参数是拷贝传递方式
# 2. 对于可变对象，参数是引用传递
###############################

print('\n')
print('>>>>>>>>函数参数传递: ')


def changer1(a, b):
    a = 2
    b[0] = 'test'


x = 1
li = [1, 2]

changer1(x, li)
print("changer1: ", 'x = ', x, '\nli = ', li)

###############################
# 避免可变参数的修改
# 对于changer(a, b)函数如果想阻止对原值的修改，可以通过以下3中方式实现
###############################

print('\n')
print('>>>>>>>>避免可变参数修改: ')
# 第1中, 参数以拷贝的方式进行


def changer2(a, b):
    a = 2
    l = b[:]
    l[0] = 'testing....'


changer2(x, li)
print("changer2: ", 'x = ', x, '\nl= ', li)
print('-' * 20)


###############################
# 关于返回值的案例：
# 看起来返回了两个2值，其实是一个元组
###############################
print('>>>>>>>>关于函数返回值: ')


def multiple():
    x = 1
    y = [2, 3]
    return x, y


tmp = multiple()
a, b = multiple()
print("multiple-1: ", tmp)
print("multiple-2: ", a, b)


###############################
# 任意参数的函数实例:
###############################
print('\n')
print('>>>>>>>>函数传参匹配语法: ')
print('#' * 20)
print('#  语法' + ' ' * 21 + '位置' + ' ' * 5 + '解释')
print('#  func(value)' + ' ' * 12 + '调用者' + ' ' * 4 + '常规参数: 通过位置进行匹配')
print('#  func(name=value)' + ' ' * 7 + '调用者' + ' ' * 4 + '关键字参数: 通过位置进行匹配')
print('#  func(*sequence)' + ' ' * 8 + '调用者' + ' ' * 4 + '以name传递所有的对象,并作为独立的基于位置的参数')
print('#  func(**dict)' + ' ' * 11 + '调用者' + ' ' * 4 + '以name成对传递所有的关键字/值,并作为独立的关键字参数')
print('#  def func(name)' + ' ' * 10 + '函数' + ' ' * 5 + '常规参数: 通过位置进行匹配')
print('#  def func(name=value)' + ' ' * 4 + '函数' + ' ' * 5 + '默认参数值,如果没有在调用中传递的话')
print('#  def func(*name)' + ' ' * 9 + '函数' + ' ' * 5 + '匹配并收集(在元组中)所有包含位置的参数')
print('#  def func(**name)' + ' ' * 8 + '函数' + ' ' * 5 + '匹配并收集(在字典中)所有包含位置的参数')
print('#  def func(*args, name)' + ' ' * 3 + '函数' + ' ' * 5 + '参数必须在调用中按照关键字传递')
print('#  def func(*, name=value)' + ' ' * 1 + '函数' + ' ' * 5 + 'Python3.0')
print('#  def func(name, name=value, *name, **name)' + ' ' * 1 + '参数顺序')
print('#' * 20)


print('\n')
print('>>>>>>>> 关键字与默认参数混合示例:')


def func_test1(spam, eggs, toast=0, ham=0):
    print('func(spam, eggs, toast=0, ham=0) => {0}'.format((spam, eggs, toast, ham)))


func_test1(1, 2)
func_test1(1, ham=1, eggs=0)
func_test1(spam=1, eggs=0)
func_test1(toast=1, eggs=2, spam=3)
func_test1(1, 2, 3, 4)

print('\n')
print('>>>>>>>> 任意参数示例:')


def more_args1(*args):
    print('moreArgs1: ', args)


more_args1(1, 2, 3, 4)


def more_args2(**kwargs):
    print('moreArgs2: ', kwargs)


more_args2(a=1, b=2, c=3)


print('\n')
print('>>>>>>>> 解包参数示例:')


def func_unpack(a, b, c, d):
    print('func_unpack(示例) => {0}'.format((a, b, c, d)))


args = (1, 2)
args += (3, 4)
func_unpack(*args)
func_unpack(*(1, 2), **{'d': 4, 'c': 3})
func_unpack(1, *(2, 3), **{'d': 4})
func_unpack(1, c=3, *(2,), **{'d': 4})


print('\n')
print('>>>>>>>> 获取任意类型的元素最小值练习')
# 其实可以使用内置函数min()和max()


def min_find(*args):
    list_to_find = list(args)
    list_to_find.sort()
    print('min_find({0}) => {1}'.format(list(args), list_to_find[0]))
    return list_to_find[0]


min_find(3, 4, 1, 2)


print('\n')
print('>>>>>>>> 模拟输出函数print30示例-1:')


def print30(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)

    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    output += end
    file.write('print30{0} => {1}'.format(tuple(args), output))


print30(1, 2, 3)


print('\n')
print('>>>>>>>> 模拟输出函数print31示例-2:')


def print31(*args, sep=' ', end='\n', file=sys.stdout):
    first = True
    output = ''
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    output += end
    file.write('print30{0} => {1}'.format(tuple(args), output))


print31('a', 'b', 'c', 'd')


###############################
# 递归1
# 对于python这种脚本类语言，迭代方式一般更自然一些
###############################
print('\n')
print('>>>>>>>> 递归函数-1: ')


def mysum1(L):
    if len(L) == 0:
        return 0
    else:
        print(L)
        return L[0] + mysum1(L[1:])


tmp = mysum1([1, 2, 3, 4, 5])
print("mysum1([1, 2, 3, 4, 5]) => {0}".format(tmp))


print('\n')
print('>>>>>>>> 递归函数-2: ')


def mysum2(L):
    print(L)
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])


tmp = mysum2([1, 2, 3, 4, 5])
print("mysum2([1, 2, 3, 4, 5]) => {0}".format(tmp))


###############################
# 递归2
# 处理任意结构
###############################
print('\n')
print('>>>>>>>> 递归函数-3(处理任意结构): ')


def sum_tree(ll):
    tot = 0
    for x in ll:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sum_tree(x)
    return tot


vll = [1, [2, [3, 4, 5]], 6, [7, 8]]
tmp = sum_tree(vll)
print("sum_tree([1, [2, [3, 4, 5]], 6, [7, 8]]) => {0}".format(tmp))


###############################
# 函数高级话题  内省(探索函数实现细节)
###############################
print('\n')
print('>>>>>>>> 函数高级话题: ')
print('function.__name__: ', sum_tree.__name__)
print('function.__code__: ', dir(sum_tree.__code__))
print('function.__code__.co_argcount: ', sum_tree.__code__.co_argcount)


###############################
# lambda表达式
# 为什么使用lambda ?
# 表达式: 是一个值,他的结果一定是一个python对象
# 语  句: 结果不是对象的代码则成为语句,例如: if  printf  for 和 while循环等。他们是一个动作而不生成一个值;
###############################

# 1.使用简洁代码代替def的函数定义
print('\n')
print('>>>>>>>> 带默认值的lambda表达式: ')
express = (lambda x=0, y=0, z=0: x + y + z)  # 括号可以去掉
tmp = express(1, 2, 3)
print('lambda: ', tmp)

# 2.编写跳转表,代替if语句
jumplist = [
    lambda x : x ** 2,
    lambda x : x ** 3,
    lambda x : x ** 4,
]

for f in jumplist:
    print('jump list: ', f(2))


jumpset = {
    'already': (lambda x, y: x + y),
    'got': (lambda x, y: x * y),
    'done': (lambda x, y: x**y)
}

print('jump set: ', jumpset['done'](2, 3))


# 3.lambda一个常用 的应用就是在tkinter GUI中定义行内的回调函数
# import sys
# from Tkinter import *
# mainwin = Tk()
# x = Button(
#     mainwin,
#     text='Press me',
#     command=(lambda: sys.stdout.write('aaaaaaaaa') )
# )
# x.pack()
# mainloop()


###############################
# 在序列中映射函数(高效率的map函数)
###############################
print('\n')
print('>>>>>>>> 序列中的映射函数: ')


def inc(x):
    return x + 10


counters = [x for x in range(0, 10)]
print('counters = [x for x in range(0, 10)] => ', counters)
tmp1 = map(inc, counters)
print('map(inc, counters) => ', list(tmp1))
tmp2 = map((lambda t: t + 10), counters)
print('map((lambda t: t + 10), counters) => ', list(tmp2))


###############################
# 函数式编程工具：filter and reduce(它们都是内置函数)
# 函数式编程的意思就是对序列应用一些函数工具
###############################

print('\n')
print('>>>>>>>> 函数式编程: ')
# filter
lst1 = [x for x in range(-5, 5)]
tmp = filter((lambda t: t > 0), lst1)
print('filter((lambda t: t > 0), lst1) => ', list(tmp))

# 等效循环
res1 = []
for i in lst1:
    if i > 0:
        res1.append(i)

# reduce
# 序列中的第一个元素初始化了起始值。
# 每一步迭代，reduce传递了当前的和或积以及列表中的下一个元素，传递给lambda函数。
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
lst2 = [x for x in range(1, 5)]
tmp1 = reduce((lambda i, j: i + j), lst2)
tmp2 = reduce((lambda i, j: i * j), lst2)
print('reduce((lambda i, j: i + j), [1, 2, 3, 4]) = ', tmp1)
print('reduce((lambda i, j: i * j), [1, 2, 3, 4]) = ', tmp2)

# 等效的tmp1循环
res2 = lst2[0]
for x in lst2[1:]:
    res2 += x


############################
#  示例
############################

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprod():
    op = choice('+-')
    nums = [randint(1, 10) for counts in range(2)]
    nums.sort(reverse=True)
    # ans = reduce(ops[op], nums)
    ans = ops[op](*nums)   # 将nums变成可变参数传递给ops[op] 等效于: ops[op](nums[0], nums[1])

    pr = '{0} {1} {2} = '.format(nums[0], op, nums[1])


    opps = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if opps == MAXTRIES:
                print('answer\n %s %d' % (pr, ans))
            else:
                print('incorrect... try again')
            opps += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print('invalid input... try again')


def main():
    while True:
        doprod()
        try:
            opt = input('Again?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    # main()
    pass