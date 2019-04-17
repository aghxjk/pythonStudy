import random
from decimal import Decimal, localcontext
from fractions import Fraction
from datetime import timedelta, datetime

#################################################
# 第三章: 数字日期和时间
#################################################
# 3.1 数字的四舍五入
#################################################


def rount_test():
    print('1.23 百分位四舍五入: ', round(1.23, 1))
    print('1.26 百分位四舍五入: ', round(1.26, 1))
    print('1.25331 千分位舍入: ', round(1.25331, 3))
    print('1.25361 千分位舍入: ', round(1.25361, 3))

    # 千位舍入
    print('1599 十位四舍五入: ', round(1530, -2))
    print('-' * 50)


#################################################
# 3.2 执行精确的浮点数运算
#################################################
def decimal_test():
    a1 = 4.2
    b1 = 2.1
    r1 = a1 + b1
    print('有误差的数学运算: 4.2 + 2.1 = ', r1)

    # 有性能损耗的精确运算
    a2 = Decimal('4.2')
    b2 = Decimal('2.1')
    r2 = a2 + b2
    print('无误差的数学运算: 4.2 + 2.1 = ', r2)
    print('-' * 50)

    a3 = Decimal('1.3')
    b3 = Decimal('1.7')
    r3 = a3 / b3
    print(a3, '/', b3, ' = ', r3)

    with localcontext() as ctx:
        ctx.prec = 3
        print('本地上下文中进行的运算: 1.3/1.7 = ', a3/b3)

    print('超出上下文后进行的运算: 1.3/1.7 = ', a3/b3)

    nums = [1.23, 1, -1.23]
    print('sum([1.23, 1, -1.23]) = ', sum(nums))
    nums = [1.23e+18, 1, -1.23e+18]
    print('sum([1.23e+18, 1, -1.23e+18]) = ', sum(nums))
    print('-' * 50)


#################################################
# 3.3 数字的格式化输出
#################################################
def number_format():
    x = 1234.56789
    print("format(1234.56789, '0.2f')) = ", format(x, '0.2f'), '2位精度')
    print("format(1234.56789, '>10.2f')) = ", format(x, '>10.2f'), '右对齐10位')
    print("format(1234.56789, '<10.2f')) = ", format(x, '<10.2f'), '左对齐10位')
    print("format(1234.56789, '^10.2f')) = ", format(x, '^10.2f'), '中间对齐')
    print("format(1234.56789, ',')) = ", format(x, ','), '千位分隔符')
    print("format(1234.56789, '0,.1f')) = ", format(x, '0,.1f'))
    print("format(1234.56789, 'e')) = ", format(x, 'e'))
    print("format(1234.56789, '0.2E')) = ", format(x, '0.2E'))
    print('-' * 50)


#################################################
# 3.4 二八十六进制整数
#################################################
def bin_oct_hex_test():
    x = 1234
    print('bin(1234) = ', bin(x))
    print('oct(1234) = ', oct(x))
    print('hex(1234) = ', hex(x))
    print('2**32 = ', format(-2**32 + x, 'b'))
    print('2**32 = ', format(-2**32 + x, 'x'))
    print('-' * 50)


#################################################
# 3.8 分数运算
#################################################
def fractions_test():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print('5/4 + 7/16 = ', a + b)
    print('-' * 50)


#################################################
# 3.11 随机选择
#################################################
def random_test():
    values = [1, 2, 3, 4, 5, 6]
    print('random.choice(1-6) = ', random.choice(values))
    print('random.choice(1-6) = ', random.choice(values))
    print('random.choice(1-6) = ', random.choice(values))
    print('random.choice(1-6) = ', random.choice(values))
    print('随机抽取多个不同样本:')
    print('random.sample(1-6) = ', random.sample(values, 2))
    print('random.sample(1-6) = ', random.sample(values, 2))
    print('打乱序列的顺序:')
    random.shuffle(values)
    print('random.shuffle(1-6) = ', values)
    random.shuffle(values)
    print('random.shuffle(1-6) = ', values)
    print('生成0-1范围内均匀分布的浮点数:')
    print('random.random() = ', random.random())
    print('获取N位随机位(二进制)的整数:')
    print('random.getrandbits(10) = ', random.getrandbits(10))
    print('-' * 50)


#################################################
# 3.11 基本的日期与时间转换
#################################################
def datetime_test():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print('天数输出:', c.days)
    print('除天数外的总秒数为:', c.seconds)
    print('除天数外的总分钟为:', c.seconds / 60)
    print('除天数外的总小时为:', c.seconds / 3600)
    print('总小时为:', c.total_seconds() / 3600)
    print('-' * 50)

    aa = datetime(2017, 8, 9)
    print('2017/08/09 + 25days = ', aa + timedelta(days=25))
    bb = datetime(2018, 4, 23)
    dd = bb - aa
    print('2017/08/09 - 2018/04/23 = ', dd)
    print('datetime.today() = ', datetime.today())
    print('自动处理闰年:')
    a1 = datetime(2012, 3, 1)
    a2 = datetime(2012, 2, 28)
    print('datetime会自动处理闰年:', (a-b).days)


if __name__ == '__main__':
    if None:
        rount_test()
        decimal_test()
        number_format()
        bin_oct_hex_test()
        fractions_test()
        random_test()
    else:
        datetime_test()

