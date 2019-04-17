#################################################
#   数据结构与算法
#################################################
import json
from collections import deque, defaultdict, OrderedDict, Counter
import heapq
from operator import itemgetter, attrgetter
from itertools import groupby


##################################################
# deque双向队列
#   1. deque在添加数据时,如果空间已满会把老的数据替换掉
#   2. deque可以两端添加和删除元素
##################################################

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


# Example use on a file
def deque_test():
    with open(r'/Users/zhaoyimeng/Downloads/test.py') as f:
        for line, prevlines in search(f, 'n', 5):
            for pline in prevlines:
                print(pline, end='')

            print(line, end='')
            print('-' * 20)


##################################################
# heapq提供了一个堆队列实现算法
# 1. heapq从一个集合中最大或最小的N个元素列表
# 2. 最小值总是保存在0点
##################################################

def heapq_test():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'APL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YAHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    # 查找最小的三个值
    cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
    # 查找最大的三个值
    expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

    print(cheap)
    print(expensive)

    print("-" * 10)
    for item in portfolio:
        print(item['name'] + ":price" + str(item['price']))
    print("-" * 10)


##################################################
# heapq.heapify 列表堆化处理
##################################################
def heapify_test():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)

    for item in nums:
        print(item)

    heapq.heappush(nums, -8)
    # heap的数据结构特征,heap[0]永远是最小的元素,通过下面代码获取
    print('获取最小的一个元素:')
    print('-' * 5)
    print(heapq.heappop(nums))


def min_test():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    minvalue = min(portfolio, key=lambda s:s['price'])
    print(minvalue)


##################################################
# 优先级队列
# 1.heappop始终弹出最小的一个元素
# 2.priority设置为负值是为了保证最大的优先级最小
# 3.之所以要增加一个index是为了避免priority和item相等时,无法比较大小
##################################################
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __len__(self):
        return len(self._queue)


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # 使用惊叹号！后接a 、r、 s，声明 是使用何种模式， ASCII模式、引用__repr__ 或 __str__
        return 'Item({!r})'.format(self.name)

    def __str__(self):
        return self.name


def priority_queue_test():
    pqueue = PriorityQueue()
    pqueue.push(Item('foo'), 1)
    pqueue.push(Item('bar'), 5)
    pqueue.push(Item('spam'), 4)
    pqueue.push(Item('grok'), 1)

    for i in range(len(pqueue)):
        item = pqueue.pop()
        print(repr(item))


##################################################
# defaultdict应用示例
##################################################
def default_dict_test():
    dl = defaultdict(list)
    dl['a'].append(1)
    dl['a'].append(2)
    dl['b'].append(3)
    dl['b'].append(4)

    ds = defaultdict(set)
    ds['a'].add(1)
    ds['a'].add(2)
    ds['b'].add(3)
    ds['b'].add(4)

    for k in dl.keys():
        print("List: " + repr(dl[k]))

    for k in ds.keys():
        print("set:  " + repr(dl[k]))


##################################################
# OrderDict应用示例(有序字典)
#  1. 内涵维护这一个双向链表,是一个普通字典的两倍
##################################################
def order_dict_test():
    od = OrderedDict()
    od['foo1'] = 1
    od['foo2'] = 2
    od['foo3'] = 3
    od['foo4'] = 4

    for k in od:
        print(k, ":", od[k])

    print(json.dumps(od))


##################################################
#  删除序列相同的元素并保持顺序
##################################################
def de_dupe(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
        seen.add(value)


def de_dupe_test():
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

    res = list(de_dupe(a, key=lambda d: (d['x'], d['y'])))
    print(res)


##################################################
#  命名切片(slice)
##################################################
def slice_test():
    record = '....................101 .......513.25 .........'
    count = slice(20, 23)
    price = slice(31, 37)
    cost = int(record[count]) * float(record[price])
    print("your cost is:", str(cost))

    s = slice(5, 50, 2)
    string = 'HelloWorld'
    s.indices(len(string))
    print(string[s])

##################################################
#  collections.Counter
#  1. 序列中出现次数最多的元素
##################################################
def collection_counter_test():
    words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
            ]

    more_words = ['why','are','you','not','looking','in','my','eyes']

    word_counts = Counter(words)
    more_counts = Counter(more_words)
    all = word_counts + more_counts
    top_three = word_counts.most_common(3)
    print(top_three)
    print("eyes:", word_counts['eyes'])
    print("eyes:", all['eyes'])


##################################################
#  operator.itemgetter
#  1. 通过某个关键字排序一个字典
#  2. itemgetter支持多个keys排序
#  3. itemgetter比lambda方式要快些
#  4.
##################################################
def itemgetter_test():
    rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

    for item in rows_by_fname:
        print('rows_by_fname:', item)

    for item in rows_by_uid:
        print('rows_by_uid:', item)

    print('-'*20)
    rs = sorted(rows, key=lambda d: d['uid'])
    for item in rs:
        print(item)



##################################################
#  operator.attrgetter
#  1. 对象排序
#  2. attrgetter比lambda方式要快些
##################################################
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def user_test():
    users = [User(23), User(3), User(99)]
    s1 = sorted(users, key=lambda u: u.user_id)

    for u in s1:
        print(u)

    print('-'*20)
    s2 = sorted(users, key=attrgetter('user_id'))
    for u in s2:
        print(repr(u))



##################################################
#  itertools.groupby
#  1. 按字段将记录分组
#  2. 注意:
#     在使用groupby之前,一个重要的准备步骤就是要跟进指定
#  字段将数据排序。groupby仅仅检查连续的元素,如果没有排序
#  将得不到想要的结果.
##################################################
def groupby_test():
    rows = [{'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}]

    # 排序过程不可少
    rows.sort(key=itemgetter('date'))

    for date, items in groupby(rows, key=itemgetter('date')):
        print("date: ", date)
        for item in items:
            print(item)

        print("-"*20)


##################################################
#  过滤序列元素(filter)
#  1. 方式1:
#       列表推导一个潜在缺陷是会产生一个非常大的结果集,
#   占用大量内存.
#  2. 方式2:
#       生成器表达式迭代产生过滤的元素,不会占用内存
#  3. 方式3:
#       filter()函数创建了一个迭代器,可以通过list转换为列表
##################################################
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def filter_test():
    my_list = [1, 4, -5, 10, -7, 2, 3, -1]

    # 列表推导
    list1 = [n for n in my_list if n > 0]
    print(type(list1))
    print(list1)

    print('-' * 20)
    # 生成器表达式
    list2 = (n for n in my_list if n > 0)
    print(type(list2))
    print(list2)

    print('-' * 20)
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    ivals = list(filter(is_int, values))
    print(ivals)


if __name__ == '__main__':
    # deque_test()
    # heapq_test()
    # heapify_test()
    # min_test()
    # priority_queue_test()
    # default_dict_test()
    # order_dict_test()
    # de_dupe_test()
    # slice_test()
    # collection_counter_test()
    # itemgetter_test()
    # user_test()
    # groupby_test()
    filter_test()










