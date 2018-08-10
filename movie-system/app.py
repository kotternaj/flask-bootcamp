
from user import User 

user = User('John')

user.add_movie("The Thing", "Horror")
user.add_movie("The Matrix", "Sci-Fi")

user.save_to_file()

