from flask import Blueprint, render_template, request
import requests
import json
from flask_paginate import Pagination, get_page_args

blueprint = Blueprint('cards', __name__)

# All cards
req = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
data = json.loads(req.content)

# single card for testing
# req = requests.get(
#     'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Tornado%20Dragon')

cards = list(data['data'])


def get_cards(offset=0, per_page=10):
    return cards[offset: offset + per_page]


@blueprint.get("/cards")
def list_cards():

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(cards)
    pagination_cards = get_cards(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template(
        'cards/cards-list.html',
        cards=pagination_cards,
        page=page,
        per_page=10,
        pagination=pagination,
    )


@blueprint.get("/decks")
def get_decks():
    return render_template(
        '/decks-list.html'
    )


@blueprint.get("/card/<id>")
def get_card(id):

    for datas in data['data']:
        name = datas['name']
        race = datas['race']
        # attribute = datas['attribute']
        # card_sets = datas['card_sets']
        desc = datas['desc']
        card_prices = datas['card_prices']

    return render_template(
        'cards/card.html',
        name=name,
        id=id,
        race=race,
        # attribute=attribute,
        # card_sets=card_sets,
        desc=desc,
        card_prices=card_prices
    )
