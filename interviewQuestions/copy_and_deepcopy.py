import copy

'''
可变对象 VS 不可变对象
可变对象: 列表、字典
不可变对象: 元组、字符串、数字

可变对象和不可变对象，打印结果不一样
'''

a = ('a', 'b', 'c')
# a = {'a', 'b', 'c'}
# a = ['a', 'b', 'c']

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

print(b)
print(c)
print(d)

print(id(b))
print(id(c))
print(id(d))


