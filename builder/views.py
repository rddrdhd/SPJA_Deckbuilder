from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from django.urls import reverse

from .models import Deck, Card
from django.shortcuts import get_object_or_404

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
    card_data = gimme_card_data_by_id(id)
    url_img = 'http://gatherer.wizards.com/Handlers/Image.ashx?id=%s&type=card' % id
    return render(request, 'search/detail.html', {'card_data':card_data, 'url_img':url_img})

def decks(request):
    decks = Deck.objects.all()
    return render(request, 'decks.html', {'decks': decks})

def deck(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    return render(request, 'deck.html', {'deck': deck})

def search(request):
    return render(request, 'search/index.html')

def gimme_card_data_by_id(id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()
    return card_data['card']

def add_to_deck(request, card_id):
    #deck = Deck(deck_name='MahDeck')
    #deck.save()

    decks = Deck.objects.all()
    return render(request, 'add_card/to_existing.html', {'card_id':card_id, 'decks':decks})

def add_to_deck_submit(request, card_id):
    deck_id = request.POST['deck_id']

    deck = get_object_or_404(Deck, pk=deck_id)
    card_data = gimme_card_data_by_id(card_id)
    card = Card(name=card_data['name'], cmc=card_data['cmc'], rarity=card_data['rarity'], text=card_data['text'],
                imgUrl=card_data['imageUrl'])
    card.save()
    deck.cards.add(card)
    deck.save()

    return HttpResponseRedirect(reverse('builder:decks'))

def create_deck(request, card_id):
    return render(request, 'add_card/to_new.html', {'card_id': card_id})

def create_deck_submit(request, card_id):

    #c_id = request.POST['card_id']
    d_name = request.POST['deck_name']

    card_data = gimme_card_data_by_id(card_id)


    deck = Deck(deck_name=d_name)
    deck.save()

    card = Card(name=card_data['name'], cmc=card_data['cmc'], rarity=card_data['rarity'], text=card_data['text'],
                imgUrl=card_data['imageUrl'])
    card.save()

    deck.cards.add(card)
    return HttpResponseRedirect(reverse('builder:decks'))




