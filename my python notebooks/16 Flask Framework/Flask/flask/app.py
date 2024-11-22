# importing library

from flask import Flask,render_template

'''
This code helps to create a WSGI which inturn facilitates the interaction between Web application and web server.
why we need render template : We will create some aesthetic page for better visuals and interaction which can be developed using render_template.
    - This render template redirects the user from web application to html page.  
'''

# WSGI initialization
app = Flask(__name__)

# creating a homepage("/"), which is basically a decorator
@app.route("/")
def welcome():
    return "Welcome to the flask realm, This course is amazing"


# creating another page
@app.route("/index")
def index():
    return "Welcome to the index page ! "

'''
if the below is executed. 
This will be the starting point of the execution as this acts as entry point.
Post run this script then rest of them will be executed
'''


if __name__ == "__main__":
    app.run(debug=True) # why debug is needed : if this input is not given, then the changes made after the server hosting wont be reflected. So, we need changes simultaneously as we modify in the script.
                # on switching on the debug option, the server automatically restarts and highlights the changes
