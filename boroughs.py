#!/usr/bzin/env python
# -*- coding: utf-8 -*-
"""Open and read a CSV file on local filesystem."""
import csv

grade_score = {
    'A': float(1.0),
    'B': float(.90),
    'C': float(.80),
    'D': float(.70),
    'F': float(.60),
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
            graded_count[grade_boro] += 1
        else:
            rest_count[grade_boro] = grade_score[grade_letter]
            graded_count[grade_boro] = 1

    print graded_count
    div = {rest_count[grade_boro] / graded_count[grade_boro] for grade_boro in graded_count.keys()}
    print div


if __name__ == '__main__':
    data = get_score_summary('inspection_results.csv')
