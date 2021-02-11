SNOWMAN_WORD = "broccoli"

def get_letter():
    user_guess = input("Please type a letter in: ")

    while not user_guess.isalpha() or len(user_guess) != 1:
        if not user_guess.isalpha():
            user_guess = input("Please type a LETTER!!! ")
        else:
            user_guess = input("Please type ONE letter!!! ")
    
    return user_guess

def snow_check():