#encoding: utf-8


# 可变集合
print('>>>>>>>>可变集合:')
s = set('cheeseshop')                  # set集合是不可重复的元素的集合
print("s = set('cheeseshop') =>", s)
s.add('test')
s.add('e')
print("s.add('test') \ns.add('e')\ns =", s)
s = {'a', 'b', 'c', 'd'}
print("s = {'a', 'b', 'c', 'd'} =>", s)


# 不可变集合
print('\n')
print('>>>>>>>>不可变集合:')
t = frozenset('bookshop')
print("t = frozenset('bookshop') =>", t)


print('\n')
print('>>>>>>>>set操作:')
albums = {'Poe', 'Gaudi', 'Freud', 'Poe2'}
print(type(sorted(albums)))
print(type(reversed(list(albums))))
print(type(enumerate(albums)))
# print(type(zip(range(len(albums)), albums))

print('>>>zip方式输出:')
for k, v in zip(range(len(albums)), albums):
    print(k, v)

print('>>>sorted输出:')
for v in sorted(albums):
    print('sorted =>', v)

print('>>>enumerate输出:')
for v in enumerate(albums):                        # v 其实就是一个元组,里面有两个元素,第一个是编号，第二个是value值
    print('enumerate =>', v[0], v[1])



