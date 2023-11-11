import random

# Lotto Class

class Lotto:
    """ Lotto class"""
    def __init__(self):
        self.lotto_numbers = []
    
    def generate_numbers(self):
        """
        Generates six random numbers from 1 to 49
        Returns the numbers in a list
        """
        self.lotto_numbers = random.sample(range(1, 50), 6)

        return self.lotto_numbers
    
    


def lotto_game():
    """
    Function to start the Lotto Game
    """


lotto_game()