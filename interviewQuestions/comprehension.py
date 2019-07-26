'''
   一行代码实现: 根据一个列表,创建一个新的列表
   lambda表达式    推导式
'''

list1 = [1, 2, 3, 4]
list2 = list(map(lambda x : x**2, list1))

print(list2)

# 列表推导式
list3 = [i**2  for i in list1]
print(list3)

# 字典推导式
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {k:v for k,v in dict1.items()}
print(dict2)

