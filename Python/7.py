# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(num):
    prime_numbers = 0

    if num < 2:
        return prime_numbers
    
    for n in range(0, nums):
        if n % 2