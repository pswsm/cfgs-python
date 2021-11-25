#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

names_list: list[str] = []

for i in range(3):
    name: str = input(f'Write a name:\t')
    names_list.append(name)

for name in names_list:
    print(f'Hello there, {name}')

print(f'\n')

for name in reversed(names_list):
    print(f'Hello there, {name}')
