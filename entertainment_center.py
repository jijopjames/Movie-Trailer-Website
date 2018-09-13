import fresh_tomatoes as ft #Importing fresh_tomatoes.py which contains open_movies_page function to publish the data on to the website
import media #Importing Media.py which contains class Movie

toy_story = media.Movie("Toy Story", #Name of the movie 
                     "http://www.gstatic.com/tv/thumb/v22vodart/17420/p17420_v_v8_an.jpg", #Poster image link
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")#Movie Trailer link

avatar = media.Movie("Avatar", #Name of the movie 
                     "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",#Poster image link
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")#Movie Trailer link

ratatouille  = media.Movie("Ratatouille ", #Name of the movie 
                     "http://www.gstatic.com/tv/thumb/v22vodart/165058/p165058_v_v8_ao.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")#Movie Trailer link

the_nun = media.Movie("The Nun ", #Name of the movie 
                     "http://www.gstatic.com/tv/thumb/movieposters/13794422/p13794422_p_v8_af.jpg",#Poster image link
                     "https://www.youtube.com/watch?v=pzD9zGcUNrw")#Movie Trailer link

mission_impossible_fallout  = media.Movie("Mission: Impossible Fallout", #Name of the movie 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWqjAfSjQGFfXUAdkAKPBS-EVWgr8Jc1RWXbZ27wBnvFFGkYuvXp8k4A",#Poster image link
                     "https://www.youtube.com/watch?v=wb49-oV0F78")#Movie Trailer link

black_panther = media.Movie("Black Panther", #Name of the movie 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNUyQ4AbW0CnBKsOF3CG4xrk7I0AcqKlzBBhwo99mvamHgJK5PvcM0oA",#Poster image link
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")#Movie Trailer link

avengers_infinity_war = media.Movie("Avengers: Infinity War", #Name of the movie 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcVCMkjly4Nun1UDWBtyhvp7J5cpSNgT7XdmFgjAfxvrpyPchvqFbjCw",#Poster image link
                     "https://www.youtube.com/watch?v=6ZfuNTqbHE8")#Movie Trailer link

venom = media.Movie("Venom", #Name of the movie 
                     "http://www.gstatic.com/tv/thumb/movieposters/13937884/p13937884_p_v8_ab.jpg",#Poster image link
                     "https://www.youtube.com/watch?v=xLCn88bfW1o")#Movie Trailer link

aquaman = media.Movie("Aquaman", #Name of the movie 
                     "https://pbs.twimg.com/media/DiPQxl3VAAAZKjs.jpg",#Poster image link
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")#Movie Trailer link



movies = [toy_story,avatar,ratatouille,the_nun,mission_impossible_fallout,black_panther,avengers_infinity_war,venom,aquaman] #list of movie names
ft.open_movies_page(movies) #function call to display the movie trailer on website
