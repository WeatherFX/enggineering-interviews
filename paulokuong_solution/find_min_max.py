"""
Sentiment Dissonance (Find Min Max)
===================================

Taking the aggregated male and female artist-to-sentiments data as
standard input, this script further reduce the data into:
 - male artist with highest sentiment value
 - male artist with lowest sentiment value
 - female artist with highest sentiment value
 - female artist with lowest sentiment value

Example call of the whole pipeline:
    cat sentiment.csv | python aggregate.py | python find_min_max.py | python find_largest_difference.py
"""
import sys

# Variables each with format {"name": "Paulo": "total_sentiment": 4}
current_MH = None  # male artist with highest sentiment value
current_FH = None  # female artist with highest sentiment value
current_ML = None  # male artist with lowest sentiment value
current_FL = None  # female artist with lowest sentiment value

for line in sys.stdin:
    line = line.strip()
    male, female = line.split('\t')
    male_name, male_sentiment = male.split(',')
    female_name, female_sentiment = female.split(',')

    if male_name and (current_MH is None or current_MH.get('total_sentiment') < int(male_sentiment)):
        current_MH = dict(name=male_name, total_sentiment=int(male_sentiment))
    if female_name and (current_FH is None or current_FH.get('total_sentiment') < int(female_sentiment)):
        current_FH = dict(name=female_name, total_sentiment=int(female_sentiment))
    if male_name and (current_ML is None or current_ML.get('total_sentiment') > int(male_sentiment)):
        current_ML = dict(name=male_name, total_sentiment=int(male_sentiment))
    if female_name and (current_FL is None or current_FL.get('total_sentiment') > int(female_sentiment)):
        current_FL = dict(name=female_name, total_sentiment=int(female_sentiment))

print(
    '{},{},{},{}\t{},{},{},{}'.format(
        current_MH.get('name'), current_MH.get('total_sentiment'),
        current_FL.get('name'), current_FL.get('total_sentiment'),
        current_ML.get('name'), current_ML.get('total_sentiment'),
        current_FH.get('name'), current_FH.get('total_sentiment')))
