f = open('test.txt', 'r', encoding='utf8')

print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string

f.close()