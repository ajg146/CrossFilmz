from user import User
from movie import Movie
# Test the functions/init of these classes
# Test putting and pulling to/from the database

# https://docs.pytest.org/en/latest/contents.html

def test_user_get_ratings():
	user = User('UserThatHasNotRatedAnythingYet')
	assert user.get_ratings() == {}
	
def test_fail():
	assert 3 == 5
	
def test_pass():
	assert 5 == 5
	