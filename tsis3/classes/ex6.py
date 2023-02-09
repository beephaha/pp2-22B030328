def is_prime(num):
    if num == 1:
        return False
    if num > 1:
        for j in range(2, int(num/2)+1):
            if (num % j) == 0:
                return False
        return True
    else:
        return True

list = [1,2,3,4,5,6,7,8,9,10,11]

nonprime = filter(lambda x: is_prime(x), list)
print(list(nonprime))