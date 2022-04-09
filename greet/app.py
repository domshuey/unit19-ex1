from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_msg():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home_msg():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back_msg():
    return 'welcome back'