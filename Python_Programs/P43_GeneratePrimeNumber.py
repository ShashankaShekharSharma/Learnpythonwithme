def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes

print(generate_primes(100))
