#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

def name_list(*args: str) -> list[str]:
    names: list[str] = []
    for arg in args:
        names.append(arg)

    return names

name_list: list[str] = name_list('Pau', 'Pep', 'Ady', 'Victor', 'Alex')

for name in name_list:
    position: int = name_list.index(name)
    print(f'{position}. {name}')
