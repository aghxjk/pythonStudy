#encoding: utf-8
import operator

__author__ = 'zhaoyimeng'


##################################
#    列表常量 和 操作
##################################

# 初始化
print('>>>>>>>>List初始化:')
list1 = []                                   # 空列表
print('[] = {0}'.format(list1))
list2 = [0, 1, 2, 3]                         # 四项,索引为0开始
print('[0, 1, 2, 3] = {0}'.format(list2))
list3 = ['abc', [0, 1]]                      # 嵌套的子列表
print("['abc', [0, 1]]] = {0}".format(list3))
list4 = list('abcd')                         # 可迭代项目列表
print("list('abcd') = {0}".format(list4))
list5 = list(range(-4, 4))
print("list(range(-4, 4)) = {0}".format(list5))

print('\n')
print('>>>>>>>>索引与分片:')
list6 = list2[::2]                         # 索引与分片
print('list2[0:-1:2] = ', list6, 'and length =', list3.__len__())           # 列表长度

print('\n')
print('>>>>迭代操作:')
listAdd = list2 + list4                      # 合并
print('list2 + list4 = {0}'.format(listAdd))

print('listAdd =', listAdd)
for x in range(0, len(listAdd)):
    print('listAdd[{0}] = {1}'.format(x, listAdd[x]))                                 # 迭代

print('\nlist2 =', list2)
print('[x**2 for x in list2] =', [x**2 for x in list2])

# 增长，排序，搜索，插入，翻转等
print('\n')
print('>>>>>>>>基本操作:')
print('list2 =', list2)
list2.append('end')
print("list2.append('end') =", list2)
list2.insert(1, 'y')
print("list2.insert(1, 'y') =", list2)
print("list2.index('t') =", list2.index('t') if 't' in list2 else 'not Found')     # 查询't'所在的索引位置
print("list2.count('end') =", list2.count('end'))                                    # 统计't'出现的次数

print('\n')
print('>>>>>>>>list排序:')
# Python2 可以对list中的str和int进行混排
# python3 list中的str和int不能混合排序,会抛异常;可参考如下转化
list2.sort(key=lambda x: str(x) if type(x) is int else x)                           # 排序
print('list2.sort() =', list2)
list2.reverse()
print('list2.reverse() = ', list2)                              # 翻转
list2[0] = 'a'                               # 对象原处修改,str和tuple不允许的
print("list2[0] = 'a' => ", list2)

lista = [['d', 2], ['c', 1], ['a', 4], ['b', 3]]
print('lista =', lista)
lista.sort()
print('lista.sort()', lista)
# 按照list中list的第一个元素进行排序
lista.sort(key=lambda x: x[0], reverse=True)
print('lista.sort(key=lambda x: x[0], reverse=True) =>', lista)

print('\n')
print('>>>>>>>>删除与替换操作:')
print('list2 =', list2)
del list2[-1]
print('del list2[-1] =', list2)              # 删除最后一个
del list2[0:2]                               # 删除前两个
print('del list2[0:2] =', list2)
list2.pop(1)                                 # 删除索引为1的值
print('list2.pop(1) =', list2)
list2.remove(3)                              # 删除值数据3
print('list2.remove(3) =', list2)
list2 = [0, 1, 2, 3]
print('list2 =', list2)
list2[1:3] = []                              # 删除索引指定的内容,左闭右开区间的索引
print('list2[1:3] = [] =>', list2)
list2[1:3] = [1, 2]                          # 索引赋值
print('list2[1:3] = [1, 2] =>', list2)
print("map(ord, 'abcd') = ", list(map(ord, 'abcd')))

print('list2 =', list2)
print("''.join([str(x) for x in list2]) + 'abc' =", ''.join([str(x) for x in list2]) + 'abc')                    # list to string
list2.extend([9, 10])                        # 增加多个值
print('list2.extend([9, 10]) =', list2)

print('\n')
print('>>>>>>>>类型判断:')
print("isinstance(list2, list) : {0}".format(isinstance(list2, list)))                 # 类型判断，适用其它数据类型
print("type([1]) == list : {0}".format(type([1]) == list))

print('\n')
print('>>>>>>>>矩阵+迭代 示例:')
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print('''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
''')
diagonal = [matrix[i][j] for i in range(3) for j in range(3) if (i == j)]
print('迭代方式-1: diagonal = {0}'.format(diagonal))

tmp = []
for i in range(3):
    for j in range(3):
        if i == j:
            tmp.append(matrix[i][j])

print('迭代方式-2: diagonal = {0}'.format(tmp))


##################################
#    列表表达式
#    语法:  [expr for iter_var in iterable if cond_expr]
##################################

print('\n')
print('>>>>>>>>列表表达式:')
seq = [ss for ss in range(0, 15)]
print('seq = [ss for ss in range(2, 15)] =>', seq)
flr = filter(lambda xxx: xxx % 2 != 0, seq)
print('filter(lambda xxx: xxx % 2 != 0, seq) =', list(flr))
mp = map(lambda sq: sq**2, seq)
print('map(lambda sq: sq**2, seq) =>', list(mp))

string_array = ['a1 b c d', 'a b c d', 'a b c d']
print('to sum the total words in string_array:', sum(len(word) for item in string_array for word in item.split()))
print('to sum the total words in string_array:', sum(len("".join(i.split())) for i in string_array))