from user import User
from movie import Movie
# Test the functions/init of these classes
# Test putting and pulling to/from the database

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
	
	"""
	user = User('testuser')
	movie2 = Movie('other', ['Action', 'Comedy'], ['Disney+', 'Amazon Instant Video'])
	user.add_rating(movie2, 5)
	user.add_rating(movie, 3)
	print(user.ratings)
	print(user.vector)
	print(user.get_recs())
	assert 2 == 3
	"""
	
def test_pass():
	assert 5 == 5
	