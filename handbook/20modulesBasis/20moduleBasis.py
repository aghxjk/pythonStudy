#encoding: utf-8
__author__ = 'zhaoyimeng'
import sys
import moda


###############################
#  宏伟蓝图： 模块
#  import: 导入者以一个整体获取一个模块(模块往往对应于Python的程序文件)
#  from:   允许导入者从一个模块文件中获取特定的变量名
#  import.reload: 在不终止python程序情况下，提供了一种重新载入模块文件代码的方法
#              reload操作不会影响import导入的属性，需要通过.运算符来使用reload之后的值
###
#  Python载入的模块存储到一个名为sys.modules表中,在导入操作开始前会检查该表，如果不存在则会启动如下3个步骤规程：
#  1. 找到模块文件
#  2. 编译成位码(需要时)
#  3. 执行模块的代码来创建其所定义的对象
###
#  模块导入的搜索路径:
#  1. 程序的主目录                        -->  自动定义
#  2. PYTHONPATH目录(如果已经进行了设置)   -->  用于扩展
#  3. 标准链接库目录                      -->  自动定义
#  4. 任何.pth文件的内容(如果存在的话)      -->  用于扩展
###############################

###############################
# import 和 from是赋值语句(隐性的赋值语句)
# 1. 像def一样,import和from是可执行的语句，而不是编译期间的声明；
# 2. 它们可以嵌套在if测试中，出现在函数def之中等
###############################
print('\n')
print('>>>>>>>> 模块信息: ')

print('获取当前系统模块: ', sys.path)
print('获取模块属性: ', sorted(dir(sys)))          # dir方法其实是对obj.__dict__.keys()的解析
print('获取模块属性: ', sorted(sys.__dict__.keys()))   # 结果同dir(sys)
print('获取模块名字: ', sys.__name__)

###############################
#  导入操作不会赋予被导入文件中的代码对上层代码的可见度:
#  即: 被导入文件无法看见进行导入文件内的变量名
###############################
print('\n')
print('>>>>>>>> 可见度示例: ')
X = 100
moda.func()
print('可见度示例: ', X, moda.X)


###############################
#  最小化的破坏:  _x 和 __all__(该变量一般定义在__init__.py中)
# 1. import * 只会导入__all__中定义的属性
# 2. import * 会忽略以‘_’开头的属性
# 3. from语句导入，是对变量名拷贝运算,而不是变量名的别名机制,本地作用域修改不会影响被导入文件的变量值
# 4. import导入整个模块时,如果使用点运算符,就会修改被导入文件的变量.
# 示例: /Users/zhaoyimeng/Library/Python/2.7/lib/python/site-packages/easygui
###############################
print('\n')
print('>>>>>>>> from import示例: ')
# flag = True
flag = False
if flag:
    from eg1 import *
    aa = eg
    aa = 10
    eg = 10              # 模块eg1中的变量eg不会被本文件中的eg覆盖
    print('printer() : ', printer())
else:
    import eg1
    eg1.eg = 88
    print('eg1.printer(): ', eg1.printer())

###############################
#   __name__ 和 __main__
# 1.文件以顶层程序文件执行，启动时，__name__自动设置为__main__
# 2.如果文件被导入,则__name__会设置为导入者所了解的模块名
###############################
print('\n')
print('>>>>>>>> 关于顶层模块: ')
print('顶层模块__name__ = ', __name__)
print('导入模块__name__ = ', moda.__name__)

# 以__name__来进行单测
# 相当于java  类中的public static void  main()一样
if __name__ == '__main__':
    print('\n__name__ = __main__')


###############################
# 修改模块搜索路径
###############################
import sys
sys.path.append('/Users/zhaoyimeng/PycharmProjects')


###############################
#  模块导入语句的as扩展
###############################
import sys as mysys
print('\n模块导入as扩展: ', mysys.__name__)
# 以上语句相当于:
# import moduleName
# name = doduleName
# del moduleName


###############################
#  用名称字符串导入模块
###############################

# import 'string'
# import 'string'
#               ^
# SyntaxError: invalid syntax

# xxx = 'string'
# import xxx
# python会尝试导入一个xxx.py的模块

# 通过内置函数exec导入
# exec的唯一缺点是: 每次运行时它必须编译import语句，如果运行多次将是非常低效的
modname = 'string'
exec('import ' + modname)

# 使用内置函数__import__来代替exec代码运行会快些
__import__(modname)


from os import system
print('\n')
print('>>>>>>>> 调用shell命令:')
system("ls -l")
