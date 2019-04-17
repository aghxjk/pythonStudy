#################################################
#   字符串和文本
#################################################
import re
import os
from fnmatch import fnmatch


#################################################
# 2.1 使用多个界定符分割字符串
#################################################


def re_split_test():
    line = 'asdf fjdk; afed, fjek,asdf, foo'

    # 正则介绍见:http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
    res = re.split(r'[;,\s]\s*', line)
    for v in res:
        print(v)

    # 使用括号捕获的分组,被匹配文本也将出现在结果列表中
    res1 = re.split(r'(;|,|\s)\s*', line)
    print(res1)

    # 获取所以分隔符
    print(res1[1::2])

    # 不想保留分隔符到结果串,但仍然需要使用括号分组正则表达式
    res2 = re.split(r'(?:;|,|\s)\s*', line)
    print(res2)


def ends_test():
    files = os.listdir('.')
    print([file for file in files if file.endswith(('.py', '.txt'))])
    print(any(name.endswith('.py') for name in files))


#################################################
# 2.2 使用shell通配符匹配字符串
#################################################
def fnmatch_test():
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Dat[0-9].csv')])


#################################################
# 2.3 re.sub()字符串替换
#################################################
def re_sub_test():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456"

    def match_case(words):
        #  此处的matched相当于获取被匹配的字符串对象
        def replace(matched):
            # group()获取被匹配字符串
            int_str = matched.group()
            res = words + "=" + int_str
            return res
        return replace

    replaced_str = re.sub("(\d+)", match_case('abc'), inputStr);
    print("replacedStr=", replaced_str)





if __name__ == "__main__":
    # re_split_test()
    # ends_test()
    # fnmatch_test()
    re_sub_test()
