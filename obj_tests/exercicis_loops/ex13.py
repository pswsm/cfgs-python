#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

def factorial(number: int) -> int:
    '''
    Just a factorial calculator.
    Give an int, return the factorial
    '''
    times: int = 1
    result: int = 1

    assert (number >= 0), "Can't factorize negative integers"

    while times <= number:
        result = result * times
        times = times + 1

    return result

print(factorial(1))

