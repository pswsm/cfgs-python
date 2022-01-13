#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

from sympy import isprime

from_to: tuple[int, int] = (25, 50)
chck_cur: int = from_to[0]

while chck_cur <= from_to[1]:
    if isprime(chck_cur): print(chck_cur)
    chck_cur = chck_cur + 1

