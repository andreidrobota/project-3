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
    print("Welcome to the Lotto Game\n")

    lotto_game = Lotto()
    
    user_nums = set()
    for i in range(6):
        while True:
            try:
                number = int(input(f"Enter the {i+1} number between 1 and 49: "))
                if 1 <= number <= 49 and number not in user_nums:
                    user_nums.add(number)
                    break
                elif number in user_nums:
                    print("You already entered this number, pick a new one!")
                else:
                    print("Please enter a number between 1 and 49!")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 49...")
    
    lotto_nums = lotto_game.generate_numbers()
    print("Lotto numbers: ", lotto_nums)

    result = lotto_game.check_numbers(user_nums)
    print(result)

def start_lotto_multiplayer(num_players):
    """
    Function to be able to play multiplayer lotto
    based on the number of players from the users input
    """
    print(f"Welcome to the Multiplayer Lotto Game with {num_players} players")

    lotto_game = Lotto()
    players_data = []

    for player in range(1, num_players + 1):
        user_nums = set()
        for i in range(6):
            while True:
                try:
                    number = int(input(f"Player {player}, enter the {i+1} number between 1 and 49: "))
                    if 1 <= number <= 49 and number not in user_nums:
                        user_nums.add(number)
                        break
                    elif number in user_nums:
                        print("You already entered this number, pick a new one!")
                    else:
                        print("Please enter a number between 1 and 49!")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 49.")
        
        players_data.append((player, user_nums))
        print(f"\nPlayer {player} has finished entering numbers. \n")
    
    lotto_nums = lotto_game.generate_numbers()
    print("\nLotto numbers: ", lotto_nums)

    for player, user_nums in players_data:
        result = lotto_game.check_numbers(user_nums)
        print(f"\nPlayer {player}: {result}\n")

def main():
    """
    Main function to handle the users input
    and decide which mode to select
    """

    print("Welcome to the Lotto 6/49 Game!\n")

    while True:
        try:
            game_mode = int(input("Chose a gome mode:\n1. Single Player\n2. Multiplayer\n3. Quit\n"))

            if game_mode == 1:
                print("You selected Single Player... Starting!")
                start_lotto_game()
            elif game_mode == 2:
                print("You selected Multi Player... Starting!")
                num_players = int(input("Please enter number of players: "))
                start_lotto_multiplayer(num_players)
            elif game_mode == 3:
                print("Exiting game... Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1,2, or 3.")

main()