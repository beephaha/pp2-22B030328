file_path = r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text.txt"
line_count = 0

with open(file_path, 'r') as file:
    for line in file:
        line_count += 1

print("The file", file_path, "contains", line_count, "lines.")