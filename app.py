from flask import Flask, render_template, request, redirect, session, url_for
from requests_oauthlib import OAuth2Session
from datamanagement import *
import os

#Ignore https for localhost
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)

# Information from github app
client_id = '06078c9479f182a8f8a4'
client_secret = '4342fac9ab22b88884381cc2b178e16196f4ec3d'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/login")
def login():
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


@app.route('/callback', methods=['GET'])
def callback():
    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)
    session['oauth_token'] = token
    return redirect(url_for('.profile'))


@app.route("/profile", methods=["GET"])
def profile():
    """Fetching a protected resource using an OAuth 2 token.
    """
    github = OAuth2Session(client_id, token=session['oauth_token'])
    users = github.get('https://api.github.com/user').json()
    repos = github.get(users['repos_url']).json()

    data_manage = DataManagement()

    list_repos = data_manage.get3most(data_manage.setformat(repos))
    return render_template('profile.html', users=users, list_repos=list_repos)

if __name__ == "__main__":
    os.environ['DEBUG'] = "1"
    app.secret_key = os.urandom(24)
    app.run(debug=True)
