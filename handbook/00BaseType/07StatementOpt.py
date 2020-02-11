#######################################
#        语句: Statement               #
#######################################


print('>>>>>>>> 赋值语句')
spam = 'Spam'                         # 基本形式
print("spam = 'Spam' => {0}".format(spam))

spam, ham = 'yum', 'YUM'              # 元组赋值运算
print("spam, ham = 'yum', 'YUM'  => spam={0}, ham={1}".format(spam, ham))

[spam, ham] = ['yum-1', 'YUM-2']     # 多目标 & 列表赋值运算
print("[spam, ham] = ['yum-1', 'YUM-1'] => spam={0}, ham={1}".format(spam, ham))

a, b, c, d = 'spam'                   # 序列赋值运算
print("a, b, c, d = 'spam' => a={0}, b={1}, c={2}, d={3}".format(a, b, c, d))

a, *b = 'spam'                        # 扩展的序列解包(Python3)
print("a, *b = 'spam' => a={0}, b={1}".format(a, b))

a, *b, c = 'spam'                        # 扩展的序列解包(Python3)
print("a, *b, c = 'spam' => a={0}, b={1}, c={2}".format(a, b, c))

spams = 10
spams += 24                           # 增强赋值运算
print("spams += 24 => spams = {0}".format(spams))

nudge = 1
wink = 2
nudge, wink = wink, nudge             # 元组赋值技巧(交换两个变量的值)
print("nudge, wink = wink, nudge => nudge={0}, wink={1}".format(nudge, wink))

string = 'SPAM'
a, b, c, d = string                   # 必须保证左右两侧数目一致,否则会报错
print('a, b, c, d = string => a={0}, b={1}, c={2}, d={3}'.format(a, b, c, d))

print('\n')
print('>>>>>>>> 增强赋值语句')
L = [1, 2]
L += [3, 4]                           # 增强赋值语句比普通赋值语句执行效率更高,python自动调用的是L.extend()方法
print('L += [3, 4] => L = {0}'.format(L))

print('\n')
print('>>>>>>>> 变量命名规范')
print('''
    1. 单一下划线开通的变量名(_X)不会被from module import *语句导入;
    2. 前后有下划线的变量名(_X_)是系统定义的变量名,对解释器有特殊意义;
    3. 两个下划线开通,结尾没有下划线的变量名(__X)是类的本地变量;
''')


print('\n')
print('>>>>>>>> 常见表达式语句')
print('''
    spam(eggs, ham)             函数调用
    spam.ham(eggs)              方法调用
    spam                        交互式模式解释器内打印变量
    print(a, b, c)              Python3.0中的打印操作
    yield x ** 2                产生表达式的语句
''')

print('>>>>>>>> 真值测试')
test = 2 or 3, 4 or 5
print('2 or 3, 4 or 5 = {0}'.format(test))

test = 2 and 3, 4 and 5
print('2 and 3, 4 and 5 = {0}'.format(test))

print('\n')
print('>>>>>>>> if/else三元表达式')
print('''
    if X:
        A = Y
    else:
        A = Z
        
    等效于：
        A = Y if X else Z
''')


print('\n')
print('>>>>>>>> while循环语句')
print('''
    while <test1>:
        <statements>
        if <test2>: break
        if <test3>: continue
    else:
        <statements>

''')

print('\n')
print('>>>>>>>> for循环语句')
print('''
    for <target> in <object>:
        <statements>
        if <test2>: break
        if <test3>: continue
    else:
        <statements>

''')

print('\n')
print('>>>>>>>> 单迭代器与多迭代器')

print('>>>> 多迭代器')
R = range(4)
I1 = iter(R)
I2 = iter(R)
print('next(I1) = {0}'.format(next(I1)))
print('next(I2) = {0}'.format(next(I2)))


print('\n')
print('>>>> 单迭代器')
L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']
Z = zip(L1, L2)
I1 = iter(Z)
I2 = iter(Z)
print('next(I1) = {0}'.format(next(I1)))
print('next(I2) = {0}'.format(next(I2)))








