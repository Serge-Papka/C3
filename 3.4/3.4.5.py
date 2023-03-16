# Дан файл numbers.txt, компоненты которого являются действительными числами (файл создайте самостоятельно и заполните
# любыми числами, в одной строке одно число). Найдите сумму наибольшего и наименьшего из значений и запишите результат
# в файл output.txt. C:\Users\user\PycharmProjects\pythonProject3.8 b1.6

with open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\numbers.txt', 'r',
          encoding='utf8') as output_t:
    min_ = max_ = int(output_t.readline())
    for i in output_t:
        if min_ > int(i):
            min_ = int(i)
        if max_ < int(i):
            max_ = int(i)
input_t = open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt',
               'w', encoding='utf8')
print(min_)
print(max_)
print((str(min_+max_),'Сумма'))
input_t.write(str(min_+max_))


    # with open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\second\\input.txt', 'w',
    #           encoding='utf8') as input_t:
