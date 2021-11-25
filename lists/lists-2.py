#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

def sum_in_list(numbers: list[float]) -> float:
    result:float = 0

    for number in numbers:
        result = result + number

    return result

numbers: list[float] = []

for i in range(3):
    number: float = float(input(f'Write a number:\t'))
    numbers.append(number)

print(sum_in_list(numbers))
