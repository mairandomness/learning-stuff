""" This file contains:
- the class Movie used in entertainment_center.py"""


# class movie has the attributes specified in fresh_tomatoes.py

class Movie():
    # This init of this class takes 3 strings as input
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
