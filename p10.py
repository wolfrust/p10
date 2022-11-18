def is_prime(n):
    if n <=3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
    
"""
1-10 4 0.4444444444444444
10-100 21 0.23333333333333334
100-1000 143 0.15888888888888889
1000-10000 1061 0.11788888888888889
10000-100000 8363 0.09292222222222223
100000-1000000 68906 0.07656222222222223
1000000-10000000 586081 0.06512011111111111
10000000-100000000 5096876 0.05663195555555556
100000000-1000000000 45086079 0.050095643333333335
"""

for i in range(9, 12):
    primes = []
    for x in range(pow(10, i-1), pow(10, i)):
        if is_prime(x):
            primes.append(x)
    print(f'{pow(10, i-1)}-{pow(10, i)}', len(primes), len(primes)/(pow(10, i) - pow(10, i-1)))
    
