#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

def cube_to(num: int) -> dict[int, int]:
    return {n: n ** 3 for n in range(num+1)}

print(cube_to(6))
