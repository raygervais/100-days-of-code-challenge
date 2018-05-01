def get_user_name():

    # Get User's Name
    user_name = input("What's your name? ")

    while True:
    
        # Provided name was not valid
        if len(user_name) == 0:
            user_name = input ("Let's try that again, what is your name? ")
        else:
            break

    return user_name

name = get_user_name().capitalize()
print("Hello, " + name)
print(name + ", say hello to the world!")
