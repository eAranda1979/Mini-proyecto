from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "password"
app.permanent_session_lifetime = timedelta(days=90)

@app.route("/")
def home():
	return render_template("base.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		flash("Login Succesful")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already Logged In")
			return redirect(url_for("user"))

		return render_template("login.html")#

@app.route("/SendFunds")
def SendFunds():
	return render_template("sendfunds.html")

@app.route("/Blockchain")
def Blockchain():
	return render_template("blockchain.html")

@app.route("/ManageAccounts")
def ManageAccounts():
	return render_template("manacc.html")

@app.route("/logout")
def logout():
	flash(f"You have been logged out", "info")
	session.pop("user", None)
	session.pop("email", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)