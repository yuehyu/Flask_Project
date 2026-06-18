from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)

# @app.route("/")
# def index():
# 	return "Hi"
# @app.route("/world", methods=["GET"], endpoint='hi-world')
# def world():
# 	return "hi world!"
# @app.route("/hi/<name>")
# def hi_name(name):
# 	return render_template("index.html", name=name)

# with app.test_request_context():
#   print(url_for("index"))
#   print(url_for("hi_name", name="alan", page="1"))
#   print(url_for("static", filename="style.css"))

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
# @app.get("/contact/complete")
# @app.post("/contact/complete")
def contact_complete():
  if request.method == "POST":
    return redirect(url_for("contact_complete"))
  return render_template("contact_complete.html")