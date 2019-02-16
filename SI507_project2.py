# Import statements necessary
from flask import Flask
from movies_tools import *

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def num_movies():
    x = MovieNumber(data_loaded)
    return x.__str__()

@app.route('/movies/ratings')
def movies_ratings():
    insts = MovieNumber(data_loaded)
    y = Movie(insts)
    z = y.__repr__()
    final = z.replace('\n', '<br>')
    return final


if __name__ == "__main__":
    app.run()
