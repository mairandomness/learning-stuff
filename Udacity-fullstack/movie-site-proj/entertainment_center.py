""" This file contains the construction of a list of instances from the class
media.Movie and the call of the function open_movies_page
(from fresh_tomatoes) that creates the html of the website"""


import fresh_tomatoes
import media

if __name__ == "__main__":
    # Create instances of Movie
    totoro = media.Movie(
        "My Neighbor Totoro",
        "https://img.posterlounge.co.uk/images/wbig/poster-mein-nachbar-totoro-341428.jpg",
        "https://www.youtube.com/watch?v=TuLX50_5UAI")

    vampire = media.Movie(
        "Interview With The Vampire",
        "https://images-na.ssl-images-amazon.com/images/I/91FaEjsX0bL._SY445_.jpg",
        "https://www.youtube.com/watch?v=BRXWYKCzOJk")

    matrix = media.Movie(
        "Matrix",
        "http://imgc.allpostersimages.com/img/posters/the-matrix_u-L-F4S5W20.jpg",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU&t=1s")

    # put them in a list
    movie_list = [totoro, vampire, matrix]
    # call the open_movies_page function that takes a list of Movie objects as input
    fresh_tomatoes.open_movies_page(movie_list)
