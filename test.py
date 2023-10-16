from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.output import put_markdown
from pywebio.input import input

from flask import Flask
app = Flask(__name__)

def welcome():
    put_markdown("## Welcome to PyWebIO Example")
    name = input("What's your name?", type="text")

def greet(name):
    put_markdown(f"Hello, {name}! Welcome to the PyWebIO example.")

if __name__ == '__main__':
    app.add_url_rule('/tool', 'webio_view', webio_view(welcome), methods=['GET', 'POST'])
    app.run(host='0.0.0.0',port=8082)
