import time
'''
    无参装饰器示例
'''


def runtime(function):
    def get_now_time():
        print(time.time())
        function()

    return get_now_time


@runtime
def run():
    print('run')


run()


'''
    带参装饰器示例-1
'''


def runtime_1(func):
    def get_now_time(*args):
        print(time.time())
        func(*args)

    return get_now_time


@runtime_1
def run1(i):
    print(i)


run1(100)


'''
    带参装饰器示例-2
'''


def runtime_2(func):
    def get_now_time(**kwargs):
        print(time.time())
        func(**kwargs)

    return get_now_time


@runtime_2
def run2(a):
    print(a)


run2(a='hahah')


'''
    带参装饰器示例-3
'''


def runtime_3(func):
    def get_now_time(name, **kwargs):
        print(time.time())
        func(name, **kwargs)

    return get_now_time


@runtime_3
def run3(name, **kwargs):
    print('{0}, {1}'.format(name, kwargs['a']))


run3("hahah", a='ccc')



