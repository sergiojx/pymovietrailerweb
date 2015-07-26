# This module builds web trailer html document
import fresh_tomatoes
# required for Movie object handling 
import media
"""
six Movie instances are created.
"""
toy_story = media.Movie(
    "Toy Story",
    "A marine in a alien planet",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "Woody (Tom Hanks) and Buzz Lightyear(Tim Allen)")

avatar = media.Movie(
    "Avatar",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "Sam Worthington")

relsalvajes = media.Movie(
    "Relatos Salvajes",
    "5 weird and crazy  tales",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQRcYnYcOMXIFSp1BP_VVCDS1PD_euBAaZjQuU3E77tjYQJSumX", # noqa
    "https://www.youtube.com/watch?v=3BxE9osMt5U",
    "Ricardo Darín")

thepianist = media.Movie(
    "The Pianist",
    "The Extraordinary True Story of One Man's Survival in Warsaw, 1939-1945",
    "http://www.gstatic.com/tv/thumb/movieposters/30193/p30193_p_v7_aa.jpg",
    "https://www.youtube.com/watch?v=e_4NvY3v51Q",
    "Adrien Brody")

lordrings = media.Movie(
    "The Lord of the Rings",
    "The Lord of the Rings is an epic high-fantasy novel written by English \
    author J. R. R. Tolkien",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4",
    "Elijah Wood")

paintedvell = media.Movie(
    "Painted Vell",
    "Caught in an affair with another man (Liev Schreiber), a scientist's \
    callow wife \   (Naomi Watts) accompanies her husband (Edward Norton) \
    to mainland China in the 1920s to fight a cholera epidemic",
    "http://www.gstatic.com/tv/thumb/dvdboxart/161862/p161862_d_v7_aa.jpg",
    "https://www.youtube.com/watch?v=9q8s4eKcqeQ",
    "Naomi Watts and Edward Norton")
"""
Movie object array is formed and passed to -fresh_tomatoes.open_movies_page-
funtion. This will buid and show the outputHTML file.
"""
movies = [toy_story, avatar, relsalvajes, thepianist,lordrings, paintedvell]
fresh_tomatoes.open_movies_page(movies)


