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


def displayCredentials():
    return User.displayCredentials()

greeting_name = input("What is your name: ")
greeting_phrase = "Hello {}, Welcome to the password locker. With just a little input, I can store your passwords for all sorts of different websites.".format(greeting_name)
print(greeting_phrase)

while True:
    get_to_it = input("Shall we begin? (y or n): ")
    if get_to_it == "y":
        print("OH YEAH!")
        break
    elif get_to_it == "n":
        print("Okay, goodbye!")
        sys.exit()
        break
    else:
        print("Please type in y or n!: ")

# print("So, here's how it works:")
# print("I store can generate passwords or store login information for a website (or several)")
print("So, here's what you can do!:")
print("Display all user accounts (display)")
print("Search for the credentials for a specific website account (search)")
print("Delete a website account(delete)")
print("Generate a password (password)")
print("And exit :( (shutdown)")
print("Psst. You can also see you option again (options)")
# if function_choice == display:

# elif function_choice == search:

# elif function_choice == delete:
while True:
    function_choice = input("Which would you like to do?: ")
    if function_choice == "display":
        if displayCredentials():
            for user in displayCredentials():
                # print(f"{user.website}{user.username}{user.password}")
                print ("")
                print ("Website: {}".format(user.website))
                print ("Username: {}".format(user.username))
                print ("Password: {}".format(user.password))
                print ("")
                break
            while True:
                continue_usage = input("Would you like to continue? (y or n): ")
                if continue_usage == "y":
                    break
                    continue
                elif continue_usage == "n":
                    print("Okay, goodbye!")
                    sys.exit()
                    break
                else:
                    print("Please type in y or n!")
        else:
            print("You don't have any account data!")
            while True:
                continue_usage = input("Would you like to continue? (y or n): ")
                if continue_usage == "y":
                    break
                    continue
                elif continue_usage == "n":
                    print("Okay, goodbye!")
                    sys.exit()
                    break
                else:
                    print("Please type in y or n!")
            

    if function_choice == "password":
        print("your password will be a randomly generated 7 digit number")
        while True:
            store_password = input("Do you want to store this passord? (y or n)?: ")
            if store_password == "y":
                print("To store this however, I am going to have to ask you two (simple) questions")
                password_website = input("What website is this for?: ")
                password_username = input("What is your username?: ")
                password_generated_saved = str(random.randint(1000000, 10000000))
                print("Your password is " + password_generated_saved)
                save_user(create_user(password_website, password_username, password_generated_saved))
                print("Your information has been saved")
                while True:
                    continue_usage = input("Would you like to continue? (y or n): ")
                    if continue_usage == "y":
                        break
                    elif continue_usage == "n":
                        print("Okay, goodbye!")
                        sys.exit()
                        break
                    else:
                        print("Please type in y or n!")
                
            elif store_password == "n":
                password = random.randint(1000000, 10000000)
                print("Your password is " + str(password))
                while True:
                    continue_usage = input("Would you like to continue? (y or n): ")
                    if continue_usage == "y":
                        break
                    elif continue_usage == "n":
                        print("Okay, goodbye!")
                        sys.exit()
                        break
                    else:
                        print("Please type in y or n!")
                    break
            else:
                print("Please type in y or n!")
            break

    elif function_choice == "shutdown":
        print("Goodbye!")
        sys.exit()

    elif function_choice == "options":
        print("So, here's what you can do!:")
        print("Display all user accounts (display)")
        print("Search for the credentials for a specific website account (search)")
        print("Delete a website account(delete)")
        print("Generate a password (password)")
        print("And exit :( (shutdown)")

    else:
        print("Please enter a valid option!")
    continue


# # while True:
# #     function = input("Which would you like to do store, account information (si) or generate a password (gp)?: ")
# #     if function == "si":
# #         print("OH YEAH!")
# #         break
# #     elif function == "gp":
#         print("your password will be a randomly generated 7 digit number")
#         while True:
#             store_password = input("Do you want to store this passord? (y or n)?: ")
#             if store_password == "y":
#                 print("To store this however, I am going to have to ask you two (simple) questions")
#                 password_website = input("What website is this for?: ")
#                 password_username = input("What is your username?: ")
#                 password_generated_saved = str(random.randint(1000000, 10000000))
#                 print("Your password is " + password_generated_saved)
#                 save_user(create_user(password_website, password_username, password_generated_saved))
#                 print("Your information has been saved")
#                 # while True:
#                 #     continue_usage = input("Would you like to continue?: ")
#                 #     if continue_usage == "y":
#                 #         break
#                 #     elif continue_usage == "n":
#                 #         print("Okay, goodbye!")
#                 #         sys.exit()
#                 #         break
#                 #     else:
#                 #         print("Please type in y or n!")
#                 break
#             elif store_password == "n":
#                 password = random.randint(1000000, 10000000)
#                 print("Your password is " + str(password))
#                 print("Goodbye!")
#                 sys.exit()
#                 break
#             else:
#                 print("Please type in y or n!")
# #     else:
# #         print("Please type in gp or si!")

