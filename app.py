from flask import Flask, render_template, request, redirect, send_file
from file import SearchAndCreateData

app = Flask(__name__)

DB = {}


@app.route("/")
def home():
    return render_template("index.html", name="Mangpha")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
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


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in DB:
        return redirect(f"/search?keyword={keyword}")
    SearchAndCreateData(keyword).CreateCSV(DB[keyword])
    return send_file(f"./jobs/{keyword}.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
