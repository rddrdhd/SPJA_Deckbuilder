from django.shortcuts import render
import requests
from .models import Card, Deck, User


def builder(request):
    """
    response = request.get('https://builder.magicthegathering.io/v1/cards')
    geodata = response.json()
    #card = Card.where(name='avacyn').all()
    """
    response = requests.get('https://builder.magicthegathering.io/v1/cards/439390')
    geodata = response.json()

    # c = Card(name=geodata['name'], cmc=geodata['cmc'], rarity=geodata['rarity'], text=geodata['text'])
    return render(request, 'builder.html', {'x': geodata})  # , {'card': c})

    """
    return render(request, 'builder/builder.html', {
        'name': geodata['name'],
        'cmc': geodata['cmc'],
        'type': geodata['type'],
        'rarity': geodata['rarity'],
        'number': geodata['number'],
        'artist': geodata['artist'],
        'imageUrl': geodata['imageUrl'],
        #multiverseid -
    })
    """

# {% elif key == 'imageUrl' or key == 'originalText' or key == 'id' %}
# {% expr ['imageUrl', 'originalText', 'id'] as idontcare %}
def result(request):
    q = request.POST['q']
    response = requests.get('https://api.magicthegathering.io/v1/cards?name=%s' % q)

    cards_data = response.json()['cards']

    #c = Card(name=card_data.cards[0].name)

    return render(request, 'search/result.html', {'q':q, 'cards_data':cards_data})


def detail(request, id):
    response = requests.get('https://api.magicthegathering.io/v1/cards/%s' % id)
    card_data = response.json()#['cards']
    url_img = 'http://gatherer.wizards.com/Handlers/Image.ashx?id=%s&type=card' % id
    return render(request, 'search/detail.html', {'card_data':card_data['card'], 'url_img':url_img})


def search(request):
    return render(request, 'search/index.html')


def index(request):
    return "Hello world!"




