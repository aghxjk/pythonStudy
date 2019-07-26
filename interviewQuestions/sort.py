'''
常见排序算法：
1. 插入排序
2. 希尔排序
3. 直接排序
4. 堆排序
5. 冒泡排序  -面试重点
6. 快速排序  -面试重点
7. 归并排序
8. 基数排序

阿里面试题:
    给定列表进行排序,要求: 时间复杂度小于O(n^2)

复杂度
1. 空间复杂度
2. 时间复杂度

常见时间复杂度:
常数阶: O(1)
对数阶: O(log2n)
线性阶: O(n)
线性对数阶: O(nlog2n)
平方阶: O(n^2)
立方阶: O(n^3)
'''

# 冒泡排序: O(n^2)


def bubble_sort(blist):
    count = len(blist)
    if len(blist) < 2:
        return blist

    for i in range(0, count):
        for j in range(i+1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist


list_to_sort = [1, 3, 9, 0, 2, 4, 5, 6]
bubble_sort(list_to_sort)
print(list_to_sort)

# 快排排序O(nlog2n)
# 步骤：
# 1. 列表中取第一个元素作为标准
# 2. 把比第一个元素小的都放左侧
# 3. 把比第一个元素大的都放右侧
# 4. 递归完成,排序结束

def quick_sort(qlist):
    if len(qlist) < 2:
        return qlist
    else:
        first = qlist[0]
        less = quick_sort([l for l in qlist[1:] if l < first])
        more = quick_sort([m for m in qlist[1:] if m >= first ])
        return less + [first] + more

list_to_sort = [1, 3, 9, 0, 2, 4, 5, 6, 10, 8, 99]
quick_sort(list_to_sort)
print(quick_sort(list_to_sort))