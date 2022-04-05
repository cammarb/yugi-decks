from flask import Flask, render_template, requests
import json
app = Flask(__name__)

req = requests.get(
    'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Tornado%20Dragon')

# req = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')

data = json.loads(req.content)


@app.route("/")
def home():
    return render_template('/home.html')


@app.route("/cards", methods=['GET'])
def list_cards():
    # req = requests.get(
    #     'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Tornado%20Dragon')

    # # req = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')

    # data = json.loads(req.content)

    return render_template(
        '/cards-list.html',
        data=data
    )


@app.route("/decks")
def get_decks():
    return render_template(
        '/decks-list.html'
    )


@app.route("/card/<id>")
def get_card(id):
    for datas in data['data']:
        name = datas['name']
    return render_template(
        '/card.html',
        name=name,
        id=id
    )
