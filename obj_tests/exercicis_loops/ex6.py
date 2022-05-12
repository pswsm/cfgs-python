#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

import random

number: int = random.randint(0, 10000)
counter: int = 0

while counter != len(str(number)):
    counter = counter + 1

print(f'{number}\n{counter}')
