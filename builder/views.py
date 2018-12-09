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
    return render(request, 'builder.html', response)


def index(request):
    return render(request, 'index.html')

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
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()
    return render(request, 'add_card/to_existing.html', {'card_data':card_data['card']})


def create_deck(request, id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()
    return render(request, 'add_card/to_new.html', {'card_data':card_data['card']})

def create_deck_submit(request):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()
    c_id = request.POST['card_id']
    d_name = request.POST['deck_name']
    card = Card(id=c_id)
    card.save()
    deck = Deck(deck_name=d_name)
    deck.save()
    return redirect('deck')





