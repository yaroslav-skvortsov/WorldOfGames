import requests
import random

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.amount_usd = None
        self.exchange_rate = None
        self.amount_ils = None

    def get_exchange_rate(self):
        url = "https://v6.exchangerate-api.com/v6/7fae091b571f63c863a8af0d/latest/USD"
        response = requests.get(url)
        data = response.json()
        self.exchange_rate = data["conversion_rates"]["ILS"]

    def generate_amount_usd(self):
        self.amount_usd = random.randint(1, 100)

    def calculate_amount_ils(self):
        self.amount_ils = self.amount_usd * self.exchange_rate

    def get_guess_from_user(self):
        while True:
            try:
                guess = float(input(f"Guess the value of {self.amount_usd} USD in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compare_results(self, guess):
        margin = 5 - self.difficulty
        lower_bound = self.amount_ils - margin
        upper_bound = self.amount_ils + margin
        return lower_bound <= guess <= upper_bound

    def play(self):
        self.get_exchange_rate()
        self.generate_amount_usd()
        self.calculate_amount_ils()
        guess = self.get_guess_from_user()
        return self.compare_results(guess)