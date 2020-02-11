# encoding:utf-8
__author__ = 'zhaoyimeng'

import re


##################################
#    列表常量 和 操作
##################################

print(">>>>>>>>初始化:")
dictNull = {}                                # 空字典
print("dictNull =", dictNull)
dict1 = {'apple': 2, 'orange': [0, 1]}       # 嵌套
print("dict1 = {'apple': 2, 'orange': [0, 1]} =>", dict1)

print('\n')
print(">>>>>>>>其它构造技术:")
dict2 = dict.fromkeys(['a', 'b'], 'zzz')
print("dict.fromkeys(['a', 'b'], 'zzz') =>", dict2)
dict3 = dict(zip(['a', 'b', 'c'], [0, 1, 3]))  # zip得到2维元组列表,然后再生成字典
print("dict(zip(['a', 'b', 'c'], [0, 1, 3])) =>", dict3)

print('\n')
print('>>>>>>>>常用基本操作:')
print("'a' in dict3 =>", 'a' in dict3)                 # 键存在测试
print('dict3.keys() =>', dict3.keys())               # 获取键组成列表
print('dict3.values() => ', dict3.values())             # 获取值
print('dict3.items() =>', dict3.items())              # 键-值

dict4 = dict3.copy()                             # 副本
print("dict3.copy() =>", dict4)
print("dict4.get('a', 'null') =>", dict4.get('a', 'null'))  # 获取a的值，，如果a不存在设置缺省值null
dict4['a'] = '1'
print("dict4['a'] = '1' =>", dict4)
print("dict1 =", dict1)
dict1 = {'a': 3}
print("dict1 = {'a': 3} =>", dict1)
dict4.update(dict1)                           # 字典合并
print("dict4.update(dict1) =>", dict4)
del dict4['a']                                # 删除指定元素
print("del dict4['a'] =>", dict4)
print("字典视图: list(dict4) =>", list(dict4))  # 字典视图，字典的key组成的列表


print('\n')
print(">>>>>>>>迭代初始化:")
dict5_1 = {x: y for (x, y) in zip(range(10), [chr(i) for i in range(97, 107)])}
print(dict5_1)

dict5_2 = dict(zip(range(10), [chr(i) for i in range(97, 107)]))
print(dict5_2)


print('\n')
print(">>>>迭代小技巧:")
# 将json串处理为dict
st = '{"username":3261233,"orderNo":143885491,"success":true,"time":3}'
dict6 = {x.replace('"', ''): y for (x, y) in zip(re.split('":|\{|\}|,', st)[1:-1:2], re.split('":|\{|\}|,', st)[2:-1:2])}
print('Json to Dict: dict6 =', dict6)


print('\n')
print(">>>>>>>>字典遍历:")
for x, y in dict6.items():
    print(x, y)


print('\n')
print(">>>>>>>>字典排序处理:")
for k in sorted(dict6.keys()):
    print(k, dict6[k])


print('\n')
print(">>>>>>>>字典格式化处理:")
dicFormat1 = '%(n)d and %(s)s' % {'n': 1, 's': 'spam'}               # 字典格式化为字符串
dicFormat2 = '{0[n]} and {0[s]} and {1[t]}'.format({'n': 1, 's': 'spam'}, {'t': 'ttt'})     # 字典格式化为字符串
print(dicFormat1)
print(dicFormat2)
print('-' * 20)

# 一个字典实现的用户登录示例
db = {}


def new_user():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another:'
            continue
        else:
            break

    pwd = input('passwd:')
    db[name] = pwd


def old_user():
    name = input('login:')
    pwd = input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print('welcome back', name)
    else:
        print('login incorrect')


def show_menu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Example Dictionary Example (continued)

    Enter choice: """

    done = False

    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            print('\n You picked:[%s]' % choice)
            if choice not in 'neq':
                print('invalid option, try again')
            elif choice == 'q':
                done = True
                break
            else:
                chosen = True
                done = True

            new_user()
            old_user()


if __name__ == '__main__':
    # show_menu()
    help({})
    # pass
