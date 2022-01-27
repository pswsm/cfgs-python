#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

import csv

with open('/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-simple-commas.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    

print(row)
