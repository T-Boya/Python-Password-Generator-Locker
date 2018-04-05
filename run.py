import random
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
greeting_phrase = "Hello {}, Welcome to the password locker. With just a little input, I can store your passwords quickly and easily".format(greeting_name)
print(greeting_phrase)