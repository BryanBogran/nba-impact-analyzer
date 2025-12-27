from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load NBA data
df = pd.read_csv("data/nba_players.csv")

# home page route
@app.route("/")
def home():
    # send players name to the HTML page
    return render_template("index.html", players=df["Player"].tolist())

# run app
if __name__ == "__main__":
    app.run(debug=True)