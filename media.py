# this module is required for opening movie youtube trailer
import webbrowser
"""
Movie class:
Instace variables:
-title: Movie title
-storyline: Movie description
-poster: Movie poster
-trailer_youtube_url: Movie trailer youtube URL
Instance methods:
-show_trailer: Function that shows movie trailer in  a web browser
"""
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, main_character):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.mainchar = main_character

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
