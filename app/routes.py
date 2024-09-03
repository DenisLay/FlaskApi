from flask import Blueprint, redirect, url_for

main = Blueprint('main', 'api')

@main.route('/')
def index():
    return f'<h1>Index</h1>'