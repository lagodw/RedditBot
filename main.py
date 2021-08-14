from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("subreddit", "")
    test = request.args.get("title", "")
    test = request.args.get("prompt", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Subreddit: <input type="text" name="subreddit">
                <br>
                <br>
                Thread Title: <input type="text" name="title">
                <br>
                <br>
                Prompt: <input type="text" name="prompt">
                <br>
                <br>
                <input type="submit" value="Generate">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
        + test
    )

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)