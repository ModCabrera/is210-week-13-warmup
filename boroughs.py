#!/usr/bin/env python
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
    """Open and Reads CSV File and returns summarized version of data.
    Args:
        scorefile = Opens file in read form.
        readscore = Reads CSV file and (demiliter = ',' )
        grade_dict (dict) = Placeholder for file score data.

    Returns:
        None

    Examples:
        >>> get_score_summary('inspection_results.csv')
        >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
        (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
        'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
        (414, 0.9719806763285017)}
    """
    scorefile = open(filename, 'r')
    readscore = csv.reader(scorefile, delimiter=',')
    grade_dict = {}

    for row in readscore:
        boro = row[1]
        grade = row[10]
        camisid = row[0]

        if camisid not in grade_dict and grade in GRADE_SCORE:
            grade_dict[camisid] = [grade, boro]
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
    """Opens File using json and stores data in dict.
    Args:
        marketfile = Opens file in read form.
        market_read = Loads json file into attribute
        market_data (dict) = Placeholder for Market density data.

    Returns:
        market_data (dict) = Market density data.

    Examples:
        >>> get_market_density('green_markets.json')
        {u'STATEN ISLAND': 2, u'BROOKLYN': 48, u'BRONX': 32,
        u'MANHATTAN': 39, u'QUEENS': 16}
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
    """Combines Data for Boroughs and returns a Dict AVG Score, markets/restaur.
    Args:
        restaurants (dict) = Restaurant Score summary file.
        markets (dict) = Market Density summary file.

    Returns:
        None

    Examples:
        {'BRONX': (0.9762820512820514, 0.1987179487179487)}
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
