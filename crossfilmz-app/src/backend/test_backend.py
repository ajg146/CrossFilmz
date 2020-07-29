import random
from user import User
from movie import Movie
from db_scripts import populate_db
import db_ops

# pytest documentation
# https://docs.pytest.org/en/latest/contents.html

def test_user_functions():
	# Empty ratings set (also adds user to database)
	user = User('UserThatHasNotRatedAnythingYet')
	assert user.get_ratings() == {}
	
	# Adding ratings to set
	movie_1 = Movie('SomeMovie', ['Action', 'Crime', 'Biography'], ['Netflix', 'Disney+'])
	movie_2 = Movie('AnotherMovie', ['Comedy', 'Thriller', 'Sci-Fi'], ['Hulu'])
	user.add_rating(movie_1, 5)
	user.add_rating(movie_2, 1)
	assert user.get_ratings() == {'SomeMovie': 5, 'AnotherMovie': 1}
	
	# Overwriting the ratings (in different order)
	user.add_rating(movie_2, 1)
	user.add_rating(movie_1, 3)
	assert user.get_ratings() == {'SomeMovie': 3, 'AnotherMovie': 1}
	
	# get_recs should return some movie recommendations
	assert user.get_recs() != {}
	

def test_movie_functions():
	# Add a new movie to the database (highly unlikely it will already exist)
	len_in = len(Movie.select_all_movies())
	add_movie = Movie('Star Wars: Episode '+str(random.random()*10), ['Action', 'Sci-Fi', 'Drama', 'Horror'], ['Disney+'])
	len_out = len(Movie.select_all_movies())
	assert len_in < len_out
	assert len_out == len_in + 1
	
def test_populate_db():
	# The Utelly API in get_availability has limited API calls, removed from testing
	# assert populate_db.get_availability('tt0374900') == {}

	# OMDb API samples should match what they actually return us
	assert populate_db.get_tags('Rushmore') == {"Title":"Rushmore","Year":"1998","Rated":"R","Released":"19 Feb 1999","Runtime":"93 min","Genre":"Comedy, Drama","Director":"Wes Anderson","Writer":"Wes Anderson, Owen Wilson","Actors":"Jason Schwartzman, Bill Murray, Olivia Williams, Seymour Cassel","Plot":"The extracurricular king of Rushmore Preparatory School is put on academic probation.","Language":"English, Spanish, Latin, French","Country":"USA","Awards":"Nominated for 1 Golden Globe. Another 16 wins & 15 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMjE2OTc3OTk2M15BMl5BanBnXkFtZTgwMjg2NjIyMDE@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.7/10"},{"Source":"Rotten Tomatoes","Value":"89%"},{"Source":"Metacritic","Value":"86/100"}],"Metascore":"86","imdbRating":"7.7","imdbVotes":"164,730","imdbID":"tt0128445","Type":"movie","DVD":"29 Jun 1999","BoxOffice":"N/A","Production":"Touchstone Pictures","Website":"N/A","Response":"True"}
	assert populate_db.get_tags('Shrek the Halls') == {"Title":"Shrek the Halls","Year":"2007","Rated":"TV-PG","Released":"28 Nov 2007","Runtime":"21 min","Genre":"Animation, Short, Adventure, Comedy, Family, Fantasy","Director":"Gary Trousdale","Writer":"Gary Trousdale (screenplay), Sean Bishop (screenplay), Theresa Cullen (screenplay), Bill Riling (screenplay), William Steig (book)","Actors":"Mike Myers, Eddie Murphy, Cameron Diaz, Antonio Banderas","Plot":"This half-hour animated TV special features the Shrek characters putting their own spin on holiday traditions.","Language":"English","Country":"USA","Awards":"4 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BZDE0NGZkOGMtNGY4My00OTM4LTliM2MtM2Y5OTVjOTFmNTA5XkEyXkFqcGdeQXVyNDgyODgxNjE@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.4/10"}],"Metascore":"N/A","imdbRating":"6.4","imdbVotes":"12,317","imdbID":"tt0897387","Type":"movie","DVD":"04 Nov 2008","BoxOffice":"N/A","Production":"DreamWorks Animation","Website":"N/A","Response":"True"}
	assert populate_db.get_tags('School of Rock') == {"Title":"School of Rock","Year":"2003","Rated":"PG-13","Released":"03 Oct 2003","Runtime":"109 min","Genre":"Comedy, Music","Director":"Richard Linklater","Writer":"Mike White","Actors":"Jack Black, Adam Pascal, Lucas Papaelias, Chris Stack","Plot":"After being kicked out of his rock band, Dewey Finn becomes a substitute teacher of an uptight elementary private school, only to try and turn his class into a rock band.","Language":"English","Country":"USA, Germany","Awards":"Nominated for 1 Golden Globe. Another 8 wins & 22 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.1/10"},{"Source":"Rotten Tomatoes","Value":"91%"},{"Source":"Metacritic","Value":"82/100"}],"Metascore":"82","imdbRating":"7.1","imdbVotes":"259,888","imdbID":"tt0332379","Type":"movie","DVD":"02 Mar 2004","BoxOffice":"$81,200,000","Production":"Paramount Pictures","Website":"N/A","Response":"True"}
	assert populate_db.get_tags('Napoleon Dynamite') == {"Title":"Napoleon Dynamite","Year":"2004","Rated":"PG","Released":"27 Aug 2004","Runtime":"96 min","Genre":"Comedy","Director":"Jared Hess","Writer":"Jared Hess, Jerusha Hess","Actors":"Jon Heder, Jon Gries, Aaron Ruell, Efren Ramirez","Plot":"A listless and alienated teenager decides to help his new friend win the class presidency in their small western high school, while he must deal with his bizarre family life back home.","Language":"English","Country":"USA","Awards":"10 wins & 22 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.9/10"},{"Source":"Rotten Tomatoes","Value":"71%"},{"Source":"Metacritic","Value":"64/100"}],"Metascore":"64","imdbRating":"6.9","imdbVotes":"193,466","imdbID":"tt0374900","Type":"movie","DVD":"21 Dec 2004","BoxOffice":"$44,478,018","Production":"Fox Searchlight Pictures","Website":"N/A","Response":"True"}
	
def test_db_ops():
	# db_ops are basically already tested because the classes use these functions,
	# but this is a more formal proof of that
	conn, cur = db_ops.open_db_conn()

	sql_command = """
		SELECT *
		FROM movies"""
	cur.execute(sql_command)
	movies_in = len(cur.fetchall())

	# Same idea as before
	add_movie = Movie('Star Wars: Episode '+str(random.random()*100), ['Action', 'Sci-Fi', 'Drama', 'Horror'], ['Disney+'])

	sql_command = """
		SELECT *
		FROM movies"""
	cur.execute(sql_command)
	movies_out = len(cur.fetchall())

	assert movies_in < movies_out
	assert movies_out == movies_in + 1