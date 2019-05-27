#encoding: utf-8
__author__ = 'zhaoyimeng'

print('>>>>>>>>初始化操作:')
tpNull = ()                                 # 空元组
print('tpNull = () =>', tpNull)
tp0 = (0,)                                  # 单个元素元组, 注意： (0) 与 (0,)的区别
print('tp0 = (0,) =>', tp0)
tp1 = (1, 2, 3, 'a')                        # 四个元素元组
print("tp1 = (1, 2, 3, 'a') =>", tp1)
tp2 = 'a', 'b', 'c', 'd'                    # 另一个四元素元组
print("tp2 = 'a', 'b', 'c', 'd' =>", tp2)
tp3 = tuple('abcd1')                        # 可迭代对象的项的元组
print("tp3 = tuple('abcd1')  =>", tp3)
tp4 = tp3[0::2]                             # 索引与切片
print("tp4 = tp3[0::2] =>", tp4)
print("len(tp4) =>", len(tp4))
merge0 = tp1 + tp2                          # 元组合并, 项可重复
print("merge0 = tp1 + tp2 =>", merge0)
merge1 = tuple(set(merge0))                 # 去掉元组中重复的元素
print('merge1 = tuple(set(merge)) =>', merge1, '    # 去掉元组中重复的元素')


print('\n')
print('>>>>>>>>基本操作:')
for x, y in zip(range(len(tp2)), tp2):
    print(x, y)

print('tp2 =', tp2)
print("'a' in tp2 =>", 'a' in tp2)                      # 判断item是否存在

try:
    print("tp2.index('b') =>", tp2.index('b'))          # item的索引
    print(tp2.index('f'))
except ValueError:
    print("tp2.index('f') => ValueError: 未找到对应的值.")

print("merge0.count('a') =>", merge0.count('a'))         # 统计a的个数
print('dir(merge0) =>', dir(merge0))                                       # 显示对象的属性

print('\n')
print('>>>>>>>>元组帮助手册:help(())')
help(())                                    # 查看元组对象支持的操作

print('\n')
print('>>>>>>>>元组帮助手册:help(().index)')
help(().index)



