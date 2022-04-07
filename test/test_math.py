from python_template.math.counting_primes import counting_primes
from python_template.math.rep_pow import rep_pow
from python_template.math.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_counting_primes():
    n = 10
    assert counting_primes(n) == 4
    n = 100
    assert counting_primes(n) == 25

def test_rep_pow():
    n, m, p = (12, 7, 15)
    assert rep_pow(n, m, p) == 3
    n, m, p = (123456789, 6574837563712, 234567894)
    assert rep_pow(n, m, p) == 120678297

def test_sieve_of_eratosthenes():
    n = 7
    assert sieve_of_eratosthenes(n) == [False, False, True, True, False, True, False, True]
    assert sieve_of_eratosthenes(n, return_num=True) == [2, 3, 5, 7]

def test_prime_factorize():
    
