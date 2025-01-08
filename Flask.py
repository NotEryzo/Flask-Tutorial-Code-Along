from flask import Flask

"""
An instance of the Flask class is created and assigned to the variable app.

The __name__ variable represents the current python file. It tells Flask where to look for resources like templates and static files.

Flask(__name__) helps to locate the application and set up paths for the project.

app is the Flask application object that handles incoming web requests and routes them to the appropriate code.
"""
app = Flask(__name__)

"""

@app.route('/') is a decorator, which is a Python feature that modifies the behavior of a function. 
In Flask, decorators are used to bind a URL to a specific function.

@app.route('/') binds the URL / (the root of the website) to the function below.

When the user accesses the / URL in a web broweser, the function below will run.    

"""
@app.route('/')
def hello_world():
    return '<h1> Hello World! </h1>'

# Can add parameters for specific routes.
@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username}</h1>'