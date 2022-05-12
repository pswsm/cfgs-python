#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
times_0: int = len(numbers) - 1

while times_0 >= 0:
    print(f'-{numbers[times_0]}')
    times_0 = times_0 - 1
