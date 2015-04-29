#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Open and read a CSV file on local filesystem."""
import csv

grades = {
    'A': float(100),
    'B': float(90),
    'C': float(80),
    'D': float(70),
    'F': float(60),
}


def get_score_summary(filename):
    openfile = open(filename, 'r')
    readfile = csv.reader(openfile, delimiter = ',')
    output = {}
    final = {}

    for row in readfile:
        if row[1] not in output and bool(row[10]) and row[10] is not 'P':
            output.update({row[0]:[row[10],row[1]]})
    openfile.close()
    boro_count = {}
    for grade_val in output.values():
        if grade_val[1] in final:
            final[grade_val[1]] += grades[grade_val[0]]
            boro_count[grade_val[1]] += 1
        elif grade_val[1] != 'BORO':
            final.update({grade_val[1]: 0})
            boro_count.update({grade_val[1]:1})
    print final, boro_count


if __name__ == '__main__':
    data = get_score_summary('inspection_results.csv')
