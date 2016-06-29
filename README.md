Data Engineering Challenge
=======================


Collaborative efforts in music are always a gamble.  While much of top 40 music consists of content resulting from partnerships between two or more artists, there are risks involved with bringing together such artists who may have opposing styles and motives.  However, these risks are often worth the reward and juxtapositions of contrasting styles have led to some very successful efforts like those from Eminem and Dido ([Stan](https://www.youtube.com/watch?v=gOMhN-hfMtY)), P!nk and Nate Ruess ([Just Give Me a Reason](https://www.youtube.com/watch?v=OpQFFLBMEPI)), or even Lady Gaga and Kermit the Frog ([Gypsy](https://www.youtube.com/watch?v=WOvxX7SHKiE)). 

These partnerships aren't always between men and women but a lot of the more interesting ones are.  In this challenge, you'll use a (fictituous) dataset to try to determine what pairings like this (i.e. between male and female artists) would be most "interesting" based on the sentiment within statements made by users online.  The sentiment of each statement will fall into one of 3 categories, positive, negative, or neutral.  Your job will then be to pair the artists up and draw conclusions about the sentiment around each pair.


Dataset
===========

The input dataset will consist of the following things:

- _user.name_ - The screenname of the user that mentioned the artist
- _artist.name_ - The name of the artist mentioned
- _artist.gender_ - The gender of the artist (either 'male' or 'female')
- _sentiment_ - The attitude within the statement made (either 1, -1, or 0 for positive, negative, and neutral respectively)

For example:

user.name | artist.name | artist.gender | sentiment |
----------|-------------|---------------|-----------|
user1     | Miley Cyrus | female | 1 |
user2     | Miley Cyrus | female | -1 |
user1     | Elton John | male | 1 |
user2     | Elton John | male | -1 |
user1     | Sam Smith | male | 1 |
user2     | Sam Smith | male | 1 |
user1     | Meghan Trainor | female | -1 |
user2     | Meghan Trainor | female | -1 |
user1     | Garth Brooks | male | 1 |
user2     | Garth Brooks | male | 1 |
user3     | Garth Brooks | male | 0 |
user4     | Garth Brooks | male | -1 |


Questions
==========

These questions all pertain to the data above and we only ask for answers to the first two, but if you're enjoying the problem then we would love to see answers to the others as well.  **Please submit an accompanying writeup to document your thought process when approaching the problems.**  When working in a collaborative environment, being able to explain yourself and justify your reasoning is often just as important as the work itself.

##Question 1: Sentiment Dissonance

Using [Apache Pig](#apache-pig) (see next section for more details on it), determine single male and female artist pair with the largest **difference** in cumulative sentiment.  We'll assume this difference would make the pairing more "interesting" since the public opinion about each is polarized.

An answer to this question should first determine the "net sentiment" for each artist.  For example, _Garth Brooks_ is mentioned in the example dataset above 4 times and the net sentiment for him over all mentions is 1 + 1 + 0 + -1 = 1.  This value should be calculated for each artist and then all the male and female artists should be paired together and ordered by the absolute value of the difference in that value for each pair.

A result for the example dataset would be (ordered by difference):

female.artist | male.artist | sentiment.difference
--------------|-------------|---------------------
Meghan Trainor | Sam Smith | abs(-2 - 2) = 4
Meghan Trainor | Garth Brooks | abs(-2 - 1) = 3
Miley Cyrus | Sam Smith | abs(0 - 2) = 2
Meghan Trainor | Elton John | abs(-2 - 0) = 2
Miley Cyrus | Garth Brooks | abs(0 - 1) = 1
Miley Cyrus | Elton John | abs(0 - 0) = 0

And we'd conclude that Meghan Trainor and Sam Smith make for the best pair.

*Notes*: 

1. We don't care about pairings of same sex artists (e.g. _Garth Brooks_ and _Sam Smith_)
2. The _user.name_ field is irrelevant for this question

##Question 2: Making Decisions

Assume you run your own record label and your job is to determine what proposed male/female duet is worth producing music for.  You'll encounter these opportunities once a week over the course of a year and each time you'll have to make a decision right away, and you can only choose one song to produce that year (and you'll never be offered the opportunity to work with the same duet twice).  For example, you might run into a chance to produce a duet for Micheal Buble and Rihanna in week 1 and then another for Kenny Chesney and Iggy Azalea in week 2 but you can't want until the end of week 2 to decide -- each opportunity expires at the end of the week in which it arose.

Finally, assume that the metric calculated in Question 1 for sentiment dissonance is a perfect estimator of success.  Each time you run into the chance to produce a song for a duet, you can calculate the value from Question 1 for it and use that to make your decision.

Given this, write a program (in python, java, or bash) that will take strings on stdin in the form ```female.artist,male.artist``` (one such pair per line) and output a decision as 'yes' or 'no' for each pair.  This program can assume that only artists seen in the input dataset for Question 1 will be used and that you can do anything within the program you'd like, but you must make a decision for each pair at the time it is seen (i.e. you can't look at them all and then decide).

*Notes:* 

1. No Googol-ing solutions for this please!  We'd much prefer your own approach.
2. Remember, you'll never see an offer for the same duet twice in this problem.


*Notes*:

1. There is no "right" answer to this question so feel free to take any approach you want!
2. You do **not** have to use Pig for this -- you can use anything you want like java, python + pandas, R, SQL, Scala, Spark or whatever you think would be best
2. The _user.name_ field is irrelevant for this question

