# importing library

from flask import Flask, render_template


# WSGI initialization
app = Flask(__name__)

# creating a homepage("/"), which is basically a decorator
@app.route("/")
def welcome():
    return "<html><H1> Welcome to the Flask course </H1></html>"

# creating another page
@app.route("/index")
def index():
    return render_template("index.html") # where do we create this index.html file ?? so that the user can be redirected ? : Use Jinja2


@app.route("/about")
def about():
    return render_template("about.html")

# Jinja 2 looks for supporting files within the templates folder, where the other files are hosted.

if __name__ == "__main__":
    app.run(debug=True)
