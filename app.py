from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Zank')
client = MongoClient(host=host)
db = client.get_default_database()
codes = db.codes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html", codes=codes.find())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/codes", methods=["GET", "POST"])
def insert_code():
    code = {
        "title": request.get("title"),
        "description": request.get("description"),
        "examples": "img",
        "last_revised": "MM-DD-YYYY",
        "duration_period": "4 years"
        [
            "title": "101",
            "description": "abc",
            "examples": "img",
            "last_revised": "1-04-2006",
            "duration_period": "6 years"
        ]
    }

    result = codes.find_one('title' == search_query)

    code_id = codes.insert_one(code).inserted_id
    print(f"added code id: {code_id}")
    return redirect(url_for("index", code_id=code_id))


@app.route("/search", methods=['POST'])
def search_codes():
    query = request.get("title")
    result = codes.find_one('title', query)
    code_id = result.get('_id')

    return redirect(url_for('show_code', code_id=code_id))


@app.route("/codes/<code_id>", methods=['GET', 'POST'])
def show_code(code_id):
    result = dbs.codes.select().where(dbs.codes.id == code_id).first()
    # code_list = []
    # for i in code:
    #     code = {
    #     "title": request.get("title"),
    #     "description": request.get("description"),
    #     "examples": "img",
    #     "last_revised": "MM-DD-YYYY",
    #     "duration_period": "4 years"
    # }

    # code = codes.find_one({'_id': ObjectId(code_id)})
    return render_template("detail.html", code=code, code_id=code_id)

# query param find_all() in code through text.


@app.route("/results")
def results():
    # search_query
    return render_template("results.html")  # search_query=search_query, code_id=code_id)


@app.route("/details")
def details():
    # code_id
    return render_template("details.html")  # code_id=code_id)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
