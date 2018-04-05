import random
import sys
from user import User

def create_user (website, username, password):
    newUser = User(website, username, password)
    return newUser

def save_user (user):
    user.save_user()

def delete_user(user):
    user.delete_user()


def find_user(number):
    return User.find_by_number(number)


def check_existing_users(fname):
    return User.user_exist(fname)


def display_users():
    return User.display_users()

greeting_name = input("What is your name: ")
greeting_phrase = "Hello {}, Welcome to the password locker. With just a little input, I can store your passwords for all sorts of different websites.".format(greeting_name)
print(greeting_phrase)

while True:
    get_to_it = input("Shall we begin? (y or n)")
    if get_to_it == "y":
        print("OH YEAH!")
        break
    elif get_to_it == "n":
        print("Okay, goodbye!")
        print("*cough* Loser *cough*")
        sys.exit()
        break
    else:
        print("Please type in y or n!")

print("hi")
