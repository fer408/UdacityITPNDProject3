#allows for this code to be viewed in a static webpage.
import fresh_tomatoes
#allows me to use the class Movie.
import media


#following is code for my favorite movies.

#code for toy story.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


#code for avatar.

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


#code for forrest gump.

forrest_gump = media.Movie("Forrest Gump",
                           "An epic tale of a mans amazing journey trough life",
                           "https://en.wikipedia.org/wiki/Forrest_Gump#/media/File:Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=YNh9Es8Ut6U")

#code for batman begins.

batman_begins = media.Movie("Batman",
                            "A story of a rich orphan who fights crime",
                            "https://en.wikipedia.org/wiki/Batman_Begins#/media/File:Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=neY2xVmOfUM")
# code for half baked.
half_baked = media.Movie("Half Baked",
                         "A story of a group of stoners who try to get their friend out the joint",
                         "https://en.wikipedia.org/wiki/Half_Baked#/media/File:Half-baked-dvd-cover.jpg",
                         "https://www.youtube.com/watch?v=-O4wMW1-tkY")
# code for jaws.
jaws = media.Movie("Jaws",
                   "A story about a giant killer shark",
                   "https://en.wikipedia.org/wiki/Jaws_(film)#/media/File:JAWS_Movie_poster.jpg",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")
#code for joe dirt.
joe_dirt = media.Movie("Joe dirt",
                       "A Hillbilly tries to find his parents but ends up finding family in other places",
                       "https://en.wikipedia.org/wiki/Joe_Dirt#/media/File:Joe_dirt.jpg",
                       "https://www.youtube.com/watch?v=FpHIIE9Lois")
#code for fight club
fight_club = media.Movie("Fight Club",
                         "a weak regular man ends up finding himself trough beating up his buddies in a secret club",
                         "https://en.wikipedia.org/wiki/Fight_Club#/media/File:Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
movies = [toy_story,avatar,forrest_gump,batman_begins,half_baked,jaws,joe_dirt,fight_club]

#code that makes it all happen
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
