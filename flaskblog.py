from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello Corey!<h1>"

@app.route("/about")
def about():
    return "<h1>About Page<h1>"

@app.route("/kido")
def kido():
    return "<h1>Sup kido<h1>"


if __name__ == "__main__":
    app.run(debug=True)
