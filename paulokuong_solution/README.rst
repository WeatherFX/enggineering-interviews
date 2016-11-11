Objective
=========

The goal is to “determine single male and female artist pair with the
largest difference in cumulative sentiment”. Sentiment difference is
defined by the difference between the two ‘net sentiments’, which is a
sum of ‘sentiment’ values each of which represented by integers (-1, 0
or 1), of a male artist and a female artist.

Analysis
========

There are couple of thoughts when analyzing the data:

1. The real data set could be a continuous stream of data. This is because people change their favorite idols all the time.

2. The real data set can be huge. We would want to consider methodologies to scaling this process.

3. We have to assume that the names will not have a comma (,) in it. This is because this csv file does not have columns enclosed by quotes. If there is a comma in the names, there is no way to know which column it is.

4. We assume that there is no “multiple best” pairs of artists, having the largest difference the same. This is because we just want to determine single pair according to objective.

5. We have to assume that there will not be a case when the names of multiple different artists are the same. For example, Paulo - male should be a unique male artist. However, we should consider a male and a female with the same name. For example, the best pair could be: Jackie - Jackie, where one is male and one is female.

6. Since user.name is irrelevant to this question, we don’t need to worry about whether an artist is “truly sentimentally positive/negative” if there are duplicate entries with the same user voting the same artist. We don’t even need to load user.name data during our process.

Solutions
=========

In order to find the best pair from 2 groups of male and female artists,
all we need to do is to compare the total sentiment value differences of
the pair of most popular male artist and least popular female artist and
the pair of the least popular male artist and most popular female
artist. The best pair will be the one that has the greatest difference.
In other word:

Let:

    MH be “male-with-highest-sentiment-value”

    FL be “female-with-lowest-sentiment-value”

    ML be “male-with-lowest-sentiment-value”

    FH be “female-with-highest-sentiment-value”

Hence:

Largest Sentiment Difference = max(abs(MH -FL), abs(ML -FH))

A naive solution would be loading the whole dataset to database and
aggregate by artist.name-artist.gender, summing up the sentiment, then
find MH, FL, ML and FH. Such process is very costly in terms of system
resource and performance. This is because the real data set could be
billions of rows and there could be millions of artists.

A better solution would be to prevent a performance bottleneck on a
single system. Therefore, I propose the following data pipeline to
reduce the data set into one answer:

1. Scan the data set, reducing the data set into 2 separate male and female data sets. The sentiment values are accumulated for each artist during the reduce process. The data sets can be stored in some Key-Value store so that read and write will be very efficient. The key in this case would be the artist name and the value would be the accumulated sentiments.

2. Now, we have 2 key-value data sets. We can now pipe the data into a process where we find the MH, FL, ML and FH (see description above). The data is now reduced to sets of (MH, FL, ML and FH).

3. Finally, we have the sets of high and low values, we further reduce the sets by picking the pairs with the less differences.

Visual explanation:
  .. image:: https://github.com/paulokuong/engineering-interviews/blob/master/paulokuong_solution/weather_workflow.jpg


Running the workflow
====================

In the directory where raw file is located:

    $ cat sentiment.csv | python aggregate.py | python find_min_max.py | python find_largest_difference.py

Dependencies
============
python 3.4.3
