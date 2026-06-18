from flask import Flask, render_template, url_for, redirect, request, flash
from email_validator import validate_email, EmailNotValidError
import logging
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "8Y3U1E0H28"
app.logger.setLevel(logging.DEBUG)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")




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
    username = request.form["username"]
    email = request.form["email"]
    description = request.form["description"]
    is_valid = True
    if not username:
      flash("必須填寫使用者名稱")
      is_valid = False
    if not email:
      flash("必須輸入郵件位址")
      is_valid = False
    try:
      validate_email(email)
    except EmailNotValidError:
      flash("請輸入正確的郵件格式")
      is_valid = False
    if not description:
      flash("必須填寫諮詢內容")
      is_valid = False
    if not is_valid:
      return redirect(url_for("contact"))
    flash("諮詢內容已傳送，感謝您的來信諮詢。")
    return redirect(url_for("contact_complete"))
  return render_template("contact_complete.html")