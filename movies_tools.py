import random
from itertools import product, permutations

data = open("movies_clean.csv", 'r')
data_loaded = data.readlines()
data.close()

divided_headline = data_loaded[0].split(',')
title_index = divided_headline.index('Title')
imdb_rating_index = divided_headline.index('IMDB Rating')


class MovieNumber():
    def __init__(self, data_list):
        self.data = data_list

    def __str__(self):
        return "{} movies recorded".format(len(self.data))


    def __repr__(self):
        random_list = []
        for x in range(5):
            random_chosen = random.randint(1,len(self.data))
            random_list.append(random_chosen)
        return random_list

#take in random list of 5 numbers
class Movie():

    def __init__(self, class_inst):
        self.random_list = class_inst.__repr__()

    def __str__(self):
        list = []
        return "{}".format('this is just for show')

    def __repr__(self):
        list = []
        for i in self.random_list:
            divided_row = data_loaded[i].split(',')
            title = divided_row[title_index]
            rating = divided_row[imdb_rating_index]
            proper_format = "{} | {}".format(title, rating)
            list.append(proper_format)
        new_list = '\n'.join(list)
        return new_list


if __name__ == "__main__":
    movienumber_insts = MovieNumber(data_loaded)
    print(type(movienumber_insts.__str__()))
    print(MovieNumber(data_loaded).__repr__())
    movie_insts = Movie(movienumber_insts)
    print(movie_insts.__repr__())
