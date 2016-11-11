"""
Sentiment Dissonance (Aggregation)
==================================

Taking the raw data as a standard input, aggregate the data so that
the data is reduced to a mapping which contains unique artists and
their corresponding accumulated sentiment values.

Example call of the whole pipeline:
    cat sentiment.csv | python aggregate.py | python find_min_max.py | python find_largest_difference.py
"""
import json
import itertools
import sys

import utils

MALE_FILE_PREFIX = 'male'
FEMALE_FILE_PREFIX = 'female'


def _map_and_aggregate(file_name, artist_name, sentiment):
    """Map and aggregate sentiment values

    Read and Write on json file, summing up sentiment
    values for each artist. This operation can be replaced
    by an efficient cloud KEY-VALUE store service. For demo
    purpose, we currently use the json.load and json.dump.

    Args:
        file_name (str): json file contains a key-value map.
        artist_name (str): artist name.
        sentiment (int): -1, 1 or 0.
    """
    utils.create_file_if_not_exists(file_name)
    data_set = json.load(open(file_name, 'r'))
    if data_set.get(artist_name):
        data_set[artist_name] += int(sentiment)
    else:
        data_set[artist_name] = int(sentiment)
    json.dump(data_set, open(file_name, 'w'))


male_file_name = '{}{}'.format(MALE_FILE_PREFIX, '.json')
female_file_name = '{}{}'.format(FEMALE_FILE_PREFIX, '.json')
utils.delete_file_if_exists(male_file_name)
utils.delete_file_if_exists(female_file_name)
for line in sys.stdin:
    line = line.strip()
    user_name, artist_name, gender, sentiment = line.split(',')
    if gender == 'female':
        _map_and_aggregate(female_file_name, artist_name, sentiment)
    elif gender == 'male':
        _map_and_aggregate(male_file_name, artist_name, sentiment)
    else:
        continue

# Sending aggregated data to standard output. In the real system, instead of json.load,
# KET-VALUE store service requests will be made. json_load is for demo purpose.
male_json_file = json.load(open(male_file_name, 'r'))
female_json_file = json.load(open(female_file_name, 'r'))
for pair in itertools.zip_longest(male_json_file.items(), female_json_file.items(), fillvalue=('', '')):
    print('{},{}\t{},{}'.format(pair[0][0], pair[0][1], pair[1][0], pair[1][1]))
