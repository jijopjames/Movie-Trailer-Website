class Movie():
    """ This Class will store differnt movie information"""
    
    def __init__(self, movie_title, poster_image, trailer_youtube_link):
        """" It takes three arguments movie_title, poster_image, trailer_youtube_link as input
        and create an object for class movie which will have different instance"""
        self.title = movie_title #Create instance Object object_name.title
        self.poster_image_url = poster_image #Create instance Object object_name.poster_image_url
        self.trailer_youtube_url = trailer_youtube_link #Create instance Object object_name.trailer_youtube_url
        
    