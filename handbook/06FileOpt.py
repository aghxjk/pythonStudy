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
