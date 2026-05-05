#!/usr/bin/env python3

for i in range(97, 123):
    char = chr(i)

    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print(format(char), end='')
