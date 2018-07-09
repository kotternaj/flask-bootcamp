from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

# BCRYPT
bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)

bcrypt.check_password_hash(hashed_password, 'wrongpassword')

bcryp.check_password_hash(hashed_password, 'supersecretpassword')

# WERKZEUG

hashed_pass = generate_password_hash('mypassword')

check = check_password_hash(hashed_pass, 'wrong')

check = check_password_hash(hashed_pass, 'mypassword')


