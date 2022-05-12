#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

numbers: list[int] = [5, 4, 3, 2, 1]
times: int = 0

while times != len(numbers):
    w_times: int = times
    while w_times != len(numbers):
        print(numbers[w_times], end=' ')
        w_times = w_times + 1
    print('')
    times = times + 1
