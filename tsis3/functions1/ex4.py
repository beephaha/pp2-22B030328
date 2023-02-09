def filter_prime(list):
    def is_prime(k):
        if k <= 1:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    primes=[]
    for j in range(len(list)):
        if is_prime(list[j]):
            primes.append(list[j])
    return primes
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(list))