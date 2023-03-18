# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
# В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к файлу, который надо открыть,
# второй — тип открываемого файла (для записи, для чтения и т. д.).
# При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
# При выходе из контекстного менеджера файл должен закрываться. (Эталоном работы можно считать контекстный менеджер open).


class open_f:
    def __init__(self, path, metod):
        # self.path = path
        # self.metod = metod
        self.f = open(path, metod, encoding='utf8')

    def __enter__(self):

        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

with open_f('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\output.txt',"r") as dd:
    for i in dd:
        print(i, end='')
    # print(dd)



