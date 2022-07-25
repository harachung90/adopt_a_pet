from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <a href="/animals/dogs"><li>Dogs</li></a>
    <a href="/animals/cats"><li>Cats</li></a>
    <a href="/animals/rabbits"><li>Rabbits</li></a>
  </ul>
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>Lits of {pet_type}</h1><ul>"

  for pet in pets:
    html += "<li>pet[pet_type]</li>"
  html += "</ul>"

  return html
