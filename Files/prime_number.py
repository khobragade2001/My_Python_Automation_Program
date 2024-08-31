def prime_num(x):
    primes = []
    
    for num in range(2,x+1):
        number = True
        for i in range(2,num):
            if num % i == 0:
                number = False
                break
        if number:
            primes.append(num)
    return primes

x = int(input("Enter a number :"))
output = prime_num(x)
print(f'prime number up to {x} :{output}')