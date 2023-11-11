import random

# Lotto Class

class Lotto:
    """ Lotto class"""
    def __init__(self):
        self.lotto_nums = []
    
    def generate_numbers(self):
        """
        Generates six random numbers from 1 to 49
        Returns the numbers in a list
        """
        self.lotto_nums = random.sample(range(1, 50), 6)

        return self.lotto_nums
    
    def check_numbers(self, user_nums):
        """
        Check if the users numbers match the current combination,
        and how many nymbers the user get
        """
        match_nums = set(user_nums).intersection(set(self.lotto_nums))

        if len(match_nums) == 0:
            return "Bad Luck! None of your numbers are between the lotto numbers. Better Luck next time!"
        elif len(match_nums) == 1:
            return "Good job! You got one number right, keep it up!"
        elif len(match_nums) == 2:
            return "Good job! You got two numbers right, keep it up!"
        elif len(match_nums) == 3:
            return "Good job! You got three numbers right, keep it up!"
        elif len(match_nums) == 4:
            return "Good job! You got four numbers right, keep it up!"
        elif len(match_nums) == 5:
            return "Good job! You got five numbers right, keep it up!"
        else:
            return "WOW! You got all the 6 numbers right! You are a good contestant!"


def start_lotto_game():
    """
    Function to start the Lotto Game
    """
    lotto_game = Lotto()
    
    user_nums = []
    for i in range(6):
        while True:
        number = int(input(f"Enter the {i+1} number between 1 and 49: "))
        if 1 <= number <= 49:
            break
        else:
            print(Please enter a number between 1 and 49!)
        user_nums.append(number)
    
    lotto_nums = lotto_game.generate_numbers()
    print("Lotto numbers: ", lotto_nums)

    result = lotto_game.check_numbers(user_nums)
    print(result)

start_lotto_game()