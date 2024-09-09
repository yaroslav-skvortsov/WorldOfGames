import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def display_sequence(self):
        print("Remember the following sequence:")
        for num in self.sequence:
            print(num, end=' ', flush=True)
        time.sleep(0.7)
        print("\033[H\033[J")  # Clear the console

    def get_list_from_user(self):
        print("Enter the numbers you remember, separated by spaces:")
        while True:
            try:
                user_input = input()
                user_sequence = [int(num) for num in user_input.split()]
                if len(user_sequence) == self.difficulty:
                    return user_sequence
                else:
                    print(f"Please enter exactly {self.difficulty} numbers.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        self.generate_sequence()
        self.display_sequence()
        user_sequence = self.get_list_from_user()
        return self.is_list_equal(self.sequence, user_sequence)