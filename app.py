#Objective of App is for user to keep track of what movies they have watched..

from movie import Movie
from user import User
import json





user=User.load_from_file("James.txt")
print(user.json)

with open("myfile.txt", "w") as f:
    json.dump(user.json(), f)
