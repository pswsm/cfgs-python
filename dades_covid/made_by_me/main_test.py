#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

from pathlib import Path
import pandas

path: str = '/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-aga.csv'

def toTable(file) -> dict[str, str]:
    csvData = pandas.read_csv(file, sep=';')
    return csvData

def sumShots(table: dict, column: str) -> float:
    totalShots = table[column].sum()
    return totalShots

table = toTable(path)
print(table)
#  print(sumShots(table, "VACUNATS_DOSI_1"))# + sumShots(table, "VACUNATS_DOSI_2"))
