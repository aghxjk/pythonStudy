#encoding: utf-8
#################################################
#    该代码文件为示例测试用，从阅读主文件moduleBasis.py
#################################################

__author__ = 'zhaoyimeng'

eg = [1]


def printer(): print('\n>>>>>>>> eg1模块printer(): {0}'.format(eg))


string = 'abcdefg'
enu = enumerate(string)
print('\n')
print('>>>>>>>> eg1模块内被执行的代码-1:')
for i in enu:
    print(i)


print('\n')
print('>>>>>>>> eg1模块内被执行的代码-2:')
str_reversed = reversed(string)
for i in str_reversed:
    print(i)


print('\n')
print('>>>>>>>> eg1模块内被执行的代码-3:')
i = -1
for i in range(-1, -len(string), -1):
    print("i = {0}   and   string = {1}".format(i, string[:i]))


