from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    deck_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_cards(self):
        return Card.objects.filter(deck=self)

    def __str__(self):
        return self.deck_name


class Card(models.Model):
    card_id = models.CharField(max_length=100)
    name = models.CharField(max_length=150)  # string
    cmc = models.IntegerField()  # int - converted mana cost
    rarity = models.CharField(max_length=20)  # string
    text = models.CharField(max_length=1000, null=True)  # string
    imgUrl = models.CharField(max_length=1000)

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, {%s}' % (self.name, self.cmc)
