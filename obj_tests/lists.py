#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

names_list: list[str] = ['a', 'b', 'c']

#  for i in range(3):
    #  name: str = input(f'Write a name:\t')
    #  names_list.append(name)

for name in names_list:
    print(f'Hello there, {name}')

x: int = 0

print(f'\n')

for name in reversed(names_list):
    print(f'Hello there, {name}')
