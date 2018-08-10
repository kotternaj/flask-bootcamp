
from user import User 

user = User.load_from_file('John.txt')

print(user.movies)

