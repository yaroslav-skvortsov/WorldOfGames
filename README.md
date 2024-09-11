World of Games

World of Games is a Python-based project that contains several mini-games such as a Memory Game, Guess Game, and Currency Roulette Game. The project includes a scoring system, an end-to-end test suite, and a Flask-based web service to display the score.

Features:

1. Memory Game: Remember a sequence of numbers displayed for a short time.
2. Guess Game: Guess a randomly generated number and see if it matches the computer’s choice.
3. Currency Roulette Game: Guess the currency exchange value between USD and ILS.
4. Score Management: Scores are tracked and accumulated across games.
5. Web Service: Scores can be viewed via a Flask-based web service.
6. End-to-End Testing: Includes automated tests using Selenium to validate the score web service.

Setup
Prerequisites:

    Python 3.8+
    Docker
    Jenkins (optional for CI/CD)

Installation:

`git clone https://github.com/yaroslav-skvortsov/WorldOfGames.git`

`cd WorldOfGames`


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
