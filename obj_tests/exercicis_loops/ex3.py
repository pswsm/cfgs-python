#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

number: int = int(input("Write a number:\t"))
cur_number: list[int] = [0]

while (len(cur_number) - 1) != number:
    cur_number.append(cur_number[len(cur_number)-1]+1)


print(f'Sum is: {sum(cur_number)}')
