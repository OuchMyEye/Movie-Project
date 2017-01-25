import media
import fresh_tomatoes

destino = media.Movie(
"Destino",
"Dali & Disney collaborate on a surreal animation short",
"https://images-na.ssl-images-amazon.com/images/M/MV5BYTlkOTUxYWUtMzNhMS00ZDRiLTg4ZjYtNmFlNzE3ZWFjODA5XkEyXkFqcGdeQXVyMjExNjgyMTc@._V1_.jpg",
"https://www.youtube.com/watch?v=1GFkN4deuZU")

lebowski = media.Movie(
"The Big Lebowski",
"Los Angeles slacker gets caught up in a bizzare case of mistaken identity",
"https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
"https://www.youtube.com/watch?v=cd-go0oBF4Y")

polyester = media.Movie(
"Polyester",
"Francine Fishpaw's downward spiral in a Baltimore suburan hell",
"https://upload.wikimedia.org/wikipedia/en/b/bc/Polyester_ver1.jpg",
"https://www.youtube.com/watch?v=fwtbY9zfOMA")

party = media.Movie(
"24 Hour Party People",
"Documentary/Comedy about the early punk and rave scene in Manchester",
"https://upload.wikimedia.org/wikipedia/en/d/d0/24_Hour_Party_People_quad_poster.jpg",
"https://www.youtube.com/watch?v=q2PYyvGFHD8")

friday = media.Movie(
"Friday",
"Ice Cube and Chris Tucker spent a Friday in their hood",
"https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
"https://www.youtube.com/watch?v=nH1Ulp4PBtA")

hedwig = media.Movie(
"Hedwig & the Angry Inch",
"East Berlin trans woman escapes to America and becomes rockstar",
"https://upload.wikimedia.org/wikipedia/en/6/62/HedwigandtheAngryInchMoviePoster.jpg",
"https://www.youtube.com/watch?v=4p9mPhGo1j0")

flicks = [destino, lebowski, polyester, party, friday, hedwig]
fresh_tomatoes.open_movies_page(flicks)
