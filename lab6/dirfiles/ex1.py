import os

path = r'C:\Users\beiba\OneDrive\Рабочий стол\кодинг'

# List only directories
print("List of Directories:")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

# List only files
print("\nList of Files:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

# List all directories and files
print("\nList of Directories and Files:")
for item in os.listdir(path):
    print(item)