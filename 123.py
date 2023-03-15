import os
print(os.getcwd()) # C:\Users\user\PycharmProjects\pythonProject3.8 b1.6\C3\3.3.7
start_path = os.getcwd()
# print(start_path)
# os.chdir("..")
# os.chdir("..")
# os.chdir("..")
# os.chdir("..")
# os.chdir("..")
# os.chdir("..")
# os.chdir("..")
# print(os.getcwd())
# os.chdir(start_path)
# print(os.getcwd())
# print(os.listdir())

# print(start_path)
# print(os.path.join(start_path, 'test'))
# print(os)
tree = "C:\\Users\\user\\"
tree = os.walk("SeaFight")

# print(tree)

for i in tree:
    print(i)



