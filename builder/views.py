from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from django.urls import reverse
from .models import Deck, Card
from django.shortcuts import get_object_or_404


# --------------------------------   MAH FUNCS

# Name says it all
def gimme_card_data_by_id(card_id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % card_id)
    card_data = response.json()
    return card_data['card'] #Bc its returning {"card":{...stuffiwant...}}


# from card_id it adds card into DB & returns card
def create_card_return(card_id):
    c_data = gimme_card_data_by_id(card_id)
    if 'text' in c_data:
        card = Card(card_id=c_data['id'], name=c_data['name'], cmc=c_data['cmc'], rarity=c_data['rarity'],
                    text=c_data['text'], imgUrl=c_data['imageUrl'])
    else:
        card = Card(card_id=c_data['id'], name=c_data['name'], cmc=c_data['cmc'], rarity=c_data['rarity'],
                    text=None, imgUrl=c_data['imageUrl'])

    card.save()
    return card


# --------------------------------   VIEWS
# TODO: Delete card from deck
# TODO: Delete deck and his cards (cascade?)
# TODO: Player (login, topic, OneToManyFiled  decks)
# Main page
def index(request):
    return render(request, 'index.html')


# Just leads to page with 'search card' field
def search(request):
    return render(request, 'search/index.html')


# Cards found by 'q'
def result(request):
    q = request.POST['q']
    response = requests.get('https://api.magicthegathering.io/v1/cards?name=%s' % q)
    c_data = response.json()['cards']
    return render(request, 'search/result.html', {'q': q, 'cards_data': c_data})


# Detail of card
def detail(request, card_id):
    c_data = gimme_card_data_by_id(card_id)
    img_url = 'http://gatherer.wizards.com/Handlers/Image.ashx?id=%s&type=card' % card_id
    return render(request, 'search/detail.html', {'card_data': c_data, 'url_img': img_url})


# All decks
def decks(request):
    ds = Deck.objects.all()
    return render(request, 'decks.html', {'decks': ds})


# Detail of deck
def deck(request, deck_id):
    d = Deck.objects.get(id=deck_id)
    return render(request, 'deck.html', {'deck': d})


# Leads to 'add card to existing deck' and sending card_id & all decks
def add_to_deck(request, card_id):
    decks = Deck.objects.all()
    return render(request, 'add_card/to_existing.html', {'card_id': card_id, 'decks': decks})


# Saving the deck from 'add card to existing deck'
def add_to_deck_submit(request, card_id):
    deck_id = request.POST['deck_id']

    d = get_object_or_404(Deck, pk=deck_id)
    card = create_card_return(card_id)
    d.cards.add(card)
    d.save()

    return HttpResponseRedirect(reverse('builder:decks'))


# Leads to 'add card to new deck' and sending card_id
def create_deck(request, card_id):
    return render(request, 'add_card/to_new.html', {'card_id': card_id})

# Saving the new deck from 'add card to new deck'
def create_deck_submit(request, card_id):
    d_name = request.POST['deck_name']
    card = create_card_return(card_id)
    d = Deck(deck_name=d_name)
    d.save()
    d.cards.add(card)
    return HttpResponseRedirect(reverse('builder:decks'))

def delete_card(request, id):
    #d = get_object_or_404(Deck, request.POST['deck_id'])
    #d.cards.objects.filter(card_id=id).delete()
    Card.objects.filter(id= id).delete()
    return HttpResponseRedirect(reverse('builder:deck'))

