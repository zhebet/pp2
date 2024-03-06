def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True
    
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    
    return prime_numbers

x = input().split()

x = [int(num) for num in x]

prime_numbers = filter_prime(x)
print(prime_numbers)
