#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

from pathlib import Path

path: str = '/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-simple.csv'

class Field:
    def __init__(self, contents: str):
        field_name: list[str] = contents.split(';', maxsplit=1)
        field_name = field_name.pop[0]
        field_contents: list[str] = contents.split(';')
        field_contents.pop[0]



def get_data(file: str) -> str:
    pfile = Path(file)
    contents: str = pfile.read_text()
    return contents

#  print(get_data('/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-simple.csv'))

def get_vax(data: str, sep: str) -> str:
    data_sorted: list[list[str]] = []
    newfield: Field = ''
    for line in data:
        data_sorted.append(data.split('\n'))
    
    for line in data:
        newfield

    return data_sorted

print(get_vax(get_data(path), ';'))
