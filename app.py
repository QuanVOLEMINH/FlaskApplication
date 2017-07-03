from flask import Flask, render_template, request
from flask_github import GitHub

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '06078c9479f182a8f8a4'
app.config['GITHUB_CLIENT_SECRET'] = '06078c9479f182a8f8a4'
github = GitHub(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   return github.authorize()

@app.route('/callback')
def callback():
    return render_template('callback.html')



if __name__ == "__main__":
    app.run(debug=True)