from flask import Blueprint, redirect, url_for

main = Blueprint('main', 'api')

@main.route('/')
def index():
    return f'<h1>Index</h1>'

@main.route('/help')
def help():
    return f'<h1>Help</h1>'

@main.route('/req')
def help():
    return f'<h1>Request</h1>'