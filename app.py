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

  for i, item in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{i}">' + item["name"] + "</a></li>"
  html += "</ul>"

  return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]

  return f'''
  <h1>{pet["name"]}</h1>
  <img src="{pet["url"]}" />
  <p>{pet["description"]}</p>
  <ul>
    <li>Age: {pet["age"]}</li>
    <li>Breed: {pet["breed"]}</li>
  </ul>
  '''
