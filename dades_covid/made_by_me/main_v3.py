#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

from pathlib import Path
import pprint

path: str = '/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-aga.csv'

def row(file: str) -> list[str]:
    text: str = Path(file).read_text()
    rows: list[str] = text.split('\n')
    return rows

def column(row: list[str]) -> list[dict[str, str]]:
    rows: list[str] = row
    headers: list[str] = rows[0].split(';')
    rows.pop(0)
    listed_rows: list[list[str]] = []
    sorted_rows: list[list[str]] = []
    for rows_num in range(len(rows)-1):
        listed_rows.append(rows[rows_num].split(';'))


    for data in range(len(listed_rows)):
            sorted_rows.append(list(listed_rows[data]))

    #  print(listed_rows)
    #  print(sorted_rows)

    table: list[dict[str, str]] = []
    
    for data in range(len(sorted_rows)):
        table.append(dict(zip(headers, sorted_rows[data])))

    return table

def search_tbl(k_to_srx: str, v_to_srx: str, table: list[dict[str, str]]) -> list[int]:
    pprint.pprint("Starting search")
    indexes: list[int] = []
    for dictionary in table:
        pprint.pprint(f'Searching {dictionary} for {v_to_srx}')
        if k_to_srx in dictionary.keys() and v_to_srx in dictionary[k_to_srx]:
            indexes.append(table.index(dictionary))

    if not indexes:
        return [0]
    else:
        return indexes

def pprint_found(idxs: list[int], table: list[dict[str, str]]):
    for idx in idxs:
        pprint.pprint(table[idx])

rows = row(path)
table = column(rows)
where = search_tbl('NOM', 'BARCELONA', table)
#  print(rows)

pprint_found(where, table)
