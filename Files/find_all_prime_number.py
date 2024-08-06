##Find All Prime Numbers up to a Given Number**
def primes_up_to(n):
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return [p for p in range(2, n + 1) if sieve[p]]

num = int(input("Enter a number up to prime number : "))
print(primes_up_to(num))