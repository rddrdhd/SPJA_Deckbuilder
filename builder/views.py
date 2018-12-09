from django.shortcuts import render, redirect
import requests
from .models import Deck, Card


def builder(request):
    """
    response = request.get('https://builder.magicthegathering.io/v1/cards')
    geodata = response.json()
    #card = Card.where(name='avacyn').all()
    """
    response = 'Hello'
    # c = Card(name=geodata['name'], cmc=geodata['cmc'], rarity=geodata['rarity'], text=geodata['text'])
    return render(request, 'builder.html', response)  # , {'card': c})


def index(request):
    return render(request, 'index.html')

# {% elif key == 'imageUrl' or key == 'originalText' or key == 'id' %}
# {% expr ['imageUrl', 'originalText', 'id'] as idontcare %}

def result(request):
    q = request.POST['q']
    response = requests.get('https://api.magicthegathering.io/v1/cards?name=%s' % q)

    cards_data = response.json()['cards']

    return render(request, 'search/result.html', {'q':q, 'cards_data':cards_data})


def detail(request, id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()
    url_img = 'http://gatherer.wizards.com/Handlers/Image.ashx?id=%s&type=card' % id
    return render(request, 'search/detail.html', {'card_data':card_data['card'], 'url_img':url_img})

def deck(request):
    return render(request, 'deck.html')

def search(request):
    return render(request, 'search/index.html')

def add_to_deck(request, id):
    return render(request, 'add_card/to_existing.html', {'card_id':id})


def create_deck(request, id):
    return render(request, 'add_card/to_new.html', {'card_id':id})

def create_deck_submit(request):
    card_id = request.POST['card_id']
    deck_name = request.POST['deck_name']
    deck = Deck()
    deck.deck_name = deck_name
    deck.save()
    return redirect('deck')





