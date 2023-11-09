from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauthlib.client import OAuth
import datetime
import requests

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["GOOGLE_ID"] = "YOUR_GOOGLE_CLIENT_ID"
app.config["GOOGLE_SECRET"] = "YOUR_GOOGLE_CLIENT_SECRET"

app.config["SESSION_TYPE"] = "filesystem"
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

oauth = OAuth(app)
google = oauth.remote_app(
    "google",
    consumer_key=app.config.get("GOOGLE_ID"),
    consumer_secret=app.config.get("GOOGLE_SECRET"),
    request_token_params={
        "scope": "email profile",
    },
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)


@app.route("/")
def index():
    if "google_token" in session:
        user_info = google.get("userinfo")
        picture_url = user_info.data["picture"]
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_email = user_info.data["email"]
        user_name = user_info.data["name"]
        return render_template(
            "index.html",
            name=user_name,
            email=user_email,
            picture_url=picture_url,
            current_time=current_time,
        )
    return render_template("index.html")


@app.route("/login")
def login():
    return google.authorize(callback=url_for("authorized", _external=True))


@app.route("/logout")
def logout():
    session.pop("google_token", None)
    return redirect(url_for("index"))


@app.route("/login/authorized")
def authorized():
    response = google.authorized_response()
    if response is None or response.get("access_token") is None:
        return "Access denied: reason={} error={}".format(
            request.args["error_reason"], request.args["error_description"]
        )
    session["google_token"] = (response["access_token"], "")
    return redirect(url_for("index"))


@google.tokengetter
def get_google_oauth_token():
    return session.get("google_token")


if __name__ == "__main__":
    app.run(debug=True)
