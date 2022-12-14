from pytest import mark, raises

from ardigen import nth_to_mth_fib


@mark.parametrize(
    "expected_input, expected_output",
    [
        ("1\n2", "1\n1"),
        ("20\n25", "6765\n10946\n17711\n28657\n46368\n75025"),
        ("2\n6", "1\n2\n3\n5\n8"),
    ],
)
def test_nth_to_mth_fib(expected_input, expected_output):
    assert nth_to_mth_fib(expected_input) == expected_output


@mark.parametrize(
    "incorrect_input, expected_error",
    [
        ("2\n1", ValueError),
        ("-1\n-3", ValueError),
        ("400\n4000", ValueError),
    ],
)
def test_incorrect_nth_to_mth_fib(incorrect_input, expected_error):
    with raises(expected_error):
        nth_to_mth_fib(incorrect_input)
