from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        input_crops= request.form.getlist("crop_check")
        input_month= request.form.get("month_check")
        found = []
        conn = sqlite3.connect("map_hilites.db")
        c = conn.cursor()
        for i in input_crops:
            c.execute("SELECT path FROM maps WHERE crop=? AND month=?", (i, input_month))
            found.append(c.fetchall())
        conn.close()
        return render_template("home.html", results = found)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(port=5003, debug = True)
