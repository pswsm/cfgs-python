#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

fibonacci: list[int] = [0, 1]

while len(fibonacci) < 10:
    fibonacci.append(fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1])

print(fibonacci)
