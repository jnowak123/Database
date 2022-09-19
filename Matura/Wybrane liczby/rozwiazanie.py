def isprime(num):
    if num == 1:
        return True
    for x in range(2, num//2 +1):
        if num % x == 0:
            return False
    return True


with open("liczby_przyklad.txt") as nums:
    for num in nums:
        num = int(num.strip())
        if isprime(num) and num > 100 and num < 5000:
            print(num)

with open("pierwsze_przyklad.txt") as primes:   
    for prime in primes:
        revprime = int(str(prime.strip())[::-1])
        if isprime(revprime):
            print(str(revprime)[::-1])

with open("pierwsze_przyklad.txt") as primes:
    count = 0        
    for prime in primes:
        prime = list(map(int, list(prime.strip())))
        while len(prime) != 1:
            prime = list(map(int, list(str(sum(prime)))))
        if prime == [1]:
            count += 1
        
    print(count)
