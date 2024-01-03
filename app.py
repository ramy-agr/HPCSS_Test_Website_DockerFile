# To run in VS CTRL + F5
# To run outside VS:
# Set an environment variable for FLASK_APP. On Linux and macOS, use export set FLASK_APP=webapp; on Windows use $env:FLASK_APP=webapp if you're using PowerShell, or set FLASK_APP=webapp if you're using Command Prompt.
# Navigate into the hello_app folder, then launch the program using python -m flask run.

from flask import Flask, redirect, url_for, request, render_template, session
from flask import Flask
from flask import render_template
from datetime import datetime
import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)



@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
