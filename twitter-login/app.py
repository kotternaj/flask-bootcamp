from flask import Flask, render_template, session, redirect
from twitter_utils import get_request_token, get_oauth_verifier_url

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token
    # redirecting the user to Twitter so they can confirm authorization
    return redirect(get_oauth_verifier_url(request_token))

@app.route('/auth/twitter')
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile'))

app.run(port=5001, debug=True)


    