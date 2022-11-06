"""
Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number
"""


def what_sign(n):
    if n > 0:
        return "Positive"
    if n == 0:
        return "Zero"
    return "Negative"


def test_what_sign():
    assert what_sign(3) == "Positive"
    assert what_sign(0) == "Zero"
    assert what_sign(-3) == "Negative"


"""
Write a program that prints the integers from 1 to 100.

But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


"""
Write a function which removes one or more indicies from a list.

For example given the list:
["John", "Bob", "Charles", "Trev"]
and the indices:
[1, 2]
the resulting list will be:
["John", "Trev"]
"""


def remove_indices(mylist, idxs):
    return [j for i, j in enumerate(mylist) if i not in idxs]


def test_remove_indices():
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [0]) == [
        "Bob",
        "Charles",
        "Trev",
    ]
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2]) == [
        "John",
        "Trev",
    ]


""""
Modify connect to handle failed connections
"""
import random


def open_connection():
    if random.randint(0, 3) != 0:
        raise ValueError("failed to connect")
    return True


def connect():
    # Your code to handle bad connection goes here
    # You might need to modify the arguments passed to connect() such as
    # how many times the caller wants to try to make a connection before
    # giving up.
    while True:
        try:
            return open_connection()
        except ValueError:
            continue


def test_connect():
    for _i in range(100):
        assert connect()
