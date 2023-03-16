# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
import os
# print(os.getcwd()) # C:\Users\user\PycharmProjects\pythonProject3.8 b1.6\C3\3.3.7
# os.chdir("..")
# list_= os.walk(os.getcwd())
# for i in list_:
#     print(i)#
# print(list_)
# C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first
# C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second

# output_t = open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\output.txt',
#          'r', encoding='utf8')  # открываем файл на чтение
# # print(output_t.readline())
# input_t = open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt',
#          'w', encoding='utf8')  # открываем файл на дозапись
# for i in output_t:
#     input_t.write(i)
# output_t.close()
# input_t.close()
with open('3.4/first/output.txt',
          "r", encoding='utf8') as output_t:
    with open('/C3/3.4\\second\\input.txt',
         'w', encoding='utf8') as input_t:
        for i in output_t:
            input_t.write(i)


