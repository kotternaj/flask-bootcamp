from user import User 

user = User('John')

user.add_movie('The matrix', 'Sci-Fi')
user.add_movie('The Interview', 'Comedy')

print(user.json())

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)

