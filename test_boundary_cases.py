# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:59:24 2021

@author: Madhura
"""

from orderqty import order_food
import csv
with open('test_boundary_cases.txt') as csv_file:
    rows =csv.reader(csv_file, delimiter=',')
    def convert_to_float(row):
        return [float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4])]
    data = []
    for row in rows:
        data.append(convert_to_float(row))
        
def test_edge():
    for item in data:
        assert order_food(item[0],item[1],item[2],item[3]) == (item[4])