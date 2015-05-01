#!/usr/bzin/env python
# -*- coding: utf-8 -*-
"""Open and read a CSV file on local filesystem."""
import csv


grade_score = {
    'A': float(1),
    'B': float(.9),
    'C': float(.8),
    'D': float(.7),
    'F': float(.6),
}


def get_score_summary(filename):
    scorefile = open(filename, 'r')
    readscore = csv.reader(scorefile, delimiter = ',')
    grade_dict ={}

    for row in readscore:
        boro = row[1]
        grade = row[10]
        camisid = row[0]
        if camisid not in grade_dict and grade in grade_score:
            grade_dict.update({camisid: [grade, boro]})
    scorefile.close()
    
    rest_summary = {}

    for grade in grade_dict.values():
        grade_letter = grade[0]
        grade_boro = grade[1]


        if grade_boro in rest_summary:
            rest_summary[grade_boro][1] += grade_score[grade_letter]
            rest_summary[grade_boro][0] += 1

        else:
            rest_summary[grade_boro] = [1, grade_score[grade_letter]]

    final = {}

    for boro, grade in rest_summary.iteritems():
        final[boro] = grade[0], grade[1]/float(grade[0])

    return final


import json


def get_market_density(filename):
    marketfile = open(filename, 'r')
    market_read = json.load(marketfile)
    market_data = {}

    for values in market_read['data']:
        boro = values[8].strip()
        if boro in market_data:
            market_data[boro] += 1
        else:
            market_data[boro] = 1
            
    return market_data


def correlate_data(gradefile, marketfile, outputfile):
    
    
    
    













    
if __name__ == '__main__':
    data = get_score_summary('inspection_results.csv')
    data2 = get_market_density('green_markets.json')
    print data2
