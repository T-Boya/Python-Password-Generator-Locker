#!/usr/bin/env python3.6


class User:
    UserAccounts = []


    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def save_user(self):
        User.UserAccounts.append(self)

    def deleteUser(self):
        User.UserAccounts.remove(self)

    def find_by_username(cls, username):
        for user in cls.UserAccounts:
            if user.username == username:
                return user
    
    def userFound(cls, username):
        for user in cls.UserAccounts:
            if user.username == username:
                return True
        
        return False

    @classmethod
    def displayCredentials(cls):
        return cls.UserAccounts
        


