from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    name = 'Ali'
    return render_template("index.html", n=name)


if __name__ == "__main__":
    app.run(debug=True)
