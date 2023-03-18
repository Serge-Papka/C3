# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
import os

list_ = []
# with open("C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt","w",encoding='utf8'
#           ) as input_t:
#     with open("C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\output.txt","r",encoding='utf8'
#               ) as output_t:
#         for i in reversed(output_t.readlines()):
#             input_t.write(i)

# with open("C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt", "w",
#           encoding='utf8') as input_file:
#     with open("C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\output.txt", "r",
#               encoding='utf8') as output_file:
#         for line in reversed(.readlines()):
#                input_file.write(line)


    #     # list_.insert(0, i)
    #     list_.append(i)
    #     print(list_)
#
#
# print(list_)
# with open("C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt","w",encoding='utf8'
#           ) as input_t:
#     for i in  list_:
#         input_t.write((i))
# -----------------
with open('input.txt', 'r',encoding='utf8') as input_file:
   with open('output.txt', 'w',encoding='utf8') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)
