#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

numbers: int = 5
start: int = 2
result: int = 0

while len(str(start)) <= numbers:
    result = result + start
    start = int(str(start)+'2')

print(result)
