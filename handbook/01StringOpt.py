#encoding: utf-8
import sys

__author__ = 'zhaoyimeng'
##################################
#    基础理论: 一切皆对象 & 动态类型
##################################
print('>>>>>>>>数值对象:')
a = 1
b = 1
print("dir(1): {0}".format(dir(1)))             # 查看对象属性

print('hex(id(a)) : {0}'.format(hex(id(a))))    # 内置函数: id(object) 返回对象的内存地址
print('hex(id(b)) : {0}'.format(hex(id(b))))
print('hex(id(a)) : {0}'.format(hex(id(1))))
print('a is b : {0}'.format(a is b))            # 关键字is用于判断两个引用所指的对象是否相同
print('\n')


print('>>>>>>>>字符串对象:')
str_1 = 'helloworldaaaa'
str_2 = str_1

# 在IDE中，此处输出的值为5，跟IDE有关系。如果直接在Python命令行中输出，值是3
print('sys.getRefcount(str_2) = {0}'.format(sys.getrefcount(str_2)))
print('str_1 is str_2 : {0}'.format(str_1 is str_2))
print('str_1 == str_2 : {0}'.format(str_1 == str_2))
print('\n')


print('>>>>>>>>List对象:')
tt = [1, 2]
mm = [1, 2]
print('"tt == mm" is {0}'.format(tt == mm))
print('"tt is mm" is {0}'.format(tt is mm))
print('\n')

##################################
#    字符串常量 和 表达式基本操作
##################################

print('>>>>>>>>字符串操作:')
str1 = ''                                      # 空字符串
str2 = "Hello Tom's cat"                       # 双引号与单引号
str3 = u"abc"                                  # Unicode编码
strRaw = r'C:\new\test.txt'                    # 字符串不会被转义,否则输出时会被转义为换行符和制表符
print('strRaw = {0}'.format(strRaw))

strMerge = str2 + " : " + str3                 # 字符串合并
print('str1 + str2 = {0}'.format(strMerge))

print('\n')
print('>>>>>>>>字符串截取:')
print('strMerge = {0}'.format(strMerge))
str4 = strMerge[0:-1:1]                        # 字符串截取：Tom's cat : ab
str5 = strMerge[0:-1:2]                        # 字符串截取：Tmsct:a
print('strMerge[0:-1:1] = {0}'.format(str4))
print('strMerge[0:-1:2] = {0}'.format(str5))

print('\n')
print('>>>>>>>>字符串长度计算:')
strLen = len(strMerge)                         # 求字符串长度
print('len(strMerge) = {0}'.format(strLen))

print('\n')
print('>>>> 字符串格式化输出:')
strFormat1 = ">> %s <<" % str2             # 字符串格式化
strFormat2 = ">> {0} <<".format(str2)      # 字符串格式化
print('str2 = {0}'.format(str2))
print('">> %s  <<" % str2 = {0}'.format(strFormat1))
print('">> {0} <<".format(str2)' + ' = {0}'.format(strFormat2))

# 下面的格式化方法要比用%这种方式有优势
print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
print('My {conf[spam]} runs {sys.platform}'.format(sys=sys, conf={'spam': 'laptop'}))

print('\n')
print('>>>> 字符串模板:')
template = 'hello: {name}, welcome to {city}'  # 字符串模板与格式化
tmp = template.format(name='Chris', city='Beijing')
print(tmp)


print('\n')
print('>>>>>>>字符串函数:')
strFind = strMerge.find('Tom')                 # 字符串查找，返回查找字符串的最新索引
print("strMerge.find('Tom') = {0}".format(strFind))

strStrip = str2.replace(' ', ':')              # 字符串替换
print("str2.replace(' ', ':') = {0}".format(strStrip))

strSplit = str2.split()                        # 字符串分隔
print("str2.split() = {0}".format(strSplit))

strNumTest = str2.isdigit()                    # 字符串是否为数字,返回:True or False
print('str2.isdigit() = {0}'.format(strNumTest))

strLower = str2.lower()                        # 字符串大小写切换
print('str2.lower() = {0}'.format(strLower))

strEndTest = str2.endswith('cat')              # 结束测试,返回:True or False
print("str2.endswith('cat') = {0}".format(strEndTest))

strStartTest = str2.startswith('Tom')          # 开始测试,返回:True or False
print("str2.startswith('Tom') = {0}".format(strStartTest))

strJoin = '-'.join(str3)                       # 插入分隔符
print("'-'.join(str3) = {0}".format(strJoin))

strEncode = str3.encode('utf-8')               # 字符编码
print("str3.encode('utf-8') = {0}".format(strEncode))

print('\n')
print('>>>>>>>字符串类型转换:')
str2int = int('123')                           # 字符串转换成数值
print("int('123') = {0}".format(str2int))
int2str = str(123)                             # 数值转换成字符串
print("str(123) = {0}".format(int2str))
str2float = float('1.5')                       # 数值转换成字符串
print("float('1.5') = {0}".format(str2float))
int2Ascii = chr(97)                            # 数值转换成ASCII
print("chr(97) = {0}".format(int2Ascii))
Ascii2int = ord('a')                           # ASCII转换成int
print("ord('a') = {0}".format(Ascii2int))

print('\n')
print('>>>>>>>字符串包含判断:')
isInStr = 'Tom' in str2                        # 判断str2中是否包含'Tom'字符串,isInStr = true or false
print("'Tom' in str2 = {0}".format(isInStr))

print('\n')
print('>>>>>>>字符串迭代表达式:')
print([c * 2 for c in str3])                 # 迭代操作
tmp = map(ord, str3)

print('map(ord, str3))) = {0}'.format(list(tmp)))                       # ASCII转换成对应的字符编码

for i in tmp:
    print('i = {0}'.format(i))

print('map(ord, str3))) = {0}'.format(list(tmp)))                       # 注意该输出内容


##################################
#    字符串模式匹配
##################################
import re

print('\n')
print('>>>>>>>字符串模式匹配:')
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print('re.match(...) = {0}'.format(type(match)))
print('match.group(1) = {0}'.format(match.group(1)))
print('match.group(2) = {0}'.format(match.group(2)))
print('match.group(3) = {0}'.format(match.group(3)))
print('match.groups() = {0}'.format(match.groups()))


# 总结
# 1.Python没有像C语言那样的单个字符这种类型,取而代之的是单个字符的字符串;
# 2.Python中的字符串(str)被划分为不可变序列,即字符串不可在原处修改;
# 3.单引号 与 双引号二者等效,而且单引号中可以嵌套双引号 或 双引号中嵌套单引号;
# 4.三重引号可以编写多行字符串;

# 备注:
# 1.动态类型概念: Python是一个动态类型的语言,而且最大的特点就是对象型语言.
# 即:Python所有的数据基本都以对象存在,且每一个对象都标识了自己的类型;

# str的特定方法
"""
     1. str.find()                         未找到情况下返回 -1; 或返回传入子串的偏移量
     2. str.replace(old, new, count=-1)    count=-1默认对全局进行搜索和替换,也可通过count指定替换的次数
     3. str.split(',')                     按指定字符将字符串分割成字符串数组
     4. str.upper()                        返回一个转换为大写字符串的拷贝
     5. str.isalpha()                      判断一个字符串是否为纯字符
     6. str.rstrip()                       删除字符串右侧空格
     7. str.lstrip()                       删除字符串左侧空格
     8. str.strip()                        删除字符串左右两侧空格
     9. dir(str)                           显示Python对象相关调用方法和实现细节
     10. help(str.replace)                 查看字符串replace函数的使用方法
"""

