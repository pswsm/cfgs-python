#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

numbers: list[int] = [12, 75, 150, 180, 145, 525, 50]
length: int = 0

while length != len(numbers)-1:
    if numbers[length] in [75, 150, 145]:
        print(numbers[length])
        length = length + 1
    else:
        length = length + 1

