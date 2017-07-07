import media
import fresh_tomatoes

# Instances of class movies
kings_speech = media.Movie(
	"King's Speech",
	"England's Prince Albert must ascend the throne as King George VI,\
	but he has a speech impediment.",
	"http://www.impawards.com/2010/posters/kings_speech.jpg",
	"https://www.youtube.com/watch?v=pzI4D6dyp_o")

salt = media.Movie(
	"Salt",
	"A Story of double agent officer",
	"http://www.gstatic.com/tv/thumb/movieposters/7937523/p7937523_p_v8_af.jpg",
	"https://www.youtube.com/watch?v=QZ40WlshNwU")

the_rock = media.Movie(
	"The Rock",
	"FBI chemical warfare expert is sent on an urgent mission\
	with a former British spy",
	"http://t1.gstatic.com/images?q=tbn:\
	ANd9GcQng4rV8ypQDPngFy1cnv38jhe_SzB88qiCmdVOko5j2GnsP07Q",
	"https://www.youtube.com/watch?v=vapdvjBcQzs")

private_ryan = media.Movie(
	"Saving Private Ryan",
	"A Captain takes his men behind enemy lines to find Private Ryan",
	"http://t2.gstatic.com/images?q=tbn:\
	ANd9GcR0lDhR_dXAKTm9wysp3nWu6kP0V5skJBVbCNC_Q8urAWcr4iF_",
	"https://www.youtube.com/watch?v=zwhP5b4tD6g")

sully = media.Movie(
	"Sully",
	"A Captain tries to make an emergency landing in New York's Hudson River",
	"http://t1.gstatic.com/images?q=tbn:\
	ANd9GcS9yR6SXAsICEMPTSdGkb57DJ62JsTg6S5fdQvnPngAhBD7AuYv",
	"https://www.youtube.com/watch?v=mjKEXxO2KNE")

monsters_inc = media.Movie(
	"Monsters Inc.",
	"A scare factory in the monster world",
	"http://t2.gstatic.com/images?q=\
	tbn:ANd9GcTaeFK9RkQM00A7cbfc2iI3C573rSkbsubdyrY-ZZnT4jk0O_cB",
	"https://www.youtube.com/watch?v=8IBNZ6O2kMk")

# List of movies:
movies = [kings_speech, salt, the_rock, private_ryan, sully, monsters_inc]

fresh_tomatoes.open_movies_page(movies)
