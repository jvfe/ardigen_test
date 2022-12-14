from pytest import mark, raises

from ardigen import fizzbuzz


@mark.parametrize(
    "expected_input, expected_output",
    [
        ("7\n16", "7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16"),
        ("1\n5", "1\n2\nFizz\n4\nBuzz"),
    ],
)
def test_fizzbuzz(expected_input, expected_output):
    assert fizzbuzz(expected_input) == expected_output


@mark.parametrize(
    "incorrect_input, expected_error",
    [
        ("2\n1", ValueError),
        ("-1\n-3", ValueError),
        ("10000\n110000", ValueError),
    ],
)
def test_incorrect_fizzbuzz(incorrect_input, expected_error):
    with raises(expected_error):
        fizzbuzz(incorrect_input)
