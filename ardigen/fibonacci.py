"""
Write a program that prints the Fibonacci numbers from n to m (inclusive).
Requirements
● for each value print corresponding fibonacci number
● 1 <= n < m <= 250
● optimal time complexity
Input
Two numbers in two lines (n, m)

Output
One result per line according to requirements

Example
Sample input:
20
25
Sample output:
6765
10946
17711
28657
46368
75025
"""
from math import sqrt

from ardigen.utils import split_numbers


def get_nth_fib(n: int) -> int:
    # Using Binet's formula to find the nth Fibonacci number
    # i.e. phi to the nth minus its conjugate to the nth
    # over sqrt of five
    # https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression

    phi = (1 + sqrt(5)) / 2
    phi_conjugate = (1 - sqrt(5)) / 2

    nth_fib = ((phi**n) - (phi_conjugate**n)) / sqrt(5)

    return round(nth_fib)


def nth_to_mth_fib(numbers: str) -> str:
    n, m = split_numbers(numbers)

    if (1 <= n and n < m and m <= 250) == False:
        raise ValueError(
            "N must be greater or equal to 1 and greater than M. "
            "And M must be less or equal to 250"
        )

    int_list = [get_nth_fib(number) for number in range(n, m + 1)]

    str_list = map(str, int_list)

    return "\n".join(str_list)
