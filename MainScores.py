from flask import Flask
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        # Attempt to read the score from the file
        with open(SCORES_FILE_NAME, "r") as file:
            score = file.read()
        # Return the score in an HTML page
        return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except Exception as e:
        # Return an error message in case of failure
        return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">Error: {str(e)}</div></h1>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)