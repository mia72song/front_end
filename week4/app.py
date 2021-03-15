from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["PERMANENT_SESSION_LIFETIME"] = 86400

@app.route("/")
def index():
    if session.get("user")==None:
        return render_template("index.html")
    else:
        return redirect(url_for("member"))

@app.route("/signin", methods=["POST", "GET"])
def signin():
    user={
        "username":"test",
        "password":"test"
        }
    if request.method!="POST":
        return redirect(url_for("index"))
    
    usr = request.form["username"]
    pwd = request.form["password"] 
    if usr==user["username"] and pwd==user["password"]:
        session["user"] = user["username"]
        #print(session["user"])
        return redirect(url_for("member"))
    else:
        return redirect(url_for("error"))

@app.route("/signout")
def signout():
    if session.get("user"):
        del session["user"]
    return redirect(url_for("index"))

@app.route("/member")
def member():
    if session.get("user"):
        return render_template("member.html")
    else:
        return redirect(url_for("index"))

@app.route("/error")
def error():
    if session.get("user"):
        return redirect(url_for("member"))
    else:
        return render_template("error.html")

if __name__=="__main__":
    app.run(port=3000)