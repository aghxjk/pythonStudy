#encoding: utf-8
import operator

__author__ = 'zhaoyimeng'


##################################
#    列表常量 和 操作
##################################

# 初始化
list1 = []                                   # 空列表
list2 = [0, 1, 2, 3]                         # 四项,索引为0开始
list3 = ['abc', [0, 1]]                      # 嵌套的子列表
list4 = list('abcd')                         # 可迭代项目列表
list5 = list(range(-4, 4))

print('>>>>索引与分片:')
list6 = list2[0:-1:2]                        # 索引与分片
print(list6, 'length=', len(list3))           # 列表长度
print('-' * 24)


print('>>>>迭代操作:')
listAdd = list2 + list4                      # 合并

for x in listAdd:
    print(x)                                 # 迭代

print([x**2 for x in list2])
print('-' * 24)

# 增长，排序，搜索，插入，翻转等
print('>>>>基本操作:')
list2.append('t')                            # 尾部添加't'
list2.insert(1, 'y')                         # 索引为1的位置插入'y'
print(list2.index('t'))                      # 查询't'所在的索引位置
print(list2.count('t'))                      # 统计't'出现的次数
# list2.sort()                                 # 排序
print('+' * 20)
list2 = [ x if type(x) is int else ord(x) for x in list2]
list2.sort()
print(list2)
list2.reverse()                              # 翻转
print(list2)
list2[0] = 'a'                               # 对象原处修改,str和tuple不允许的
print(list2)
print('-' * 24)

print('>>>>删除与替换操作:')
del list2[-1]                                # 删除最后一个
del list2[0:2]                               # 删除前两个
list2.pop(1)                                 # 删除索引为1的值
list2.remove(3)                              # 删除值数据3
list2 = [0, 1, 2, 3]
list2[1:3] = []                              # 删除索引指定的内容,左闭右开区间的索引
print(list2)
list2[1:3] = [1, 2]                          # 索引赋值
print(list2)
print(map(ord, 'abcd'))
print("".join([str(x) for x in list2]) + 'abc')                    # list to string
list2.extend([9, 10])                        # 增加多个值
print(list2)
print('-' * 24)


print('>>>>类型判断:')
print("type(list2) == type([]) : {0}".format(isinstance(list2, list)))                 # 类型判断，适用其它数据类型
print("type([1]) == list : {0}".format(type([1]) == list))
print('-' * 24)


print('>>>>矩阵+迭代 示例:')
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

# 备注:  两种迭代方式有何区别?

lista = [['d', 2], ['c', 1], ['a', 4], ['b', 3]]
# lista.sort()
lista.sort(lambda x, y: operator.lt(x[1], y[1]), reverse=True)
print(lista)

##################################
#    列表表达式
#    语法:  [expr for iter_var in iterable if cond_expr]
##################################

seq = [ss for ss in range(2, 15)]
flr = filter(lambda xxx: xxx % 2 != 0, seq)
mp = map(lambda sq: sq**2, seq)
print(flr)
print(mp)

string_array = ['a1 b c d', 'a b c d', 'a b c d']
print('to sum the total words in string_array:', sum(len(word) for item in string_array for word in item.split()))
print('to sum the total words in string_array:', sum(len("".join(i.split())) for i in string_array))