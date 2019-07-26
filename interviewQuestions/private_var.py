class Student:
    __name = 'SanMao'   # 私有变量
    school = 'BeiDa'

print(Student.school)
# print(Student.__name)  会报错
print(Student._Student__name)  # 访问私有变量