#code that allows the trailer to be viewed on the web brower.
import webbrowser
# this is the class Movie which is the foundation for everything.
class Movie():
    """This class alows for movie information to be stored."""
    
    VALID_RATINGS = ["G","PG","PG-13","R"]

# this function is the base for the Movie objects.   
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#this function allows for trailers to be showed.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


