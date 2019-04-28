#encoding: utf-8
import sys

__author__ = 'zhaoyimeng'
##################################
#    基础理论: 一切皆对象 & 动态类型
##################################
a = 1
b = 1

print(hex(id(a)))            # 内置函数: id(object) 返回对象的内存地址
print(hex(id(b)))
print(hex(id(1)))
print(a is b)               # 关键字is用于判断两个引用所指的对象是否相同
print('-' * 24)

str_1 = 'helloworldaaaa'
str_2 = str_1

print('引用次数: {0}'.format(sys.getrefcount(str_2)))
print(str_1 is str_2)
print(str_1 == str_2)
print('-' * 24)

print(dir(1))

print('-' * 24)
tt = [1, 2]
mm = [1, 2]

print('"tt == mm" is {0}'.format(tt == mm))
print('"tt is mm" is {0}'.format(tt is mm))

##################################
#    字符串常量 和 表达式基本操作
##################################

str1 = ''                                      # 空字符串
str2 = "Hello Tom's cat"                       # 双引号与单引号
str3 = u"abc"                                  # Unicode编码
strRaw = r'C:\new\test.txt'                    # 字符串不会被转义,否则输出时会被转义为换行符和制表符
print('>>>>字符串合并操作:')
print('strRaw = {0}'.format(strRaw))
strMerge = str2 + " : " + str3                 # 字符串合并
print('str1 + str2 = {0}'.format(strMerge))

print('-' * 24)
print('>>>> 字符串截取 & 长度计算操作:')
str4 = strMerge[0:-1:1]                        # 字符串截取：Tom's cat : ab
str5 = strMerge[0:-1:2]                        # 字符串截取：Tmsct:a

strLen = len(strMerge)                         # 求字符串长度
print('str4 = ' + str4)
print('str5 = ' + str5)
print('lenth of strMerge = {0}'.format(strLen))

print('-' * 24)
print('>>>> 字符串格式化输出操作:')
strFormat1 = "begin %s end" % str2             # 字符串格式化
strFormat2 = "begin {0} end".format(str2)      # 字符串格式化
print('strFormat1 = {0}'.format(strFormat1))
print('strFormat2 = {0}'.format(strFormat2))

# 下面的格式化方法要比用%这种方式有优势
print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
print('My {conf[spam]} runs {sys.platform}'.format(sys=sys, conf={'spam': 'laptop'}))


print('-' * 24)
print('>>>> 字符其它操作:')
strFind = strMerge.find('Tom')                 # 字符串查找，返回查找字符串的最新索引
print('strFind = {0}'.format(strFind))

strStrip = str2.replace(' ', ':')              # 字符串替换
print('strStrip = {0}'.format(strStrip))

strSplit = str2.split()                        # 字符串分隔
print('strSplit = {0}'.format(strSplit))

strNumTest = str2.isdigit()                    # 字符串是否为数字,返回:True or False
print('strNumTest = {0}'.format(strNumTest))

strLower = str2.lower()                        # 字符串大小写切换
print('strLower = {0}'.format(strLower))

strEndTest = str2.endswith('cat')              # 结束测试,返回:True or False
print('strEndTest = {0}'.format(strEndTest))

strStartTest = str2.startswith('Tom')          # 开始测试,返回:True or False
print('strStartTest = {0}'.format(strStartTest))

strJoin = '-'.join(str3)                       # 插入分隔符
print('strJoin = {0}'.format(strJoin))

strEncode = str3.encode('utf-8')               # 字符编码
print('strEncode = {0}'.format(strEncode))

str2int = int('123')                           # 字符串转换成数值
int2str = str(123)                             # 数值转换成字符串
str2float = float('1.5')                       # 数值转换成字符串
int2Ascii = chr(97)                            # 数值转换成ASCII
Ascii2int = ord('a')                           # ASCII转换成int

isInStr = 'Tom' in str2                        # 判断str2中是否包含'Tom'字符串,isInStr = true or false
print('isInStr = {0}'.format(isInStr))

print([c * 2 for c in str3])                 # 迭代操作
print(map(ord, str3))                        # ASCII转换成对应的字符编码

template = 'hello: {name}, welcome to {city}'  # 字符串模板与格式化
tmp = template.format(name='Chris', city='Beijing')
print(tmp)


# 总结
# 1.Python没有像C语言那样的单个字符这种类型,取而代之的是单个字符的字符串;
# 2.Python中的字符串(str)被划分为不可变序列,即字符串不可在原处修改;
# 3.单引号 与 双引号二者等效,而且单引号中可以嵌套双引号 或 双引号中嵌套单引号;
# 4.三重引号可以编写多行字符串;

# 备注:
# 1.动态类型概念: Python是一个动态类型的语言,而且最大的特点就是对象型语言.
# 即:Python所有的数据基本都以对象存在,且每一个对象都标识了自己的类型;
