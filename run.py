# Importing- Setting up Flask

import os
from flask import Flask, render_template, redirect, request, url_for



app = Flask(__name__)

# Routing

@app.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)