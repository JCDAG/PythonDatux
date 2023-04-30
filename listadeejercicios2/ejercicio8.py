def primes_range(max_num, step=1):
    primes_list = []
    for num in range(2, max_num + 1, step):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(num)
    return primes_list
primes = primes_range(10**5)
print(primes)