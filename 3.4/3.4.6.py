# # В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную. Выведите на экран всех
# # учащихся, чья оценка меньше 3 баллов. Cодержание файла:
# Иванов О. 4
# Петров И. 3
# Дмитриев Н. 2
# Смирнова О. 4
# Керченских В. 5
# Котов Д. 2
# Бирюкова Н. 1
# Данилов П. 3
# Аранских В. 5
# Лемонов Ю. 2
# Олегова К. 4

with open('C:\\Users\\user\\PycharmProjects\\pythonProject3.8 b1.6\\C3\\3.4\\first\\output.txt', 'r',
          encoding='utf8') as output_t:
    for line in output_t:
        print(line.split())
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)


