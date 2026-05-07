#!/usr/bin/env python3

def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)

    number = 1
    for i in range(b):
        number = number * a
    return (number)
