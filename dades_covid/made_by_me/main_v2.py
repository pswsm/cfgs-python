#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

from pathlib import Path

path: str = '/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-simple.csv'

def row(file: str) -> list[str]:
    text: str = Path(file).read_text()
    rows: list[str] = text.split('\n')
    return rows

def column(row: list[str]) -> dict[str, list[str]]:
    rows: list[str] = row
    headers: list[str] = rows[0].split(';')
    rows.pop(0)
    listed_rows: list[list[str]] = []
    sorted_rows: list[list[str]] = []
    for rows_num in range(len(rows)-1):
        listed_rows.append(rows[rows_num].split(';'))


    for data in range(len(listed_rows)):
        for header in range(len(headers)):
            sorted_rows.append(list(listed_rows[data][header].split(';')))

    table: dict[str, list[str]] = {k: v for k, v in zip(headers, sorted_rows)}
    return table



rows = row(path)
table = column(rows)
#  print(rows)
print(table)
