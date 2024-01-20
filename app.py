from flask import Flask, render_template, request
from file import SearchAndCreateData

app = Flask(__name__)

DB = {}


@app.route("/")
def home():
    return render_template("index.html", name="Mangpha")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # keywords = [
    #     "flutter",
    #     "python",
    #     "kotlin",
    # ]

    # for i in range(len(keywords)):
    #     data = SearchAndCreateData(keywords[i])
    #     DB[keywords[i]] = data.Search()
    #     data.CreateCSV(DB[keywords[i]])
    if keyword not in DB:
        data = SearchAndCreateData(keyword)
        DB[keyword] = data.Search()
    return render_template("search.html", keyword=keyword, jobs=DB[keyword])


if __name__ == "__main__":
    app.run(debug=True)
