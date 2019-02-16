# SI 507 - Homework 4
# Note the changed name (Lab -> Homework)

# Instructions all provided in this file.
# IMPORTANT: Please read ALL of the instructions for each part before starting on it.

# Submit this edited code file (only) to HW 4 on Gradescope via Canvas to see test results!

## Your import statements for use in the program (both things installed wih pip & things that come default with Python) should go here!
import csv
import pandas as pd
import numpy as np
import random
from itertools import product, permutations


#####################

## [PART 1]
# Provided is a dataset: movies_dataset_group.csv
# Your first goal is to write code to "clean" this dataset a little bit and produce a cleaned version of the dataset in a file called movies_clean.csv.

filename = 'movies_dataset_group.csv'
df = pd.read_csv(filename)
# print(df.head(1))

df.fillna(value = 'NA', inplace = True)
# print(df.head(1))

length = len(df['Release Date'])

dates = df['Release Date'].values.tolist()

for i in range(len(dates)):
    if len(dates[i]) < 8:
        dates[i] = 'NA'
    elif len(dates[i]) > 9:
        dates[i] = 'NA'
    elif len(dates[i]) == 8:
        dates[i] = '0' + dates[i]

df['Release Date'] = dates


# print(df['Release Date'])
df.to_csv('movies_clean.csv')


## [PART 2]

dict = {'G': 1, 'PG': 2, 'PG-13': 3, 'R': 4, 'NC-17': 5}
coded_list = []


for i in df['MPAA Rating']:
    if i in dict.keys():
        coded_list.append(dict.get(i))
sorted_list = sorted(coded_list)

median_value = np.median(sorted_list)

for rating, coding in dict.items():
    if coding == median_value:
        median_rating = rating

# print(median_rating)
# print(sorted_list)


## [PART 3]

print("\n\nNEW FAKE MOVIE TITLES CREATED BELOW...\n\n")
# Write your code to enact all of this below

title_list = []
word_list = []
ratings_list = ['G', 'PG', 'PG-13', 'R', 'NC-17']

for i in df['Title']:
    title_list.append(i)

for i in title_list:
    word = i.split()
    for e in word:
        if e.title() not in word_list:
            word_list.append(e.title())

# print(word_list)

space = " "
random.shuffle(word_list)
title_options = permutations(word_list, 2)
all_title_options = list(title_options)
random.shuffle(all_title_options)
for item in all_title_options[:10]:
    sample_fake_movies = "{} - {}".format(space.join(item), random.choice(ratings_list))
    print(sample_fake_movies)
