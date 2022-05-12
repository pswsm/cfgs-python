#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

names: list[str] = ['Pau', 'Gabi', 'Berta']
new_names: list[str] = []

for name in names:
    index: int = names.index(name)
    new_names.append(names[index])

print(new_names)
