#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

number: int = int(input("Write a number:\t"))
multiply_by: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
times: int = 0

while times != multiply_by[len(multiply_by)-1]:
    print(number*multiply_by[times])
    times = times + 1
