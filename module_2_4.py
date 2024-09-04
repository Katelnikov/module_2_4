
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создайте пустые списки primes и not_primes.
primes = []
not_primes = []
#При помощи цикла for переберите список numbers.
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print('Primes:', primes)
print('not_primes:', not_primes)