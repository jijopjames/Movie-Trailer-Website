# Importing fresh_tomatoes.py to create website
import fresh_tomatoes as ft
# Importing Media.py which contains class Movie
import media

# Name of the movie, Poster image link, Movie Trailer link
toy_story = media.Movie("Toy Story",
                        "http://www.gstatic.com/tv/thumb/v22vodart/17420/p17420_v_v8_an.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Name of the movie, Poster image link, Movie Trailer link
avatar = media.Movie("Avatar",
                     "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# Name of the movie, Poster image link, Movie Trailer link
ratatouille = media.Movie("Ratatouille ",
                          "http://www.gstatic.com/tv/thumb/v22vodart/165058/p165058_v_v8_ao.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Name of the movie, Poster image link, Movie Trailer link
the_nun = media.Movie("The Nun ",
                      "http://www.gstatic.com/tv/thumb/movieposters/13794422/p13794422_p_v8_af.jpg",
                      "https://www.youtube.com/watch?v=pzD9zGcUNrw")

# Name of the movie, Poster image link, Movie Trailer link
mission_impossible_fallout = media.Movie("Mission: Impossible Fallout",
                                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWqjAfSjQGFfXUAdkAKPBS-EVWgr8Jc1RWXbZ27wBnvFFGkYuvXp8k4A",
                                         "https://www.youtube.com/watch?v=wb49-oV0F78")

# Name of the movie, Poster image link, Movie Trailer link
black_panther = media.Movie("Black Panther",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNUyQ4AbW0CnBKsOF3CG4xrk7I0AcqKlzBBhwo99mvamHgJK5PvcM0oA",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

# Name of the movie, Poster image link, Movie Trailer link
avengers_infinity_war = media.Movie("Avengers: Infinity War",
                                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcVCMkjly4Nun1UDWBtyhvp7J5cpSNgT7XdmFgjAfxvrpyPchvqFbjCw",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Name of the movie, Poster image link, Movie Trailer link
venom = media.Movie("Venom",
                    "http://www.gstatic.com/tv/thumb/movieposters/13937884/p13937884_p_v8_ab.jpg",
                    "https://www.youtube.com/watch?v=xLCn88bfW1o")

# Name of the movie, Poster image link, Movie Trailer link
aquaman = media.Movie("Aquaman",
                      "https://pbs.twimg.com/media/DiPQxl3VAAAZKjs.jpg",
                      "https://www.youtube.com/watch?v=xjDjIWPwcPU")

# list of movies
movies = [toy_story, avatar, ratatouille, the_nun,
          mission_impossible_fallout, black_panther,
          avengers_infinity_war, venom, aquaman]
# function call to display the movie trailer on website
ft.open_movies_page(movies)
