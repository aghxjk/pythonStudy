import os

print(__file__)
current_path = os.path.abspath(__file__)
print(current_path)
# dir_path = os.path.dirname(current_path)
# print(dir_path)
data_path = os.path.dirname(os.path.dirname(current_path)) + '/tempDir'

if not os.path.exists(data_path):
    os.makedirs(data_path)


fileName = data_path + '/data.txt'
print('fileName = ', fileName)
file = open(fileName, 'w')
file.write('hello world 1\n')
file.write('hello world 2')
file.close()

file = open(fileName, 'r')
text = file.read()
print(text)
file.close()

# 最理想的读取文件方式
# 使用with语句,控制块结束时会自动化关闭文件句柄
# 内存管理/IO缓存管理自动实现,不用担心大文件问题
print('>>>>>>>> 理想的读取文件方式:')
with open(fileName, 'r', buffering=4096, encoding='utf-8') as linesBuffer:
    for line in linesBuffer:
        print(line, end='')

####################################################
#                    File 说明                      #
####################################################
'''
    .read()         每次读取整个文件,不适合大文件,尤其是文件大于内存情况;     -> 效率最高,但是功能简约
    .read(size)     为了避免内存溢出,可以指定每次读取文件的大小;
    .readline()     每次读取一行,只需要很少的内存;                        -> 效率最低,但内存最节省
    .readlines()    一次读完文件所有行,并放在list中,内存不足无法使用该方式;   -> 效率中等,内存高耗型
'''

