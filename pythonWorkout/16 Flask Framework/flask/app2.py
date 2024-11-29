# importing library

from flask import Flask,render_template,request

'''
This code helps to create a WSGI which inturn facilitates the interaction between Web application and web server.
why we need render template : We will create some aesthetic page for better visuals and interaction which can be developed using render_template.
    - This render template redirects the user from web application to html page.  
'''

'''
Discussing about 
1. variable rule 
2. dynamic url 
3. Jinja 2 template : this enables the storage of information and showcasing the result in the final web-page.

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
    return render_template('index.html')



@app.route("/submit", methods = ['GET','POST'])
def submit():
    if request.method =='POST':    
        name = request.form['name']   
        return f"Hi {name}" 
    return render_template('form.html')



## 3. creating new dynamic url
@app.route("/success/<int:score>")
def success(score):
    res = " "
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('results.html',results = res)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/successif/<int:score>")
def successif(score):
    # Ensure score is an integer
    if not isinstance(score, int):
        return "Error: Score must be an integer", 400

    # Determine pass/fail status
    res = "PASSED" if score > 50 else "FAILED"

    # Pass results as a dictionary to the template
    results = {'score': int(score), 'res': res}
    return render_template('results1.html', results=results)

        

# by default, every function here has get method in it.
# there are four methods generally GET, POST, 

@app.route("/about")
def about():
    return render_template('about.html')
    



'''
if the below is executed. 
This will be the starting point of the execution as this acts as entry point.
Post run this script then rest of them will be executed
'''


if __name__ == "__main__":
    app.run(debug=True) # why debug is needed : if this input is not given, then the changes made after the server hosting wont be reflected. So, we need changes simultaneously as we modify in the script.
                # on switching on the debug option, the server automatically restarts and highlights the changes
