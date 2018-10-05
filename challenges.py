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
    if request.method == 'GET':
        baseurl = "https://itunes.apple.com/search?"
        result = request.args
        params = {}
        params['term'] = result.get('artist')
        params['limit'] = result.get('num')
        resp = requests.get(baseurl, params = params)
        data = json.loads(resp.text)
        return render_template('list.html', results = data['results'])

    # params_diction = {}
    # params_diction["term"] = artist
    # resp = requests.get(baseurl, params=params_diction)
    # text = resp.text
    # python_obj = json.loads(text)
    # return str(python_obj)


if __name__ == '__main__':
    app.run(debug = True)
