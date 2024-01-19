from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Mangpha")


@app.route("/hello")
def hello():
    return "Hi There"


if __name__ == "__main__":
    app.run(debug=True)
