def primes(list):
    prime = [] 
    for i in range(len(list)):
        if list[i] == 2 or list[i] == 3:
            prime.append(list[i])
        elif list[i] % 3 != 0 and list[i] % 2 != 0 and list[i] != 1:
            prime.append(list[i])
    return prime
list = [1, 2, 3, 49, 53, 61, 77, 8, 9, 11]
print(primes(list))