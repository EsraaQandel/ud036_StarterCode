import webbrowser

class Movie():

	""" A class the presents a movie with its title,storyline,image and a youtube trailer"""
	def __init__ (self,movie_title, movie_storyline,poster_images,trailer_youtube):
	    self.title= movie_title
	    self.storyline = movie_storyline
	    self.poster_image_url = poster_images
	    self.trailer_youtube_url = trailer_youtube
	

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
            
      


