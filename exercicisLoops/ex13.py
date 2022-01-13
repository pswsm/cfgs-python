#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

number: int = 5
times: int = 1
result: int = 1

# Calculate Factorial
while times <= number:
    result = result * times
    #  print(times)
    times = times + 1

print(result)
