#importing essential files for the program to work 
import media
import fresh_tomatoes

#creating instances of class Movie
toy_story = media.Movie(
	"Toy Story",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)

Mohamed_story = media.Movie(
	"Muhammad Story",
	"A story of a boy who became a prophet",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNDRmYWRmNjctMmFkMy00MmE0LWE1ZTEtOWI5ZTY3OWU3MDBlXkEyXkFqcGdeQXVyMjExNjgyMTc@._V1_UY268_CR8,0,182,268_AL_.jpg",
	"https://www.youtube.com/watch?v=xYXoIXEsm2s"
	)

the_fog_is_lifting = media.Movie(
	"The Fog is Lifting",
	"What do you really know about Islam?",
	"https://australianculturalfund.org.au/wp-content/uploads/2017/04/Screen-Shot-2017-05-30-at-5.18.43-pm-753x960.png",
	"https://www.youtube.com/watch?v=S3bs67FXLE8&list=PL30A23D29A4C76451"
	)

islam_in_women = media.Movie(
	"Islam in Women",
	"Are women in Islam oppressed?",
	"https://scontent-cai1-1.xx.fbcdn.net/v/t1.0-9/22046934_785659588288065_5574885058776354699_n.jpg?oh=a16847ef560b65c301f537f49b90345e&oe=5A3EEFE4",
	"https://www.youtube.com/watch?v=mZVZxWPEZT0"
	)

Mulan = media.Movie(
	"Mulan",
	"A story of a girl who saved her father",
	"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-1c13wdp_596c4400.jpeg?region=0,0,300,450",
	"https://www.youtube.com/watch?v=sEQjLQA9qW4"
	)
Bilal = media.Movie(
	"Bilal",
	"A story of a boy who will challange everything!",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BZGIwMDhmZjgtOGEyNi00NGQzLTk3ZTEtOTc0ZTJiZTdkZmE3XkEyXkFqcGdeQXVyMTYxMzQzNTU@._V1_UY1200_CR65,0,630,1200_AL_.jpg",
	"https://www.youtube.com/watch?v=X7ifDf6chNw"
	)

#making a list of the movies 
Movies = [toy_story,Mohamed_story,the_fog_is_lifting,islam_in_women,Mulan,Bilal]

#passing the list of movies to the open_movies_page fun to create the html page 
fresh_tomatoes.open_movies_page(Movies)
