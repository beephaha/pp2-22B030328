def multiply(list):
    product = 1
    for i in list:
        product = product * i
    return product

list = [1, 2, 3, 4, 5]

print(multiply(list))