"""
Write a program that prints the integers from n to m (inclusive).
Requirements
● for multiples of three, print Fizz (instead of the number)
● for multiples of five, print Buzz (instead of the number)
● for multiples of both three and five, print FizzBuzz (instead of the number)
● 1 <= n < m <= 10000
Input
Two numbers in two lines (n, m)
Output
One result per line including requirements
Example
Sample input:
7
16
Sample output:
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

from ardigen.utils import split_numbers


def fizzbuzz(numbers: str) -> str:

    n, m = split_numbers(numbers)

    if (1 <= n and n < m and m <= 10000) == False:
        raise ValueError(
            "N must be greater or equal to 1 and greater than M. "
            "And M must be less or equal to 10000"
        )

    output = []
    for i in range(n, m + 1):
        curr_output = "Fizz" if i % 3 == 0 else ""
        curr_output += "Buzz" if i % 5 == 0 else ""
        output.append(str(i) if curr_output == "" else curr_output)

    return "\n".join(output)
