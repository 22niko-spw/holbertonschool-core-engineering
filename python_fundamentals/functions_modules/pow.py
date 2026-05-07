#!/usr/bin/env python3

def pow(a, b):
    number = 1
    for i in range(b):
        number = number * a
    print("{}".format(number))
