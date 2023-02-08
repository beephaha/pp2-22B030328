def unique(list):
    unique_list = []
    for i in range(len(list)):
        while unique_list.count(list[i]) == 0:
            unique_list.append(list[i])
    return unique_list

list = [1, 2, 1, 3, 4, 7]
list2 = ["we", "we", "are", "hello", "hello"]
print(unique(list))
print(unique(list2))
