World of Games

World of Games is a Python-based project that contains several mini-games such as a Memory Game, Guess Game, and Currency Roulette Game. The project includes a scoring system, an end-to-end test suite, and a Flask-based web service to display the score.
Features

    Memory Game: Remember a sequence of numbers displayed for a short time.
    Guess Game: Guess a randomly generated number and see if it matches the computer’s choice.
    Currency Roulette Game: Guess the currency exchange value between USD and ILS.
    Score Management: Scores are tracked and accumulated across games.
    Web Service: Scores can be viewed via a Flask-based web service.
    End-to-End Testing: Includes automated tests using Selenium to validate the score web service.

Setup
Prerequisites:

    Python 3.8+
    Docker
    Docker Compose
    Jenkins (optional for CI/CD)

Installation:

    Clone the repository:

    bash

git clone https://github.com/yaroslav-skvortsov/WorldOfGames.git
cd WorldOfGames

Install Python dependencies:

`pip install -r requirements.txt`

Build the Docker image:

`docker-compose build`

Run the application:

`docker-compose up`

Access the Application

Flask App: Visit http://localhost:8777 to view the score.

To run test, use:

`python3 tests/e2e.py`
