"""
Sentiment Dissonance (Rank Largest Sentiment Difference)
========================================================

Taking the potential best pairs data as standard input,
this script further reduce the data into a list of best pairs.

Example call of the whole pipeline:
    cat sentiment.csv | python aggregate.py | python find_min_max.py | python find_largest_difference.py
"""
import sys


best_pair = None
for line in sys.stdin:
    line = line.strip()
    pairs = line.split('\t')

    male_name1, male_sentiment1, female_name1, female_sentiment1 = pairs[0].split(',')
    male_name2, male_sentiment2, female_name2, female_sentiment2 = pairs[1].split(',')

    sentiment_difference1 = abs(int(male_sentiment1) - int(female_sentiment1))
    sentiment_difference2 = abs(int(male_sentiment2) - int(female_sentiment2))

    if sentiment_difference1 > sentiment_difference2:
        best_pair = (sentiment_difference1, male_name1, female_name1)
    else:
        best_pair = (sentiment_difference2, male_name2, female_name2)

print('Best pair is: [{}] and [{}] with sentiment difference [{}]'.format(
    best_pair[1], best_pair[2], best_pair[0]))
