#!/usr/bzin/env python
# -*- coding: utf-8 -*-
"""Open and read a CSV file on local filesystem."""
import csv
import json


GRADE_SCORE = {
    'A': float(1),
    'B': float(.9),
    'C': float(.8),
    'D': float(.7),
    'F': float(.6),
}


def get_score_summary(filename):
    """
    Args:
    Returns:
    Examples:
    """
    scorefile = open(filename, 'r')
    readscore = csv.reader(scorefile, delimiter=',')
    grade_dict = {}

    for row in readscore:
        boro = row[1]
        grade = row[10]
        camisid = row[0]

        if camisid not in grade_dict and grade in GRADE_SCORE:
            grade_dict.update({camisid: [grade, boro]})
    scorefile.close()

    rest_summary = {}
    for grade in grade_dict.values():
        grade_letter = grade[0]
        grade_boro = grade[1]

        if grade_boro in rest_summary:
            rest_summary[grade_boro][1] += GRADE_SCORE[grade_letter]
            rest_summary[grade_boro][0] += 1
        else:
            rest_summary[grade_boro] = [1, GRADE_SCORE[grade_letter]]

    final = {}
    for boro, grade in rest_summary.iteritems():
        final[boro] = grade[0], grade[1]/grade[0]
    return final


def get_market_density(filename):
    """
    Args:
    Returns:
    Examples:
    """
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


def correlate_data(restaurants, markets, outputfile):
    """
    Args:
    Returns:
    Examples:
    """
    restaurants = get_score_summary(restaurants)
    markets = get_market_density(markets)
    data_dict = {}

    for key, value in markets.iteritems():
        boro = key.upper()
        markval = float(value)
        restval = float(restaurants[boro][0])

        if boro in restaurants:
            data_dict[boro] = restaurants[boro][1], markval/restval

    with open(outputfile, 'w') as outfile:
        json.dump(data_dict, outfile)
