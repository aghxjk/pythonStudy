import time
'''
    无参装饰器示例
'''


def runtime(function):
    def get_now_time():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        function()

    return get_now_time


@runtime
def run():
    print('run')
    print('-' * 20)


run()


'''
    带参装饰器示例-1
'''


def runtime_1(func):
    def get_now_time(*args):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(*args)

    return get_now_time


@runtime_1
def run1(i):
    print(i)
    print('-' * 20)


run1(100)


'''
    带参装饰器示例-2
'''


def runtime_2(func):
    def get_now_time(**kwargs):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(**kwargs)

    return get_now_time


@runtime_2
def run2(a):
    print(a)
    print('-' * 20)


run2(a='hahah')


'''
    带参装饰器示例-3
'''


def runtime_3(func):
    def get_now_time(name, **kwargs):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(name, **kwargs)

    return get_now_time


@runtime_3
def run3(name, **kwargs):
    print('{0}, {1}'.format(name, kwargs['a']))
    print('-' * 20)


run3("hahah", a='ccc')



