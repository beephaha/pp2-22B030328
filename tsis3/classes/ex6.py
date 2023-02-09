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

my_list = [1,2,3,4,5,6,7,8,9,10,11]

ura_last_task = filter(lambda x: is_prime(x), my_list)
print(list(ura_last_task))