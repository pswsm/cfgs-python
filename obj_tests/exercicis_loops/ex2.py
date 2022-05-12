#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

counter: list[int] = ['1']

while len(counter) <= 5:
    for i in range(len(counter)):
        print(counter[i], end=" ")
    print('')
    counter.append(len(counter)+1)
