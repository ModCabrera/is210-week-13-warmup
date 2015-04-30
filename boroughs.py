#!/usr/bzin/env python
# -*- coding: utf-8 -*-
"""Open and read a CSV file on local filesystem."""
import csv
import decimal

grade_score = {
    'A': float('100'),
    'B': float('90'),
    'C': float('80'),
    'D': float('70'),
    'F': float('60'),
}


def get_score_summary(filename):
    scorefile = open(filename, 'r')
    readscore = csv.reader(scorefile, delimiter = ',')
    grade_dict ={}

    for row in readscore:
        boro = row[1]
        grade = row[10]
        camisid = row[0]
        if boro not in grade_dict and grade in grade_score:
            grade_dict.update({camisid: [grade, boro]})
    scorefile.close()
    rest_count = {}
    graded_count = {}

    for grade in grade_dict.values():
        grade_letter = grade[0]
        grade_boro = grade[1]

        if grade_boro in rest_count:
            rest_count[grade_boro] += grade_score[grade_letter]
            graded_count[grade_boro] += float('100')
        else:
            rest_count.update({grade_boro: grade_score[grade_letter]})
            graded_count.update({grade_boro: float('100')})
    print rest_count
    print graded_count

    div = {rest_count[grade_boros] / graded_count[grade_boros] for grade_boros in graded_count.keys()}
    print div
    

#prints above for debug purposes. output below
#{'BRONX': 15230.0, 'BROOKLYN': 40640.0, 'STATEN ISLAND': 4510.0, 'MANHATTAN': 73090.0, 'QUEENS': 40240.0}
#{'BRONX': 15600.0, 'BROOKLYN': 41700.0, 'STATEN ISLAND': 4600.0, 'MANHATTAN': 74800.0, 'QUEENS': 41400.0}
#set([0.9771390374331551, 0.9719806763285024, 0.9762820512820513, 0.9745803357314149, 0.9804347826086957])
#>>> 

if __name__ == '__main__':
    data = get_score_summary('inspection_results.csv')
