#!/usr/bin/bash python3

from calculator_1 import add
if __name__ == "__main__":
    a = 10
    b = 5
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

from calculator_1 import sub
if __name__ == "__main__":
    a = 10
    b = 5
    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result))

from calculator_1 import mul
if __name__ == "__main__":
    a = 10
    b = 5
    result = mul(a, b)
    print("{} x {} = {}".format(a, b, result))

from calculator_1 import div
if __name__ == "__main__":
    a = 10
    b = 5
    result = add(a, b)
    print("{} / {} = {}".format(a, b, result))
