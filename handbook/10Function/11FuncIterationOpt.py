#encoding: utf-8
__author__ = 'zhaoyimeng'


###############################
#   迭代与解析：
###############################

print('>>>>>>>> 迭代与解析:')

# 收集字符串的ASCII编码
# 1.直接迭代方式:
res1 = []
for x in 'abcdefg':
    res1.append(ord(x))

print('res1.append(ord(x)) => ', res1)

# 2.map方式:
res2 = map(ord, 'abcdefg')
print("map(ord, 'abcdefg') => ", list(res2))

# 3.列表解析表达式
res3 = [ord(x) for x in 'abcdefg']
print("[ord(x) for x in 'abcdefg'] => ", res3)


###############################
#   列表解析表达式增加测试条件
###############################
print('\n')
print('>>>>>>>> 迭代增加测试条件:')
# 获取10以内的偶数的平方列表
res1 = [x**2 for x in range(11) if (x % 2) == 0]
print('[x**2 for x in range(11) if (x % 2) == 0] => ', res1)

# 等效的map调用
res2 = map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(11)))
print('map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(11))) => ', list(res2))



###############################
#   列表解析表达式增加嵌套循环
###############################
print('\n')
print('>>>>>>>> 列表解析表达式增加嵌套循环:')
res3 = [x + y for x in [1, 2, 3]
              for y in [10, 20, 30]
       ]
print('循环嵌套: ', res3)

# 等效的冗长代码
# 注意: 此处的等效仅仅效果上的等效,而不是效率上的等效
res = []
for x in [1, 2, 3]:
    for y in [10, 20, 30]:
        res.append(x+y)

print('等效代码: ', res)


###############################
#   列表解析表达式: 条件测试 + 嵌套循环
###############################
print('\n')
print('>>>>>>>> 列表解析表达式:条件测试 + 嵌套循环:')
res = [(x, y)
       for x in range(5) if x % 2 == 0
       for y in range(5) if y % 2 == 1]

print('测试 + 循环: ', res)


###############################
#   生成器函数: yield
#   优点：
#       避免函数一次性把所有的工作完成，
#   尤其结果的列很大或者处理的每一个结果
#   都需要很多时间时，这一点尤其有用
###############################
print('\n')
print('>>>>>>>> 列表解析表达式:条件测试 + 嵌套循环:')


print('>>>>>>>> 传统方式:')


def gen_squares(n):
    tmp = []
    for idx in range(n):
        tmp.append(idx ** 2)
    return tmp


funObj1 = gen_squares(5)
print('传统方式: ', funObj1)


print('\n')
print('>>>>>>>> yield方式:')


def yield_squares(n):
    for idx in range(n):
        yield idx ** 2


funObj2 = yield_squares(5)
print('yield方式: ', funObj2)


print('\n')
print('>>>>>>>> 生成器对象支持迭代协议:')
for i in funObj2:
    print(i)


print('\n')
print('>>>>>>>> 生成器有一个__next__方法:')

funObj = yield_squares(5)
print('next(x)调用X.__next__()方法: ', next(funObj))
print('next(x)调用X.__next__()方法: ', next(funObj))
print('next(x)调用X.__next__()方法: ', next(funObj))
print('next(x)调用X.__next__()方法: ', next(funObj))
print('next(x)调用X.__next__()方法: ', next(funObj))


###############################
#  生成器表达式
###############################
print('\n')
print('>>>>>>>> 生成器表达式:')
obj1 = [x**2 for x in range(4)]
obj2 = (x**2 for x in range(4))
print('一次生成结果: ', obj1)                  # list object, not an iterator
print('生成器表达式: ', obj2.__next__())
print('生成器表达式: ', obj2.__next__())
print('生成器表达式: ', obj2.__next__())
print('生成器表达式: ', obj2.__next__())           # 注意,如果再次调用obj2.next()会发生StopIteration异常
