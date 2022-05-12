#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

number: int = 698143
str_number: str = str(number)
rev_number: str = ''
times: int = len(str_number)-1


while len(rev_number) < len(str_number):
    rev_number = rev_number + str_number[times]
    times = times - 1

print(rev_number)

