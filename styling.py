from flask import Flask, render_template

"""
render_template is a built-in function that knows how to handle requests and directs them into HTML files.
"""

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')  # Allows us to display the HTML file instead of some strings