#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

number: int = 6
cur_num: int = 1

while cur_num <= number:
    print(f'Current number is: {cur_num}. Cube is: {cur_num ** 3}')
    cur_num += 1
