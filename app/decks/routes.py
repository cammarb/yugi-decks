from flask import Flask, Blueprint, render_template, request
import requests
import json
from flask_paginate import Pagination, get_page_args

blueprint = Blueprint('decks', __name__)

req = requests.get('https://db.ygoprodeck.com/api/v7/cardsets.php')
data = json.loads(req.content)

decks = list(data)


def get_decks(offset=0, per_page=10):
    return decks[offset: offset + per_page]


@blueprint.get('/decks')
def list_decks():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(decks)
    pagination_decks = get_decks(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template(
        'decks/decks.html',
        decks=pagination_decks,
        page=page,
        per_page=10,
        pagination=pagination,
    )
