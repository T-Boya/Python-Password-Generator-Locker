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


def find_user(username):
    return User.find_by_username(username)

def userFound(username):
    return User.userFound(username)


def displayCredentials():
    return User.displayCredentials()

greeting_name = input("What is your name: ")
greeting_phrase = "Hello {}, welcome to the password locker. With just a little input, I can store your passwords for all sorts of different websites.".format(greeting_name)
print(greeting_phrase)

while True:
    get_to_it = input("Shall we begin? (y or n): ")
    if get_to_it == "y":
        print("OH YEAH!")
        print("")
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
print("Create an account for storage (create)")
print("Display all user accounts (display)")
print("Search for the credentials for a specific website account (search)")
print("Delete a website account(delete)")
print("Generate a password (password)")
print("And exit :( (shutdown)")
print("Psst. You can also see you option again (options)")
print("")

while True:
    function_choice = input("Which would you like to do?: ")
    if function_choice == "display":
        if displayCredentials():
            for user in displayCredentials():
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

    if function_choice == "create":
        create_website = input("What wesbite is this for?: ")
        create_username = input("What is your username?: ")
        create_password = input("what is your password?: ")
        save_user(create_user(create_website, create_username, create_password))
        print("Your information has been saved")
        while True:
            continue_usage = input("Would you like to continue? (y or n): ")
            if continue_usage == "y":
                break
                break
                continue
            elif continue_usage == "n":
                print("Okay, goodbye!")
                sys.exit()
                break
            else:
                print("Please type in y or n!")


    if function_choice == "search":
        searched_username = input("What is the username for the account that you want to search for?: ")
        if userFound(searched_username):
            print("These are the credentials:")
            found_username = find_user(User, searched_username)
            print ("Website: {}".format(searched_username.website))
            print ("Username: {}".format(searched_username.username))
            print ("Password: {}".format(searched_username.password))
            print ("")

        else:
            print("We do not have that account's data")

    if function_choice == "delete":
        account_to_delete = input("What is the username of the credential set you want to delete?: ")
        if userFound(account_to_delete):
            searchDelete = find_user(account_to_delete)
            delete_user(searchDelete)
            print("The following has been deleted: ")
            print ("Website: {}".format(searched_username.website))
            print ("Username: {}".format(searched_username.username))
            print ("Password: {}".format(searched_username.password))
            delete_user(search_delete_user)
    
        else:
            print("We do not have that account's data")


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
        print("Create an account for storage (create)")
        print("Display all user accounts (display)")
        print("Search for the credentials for a specific website account (search)")
        print("Delete a website account(delete)")
        print("Generate a password (password)")
        print("And exit :( (shutdown)")

    else:
        print("Please enter a valid option!")
    continue