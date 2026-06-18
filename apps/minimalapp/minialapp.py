from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def index():
	return "Hi"
@app.route("/world", methods=["GET"], endpoint='hi-world')
def world():
	return "hi world!"
@app.route("/hi/<name>")
def hi_name(name):
	return render_template("index.html", name=name)

with app.test_request_context():
  print(url_for("index"))
  print(url_for("hi_name", name="alan", page="1"))
  print(url_for("static", filename="style.css"))