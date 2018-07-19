from user import User
from database import Database

Database.initialize(user='postgres', password='1234',database='learning', host='localhost')

user = User('teom@smith.com', 'Rolf', 'Smith', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('bob@smith.com')

print(user_from_db)



