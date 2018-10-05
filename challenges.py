from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

# Challenge 1: Return the 404.html template
# Edit it such that it displays an interesting message

@app.errorhandler(404)
def error404(e):
    return render_template('404.html')

@app.errorhandler(500)
def error500(e):
    return render_template('500.html')

# Challenge 3: Write an error handler for 500 error
## YOUR CODE HERE

# Challenge 4: Edit the 500.html template to display link to homepage and link to itunes-form.


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/itunes-form')
def ituneForm():
    return render_template('itunes-form.html')


@app.route('/itunes-result')
def resultTunes():
    pass


if __name__ == '__main__':
    app.run(debug = True)
