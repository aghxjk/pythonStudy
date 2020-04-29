class Student:

    name = '可乐'

    # 实例方法
    def eat(self):
        print("会吃饭")

    # 类方法
    @classmethod
    def study(cls):
        print(cls.name + '会学习')

    # 静态方法
    @staticmethod
    def run():
        print('running...')

    # 私有方法
    def __kaoShi(self):
        print('会考试')


Student.study()
Student.run()
s = Student()
# 私有方法也可以被调用,只是私有方法被解释器增了_ClassName前缀
s._Student__kaoShi()

