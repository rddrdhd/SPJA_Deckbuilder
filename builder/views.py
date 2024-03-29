from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Deck, Card, Comment
import requests
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


# --------------------------------   MAH FUNCS

# Name says it all
def gimme_card_data_by_id(card_id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % card_id)
    card_data = response.json()
    return card_data['card']  # Bc its returning {"card":{...stuffiwant...}}


# from card_id it adds card into DB & returns card
def create_card_return(card_id, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    c_data = gimme_card_data_by_id(card_id)

    card = Card(card_id=c_data['id'], name=c_data['name'], colors=None,
                type=c_data['type'], cmc=c_data['cmc'], rarity=c_data['rarity'], text=None,
                flavor=None, artist=c_data['artist'], imgUrl=c_data['imageUrl'],
                number=None, deck=deck)
    if 'text' in c_data:
        card.text = c_data['text']
    if 'colors' in c_data:
        card.colors = c_data['colors']
    if 'flavor' in c_data:
        card.flavor = c_data['flavor']
    if 'manaCost' in c_data:
        card.manaCost = c_data['manaCost']
    if 'number' in c_data:
        card.number = c_data['number']

    card.save()
    return card


# --------------------------------  signup
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    # for all generic class-based views the urls are not loaded when the file is imported, so we have to use the lazy
    # form of reverse to load them later when they’re available
    template_name = 'registration/signup.html'


# --------------------------------   VIEWS
# Main page
def index(request):
    return render(request, 'index.html')


# def home(request):
#   return render(request, 'home.html')


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
    return render(request, 'deck/decks.html', {'decks': ds})


# Detail of deck
def deck(request, deck_id):
    d = Deck.objects.get(id=deck_id)
    c = d.get_cards()
    userid = None
    if request.user.is_authenticated:
        userid = request.user.id
    comments = Comment.objects.filter(to_deck=deck_id)
    return render(request, 'deck/deck.html', {'deck': d, 'cards': c, 'userid': userid, 'comments': comments})


# Leads to 'add card to existing deck' and sending card_id & all decks
def add_to_deck(request, card_id):
    decks = Deck.objects.all()
    userid = None
    if request.user.is_authenticated:
        userid = request.user.id
    return render(request, 'add_card/to_existing.html', {'card_id': card_id, 'decks': decks, 'userid': userid})


# Saving the deck from 'add card to existing deck'
def add_to_deck_submit(request, card_id):
    deck_id = request.POST['deck_id']

    d = get_object_or_404(Deck, pk=deck_id)
    create_card_return(card_id, deck_id)
    d.save()

    return HttpResponseRedirect(reverse('builder:decks'))


# Leads to 'add card to new deck' and sending card_id
def create_deck(request, card_id):
    players = User.objects.all()
    userid = None
    if request.user.is_authenticated:
        userid = request.user.id
    return render(request, 'add_card/to_new.html', {'card_id': card_id, 'players': players, 'userid': userid})


# Saving the new deck from 'add card to new deck'
def create_deck_submit(request, card_id):
    p_id = request.POST['player_id']
    p = get_object_or_404(User, pk=p_id)
    d_name = request.POST['deck_name']
    d = Deck(deck_name=d_name, owner=p)
    d.save()
    create_card_return(card_id, d.id)
    return HttpResponseRedirect(reverse('builder:decks'))


def delete_deck(request, id):
    Deck.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('builder:decks'))


def delete_card(request, id):
    Card.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('builder:decks'))


def players(request):
    players = User.objects.all()
    return render(request, 'player/players.html', {'players': players})


def player(request, player_id):
    player = User.objects.get(pk=player_id)

    decks = Deck.objects.filter(owner=player_id)
    userid = None
    if request.user.is_authenticated:
        userid = request.user.id
    return render(request, 'player/player.html', {'player': player, 'decks': decks, 'userid': userid})


def new_comment(request, deck_id):
    userid = None
    if request.user.is_authenticated:
        userid = request.user.id
    return render(request, 'comment/new_comment.html', {'userid':userid, 'deck_id':deck_id})


def new_comment_submit(request, deck_id):
    text = request.POST['text']
    title = request.POST['title']
    deck = get_object_or_404(Deck, pk=deck_id)
    user = None
    if request.user.is_authenticated:
        user = request.user
    comment = Comment(title=title, text=text, author=user, to_deck=deck)
    comment.save()
    return HttpResponseRedirect(reverse('builder:index'))
