#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

numlist: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cur_pos: int = 0

while cur_pos < len(numlist):
    if cur_pos == 1 or cur_pos % 2 == 1:
        print(numlist[cur_pos], end=' ')

    cur_pos += 1
