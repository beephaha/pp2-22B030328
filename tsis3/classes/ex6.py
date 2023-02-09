def is_prime(k):
    if k == 1:
        return False
    if k > 1:
        for j in range(2, int(k/2)+1):
            if (k % j) == 0:
                return False
        return True
    else:
        return True

my_list = [1,2,3,4,5,6,7,8,9,10,11]

nonprime = filter(lambda x: is_prime(x), my_list)
print(list(nonprime))