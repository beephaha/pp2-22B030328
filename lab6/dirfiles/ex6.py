import os 

os.chdir(r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(alphabet)):
    os.mkdir(alphabet[i] + ".txt")