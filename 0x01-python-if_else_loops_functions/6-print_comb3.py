#!/usr/bin/python3
"""all possible combination of two diff digits"""

for i in range(8):
    for j in range(i, 10):
        if i != j:
            print("{:d}{:d}, ".format(i, j), end="")

print(89)
