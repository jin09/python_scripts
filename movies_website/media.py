import webbrowser


class Movie():

     def __init__(self,movietitle,movie_storyline,movie_poster,movie_trailer):
          self.title = movietitle
          self.storyline  = movie_storyline
          self.poster_image_url = movie_poster
          self.trailer_youtube_url = movie_trailer

     def show_trailer(self):
          webbrowser.open_new_tab(self.trailer_youtube_url)


